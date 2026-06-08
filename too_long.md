./scripts/jarvis_auth_service.py:142:@app.get("/auth/portal/me/balances")
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild || exit 1

printf '\n=== auth_router.py admin area ===\n'
sed -n '200,280p' services/auth_router.py

printf '\n=== auth_router.py portal balances area ===\n'
sed -n '500,560p' services/auth_router.py

printf '\n=== jarvis_auth_service.py auth endpoints ===\n'
sed -n '110,170p' .scripts/jarvis_auth_service.py

=== auth_router.py admin area ===
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



=== auth_router.py portal balances area ===
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
        cur.execute("SELECT ems_balance, pms_balance, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
        bal = cur.fetchone()
        cur.execute("SELECT serial_number, minted_at, cohort, allocation_type FROM founder_tokens WHERE ueid = %s", (ueid,))
        ft = cur.fetchone()
        cur.execute("SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s OR ueid = %s", (sub, ueid))
        session_ems = float(cur.fetchone()[0])
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"DB error: {e}")
    founder_token = None
    if ft:

=== jarvis_auth_service.py auth endpoints ===
sed: can't read .scripts/jarvis_auth_service.py: No such file or directory
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild || exit 1

python3 - <<'PY'
from pathlib import Path
p = Path("services/auth_router.py")
s = p.read_text()

if '@auth_router.get("/admin/chat-metrics")' in s:
    print("route already exists")
    raise SystemExit(0)

anchor = '\n# ── Admin: list pending applications ─────────────────────────────────────────\n'
if anchor not in s:
    raise SystemExit("anchor not found in services/auth_router.py")

insert = '''
# ── Admin: chat metrics ──────────────────────────────────────────────────────

@auth_router.get("/admin/chat-metrics")
async def admin_chat_metrics(payload: Annotated[dict, Depends(_current_user)]):
    if "admin" not in payload.get("roles", []):
sed -n '220,270p' services/auth_router.py/pending' services/auth_router.py | sed -n
inserted /admin/chat-metrics route
233:@auth_router.get("/admin/chat-metrics")
253:@auth_router.get("/applications/pending")
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
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ pm2 list
systemctl --type=service --state=running | grep -Ei 'auth|router|fastapi|uvicorn|gunicorn|jarvis|backend'
┌────┬────────────────────┬──────────┬──────┬───────────┬──────────┬──────────┐
│ id │ name               │ mode     │ ↺    │ status    │ cpu      │ memory   │
├────┼────────────────────┼──────────┼──────┼───────────┼──────────┼──────────┤
│ 0  │ ms-allis-frontend  │ fork     │ 14   │ online    │ 0%       │ 54.1mb   │
└────┴────────────────────┴──────────┴──────┴───────────┴──────────┴──────────┘
  jarvis-auth.service                 loaded active running Ms. Jarvis Auth + Status Service
  jarvis-chat.service                 loaded active running Ms. Jarvis Production Chat
  ms-allis-auth-router.service        loaded active running Ms Allis Auth Router (port 8095)
  msjarvis-69dgm-9002-chat.service    loaded active running MsJarvis Port 9002 → 69-DGM Chat Wrapper
  msjarvis-interaction-logger.service loaded active running MS Jarvis Interaction Logger
  polkit.service                      loaded active running Authorization Manager
  postgresql@16-msjarvis.service      loaded active running PostgreSQL Cluster 16-msjarvis
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ pm2 logs --lines 120 --nostream
journalctl -n 120 --no-pager
[TAILING] Tailing last 120 lines for [all] processes (change the value with --lines option)
/home/cakidd/.pm2/pm2.log last 120 lines:
PM2        | 2026-06-07T19:36:22: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-07T19:36:22: PM2 log: pid=1216457 msg=process tree killed (3 pids)
PM2        | 2026-06-07T19:36:22: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:22: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:22: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:22: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:22: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:23: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:23: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:23: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:23: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:23: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:23: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:23: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:23: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:23: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:23: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:23: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:23: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:24: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:24: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:24: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:24: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:24: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:24: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:24: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:24: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:24: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:24: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:24: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:24: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:25: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:25: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:25: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:25: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:25: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:25: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:25: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:25: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:25: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:25: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:25: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:25: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:26: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:26: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:26: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:26: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:26: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:36:26: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T19:36:26: PM2 log: App [ms-allis-frontend:0] exited with code [1] via signal [SIGINT]
PM2        | 2026-06-07T19:36:26: PM2 log: Script /usr/bin/npm had too many unstable restarts (16). Stopped. "errored"
PM2        | 2026-06-07T19:40:25: PM2 log: Stopping app:ms-allis-frontend id:0
PM2        | 2026-06-07T19:40:25: PM2 error: app=ms-allis-frontend id=0 does not have a pid
PM2        | 2026-06-07T19:40:25: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T19:40:25: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-07T20:05:57: PM2 log: Stopping app:ms-allis-frontend id:0
PM2        | 2026-06-07T20:05:57: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-07T20:05:57: PM2 log: pid=1229019 msg=process tree killed (3 pids)
PM2        | 2026-06-07T20:05:57: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-07T20:05:57: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-08T12:07:35: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-08T12:07:35: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-08T12:07:35: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-08T12:12:32: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-08T12:12:32: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-08T12:12:32: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-08T12:18:29: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-08T12:18:29: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-08T12:18:29: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-08T12:18:31: PM2 log: App [ms-allis-frontend:0] exited with code [137] via signal [SIGINT]
PM2        | 2026-06-08T12:18:31: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-08T12:18:31: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-08T12:20:23: PM2 log: Stopping app:ms-allis-frontend id:0
PM2        | 2026-06-08T12:20:23: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-08T12:20:23: PM2 log: pid=3336776 msg=process tree killed (3 pids)
PM2        | 2026-06-08T12:20:23: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-08T12:20:23: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-08T12:20:37: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-08T12:20:37: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-08T12:20:37: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-08T12:25:40: PM2 log: Stopping app:ms-allis-frontend id:0
PM2        | 2026-06-08T12:25:40: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-08T12:25:40: PM2 log: pid=3339633 msg=process tree killed (3 pids)
PM2        | 2026-06-08T12:25:40: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-08T12:25:40: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-08T12:26:02: PM2 log: Stopping app:ms-allis-frontend id:0
PM2        | 2026-06-08T12:26:02: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-08T12:26:02: PM2 log: pid=3348470 msg=process tree killed (3 pids)
PM2        | 2026-06-08T12:26:02: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-08T12:26:02: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-08T12:33:05: PM2 log: Stopping app:ms-allis-frontend id:0
PM2        | 2026-06-08T12:33:05: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-08T12:33:05: PM2 log: pid=3349441 msg=process tree killed (3 pids)
PM2        | 2026-06-08T12:33:05: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-08T12:33:05: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-08T12:34:55: PM2 log: Stopping app:ms-allis-frontend id:0
PM2        | 2026-06-08T12:34:55: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-08T12:34:55: PM2 log: pid=3358275 msg=process tree killed (3 pids)
PM2        | 2026-06-08T12:34:55: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-08T12:34:55: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-08T12:35:16: PM2 log: Stopping app:ms-allis-frontend id:0
PM2        | 2026-06-08T12:35:16: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-08T12:35:16: PM2 log: pid=3363314 msg=process tree killed (3 pids)
PM2        | 2026-06-08T12:35:16: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-08T12:35:16: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-08T12:40:30: PM2 log: Stopping app:ms-allis-frontend id:0
PM2        | 2026-06-08T12:40:30: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-08T12:40:30: PM2 log: pid=3364388 msg=process tree killed (3 pids)
PM2        | 2026-06-08T12:40:30: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-08T12:40:30: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-08T12:42:58: PM2 log: Stopping app:ms-allis-frontend id:0
PM2        | 2026-06-08T12:42:58: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-08T12:42:59: PM2 log: pid=3373190 msg=process tree killed (3 pids)
PM2        | 2026-06-08T12:42:59: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-08T12:42:59: PM2 log: App [ms-allis-frontend:0] online
PM2        | 2026-06-08T12:44:25: PM2 log: Stopping app:ms-allis-frontend id:0
PM2        | 2026-06-08T12:44:25: PM2 log: App [ms-allis-frontend:0] exited with code [0] via signal [SIGINT]
PM2        | 2026-06-08T12:44:25: PM2 log: pid=3375967 msg=process tree killed (3 pids)
PM2        | 2026-06-08T12:44:25: PM2 log: App [ms-allis-frontend:0] starting in -fork mode-
PM2        | 2026-06-08T12:44:25: PM2 log: App [ms-allis-frontend:0] online

/home/cakidd/.pm2/logs/ms-allis-frontend-error.log last 120 lines:
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/bin/next:105:856 {
0|ms-allis |   code: 'EADDRINUSE',
0|ms-allis |   errno: -98,
0|ms-allis |   syscall: 'listen',
0|ms-allis |   address: '::',
0|ms-allis |   port: 3001
0|ms-allis | }
0|ms-allis |  ⨯ Failed to start server
0|ms-allis | Error: listen EADDRINUSE: address already in use :::3001
0|ms-allis |     at Server.setupListenHandle [as _listen2] (node:net:1908:16)
0|ms-allis |     at listenInCluster (node:net:1965:12)
0|ms-allis |     at Server.listen (node:net:2067:7)
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/server/lib/start-server.js:280:16
0|ms-allis |     at new Promise (<anonymous>)
0|ms-allis |     at startServer (/opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/server/lib/start-server.js:191:11)
0|ms-allis |     at Module.nextStart (/opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/cli/next-start.js:25:40)
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/bin/next:105:856 {
0|ms-allis |   code: 'EADDRINUSE',
0|ms-allis |   errno: -98,
0|ms-allis |   syscall: 'listen',
0|ms-allis |   address: '::',
0|ms-allis |   port: 3001
0|ms-allis | }
0|ms-allis |  ⨯ Failed to start server
0|ms-allis | Error: listen EADDRINUSE: address already in use :::3001
0|ms-allis |     at Server.setupListenHandle [as _listen2] (node:net:1908:16)
0|ms-allis |     at listenInCluster (node:net:1965:12)
0|ms-allis |     at Server.listen (node:net:2067:7)
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/server/lib/start-server.js:280:16
0|ms-allis |     at new Promise (<anonymous>)
0|ms-allis |     at startServer (/opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/server/lib/start-server.js:191:11)
0|ms-allis |     at Module.nextStart (/opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/cli/next-start.js:25:40)
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/bin/next:105:856 {
0|ms-allis |   code: 'EADDRINUSE',
0|ms-allis |   errno: -98,
0|ms-allis |   syscall: 'listen',
0|ms-allis |   address: '::',
0|ms-allis |   port: 3001
0|ms-allis | }
0|ms-allis |  ⨯ Failed to start server
0|ms-allis | Error: listen EADDRINUSE: address already in use :::3001
0|ms-allis |     at Server.setupListenHandle [as _listen2] (node:net:1908:16)
0|ms-allis |     at listenInCluster (node:net:1965:12)
0|ms-allis |     at Server.listen (node:net:2067:7)
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/server/lib/start-server.js:280:16
0|ms-allis |     at new Promise (<anonymous>)
0|ms-allis |     at startServer (/opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/server/lib/start-server.js:191:11)
0|ms-allis |     at Module.nextStart (/opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/cli/next-start.js:25:40)
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/bin/next:105:856 {
0|ms-allis |   code: 'EADDRINUSE',
0|ms-allis |   errno: -98,
0|ms-allis |   syscall: 'listen',
0|ms-allis |   address: '::',
0|ms-allis |   port: 3001
0|ms-allis | }
0|ms-allis |  ⨯ Failed to start server
0|ms-allis | Error: listen EADDRINUSE: address already in use :::3001
0|ms-allis |     at Server.setupListenHandle [as _listen2] (node:net:1908:16)
0|ms-allis |     at listenInCluster (node:net:1965:12)
0|ms-allis |     at Server.listen (node:net:2067:7)
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/server/lib/start-server.js:280:16
0|ms-allis |     at new Promise (<anonymous>)
0|ms-allis |     at startServer (/opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/server/lib/start-server.js:191:11)
0|ms-allis |     at Module.nextStart (/opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/cli/next-start.js:25:40)
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/bin/next:105:856 {
0|ms-allis |   code: 'EADDRINUSE',
0|ms-allis |   errno: -98,
0|ms-allis |   syscall: 'listen',
0|ms-allis |   address: '::',
0|ms-allis |   port: 3001
0|ms-allis | }
0|ms-allis |  ⨯ Failed to start server
0|ms-allis | Error: listen EADDRINUSE: address already in use :::3001
0|ms-allis |     at Server.setupListenHandle [as _listen2] (node:net:1908:16)
0|ms-allis |     at listenInCluster (node:net:1965:12)
0|ms-allis |     at Server.listen (node:net:2067:7)
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/server/lib/start-server.js:280:16
0|ms-allis |     at new Promise (<anonymous>)
0|ms-allis |     at startServer (/opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/server/lib/start-server.js:191:11)
0|ms-allis |     at Module.nextStart (/opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/cli/next-start.js:25:40)
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/bin/next:105:856 {
0|ms-allis |   code: 'EADDRINUSE',
0|ms-allis |   errno: -98,
0|ms-allis |   syscall: 'listen',
0|ms-allis |   address: '::',
0|ms-allis |   port: 3001
0|ms-allis | }
0|ms-allis |  ⨯ Failed to start server
0|ms-allis | Error: listen EADDRINUSE: address already in use :::3001
0|ms-allis |     at Server.setupListenHandle [as _listen2] (node:net:1908:16)
0|ms-allis |     at listenInCluster (node:net:1965:12)
0|ms-allis |     at Server.listen (node:net:2067:7)
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/server/lib/start-server.js:280:16
0|ms-allis |     at new Promise (<anonymous>)
0|ms-allis |     at startServer (/opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/server/lib/start-server.js:191:11)
0|ms-allis |     at Module.nextStart (/opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/cli/next-start.js:25:40)
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/bin/next:105:856 {
0|ms-allis |   code: 'EADDRINUSE',
0|ms-allis |   errno: -98,
0|ms-allis |   syscall: 'listen',
0|ms-allis |   address: '::',
0|ms-allis |   port: 3001
0|ms-allis | }
0|ms-allis |  ⨯ Failed to start server
0|ms-allis | Error: listen EADDRINUSE: address already in use :::3001
0|ms-allis |     at Server.setupListenHandle [as _listen2] (node:net:1908:16)
0|ms-allis |     at listenInCluster (node:net:1965:12)
0|ms-allis |     at Server.listen (node:net:2067:7)
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/server/lib/start-server.js:280:16
0|ms-allis |     at new Promise (<anonymous>)
0|ms-allis |     at startServer (/opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/server/lib/start-server.js:191:11)
0|ms-allis |     at Module.nextStart (/opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/cli/next-start.js:25:40)
0|ms-allis |     at /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/next/dist/bin/next:105:856 {
0|ms-allis |   code: 'EADDRINUSE',
0|ms-allis |   errno: -98,
0|ms-allis |   syscall: 'listen',
0|ms-allis |   address: '::',
0|ms-allis |   port: 3001
0|ms-allis | }
0|ms-allis | Killed

/home/cakidd/.pm2/logs/ms-allis-frontend-out.log last 120 lines:
0|ms-allis | 
0|ms-allis |  ✓ Starting...
0|ms-allis |  ✓ Ready in 197ms
0|ms-allis | 
0|ms-allis | > ms-allis-frontend@1.0.0 start
0|ms-allis | > next start -p 3001
0|ms-allis | 
0|ms-allis |   ▲ Next.js 14.2.29
0|ms-allis |   - Local:        http://localhost:3001
0|ms-allis | 
0|ms-allis |  ✓ Starting...
0|ms-allis |  ✓ Ready in 193ms
0|ms-allis | 
0|ms-allis | > ms-allis-frontend@1.0.0 start
0|ms-allis | > next start -p 3001
0|ms-allis | 
0|ms-allis |   ▲ Next.js 14.2.29
0|ms-allis |   - Local:        http://localhost:3001
0|ms-allis | 
0|ms-allis |  ✓ Starting...
0|ms-allis |  ✓ Ready in 183ms
0|ms-allis | 
0|ms-allis | > ms-allis-frontend@1.0.0 start
0|ms-allis | > next start -p 3001
0|ms-allis | 
0|ms-allis |   ▲ Next.js 14.2.29
0|ms-allis |   - Local:        http://localhost:3001
0|ms-allis | 
0|ms-allis |  ✓ Starting...
0|ms-allis |  ✓ Ready in 188ms
0|ms-allis | 
0|ms-allis | > ms-allis-frontend@1.0.0 start
0|ms-allis | > next start -p 3001
0|ms-allis | 
0|ms-allis |   ▲ Next.js 14.2.29
0|ms-allis |   - Local:        http://localhost:3001
0|ms-allis | 
0|ms-allis |  ✓ Starting...
0|ms-allis |  ✓ Ready in 187ms
0|ms-allis | 
0|ms-allis | > ms-allis-frontend@1.0.0 start
0|ms-allis | > next start -p 3001
0|ms-allis | 
0|ms-allis |   ▲ Next.js 14.2.29
0|ms-allis |   - Local:        http://localhost:3001
0|ms-allis | 
0|ms-allis |  ✓ Starting...
0|ms-allis |  ✓ Ready in 202ms
0|ms-allis | 
0|ms-allis | > ms-allis-frontend@1.0.0 start
0|ms-allis | > next start -p 3001
0|ms-allis | 
0|ms-allis |   ▲ Next.js 14.2.29
0|ms-allis |   - Local:        http://localhost:3001
0|ms-allis | 
0|ms-allis |  ✓ Starting...
0|ms-allis |  ✓ Ready in 191ms
0|ms-allis | 
0|ms-allis | > ms-allis-frontend@1.0.0 start
0|ms-allis | > next start -p 3001
0|ms-allis | 
0|ms-allis |   ▲ Next.js 14.2.29
0|ms-allis |   - Local:        http://localhost:3001
0|ms-allis | 
0|ms-allis |  ✓ Starting...
0|ms-allis |  ✓ Ready in 186ms
0|ms-allis | 
0|ms-allis | > ms-allis-frontend@1.0.0 start
0|ms-allis | > next start -p 3001
0|ms-allis | 
0|ms-allis |   ▲ Next.js 14.2.29
0|ms-allis |   - Local:        http://localhost:3001
0|ms-allis | 
0|ms-allis |  ✓ Starting...
0|ms-allis |  ✓ Ready in 200ms
0|ms-allis | 
0|ms-allis | > ms-allis-frontend@1.0.0 start
0|ms-allis | > next start -p 3001
0|ms-allis | 
0|ms-allis |   ▲ Next.js 14.2.29
0|ms-allis |   - Local:        http://localhost:3001
0|ms-allis | 
0|ms-allis |  ✓ Starting...
0|ms-allis |  ✓ Ready in 192ms
0|ms-allis | 
0|ms-allis | > ms-allis-frontend@1.0.0 start
0|ms-allis | > next start -p 3001
0|ms-allis | 
0|ms-allis |   ▲ Next.js 14.2.29
0|ms-allis |   - Local:        http://localhost:3001
0|ms-allis | 
0|ms-allis |  ✓ Starting...
0|ms-allis |  ✓ Ready in 187ms
0|ms-allis | 
0|ms-allis | > ms-allis-frontend@1.0.0 start
0|ms-allis | > next start -p 3001
0|ms-allis | 
0|ms-allis |   ▲ Next.js 14.2.29
0|ms-allis |   - Local:        http://localhost:3001
0|ms-allis | 
0|ms-allis |  ✓ Starting...
0|ms-allis |  ✓ Ready in 184ms
0|ms-allis | 
0|ms-allis | > ms-allis-frontend@1.0.0 start
0|ms-allis | > next start -p 3001
0|ms-allis | 
0|ms-allis |   ▲ Next.js 14.2.29
0|ms-allis |   - Local:        http://localhost:3001
0|ms-allis | 
0|ms-allis |  ✓ Starting...
0|ms-allis |  ✓ Ready in 189ms
0|ms-allis | 
0|ms-allis | > ms-allis-frontend@1.0.0 start
0|ms-allis | > next start -p 3001
0|ms-allis | 
0|ms-allis |   ▲ Next.js 14.2.29
0|ms-allis |   - Local:        http://localhost:3001
0|ms-allis | 
0|ms-allis |  ✓ Starting...
0|ms-allis |  ✓ Ready in 185ms

Jun 08 12:49:51 cakidd-Legion-5-16IRX9 python3[3388001]: ERROR:    [Errno 98] error while attempting to bind on address ('0.0.0.0', 8018): address already in use
Jun 08 12:49:51 cakidd-Legion-5-16IRX9 python3[3388001]: INFO:     Waiting for application shutdown.
Jun 08 12:49:51 cakidd-Legion-5-16IRX9 python3[3388001]: INFO:     Application shutdown complete.
Jun 08 12:49:51 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Main process exited, code=exited, status=1/FAILURE
Jun 08 12:49:51 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Failed with result 'exit-code'.
Jun 08 12:49:52 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Scheduled restart job, restart counter is at 132372.
Jun 08 12:49:52 cakidd-Legion-5-16IRX9 systemd[1]: Started qualia-orchestrator.service - Qualia Unified Orchestrator 69-DGM.
Jun 08 12:49:52 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Main process exited, code=exited, status=203/EXEC
Jun 08 12:49:52 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Failed with result 'exit-code'.
Jun 08 12:49:56 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Scheduled restart job, restart counter is at 14380.
Jun 08 12:49:56 cakidd-Legion-5-16IRX9 systemd[1]: Started msjarvis-production-chat.service - Ms. Allis Production Chat Pipeline (port 8018).
Jun 08 12:49:56 cakidd-Legion-5-16IRX9 python3[3388013]: INFO:     Started server process [3388013]
Jun 08 12:49:56 cakidd-Legion-5-16IRX9 python3[3388013]: INFO:     Waiting for application startup.
Jun 08 12:49:56 cakidd-Legion-5-16IRX9 python3[3388013]: INFO:     Application startup complete.
Jun 08 12:49:56 cakidd-Legion-5-16IRX9 python3[3388013]: ERROR:    [Errno 98] error while attempting to bind on address ('0.0.0.0', 8018): address already in use
Jun 08 12:49:56 cakidd-Legion-5-16IRX9 python3[3388013]: INFO:     Waiting for application shutdown.
Jun 08 12:49:56 cakidd-Legion-5-16IRX9 python3[3388013]: INFO:     Application shutdown complete.
Jun 08 12:49:56 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Main process exited, code=exited, status=1/FAILURE
Jun 08 12:49:56 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Failed with result 'exit-code'.
Jun 08 12:49:57 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Scheduled restart job, restart counter is at 132373.
Jun 08 12:49:57 cakidd-Legion-5-16IRX9 systemd[1]: Started qualia-orchestrator.service - Qualia Unified Orchestrator 69-DGM.
Jun 08 12:49:57 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Main process exited, code=exited, status=203/EXEC
Jun 08 12:49:57 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Failed with result 'exit-code'.
Jun 08 12:50:01 cakidd-Legion-5-16IRX9 CRON[3388059]: pam_unix(cron:session): session opened for user cakidd(uid=1000) by cakidd(uid=0)
Jun 08 12:50:01 cakidd-Legion-5-16IRX9 systemd[1]: Starting sysstat-collect.service - system activity accounting tool...
Jun 08 12:50:01 cakidd-Legion-5-16IRX9 CRON[3388060]: pam_unix(cron:session): session opened for user cakidd(uid=1000) by cakidd(uid=0)
Jun 08 12:50:01 cakidd-Legion-5-16IRX9 CRON[3388062]: (cakidd) CMD (/opt/msjarvis-rebuild/scripts/check_proxies.sh >> /home/cakidd/logs/msjarvis-proxy-health.log 2>&1)
Jun 08 12:50:01 cakidd-Legion-5-16IRX9 CRON[3388063]: (cakidd) CMD (/usr/local/bin/jarvis_bbb_watchdog.sh)
Jun 08 12:50:01 cakidd-Legion-5-16IRX9 systemd[1]: sysstat-collect.service: Deactivated successfully.
Jun 08 12:50:01 cakidd-Legion-5-16IRX9 systemd[1]: Finished sysstat-collect.service - system activity accounting tool.
Jun 08 12:50:01 cakidd-Legion-5-16IRX9 CRON[3388060]: pam_unix(cron:session): session closed for user cakidd
Jun 08 12:50:01 cakidd-Legion-5-16IRX9 CRON[3388059]: pam_unix(cron:session): session closed for user cakidd
Jun 08 12:50:01 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Scheduled restart job, restart counter is at 14381.
Jun 08 12:50:01 cakidd-Legion-5-16IRX9 systemd[1]: Started msjarvis-production-chat.service - Ms. Allis Production Chat Pipeline (port 8018).
Jun 08 12:50:02 cakidd-Legion-5-16IRX9 python3[3388153]: INFO:     Started server process [3388153]
Jun 08 12:50:02 cakidd-Legion-5-16IRX9 python3[3388153]: INFO:     Waiting for application startup.
Jun 08 12:50:02 cakidd-Legion-5-16IRX9 python3[3388153]: INFO:     Application startup complete.
Jun 08 12:50:02 cakidd-Legion-5-16IRX9 python3[3388153]: ERROR:    [Errno 98] error while attempting to bind on address ('0.0.0.0', 8018): address already in use
Jun 08 12:50:02 cakidd-Legion-5-16IRX9 python3[3388153]: INFO:     Waiting for application shutdown.
Jun 08 12:50:02 cakidd-Legion-5-16IRX9 python3[3388153]: INFO:     Application shutdown complete.
Jun 08 12:50:02 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Main process exited, code=exited, status=1/FAILURE
Jun 08 12:50:02 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Failed with result 'exit-code'.
Jun 08 12:50:02 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Scheduled restart job, restart counter is at 132374.
Jun 08 12:50:02 cakidd-Legion-5-16IRX9 systemd[1]: Started qualia-orchestrator.service - Qualia Unified Orchestrator 69-DGM.
Jun 08 12:50:02 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Main process exited, code=exited, status=203/EXEC
Jun 08 12:50:02 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Failed with result 'exit-code'.
Jun 08 12:50:07 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Scheduled restart job, restart counter is at 14382.
Jun 08 12:50:07 cakidd-Legion-5-16IRX9 systemd[1]: Started msjarvis-production-chat.service - Ms. Allis Production Chat Pipeline (port 8018).
Jun 08 12:50:07 cakidd-Legion-5-16IRX9 python3[3388185]: INFO:     Started server process [3388185]
Jun 08 12:50:07 cakidd-Legion-5-16IRX9 python3[3388185]: INFO:     Waiting for application startup.
Jun 08 12:50:07 cakidd-Legion-5-16IRX9 python3[3388185]: INFO:     Application startup complete.
Jun 08 12:50:07 cakidd-Legion-5-16IRX9 python3[3388185]: ERROR:    [Errno 98] error while attempting to bind on address ('0.0.0.0', 8018): address already in use
Jun 08 12:50:07 cakidd-Legion-5-16IRX9 python3[3388185]: INFO:     Waiting for application shutdown.
Jun 08 12:50:07 cakidd-Legion-5-16IRX9 python3[3388185]: INFO:     Application shutdown complete.
Jun 08 12:50:07 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Main process exited, code=exited, status=1/FAILURE
Jun 08 12:50:07 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Failed with result 'exit-code'.
Jun 08 12:50:08 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Scheduled restart job, restart counter is at 132375.
Jun 08 12:50:08 cakidd-Legion-5-16IRX9 systemd[1]: Started qualia-orchestrator.service - Qualia Unified Orchestrator 69-DGM.
Jun 08 12:50:08 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Main process exited, code=exited, status=203/EXEC
Jun 08 12:50:08 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Failed with result 'exit-code'.
Jun 08 12:50:12 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Scheduled restart job, restart counter is at 14383.
Jun 08 12:50:12 cakidd-Legion-5-16IRX9 systemd[1]: Started msjarvis-production-chat.service - Ms. Allis Production Chat Pipeline (port 8018).
Jun 08 12:50:13 cakidd-Legion-5-16IRX9 python3[3388213]: INFO:     Started server process [3388213]
Jun 08 12:50:13 cakidd-Legion-5-16IRX9 python3[3388213]: INFO:     Waiting for application startup.
Jun 08 12:50:13 cakidd-Legion-5-16IRX9 python3[3388213]: INFO:     Application startup complete.
Jun 08 12:50:13 cakidd-Legion-5-16IRX9 python3[3388213]: ERROR:    [Errno 98] error while attempting to bind on address ('0.0.0.0', 8018): address already in use
Jun 08 12:50:13 cakidd-Legion-5-16IRX9 python3[3388213]: INFO:     Waiting for application shutdown.
Jun 08 12:50:13 cakidd-Legion-5-16IRX9 python3[3388213]: INFO:     Application shutdown complete.
Jun 08 12:50:13 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Main process exited, code=exited, status=1/FAILURE
Jun 08 12:50:13 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Failed with result 'exit-code'.
Jun 08 12:50:13 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Scheduled restart job, restart counter is at 132376.
Jun 08 12:50:13 cakidd-Legion-5-16IRX9 systemd[1]: Started qualia-orchestrator.service - Qualia Unified Orchestrator 69-DGM.
Jun 08 12:50:13 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Main process exited, code=exited, status=203/EXEC
Jun 08 12:50:13 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Failed with result 'exit-code'.
Jun 08 12:50:18 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Scheduled restart job, restart counter is at 14384.
Jun 08 12:50:18 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Scheduled restart job, restart counter is at 132377.
Jun 08 12:50:18 cakidd-Legion-5-16IRX9 systemd[1]: Started msjarvis-production-chat.service - Ms. Allis Production Chat Pipeline (port 8018).
Jun 08 12:50:18 cakidd-Legion-5-16IRX9 systemd[1]: Started qualia-orchestrator.service - Qualia Unified Orchestrator 69-DGM.
Jun 08 12:50:18 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Main process exited, code=exited, status=203/EXEC
Jun 08 12:50:18 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Failed with result 'exit-code'.
Jun 08 12:50:18 cakidd-Legion-5-16IRX9 python3[3388228]: INFO:     Started server process [3388228]
Jun 08 12:50:18 cakidd-Legion-5-16IRX9 python3[3388228]: INFO:     Waiting for application startup.
Jun 08 12:50:18 cakidd-Legion-5-16IRX9 python3[3388228]: INFO:     Application startup complete.
Jun 08 12:50:18 cakidd-Legion-5-16IRX9 python3[3388228]: ERROR:    [Errno 98] error while attempting to bind on address ('0.0.0.0', 8018): address already in use
Jun 08 12:50:18 cakidd-Legion-5-16IRX9 python3[3388228]: INFO:     Waiting for application shutdown.
Jun 08 12:50:18 cakidd-Legion-5-16IRX9 python3[3388228]: INFO:     Application shutdown complete.
Jun 08 12:50:18 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Main process exited, code=exited, status=1/FAILURE
Jun 08 12:50:18 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Failed with result 'exit-code'.
Jun 08 12:50:23 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Scheduled restart job, restart counter is at 132378.
Jun 08 12:50:23 cakidd-Legion-5-16IRX9 systemd[1]: Started qualia-orchestrator.service - Qualia Unified Orchestrator 69-DGM.
Jun 08 12:50:23 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Main process exited, code=exited, status=203/EXEC
Jun 08 12:50:23 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Failed with result 'exit-code'.
Jun 08 12:50:23 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Scheduled restart job, restart counter is at 14385.
Jun 08 12:50:23 cakidd-Legion-5-16IRX9 systemd[1]: Started msjarvis-production-chat.service - Ms. Allis Production Chat Pipeline (port 8018).
Jun 08 12:50:24 cakidd-Legion-5-16IRX9 python3[3388279]: INFO:     Started server process [3388279]
Jun 08 12:50:24 cakidd-Legion-5-16IRX9 python3[3388279]: INFO:     Waiting for application startup.
Jun 08 12:50:24 cakidd-Legion-5-16IRX9 python3[3388279]: INFO:     Application startup complete.
Jun 08 12:50:24 cakidd-Legion-5-16IRX9 python3[3388279]: ERROR:    [Errno 98] error while attempting to bind on address ('0.0.0.0', 8018): address already in use
Jun 08 12:50:24 cakidd-Legion-5-16IRX9 python3[3388279]: INFO:     Waiting for application shutdown.
Jun 08 12:50:24 cakidd-Legion-5-16IRX9 python3[3388279]: INFO:     Application shutdown complete.
Jun 08 12:50:24 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Main process exited, code=exited, status=1/FAILURE
Jun 08 12:50:24 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Failed with result 'exit-code'.
Jun 08 12:50:28 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Scheduled restart job, restart counter is at 132379.
Jun 08 12:50:28 cakidd-Legion-5-16IRX9 systemd[1]: Started qualia-orchestrator.service - Qualia Unified Orchestrator 69-DGM.
Jun 08 12:50:28 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Main process exited, code=exited, status=203/EXEC
Jun 08 12:50:28 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Failed with result 'exit-code'.
Jun 08 12:50:29 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Scheduled restart job, restart counter is at 14386.
Jun 08 12:50:29 cakidd-Legion-5-16IRX9 systemd[1]: Started msjarvis-production-chat.service - Ms. Allis Production Chat Pipeline (port 8018).
Jun 08 12:50:29 cakidd-Legion-5-16IRX9 python3[3388317]: INFO:     Started server process [3388317]
Jun 08 12:50:29 cakidd-Legion-5-16IRX9 python3[3388317]: INFO:     Waiting for application startup.
Jun 08 12:50:29 cakidd-Legion-5-16IRX9 python3[3388317]: INFO:     Application startup complete.
Jun 08 12:50:29 cakidd-Legion-5-16IRX9 python3[3388317]: ERROR:    [Errno 98] error while attempting to bind on address ('0.0.0.0', 8018): address already in use
Jun 08 12:50:29 cakidd-Legion-5-16IRX9 python3[3388317]: INFO:     Waiting for application shutdown.
Jun 08 12:50:29 cakidd-Legion-5-16IRX9 python3[3388317]: INFO:     Application shutdown complete.
Jun 08 12:50:29 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Main process exited, code=exited, status=1/FAILURE
Jun 08 12:50:29 cakidd-Legion-5-16IRX9 systemd[1]: msjarvis-production-chat.service: Failed with result 'exit-code'.
Jun 08 12:50:34 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Scheduled restart job, restart counter is at 132380.
Jun 08 12:50:34 cakidd-Legion-5-16IRX9 systemd[1]: Started qualia-orchestrator.service - Qualia Unified Orchestrator 69-DGM.
Jun 08 12:50:34 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Main process exited, code=exited, status=203/EXEC
Jun 08 12:50:34 cakidd-Legion-5-16IRX9 systemd[1]: qualia-orchestrator.service: Failed with result 'exit-code'.
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

