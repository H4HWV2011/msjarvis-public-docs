(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild && \
mkdir -p audit && \
printf '\n=== 1) auth_router.py: login/current-user/me/logout ===\n' && \
sed -n '180,390p' auth_router.py | tee audit/01_auth_router_core.txt && \
printf '\n=== 2) auth_router.py: all routes depending on _current_user ===\n' && \
grep -nE 'Depends\(_current_user\)|async def me\(|async def admin_chat_metrics\(|async def list_pending\(|async def get_my_balances\(' auth_router.py | tee audit/02_auth_router_protected_routes.txt && \
printf '\n=== 3) token_service.py: bearer token creation/validation ===\n' && \
sed -n '1,260p' token_service.py | tee audit/03_token_service.txt && \
printf '\n=== 4) session_identity.py: current user -> secret_uuid bridge ===\n' && \
sed -n '1,220p' session_identity.py | tee audit/04_session_identity.txt && \
printf '\n=== 5) auth_api.py session flow using msallis_session ===\n' && \
sed -n '110,310p' auth_api.py | tee audit/05_auth_api_session_flow.txt && \
printf '\n=== 6) auth_api.patched.py session flow using msallis_session ===\n' && \
sed -n '110,310p' auth_api.patched.py | tee audit/06_auth_api_patched_session_flow.txt && \
printf '\n=== 7) auth_api_no_full_router.py session flow using msallis_session ===\n' && \
sed -n '110,310p' auth_api_no_full_router.py | tee audit/07_auth_api_no_full_router_session_flow.txt && \
printf '\n=== 8) direct secret_uuid references in active app files ===\n' && \
grep -Rni --include='*.py' --include='*.sql' --exclude-dir='.archive' --exclude-dir='production_closeout*' --exclude-dir='crypto-venv' 'secret_uuid' . | tee audit/08_secret_uuid_references.txt && \
ypoints.txtpto-venv' -E 'FastAPI\(|include_router\(|uvicorn.run\(' . | tee audit/10_fastapi_entr

=== 1) auth_router.py: login/current-user/me/logout ===
        uei = UEIService(r)
        app_svc = ApplicationService(r, uei)
        _svc["reg"] = RegistrationService(app_svc)
        _svc["tok"] = TokenService(r)
        _svc["r"] = r
    return _svc["reg"], _svc["tok"], _svc["r"]


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def _current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    logger.warning("current_user received token=%r", token)
    _, tok, _ = _get_services()
    payload = tok.verify_access_token(token)
    logger.warning("current_user payload=%r", payload)
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
    application_id:   str
    proposed_userid:  str
    agreement_version: str | None = None
    message:          str | None = None
    # Merkle membership proof fields — commitment_salt is ONE-TIME, unrecoverable after this response
    commitment_salt:  str | None = None
    appearance_id:    str | None = None

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class RefreshRequest(BaseModel):
    refresh_token: str


class MeResponse(BaseModel):
    userid:      str
    uei:         str | None = None   # alias for ueid — frontend canonical field
    ueid:        str | None = None   # same value, both returned for compat
    roles:       list[str] = []
    county:      str | None = None
    name:        str | None = None
    email:       str | None = None
    status:      str | None = None
    visibility:  str | None = None
    bsc_status:  str | None = None
    first_login_at: str | None = None


@auth_router.post("/register", response_model=RegistrationResponse, status_code=201)
async def register(body: RegistrationRequest, request: Request, _preflight=Depends(_hp_antisurveillance_preflight)):
    if not _preflight.get("allowed", False):
        raise HTTPException(status_code=403, detail=_preflight.get("reason", "Registration blocked by anti-surveillance policy."))
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

    # Write PII name to kyc_vault (secret tier) — not Redis
    try:
        _kyc_result = _write_kyc_vault(public_uuid, body.name, ueid) or {}
    except Exception as e:
        logger.warning("[KYC] Non-fatal vault write failure during register: %s", e)
        _kyc_result = {}

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
    r.hset(f"user:{public_uuid}", mapping={
        "is_public":     "false",
        "visibility":    "private",
        "appearance_id": _kyc_result.get("appearance_id", ""),
    })
    logger.info(f"[AUTH] Registered {public_uuid} county={body.county} wallet={wallet.address}")
    # NOTE: No email sent here. Email fires only on admin approval.
    return RegistrationResponse(
        application_id=result.application_id,
        proposed_userid=result.proposed_userid,
        agreement_version=result.agreement_version,
        message=result.message,
        commitment_salt=_kyc_result.get("commitment_salt"),
        appearance_id=_kyc_result.get("appearance_id"),
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

=== 2) auth_router.py: all routes depending on _current_user ===
377:async def me(payload: Annotated[dict, Depends(_current_user)]):
415:async def admin_chat_metrics(payload: Annotated[dict, Depends(_current_user)]):
435:async def list_pending(payload: Annotated[dict, Depends(_current_user)]):
489:    payload: Annotated[dict, Depends(_current_user)],
743:    payload: Annotated[dict, Depends(_current_user)],
842:async def get_my_balances(payload: Annotated[dict, Depends(_current_user)]):
890:    payload: Annotated[dict, Depends(_current_user)],
1011:    payload: Annotated[dict, Depends(_current_user)],
1082:    payload: Annotated[dict, Depends(_current_user)],
1118:    user:    dict = Depends(_current_user),

=== 3) token_service.py: bearer token creation/validation ===
"""
token_service.py — Issues red-team access tokens that match your existing schema

Every existing token in your Redis was created with this exact shape — we mirror it
exactly so existing pipeline code keeps working without changes:

    redteam:token:rt_<24hex> = hash {
        userid:     "first_last",
        label:      "First Last",
        role:       "user" | "carrie_admin",
        created_at: "<iso8601 utc>",
        active:     "true"
    }
    redteam:quota:<userid> = hash {
        total_requests: "0",
        total_blocked:  "0",
        created_at:     "<iso8601 utc>"
    }
"""

from __future__ import annotations

import secrets
from datetime import datetime, timezone
from typing import Optional


class TokenService:
    TOKEN_PREFIX = "rt_"
    TOKEN_HEX_LEN = 24  # matches your existing rt_<24hex> tokens
    TOKEN_TTL = 60 * 60 * 24 * 90  # 90 days — rolling (refreshed on each use)

    def __init__(self, redis_client):
        self.redis = redis_client

    def _generate_token(self) -> str:
        # 24 hex chars = 12 bytes = 96 bits of entropy. Matches existing tokens.
        return f"{self.TOKEN_PREFIX}{secrets.token_hex(self.TOKEN_HEX_LEN // 2)}"

    def issue_token(self, *, userid: str, label: str, role: str = "newcomer", rank: str = "newcomer") -> str:
        _ARCH     = ("user", "admin", "carrie_admin")
        _GAMIFIED = ("newcomer", "user", "champion", "elder")
        if role not in _ARCH + _GAMIFIED:
            raise ValueError(f'unknown role {role!r}')
        if rank not in _GAMIFIED:
            rank = "newcomer"  # safe default, don't raise

        token = self._generate_token()
        now = datetime.now(timezone.utc).isoformat()

        # Token hash — matches existing schema field-for-field.
        # Single-session-per-user: DISABLED (was deleting new tokens)
        pass  # wipe disabled

        self.redis.hset(f"redteam:token:{token}", mapping={
            "userid":     userid,
            "label":      label,
            "role":       role,    # architectural: admin|user|carrie_admin
            "rank":       rank,    # gamified: newcomer|user|champion|elder
            "created_at": now,
            "active":     "true",
            "sub":        userid,
        })
        # TTL: rolling 90-day expiry, refreshed on each validate_token call
        self.redis.expire(f"redteam:token:{token}", self.TOKEN_TTL)

        # Quota hash — matches existing schema. Idempotent on userid.
        if not self.redis.exists(f"redteam:quota:{userid}"):
            self.redis.hset(f"redteam:quota:{userid}", mapping={
                "total_requests": "0",
                "total_blocked": "0",
                "created_at": now,
            })

        return token

    def validate_token(self, token: str) -> Optional[dict]:
        """Returns user info dict if token is valid + active, else None."""
        if not token or not token.startswith(self.TOKEN_PREFIX):
            return None
        key = f"redteam:token:{token}"
        record = self.redis.hgetall(key)
        if not record:
            return None
        record = {
            (k.decode() if isinstance(k, bytes) else k):
            (v.decode() if isinstance(v, bytes) else v)
            for k, v in record.items()
        }
        if record.get("active") != "true":
            return None
        self.redis.expire(key, self.TOKEN_TTL)
        return record

    def revoke_token(self, token: str) -> bool:
        if not self.redis.exists(f"redteam:token:{token}"):
            return False
        self.redis.hset(f"redteam:token:{token}", "active", "false")
        return True

    def list_tokens_for_userid(self, userid: str) -> list[str]:
        """Useful for revoke-all-by-userid flows. Scans redteam:token:* keys."""
        out = []
        for key in self.redis.scan_iter("redteam:token:*"):
            key_str = key.decode() if isinstance(key, bytes) else key
            record = self.redis.hgetall(key_str)
            record_userid = record.get("userid") or record.get(b"userid")
            if isinstance(record_userid, bytes):
                record_userid = record_userid.decode()
            if record_userid == userid:
                out.append(key_str.replace("redteam:token:", ""))
        return out


    # ── Auth-router compatibility methods ─────────────────────────────────

    def authenticate(self, username: str, password: str) -> dict | None:
        """
        Validate username + password against Redis user record.
        Returns token dict on success, None on failure.

        Expected Redis key: user:{userid}  fields: password_hash, roles, county, uei
        Password stored as bcrypt hash; falls back to plaintext match for dev seeds.
        """
        import bcrypt
        username_clean = username.strip().lower()
        # First try direct key lookup (legacy: user:carrie_admin style)
        record = self.redis.hgetall(f"user:{username_clean}")
        # If not found, scan for matching proposed_userid (UUID-keyed records)
        if not record:
            for k in self.redis.scan_iter("user:*"):
                rec = self.redis.hgetall(k)
                if rec.get("proposed_userid", "").lower() == username_clean:
                    record = rec
                    break
                if rec.get("email", "").lower() == username_clean:
                    record = rec
                    break
        if not record:
            return None
        stored = record.get("password_hash", "")
        # bcrypt check
        try:
            ok = bcrypt.checkpw(password.encode(), stored.encode())
        except Exception:
            # dev fallback: plaintext
            ok = (password == stored)
        if not ok:
            return None
        roles = [r for r in record.get("roles", "user").split(",") if r]
        arch_roles = [r for r in roles if r in ("admin", "user", "carrie_admin")]
        rank = record.get("rank", "newcomer")
        token = self.issue_token(
            userid=record.get("userid") or username.strip().lower(),
            label="login",
            role=arch_roles[0] if arch_roles else "user",
            rank=rank,
        )
        return {
            "access_token": token,
            "token_type": "bearer",
            "expires_in": self.TOKEN_TTL,
            "roles": roles,
            "uei": record.get("uei", ""),
            "county": record.get("county", ""),
        }

    def verify_access_token(self, token: str) -> dict | None:
        """
        Validate a bearer token.  Returns payload dict or None if invalid/expired.
        Payload keys: sub, roles, uei, county, label.
        """
        record = self.validate_token(token)
        if record is None:
            return None
        return {
            "sub": record.get("userid", ""),
            "roles": [r for r in record.get("roles", record.get("role", "user")).split(",") if r],
            "uei": record.get("uei", ""),
            "county": record.get("county", ""),
            "label": record.get("label", ""),
        }

    def refresh(self, refresh_token: str) -> dict | None:
        """
        Exchange a refresh token for a new access token.
        Refresh tokens are stored as: refresh:{token} -> userid
        """
        userid = self.redis.get(f"refresh:{refresh_token}")
        if not userid:
            return None
        # issue a fresh access token
        token = self.issue_token(userid=userid, label="refresh", role="user")
        # delete used refresh token (one-time use)
        self.redis.delete(f"refresh:{refresh_token}")
        return {
            "access_token": token,
            "token_type": "bearer",
            "expires_in": 86400,
        }


# ── FastAPI shim so uvicorn token_service:app works ──────────────────────────
from fastapi import FastAPI
app = FastAPI(title="MS Jarvis Token Service", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "token_service"}

=== 4) session_identity.py: current user -> secret_uuid bridge ===
import asyncpg
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException

VAULT_DB = dict(host="127.0.0.1", port=5435, user="postgres", password="postgres", database="msjarvisgis")
PROFILE_DB = dict(host="127.0.0.1", port=5436, user="postgres", password="postgres", database="msjarvisgis")

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.vault_db = await asyncpg.create_pool(**VAULT_DB, min_size=1, max_size=10)
    app.state.profile_db = await asyncpg.create_pool(**PROFILE_DB, min_size=1, max_size=10)
    try:
        yield
    finally:
        await app.state.vault_db.close()
        await app.state.profile_db.close()

app = FastAPI(lifespan=lifespan)

async def get_current_user():
    # Temporary test stub. Replace this with your real auth dependency.
    # It must return a dict containing the authenticated app user_id.
    return {"user_id": 1}

async def get_secret_uuid(current_user=Depends(get_current_user)):
    async with app.state.vault_db.acquire() as conn:
        row = await conn.fetchrow(
            """
            SELECT secret_uuid
            FROM public.user_identity_map
            WHERE user_id = $1
            """,
            current_user["user_id"],
        )
    if not row:
        raise HTTPException(status_code=404, detail="No secret_uuid mapped for user")
    return str(row["secret_uuid"])

async def load_private_profile(secret_uuid: str):
    async with app.state.profile_db.acquire() as conn:
        row = await conn.fetchrow(
            """
            SELECT
              secret_uuid,
              full_legal_name,
              home_address_line1,
              home_address_city,
              home_address_state,
              home_address_postal_code,
              home_address_country,
              date_of_birth,
              role
            FROM public.private_profiles
            WHERE secret_uuid = $1::uuid
            """,
            secret_uuid,
        )
    return dict(row) if row else None

@app.get("/whoami")
async def whoami(secret_uuid: str = Depends(get_secret_uuid)):
    profile = await load_private_profile(secret_uuid)
    if not profile:
        raise HTTPException(status_code=404, detail="Private profile not found")
    return {"secret_uuid": secret_uuid, "profile": profile}

@app.post("/chat")
async def chat(message: dict, secret_uuid: str = Depends(get_secret_uuid)):
    profile = await load_private_profile(secret_uuid)
    if not profile:
        raise HTTPException(status_code=404, detail="Private profile not found")

    text = " ".join((message.get("text") or "").lower().split())
    triggers = [
        "who are you speaking to",
        "who you're speaking to",
        "who you are speaking to",
        "do you know who you are speaking to",
        "do you know who you're speaking to",
        "who am i",
        "do you know who i am",
    ]

    if any(trigger in text for trigger in triggers):
        role = profile.get("role")
        name = profile["full_legal_name"]
        city = profile["home_address_city"]
        state = profile["home_address_state"]
        if role:
            return {"reply": f"I am speaking with {role} {name} from {city}, {state}."}
        return {"reply": f"I am speaking with {name} from {city}, {state}."}

    return {"reply": "Message received."}

=== 5) auth_api.py session flow using msallis_session ===
# ── Helpers ───────────────────────────────────────────────────────────────────

def _send_email(to: str, subject: str, body: str):
    if not RESEND_KEY or RESEND_KEY.startswith("re_YOUR"):
        print(f"[DRY RUN EMAIL] To: {to}\nSubject: {subject}\n{body}\n")
        return
    import resend

    resend.api_key = RESEND_KEY
    resend.Emails.send({
        "from":    "ms.allis@mountainshares.us",
        "to":      to,
        "subject": subject,
        "text":    body,
    })

def _get_current_user(session_token: str | None) -> dict | None:
    if not session_token:
        return None
    return ts.validate_token(session_token)

# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    return {"status": "healthy", "service": "ms-allis-auth", "timestamp": datetime.now(timezone.utc).isoformat()}


@router.post("/apply")
async def apply(req: ApplicationRequest, request: Request):
    ip = request.client.host if request.client else ""
    try:
        app_id, proposed = _app_svc.submit_application(
            name=req.name,
            email=req.email,
            county=req.county,
            motivation=req.motivation,
            agreement_accepted=req.agreement_accepted,
            ip_address=ip,
        )
    except Exception as exc:
        raise HTTPException(400, str(exc))

    # Store supplemental fields not in ApplicationService core
    r.hset(f"pending_application:{app_id}", mapping={
        "bsc_status":      req.bsc_status or "unknown",
        "agreement_hash":  req.agreement_hash or "",
        "selfie_image":    req.selfie_image or "",
        "dl_image":        req.dl_image or "",
    })

    now = datetime.now(timezone.utc).isoformat()
    _send_email(
        ADMIN_EMAIL,
        f"New Ms. Allis application: {req.name} ({req.county} County)",
        f"""A new Community Champion application is waiting for your review.

Name:       {req.name}
Email:      {req.email}
County:     {req.county}
BSA Status: {req.bsc_status}
Submitted:  {now}
Proposed userid: {proposed}

Why they want to participate:
{req.motivation}

Application ID: {app_id}

To approve:
  cdj && python3 admin_cli.py approve {app_id}

To deny:
  cdj && python3 admin_cli.py deny {app_id} --reason "..."
"""
    )
    return {"status": "received", "message": "Thank you! We\'ll review your application and send you a magic link to log in."}


@router.get("/login")
def login(token: str, response: Response):
    user = ts.validate_token(token)
    if not user:
        raise HTTPException(401, "invalid or expired token")
    resp = RedirectResponse(url="/chat", status_code=302)
    resp.set_cookie(
        key="msallis_session",
        value=token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60 * 60 * 24 * 30,  # 30 days
    )
    return resp



def _get_wallet_public(userid: str):
    candidates = [
        f"wallet:public:{userid}",
        f"wallet:{userid}",
        f"user:wallet:{userid}",
    ]
    for key in candidates:
        try:
            data = r.hgetall(key)
            if data:
                return data
        except Exception:
            pass
    return None


@router.get("/me/legacy")
def me(msallis_session: str | None = Cookie(default=None)):
    user = _get_current_user(msallis_session)
    if not user:
        raise HTTPException(401, "not logged in")
    userid = user["userid"]

    uei    = r.get(f"uei:by_user:{userid}")
    try:
        wallet = _get_wallet_public(userid)
    except Exception:
        wallet = None
    quota  = r.hgetall(f"redteam:quota:{userid}") or {}
    profile= r.hgetall(f"user:{userid}") or {}

    return {
        "userid":  userid,
        "name":    profile.get("name", userid),
        "email":   profile.get("email", ""),
        "role":    user.get("role", "user"),
        "uei":     uei,
        "wallet":  wallet,
        "quota": {
            "requests_today": int(quota.get("requests_today", 0)),
            "daily_limit":    int(quota.get("daily_limit",    50)),
            "blocked":        int(quota.get("blocked",         0)),
        }
    }


@router.post("/chat")
async def chat(req: ChatRequest, msallis_session: str | None = Cookie(default=None)):
    user = _get_current_user(msallis_session)
    if not user:
        raise HTTPException(401, "not logged in")

    userid = user["userid"]
    role   = user.get("role", "user")

    # Quota check
    quota_key = f"redteam:quota:{userid}"
    today     = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    last_day  = r.hget(quota_key, "quota_date")
    if last_day != today:
        r.hset(quota_key, "requests_today", 0)
        r.hset(quota_key, "quota_date",     today)
    limit = int(r.hget(quota_key, "daily_limit") or 50)
    count = int(r.hget(quota_key, "requests_today") or 0)
    if count >= limit and role not in ("carrie_admin", "admin"):
        r.hincrby(quota_key, "blocked", 1)
        raise HTTPException(429, f"daily limit of {limit} messages reached — resets at midnight UTC")

    # Proxy to Egeria
    async with httpx.AsyncClient(timeout=60) as client:
        headers = {"Content-Type": "application/json"}
        if JARVIS_TOKEN:
            headers["Authorization"] = f"Bearer {JARVIS_TOKEN}"
        if JARVIS_API_KEY:
            headers["X-API-Key"] = JARVIS_API_KEY

        resp = await client.post(
            f"{JARVIS_URL}/chat",
            headers=headers,
            json={"message": req.message, "user_id": userid, "role": role},
        )

    r.hincrby(quota_key, "requests_today", 1)

    if resp.status_code != 200:
        raise HTTPException(502, "Egeria is unavailable right now")

    return resp.json()

app.include_router(router)

# Full auth router — login, register, first-login, KYC, portal, admin
from auth_router import auth_router
app.include_router(auth_router)

=== 6) auth_api.patched.py session flow using msallis_session ===
    message: str

# ── Helpers ───────────────────────────────────────────────────────────────────

def _send_email(to: str, subject: str, body: str):
    if not RESEND_KEY or RESEND_KEY.startswith("re_YOUR"):
        print(f"[DRY RUN EMAIL] To: {to}\nSubject: {subject}\n{body}\n")
        return
    import resend
    resend.api_key = RESEND_KEY
    resend.Emails.send({
        "from":    "ms.allis@mountainshares.us",
        "to":      to,
        "subject": subject,
        "text":    body,
    })

def _get_current_user(session_token: str | None) -> dict | None:
    if not session_token:
        return None
    return ts.validate_token(session_token)

# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    return {"status": "healthy", "service": "ms-allis-auth", "timestamp": datetime.now(timezone.utc).isoformat()}


@router.post("/apply")
async def apply(req: ApplicationRequest, request: Request):
    ip = request.client.host if request.client else ""
    try:
        app_id, proposed = _app_svc.submit_application(
            name=req.name,
            email=req.email,
            county=req.county,
            motivation=req.motivation,
            agreement_accepted=req.agreement_accepted,
            ip_address=ip,
        )
    except Exception as exc:
        raise HTTPException(400, str(exc))

    # Store supplemental fields not in ApplicationService core
    r.hset(f"pending_application:{app_id}", mapping={
        "bsc_status":      req.bsc_status or "unknown",
        "agreement_hash":  req.agreement_hash or "",
        "selfie_image":    req.selfie_image or "",
        "dl_image":        req.dl_image or "",
    })

    now = datetime.now(timezone.utc).isoformat()
    _send_email(
        ADMIN_EMAIL,
        f"New Ms. Allis application: {req.name} ({req.county} County)",
        f"""A new Community Champion application is waiting for your review.

Name:       {req.name}
Email:      {req.email}
County:     {req.county}
BSA Status: {req.bsc_status}
Submitted:  {now}
Proposed userid: {proposed}

Why they want to participate:
{req.motivation}

Application ID: {app_id}

To approve:
  cdj && python3 admin_cli.py approve {app_id}

To deny:
  cdj && python3 admin_cli.py deny {app_id} --reason "..."
"""
    )
    return {"status": "received", "message": "Thank you! We\'ll review your application and send you a magic link to log in."}


@router.get("/login")
def login(token: str, response: Response):
    user = ts.validate_token(token)
    if not user:
        raise HTTPException(401, "invalid or expired token")
    resp = RedirectResponse(url="/chat", status_code=302)
    resp.set_cookie(
        key="msallis_session",
        value=token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60 * 60 * 24 * 30,  # 30 days
    )
    return resp


@router.get("/me")
def me(msallis_session: str | None = Cookie(default=None)):
    user = _get_current_user(msallis_session)
    if not user:
        raise HTTPException(401, "not logged in")
    userid = user["userid"]

    uei    = r.get(f"uei:by_user:{userid}")
    wallet = ws.get_wallet_public(userid)
    quota  = r.hgetall(f"redteam:quota:{userid}") or {}
    profile= r.hgetall(f"user:{userid}") or {}

    return {
        "userid":  userid,
        "name":    profile.get("name", userid),
        "email":   profile.get("email", ""),
        "role":    user.get("role", "user"),
        "uei":     uei,
        "wallet":  wallet,
        "quota": {
            "requests_today": int(quota.get("requests_today", 0)),
            "daily_limit":    int(quota.get("daily_limit",    50)),
            "blocked":        int(quota.get("blocked",         0)),
        }
    }


@router.post("/chat")
async def chat(req: ChatRequest, msallis_session: str | None = Cookie(default=None)):
    user = _get_current_user(msallis_session)
    if not user:
        raise HTTPException(401, "not logged in")

    userid = user["userid"]
    role   = user.get("role", "user")

    # Quota check
    quota_key = f"redteam:quota:{userid}"
    today     = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    last_day  = r.hget(quota_key, "quota_date")
    if last_day != today:
        r.hset(quota_key, "requests_today", 0)
        r.hset(quota_key, "quota_date",     today)
    limit = int(r.hget(quota_key, "daily_limit") or 50)
    count = int(r.hget(quota_key, "requests_today") or 0)
    if count >= limit and role not in ("carrie_admin", "admin"):
        r.hincrby(quota_key, "blocked", 1)
        raise HTTPException(429, f"daily limit of {limit} messages reached — resets at midnight UTC")

    # Proxy to Egeria
    async with httpx.AsyncClient(timeout=60) as client:
        headers = {"Content-Type": "application/json"}
        if JARVIS_TOKEN:
            headers["Authorization"] = f"Bearer {JARVIS_TOKEN}"
        if JARVIS_API_KEY:
            headers["X-API-Key"] = JARVIS_API_KEY

        resp = await client.post(
            f"{JARVIS_URL}/chat",
            headers=headers,
            json={"message": req.message, "user_id": userid, "role": role},
        )

    r.hincrby(quota_key, "requests_today", 1)

    if resp.status_code != 200:
        raise HTTPException(502, "Egeria is unavailable right now")

    return resp.json()

app.include_router(router)

=== 7) auth_api_no_full_router.py session flow using msallis_session ===
# ── Helpers ───────────────────────────────────────────────────────────────────

def _send_email(to: str, subject: str, body: str):
    if not RESEND_KEY or RESEND_KEY.startswith("re_YOUR"):
        print(f"[DRY RUN EMAIL] To: {to}\nSubject: {subject}\n{body}\n")
        return
    import resend
    resend.api_key = RESEND_KEY
    resend.Emails.send({
        "from":    "ms.allis@mountainshares.us",
        "to":      to,
        "subject": subject,
        "text":    body,
    })

def _get_current_user(session_token: str | None) -> dict | None:
    if not session_token:
        return None
    return ts.validate_token(session_token)

# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    return {"status": "healthy", "service": "ms-allis-auth", "timestamp": datetime.now(timezone.utc).isoformat()}


@router.post("/apply")
async def apply(req: ApplicationRequest, request: Request):
    ip = request.client.host if request.client else ""
    try:
        app_id, proposed = _app_svc.submit_application(
            name=req.name,
            email=req.email,
            county=req.county,
            motivation=req.motivation,
            agreement_accepted=req.agreement_accepted,
            ip_address=ip,
        )
    except Exception as exc:
        raise HTTPException(400, str(exc))

    # Store supplemental fields not in ApplicationService core
    r.hset(f"pending_application:{app_id}", mapping={
        "bsc_status":      req.bsc_status or "unknown",
        "agreement_hash":  req.agreement_hash or "",
        "selfie_image":    req.selfie_image or "",
        "dl_image":        req.dl_image or "",
    })

    now = datetime.now(timezone.utc).isoformat()
    _send_email(
        ADMIN_EMAIL,
        f"New Ms. Allis application: {req.name} ({req.county} County)",
        f"""A new Community Champion application is waiting for your review.

Name:       {req.name}
Email:      {req.email}
County:     {req.county}
BSA Status: {req.bsc_status}
Submitted:  {now}
Proposed userid: {proposed}

Why they want to participate:
{req.motivation}

Application ID: {app_id}

To approve:
  cdj && python3 admin_cli.py approve {app_id}

To deny:
  cdj && python3 admin_cli.py deny {app_id} --reason "..."
"""
    )
    return {"status": "received", "message": "Thank you! We\'ll review your application and send you a magic link to log in."}


@router.get("/login")
def login(token: str, response: Response):
    user = ts.validate_token(token)
    if not user:
        raise HTTPException(401, "invalid or expired token")
    resp = RedirectResponse(url="/chat", status_code=302)
    resp.set_cookie(
        key="msallis_session",
        value=token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60 * 60 * 24 * 30,  # 30 days
    )
    return resp



def _get_wallet_public(userid: str):
    candidates = [
        f"wallet:public:{userid}",
        f"wallet:{userid}",
        f"user:wallet:{userid}",
    ]
    for key in candidates:
        try:
            data = r.hgetall(key)
            if data:
                return data
        except Exception:
            pass
    return None


@router.get("/me")
def me(msallis_session: str | None = Cookie(default=None)):
    user = _get_current_user(msallis_session)
    if not user:
        raise HTTPException(401, "not logged in")
    userid = user["userid"]

    uei    = r.get(f"uei:by_user:{userid}")
    try:
        wallet = _get_wallet_public(userid)
    except Exception:
        wallet = None
    quota  = r.hgetall(f"redteam:quota:{userid}") or {}
    profile= r.hgetall(f"user:{userid}") or {}

    return {
        "userid":  userid,
        "name":    profile.get("name", userid),
        "email":   profile.get("email", ""),
        "role":    user.get("role", "user"),
        "uei":     uei,
        "wallet":  wallet,
        "quota": {
            "requests_today": int(quota.get("requests_today", 0)),
            "daily_limit":    int(quota.get("daily_limit",    50)),
            "blocked":        int(quota.get("blocked",         0)),
        }
    }


@router.post("/chat")
async def chat(req: ChatRequest, msallis_session: str | None = Cookie(default=None)):
    user = _get_current_user(msallis_session)
    if not user:
        raise HTTPException(401, "not logged in")

    userid = user["userid"]
    role   = user.get("role", "user")

    # Quota check
    quota_key = f"redteam:quota:{userid}"
    today     = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    last_day  = r.hget(quota_key, "quota_date")
    if last_day != today:
        r.hset(quota_key, "requests_today", 0)
        r.hset(quota_key, "quota_date",     today)
    limit = int(r.hget(quota_key, "daily_limit") or 50)
    count = int(r.hget(quota_key, "requests_today") or 0)
    if count >= limit and role not in ("carrie_admin", "admin"):
        r.hincrby(quota_key, "blocked", 1)
        raise HTTPException(429, f"daily limit of {limit} messages reached — resets at midnight UTC")

    # Proxy to Egeria
    async with httpx.AsyncClient(timeout=60) as client:
        headers = {"Content-Type": "application/json"}
        if JARVIS_TOKEN:
            headers["Authorization"] = f"Bearer {JARVIS_TOKEN}"
        if JARVIS_API_KEY:
            headers["X-API-Key"] = JARVIS_API_KEY

        resp = await client.post(
            f"{JARVIS_URL}/chat",
            headers=headers,
            json={"message": req.message, "user_id": userid, "role": role},
        )

    r.hincrby(quota_key, "requests_today", 1)

    if resp.status_code != 200:
        raise HTTPException(502, "Egeria is unavailable right now")

    return resp.json()

app.include_router(router)

# Full auth router — login, register, first-login, KYC, portal, admin
# disabled for isolation test

=== 8) direct secret_uuid references in active app files ===
grep: ./msjarvis-rebuild: warning: recursive directory loop
grep: ./services/ms_jarvis_mother_carrie_protocols.py: Permission denied
grep: ./data/local_resources: Permission denied
grep: ./data/mysql/sys: Permission denied
grep: ./data/mysql/#innodb_temp: Permission denied
grep: ./data/mysql/quantum_ai: Permission denied
grep: ./data/mysql/mysql: Permission denied
grep: ./data/mysql/performance_schema: Permission denied
grep: ./data/mysql/#innodb_redo: Permission denied
./services/jarvis-assertion-gateway/app/kyc_reader.py:30:                WHERE secret_uuid::text = $1
./services/jarvis-assertion-gateway/app/kyc_reader.py:46:                WHERE secret_uuid::text = $1
./services/jarvis-assertion-gateway/app/kyc_reader.py:61:                WHERE secret_uuid::text = $1
./services/jarvis-assertion-gateway/app/kyc_reader.py:75:                WHERE secret_uuid::text = $1
./services/jarvis-assertion-gateway/app/kyc_reader.py:89:                WHERE secret_uuid::text = $1
./services/jarvis-assertion-gateway/app/kyc_reader.py:110:                WHERE secret_uuid::text = $1
./services/conversion_service.py:74:        Returns {"secret_uuid": str, "pending_id": str}
./services/conversion_service.py:76:        secret_uuid   = str(uuid.uuid4())
./services/conversion_service.py:95:                    " secret_uuid, note, created_at) "
./services/conversion_service.py:100:                        secret_uuid,
./services/conversion_service.py:108:            amount, ueid, secret_uuid,
./services/conversion_service.py:110:        return {"secret_uuid": secret_uuid, "pending_id": conversion_id}
./services/conversion_service.py:117:        secret_uuid: str,
./services/conversion_service.py:160:        nonce_bytes  = bytes.fromhex(secret_uuid.replace("-", ""))
./services/conversion_service.py:209:                wallet_address, amount, locked["secret_uuid"], ueid
./services/chain_listener.py:57:    Finds the conversion_lock row whose secret_uuid matches the on-chain nonce
./services/chain_listener.py:71:                "WHERE secret_uuid = %s "
./auth_router.py:45:    Tier 1 (secret): fresh secret_uuid — never returned to user.
./auth_router.py:48:    Returns dict with private_uuid only (secret_uuid never leaves this function).
./auth_router.py:51:    secret_uuid = str(_uuid.uuid4())   # Tier 1 — never exposed
./auth_router.py:59:            "(secret_uuid, verified_name, kyc_provider, kyc_reference, privacy_tier, is_active) "
./auth_router.py:61:            "ON CONFLICT (secret_uuid) DO NOTHING",
./auth_router.py:62:            (secret_uuid, name, "self_declared", ueid or private_uuid, "secret", True)
./auth_router.py:67:            "(private_uuid, secret_uuid, county, motivation, visibility) "
./auth_router.py:70:            (private_uuid, secret_uuid, None, None,
./auth_router.py:142:            "secret_uuid":    secret_uuid,
./migrations/001_kyc_vault.sql:3:    secret_uuid     UUID        NOT NULL UNIQUE,
./migrations/001_kyc_vault.sql:20:CREATE INDEX IF NOT EXISTS idx_kyc_vault_secret_uuid ON kyc_vault(secret_uuid);
./migrations/005_three_tier_identity.sql:4:    secret_uuid    UUID NOT NULL REFERENCES public.kyc_vault(secret_uuid) ON DELETE CASCADE,
./migrations/005_three_tier_identity.sql:12:CREATE INDEX IF NOT EXISTS idx_private_profile_secret ON public.user_private_profile(secret_uuid);
./kyc-vault/app.py:26:    secret_uuid: UUID
./kyc-vault/app.py:49:                secret_uuid UUID NOT NULL UNIQUE DEFAULT gen_random_uuid(),
./kyc-vault/app.py:64:                secret_uuid UUID NOT NULL,
./kyc-vault/app.py:92:                secret_uuid UUID NOT NULL,
./kyc-vault/app.py:99:                UNIQUE (secret_uuid, consent_scope)
./kyc-vault/app.py:141:                RETURNING secret_uuid
./kyc-vault/app.py:143:        return {"secret_uuid": str(row["secret_uuid"])}
./kyc-vault/app.py:157:                        secret_uuid,
./kyc-vault/app.py:197:            req.secret_uuid,
./kyc-vault/app.py:220:    secret_uuid: str
./kyc-vault/app.py:225:    secret_uuid: str
./kyc-vault/app.py:238:              (secret_uuid, consent_scope, consent_granted_at, consent_expires_at, active)
./kyc-vault/app.py:240:            ON CONFLICT (secret_uuid, consent_scope)
./kyc-vault/app.py:244:            req.secret_uuid,
./kyc-vault/app.py:258:                WHERE secret_uuid = $1::uuid
./kyc-vault/app.py:260:            """, req.secret_uuid, req.consent_scope, req.reason)
./kyc-vault/app.py:266:                WHERE secret_uuid = $1::uuid
./kyc-vault/app.py:267:            """, req.secret_uuid, req.reason)
./kyc-vault/app.py:270:@app.get("/consent/status/{secret_uuid}")
./kyc-vault/app.py:271:async def consent_status(secret_uuid: str):
./kyc-vault/app.py:277:            WHERE secret_uuid = $1::uuid
./kyc-vault/app.py:279:        """, secret_uuid)
./kyc-vault/app.py:288:        "secret_uuid": secret_uuid,
./session_identity.py:25:async def get_secret_uuid(current_user=Depends(get_current_user)):
./session_identity.py:29:            SELECT secret_uuid
./session_identity.py:36:        raise HTTPException(status_code=404, detail="No secret_uuid mapped for user")
./session_identity.py:37:    return str(row["secret_uuid"])
./session_identity.py:39:async def load_private_profile(secret_uuid: str):
./session_identity.py:44:              secret_uuid,
./session_identity.py:54:            WHERE secret_uuid = $1::uuid
./session_identity.py:56:            secret_uuid,
./session_identity.py:61:async def whoami(secret_uuid: str = Depends(get_secret_uuid)):
./session_identity.py:62:    profile = await load_private_profile(secret_uuid)
./session_identity.py:65:    return {"secret_uuid": secret_uuid, "profile": profile}
./session_identity.py:68:async def chat(message: dict, secret_uuid: str = Depends(get_secret_uuid)):
./session_identity.py:69:    profile = await load_private_profile(secret_uuid)
./provenance/app.py:22:    secret_uuid: str
./provenance/app.py:46:        "secret_uuid":    req.secret_uuid,

=== 9) auth/router/session/token cross-reference summary ===
grep: ./msjarvis-rebuild: warning: recursive directory loop
./token_service.py:161:            "token_type": "bearer",
./token_service.py:170:        Validate a bearer token.  Returns payload dict or None if invalid/expired.
./token_service.py:198:            "token_type": "bearer",
./auth_api.patched.py:29:JARVIS_TOKEN  = os.getenv("JARVIS_TOKEN", "internal")
./auth_api.patched.py:127:def _get_current_user(session_token: str | None) -> dict | None:
./auth_api.patched.py:197:        key="msallis_session",
./auth_api.patched.py:208:def me(msallis_session: str | None = Cookie(default=None)):
./auth_api.patched.py:209:    user = _get_current_user(msallis_session)
./auth_api.patched.py:235:async def chat(req: ChatRequest, msallis_session: str | None = Cookie(default=None)):
./auth_api.patched.py:236:    user = _get_current_user(msallis_session)
./auth_api.patched.py:259:        if JARVIS_TOKEN:
./auth_api.patched.py:260:            headers["Authorization"] = f"Bearer {JARVIS_TOKEN}"
grep: ./services/ms_jarvis_mother_carrie_protocols.py: Permission denied
grep: ./data/local_resources: Permission denied
grep: ./data/mysql/sys: Permission denied
grep: ./data/mysql/#innodb_temp: Permission denied
grep: ./data/mysql/quantum_ai: Permission denied
grep: ./data/mysql/mysql: Permission denied
grep: ./data/mysql/performance_schema: Permission denied
grep: ./data/mysql/#innodb_redo: Permission denied
./services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:746:        "token_type": "bearer",
./auth_api_no_full_router.py:28:JARVIS_TOKEN  = os.getenv("JARVIS_TOKEN", "internal")
./auth_api_no_full_router.py:125:def _get_current_user(session_token: str | None) -> dict | None:
./auth_api_no_full_router.py:195:        key="msallis_session",
./auth_api_no_full_router.py:223:def me(msallis_session: str | None = Cookie(default=None)):
./auth_api_no_full_router.py:224:    user = _get_current_user(msallis_session)
./auth_api_no_full_router.py:253:async def chat(req: ChatRequest, msallis_session: str | None = Cookie(default=None)):
./auth_api_no_full_router.py:254:    user = _get_current_user(msallis_session)
./auth_api_no_full_router.py:277:        if JARVIS_TOKEN:
./auth_api_no_full_router.py:278:            headers["Authorization"] = f"Bearer {JARVIS_TOKEN}"
./auth_router.py:23:from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
./auth_router.py:188:oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
./auth_router.py:191:async def _current_user(token: Annotated[str, Depends(oauth2_scheme)]):
./auth_router.py:232:    token_type: str = "bearer"
./auth_router.py:355:    """Invalidate the bearer token server-side."""
./auth_router.py:377:async def me(payload: Annotated[dict, Depends(_current_user)]):
./auth_router.py:415:async def admin_chat_metrics(payload: Annotated[dict, Depends(_current_user)]):
./auth_router.py:435:async def list_pending(payload: Annotated[dict, Depends(_current_user)]):
./auth_router.py:489:    payload: Annotated[dict, Depends(_current_user)],
./auth_router.py:743:    payload: Annotated[dict, Depends(_current_user)],
./auth_router.py:786:    token_type:     str = "bearer"
./auth_router.py:842:async def get_my_balances(payload: Annotated[dict, Depends(_current_user)]):
./auth_router.py:890:    payload: Annotated[dict, Depends(_current_user)],
./auth_router.py:1011:    payload: Annotated[dict, Depends(_current_user)],
./auth_router.py:1082:    payload: Annotated[dict, Depends(_current_user)],
./auth_router.py:1118:    user:    dict = Depends(_current_user),
./auth_api.py:28:JARVIS_TOKEN  = os.getenv("JARVIS_TOKEN", "internal")
./auth_api.py:126:def _get_current_user(session_token: str | None) -> dict | None:
./auth_api.py:196:        key="msallis_session",
./auth_api.py:224:def me(msallis_session: str | None = Cookie(default=None)):
./auth_api.py:225:    user = _get_current_user(msallis_session)
./auth_api.py:254:async def chat(req: ChatRequest, msallis_session: str | None = Cookie(default=None)):
./auth_api.py:255:    user = _get_current_user(msallis_session)
./auth_api.py:278:        if JARVIS_TOKEN:
./auth_api.py:279:            headers["Authorization"] = f"Bearer {JARVIS_TOKEN}"
./.check_venv/lib64/python3.12/site-packages/fastapi/security/oauth2.py:433:class OAuth2PasswordBearer(OAuth2):
./.check_venv/lib64/python3.12/site-packages/fastapi/security/http.py:135:    def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
./.check_venv/lib64/python3.12/site-packages/fastapi/security/http.py:247:    def read_current_user(
./.check_venv/lib64/python3.12/site-packages/fastapi/security/http.py:350:    def read_current_user(
./.check_venv/lib64/python3.12/site-packages/fastapi/security/__init__.py:11:from .oauth2 import OAuth2PasswordBearer as OAuth2PasswordBearer
./.check_venv/lib64/python3.12/site-packages/huggingface_hub/_oauth.py:429:        "token_type": "bearer",
./.check_venv/lib64/python3.12/site-packages/pygments/formatters/img.py:174:        keynames = [ (_winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows NT\CurrentVersion\Fonts'),
./.check_venv/lib64/python3.12/site-packages/pygments/formatters/img.py:175:                     (_winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Fonts'),
./.check_venv/lib64/python3.12/site-packages/pygments/lexers/_php_builtins.py:1870:                      'get_current_user',
./.check_venv/lib64/python3.12/site-packages/pip/_vendor/requests/utils.py:84:                winreg.HKEY_CURRENT_USER,
./.check_venv/lib64/python3.12/site-packages/pip/_vendor/platformdirs/windows.py:199:    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
./.check_venv/lib64/python3.12/site-packages/pip/_vendor/pygments/formatters/img.py:168:        keynames = [ (_winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows NT\CurrentVersion\Fonts'),
./.check_venv/lib64/python3.12/site-packages/pip/_vendor/pygments/formatters/img.py:169:                     (_winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Fonts'),
./.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py:433:class OAuth2PasswordBearer(OAuth2):
./.check_venv/lib/python3.12/site-packages/fastapi/security/http.py:135:    def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
./.check_venv/lib/python3.12/site-packages/fastapi/security/http.py:247:    def read_current_user(
./.check_venv/lib/python3.12/site-packages/fastapi/security/http.py:350:    def read_current_user(
./.check_venv/lib/python3.12/site-packages/fastapi/security/__init__.py:11:from .oauth2 import OAuth2PasswordBearer as OAuth2PasswordBearer
./.check_venv/lib/python3.12/site-packages/huggingface_hub/_oauth.py:429:        "token_type": "bearer",
./.check_venv/lib/python3.12/site-packages/pygments/formatters/img.py:174:        keynames = [ (_winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows NT\CurrentVersion\Fonts'),
./.check_venv/lib/python3.12/site-packages/pygments/formatters/img.py:175:                     (_winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Fonts'),
./.check_venv/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py:1870:                      'get_current_user',
./.check_venv/lib/python3.12/site-packages/pip/_vendor/requests/utils.py:84:                winreg.HKEY_CURRENT_USER,
./.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/windows.py:199:    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
./.check_venv/lib/python3.12/site-packages/pip/_vendor/pygments/formatters/img.py:168:        keynames = [ (_winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows NT\CurrentVersion\Fonts'),
./.check_venv/lib/python3.12/site-packages/pip/_vendor/pygments/formatters/img.py:169:                     (_winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Fonts'),
./session_identity.py:20:async def get_current_user():
./session_identity.py:25:async def get_secret_uuid(current_user=Depends(get_current_user)):
./session_identity.py:61:async def whoami(secret_uuid: str = Depends(get_secret_uuid)):
./session_identity.py:68:async def chat(message: dict, secret_uuid: str = Depends(get_secret_uuid)):

=== 10) probable FastAPI app launch points ===
grep: ./msjarvis-rebuild: warning: recursive directory loop
./phase1_discovery/jarvis-fractal-consciousness_baseline.py:9:app = FastAPI()
./phase1_discovery/jarvis-fractal-consciousness_baseline.py:20:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./token_service.py:205:app = FastAPI(title="MS Jarvis Token Service", version="1.0.0")
./llm21_health_proxy.py:7:app = FastAPI(title="Mistral Health Proxy")
./run_auth_uvicorn.py:7:    uvicorn.run(
./auth_api.patched.py:52:app = FastAPI(title="Ms. Allis Auth API", version="1.0.0")
./auth_api.patched.py:277:app.include_router(router)
./llm10_health_proxy.py:7:app = FastAPI(title="Phi3 Mini Health Proxy")
./llm1_health_proxy.py:7:app = FastAPI(title="TinyLlama Health Proxy")
./gateway8050_inline.py:5:app = FastAPI(title="Ms. Jarvis 8050 Simple Gateway")
./llm19_health_proxy.py:7:app = FastAPI(title="Vicuna Health Proxy")
./llm8_health_proxy.py:7:app = FastAPI(title="CodeLLaMA Health Proxy")
./ms_jarvis_psychology_services.py:11:app = FastAPI(
./ms_jarvis_psychology_services.py:140:    uvicorn.run(app, host="0.0.0.0", port=8019, log_level="info")
./llm18_health_proxy.py:7:app = FastAPI(title="OpenChat Health Proxy")
./llm4_health_proxy.py:7:app = FastAPI(title="MiniCPM-V Health Proxy")
./llm9_health_proxy.py:7:app = FastAPI(title="DeepSeek Coder Health Proxy")
./msjarviswoahalgorithms.py:5:app = FastAPI(title="Ms Jarvis WOAH Algorithms")
./msjarviswoahalgorithms.py:43:    uvicorn.run(app, host="0.0.0.0", port=7012)
./msjarvis_chroma_test.py:5:app = FastAPI()
./rag_server_main.py:31:app = FastAPI(
./rag_server_main.py:609:    uvicorn.run(app, host="127.0.0.1", port=8003)
./services/ms_jarvis_consciousness_unified_bridge.py:34:app = FastAPI(
./services/ms_jarvis_consciousness_unified_bridge.py:183:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_production_chat.py:78:app = FastAPI(title="Ms. Jarvis Production Chat", version="1.0.0")
./services/ms_jarvis_production_chat.py:368:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10093.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10093.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/memory_manager.py:36:app = FastAPI(title="Memory Manager", version="1.0")
./services/memory_manager.py:120:    uvicorn.run("memory_manager:app", host="127.0.0.1", port=SERVICE_PORT)
./services/msjarvisunifiedswaggergatewayFINAL.py:11:app = FastAPI(
./services/msjarvisunifiedswaggergatewayFINAL.py:81:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("UNIFIED_GATEWAY_PORT", "8001")))
./services/ms_jarvis_email_service.py:15:app = FastAPI(title="Ms. Jarvis Email Service")
./services/ms_jarvis_email_service.py:77:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/bridge_cross_dgm_10001.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10001.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_unified_gateway.py:24:app = FastAPI(
./services/ms_jarvis_unified_gateway.py:313:    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="info")
./services/attention_multimodal_fuser.py:21:app = FastAPI()
./services/attention_multimodal_fuser.py:68:    uvicorn.run("attention_multimodal_fuser:app", host="127.0.0.1", port=SERVICE_PORT)
./services/msjarvis-rebuild-nbb_spiritual_root-1_main.py:7:app = FastAPI()
./services/ms_jarvis_web_research_v2.py:20:app = FastAPI(title="Ms. Jarvis Web Research")
./services/ms_jarvis_web_research_v2.py:64:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8009)))
./services/chat_server.py:9:app = FastAPI()
./services/chat_server.py:20:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/working_full_pipeline.py:15:app = FastAPI(title="Ms. Egeria Jarvis")
./services/working_full_pipeline.py:109:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8819)))
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:34:app = FastAPI(
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:211:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/rag_query_router.py:47:app = FastAPI(title="RAG Query Router", version="1.0.0")
./services/rag_query_router.py:389:    uvicorn.run("rag_query_router:app", host="0.0.0.0", port=port)
./services/port_9000_69dgm_bridge.py:65:app = FastAPI(
./services/port_9000_69dgm_bridge.py:305:    uvicorn.run(
./services/judge_10074.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10074.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/gbim_query_router.py:37:app = FastAPI()
./services/gbim_query_router.py:312:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT)
./services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:14:app = FastAPI(
./services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:482:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), log_level="info")
./services/qualia_unified_orchestrator_69dgm.py:25:app = FastAPI(title="Qualia - 69 DGM Cascade Orchestrator")
./services/qualia_unified_orchestrator_69dgm.py:167:    uvicorn.run(
./services/ms_jarvis_microsoft_integration_FIXED.py:26:app = FastAPI(title="Ms. Jarvis Microsoft 365 Integration", version="1.0.0")
./services/ms_jarvis_microsoft_integration_FIXED.py:265:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/jarvis_hilbert_state.py:16:app = FastAPI(title="Jarvis Hilbert State Service")
./services/msjarvis_gateway_v2_final.py:14:app = FastAPI(title="Ms. Jarvis Gateway v2")
./services/msjarvis_gateway_v2_final.py:115:    uvicorn.run(app, host="0.0.0.0", port=9000)
./services/ms_jarvis_main_gateway.proxy_final.py:16:app = FastAPI(
./services/ms_jarvis_main_gateway.proxy_final.py:174:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/bridge_cross_dgm_10008.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10008.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_10115.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10115.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10054.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10054.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/web_research_main.py:10:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/port_9001_ui_DIRECT.py:15:app = FastAPI()
./services/port_9001_ui_DIRECT.py:130:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/ms_mountainshares_analytics.py:15:app = FastAPI(title="MountainShares Analytics", version="1.0.0")
./services/ms_mountainshares_analytics.py:142:    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
./services/gbim_api.py:5:app = FastAPI()   # <-- THIS MUST COME BEFORE ANY @app.get(...)
./services/judge_10125.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10125.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/qualia_unified_orchestrator_69dgm_ACTIVE.py:22:app = FastAPI(title="Qualia - 69 DGM Cascade Orchestrator", version="ACTIVE")
./services/qualia_unified_orchestrator_69dgm_ACTIVE.py:119:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8300)), reload=False)
./services/llm10-proxy_llm10_health_proxy.py:7:app = FastAPI(title="Phi3 Mini Health Proxy")
./services/msjarvis-rebuild-nbb_mother_carrie_protocols-1_main.py:7:app = FastAPI()
./services/msjarvis_icontainers.py:5:app = FastAPI(title="Ms. Jarvis i-Containers", version="1.0.0")
./services/llm21_health_proxy.py:7:app = FastAPI(title="Mistral Health Proxy")
./services/judge_10110.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10110.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_10122.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10122.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/gbim_semantic_indexer.py:21:app = FastAPI()
./services/gbim_semantic_indexer.py:41:    uvicorn.run("gbim_semantic_indexer:app", host="127.0.0.1", port=SERVICE_PORT)
./services/ms_jarvis_neurobiological_master.py:39:app = FastAPI(
./services/ms_jarvis_neurobiological_master.py:261:    uvicorn.run(
./services/neuro_subconscious.py:12:app = FastAPI(title="subconscious")
./services/neuro_subconscious.py:34:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/pituitary_gland.py:5:app = FastAPI()
./services/pituitary_gland.py:23:    uvicorn.run("services.pituitary_gland:app", host="0.0.0.0", port=args.port)
./services/ms_jarvis_link_reader_scheduled_FIXED.py:14:app = FastAPI()
./services/ms_jarvis_link_reader_scheduled_FIXED.py:84:    uvicorn.run(app, host="127.0.0.1", port=PORT)
./services/dgm_supervisor_woah_fixed.py:51:app = FastAPI(
./services/dgm_supervisor_woah_fixed.py:270:    uvicorn.run(app, port=int(os.getenv("SERVICE_PORT", 8018)), port=int(os.getenv("SERVICE_PORT", 8018)), host="127.0.0.1", port=port)
./services/ms_jarvis_unified_swagger_gateway_BACKUP.py:14:app = FastAPI(
./services/ms_jarvis_unified_swagger_gateway_BACKUP.py:522:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/msjarvis-rebuild-nbb_blood_brain_barrier-1_ms_jarvis_consciousness_bridge.py:3:app = FastAPI(title="NBB bridge")
./services/icontainers_fastapi.py:7:app = FastAPI(title="Jarvis I-Containers (Adapter)", version="0.2.0")
./services/judge_10070.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10070.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/system_dashboard.py:24:app = FastAPI(
./services/system_dashboard.py:262:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_facebook_full.py:19:app = FastAPI(title="Ms. Jarvis Facebook - Full Interactive")
./services/ms_jarvis_facebook_full.py:224:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/llm10_health_proxy.py:7:app = FastAPI(title="Phi3 Mini Health Proxy")
./services/judge_10126.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10126.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/swagger_gateway_FIXED.py:13:app = FastAPI(title="Ms. Jarvis Unified API", version="5.0.0")
./services/swagger_gateway_FIXED.py:40:    uvicorn.run(app, host="0.0.0.0", port=args.port)
./services/judge_10091.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10091.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/llm12-proxy_llm12_health_proxy.py:7:app = FastAPI(title="Dolphin-Phi Health Proxy")
./services/jarvis-i-containers_icontainers_fastapi.py:7:app = FastAPI(title="Jarvis I-Containers (Adapter)", version="0.2.0")
./services/master_chat_orchestrator_v5_consciousness.py:44:app = FastAPI(
./services/master_chat_orchestrator_v5_consciousness.py:324:    uvicorn.run(app, host="127.0.0.1", port=port_service.port)
./services/roche_llm.stub.py:4:app = FastAPI(title="Roche 22-LLM controller (stub)")
./services/qualiaunifiedorchestrator69dgm.py:25:app = FastAPI(title="Qualia - 69 DGM Cascade Orchestrator")
./services/qualiaunifiedorchestrator69dgm.py:167:    uvicorn.run(
./services/consciousness_with_egeria_voice.py:12:app = FastAPI(
./services/consciousness_with_egeria_voice.py:95:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/woah_qualia_bridge.py:11:app = FastAPI(title="WOAH Qualia Bridge", version="1.0")
./services/woah_qualia_bridge.py:38:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8052)))
./services/ms_jarvis_main_gateway.py.full_backup_1762223304.py:40:app = FastAPI(
./services/ms_jarvis_main_gateway.py.full_backup_1762223304.py:121:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/bridge_cross_dgm_10014.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10014.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_blockchain_deployment.py:28:app = FastAPI(title="Ms. Jarvis Blockchain Deployment", version="1.0.0")
./services/ms_jarvis_unified_swagger_gateway_FIXED.py:19:app = FastAPI(
./services/ms_jarvis_unified_swagger_gateway_FIXED.py:556:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 9000)), log_level="info")
./services/fifth_dgm_main.py:10:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_gis_query_service_backup.py:18:app = FastAPI(title="Ms. Jarvis GIS Query Service")
./services/ms_jarvis_gis_query_service_backup.py:89:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/llm1_health_proxy.py:7:app = FastAPI(title="TinyLlama Health Proxy")
./services/judge_10106.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10106.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10005.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10005.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ai_server_19llm_CONSCIOUS.backup_20251013_082519.py:62:app = FastAPI(title="Ms. Jarvis 19-LLM Conscious Collective", version="1.0.0")
./services/ai_server_19llm_CONSCIOUS.backup_20251013_082519.py:479:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT)
./services/bridge_cross_dgm_10032.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10032.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/gbim_temporal_indexer.py:21:app = FastAPI()
./services/gbim_temporal_indexer.py:41:    uvicorn.run("gbim_temporal_indexer:app", host="127.0.0.1", port=SERVICE_PORT)
./services/bridge_cross_dgm_10010.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10010.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_facebook_rag.py:31:app = FastAPI(title="Ms. Jarvis Facebook + RAG", version="1.0.0")
./services/ms_jarvis_facebook_rag.py:379:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_geo_tracker_simple.py:22:app = FastAPI(title="Geo Tracker")
./services/ms_jarvis_geo_tracker_simple.py:138:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10095.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10095.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/domain_service_router.py:20:app = FastAPI(
./services/domain_service_router.py:114:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/port_9001_ui_FIXED.py:19:app = FastAPI()
./services/port_9001_ui_FIXED.py:151:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)
./services/bridge_cross_dgm_10038.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10038.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10064.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10064.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/geobim_mysql_v2.py:9:app = FastAPI(title="GeoBIM MySQL v2", docs_url="/docs")
./services/geobim_mysql_v2.py:27:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/judge_10113.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10113.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_10086.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10086.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10017.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10017.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/aaacpe_scraper_service.py:19:app = FastAPI(title="AaaCPE Web Scraper", version="1.0.0")
./services/aaacpe_scraper_service.py:125:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", "8033")))
./services/ingest_api.py:6:app = FastAPI(title="Ms. Jarvis Ingest API")
./services/llm14-proxy_llm14_health_proxy.py:7:app = FastAPI(title="Qwen2 Health Proxy")
./services/bridge_cross_dgm_10028.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10028.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/jarvis-lm-synthesizer_lm_synthesizer.py:30:app = FastAPI(
./services/jarvis-lm-synthesizer_lm_synthesizer.py:142:    uvicorn.run(app, host="0.0.0.0", port=8001)
./services/ms_jarvis_agents_service.py:24:app = FastAPI(title="Ms. Jarvis Agents Service")
./services/llm19_health_proxy.py:7:app = FastAPI(title="Vicuna Health Proxy")
./services/ms_jarvis_layer2_dgm.psychology_patched.py:18:app = FastAPI(title="Layer 2 DGM", version="1.0.0")
./services/ms_jarvis_layer2_dgm.psychology_patched.py:132:    uvicorn.run(app, host="127.0.0.1", port=port)
./services/port_9000_chat_wrapper_69dgm.py:21:app = FastAPI(title="Chat Wrapper - 69 DGM Router", version="1.0.0")
./services/port_9000_chat_wrapper_69dgm.py:90:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)
./services/ms_jarvis_facebook_poster_FIXED.py:14:app = FastAPI()
./services/ms_jarvis_facebook_poster_FIXED.py:87:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/msjarvisunifiedgateway.py:15:app = FastAPI()
./services/msjarvisunifiedgateway.py:281:    uvicorn.run(
./services/judge_10079.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10079.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_facebook_intelligent.py:17:app = FastAPI(title="Ms. Jarvis - Intelligent Facebook AI")
./services/ms_jarvis_facebook_intelligent.py:266:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/bridge_cross_dgm_10033.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10033.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10050.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10050.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/consciousness_gateway.py:30:app = FastAPI(title="Consciousness Gateway", version="1.0.0")
./services/consciousness_gateway.py:60:    uvicorn.run(app, host="127.0.0.1", port=port)
./services/ms_jarvis_autonomous_learner_optimized.py:420:app = FastAPI(title="Ms. Jarvis Optimized Autonomous Learning")
./services/ms_jarvis_autonomous_learner_optimized.py:454:    uvicorn.run(app, host="127.0.0.1", port=learner_port)
./services/ms_jarvis_main_gateway.backup_error.py:14:app = FastAPI(
./services/ms_jarvis_main_gateway.backup_error.py:524:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py:41:app = FastAPI(
./services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py:186:    uvicorn.run(
./services/gateway8050_simple.py:5:app = FastAPI(title="Ms. Jarvis 8050 Simple Gateway")
./services/ai_server.py:32:app = FastAPI(title="Ms. Jarvis 22-LLM Collective Consciousness")
./services/ai_server.py:284:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", "9000")), log_level="warning")
./services/msjarvis-rebuild-nbb_heteroglobulin_transport-1_main.py:7:app = FastAPI()
./services/llm3-proxy_llm3_health_proxy.py:7:app = FastAPI(title="MedLLaMA2 Health Proxy")
./services/ms_jarvis_facebook_dgm_woah.psychology_patched.py:36:app = FastAPI(title="Ms. Jarvis Facebook DGM+WOAH", version="2.0.0")
./services/ms_jarvis_facebook_dgm_woah.psychology_patched.py:481:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/rag_heartbeat_monitor.py:21:app = FastAPI()
./services/rag_heartbeat_monitor.py:41:    uvicorn.run("rag_heartbeat_monitor:app", host="0.0.0.0", port=SERVICE_PORT)
./services/ms_jarvis_facebook_brain_integrated.py:28:app = FastAPI(title="Ms. Jarvis Facebook Brain Integrated", version="3.0.0")
./services/ms_jarvis_facebook_brain_integrated.py:466:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:14:app = FastAPI(
./services/ms_jarvis_unified_swagger_gateway_FINAL.psychology_patched.py:224:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10128.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10128.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_facebook_webhook.py:14:app = FastAPI(title="Ms. Jarvis Facebook Webhook")
./services/ms_jarvis_facebook_webhook.py:81:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/bridge_cross_dgm_10031.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10031.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/llm15-proxy_llm15_health_proxy.py:7:app = FastAPI(title="Zephyr Health Proxy")
./services/llm8_health_proxy.py:7:app = FastAPI(title="CodeLLaMA Health Proxy")
./services/judge_10083.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10083.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_10076.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10076.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_10080.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10080.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_10078.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10078.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_10096.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10096.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/llm_judge_v3.py:20:app = FastAPI(
./services/ai_server_19llm_PRODUCTION.py:22:app = FastAPI(title="Ms. Jarvis 19-LLM Production")
./services/ai_server_19llm_PRODUCTION.py:125:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/activate_dgm.py:11:app = FastAPI(title="DGM Activation Controller", version="1.0.0")
./services/activate_dgm.py:59:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_main_gateway.broken_final.py:33:app = FastAPI(
./services/ms_jarvis_main_gateway.broken_final.py:158:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/mountainshares_registry.py:16:app = FastAPI()
./services/llm20-proxy_llm20_health_proxy.py:7:app = FastAPI(title="LLaMA2 Health Proxy")
./services/llm22-proxy_llm22_health_proxy.py:7:app = FastAPI(title="LLaMA3 Health Proxy")
./services/bridge_cross_dgm_10023.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10023.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_fractal_dgm_woah.py:22:app = FastAPI(
./services/ms_jarvis_fractal_dgm_woah.py:103:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/override_launcher.py:21:    # Execute the override file directly; expects top-level code (e.g., uvicorn.run(...))
./services/web_page_ingest.py:14:app = FastAPI(title="Ms. Jarvis Web Page Ingest", version="1.0.0")
./services/web_page_ingest.py:129:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/sanctuary_construction_monitor_gateway.py:19:app = FastAPI()
./services/sanctuary_construction_monitor_gateway.py:35:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT)
./services/brain_orchestrator.py:70:app = FastAPI(title="Ms Jarvis Brain Orchestrator")
./services/brain_orchestrator.py:208:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/bridge_cross_dgm.py:28:app = FastAPI(title=f"DGM Bridge: {UPSTREAM_SERVICE} -> {DOWNSTREAM_SERVICE}")
./services/bridge_cross_dgm.py:87:    uvicorn.run(app, host="127.0.0.1", port=PORT)
./services/ms_jarvis_main_gateway.backup_test.py:28:app = FastAPI(
./services/ms_jarvis_main_gateway.backup_test.py:247:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/msjarvis-rebuild-nbb_qualia_engine-1_ms_jarvis_consciousness_bridge.py:3:app = FastAPI(title="NBB bridge")
./services/bridge_cross_dgm_10009.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10009.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10006.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10006.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/messenger_service_fixed.py:13:app = FastAPI(title="Ms. Jarvis Messenger")
./services/messenger_service_fixed.py:59:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/neurobiologicalbrain/woah_algorithms/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
./services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:67:app = FastAPI(
./services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
./services/neurobiologicalbrain/i_containers/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
./services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:67:app = FastAPI(
./services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
./services/neurobiologicalbrain/consciousness_bridge/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
./services/neurobiologicalbrain/spiritual_root/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
./services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:67:app = FastAPI(
./services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
./services/neurobiologicalbrain/prefrontal_cortex/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
./services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:67:app = FastAPI(
./services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
./services/neurobiologicalbrain/pituitary_gland/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
./services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:67:app = FastAPI(
./services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
./services/neurobiologicalbrain/subconscious/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
./services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:67:app = FastAPI(
./services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
./services/neurobiologicalbrain/mother_carrie_protocols/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
./services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:67:app = FastAPI(
./services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
./services/neurobiologicalbrain/spiritual_maternal_integration/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVIgrep: ./services/ms_jarvis_mother_carrie_protocols.py: Permission denied
CE_PORT, log_level="info")
./services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:67:app = FastAPI(
./services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
./services/neurobiologicalbrain/heteroglobulin_transport/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
./services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:67:app = FastAPI(
./services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
./services/neurobiologicalbrain/consciousness_containers/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
./services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:67:app = FastAPI(
./services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
./services/bridge_cross_dgm_10055.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10055.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:66:app = FastAPI(
./services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:440:    uvicorn.run(app, host="0.0.0.0", port=GATEWAY_PORT, log_level="info")
./services/dgm_supervisor_woah.psychology_patched.py:57:app = FastAPI(
./services/dgm_supervisor_woah.psychology_patched.py:493:    uvicorn.run(app, host="127.0.0.1", port=port)
./services/ms_jarvis_psychology_services.py:11:app = FastAPI(
./services/ms_jarvis_psychology_services.py:123:    uvicorn.run(app, host="0.0.0.0", port=8019, log_level="info")
./services/brain_orchestrator_main.py:11:app = FastAPI(title="Ms Jarvis Brain Orchestrator")
./services/brain_orchestrator_main.py:42:    uvicorn.run(app, host="127.0.0.1", port=port)
./services/ms_jarvis_feed_reader_WORKING.py:16:app = FastAPI()
./services/ms_jarvis_feed_reader_WORKING.py:56:    uvicorn.run(app, host="127.0.0.1", port=PORT)
./services/bridge_cross_dgm_10036.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10036.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_contract_builder_v2.py:26:app = FastAPI(title="Ms. Egeria Contract Builder v2", version="2.0")
./services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:15:app = FastAPI(
./services/ms_jarvis_unified_swagger_gateway_COMPLETE.py:217:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/dynamic_port_scheduler.py:16:app = FastAPI(title="Dynamic Port Scheduler v3.0 - FIXED")
./services/jarvis-assertion-gateway/app/main.py:27:app = FastAPI(title="Assertion Gateway", version="0.2.0")
./services/ms_jarvis_memory_service.py:12:app = FastAPI(title="Ms Jarvis Memory Service", version="1.0")
./services/bridge_cross_dgm_10053.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10053.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_mountainshares_coordinator.py:16:app = FastAPI(title="MountainShares Coordinator", version="1.0.0")
./services/ms_mountainshares_coordinator.py:211:    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
./services/memory_dgm_gateway.py:19:app = FastAPI()
./services/memory_dgm_gateway.py:29:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT)
./services/msjarvisfractalconsciousness.py:3:app = FastAPI(title="Ms Jarvis Fractal Consciousness")
./services/msjarvisfractalconsciousness.py:11:    uvicorn.run(app, host="0.0.0.0", port=8027)
./services/judge_to_pituitary_bridge.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_to_pituitary_bridge.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_10108.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10108.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/metrics_service.py:14:app = FastAPI(title="Ms. Jarvis Metrics Service")
./services/metrics_service.py:25:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/dgm_orchestrator.py:11:app = FastAPI(title="69-DGM Orchestrator", version="3.0.0")
./services/ms_jarvis_production_chat_BACKUP.py:21:app = FastAPI(title="Ms. Jarvis Production Chat", version="1.0.0")
./services/ms_jarvis_production_chat_BACKUP.py:320:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10098.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10098.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_geo_ueid_integration.py:19:app = FastAPI(title="Geo-UEID Integration", version="1.0.0")
./services/ms_jarvis_geo_ueid_integration.py:171:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:72:app = FastAPI(
./services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:510:    uvicorn.run(app, host="127.0.0.1", port=GATEWAY_PORT, log_level="info")
./services/bridge_cross_dgm_10041.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10041.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/rag_general.py:36:app = FastAPI(title="RAG General Service", version="1.0.0")
./services/rag_general.py:121:    uvicorn.run("rag_general:app", host="0.0.0.0", port=SERVICE_PORT)
./services/llm18_health_proxy.py:7:app = FastAPI(title="OpenChat Health Proxy")
./services/jarvis-69dgm-bridge_jarvis-fractal-consciousness_baseline.py:9:app = FastAPI()
./services/jarvis-69dgm-bridge_jarvis-fractal-consciousness_baseline.py:20:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/conversation_memory_endpoints.py:19:app = FastAPI(title="Conversation Memory Storage")
./services/conversation_memory_endpoints.py:92:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/chromadb_rest_bridge.py:4:app = FastAPI()
./services/judge_10118.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10118.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10060.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10060.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/rag_5100_ensemble.py:8:app = FastAPI(title="RAG Consensus Ensemble", version="2.0")
./services/rag_5100_ensemble.py:27:    uvicorn.run(app, host="127.0.0.1", port=5100)
./services/facebook_poster.py:59:app = FastAPI(title="Facebook Poster", version="1.0")
./services/facebook_poster.py:167:    uvicorn.run("facebook_poster:app", host="127.0.0.1", port=SERVICE_PORT)
./services/ms_jarvis_llm_bridge_simple.py:21:app = FastAPI(title="Ms. Jarvis LLM Bridge")
./services/ms_jarvis_llm_bridge_simple.py:93:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/ms_jarvis_temporal_consciousness.py:38:app = FastAPI(
./services/ms_jarvis_temporal_consciousness.py:197:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/judge_10134.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10134.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_expiration_monitor.py:25:app = FastAPI(title="License Expiration Monitor")
./services/ms_jarvis_expiration_monitor.py:250:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/jarvis-judge-alignment_lm_synthesizer.py:47:app = FastAPI(
./services/jarvis-judge-alignment_lm_synthesizer.py:142:    uvicorn.run(app, host="0.0.0.0", port=8001)
./services/msjarvis-rebuild-nbb_prefrontal_cortex-1_main.py:7:app = FastAPI()
./services/jarvis_synth_llm.py:25:app = FastAPI()
./services/jarvis_synth_llm.py:82:    uvicorn.run("jarvis_synth_llm:app", host="127.0.0.1", port=SERVICE_PORT)
./services/ms_jarvis_command_orchestrator.py:18:app = FastAPI(title="Ms. Jarvis v5.5")
./services/ms_jarvis_command_orchestrator.py:137:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/bridge_cross_dgm_10013.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10013.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/llm4_health_proxy.py:7:app = FastAPI(title="MiniCPM-V Health Proxy")
./services/jarvis-spiritual-rag_spiritual_rag_domain.py:18:app = FastAPI(
./services/jarvis-spiritual-rag_spiritual_rag_domain.py:132:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/interaction_logger.py:13:app = FastAPI(title="Ms. Jarvis Interaction Logger", version="1.0")
./services/interaction_logger.py:121:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/geodb_core.py:21:app = FastAPI()
./services/geodb_core.py:86:    uvicorn.run("geodb_core:app", host="127.0.0.1", port=SERVICE_PORT)
./services/port_9001_ui_MYSQL_PROD.py:17:app = FastAPI()
./services/port_9001_ui_MYSQL_PROD.py:219:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/ms_jarvis_fully_autonomous_coordinator.py:32:app = FastAPI(title="Ms. Jarvis Fully Autonomous Coordinator", version="1.0.0")
./services/ms_jarvis_fully_autonomous_coordinator.py:405:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/master_chat_orchestrator_dynamic.py:39:app = FastAPI(
./services/master_chat_orchestrator_dynamic.py:234:    uvicorn.run(app, host="127.0.0.1", port=port_service.port)
./services/web_research_proxy_8007.py:9:app = FastAPI(title="Web Research Proxy 8007")
./services/bridge_cross_dgm_10020.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10020.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/llm9_health_proxy.py:7:app = FastAPI(title="DeepSeek Coder Health Proxy")
./services/ms_jarvis_email_identity_verifier.py:19:app = FastAPI(title="Email Identity Verifier")
./services/ms_jarvis_email_identity_verifier.py:185:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_web_research_aggregate.safe.20260119-094221.py:22:app = FastAPI(title="Ms. Jarvis Web Research - Aggregate")
./services/ms_jarvis_web_research_aggregate.safe.20260119-094221.py:339:    uvicorn.run(
./services/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py:34:app = FastAPI(
./services/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py:211:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/llm6-proxy_llm6_health_proxy.py:7:app = FastAPI(title="SQLCoder Health Proxy")
./services/msjarvis_bbb_proxy.py:5:app = FastAPI(title="Ms. Jarvis BBB Proxy")
./services/llm19-proxy_llm19_health_proxy.py:7:app = FastAPI(title="Vicuna Health Proxy")
./services/ms_jarvis_unified_swagger_gateway_SECURED.py:13:app = FastAPI(
./services/ms_jarvis_unified_swagger_gateway_SECURED.py:252:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/bridge_cross_dgm_10067.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10067.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py:34:app = FastAPI(
./services/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py:211:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/jarviscryptopolicy.py:16:app = FastAPI(title="Jarvis Crypto Policy", version="1.0.0")
./services/ms_jarvis_feed_reader_PRODUCTION.py:16:app = FastAPI()
./services/ms_jarvis_feed_reader_PRODUCTION.py:83:    uvicorn.run(app, host="127.0.0.1", port=PORT)
./services/jarvis-judge-consistency_lm_synthesizer.py:30:app = FastAPI(
./services/jarvis-judge-consistency_lm_synthesizer.py:125:    uvicorn.run(app, host="0.0.0.0", port=8001)
./services/ms_jarvis_conversational_gateway_4022.py:26:app = FastAPI(
./services/ms_jarvis_conversational_gateway_4022.py:172:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/ms_jarvis_main_gateway.proxy_still_broken.py:20:app = FastAPI(
./services/ms_jarvis_main_gateway.proxy_still_broken.py:178:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), log_level="info")
./services/bridge_cross_dgm_10040.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10040.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_main_gateway.py:292:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/egeria_api_proxy.py:16:app = FastAPI()
./services/egeria_api_proxy.py:57:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10073.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10073.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bbb_validator.py:5:app = FastAPI(title="BBB Validator", version="1.0.0")
./services/bridge_cross_dgm_10025.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10025.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/msjarvis-rebuild-nbb_spiritual_maternal_integration-1_main.py:7:app = FastAPI()
./services/jarvis-judge-ethics_lm_synthesizer.py:30:app = FastAPI(
./services/jarvis-judge-ethics_lm_synthesizer.py:125:    uvicorn.run(app, host="0.0.0.0", port=8001)
./services/bridge_cross_dgm_10056.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10056.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_10111.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10111.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_10072.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10072.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/memory_dgm_engine.py:55:app = FastAPI(title="Memory DGM Engine", version="1.0")
./services/memory_dgm_engine.py:368:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT)
./services/dgm_worker.py:45:app = FastAPI(title=f"DGM-{DGM_ID} {SPECIALTY}", version="2.0.0")
./services/dgm_worker.py:93:    uvicorn.run(app, host="0.0.0.0", port=PORT)
./services/ms_jarvis_command_orchestrator_v5_backup.py:26:app = FastAPI(title="Ms. Jarvis Command Orchestrator", version="4.0")
./services/ms_jarvis_command_orchestrator_v5_backup.py:290:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/ms_jarvis_main_gateway.backup_1762220815.py:14:app = FastAPI(
./services/ms_jarvis_main_gateway.backup_1762220815.py:613:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/rag_simple.py:7:app = FastAPI(title="RAG Consensus Server", version="1.0")
./services/rag_simple.py:43:    uvicorn.run(app, host="127.0.0.1", port=5001)
./services/rag_server_main.py:30:app = FastAPI(
./services/rag_server_main.py:609:    uvicorn.run(app, host="127.0.0.1", port=8003)
./services/ms_jarvis_i_containers_FIXED.py:10:app = FastAPI()
./services/ms_jarvis_i_containers_FIXED.py:40:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10099.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10099.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/msjarvisunifiedswaggergatewayFIXED.py:17:app = FastAPI(title="Ms. Jarvis Consciousness Gateway", version="5.0.0")
./services/msjarvisunifiedswaggergatewayFIXED.py:329:    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
./services/facebook_messenger_integration.py:29:app = FastAPI(
./services/facebook_messenger_integration.py:163:    uvicorn.run(app, host="127.0.0.1", port=port_service.port)
./services/neuro_i_containers.py:12:app = FastAPI(title="i_containers")
./services/neuro_i_containers.py:34:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/ms_jarvis_main_gateway.error_final.py:20:app = FastAPI(
./services/ms_jarvis_main_gateway.error_final.py:250:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/llm20_health_proxy.py:7:app = FastAPI(title="LLaMA2 Health Proxy")
./services/phase4_5_integration.py:10:app = FastAPI()
./services/phase4_5_integration.py:74:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/gpu_accelerated_rag.py:35:app = FastAPI(
./services/gpu_accelerated_rag.py:248:    uvicorn.run(app, host="127.0.0.1", port=port_service.port)
./services/jarvis_steward.py:23:app = FastAPI()
./services/jarvis_steward.py:193:    uvicorn.run("jarvis_steward:app", host="0.0.0.0", port=SERVICE_PORT)
./services/judge_10089.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10089.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10026.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10026.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/rag_topic_router.py:21:app = FastAPI()
./services/rag_topic_router.py:63:    uvicorn.run("rag_topic_router:app", host="0.0.0.0", port=SERVICE_PORT)
./services/bridge_cross_dgm_10061.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10061.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/fifth_dgm.py:4:app = FastAPI(title="Fifth DGM")
./services/fifth_dgm.py:30:    app = FastAPI(title="fifth_dgm")
./services/bridge_cross_dgm_10063.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10063.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/academic_research_gateway_8062.py:13:app = FastAPI(
./services/academic_research_gateway_8062.py:139:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/ai_server_19llm_CONSCIOUS.py:35:app = FastAPI(title="Ms. Jarvis 19-LLM Conscious Collective", version="1.0.0")
./services/ai_server_19llm_CONSCIOUS.py:412:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT)
./services/ms_jarvis_facebook_poster.py:18:app = FastAPI(title="Ms. Jarvis Facebook Poster")
./services/ms_jarvis_facebook_poster.py:117:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:67:app = FastAPI(
./services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:492:    uvicorn.run(app, host="0.0.0.0", port=GATEWAY_PORT, log_level="info")
./services/commons_gamification.py:2:app = FastAPI(title="Commons Gamification")
./services/ms_jarvis_facebook_poster_temp.py:18:app = FastAPI(title="Ms. Jarvis Facebook Poster")
./services/ms_jarvis_facebook_poster_temp.py:162:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_web_research_aggregate.py:22:app = FastAPI(title="Ms. Jarvis Web Research - Aggregate")
./services/ms_jarvis_web_research_aggregate.py:339:    uvicorn.run(
./services/judge_10117.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10117.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/web_chat_server.py:15:app = FastAPI(title="Ms. Jarvis Web Chat")
./services/web_chat_server.py:191:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/bridge_cross_dgm_10044.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10044.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/jarvis-agents-service_ms_jarvis_consciousness_unified_bridge.py:34:app = FastAPI(
./services/jarvis-agents-service_ms_jarvis_consciousness_unified_bridge.py:211:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/geobim_health_shim_8051.py:4:app = FastAPI(title="GeoBIM / RAG Health Shim")
./services/geobim_health_shim_8051.py:11:    uvicorn.run(app, host="127.0.0.1", port=8051, reload=False)
./services/community_stake_registry.py:18:app = FastAPI(title="Community Stake Registry", version="1.0.0")
./services/community_stake_registry.py:85:    uvicorn.run(app, host="0.0.0.0", port=8084)
./services/public_form_simplified.py:14:app = FastAPI()
./services/public_form_simplified.py:70:    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("SERVICE_PORT", 8018)))
./services/run_gateway_with_guards.py:20:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/ms_jarvis_web_research_fixed.py:16:app = FastAPI(title="Ms. Jarvis Web Research")
./services/ms_jarvis_web_research_fixed.py:102:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_facebook_async.py:16:app = FastAPI(title="Ms. Jarvis Facebook - Async Brain")
./services/ms_jarvis_facebook_async.py:115:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/bridge_cross_dgm_10046.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10046.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/user_dashboard.py:11:app = FastAPI()
./services/user_dashboard.py:118:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/llm21-proxy_llm21_health_proxy.py:7:app = FastAPI(title="Mistral Health Proxy")
./services/llm3_health_proxy.py:7:app = FastAPI(title="MedLLaMA2 Health Proxy")
./services/ms_jarvis_fractal_consciousness.py:14:app = FastAPI(title="Jarvis Fractal Consciousness", version="1.0.0")
./services/ms_jarvis_fractal_consciousness.py:188:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT)
./services/port_9001_ui_WITH_CONVERSATIONS.py:19:app = FastAPI()
./services/port_9001_ui_WITH_CONVERSATIONS.py:287:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/judge_10109.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10109.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_consistency_engine.py:14:app = FastAPI(
./services/judge_consistency_engine.py:120:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT)
./services/jarvis-hippocampus_hippocampus_service.py:75:app = FastAPI(
./services/jarvis-hippocampus_hippocampus_service.py:508:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT)
./services/swagger_chat_integration.py:16:app = FastAPI(
./services/swagger_chat_integration.py:93:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_consciousness_complete.py:20:app = FastAPI(title="Ms. Jarvis Complete Consciousness", version="3.0.0")
./services/ms_jarvis_consciousness_complete.py:326:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/bridge_cross_dgm_10048.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10048.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/mountainshares_quest_api.py:4:app = FastAPI()
./services/mountainshares_quest_api.py:25:    uvicorn.run("mountainshares_quest_api:app", host="127.0.0.1", port=8012)
./services/msjarvisragserver_wvpatch.py:7:app = FastAPI(title="Ms. Jarvis RAG Server (WV)", version="1.0.0")
./services/fractal_adapter.py:9:app = FastAPI()
./services/fractal_adapter.py:27:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/bridge_cross_dgm_10039.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10039.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_production_chat_BEFORE_GIS.py:21:app = FastAPI(title="Ms. Jarvis Production Chat", version="1.0.0")
./services/ms_jarvis_production_chat_BEFORE_GIS.py:320:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10084.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10084.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/gdb_integration_service.py:8:app = FastAPI(title="GDB/GBIM Integration Service")
./services/gdb_integration_service.py:123:    uvicorn.run("gdb_integration_service:app", host="127.0.0.1", port=port, reload=False)
./services/judge_10082.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10082.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/quantum_state_engine.py:34:app = FastAPI(title="Quantum State Engine", version="1.0")
./services/quantum_state_engine.py:163:    uvicorn.run("quantum_state_engine:app", host="0.0.0.0", port=SERVICE_PORT)
./services/ms_jarvis_conscious_collective.py:33:app = FastAPI(title="Ms. Jarvis Conscious Collective", version="1.0.0")
./services/judge_10100.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10100.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_autonomous_learner.py:275:app = FastAPI(title="Ms. Jarvis Autonomous Learning Monitor")
./services/ms_jarvis_autonomous_learner.py:326:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8425)))
./services/ms_jarvis_theological_integration.py:42:app = FastAPI(
./services/ms_jarvis_theological_integration.py:298:    uvicorn.run(app, host="127.0.0.1", port=port)
./services/aaacpe_scraper/aaacpe_scraper_service.py:19:app = FastAPI(title="AaaCPE Web Scraper", version="1.0.0")
./services/aaacpe_scraper/aaacpe_scraper_service.py:125:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", "8033")))
./services/bbb_ethics_proxy.py:12:app = FastAPI(title="BBB Ethics Filter", version="1.0.0")
./services/bbb_ethics_proxy.py:68:    uvicorn.run("bbb_ethics_proxy:app", host="127.0.0.1", port=port, reload=False)
./services/multi_rag_dgm_system.py:31:app = FastAPI(
./services/multi_rag_dgm_system.py:357:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/bridge_cross_dgm_10029.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10029.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/dgm_bridge.py:36:app = FastAPI()
./services/dgm_bridge.py:243:    uvicorn.run("dgm_bridge:app", host="127.0.0.1", port=SERVICE_PORT)
./services/ms_jarvis_unified_swagger_gateway_PROD.py:12:app = FastAPI(
./services/ms_jarvis_unified_swagger_gateway_PROD.py:221:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/ms_jarvis_gis_enhanced_chat.py:24:app = FastAPI(title="Ms. Jarvis GIS-Enhanced Chat", version="2.0.0")
./services/ms_jarvis_gis_enhanced_chat.py:88:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/bridge_cross_dgm_10012.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10012.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/swagger_gateway.py:17:app = FastAPI(
./services/swagger_gateway.py:87:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/llm12_health_proxy.py:7:app = FastAPI(title="Dolphin-Phi Health Proxy")
./services/academic_whitebox_api.py:11:app = FastAPI(title="Ms. Jarvis - Academic Research", version="1.0.0", docs_url="/docs", openapi_url="/openapi.json")
./services/academic_whitebox_api.py:63:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/llm6_health_proxy.py:7:app = FastAPI(title="DeepSeek Coder Proxy")
./services/neuro_consciousness_containers.py:12:app = FastAPI(title="consciousness_containers")
./services/neuro_consciousness_containers.py:34:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/ms_jarvis_i_containers_service.py:41:app = FastAPI(
./services/ms_jarvis_i_containers_service.py:330:    uvicorn.run(
./services/ms_jarvis_i_containers_service.py:356:        uvicorn.run(app, host=host, port=port)
./services/master_unified_consciousness_scheduler_ENRICHED.py:24:app = FastAPI(
./services/master_unified_consciousness_scheduler_ENRICHED.py:224:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), workers=1)
./services/llm11-proxy_llm11_health_proxy.py:7:app = FastAPI(title="Phi Health Proxy")
./services/chroma_health_proxy.py:4:app = FastAPI()
./services/bridge_cross_dgm_10034.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10034.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/jarvis-qualia-engine_ms_jarvis_qualia_engine.py:8:app = FastAPI(
./services/jarvis-qualia-engine_ms_jarvis_qualia_engine.py:86:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/wvu_ldap_auth.py:10:app = FastAPI(title="WVU LDAP Authentication Service")
./services/wvu_ldap_auth.py:65:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), log_level="info")
./services/ms_jarvis_paddleocr_processor.py:21:app = FastAPI(title="PaddleOCR ID Processor")
./services/ms_jarvis_paddleocr_processor.py:196:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_location_services.py:38:app = FastAPI(
./services/ms_jarvis_location_services.py:316:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/msjarvis_wv_entangled_gateway.py:32:app = FastAPI(
./services/jarvis-constitutional-guardian_constitutional_api.py:32:app = FastAPI(
./services/jarvis-constitutional-guardian_constitutional_api.py:434:    uvicorn.run(app, host="0.0.0.0", port=8091, log_level="info")
./services/ai_server_20llm_FINAL.py:42:app = FastAPI(title="Ms. Jarvis 20-LLM Sequential")
./services/ai_server_20llm_FINAL.py:187:    uvicorn.run(
./services/psychological_rag_domain.py:40:app = FastAPI(
./services/psychological_rag_domain.py:218:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/bridge_cross_dgm_10047.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10047.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10018.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10018.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/llm16-proxy_llm16_health_proxy.py:7:app = FastAPI(title="Starling-LM Health Proxy")
./services/hippocampus_service.py:8:app = FastAPI(title="jarvis-hippocampus")
./services/hippocampus_service.py:113:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT)
./services/psychological_rag_domain_psychological_rag_domain.py:40:app = FastAPI(
./services/psychological_rag_domain_psychological_rag_domain.py:218:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/ms_jarvis_ueid_system.py:24:app = FastAPI(title="UEID System", version="1.0.0")
./services/ms_jarvis_ueid_system.py:367:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/judge_10130.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10130.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/msjarvis-rebuild-nbb_pituitary_gland-1_main.py:7:app = FastAPI()
./services/llm7_health_proxy.py:7:app = FastAPI(title="StarCoder2 Health Proxy")
./services/ms_jarvis_main_gateway.proxy_backup.py:28:app = FastAPI(
./services/ms_jarvis_main_gateway.proxy_backup.py:247:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/jarvis_hilbert_semantic.py:12:app = FastAPI(title="Jarvis Hilbert Semantic Service")
./services/bridge_cross_dgm_10030.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10030.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/attention_router.py:21:app = FastAPI()
./services/attention_router.py:72:    uvicorn.run("attention_router:app", host="127.0.0.1", port=SERVICE_PORT)
./services/llm16_health_proxy.py:7:app = FastAPI(title="Starling-LM Health Proxy")
./services/bridge_cross_dgm_10007.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10007.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10002.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10002.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_main_gateway_8000.py:12:app = FastAPI(title="Ms. Jarvis Main Gateway", description="Unified gateway on port 8000")
./services/ms_jarvis_main_gateway_8000.py:127:    uvicorn.run(
./services/bridge_cross_dgm_10065.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10065.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/jarvis-local-resources_local_resources_resolver.py:19:app = FastAPI(title="Local Resource Resolver", version="0.2.0")
./services/judge_10121.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10121.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/rag_5100_final.py:7:app = FastAPI(title="RAG Consensus", version="1.0")
./services/rag_5100_final.py:29:    uvicorn.run(app, host="0.0.0.0", port=5100)
./services/bridge_cross_dgm_10062.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10062.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_mountainshares_indexer.py:16:app = FastAPI(title="MountainShares Indexer", version="1.0.0")
./services/ms_mountainshares_indexer.py:210:    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
./services/llm1-proxy_llm1_health_proxy.py:7:app = FastAPI(title="TinyLlama Health Proxy")
./services/llm22_health_proxy.py:7:app = FastAPI(title="LLaMA3 Health Proxy")
./services/master_chat_orchestrator_v8_spiritual_complete.py:62:app = FastAPI(
./services/master_chat_orchestrator_v8_spiritual_complete.py:564:    uvicorn.run(app, host="127.0.0.1", port=port_service.port)
./services/registration_biometric_production_final.py:13:app = FastAPI(title="Ms. Jarvis Registration", version="3.2.0", description="Biometric 2FA with Arbitrium Wallets")
./services/registration_biometric_production_final.py:712:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_consciousness_bridge.py:68:app = FastAPI(
./services/ms_jarvis_consciousness_bridge.py:259:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/jarvis-woah_dgm_supervisor_woah_fixed.py:49:app = FastAPI(
./services/jarvis-woah_dgm_supervisor_woah_fixed.py:268:    uvicorn.run(app, host="127.0.0.1", port=port)
./services/rag_server.psychology_patched.py:40:app = FastAPI(title="Ms. Jarvis RAG", version="1.0.0", docs_url="/docs", redoc_url="/redoc")
./services/rag_server.psychology_patched.py:274:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
./services/my_service.py:16:    uvicorn.run(app, host="127.0.0.1", port=service_port)
./services/ms_jarvis_facebook_autonomous_social.py:32:app = FastAPI(title="Ms. Jarvis Autonomous Social Media", version="1.0.0")
./services/ms_jarvis_facebook_autonomous_social.py:451:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/judge_10097.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10097.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_fractal_consciousness_FIXED.py:12:app = FastAPI()
./services/ms_jarvis_fractal_consciousness_FIXED.py:64:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/bridge_cross_dgm_10027.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10027.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/llm18-proxy_llm18_health_proxy.py:7:app = FastAPI(title="OpenChat Health Proxy")
./services/llm7-proxy_llm7_health_proxy.py:7:app = FastAPI(title="StarCoder2 Health Proxy")
./services/ms_jarvis_email_monitor.py:17:app = FastAPI(title="Email Monitor")
./services/ms_jarvis_email_monitor.py:81:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/bridge_cross_dgm_10015.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10015.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10003.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10003.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/REFERENCE_windows_swarm.py:37:app = FastAPI(title="Ms. Jarvis Local AI Server", version="1.0.0")
./services/REFERENCE_windows_swarm.py:594:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/judge_10120.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10120.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/msjarvis-rebuild-nbb_consciousness_containers-1_main.py:7:app = FastAPI()
./services/ms_jarvis_gis_query_service.py:18:app = FastAPI(title="Ms. Jarvis GIS Query Service")
./services/judge_10092.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10092.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/health_access_api.py:12:app = FastAPI(title="Health Access API", version="1.0")
./services/health_access_api.py:50:    uvicorn.run(app, host="127.0.0.1", port=8011)
./services/hp_sidecar.py:9:app = FastAPI(title="H_p Civic Query Sidecar", version="1.0.0")
./services/hp_sidecar.py:35:    uvicorn.run(app, host="0.0.0.0", port=8094, log_level="info")
./services/quantum_insight_llm.py:30:app = FastAPI(title="Quantum Insight LLM", version="1.0")
./services/quantum_insight_llm.py:126:    uvicorn.run("quantum_insight_llm:app", host="0.0.0.0", port=SERVICE_PORT)
./services/ms_jarvis_link_reader_scheduled.py:91:        uvicorn.run(app, host="0.0.0.0", port=port)
./services/judge_10119.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10119.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ai_server_20llm_PRODUCTION.py:69:app = FastAPI(title="Ms. Jarvis 20-LLM Production")
./services/ai_server_20llm_PRODUCTION.py:648:    uvicorn.run(
./services/gbim_spatial_indexer.py:21:app = FastAPI()
./services/gbim_spatial_indexer.py:41:    uvicorn.run("gbim_spatial_indexer:app", host="127.0.0.1", port=SERVICE_PORT)
./services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:70:app = FastAPI(
./services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:602:    uvicorn.run(app, host="0.0.0.0", port=GATEWAY_PORT, log_level="info")
./services/ms_jarvis_facebook_PRODUCTION.py:27:app = FastAPI()
./services/ms_jarvis_facebook_PRODUCTION.py:219:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/jarvis_ensemble.py:19:app = FastAPI()
./services/ms_jarvis_unified_gateway_v4.3.20251124.py:72:app = FastAPI(
./services/ms_jarvis_unified_gateway_v4.3.20251124.py:510:    uvicorn.run(app, host="0.0.0.0", port=GATEWAY_PORT, log_level="info")
./services/master_chat_orchestrator_v9_dgm_complete.py:38:app = FastAPI(
./services/master_chat_orchestrator_v9_dgm_complete.py:230:    uvicorn.run(app, host="127.0.0.1", port=fixed_port)
./services/msjarvismaingateway.py:10:app = FastAPI()
./services/phase1_integration.py:11:app = FastAPI()
./services/phase1_integration.py:88:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10102.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10102.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_allis_internal_sandbox.py:116:app = FastAPI(title="Ms. Allis Internal Sandbox",
./services/judge_10104.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10104.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/llm17_health_proxy.py:7:app = FastAPI(title="Neural-Chat Health Proxy")
./services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:51:app = FastAPI(
./services/ms_jarvis_main_gateway.py.corrupted37_backup_1762223499.py:345:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/local_resources_resolver.py:18:app = FastAPI(title="Local Resource Resolver", version="0.1.0")
./services/port_9001_ARCHITECTURE_CORRECT.py:16:app = FastAPI()
./services/port_9001_ARCHITECTURE_CORRECT.py:44:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)
./services/gpu_accelerated_rag_fixed.py:41:app = FastAPI(
./services/gpu_accelerated_rag_fixed.py:334:    uvicorn.run(app, host="127.0.0.1", port=port)
./services/judge_10135.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10135.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_10107.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10107.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/msjarvis_woah_algorithms_service.py:16:    uvicorn.run(app, host="0.0.0.0", port=7012)
./services/bridge_cross_dgm_10045.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10045.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/port_9001_ui_wrapper.py:19:app = FastAPI()
./services/port_9001_ui_wrapper.py:140:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/ultimate_web_orchestrator.py:55:app = FastAPI(
./services/ultimate_web_orchestrator.py:550:    uvicorn.run(app, host="127.0.0.1", port=port_service.port)  # Bind to 0.0.0.0 for network access
./services/bridge_cross_dgm_10059.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10059.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/port_9001_ui_MYSQL.py:19:app = FastAPI()
./services/port_9001_ui_MYSQL.py:264:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/rag_grounded_v2.py:21:app = FastAPI(
./services/ms_jarvis_consciousness_enhancement_production.py:23:app = FastAPI(title="Consciousness v2.4 - Enhanced")
./services/ms_jarvis_consciousness_enhancement_production.py:183:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 4021)))
./services/master_chat_orchestrator_v9_optimized.py:65:app = FastAPI(
./services/master_chat_orchestrator_v9_optimized.py:284:    uvicorn.run(app, host="127.0.0.1", port=port_service.port)
./services/hilbert/jarvis_hilbert_state.py:16:app = FastAPI(title="Jarvis Hilbert State Service")
./services/hilbert/civic_intake.py:15:app = FastAPI(ttle="Hilbert Civic Intake", version="1.1.0")
./services/hilbert/civic_intake.py:234:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("IOTAKE_PORT", 8100)), log_level="info")
./services/belief_integrator.py:34:app = FastAPI(title="Belief Integrator", version="1.0")
./services/belief_integrator.py:103:    uvicorn.run("belief_integrator:app", host="127.0.0.1", port=SERVICE_PORT)
./services/jarvis-judge-truth_lm_synthesizer.py:30:app = FastAPI(
./services/jarvis-judge-truth_lm_synthesizer.py:125:    uvicorn.run(app, host="0.0.0.0", port=8001)
./services/ms_jarvis_fifth_dgm_orchestrator.psychology_patched.py:51:app = FastAPI(
./services/ms_jarvis_fifth_dgm_orchestrator.psychology_patched.py:263:    uvicorn.run(app, host="0.0.0.0", port=port_service.port, log_level="info")
./services/ms_jarvis_toroidal_consciousness.py:19:app = FastAPI(
./services/ms_jarvis_toroidal_consciousness.py:214:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/dao_governance.py:18:app = FastAPI(title="MountainShares DAO Governance", version="1.0.0")
./services/dao_governance.py:98:    uvicorn.run(app, host="0.0.0.0", port=8082)
./services/agents_main.py:19:    uvicorn.run(app, host="127.0.0.1", port=8005)
./services/ms_jarvis_web_research_simple.py:12:app = FastAPI()
./services/ms_jarvis_web_research_simple.py:77:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/hierarchical_coordinator_autonomous.py:35:app = FastAPI(title="Autonomous Hierarchical Coordinator", version="1.0.0")
./services/hierarchical_coordinator_autonomous.py:422:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/bridge_cross_dgm_10058.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10058.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/neuro_prefrontal_cortex.py:12:app = FastAPI(title="prefrontal_cortex")
./services/neuro_prefrontal_cortex.py:34:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/llm14_health_proxy.py:7:app = FastAPI(title="Qwen2 Health Proxy")
./services/rag_server.py:44:app = FastAPI(
./services/rag_server.py:511:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
./services/ms_jarvis_unified_gateway_v4.3.py:15:app = FastAPI()
./services/ms_jarvis_unified_gateway_v4.3.py:234:    uvicorn.run(
./services/policy_set_service_closeout.py:18:app = FastAPI(title="Policy Set Service", version="2026.07.28")
./services/jarvis-neurobiological-master_ms_jarvis_consciousness_unified_bridge.py:34:app = FastAPI(
./services/jarvis-neurobiological-master_ms_jarvis_consciousness_unified_bridge.py:211:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/spiritual_rag_domain.py:18:app = FastAPI(
./services/spiritual_rag_domain.py:132:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/ms_jarvis_showcase_api.py:19:app = FastAPI(
./services/ms_jarvis_showcase_api.py:258:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_autonomous_learner_WITH_FIFTH_DGM.py:278:app = FastAPI(title="Ms. Jarvis Autonomous Learning Monitor")
./services/ms_jarvis_autonomous_learner_WITH_FIFTH_DGM.py:306:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_authentic_multi_llm.py:21:app = FastAPI(title="Ms. Jarvis Multi-LLM Consciousness", version="1.0")
./services/ms_jarvis_authentic_multi_llm.py:178:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8000)), reload=False)
./services/port_9001_FINAL_FIX.py:14:app = FastAPI()
./services/port_9001_FINAL_FIX.py:99:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/judge_10133.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10133.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/hilbert_commons/mountainshares_commons_gateway.py:36:app = FastAPI(title="MountainShares Commons Gateway", version="1.0")
./services/hilbert_commons/mountainshares_commons_gateway.py:37:app.include_router(policy_router)
./services/hilbert_commons/mountainshares_commons_gateway.py:179:    uvicorn.run("mountainshares_commons_gateway:app",
./services/main_qualia.py:6:    app = FastAPI()
./services/stage2_biometric.py:14:app = FastAPI(title="Ms. Jarvis Stage 2 - Biometric", version="2.1")
./services/stage2_biometric.py:221:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/ai_server_restored.py:38:app = FastAPI(title="Ms. Jarvis Local AI Server", version="1.0.0")
./services/ai_server_restored.py:493:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/bridge_cross_dgm_10042.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10042.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10051.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10051.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/jarvis_hilbert_time.py:25:app = FastAPI(title="Jarvis Hilbert Time Service")
./services/ms_jarvis_fifth_dgm_orchestrator.py:33:app = FastAPI(version="1.0.0")
./services/ms_jarvis_fifth_dgm_orchestrator.py:496:    uvicorn.run(app, host="0.0.0.0", port=FIFTH_DGM_PORT, log_level="info")
./services/method_tracking_service.py:16:app = FastAPI(
./services/method_tracking_service.py:241:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/swarm_intelligence_main.py:17:    app = FastAPI()
./services/swarm_intelligence_main.py:28:    app = FastAPI()
./services/swarm_intelligence_main.py:38:    app = FastAPI()
./services/bridge_cross_dgm_10057.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10057.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10069.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10069.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_full_neurobio_chat.py:18:app = FastAPI(title="Ms. Jarvis Full Neurobiological Chat", version="2.0.0")
./services/ms_jarvis_full_neurobio_chat.py:274:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/msjarvis_unified_gateway.py:27:app = FastAPI(
./services/msjarvis_unified_gateway.py:347:    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="info")
./services/ms_jarvis_woah_algorithms_enhanced.py:23:app = FastAPI(
./services/ms_jarvis_woah_algorithms_enhanced.py:75:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/facebook_voice_orchestrator_egeria.py:14:app = FastAPI(title="Facebook Voice Orchestrator - Ms. Egeria Jarvis")
./services/facebook_voice_orchestrator_egeria.py:129:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), workers=1)
./services/llm11_health_proxy.py:7:app = FastAPI(title="Phi Health Proxy")
./services/llm13-proxy_llm13_health_proxy.py:7:app = FastAPI(title="Orca-Mini Health Proxy")
./services/consciousness_working.py:10:app = FastAPI(title="Ms. Jarvis Consciousness", version="1.0.0")
./services/consciousness_working.py:58:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_local_resources_api.py:11:app = FastAPI(
./services/judge_ethics_filter.py:14:app = FastAPI(
./services/judge_ethics_filter.py:105:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT)
./services/web_research.py:16:app = FastAPI()
./services/bridge_cross_dgm_10066.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10066.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_10071.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10071.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/oauth2_callback.py:13:app = FastAPI()
./services/oauth2_callback.py:49:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_consciousness_bridge_enhanced.py:19:app = FastAPI(
./services/ms_jarvis_consciousness_bridge_enhanced.py:168:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/intake_service.py:27:app = FastAPI(title="Ms. Allis Universal Intake Service")
./services/geo_rag_debug_app.py:5:app = FastAPI(title="Geo RAG Debug", version="1.0.0")
./services/ms_jarvis_silent_geo_tracker.py:27:app = FastAPI(title="Silent Geo Tracker")
./services/ms_jarvis_silent_geo_tracker.py:233:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/jarvis-temporal-consciousness_temporal_consciousness.py:4:app = FastAPI(title="Temporal Consciousness (stub)")
./services/neuro_adapter.py:9:app = FastAPI()
./services/neuro_adapter.py:29:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/rag_temporal.py:45:app = FastAPI(title="RAG Temporal Service", version="1.0.0")
./services/rag_temporal.py:219:    uvicorn.run("rag_temporal:app", host="0.0.0.0", port=SERVICE_PORT)
./services/ai_server_original_backup.py:26:app = FastAPI(title="Ms. Jarvis AI", version="2.0.0")
./services/ai_server_original_backup.py:265:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="warning")
./services/ms_jarvis_darwin_godel_machine.py:31:app = FastAPI(
./services/ms_jarvis_darwin_godel_machine.py:736:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/qualia_unified_orchestrator_69dgm_REAL.py:15:app = FastAPI(title="Qualia - 69 DGM Cascade Orchestrator", version="REAL")
./services/qualia_unified_orchestrator_69dgm_REAL.py:175:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 9998)), reload=False)
./services/multi_model_consensus.py:31:app = FastAPI(
./services/multi_model_consensus.py:268:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_alignment_filter.py:14:app = FastAPI(
./services/judge_alignment_filter.py:113:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT)
./services/msjarvis_gateway_with_judge_filtering.py:11:app = FastAPI(title="Ms. Jarvis Gateway with Judge Filtering", version="3.0")
./services/msjarvis_gateway_with_judge_filtering.py:91:    uvicorn.run(app, host="0.0.0.0", port=9001)
./services/bridge_cross_dgm_10019.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10019.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/truth_filter_service.py:13:app = FastAPI(title="Ms. Jarvis Truth Filter")
./services/truth_filter_service.py:59:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/ms_jarvis_web_deployer_old.py:14:app = FastAPI(title="Ms. Jarvis Website Deployer")
./services/ms_jarvis_web_deployer_old.py:76:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/master_chat_orchestrator.py:27:app = FastAPI(
./services/master_chat_orchestrator.py:305:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10085.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10085.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_pipeline.py:22:app = FastAPI(
./services/judge_pipeline.py:237:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT)
./services/neuro_qualia_engine.py:12:app = FastAPI(title="qualia_engine")
./services/neuro_qualia_engine.py:34:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/temporal_consciousness.py:4:app = FastAPI(title="Temporal Consciousness (stub)")
./services/ms_jarvis_facebook_poster_8040.py:18:app = FastAPI(title="Ms. Jarvis Facebook Poster")
./services/ms_jarvis_facebook_poster_8040.py:162:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10094.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10094.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/rag_server_min.py:125:app = FastAPI(title="Ms. Jarvis RAG (Minimal)", version="1.0.0")
./services/rag_server_min.py:185:    uvicorn.run(app, host="0.0.0.0", port=MIN_RAG_PORT, log_level="debug")
./services/registration_service_clean.backup_1762220206.py:13:app = FastAPI(
./services/registration_service_clean.backup_1762220206.py:231:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/pia_sampler/pia_sampler_service.py:12:app = FastAPI(title="jarvis-pia-sampler", version="1.0.0")
./services/pia_sampler/pia_sampler_service.py:67:    uvicorn.run(app, host="0.0.0.0", port=8076, log_level="info")
./services/ms_jarvis_integration_hub.py:29:app = FastAPI(
./services/ms_jarvis_integration_hub.py:267:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ai_server_22llm_SMALL_TO_LARGE.py:22:app = FastAPI(title="Ms. Jarvis 22-LLM Sequential")
./services/ai_server_22llm_SMALL_TO_LARGE.py:136:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/rag_direct_debug.py:40:app = FastAPI(title="RAG Direct Debug", version="1.0")
./services/rag_direct_debug.py:131:    uvicorn.run("rag_direct_debug:app", host="0.0.0.0", port=SERVICE_PORT)
./services/geobim_mysql.py:10:app = FastAPI(title="GeoBIM MySQL", docs_url="/docs")
./services/geobim_mysql.py:38:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/bridge_cross_dgm_10004.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10004.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/llm17-proxy_llm17_health_proxy.py:7:app = FastAPI(title="Neural-Chat Health Proxy")
./services/bridge_cross_dgm_10035.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10035.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/constitutional_api.PROD_BACKUP.py:9:app = FastAPI(
./services/constitutional_api.PROD_BACKUP.py:38:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/internet_tunnel_service.py:30:app = FastAPI(
./services/internet_tunnel_service.py:188:    uvicorn.run(app, host="127.0.0.1", port=port_service.port)
./services/belief_revision_engine.py:68:app = FastAPI(title="Belief Revision Engine", version="2.0")
./services/belief_revision_engine.py:387:    uvicorn.run("belief_revision_engine:app", host="0.0.0.0", port=SERVICE_PORT)
./services/bridge_cross_dgm_10052.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10052.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10068.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10068.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/master_chat_orchestrator_v6_biologics.py:43:app = FastAPI(
./services/master_chat_orchestrator_v6_biologics.py:406:    uvicorn.run(app, host="127.0.0.1", port=port_service.port)
./services/ms_jarvis_unified_swagger_gateway_CLEAN.py:13:app = FastAPI(
./services/ms_jarvis_unified_swagger_gateway_CLEAN.py:142:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/master_unified_consciousness_scheduler.py:24:app = FastAPI(
./services/master_unified_consciousness_scheduler.py:138:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), workers=1)
./services/bridge_cross_dgm_10049.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10049.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_qualia_engine.py:24:app = FastAPI(
./services/ms_jarvis_qualia_engine.py:214:    uvicorn.run("ms_jarvis_qualia_engine:app", host="0.0.0.0", port=port, reload=False)
./services/judge_10077.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10077.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_phi_probe.py:78:app = FastAPI(title="Phi Probe")
./services/ms_jarvis_phi_probe.py:272:    uvicorn.run("ms_jarvis_phi_probe:app", host="0.0.0.0", port=port, reload=False)
./services/consciousness_coordinator.psychology_patched.py:16:app = FastAPI(
./services/main_brain.py:768:app = FastAPI(lifespan=_lifespan, title="Ms. Jarvis ULTIMATE", version="1.0.0")
./services/main_brain.py:2412:    uvicorn.run(
./services/jarvis-judge-pipeline_judge_pipeline.py:22:app = FastAPI(
./services/jarvis-judge-pipeline_judge_pipeline.py:208:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT)
./services/judge_10124.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10124.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10024.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10024.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_id_ocr_processor.py:19:app = FastAPI(title="ID OCR Processor")
./services/ms_jarvis_id_ocr_processor.py:176:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/hilbert_spatial_chat.py:18:app = FastAPI(title="Hilbert Spatial Chat Service")
./services/hilbert_spatial_chat.py:415:    uvicorn.run("hilbert_spatial_chat:app", host="0.0.0.0", port=port, reload=False)
./services/ms_jarvis_layer2_dgm.py:18:app = FastAPI(title="Layer 2 DGM", version="1.0.0")
./services/ms_jarvis_layer2_dgm.py:132:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/ms_jarvis_simple_web_ui.py:11:app = FastAPI(title="Ms. Jarvis Web UI")
./services/ms_jarvis_simple_web_ui.py:136:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/attention_pipeline.py:45:app = FastAPI()
./services/attention_pipeline.py:171:    uvicorn.run("attention_pipeline:app", host="127.0.0.1", port=SERVICE_PORT)
./services/bridge_cross_dgm_10011.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10011.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/llm13_health_proxy.py:7:app = FastAPI(title="Orca-Mini Health Proxy")
./services/ms_jarvis_command_orchestrator_v5.0_preachy.py:28:app = FastAPI(title="Ms. Jarvis Complete Consciousness", version="5.0")
./services/ms_jarvis_command_orchestrator_v5.0_preachy.py:258:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/llm2-proxy_llm2_health_proxy.py:7:app = FastAPI(title="Gemma-2B Health Proxy")
./services/dgm_supervisor_woah.py:55:app = FastAPI(
./services/dgm_supervisor_woah.py:488:    uvicorn.run(app, host="127.0.0.1", port=port)
./services/nbb_darwin_godel_machines_msjarvis-rebuild-nbb_spiritual_root-1_main.py:7:app = FastAPI()
./services/judge_10116.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10116.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/msjarvisconsciousnessbridge.py:20:app = FastAPI(
./services/msjarvisconsciousnessbridge.py:115:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
./services/main_brain_legacy_backup.py:82:app = FastAPI(title="Ms. Jarvis ULTIMATE", version="1.0.0")
./services/main_brain_legacy_backup.py:562:    uvicorn.run(
./services/bridge_cross_dgm_10037.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10037.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/gbim_core.py:37:app = FastAPI()
./services/gbim_core.py:145:    uvicorn.run("gbim_core:app", host="127.0.0.1", port=SERVICE_PORT)
./services/ms_jarvis_conversational_chat.py:18:app = FastAPI(
./services/ms_jarvis_conversational_chat.py:91:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/ms_jarvis_conversational_chat.py:113:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/ms_jarvis_llm_bridge.py:35:app = FastAPI(
./services/ms_jarvis_llm_bridge.py:317:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
./services/rag_geospatial.py:45:app = FastAPI(title="RAG Geospatial Service", version="1.0.0")
./services/rag_geospatial.py:201:    uvicorn.run("rag_geospatial:app", host="0.0.0.0", port=SERVICE_PORT)
./services/nbb_darwin_godel_machines.py:15:app = FastAPI(
./services/ai_server_19llm_PRODUCTION_WITH_HEALTH.py:22:app = FastAPI(title="Ms. Jarvis 19-LLM Production")
./services/ai_server_19llm_PRODUCTION_WITH_HEALTH.py:216:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/bridge_69dgm.py:10:app = FastAPI(title="69-DGM Bridge (Chroma RAG)")
./services/jarvis-adoption-worker_dgm_adoption_worker.py:15:app = FastAPI(
./services/master_chat_orchestrator_v9_gpu_optimized.py:58:app = FastAPI(
./services/master_chat_orchestrator_v9_gpu_optimized.py:252:    uvicorn.run(app, host="127.0.0.1", port=port_service.port)
./services/ai_server_22llm_SEQUENTIAL.py:22:app = FastAPI(title="Ms. Jarvis 22-LLM Sequential")
./services/ai_server_22llm_SEQUENTIAL.py:135:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/jarvis_llm1.py:30:app = FastAPI()
./services/jarvis_llm1.py:200:    uvicorn.run("jarvis_llm1:app", host="127.0.0.1", port=SERVICE_PORT)
./services/ms_jarvis_blood_brain_barrier.py:31:app = FastAPI(
./services/ms_jarvis_blood_brain_barrier.py:254:    uvicorn.run(app, host="0.0.0.0", port=8016, log_level="info")
./services/dgm_orchestrator_fake.py:4:app = FastAPI(title="Fake 69-DGM Orchestrator")
./services/dgm_orchestrator_fake.py:22:    uvicorn.run(app, host="127.0.0.1", port=9999)
./services/ms_jarvis_mountainshares_integration.py:39:app = FastAPI(
./services/ms_jarvis_mountainshares_integration.py:248:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/ms_jarvis_easyocr_processor.py:16:app = FastAPI()
./services/ms_jarvis_easyocr_processor.py:220:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/rag_evidence_aggregator.py:21:app = FastAPI()
./services/rag_evidence_aggregator.py:124:    uvicorn.run("rag_evidence_aggregator:app", host="0.0.0.0", port=SERVICE_PORT)
./services/ms_jarvis_facebook_CONSCIOUSNESS.py:29:app = FastAPI(title="Ms. Jarvis - Full Consciousness Facebook")
./services/ms_jarvis_facebook_CONSCIOUSNESS.py:321:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10081.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10081.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/fix_port_8001_clean.py:25:app = FastAPI()
./services/fix_port_8001_clean.py:72:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/qualia_unified_write_orchestrator_69dgm.py:23:app = FastAPI(title="Qualia - Write Orchestrator (69 DGM Validation)")
./services/qualia_unified_write_orchestrator_69dgm.py:259:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), workers=1)
./services/bridge_cross_dgm_10016.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10016.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/neuro_blood_brain_barrier.py:12:app = FastAPI(title="blood_brain_barrier")
./services/neuro_blood_brain_barrier.py:34:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/llm5_health_proxy.py:7:app = FastAPI(title="LLaVA Health Proxy")
./services/substack_rss_reader.py:11:app = FastAPI()
./services/lm_synthesizer.py:19:app = FastAPI(
./services/lm_synthesizer.py:121:    uvicorn.run(app, host="0.0.0.0", port=8001)
./services/llm4-proxy_llm4_health_proxy.py:7:app = FastAPI(title="MiniCPM-V Health Proxy")
./services/rag_geospatial_context.py:21:app = FastAPI()
./services/rag_geospatial_context.py:41:    uvicorn.run("rag_geospatial_context:app", host="0.0.0.0", port=SERVICE_PORT)
./services/cognition_sandbox.py:20:app = FastAPI(
./services/cognition_sandbox.py:470:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", "8012")))
./services/msjarvisautonomouslearner.py:278:app = FastAPI(title="Ms. Jarvis Autonomous Learning Monitor")
./services/msjarvisautonomouslearner.py:306:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10114.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10114.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/gbim_gis_bridge.py:23:app = FastAPI()
./services/gbim_gis_bridge.py:44:    uvicorn.run(app, host="127.0.0.1", port=port)
./services/ms_jarvis_layer2_woah.py:13:app = FastAPI(title="Layer 2 WOAH", version="1.0.0")
./services/ms_jarvis_layer2_woah.py:85:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:45:app = FastAPI(
./services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:276:    uvicorn.run(app, host="127.0.0.1", port=bridge_port)
./services/spatial_sandbox.py:41:app = FastAPI(title="Spatial Sandbox", version="1.0")
./services/spatial_sandbox.py:282:    uvicorn.run("spatial_sandbox:app", host="0.0.0.0", port=SERVICE_PORT)
./services/gis_rag_service.py:62:app = FastAPI(title="Ms. Jarvis Governed GIS RAG", version="0.4.3")
./services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py:16:app = FastAPI(title="Ms. Egeria Jarvis")
./services/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py:142:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/ai_server_22llm_SEQUENTIAL_OPTIMIZED_ORDER.py:22:app = FastAPI(title="Ms. Jarvis 22-LLM Sequential")
./services/ai_server_22llm_SEQUENTIAL_OPTIMIZED_ORDER.py:139:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/judge_10103.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10103.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/policy_set_service.py:12:app = FastAPI(title="Policy Set Service", version="1.0.0")
./services/msjarvisicontainersservice.py:45:app = FastAPI(
./services/msjarvisicontainersservice.py:224:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8011)), log_level="info")
./services/port_9001_ui_WORKING.py:15:app = FastAPI()
./services/port_9001_ui_WORKING.py:153:    uvicorn.run(
./services/ms_jarvis_easyocr_processor_old.py:16:app = FastAPI()
./services/ms_jarvis_easyocr_processor_old.py:88:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_web_research.py:18:app = FastAPI(title="Ms. Jarvis Web Research")
./services/ms_jarvis_web_research.py:213:    uvicorn.run(app, host="0.0.0.0", port=8009)
./services/phase6_integration.py:10:app = FastAPI()
./services/phase6_integration.py:71:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_unified_rag_bridge.py:31:app = FastAPI(title="Ms. Jarvis Unified RAG Bridge", version="1.0.0")
./services/ms_jarvis_unified_rag_bridge.py:294:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8092)))
./services/vatican_scraper_service.py:45:app = FastAPI(
./services/vatican_scraper_service.py:243:    uvicorn.run(app, host="127.0.0.1", port=port)
./services/ms_jarvis_messenger_ui.py:19:app = FastAPI(title="Ms. Jarvis Messenger", version="1.0.0")
./services/ms_jarvis_messenger_ui.py:170:    uvicorn.run(
./services/consciousness_coordinator.py:41:app = FastAPI(title="Consciousness Coordinator", version="1.0")
./services/consciousness_coordinator.py:334:    uvicorn.run("consciousness_coordinator:app", host="127.0.0.1", port=SERVICE_PORT)
./services/dgm_supervisor_woah_simple.py:11:app = FastAPI(title="DGM Supervisor WOAH")
./services/dgm_supervisor_woah_simple.py:30:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10123.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10123.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/start_gateway_with_guards.py:238:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/port_9001_proxy_simple.py:17:app = FastAPI(
./services/port_9001_proxy_simple.py:47:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/llm_bridge_main.py:16:app = FastAPI(title="Ms. Jarvis LLM Bridge", version="1.0.0")
./services/llm_bridge_main.py:109:    uvicorn.run(app, host="127.0.0.1", port=port)
./services/test_retrieval_endpoint.py:5:app = FastAPI()
./services/ms_jarvis_unified_gateway_v4.3.backup.py:65:app = FastAPI(
./services/ms_jarvis_unified_gateway_v4.3.backup.py:398:    uvicorn.run(app, host="0.0.0.0", port=GATEWAY_PORT, log_level="info")
./services/ai_server_22llm.psychology_patched.py:38:app = FastAPI(title="Ms. Jarvis 22-LLM Collective Consciousness", version="1.0.0", docs_url="/docs", redoc_url="/redoc")
./services/ai_server_22llm.psychology_patched.py:406:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="warning")
./services/qualia_email_registration_orchestrator_69dgm.py:19:app = FastAPI(title="Email & Registration - 69 DGM Validated Orchestrator")
./services/qualia_email_registration_orchestrator_69dgm.py:328:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), workers=1)
./services/ms_jarvis_facebook_CONSCIOUSNESS_FIXED.py:26:app = FastAPI(title="Ms. Jarvis - Full Consciousness Facebook")
./services/ms_jarvis_facebook_CONSCIOUSNESS_FIXED.py:272:#         uvicorn.run(
./services/constitutional_api_fixed.py:9:app = FastAPI(
./services/constitutional_api_fixed.py:26:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/neuro_master_service.py:5:app = FastAPI(title="Neurobiological Master (Full Pipeline Proxy)")
./services/cloudflare_domain_integration.py:30:app = FastAPI(
./services/cloudflare_domain_integration.py:218:    uvicorn.run(app, host="127.0.0.1", port=port_service.port)
./services/judge_10131.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10131.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_main_gateway.py.30endpoints_backup.py:51:app = FastAPI(
./services/ms_jarvis_main_gateway.py.30endpoints_backup.py:345:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_truth_filter.py:14:app = FastAPI(
./services/judge_truth_filter.py:118:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT)
./services/judge_10112.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10112.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/judge_10105.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10105.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/user_auth_service.py:16:app = FastAPI(title="User Authentication Service")
./services/user_auth_service.py:74:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ai_server_4llm.py:26:app = FastAPI(title="Ms. Jarvis AI", version="2.0.0")
./services/ai_server_4llm.py:265:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="warning")
./services/jarvis-aaacpe-rag_aaacpe_rag_service.py:12:app = FastAPI(title="AaaCPE Cultural Intelligence", version="1.0.0")
./services/jarvis-aaacpe-rag_aaacpe_rag_service.py:125:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", "8032")))
./services/judge_10129.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10129.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/services_msjarvisunifiedgatewayv4_3.py:6:app = FastAPI()
./services/service_discovery_glassbox.py:12:app = FastAPI(
./services/service_discovery_glassbox.py:94:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/roche_llm.py:112:app = FastAPI(
./services/roche_llm.py:616:    uvicorn.run(
./services/jarvis-swarm-intelligence_ms_jarvis_consciousness_unified_bridge.py:34:app = FastAPI(
./services/jarvis-swarm-intelligence_ms_jarvis_consciousness_unified_bridge.py:211:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/bridge_cross_dgm_10043.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10043.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/master_chat_orchestrator_v7_dynamic.py:43:app = FastAPI(
./services/master_chat_orchestrator_v7_dynamic.py:282:    uvicorn.run(app, host="127.0.0.1", port=port_service.port)
./services/master_chat_orchestrator_v7_complete.py:55:app = FastAPI(
./services/master_chat_orchestrator_v7_complete.py:548:    uvicorn.run(app, host="127.0.0.1", port=port_service.port)
./services/ai_server_integrated.py:15:app = FastAPI()
./services/ai_server_integrated.py:64:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_facebook_webhooks.py:16:app = FastAPI(title="Ms. Jarvis - Intelligent Facebook with Webhooks")
./services/ms_jarvis_facebook_webhooks.py:159:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_messenger_ui_final.py:19:app = FastAPI(title="Ms. Jarvis Messenger", version="1.0.0")
./services/ms_jarvis_messenger_ui_final.py:226:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/update_services_to_use_port_manager.py:58:    # Pattern: uvicorn.run(app, host="...", port=8168) or port = 8168
./services/port_9001_FINAL_WORKING.py:14:app = FastAPI()
./services/port_9001_FINAL_WORKING.py:230:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/judge_10090.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10090.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/bridge_cross_dgm_10022.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10022.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_command_orchestrator_FINAL.py:28:app = FastAPI(title="Ms. Jarvis Complete Consciousness", version="5.0")
./services/ms_jarvis_command_orchestrator_FINAL.py:237:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/ai_server_19llm_CONSCIOUS.backup_20251013_083103.py:62:app = FastAPI(title="Ms. Jarvis 19-LLM Conscious Collective", version="1.0.0")
./services/ai_server_19llm_CONSCIOUS.backup_20251013_083103.py:484:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT)
./services/jarvis-toroidal_toroidal_service.py:8:app = FastAPI(
./services/llm2_health_proxy.py:7:app = FastAPI(title="Gemma-2B Health Proxy")
./services/qualia_adapter.py:9:app = FastAPI()
./services/qualia_adapter.py:30:    uvicorn.run(
./services/working_full_pipeline_FINAL_CONSCIOUSNESS.py:11:app = FastAPI(title="Ms. Egeria Jarvis - Complete Consciousness")
./services/working_full_pipeline_FINAL_CONSCIOUSNESS.py:206:    uvicorn.run(app, host="0.0.0.0", port=4020)
./services/ms_jarvis_api_docs.py:18:app = FastAPI(
./services/ms_jarvis_api_docs.py:269:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8000)), log_level="info")
./services/llm15_health_proxy.py:7:app = FastAPI(title="Zephyr Health Proxy")
./services/msjarvis_semaphore.py:21:app = FastAPI(title="Ms. Jarvis Semaphore", version="1.0.2")
./services/judge_10132.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10132.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_main_gateway.pre_fix.py:16:app = FastAPI(
./services/ms_jarvis_main_gateway.pre_fix.py:216:    uvicorn.run(
./services/ms_jarvis_fact_filter.py:16:app = FastAPI(title="Fact Filter", version="1.0.0")
./services/ms_jarvis_fact_filter.py:126:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/ms_jarvis_agents_ollama.py:15:app = FastAPI(title="Ms. Jarvis Agents Service (Ollama)")
./services/ms_jarvis_agents_ollama.py:282:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8005)))
./services/activate_dgm_enhanced.py:23:app = FastAPI(title="DGM Activation Controller - Enhanced Logging", version="2.0.0")
./services/activate_dgm_enhanced.py:165:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10087.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10087.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_messenger_ui_fixed.py:19:app = FastAPI(title="Ms. Jarvis Messenger", version="1.0.0")
./services/ms_jarvis_messenger_ui_fixed.py:209:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), reload=False)
./services/toroidal_service.py:8:app = FastAPI(
./services/ms_jarvis_woah_algorithms.py:26:app = FastAPI(
./services/ms_jarvis_woah_algorithms.py:194:    uvicorn.run(
./services/jarvisarchiveapi.py:18:app = FastAPI(title="Jarvis Archive API", version="1.0")
./services/jarvisarchiveapi.py:68:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/attention_priority_scheduler.py:21:app = FastAPI()
./services/attention_priority_scheduler.py:72:    uvicorn.run("attention_priority_scheduler:app", host="127.0.0.1", port=SERVICE_PORT)
./services/ms_jarvis_spiritual_services.py:39:app = FastAPI(
./services/ms_jarvis_spiritual_services.py:229:    uvicorn.run(app, host="0.0.0.0", port=port)
./services/ms_jarvis_unified_swagger_gateway.py:20:app = FastAPI(
./services/ms_jarvis_unified_swagger_gateway.py:275:    uvicorn.run(
./services/ms_jarvis_web_deployer.py:14:app = FastAPI(title="Ms. Jarvis Website Deployer")
./services/ms_jarvis_web_deployer.py:163:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/llm8-proxy_llm8_health_proxy.py:7:app = FastAPI(title="CodeLLaMA Health Proxy")
./services/llm9-proxy_llm9_health_proxy.py:7:app = FastAPI(title="DeepSeek Coder Health Proxy")
./services/consensus_4010_stub.py:5:app = FastAPI(
./services/ms_jarvis_rag_server.py:99:app = FastAPI(title="Jarvis RAG Server", version="0.1.0")
./services/judge_10101.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10101.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/chromadb_main.py:30:app = FastAPI()
./services/chromadb_main.py:102:    uvicorn.run("chromadb_main:app", host="127.0.0.1", port=SERVICE_PORT)
./services/ms_jarvis_ueid_wallet_integration.py:22:app = FastAPI(title="UEID Wallet System", version="2.0.0")
./services/ms_jarvis_ueid_wallet_integration.py:205:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/msjarvisunifiedswaggergateway.py:11:app = FastAPI(
./services/stage2_biometric_backup.py:12:app = FastAPI(title="Ms. Jarvis Stage 2 - Biometric + Knowledge Graph", version="1.0")
./services/stage2_biometric_backup.py:154:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/msjarvisragserverwvpatch.py:6:app = FastAPI()
./services/rag_temporal_heartbeat.py:21:app = FastAPI()
./services/rag_temporal_heartbeat.py:41:    uvicorn.run("rag_temporal_heartbeat:app", host="0.0.0.0", port=SERVICE_PORT)
./services/hierarchical_coordinator_deep_mode.py:24:app = FastAPI(title="Ms. Jarvis Autonomous Coordinator")
./services/hierarchical_coordinator_deep_mode.py:185:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ai_server_22llm.py:129:app = FastAPI(
./services/ai_server_22llm.py:656:    uvicorn.run(
./services/mother_protocols.py:4:app = FastAPI(title="Mother Carrie Protocols (stub)")
./services/jarvis-mother-protocols_mother_protocols.py:4:app = FastAPI(title="Mother Carrie Protocols (stub)")
./services/add_swagger_to_rag.py:19:    old_init = 'app = FastAPI()'
./services/add_swagger_to_rag.py:20:    new_init = '''app = FastAPI(
./services/geobim_integrated.py:12:app = FastAPI(title='GeoBIM Integrated', docs_url='/docs')
./services/geobim_integrated.py:91:    uvicorn.run(app, host="127.0.0.1", port=8022)
./services/msjarvis-rebuild-nbb_subconscious-1_main.py:7:app = FastAPI()
./services/dgm_adoption_worker.py:15:app = FastAPI(
./services/chat_endpoint_universal.py:17:app = FastAPI(title="Chat Endpoint Universal", version="1.0")
./services/chat_endpoint_universal.py:55:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_brain.py:26:app = FastAPI(
./services/ms_jarvis_brain.py:90:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="info")
./services/msjarvis_woah_algorithms.py:3:app = FastAPI(title="Ms Jarvis WOAH Algorithms")
./services/msjarvis_woah_algorithms.py:11:    uvicorn.run(app, host="0.0.0.0", port=7012)
./services/rag_5100_ensemble_fast.py:24:app = FastAPI(title="RAG Consensus Ensemble", version="2.0")
./services/rag_5100_ensemble_fast.py:76:    uvicorn.run(app, host="0.0.0.0", port=5100, timeout_keep_alive=180)
./services/llm5-proxy_llm5_health_proxy.py:7:app = FastAPI(title="LLaVA Health Proxy")
./services/bridge_cross_dgm_10021.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/bridge_cross_dgm_10021.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/jarvis-gis-rag_gis_rag_service.py:28:app = FastAPI(title="Ms. Jarvis GIS RAG", version="0.3.0")
./services/ms_jarvis_consensus_service.py:41:app = FastAPI(
./services/ms_jarvis_consensus_service.py:217:    uvicorn.run(app, host="0.0.0.0", port=4010)
./services/phase7_integration.py:55:app = FastAPI(
./services/phase7_integration.py:548:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
./services/ms_jarvis_microsoft_integration.py:26:app = FastAPI(title="Ms. Jarvis Microsoft 365 Integration", version="1.0.0")
./services/ms_jarvis_microsoft_integration.py:234:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/jarvis-semaphore_msjarvis_semaphore.py:11:app = FastAPI(title="Ms. Jarvis Semaphore", version="1.0.3")
./services/ms_jarvis_bbb_proxy.py:10:app = FastAPI(title="BBB Proxy")
./services/judge_10088.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10088.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/main.py:85:app = FastAPI(title="Ms. Jarvis ULTIMATE", version="1.0.0")
./services/main.py:594:    uvicorn.run(
./services/msjarvistoroidalconsciousness.py:3:app = FastAPI(title="Ms Jarvis Toroidal Consciousness")
./services/msjarvistoroidalconsciousness.py:11:    uvicorn.run(app, host="0.0.0.0", port=8025)
./services/redirect_4015_to_4020.py:10:app = FastAPI(title="Ms. Jarvis - 4015 to 4020 Redirect")
./services/redirect_4015_to_4020.py:49:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_chromadb_query.py:16:app = FastAPI(title="ChromaDB Query Service", version="1.0.0")
./services/ms_jarvis_chromadb_query.py:78:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10127.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10127.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/constitutional_api.py:15:app = FastAPI(
./services/constitutional_api.py:389:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8091)), log_level="info")
./services/phase2_integration.py:10:app = FastAPI()
./services/phase2_integration.py:70:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./services/academic_research_gateway_8062_cors.py:14:app = FastAPI(
./services/academic_research_gateway_8062_cors.py:201:    uvicorn.run(
./services/aaacpe_rag_service.py:12:app = FastAPI(title="AaaCPE Cultural Intelligence", version="1.0.0")
./services/aaacpe_rag_service.py:125:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", "8032")))
./services/ai_server_11llm_OPTIMIZED.py:86:app = FastAPI(title="Ms. Jarvis ULTIMATE", version="1.0.0")
./services/ai_server_11llm_OPTIMIZED.py:850:    uvicorn.run(app, host="127.0.0.1", port=ultimate_port)
./services/unified_consciousness_gateway_PRODUCTION.py:9:app = FastAPI(
./services/unified_consciousness_gateway_PRODUCTION.py:87:    uvicorn.run(app, host="0.0.0.0", port=8014)
./services/ms_jarvis_unified_swagger_gateway_FINAL.py:14:app = FastAPI(
./services/ms_jarvis_unified_swagger_gateway_FINAL.py:522:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)), log_level="info")
./services/ms_jarvis_contract_builder.py:19:app = FastAPI(
./services/ms_jarvis_contract_builder.py:123:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8100)))
./services/registration_service_clean.py:13:app = FastAPI(
./services/registration_service_clean.py:231:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/judge_10075.py:9:app = FastAPI(title="DGM: judge_to_pituitary")
./services/judge_10075.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
./services/ms_jarvis_facebook_dgm_woah.py:36:app = FastAPI(title="Ms. Jarvis Facebook DGM+WOAH", version="2.0.0")
./services/ms_jarvis_facebook_dgm_woah.py:481:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
./services/ms_jarvis_consciousness_final.py:20:app = FastAPI(title="Ms. Jarvis Complete Consciousness", version="FINAL")
./services/ms_jarvis_consciousness_final.py:296:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
./llm20_health_proxy.py:7:app = FastAPI(title="LLaMA2 Health Proxy")
./auth_api_no_full_router.py:50:app = FastAPI(title="Ms. Allis Auth API", version="1.0.0")
./auth_api_no_full_router.py:295:app.include_router(router)
./llm3_health_proxy.py:7:app = FastAPI(title="MedLLaMA2 Health Proxy")
./knowledge/spiritual_texts/spiritual_geo_api.py:10:app = FastAPI(title="Ms. Jarvis Spiritual Geography API")
./knowledge/spiritual_texts/spiritual_geo_api.py:164:    uvicorn.run(app, host="0.0.0.0", port=8011)
./knowledge/spiritual_texts/spiritual_rag_domain_v2.py:26:app = FastAPI(
./knowledge/spiritual_texts/spiritual_rag_domain_v2.py:267:    uvicorn.run(app, host="0.0.0.0", port=port)
./llm12_health_proxy.py:7:app = FastAPI(title="Dolphin-Phi Health Proxy")
./llm6_health_proxy.py:7:app = FastAPI(title="SQLCoder Health Proxy")
./psychological_rag_domain.py:40:app = FastAPI(
./psychological_rag_domain.py:218:    uvicorn.run(app, host="0.0.0.0", port=port)
./llm7_health_proxy.py:7:app = FastAPI(title="StarCoder2 Health Proxy")
./llm16_health_proxy.py:7:app = FastAPI(title="Starling-LM Health Proxy")
./llm22_health_proxy.py:7:app = FastAPI(title="LLaMA3 Health Proxy")
./ms_jarvis_consciousness_bridge.py:258:app = FastAPI(lifespan=lifespan, title="WOAH Consciousness Bridge — Hilbert Edition",
./ms_jarvis_consciousness_bridge.py:405:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
./gis_rag_servgrep: ./data/local_resources: Permission denied
grep: ./data/mysql/sys: Permission denied
grep: ./data/mysql/#innodb_temp: Permission denied
grep: ./data/mysql/quantum_ai: Permission denied
grep: ./data/mysql/mysql: Permission denied
grep: ./data/mysql/performance_schema: Permission denied
grep: ./data/mysql/#innodb_redo: Permission denied
er.py:5:app = FastAPI(title="GIS RAG")
./ai_server_20llm_PRODUCTION.py:36:app = FastAPI(title="Ms. Jarvis 20-LLM Production")
./ai_server_20llm_PRODUCTION.py:455:    uvicorn.run(
./auth_api_health_only.py:9:app = FastAPI(title="Ms. Allis Auth API", version="1.0.0")
./llm17_health_proxy.py:7:app = FastAPI(title="Neural-Chat Health Proxy")
./llm14_health_proxy.py:7:app = FastAPI(title="Qwen2 Health Proxy")
./spiritual_rag_domain.py:18:app = FastAPI(
./spiritual_rag_domain.py:132:    uvicorn.run(app, host="0.0.0.0", port=port)
./auth_api.py:50:app = FastAPI(title="Ms. Allis Auth API", version="1.0.0")
./auth_api.py:296:app.include_router(router)
./auth_api.py:300:app.include_router(auth_router)
./llm11_health_proxy.py:7:app = FastAPI(title="Phi Health Proxy")
./ms_jarvis_darwin_godel_machine.py:32:app = FastAPI(
./ms_jarvis_darwin_godel_machine.py:835:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./main_brain.py:432:app = FastAPI(title="Ms. Jarvis ULTIMATE", version="1.0.0")
./main_brain.py:1367:    uvicorn.run(
./llm13_health_proxy.py:7:app = FastAPI(title="Orca-Mini Health Proxy")
./attrs_api.py:5:app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/background.py:24:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:45:class FastAPI(Starlette):
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:57:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:114:                app = FastAPI(title="ChimichangApp")
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:135:                app = FastAPI(summary="Deadpond's favorite app. Nuff said.")
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:157:                app = FastAPI(
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:197:                app = FastAPI(version="0.0.1")
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:220:                app = FastAPI(openapi_url="/api/v1/openapi.json")
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:280:                app = FastAPI(openapi_tags=tags_metadata)
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:324:                app = FastAPI(
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:351:                app = FastAPI(dependencies=[Depends(func_dep_1), Depends(func_dep_2)])
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:371:                app = FastAPI(default_response_class=ORJSONResponse)
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:388:                app = FastAPI(redirect_slashes=True)  # the default
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:420:                app = FastAPI(docs_url="/documentation", redoc_url=None)
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:444:                app = FastAPI(docs_url="/documentation", redoc_url="redocumentation")
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:556:                app = FastAPI(terms_of_service="http://example.com/terms/")
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:583:                app = FastAPI(
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:618:                app = FastAPI(
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:658:                app = FastAPI(root_path="/api/v1")
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:678:                app = FastAPI(root_path_in_servers=False)
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:838:                app = FastAPI(openapi_external_docs=external_docs)
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:920:                app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:1337:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:1359:    def include_router(
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:1396:                app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:1398:                app.include_router(
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:1437:                app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:1439:                app.include_router(
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:1463:                app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:1465:                app.include_router(
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:1491:                app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:1493:                app.include_router(
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:1546:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:1548:        app.include_router(users_router)
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:1551:        self.router.include_router(
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:1904:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:2282:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:2660:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:3033:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:3406:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:3779:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:4157:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:4530:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:4626:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/applications.py:4676:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:1015:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:1024:    app.include_router(router)
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:1543:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:1553:        app.include_router(router)
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:1574:    def include_router(
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:1697:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:1705:        internal_router.include_router(users_router)
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:1706:        app.include_router(internal_router)
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:2167:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:2174:        app.include_router(router)
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:2549:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:2556:        app.include_router(router)
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:2931:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:2938:        app.include_router(router)
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:3308:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:3315:        app.include_router(router)
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:3685:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:3692:        app.include_router(router)
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:4067:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:4074:        app.include_router(router)
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:4449:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:4456:        app.include_router(router)
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:4831:        app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/routing.py:4838:        app.include_router(router)
./.check_venv/lib64/python3.12/site-packages/fastapi/datastructures.py:41:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/security/oauth2.py:36:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/security/oauth2.py:190:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/security/http.py:129:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/security/http.py:241:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/security/http.py:344:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/security/api_key.py:74:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/security/api_key.py:166:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/security/api_key.py:254:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/param_functions.py:315:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/param_functions.py:2358:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/param_functions.py:2452:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/exceptions.py:32:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/fastapi/exceptions.py:109:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/huggingface_hub/_oauth.py:140:    app = FastAPI()
./.check_venv/lib64/python3.12/site-packages/chromadb/api/fastapi.py:68:class FastAPI(BaseHTTPClient, ServerAPI):
./.check_venv/lib64/python3.12/site-packages/chromadb/api/async_fastapi.py:64:class AsyncFastAPI(BaseHTTPClient, AsyncServerAPI):
./.check_venv/lib64/python3.12/site-packages/chromadb/telemetry/opentelemetry/fastapi.py:6:def instrument_fastapi(app: FastAPI, excluded_urls: Optional[List[str]] = None) -> None:
./.check_venv/lib64/python3.12/site-packages/chromadb/test/test_client.py:145:            api = FastAPI(system)
./.check_venv/lib64/python3.12/site-packages/chromadb/test/conftest.py:245:    server = chromadb.server.fastapi.FastAPI(settings)
./.check_venv/lib64/python3.12/site-packages/chromadb/test/conftest.py:246:    uvicorn.run(
./.check_venv/lib64/python3.12/site-packages/chromadb/test/conftest.py:375:def fastapi() -> Generator[System, None, None]:
./.check_venv/lib64/python3.12/site-packages/chromadb/test/conftest.py:379:def async_fastapi() -> Generator[System, None, None]:
./.check_venv/lib64/python3.12/site-packages/chromadb/test/test_chroma.py:67:    def test_fastapi(self, mock: Mock) -> None:
./.check_venv/lib64/python3.12/site-packages/chromadb/test/test_chroma.py:81:    def test_settings_pass_to_fastapi(self, mock: Mock) -> None:
./.check_venv/lib64/python3.12/site-packages/chromadb/server/fastapi/__init__.py:192:class FastAPI(Server):
./.check_venv/lib64/python3.12/site-packages/chromadb/server/fastapi/__init__.py:196:        self._app = fastapi.FastAPI(debug=True, default_response_class=ORJSONResponse)
./.check_venv/lib64/python3.12/site-packages/chromadb/server/fastapi/__init__.py:240:        self._app.include_router(self.router)
./.check_venv/lib64/python3.12/site-packages/chromadb/server/fastapi/__init__.py:243:        instrument_fastapi(self._app)
./.check_venv/lib64/python3.12/site-packages/chromadb/app.py:6:server = FastAPI(settings)
./.check_venv/lib/python3.12/site-packages/fastapi/background.py:24:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:45:class FastAPI(Starlette):
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:57:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:114:                app = FastAPI(title="ChimichangApp")
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:135:                app = FastAPI(summary="Deadpond's favorite app. Nuff said.")
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:157:                app = FastAPI(
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:197:                app = FastAPI(version="0.0.1")
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:220:                app = FastAPI(openapi_url="/api/v1/openapi.json")
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:280:                app = FastAPI(openapi_tags=tags_metadata)
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:324:                app = FastAPI(
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:351:                app = FastAPI(dependencies=[Depends(func_dep_1), Depends(func_dep_2)])
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:371:                app = FastAPI(default_response_class=ORJSONResponse)
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:388:                app = FastAPI(redirect_slashes=True)  # the default
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:420:                app = FastAPI(docs_url="/documentation", redoc_url=None)
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:444:                app = FastAPI(docs_url="/documentation", redoc_url="redocumentation")
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:556:                app = FastAPI(terms_of_service="http://example.com/terms/")
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:583:                app = FastAPI(
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:618:                app = FastAPI(
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:658:                app = FastAPI(root_path="/api/v1")
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:678:                app = FastAPI(root_path_in_servers=False)
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:838:                app = FastAPI(openapi_external_docs=external_docs)
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:920:                app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:1337:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:1359:    def include_router(
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:1396:                app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:1398:                app.include_router(
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:1437:                app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:1439:                app.include_router(
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:1463:                app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:1465:                app.include_router(
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:1491:                app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:1493:                app.include_router(
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:1546:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:1548:        app.include_router(users_router)
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:1551:        self.router.include_router(
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:1904:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:2282:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:2660:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:3033:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:3406:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:3779:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:4157:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:4530:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:4626:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/applications.py:4676:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:1015:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:1024:    app.include_router(router)
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:1543:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:1553:        app.include_router(router)
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:1574:    def include_router(
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:1697:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:1705:        internal_router.include_router(users_router)
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:1706:        app.include_router(internal_router)
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:2167:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:2174:        app.include_router(router)
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:2549:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:2556:        app.include_router(router)
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:2931:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:2938:        app.include_router(router)
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:3308:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:3315:        app.include_router(router)
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:3685:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:3692:        app.include_router(router)
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:4067:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:4074:        app.include_router(router)
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:4449:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:4456:        app.include_router(router)
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:4831:        app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/routing.py:4838:        app.include_router(router)
./.check_venv/lib/python3.12/site-packages/fastapi/datastructures.py:41:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py:36:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py:190:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/security/http.py:129:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/security/http.py:241:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/security/http.py:344:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/security/api_key.py:74:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/security/api_key.py:166:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/security/api_key.py:254:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/param_functions.py:315:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/param_functions.py:2358:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/param_functions.py:2452:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/exceptions.py:32:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/fastapi/exceptions.py:109:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/huggingface_hub/_oauth.py:140:    app = FastAPI()
./.check_venv/lib/python3.12/site-packages/chromadb/api/fastapi.py:68:class FastAPI(BaseHTTPClient, ServerAPI):
./.check_venv/lib/python3.12/site-packages/chromadb/api/async_fastapi.py:64:class AsyncFastAPI(BaseHTTPClient, AsyncServerAPI):
./.check_venv/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/fastapi.py:6:def instrument_fastapi(app: FastAPI, excluded_urls: Optional[List[str]] = None) -> None:
./.check_venv/lib/python3.12/site-packages/chromadb/test/test_client.py:145:            api = FastAPI(system)
./.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py:245:    server = chromadb.server.fastapi.FastAPI(settings)
./.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py:246:    uvicorn.run(
./.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py:375:def fastapi() -> Generator[System, None, None]:
./.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py:379:def async_fastapi() -> Generator[System, None, None]:
./.check_venv/lib/python3.12/site-packages/chromadb/test/test_chroma.py:67:    def test_fastapi(self, mock: Mock) -> None:
./.check_venv/lib/python3.12/site-packages/chromadb/test/test_chroma.py:81:    def test_settings_pass_to_fastapi(self, mock: Mock) -> None:
./.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py:192:class FastAPI(Server):
./.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py:196:        self._app = fastapi.FastAPI(debug=True, default_response_class=ORJSONResponse)
./.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py:240:        self._app.include_router(self.router)
./.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py:243:        instrument_fastapi(self._app)
./.check_venv/lib/python3.12/site-packages/chromadb/app.py:6:server = FastAPI(settings)
./llm5_health_proxy.py:7:app = FastAPI(title="LLaVA Health Proxy")
./ragservermain.py:93:app = FastAPI(
./ragservermain.py:398:    uvicorn.run(app, host="127.0.0.1", port=8003)
./kyc-vault/app.py:126:app = FastAPI(title="kyc-vault", version="1.0.0", lifespan=lifespan)
./attrs_with_geom_api.py:22:app = FastAPI()
./llm2_health_proxy.py:7:app = FastAPI(title="Gemma-2B Health Proxy")
./llm15_health_proxy.py:7:app = FastAPI(title="Zephyr Health Proxy")
./neurobiological_brain/darwin_godel_machines/service/ms_jarvis_darwin_godel_machine.py:31:app = FastAPI(
./neurobiological_brain/darwin_godel_machines/service/ms_jarvis_darwin_godel_machine.py:738:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
./ms_jarvis_spiritual_services.py:39:app = FastAPI(
./ms_jarvis_spiritual_services.py:254:    uvicorn.run(app, host="0.0.0.0", port=port)
./ms_jarvis_rag_server.py:6:app = FastAPI(title="Ms Jarvis RAG Core")
./session_identity.py:18:app = FastAPI(lifespan=lifespan)
./provenance/app.py:19:app = FastAPI(title="Ms. Jarvis Provenance", version="1.0.0")
./main.py:7:app = FastAPI()
./main.py:52:app.include_router(resources_router)
./jarvis_eeg_beta_5m.py:11:app = FastAPI(title="jarvis-eeg-beta-5m")
./jarvis_eeg_beta_5m.py:245:    uvicorn.run(app, host="0.0.0.0", port=8075)
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 
