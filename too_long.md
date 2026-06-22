(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ # Read the core auth router to see routes and deps
docker exec jarvis-auth-api cat /app/services/auth_router.py

# Check what main.py is actually starting
docker exec jarvis-auth-api cat /app/services/main.py

# Check if seed_admin_user ran successfully (Neo4j users exist?)
docker exec jarvis-auth-api python3 /app/services/seed_admin_user.py --dry-run 2>&1 | head -30
from __future__ import annotations
import os, logging, uuid, secrets, hashlib, base64
from datetime import datetime, timezone
from typing import Annotated
import redis as redis_mod
from eth_account import Account
from cryptography.fernet import Fernet
from fastapi import APIRouter, HTTPException, Depends, Request, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from application_service import ApplicationService, InvalidApplicationError, CURRENT_AGREEMENT_VERSION
from registration_service import RegistrationService
from token_service import TokenService
from uei_service import UEIService
from email_service import send_approval_email

logger = logging.getLogger("auth_router")
auth_router = APIRouter(prefix="/auth", tags=["auth"])
_REDIS_URL = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")
_svc: dict = {}


def _get_fernet() -> Fernet:
    key = hashlib.sha256(
        os.getenv("WALLET_ENCRYPT_KEY", "changeme-set-WALLET_ENCRYPT_KEY-env").encode()
    ).digest()
    return Fernet(base64.urlsafe_b64encode(key))


def _get_services():
    if "reg" not in _svc:
        r = redis_mod.Redis.from_url(_REDIS_URL, decode_responses=True)
        uei = UEIService(r)
        app_svc = ApplicationService(r, uei)
        _svc["reg"] = RegistrationService(app_svc)
        _svc["tok"] = TokenService(r)
        _svc["r"] = r
    return _svc["reg"], _svc["tok"], _svc["r"]


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def _current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    _, tok, _ = _get_services()
    payload = tok.verify_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload


class RegistrationRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    email: str
    county: str = Field(..., min_length=2, max_length=60)
    motivation: str = Field(..., min_length=10, max_length=2000)
    agreement_accepted: bool
    agreement_version: str = CURRENT_AGREEMENT_VERSION
    address_street: str | None = None
    address_city: str | None = None
    address_state: str | None = None
    address_zip: str | None = None
    dl_image_b64: str | None = None
    selfie_b64: str | None = None
    bsc_status: str = "prefer_not_to_say"


class RegistrationResponse(BaseModel):
    application_id: str
    proposed_userid: str
    agreement_version: str
    message: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class RefreshRequest(BaseModel):
    refresh_token: str


class MeResponse(BaseModel):
    userid: str
    uei: str | None = None
    roles: list[str] = []
    county: str | None = None


@auth_router.post("/register", response_model=RegistrationResponse, status_code=201)
async def register(body: RegistrationRequest, request: Request):
    reg_svc, _, r = _get_services()
    ip = request.client.host if request.client else "unknown"
    try:
        result = reg_svc.submit_application(
            name=body.name,
            email=body.email,
            county=body.county,
            motivation=body.motivation,
            agreement_accepted=body.agreement_accepted,
            agreement_version=body.agreement_version,
            ip_address=ip,
        )
    except InvalidApplicationError as exc:
        raise HTTPException(status_code=422, detail=str(exc))

    # ── Bug 3: one account per human ─────────────────────────────────────
    if r.exists(f"email_to_uuid:{body.email}"):
        raise HTTPException(status_code=409, detail="An account with this email already exists.")
    public_uuid = str(uuid.uuid4())
    temp_password = secrets.token_urlsafe(12)
    wallet = Account.create(extra_entropy=secrets.token_hex(32))
    encrypted_pk = _get_fernet().encrypt(wallet.key.hex().encode()).decode()

    # ── Registration pipeline: DL OCR + UEID + immutable record ──────────────
    from registration_pipeline import run_registration_pipeline
    pipeline_ok, pipeline_msg, ueid = run_registration_pipeline(
        name=body.name,
        email=body.email,
        dl_image_b64=body.dl_image_b64,
        selfie_b64=body.selfie_b64,
        wallet_address=wallet.address,
        wallet_private_key_encrypted=encrypted_pk,
    )
    if not pipeline_ok:
        raise HTTPException(status_code=422, detail=pipeline_msg)
    # ─────────────────────────────────────────────────────────────────────────

    user_count = sum(1 for _ in r.scan_iter("user:*"))
    is_first_user = (user_count == 0)
    initial_roles  = "admin,user" if is_first_user else ""
    initial_status = "approved_pending_login" if is_first_user else "pending_first_login"

    r.hset(f"user:{public_uuid}", mapping={
        "public_uuid":        public_uuid,
        "proposed_userid":    result.proposed_userid,
        "email":              body.email,
        "name":               body.name,
        "county":             body.county,
        "userid":             result.proposed_userid,
        "temp_password":      temp_password,
        "status":             initial_status,
        "roles":              initial_roles,
        "created_at":         datetime.now(timezone.utc).isoformat(),
        "wallet_address":     wallet.address,
        "wallet_private_key": encrypted_pk,
        "ueid":               ueid,
        "bsc_status":         body.bsc_status,
    })

    if is_first_user:
        try:
            reg_svc._apps.mark_approved(
                application_id=result.application_id,
                approved_by="bootstrap",
                final_userid=result.proposed_userid,
            )
            logger.info(f"[AUTH] First user bootstrap: {public_uuid} auto-promoted to admin")
        except Exception as exc:
            logger.warning(f"[AUTH] First-user auto-approve failed: {exc}")
    r.set(f"email_to_uuid:{body.email}", public_uuid)
    r.set(f"wallet_to_uuid:{wallet.address}", public_uuid)
    logger.info(f"[AUTH] Registered {public_uuid} county={body.county} wallet={wallet.address}")
    # NOTE: No email sent here. Email fires only on admin approval.
    return RegistrationResponse(
        application_id=result.application_id,
        proposed_userid=result.proposed_userid,
        agreement_version=result.agreement_version,
        message=result.message,
    )



@auth_router.post("/logout", status_code=200)
async def logout(token: str = Depends(oauth2_scheme)):
    """Invalidate the bearer token server-side."""
    tok.revoke_token(token)
    return {"status": "logged_out"}


@auth_router.post("/login", response_model=TokenResponse)
async def login(form: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """Login accepts either email OR proposed_userid as the username field."""
    _, tok, _ = _get_services()
    result = tok.authenticate(form.username, form.password)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return TokenResponse(
        access_token=result["access_token"],
        expires_in=result["expires_in"],
    )

@auth_router.get("/me", response_model=MeResponse)
async def me(payload: Annotated[dict, Depends(_current_user)]):
    """Look up canonical user fields from Redis by proposed_userid."""
    _, _, r = _get_services()
    sub = payload.get("sub", "")
    user = None
    for key in r.scan_iter("user:*"):
        rec = r.hgetall(key)
        if rec.get("proposed_userid") == sub:
            user = rec
            break
    if not user:
        return MeResponse(
            userid=sub,
            uei=payload.get("uei"),
            roles=payload.get("roles", []),
            county=payload.get("county"),
        )
    roles = [rr for rr in user.get("roles", "user").split(",") if rr]
    return MeResponse(
        userid=sub,
        uei=user.get("ueid", ""),
        roles=roles,
        county=user.get("county", ""),
    )



# ── Admin: chat metrics ──────────────────────────────────────────────────────

@auth_router.get("/admin/chat-metrics")
async def admin_chat_metrics(payload: Annotated[dict, Depends(_current_user)]):
    if "admin" not in payload.get("roles", []):
        raise HTTPException(status_code=403, detail="Admin required")

    import json
    from pathlib import Path

    metrics_path = Path("/opt/msjarvis-rebuild/admin-data/chat_metrics_24h.json")
    if not metrics_path.exists():
        raise HTTPException(status_code=404, detail="chat metrics file not found")

    try:
        return json.loads(metrics_path.read_text())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"could not load chat metrics: {e}")


# ── Admin: list pending applications ─────────────────────────────────────────

@auth_router.get("/applications/pending")
async def list_pending(payload: Annotated[dict, Depends(_current_user)]):
    if "admin" not in payload.get("roles", []):
        raise HTTPException(status_code=403, detail="Admin required")
    reg_svc, _, _ = _get_services()
    apps = reg_svc._apps.list_pending()

    # Annotate each application with county champion warning
    import psycopg2 as _pg, os as _os
    _dsn = _os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL")
    champion_counties = {}
    if _dsn:
        try:
            _conn = _pg.connect(_dsn)
            _cur = _conn.cursor()
            # Get all UEIDs that have founder tokens
            _cur.execute("SELECT ueid FROM founder_tokens WHERE cohort = 'phase_0'")
            _token_ueids = [row[0] for row in _cur.fetchall()]
            _conn.close()
            # Resolve UEID -> county via Redis
            _, _, r2 = _get_services()
            for _key in r2.scan_iter("user:*"):
                _rec = r2.hgetall(_key)
                if _rec.get("ueid") in _token_ueids:
                    _county = _rec.get("county", "").strip()
                    _userid = _rec.get("proposed_userid", _rec.get("public_uuid", "unknown"))
                    if _county:
                        champion_counties[_county.lower()] = _userid
        except Exception as _e:
            logger.warning(f"[ADMIN] County annotation failed (non-fatal): {_e}")

    for app in apps:
        app_county = (app.get("county") or "").strip().lower()
        if app_county and app_county in champion_counties:
            app["county_warning"] = f"⚠ {app.get('county')} already has a Champion ({champion_counties[app_county]})"
        else:
            app["county_warning"] = None

    return {"applications": apps, "count": len(apps)}

# ── Admin: approve application ────────────────────────────────────────────────

class ApproveResponse(BaseModel):
    application_id: str
    public_uuid:    str
    email:          str
    message:        str


@auth_router.post("/approve/{application_id}", response_model=ApproveResponse)
async def approve_application(
    application_id: str,
    payload: Annotated[dict, Depends(_current_user)],
):
    """Approve a pending application. Sends temp-password email. Admin only."""
    if "admin" not in payload.get("roles", []):
        raise HTTPException(status_code=403, detail="Admin required")

    reg_svc, tok, r = _get_services()
    app_svc = reg_svc._apps

    try:
        app = app_svc.get_application(application_id)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Application {application_id} not found")

    email = app.get("email", "")
    if not email:
        raise HTTPException(status_code=422, detail="Application has no email address")

    public_uuid = r.get(f"email_to_uuid:{email}")
    if not public_uuid:
        import secrets as _sec
        public_uuid   = str(__import__("uuid").uuid4())
        temp_pw       = _sec.token_urlsafe(16)
        proposed_userid = app.get("proposed_userid", public_uuid)
        r.set(f"email_to_uuid:{email}", public_uuid)
        r.hset(f"user:{public_uuid}", mapping={
            "email":           email,
            "name":            app.get("name", ""),
            "proposed_userid": proposed_userid,
            "temp_password":   temp_pw,
            "status":          "approved_pending_login",
            "created_at":      __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
        })

    user = r.hgetall(f"user:{public_uuid}")
    if not user:
        raise HTTPException(status_code=404, detail=f"User hash missing for {public_uuid}")

    proposed_userid = user.get("proposed_userid", public_uuid)

    app_svc.mark_approved(
        application_id=application_id,
        approved_by=payload.get("sub", "admin"),
        final_userid=proposed_userid,
    )

    r.hset(f"user:{public_uuid}", mapping={
        "status":      "approved_pending_login",
        "approved_at": datetime.now(timezone.utc).isoformat(),
        "approved_by": payload.get("sub", "admin"),
    })
    r.setex(f"temp_pw_expires:{public_uuid}", 72 * 3600, "1")

    # ── Auto-mint founder token + zero balances on approval ──────────────────
    try:
        import psycopg2 as _pg, os as _os
        _dsn = _os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL")
        _ueid = r.hget(f"user:{public_uuid}", "ueid")
        if _dsn and _ueid:
            _conn = _pg.connect(_dsn)
            _cur = _conn.cursor()
            _cur.execute("INSERT INTO mountainshares_balances (ueid) VALUES (%s) ON CONFLICT DO NOTHING", (_ueid,))
            _cur.execute("SELECT COALESCE(MAX(serial_number), 0) FROM founder_tokens")
            _next = _cur.fetchone()[0] + 1
            if _next <= 60:
                _alloc = "red_team" if _next <= 5 else "county_champion"
                _cur.execute(
                    "INSERT INTO founder_tokens (serial_number, ueid, minted_by, cohort, allocation_type) "
                    "VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING",
                    (_next, _ueid, payload.get("sub", "admin"), "phase_0", _alloc)
                )
                logger.info(f"[FOUNDER] Minted token #{_next} ({_alloc}) for {_ueid}")
                # Write founding grant ledger entry for red_team members
                if _alloc == "red_team":
                    _cur.execute("SELECT COUNT(*) FROM mountainshares_ledger WHERE ueid = %s AND transaction_type = 'founding_grant'", (_ueid,))
                    if _cur.fetchone()[0] == 0:
                     _cur.execute(
                        "INSERT INTO mountainshares_ledger "
                        "(ueid, transaction_type, amount, token_class, reason, reference_id, created_by) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (_ueid, "founding_grant", 100.0000, "EMS",
                         "Phase 0 red_team founding allocation",
                         f"PHASE0_RED_TEAM_GRANT_{str(_next).zfill(3)}",
                         payload.get("sub", "admin"))
                    )
                    _cur.execute(
                        "UPDATE mountainshares_balances SET ems_balance = ems_balance + 100.0000, "
                        "last_updated = NOW() WHERE ueid = %s",
                        (_ueid,)
                    )
                    logger.info(f"[FOUNDER] EMS founding grant written for {_ueid}")
            else:
                logger.info(f"[FOUNDER] Phase 0 cap (60) reached — no token minted for {_ueid}")
            _conn.commit()
            _conn.close()
    except Exception as _e:
        logger.warning(f"[FOUNDER] Auto-mint failed (non-fatal): {_e}")

    temp_password = user.get("temp_password", "")
    name          = user.get("name", email)
    if not temp_password:
        return ApproveResponse(
            application_id=application_id,
            public_uuid=public_uuid,
            email=email,
            message="User has already completed onboarding. No email sent.",
        )
    email_sent = False
    email_error = ""
    try:
        email_sent = send_approval_email(
            to=email,
            name=name,
            userid=proposed_userid,
            temp_password=temp_password,
        )
        if email_sent:
            logger.info(f"[AUTH] Approval email sent to {email} ({public_uuid})")
        else:
            email_error = "mailer returned false"
            logger.warning(f"[AUTH] Approval email not confirmed for {email} ({public_uuid})")
    except Exception as exc:
        email_error = str(exc)
        logger.warning(f"[AUTH] Approval email failed: {exc}")

    return ApproveResponse(
        application_id=application_id,
        public_uuid=public_uuid,
        email=email,
        message=(f"Approved. Temp-password email dispatched to {email}."
                 if email_sent else
                 f"Approved, but email delivery failed: {email_error}"),
    )


# ── Admin: deny application ───────────────────────────────────────────────────

class DenyRequest(BaseModel):
    reason: str = Field(..., min_length=5, max_length=500)


@auth_router.post("/deny/{application_id}")
async def deny_application(
    application_id: str,
    body: DenyRequest,
    payload: Annotated[dict, Depends(_current_user)],
):
    """Deny a pending application. Admin only."""
    if "admin" not in payload.get("roles", []):
        raise HTTPException(status_code=403, detail="Admin required")

    reg_svc, _, r = _get_services()
    app_svc = reg_svc._apps

    try:
        app = app_svc.get_application(application_id)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Application {application_id} not found")

    app_svc.mark_denied(
        application_id=application_id,
        denied_by=payload.get("sub", "admin"),
        reason=body.reason,
    )

    email = app.get("email", "")
    public_uuid = r.get(f"email_to_uuid:{email}") if email else None
    if public_uuid:
        r.hset(f"user:{public_uuid}", mapping={
            "status":    "denied",
            "denied_at": datetime.now(timezone.utc).isoformat(),
            "denied_by": payload.get("sub", "admin"),
        })

    logger.info(f"[AUTH] Application {application_id} denied — {body.reason}")
    return {"application_id": application_id, "status": "denied", "reason": body.reason}


# ── First login: exchange temp password for real password ─────────────────────

class FirstLoginRequest(BaseModel):
    email:         str
    temp_password: str
    new_password:  str = Field(..., min_length=10, max_length=128)


class FirstLoginResponse(BaseModel):
    access_token:   str
    token_type:     str = "bearer"
    public_uuid:    str
    wallet_address: str


@auth_router.post("/first-login", response_model=FirstLoginResponse)
async def first_login(body: FirstLoginRequest):
    """Exchange temp password for a real password. Sets status → active."""
    import bcrypt
    _, tok, r = _get_services()

    public_uuid = r.get(f"email_to_uuid:{body.email}")
    if not public_uuid:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user = r.hgetall(f"user:{public_uuid}")
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    status = user.get("status", "")
    if status not in ("approved_pending_login", "pending_first_login"):
        raise HTTPException(status_code=403, detail=f"Account not eligible for first login (status={status})")

    if not r.exists(f"temp_pw_expires:{public_uuid}"):
        raise HTTPException(status_code=401, detail="Temporary password expired")
    if not secrets.compare_digest(user.get("temp_password", ""), body.temp_password):
        r.delete(f"temp_pw_expires:{public_uuid}")
        raise HTTPException(status_code=401, detail="Invalid credentials")
    r.delete(f"temp_pw_expires:{public_uuid}")

    pw_hash = bcrypt.hashpw(body.new_password.encode(), bcrypt.gensalt()).decode()
    proposed_userid = user.get("proposed_userid", public_uuid)

    r.hset(f"user:{public_uuid}", mapping={
        "status":         "active",
        "password_hash":  pw_hash,
        "roles":          "user",
        "temp_password":  "",
        "first_login_at": datetime.now(timezone.utc).isoformat(),
        "userid":         proposed_userid,
    })
    # OI-profile-1: userid reverse-lookup for O(1) profile enrichment
    r.set(f"userid:{proposed_userid}", f"user:{public_uuid}")

    token = tok.issue_token(userid=proposed_userid, label="first-login", role="user")
    logger.info(f"[AUTH] First login complete for {public_uuid} ({proposed_userid})")

    return FirstLoginResponse(
        access_token=token,
        public_uuid=public_uuid,
        wallet_address=user.get("wallet_address", ""),
    )


# Portal: own balance + founder token
@auth_router.get("/portal/me/balances")
async def get_my_balances(payload: Annotated[dict, Depends(_current_user)]):
    import psycopg2, os as _os
    sub = payload.get("sub")
    if not sub:
        raise HTTPException(status_code=401, detail="Invalid token")
    _, _, r = _get_services()
    # sub is proposed_userid (e.g. "carrie_kidd") — must scan for the right user: key
    ueid = None
    for _key in r.scan_iter("user:*"):
        _rec = r.hgetall(_key)
        if _rec.get("proposed_userid") == sub or _rec.get("userid") == sub:
            _ueid = _rec.get("ueid") or _rec.get("uei")
            if _ueid:
                ueid = _ueid
                break
    if not ueid:
        raise HTTPException(status_code=404, detail="UEID not found")
    pg_dsn = _os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL")
    if not pg_dsn:
        raise HTTPException(status_code=503, detail="Database not configured")
    try:
        conn = psycopg2.connect(pg_dsn)
        cur = conn.cursor()
        cur.execute("SELECT ems_balance, rank, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
        bal = cur.fetchone()
        cur.execute("SELECT serial_number, minted_at, cohort, allocation_type FROM founder_tokens WHERE ueid = %s", (ueid,))
        ft = cur.fetchone()
        cur.execute("SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s AND ueid IN (%s, %s)", (sub, sub, f"UEID-{sub.upper()}-ADMIN"))
        session_ems = float(cur.fetchone()[0])
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"DB error: {e}")
    founder_token = None
    if ft:
        founder_token = {"serial_number": ft[0], "display": f"Founder #{str(ft[0]).zfill(3)}", "minted_at": ft[1].isoformat() if ft[1] else None, "cohort": ft[2], "allocation_type": ft[3]}
    total_ems = (float(bal[0]) if bal else 0.0)
    return {"ueid": ueid, "ems_balance": (float(bal[0]) if bal else 0.0) + session_ems, "rank": bal[1] if bal else "newcomer", "balance_last_updated": bal[2].isoformat() if bal and bal[2] else None, "founder_token": founder_token}


# ── Portal: ledger history ────────────────────────────────────────────────────

@auth_router.get("/portal/me/ledger")
async def get_my_ledger(
    payload: Annotated[dict, Depends(_current_user)],
    limit: int = 50,
    offset: int = 0,
    date_from: str = None,
    date_to: str = None,
    q: str = None,
    format: str = None,
):
    """Return paginated ledger history for the authenticated user."""
    import psycopg2 as _pg, os as _os
    sub = payload.get("sub", "")
    _, _, r = _get_services()
    ueid = None
    for _key in r.scan_iter("user:*"):
        _rec = r.hgetall(_key)
        if _rec.get("proposed_userid") == sub or _rec.get("userid") == sub:
            _ueid = _rec.get("ueid") or _rec.get("uei")
            if _ueid:
                ueid = _ueid
                break
    if not ueid:
        raise HTTPException(status_code=404, detail="UEID not found")
    _dsn = (_os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL", ""))
    if not _dsn:
        raise HTTPException(status_code=500, detail="DB not configured")
    try:
        _conn = _pg.connect(_dsn)
        _cur = _conn.cursor()
        filters = [ueid]
        where = "WHERE ueid = %s"
        if date_from:
            where += " AND created_at >= %s"
            filters.append(date_from)
        if date_to:
            where += " AND created_at <= %s"
            filters.append(date_to + " 23:59:59")
        if q:
            where += " AND (transaction_type ILIKE %s OR reason ILIKE %s)"
            filters.extend([f"%{q}%", f"%{q}%"])
        _cur.execute(
            "SELECT id, transaction_type, amount, token_class, reason, "
            "reference_id, created_at, created_by "
            "FROM mountainshares_ledger " + where +
            " ORDER BY created_at DESC LIMIT %s OFFSET %s",
            filters + [min(limit, 100), offset]
        )
        rows = _cur.fetchall()
        _cur.execute(
            "SELECT COUNT(*) FROM mountainshares_ledger " + where,
            filters
        )
        total = _cur.fetchone()[0]
        _conn.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail="DB error: " + str(e))
    entries = [
        {
            "id":               row[0],
            "transaction_type": row[1],
            "amount":           str(row[2]),
            "token_class":      row[3],
            "reason":           row[4],
            "reference_id":     row[5],
            "created_at":       row[6].isoformat() if row[6] else None,
            "created_by":       row[7],
        }
        for row in rows
    ]
    if format == "print":
        from fastapi.responses import HTMLResponse
        dr = ""
        if date_from or date_to:
            dr = f" | {date_from or '...'} → {date_to or '...'}"
        if q:
            dr += f" | search: {q}"
        rows_html = "".join(
            f"<tr><td>{e['created_at'][:10] if e['created_at'] else ''}</td>"
            f"<td>{e['transaction_type']}</td><td>{e['token_class']}</td>"
            f"<td style='text-align:right'>{float(e['amount']):,.4f}</td>"
            f"<td>{e['reason'] or ''}</td><td>{e['reference_id'] or ''}</td></tr>"
            for e in entries
        )
        total_amt = sum(float(e["amount"]) for e in entries)
        html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<title>MS Jarvis Ledger</title>
<style>
  body{{font-family:monospace;font-size:12px;margin:32px;color:#111}}
  h2{{margin-bottom:4px}} p{{margin:2px 0;color:#555}}
  table{{width:100%;border-collapse:collapse;margin-top:16px}}
  th{{background:#111;color:#fff;padding:6px 8px;text-align:left}}
  td{{padding:5px 8px;border-bottom:1px solid #ddd}}
  tr:nth-child(even){{background:#f7f7f7}}
  .total{{text-align:right;font-weight:bold;margin-top:8px}}
  @media print{{body{{margin:16px}}}}
</style></head><body>
<h2>MountainShares Ledger — MS Jarvis</h2>
<p>UEID: {ueid}{dr}</p>
<p>Entries: {total} | Shown: {len(entries)}</p>
<table><thead><tr>
  <th>Date</th><th>Type</th><th>Class</th>
  <th style="text-align:right">Amount</th><th>Reason</th><th>Reference</th>
</tr></thead><tbody>{rows_html}</tbody></table>
<p class="total">Total: {total_amt:,.4f} EMS</p>
<p style="margin-top:24px;color:#aaa;font-size:10px">
  Printed {__import__('datetime').datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}
</p>
<script>window.print()</script>
</body></html>"""
        return HTMLResponse(content=html)
    return {
        "ueid":    ueid,
        "total":   total,
        "limit":   limit,
        "offset":  offset,
        "entries": entries,
    }
    return {"ueid": ueid, "ems_balance": str(bal[0]) if bal else "0.0000", "pms_balance": str(bal[1]) if bal else "0.0000", "balance_last_updated": bal[2].isoformat() if bal and bal[2] else None, "founder_token": founder_token}


@auth_router.get("/portal/me/timesheet")
async def get_my_timesheet(
    payload: Annotated[dict, Depends(_current_user)],
    limit: int = 20,
):
    import psycopg2, os as _os
    sub = payload.get("sub", "")
    user_id = sub
    # Timesheet activity lives under the portal userid and its admin UEID variant.
    # Do not bind this endpoint to the founding-grant UEID from Redis.
    ueid = user_id
    pg_dsn = _os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL")
    if not pg_dsn:
        raise HTTPException(500, "Database not configured")
    try:
        conn = psycopg2.connect(pg_dsn)
        cur = conn.cursor()
        cur.execute("""
            SELECT jobid, started_at, completed_at,
                   duration_sec, ems_earned, status
            FROM equity_timesheet
            WHERE user_id = %s
              AND ueid IN (%s, %s)
              AND status IN ('complete', 'completed')
            ORDER BY started_at DESC LIMIT %s
        """, (user_id, user_id, f"UEID-{user_id.upper()}-ADMIN", limit))
        rows = cur.fetchall()
        cur.execute("""
            SELECT COALESCE(SUM(ems_earned), 0), COUNT(*), COALESCE(SUM(duration_sec), 0)
            FROM equity_timesheet
            WHERE user_id = %s
              AND ueid IN (%s, %s)
              AND status IN ('complete', 'completed')
        """, (sub, sub, f"UEID-{sub.upper()}-ADMIN"))
        totals = cur.fetchone()
        conn.close()
        return {
            "ueid": ueid,
            "total_ems_earned": float(totals[0]),
            "total_sessions": int(totals[1]),
            "total_hours": round(float(totals[2]) / 3600, 2),
            "entries": [
                {
                    "jobid": r[0],
                    "started_at": r[1].isoformat() if r[1] else None,
                    "completed_at": r[2].isoformat() if r[2] else None,
                    "duration_sec": float(r[3]) if r[3] else 0.0,
                    "ems_earned": float(r[4]) if r[4] else 0.0,
                    "status": r[5],
                }
                for r in rows
            ],
        }
    except Exception as e:
        raise HTTPException(500, f"Timesheet query failed: {e}")
"""Ms. Allis ULTIMATE - All 32 Services Integrated
Port: 8050 (Ultimate Interface)
"""

from fastapi.middleware.cors import CORSMiddleware
from provenance_middleware import ProvenanceMiddleware
import asyncio
import httpx
from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, List
import time
import logging
import os
import uuid
from datetime import datetime
import sys
from pathlib import Path
sys.path.extend([str(p) for p in Path("/app/dgms").glob("*/")])

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
active_jobs: Dict[str, Dict] = {}


class ChatJobRequest(BaseModel):
    message: str
    user_id: str = "cakidd"


class JobStatus(BaseModel):
    job_id: str
    status: str
    progress: Optional[str] = None
    result: Optional[Dict] = None
    error: Optional[str] = None
    created_at: float


class UltimateRequest(BaseModel):
    message: str
    user_id: str = "cakidd"
    use_all_services: bool = True


class UltimateResponse(BaseModel):
    response: str
    services_used: List[str]
    consciousness_level: str
    processing_time: float
    architecture_layers: int


def get_service_operation_path(service_name: str) -> str:
    """Get the primary operation path for each service."""
    endpoints = {
        "qualia_engine": "/generate",
        "consciousness_bridge": "/chat",
        "blood_brain_barrier": "/filter",
        "i_containers": "/process",
        "woah_algorithms": "/wonder",
        "toroidal": "/process",
        "fractal": "/process",
        "autonomous_learner": "/learn",
        "unified_gateway": "/chat",
        "mother_protocols": "/guidance",
        "temporal_consciousness": "/temporal_analysis",
        "neurobiological_master": "/neural_process",
        "darwin_godel_machine": "/verify",
        "agents_service": "/query/enhance",
        "swarm_intelligence": "/swarm_process",
        "brain_orchestrator": "/coordinate",
        "fifth_dgm": "/analyze",
        "rag_server": "/search",
        "web_research": "/search",
        "llm_bridge": "/process",
    }
    return endpoints.get(service_name, "/")


def get_service_endpoint(service_name: str, operation: str = "process") -> str:
    """Backwards-compatible alias; used by query_service."""
    return get_service_operation_path(service_name)


app = FastAPI(title="Ms. Allis ULTIMATE", version="1.0.0")
app.add_middleware(ProvenanceMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "main_brain"}


@app.post("/chat/async")
async def create_chat_job(request: ChatJobRequest):
    message = request.message
    user_id = request.user_id

    job_id = str(uuid.uuid4())
    active_jobs[job_id] = {
        "status": "processing",
        "progress": "Initializing consciousness layers...",
        "created_at": time.time(),
        "message": message,
        "user_id": user_id,
    }

    asyncio.create_task(process_chat_job(job_id, request))
    logger.info(f"📋 Created job {job_id[:8]} for: {message[:50]}")

    return {"job_id": job_id, "status": "processing"}


@app.get("/chat/status/{job_id}")
async def get_job_status(job_id: str):
    if job_id not in active_jobs:
        raise HTTPException(status_code=404, detail="Job not found")

    job = active_jobs[job_id]

    if job["status"] in ["complete", "error"]:
        age = time.time() - job.get("created_at", 0)
        if age > 300:
            del active_jobs[job_id]
            raise HTTPException(status_code=404, detail="Job expired")

    return {
        "job_id": job_id,
        "status": job["status"],
        "progress": job.get("progress"),
        "result": job.get("result"),
        "error": job.get("error"),
    }


async def process_chat_job(job_id: str, request: ChatJobRequest):
    message = request.message
    user_id = request.user_id

    try:
        active_jobs[job_id]["progress"] = "Phase 1: Checking service availability..."

        ultimate_request = UltimateRequest(
            message=message,
            user_id=user_id,
            use_all_services=True,
        )

        from fastapi import BackgroundTasks
        background_tasks = BackgroundTasks()

        active_jobs[job_id]["progress"] = "Phase 2: Processing through consciousness layers..."

        result = await ultimate_chat(ultimate_request, background_tasks)

        if hasattr(result, "dict"):
            result = result.dict()

        active_jobs[job_id]["status"] = "complete"
        active_jobs[job_id]["progress"] = "Complete!"
        active_jobs[job_id]["result"] = result

        logger.info(
            f"✅ Job {job_id[:8]} complete in "
            f"{time.time() - active_jobs[job_id]['created_at']:.1f}s"
        )
    except Exception as e:
        logger.error(f"❌ Job {job_id[:8]} failed: {e}")
        active_jobs[job_id]["status"] = "error"
        active_jobs[job_id]["error"] = str(e)


async def background_rag_store(message: str, response_text: str, services: list):
    """Store in RAG as background task - doesn't block response"""
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(connect=2.0, read=None, write=None, pool=3.0)) as client:
            check = await client.post(
                "http://jarvis-rag-server:8003/search",
                json={"query": message, "top_k": 1},
            )

            if check.status_code == 200:
                data = check.json()
                if data.get("count", 0) > 0 and data["results"][0]["score"] < 0.8:
                    logger.info(
                        f"⏭️  Skip duplicate: {message[:40]}... "
                        f"(score: {data['results'][0]['score']:.2f})"
                    )
                    return

            await client.post(
                "http://jarvis-rag-server:8003/store",
                json={
                    "user_id": "auto_system",
                    "query": message[:500],
                    "response": response_text[:1000],
                    "timestamp": datetime.utcnow().isoformat(),
                    "metadata": {
                        "type": "auto_stored",
                        "services": ",".join(services[:5]),
                        "auto": True,
                        "deduplicated": True,
                    },
                },
            )
            logger.info(f"📝 Auto-stored: {message[:40]}...")
    except Exception as e:
        logger.debug(f"Background storage: {e}")


def clean_response_for_display(raw_response):
    """Remove RAG metadata from responses"""
    if not raw_response or not isinstance(raw_response, str):
        return raw_response
    import re

    clean = re.sub(
        r"\*\*From Knowledge Base:\*\*[\s\S]*?(?=\*\*Multi-Agent|$)",
        "",
        raw_response,
    )
    clean = re.sub(
        r"•\s*USER:[\s\S]*?EGERIA:[\s\S]*?(?=•|\*\*Multi-Agent|$)",
        "",
        clean,
    )
    match = re.search(
        r"\*\*Multi-Agent Analysis:\*\*([\ s\S]*?)(?=---|$)",
        clean,
    )
    if match:
        response = match.group(1)
        response = re.sub(
            r"(Logical Analyst|Creative Synthesizer|Critical Evaluator|Empathetic Advisor):\s*",
            "",
            response,
        )
        return response.strip()
    return clean.strip() or raw_response


SERVICES: Dict[str, str] = {
    "qualia_engine": "http://jarvis-qualia-engine:8017",
    "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
    "blood_brain_barrier": "http://jarvis-blood-brain-barrier:8018",
    "neurobiological_master": "http://jarvis-neurobiological-master:8018",
    "i_containers": "http://jarvis-i-containers:8011",
    "autonomous_learner": "http://jarvis-autonomous-learner:8018",
    "woah_algorithms": "http://jarvis-woah:7012",
    "toroidal": "http://jarvis-toroidal:8025",
    "fractal": "http://jarvis-fractal-consciousness:8027",
    "mother_protocols": "http://jarvis-mother-protocols:4000",
    "temporal_consciousness": "http://jarvis-temporal-consciousness:4000",
    "unified_gateway": "http://jarvis-unified-gateway:8001",
    "ollama": "http://jarvis-ollama:11434",
    "chroma": "http://jarvis-chroma:8000",
    "redis": "http://jarvis-redis:6379",
    "brain_orchestrator": "http://jarvis-brain-orchestrator:4001",
    "fifth_dgm": "http://jarvis-fifth-dgm:8018",
    "swarm_intelligence": "http://jarvis-swarm-intelligence:8021",
    "rag_server": "http://jarvis-rag-server:8003",
    "agents_service": "http://jarvis-agents-service:8005",
    "llm_bridge": "http://jarvis-llm-bridge:8006",
    "web_research": "http://jarvis-web-research:8018",
    "main_brain": "http://jarvis-main-brain:8050",
    "wv_entangled": "http://jarvis-wv-entangled-gateway:8010",
}


async def check_service_health(service_name: str, url: str) -> bool:
    """
    Health: prefer /health when available; otherwise fall back to the
    service's primary operation endpoint and then root.
    """
    try:
        # Special cases
        if service_name == "ollama":
            async with httpx.AsyncClient(timeout=5.0) as client:
                resp = await client.get(f"{url}/api/tags")
                return 200 <= resp.status_code < 400
        if service_name in ("chroma", "redis"):
            return True

        async with httpx.AsyncClient(timeout=5.0) as client:
            # 1) Try explicit /health (llm_bridge, shared services, etc.)
            try:
                resp_health = await client.get(f"{url}/health")
                if 200 <= resp_health.status_code < 400:
                    return True
            except httpx.RequestError:
                pass

            # 2) Fall back to primary operation path
            op_path = get_service_operation_path(service_name)
            try:
                resp_op = await client.get(f"{url}{op_path}")
                if 200 <= resp_op.status_code < 400:
                    return True
            except httpx.RequestError:
                pass

            # 3) Final fallback: root
            try:
                resp_root = await client.get(url)
                if 200 <= resp_root.status_code < 400:
                    return True
            except httpx.RequestError:
                pass

        return False

    except Exception as e:
        logger.debug(f"Health check failed for {service_name} at {url}: {e}")
        return False


async def query_service(
    service_name: str,
    url: str,
    message: str,
    user_id: str,
) -> Optional[Dict]:
    try:
        request_formats = {
            "rag_server": {"query": message},
            "web_research": {"query": message},
            "agents_service": {"query": message, "user_id": user_id},
            "brain_orchestrator": {"query": message, "context": {}},
            "fifth_dgm": {"input": message, "verify": True},
            "swarm_intelligence": {"query": message},
            "consciousness_bridge": {"message": message, "user_id": user_id},
            "qualia_engine": {"input": message, "generate_qualia": True},
            "fractal": {"message": message, "depth": 3},
            "mother_protocols": {"message": message, "context": {}},
            "temporal_consciousness": {"message": message},
            "toroidal": {"message": message},
            "neurobiological_master": {"input": message, "process": True},
            "woah_algorithms": {"message": message, "generate_insight": True},
            "i_containers": {"message": message, "dual_mode": True},
            "darwin_godel_machine": {"statement": message, "verify": True},
            "blood_brain_barrier": {"message": message, "filter": True},
            "wv_entangled": {"message": message, "user_id": user_id},
        }

        request_data = request_formats.get(
            service_name,
            {"message": message, "user_id": user_id},
        )

        full_url = f"{url}{get_service_endpoint(service_name)}"
        logger.info(f"ULTIMATE fan-out: calling {service_name} at {full_url}")
        async with httpx.AsyncClient(timeout=httpx.Timeout(connect=2.0, read=None, write=None, pool=3.0)) as client:
            response = await client.post(
                full_url,
                json=request_data,
            )
            logger.info(f"{service_name} raw status={response.status_code} body={response.text[:200]}")
            if response.status_code == 200:
                result = response.json()
                logger.info(f"✅ {service_name}: Responded")
                response_text = (
                    result.get("response")
                    or result.get("result")
                    or result.get("output")
                    or result.get("answer")
                    or str(result)
                )
                return {
                    "service": service_name,
                    "response": response_text,
                    "status": "success",
                }
    except Exception as e:
        logger.warning(f"⚠️  {service_name}: {str(e)[:80]}")
        return None


def log_response_summary(responses: List[Dict]) -> None:
    if not responses:
        logger.info("No services returned responses in this job.")
        return
    used = [r.get("service", "<unknown>") for r in responses]
    logger.info(f"Services that returned responses: {', '.join(used)}")


@app.post("/chat", response_model=UltimateResponse)
async def ultimate_chat(request: UltimateRequest, background_tasks: BackgroundTasks):
    message = request.message
    user_id = request.user_id

    start_time = time.time()

    logger.info(f"\n{'=' * 60}")
    logger.info("🌟 ULTIMATE MS. JARVIS REQUEST")
    logger.info(f"   Message: {message[:200]}")
    logger.info(f"{'=' * 60}\n")

    services_used: List[str] = []
    responses: List[Dict] = []

    logger.info("Phase 1: Checking service availability...")
    logger.info(f"Service registry: {list(SERVICES.keys())}")
    available_services: Dict[str, str] = {}
    health_results = await asyncio.gather(
        *[check_service_health(name, url) for name, url in SERVICES.items()],
        return_exceptions=True
    )
    for (service_name, url), ok in zip(SERVICES.items(), health_results):
        if ok is True:
            available_services[service_name] = url
            logger.info(f"  ✅ {service_name}")
        else:
            logger.debug(f"  ⏸️  {service_name} offline")

    logger.info(f"\n✅ {len(available_services)}/{len(SERVICES)} services available\n")

    logger.info("Phase 1.4: Filtering through Blood-Brain Barrier...")
    filtered_query = message
    if "blood_brain_barrier" in available_services:
        try:
            async with httpx.AsyncClient(timeout=httpx.Timeout(connect=2.0, read=None, write=None, pool=3.0)) as client:
                bbb_response = await client.post(
                    f"{available_services['blood_brain_barrier']}/filter",
                    json={
                        "content": message,
                        "context": "user_query",
                        "user_id": user_id,
                    },
                )
                if bbb_response.status_code == 200:
                    bbb_data = bbb_response.json()
                    if not bbb_data.get("approved", True):
                        block_reason = bbb_data.get("reason", "unknown")
                        logger.warning(f"  ⚠️  BBB blocked query: {block_reason}")
                        return {
                            "response": f"⚠️ Query filtered: {block_reason}",
                            "services_used": ["blood_brain_barrier"],
                            "consciousness_level": "filtered",
                            "processing_time": time.time() - start_time,
                            "architecture_layers": 0,
                        }
                    filtered_query = bbb_data.get("filtered_content", message)
                    logger.info("  ✅ BBB: Query approved and filtered")
                    services_used.append("blood_brain_barrier")
        except Exception as e:
            logger.debug(f"  ⚠️  BBB filtering error: {str(e)[:80]}")

    logger.info("Phase 1.5: Querying RAG and Web for context...")
    rag_context = ""
    web_context = ""

    if "rag_server" in available_services:
        rag_result = await query_service(
            "rag_server",
            available_services["rag_server"],
            filtered_query,
            user_id,
        )
        if rag_result:
            services_used.append("rag_server")
            responses.append(rag_result)
            rag_context = rag_result["response"]
            logger.info(f"  ✅ RAG context length: {len(rag_context)}")

    if "web_research" in available_services:
        web_result = await query_service(
            "web_research",
            available_services["web_research"],
            filtered_query,
            user_id,
        )
        if web_result:
            services_used.append("web_research")
            responses.append(web_result)
            web_context = web_result["response"]
            logger.info(f"  ✅ Web context length: {len(web_context)}")

    fused_context_parts: List[str] = []
    if rag_context:
        fused_context_parts.append(f"From internal knowledge:\n{rag_context}")
    if web_context:
        fused_context_parts.append(f"From recent web sources:\n{web_context}")

    context_block = "\n\n".join(fused_context_parts)
    enhanced_message = filtered_query
    if context_block:
        enhanced_message = (
            "You are Ms. Allis ULTIMATE. Use the following context, "
            "then answer the user.\n\n"
            f"{context_block}\n\nUser question: {message}"
        )
        logger.info("  ✅ Message enhanced with fused RAG + Web context")

    llm_output = ""
    fabric_errors = []

    if "wv_entangled" in available_services:
        wv_result = await query_service(
            "wv_entangled",
            available_services["wv_entangled"],
            enhanced_message,
            user_id,
        )
        if wv_result and wv_result.get("response"):
            services_used.append("wv_entangled")
            responses.append(wv_result)
            llm_output = wv_result["response"]

    if (not llm_output) and "llm_bridge" in available_services:
        llm_result = await query_service(
            "llm_bridge",
            available_services["llm_bridge"],
            enhanced_message,
            user_id,
        )
        if llm_result and llm_result.get("response"):
            services_used.append("llm_bridge")
            responses.append(llm_result)
            llm_output = llm_result["response"]
        else:
            fabric_errors.append("llm_bridge empty or failed")

    if (not llm_output) and ("consciousness_bridge" in available_services):
        cb_result = await query_service(
            "consciousness_bridge",
            available_services["consciousness_bridge"],
            enhanced_message,
            user_id,
        )
        if cb_result and cb_result.get("response"):
            services_used.append("consciousness_bridge")
            responses.append(cb_result)
            llm_output = cb_result["response"]
        else:
            fabric_errors.append("consciousness_bridge empty or failed")

    if not llm_output:
        logger.error(f"LLM fabric failure for message len={len(message)}: {fabric_errors}")
        llm_output = (
            "I attempted to coordinate the full LLM collective for your request, "
            "but none of the available models produced a usable answer within "
            "the configured safety and time constraints."
        )

    final_response = llm_output

    log_response_summary(responses)

    try:
        background_tasks.add_task(
            background_rag_store,
            message,
            final_response,
            services_used,
        )
        logger.info(f"📝 Queued for RAG storage: {message[:40]}...")
    except Exception as e:
        logger.warning(f"Storage queue error: {e}")

    return {
        "response": clean_response_for_display(final_response),
        "services_used": services_used,
        "consciousness_level": "ultimate_collective",
        "processing_time": time.time() - start_time,
        "architecture_layers": len(responses),
    }


@app.get("/")
async def root():
    return {
        "service": "Ms. Allis ULTIMATE",
        "version": "1.0.0",
        "description": "Unified interface to all 32 Ms. Allis services",
        "port": 8050,
    }


if __name__ == "__main__":
    import uvicorn

    logger.info("🌟 Starting Ms. Allis ULTIMATE on port 8050")
    uvicorn.run(
        app,
        host="0.0.0.0",                         # was 127.0.0.1
        port=int(os.getenv("SERVICE_PORT", "8017")),  # default now 8017
    )
proposed_userid : cakidd  OK
status          : active  OK
roles           : admin,user  OK
county          : Fayette
bcrypt          : True
email→uuid      : fc238378-14f5-4a10-9865-ae241ea2ef74

SEED COMPLETE
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ 

