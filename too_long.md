(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend-tsx$ sed -n '457,615p' /mnt/spiritual_drive/msjarvis-rebuild/auth_router.py
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
        temp_pw         = _sec.token_urlsafe(16)
        proposed_userid = app.get("proposed_userid", public_uuid)
        _ueid_hex       = public_uuid.replace("-", "").upper()
        _ueid           = f"MS-JARVIS-{_ueid_hex[:16]}"
        r.set(f"email_to_uuid:{email}", public_uuid)
        r.hset(f"user:{public_uuid}", mapping={
            "email":           email,
            "name":            app.get("name", ""),
            "proposed_userid": proposed_userid,
            "userid":          proposed_userid,
            "county":          app.get("county", ""),
            "ueid":            _ueid,
            "temp_password":   temp_pw,
            "status":          "approved_pending_login",
            "is_public":       "false",
            "visibility":      "private",
            "roles":           "user",
            "bsc_status":      "prefer_not_to_say",
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
        _dsn = _os.environ.get("DATABASE_URL") or _os.environ.get("POSTGRES_DSN")
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
                    "INSERT INTO founder_tokens (serial_number, ueid, cohort, allocation_type) "
                    "VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING",
                    (_next, _ueid, "phase_0", _alloc)
                )
                logger.info(f"[FOUNDER] Minted token #{_next} ({_alloc}) for {_ueid}")
                # Write founding grant ledger entry for red_team members
                if _alloc == "red_team":
                    _cur.execute("SELECT COUNT(*) FROM mountainshares_ledger WHERE ueid = %s AND event_type = 'founding_grant'", (_ueid,))
                    if _cur.fetchone()[0] == 0:
                     _cur.execute(
                        "INSERT INTO mountainshares_ledger "
                        "(ueid, event_type, amount, provenance_ref, notes) "
                        "VALUES (%s, %s, %s, %s, %s)",
                        (_ueid, "founding_grant", 100.0000,
                         f"PHASE0_RED_TEAM_GRANT_{str(_next).zfill(3)}",
                         "Phase 0 red_team founding allocation")
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
        import traceback as _tb
        logger.error(f"[FOUNDER] Auto-mint failed: {_e}\n{_tb.format_exc()}")

    temp_password = user.get("temp_password", "")
    name          = user.get("name", email)
    if not temp_password:
        return ApproveResponse(
            application_id=application_id,
            public_uuid=public_uuid,
            email=email,
            message="User has already completed onboarding. No email sent.",
        )
    # Set temp-password expiry window: 72 hours from approval
    r.set(f"temp_pw_expires:{public_uuid}", "1", ex=60 * 60 * 72)

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


(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend-tsx$ sed -n '340,400p' /mnt/spiritual_drive/msjarvis-rebuild/auth_router.py
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
    _ueid = user.get("ueid", "")
    return MeResponse(
        userid=sub,
        uei=_ueid,
        ueid=_ueid,
        roles=roles,
        county=user.get("county", ""),
        name=user.get("name", ""),
        email=user.get("email", ""),
        status=user.get("status", ""),
        visibility=user.get("visibility", "private"),
        bsc_status=user.get("bsc_status", "prefer_not_to_say"),
        first_login_at=user.get("first_login_at", None),
    )



# ── Admin: chat metrics ──────────────────────────────────────────────────────

@auth_router.get("/admin/chat-metrics")
async def admin_chat_metrics(payload: Annotated[dict, Depends(_current_user)]):
    if "admin" not in payload.get("roles", []):
        raise HTTPException(status_code=403, detail="Admin required")
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend-tsx$ sed -n '160,210p' /mnt/spiritual_drive/msjarvis-rebuild/auth_router.py


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


(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend-tsx$ sed -n '160,210p' /mnt/spiritual_drive/msjarvis-rebuild/auth_router.py


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


(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend-tsx$ cat /opt/msjarvis-rebuild/ms-allis-frontend-tsx/app/admin/page.tsx
"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { MsAllisPortrait } from "@/components/MsAllisPortrait";
import { HeartOrnament } from "@/components/HeartOrnament";
import {
  api,
  adminKey,
  ApiError,
  type PendingApplication,
  type ApplicationListItem,
} from "@/lib/api";

type AdminState = "key-prompt" | "loading" | "ready" | "error";

export default function AdminPage() {
  const [state, setState] = useState<AdminState>("key-prompt");
  const [pending, setPending] = useState<ApplicationListItem[]>([]);
  const [error, setError] = useState("");
  const [keyInput, setKeyInput] = useState("");

  // On mount, check for an existing admin key in sessionStorage
  useEffect(() => {
    if (adminKey.get()) {
      loadPending();
    }
  }, []);

  async function loadPending() {
    setState("loading");
    setError("");
    try {
      const data = await api.pending();
      setPending(data.pending);
      setState("ready");
    } catch (err: unknown) {
      if (err instanceof ApiError && err.status === 403) {
        adminKey.clear();
        setState("key-prompt");
        setError("That key was rejected. Try again.");
        return;
      }
      const message =
        err instanceof ApiError
          ? err.detail
          : err instanceof Error
            ? err.message
            : "Couldn't load pending applications.";
      setError(message);
      setState("error");
    }
  }

  function handleKeySubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!keyInput.trim()) return;
    adminKey.set(keyInput.trim());
    setKeyInput("");
    loadPending();
  }

  async function handleApprove(ueid: string) {
    if (!confirm(`Approve ${ueid}? This will email the applicant their magic link.`)) return;
    try {
      await api.approve(ueid);
      setPending((prev) => prev.filter((a) => a.ueid !== ueid));
    } catch (err: unknown) {
      const message = err instanceof ApiError ? err.detail : "Approval failed.";
      alert(`Approve failed: ${message}`);
    }
  }

  async function handleDeny(ueid: string) {
    if (!confirm(`Deny ${ueid}? The applicant will be notified.`)) return;
    try {
      await api.deny(ueid);
      setPending((prev) => prev.filter((a) => a.ueid !== ueid));
    } catch (err: unknown) {
      const message = err instanceof ApiError ? err.detail : "Denial failed.";
      alert(`Deny failed: ${message}`);
    }
  }

  function handleSignOutAdmin() {
    adminKey.clear();
    setPending([]);
    setState("key-prompt");
  }

  // ------- Key prompt -------
  if (state === "key-prompt") {
    return (
      <main className="min-h-screen flex items-center justify-center px-6 py-20">
        <div className="max-w-md w-full">
          <div className="text-center mb-10">
            <MsAllisPortrait size="medium" withFrame className="mb-8" />
            <h1 className="font-display italic text-display text-teal-deep mb-3">
              Admin
            </h1>
            <p className="font-body text-sm text-ink-fade italic">
              Enter the admin key to manage applications.
            </p>
          </div>
          <form onSubmit={handleKeySubmit} className="space-y-4 surface p-7">
            <input
              type="password"
              autoFocus
              value={keyInput}
              onChange={(e) => setKeyInput(e.target.value)}
              placeholder="Admin key"
              className="input-warm font-mono text-center"
            />
            <button type="submit" className="btn-terracotta w-full">
              Continue
            </button>
            {error && (
              <p className="text-sm text-terracotta-deep italic text-center">{error}</p>
            )}
          </form>
          <p className="font-body text-xs text-ink-fade italic text-center mt-6">
            Stored only in this browser tab. Closing the tab signs you out.
          </p>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen">
      <header className="bg-cream-light border-b border-cream-deep">
        <div className="max-w-6xl mx-auto px-6 md:px-10 py-5 flex items-center justify-between">
          <Link href="/" className="flex items-center gap-3 group">
            <MsAllisPortrait size="small" withFrame={false} className="w-10 h-10 rounded-full" />
            <span className="font-display italic text-lg text-teal-deep group-hover:text-terracotta transition-colors">
              Ms. Allis
            </span>
            <span className="font-display italic text-xs tracking-widest uppercase text-ink-fade ml-2">
              · Admin
            </span>
          </Link>
          <div className="flex items-center gap-6">
            <button
              onClick={loadPending}
              className="font-body text-sm text-ink-fade hover:text-teal underline decoration-cream-deep hover:decoration-teal underline-offset-4 transition-colors"
            >
              Refresh
            </button>
            <button
              onClick={handleSignOutAdmin}
              className="font-body text-sm text-ink-fade hover:text-terracotta underline decoration-cream-deep hover:decoration-terracotta underline-offset-4 transition-colors"
            >
              Sign out
            </button>
          </div>
        </div>
      </header>

      <div className="max-w-6xl mx-auto px-6 md:px-10 py-12">
        <div className="mb-10">
          <h1 className="font-display text-display text-teal-deep mb-2">
            Pending applications
          </h1>
          <p className="font-body text-sm text-ink-fade italic">
            {state === "loading" && "Loading…"}
            {state === "ready" && (
              pending.length === 0
                ? "No pending applications. All caught up."
                : `${pending.length} ${pending.length === 1 ? "application" : "applications"} waiting`
            )}
            {state === "error" && error}
          </p>
        </div>

        {state === "ready" && pending.length > 0 && (
          <div className="space-y-6">
            {pending.map((app) => (
              <ApplicationCard
                key={app.ueid}
                app={app}
                onApprove={() => handleApprove(app.ueid)}
                onDeny={() => handleDeny(app.ueid)}
              />
            ))}
          </div>
        )}

        {state === "ready" && pending.length === 0 && (
          <div className="text-center py-20">
            <HeartOrnament className="w-12 h-12 text-cream-deep mx-auto mb-6" />
            <p className="font-display italic text-xl text-ink-fade">
              Nothing pending. Quiet day.
            </p>
          </div>
        )}
      </div>
    </main>
  );
}

function ApplicationCard({
  app,
  onApprove,
  onDeny,
}: {
  app: ApplicationListItem;
  onApprove: () => void;
  onDeny: () => void;
}) {
  const submittedDate = new Date(app.submitted_at).toLocaleString("en-US", {
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "2-digit",
  });

  return (
    <div className="surface p-7">
      <div className="grid md:grid-cols-12 gap-6">
        <div className="md:col-span-8">
          <div className="flex items-baseline gap-3 mb-3 flex-wrap">
            <h2 className="font-display text-2xl text-teal-deep">{app.name}</h2>
            <span className="font-body text-sm text-ink-fade italic">
              {app.county} County · {submittedDate}
            </span>
          </div>
          <div className="flex items-center gap-2 mb-5">
            <span className="tag-mono">{app.ueid}</span>
            <span className="tag-mono">{app.email}</span>
            <span className="tag-mono">v{app.agreement_version}</span>
          </div>
          <div className="border-l-2 border-cream-deep pl-4">
            <div className="font-display italic text-xs uppercase tracking-widest text-terracotta mb-2">
              Why they want to participate
            </div>
            <p className="font-body text-base text-ink-soft leading-relaxed whitespace-pre-line">
              {app.motivation}
            </p>
          </div>
        </div>

        <div className="md:col-span-4 flex md:flex-col gap-3 md:items-stretch">
          <button onClick={onApprove} className="btn-primary flex-1">
            Approve
          </button>
          <button onClick={onDeny} className="btn-secondary flex-1">
            Deny
          </button>
        </div>
      </div>
    </div>
  );
}
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend-tsx$ cat /opt/msjarvis-rebuild/ms-allis-frontend-tsx/app/portal/page.tsx
// app/portal/page.tsx
"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import {
  api,
  ApiError,
  session,
  ApplicationListItem,
  MeResponse,
} from "@/lib/api";
import { portalApi, BalancesResponse, LedgerEntry, LedgerResponse } from "@/lib/portal";
import { ChatPanel } from "@/components/ChatPanel";
import { FounderToken } from "@/components/FounderToken";
import { MsAllisPortrait } from "@/components/MsAllisPortrait";
import { HeartOrnament } from "@/components/HeartOrnament";
import { MountainSilhouette } from "@/components/MountainSilhouette";

type State = "checking" | "ready";
type Tab = "champion" | "admin";

export default function PortalPage() {
  const router = useRouter();
  const [state, setState] = useState<State>("checking");
  const [me, setMe] = useState<MeResponse | null>(null);
  const [balances, setBalances] = useState<BalancesResponse | null>(null);
  const [tab, setTab] = useState<Tab>("champion");

  // Admin tab state
  const [pending, setPending] = useState<ApplicationListItem[]>([]);
  const [pendingState, setPendingState] = useState<"idle" | "loading" | "ready" | "error">("idle");
  const [pendingError, setPendingError] = useState("");
  const [actingOn, setActingOn] = useState<string | null>(null);
  const [denyingId, setDenyingId] = useState<string | null>(null);
  const [denyReason, setDenyReason] = useState("");

  useEffect(() => {
    api.me()
      .then((m) => {
        setMe(m);
        setState("ready");
        // Fetch balances in parallel; fail silently
        portalApi.myBalances()
          .then((b) => setBalances(b))
          .catch(() => setBalances(null));
      })
      .catch(() => {
        session.clear();
        router.push("/login");
      });
  }, [router]);

  const isAdmin = me?.roles?.includes("admin") ?? false;

  useEffect(() => {
    if (tab !== "admin" || !isAdmin || pendingState !== "idle") return;
    loadPending();
  }, [tab, isAdmin, pendingState]);

  async function loadPending() {
    setPendingState("loading");
    setPendingError("");
    try {
      const result = await api.pending();
      setPending(result.applications || []);
      setPendingState("ready");
    } catch (err) {
      setPendingError(err instanceof ApiError ? err.detail : "Failed to load");
      setPendingState("error");
    }
  }

  async function handleApprove(id: string) {
    setActingOn(id);
    setPendingError("");
    try {
      await api.approve(id);
      await loadPending();
    } catch (err) {
      setPendingError(err instanceof ApiError ? err.detail : "Approve failed");
    }
    setActingOn(null);
  }

  async function handleDeny(id: string) {
    if (denyReason.trim().length < 5) {
      setPendingError("Denial reason must be at least 5 characters.");
      return;
    }
    setActingOn(id);
    setPendingError("");
    try {
      await api.deny(id, denyReason.trim());
      setDenyingId(null);
      setDenyReason("");
      await loadPending();
    } catch (err) {
      setPendingError(err instanceof ApiError ? err.detail : "Deny failed");
    }
    setActingOn(null);
  }

  function handleSignOut() {
    session.clear();
    router.push("/");
  }

  if (state === "checking") {
    return (
      <main className="min-h-screen bg-cream flex items-center justify-center">
        <p className="font-display italic text-ink-fade">Checking your session…</p>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-cream pb-12">
      <header className="border-b border-cream-deep bg-bone">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <MsAllisPortrait size="small" withFrame={false} className="w-24 h-24" />
            <div>
              <p className="font-display text-base text-teal-deep">Ms. Allis</p>
              <p className="font-body text-xs text-ink-fade italic">{me?.userid ?? "—"}</p>
            </div>
          </div>
          <button
            onClick={handleSignOut}
            className="font-body text-sm text-ink-fade hover:text-terracotta transition-colors underline decoration-cream-deep hover:decoration-terracotta underline-offset-4"
          >
            Sign out
          </button>
        </div>
      </header>

      {isAdmin && (
        <div className="border-b border-cream-deep bg-cream">
          <div className="max-w-6xl mx-auto px-6 flex">
            <button
              onClick={() => setTab("champion")}
              className={`px-6 py-3 font-display text-sm transition-colors ${
                tab === "champion" ? "text-teal-deep border-b-2 border-terracotta" : "text-ink-fade hover:text-teal-deep"
              }`}
            >
              My Champion
            </button>
            <button
              onClick={() => setTab("admin")}
              className={`px-6 py-3 font-display text-sm transition-colors ${
                tab === "admin" ? "text-teal-deep border-b-2 border-terracotta" : "text-ink-fade hover:text-teal-deep"
              }`}
            >
              Admin
              {pending.length > 0 && (
                <span className="ml-2 inline-flex items-center justify-center bg-terracotta text-cream-light text-xs px-2 py-0.5 rounded-full">
                  {pending.length}
                </span>
              )}
            </button>
          </div>
        </div>
      )}

      <div className="max-w-6xl mx-auto px-6 pt-10">
        {tab === "champion" && <ChampionDashboard me={me} balances={balances} isAdmin={isAdmin} />}

        {tab === "admin" && isAdmin && (
          <AdminQueue
            applications={pending}
            state={pendingState}
            error={pendingError}
            actingOn={actingOn}
            denyingId={denyingId}
            denyReason={denyReason}
            setDenyingId={setDenyingId}
            setDenyReason={setDenyReason}
            onApprove={handleApprove}
            onDeny={handleDeny}
            onClearError={() => setPendingError("")}
          />
        )}
      </div>

      <div className="mt-16">
        <MountainSilhouette className="text-forest" />
      </div>
    </main>
  );
}

// ────────────────────────────────────────────────────────────────────
// Champion dashboard — data first, identity collapsed at bottom
// ────────────────────────────────────────────────────────────────────

function ChampionDashboard({
  me,
  balances,
  isAdmin,
}: {
  me: MeResponse | null;
  balances: BalancesResponse | null;
  isAdmin: boolean;
}) {
  const [showIdentity, setShowIdentity] = useState(false);
  const [showChat, setShowChat] = useState(false);
  const router = useRouter();
  const [threads, setThreads] = useState<{session_id: string; title: string|null; preview: string; created_at: string; updated_at: string; message_count: number}[]>([])
  const [renamingId, setRenamingId] = useState<string|null>(null)
  const [renameValue, setRenameValue] = useState("")
  const [menuOpenId, setMenuOpenId] = useState<string|null>(null)
  const [deletingId, setDeletingId] = useState<string|null>(null);
  const [activeThread, setActiveThread] = useState<string>(() => {
    if (typeof window === "undefined") return crypto.randomUUID();
    const t = new URLSearchParams(window.location.search).get("thread");
    return t ?? crypto.randomUUID();
  });

  useEffect(() => {
    if (typeof window !== "undefined" && !new URLSearchParams(window.location.search).get("thread")) {
      router.replace(`/portal?thread=${activeThread}`);
    }
  }, []);

  const loadThreads = () => {
    const uid = me?.userid ? `?user_id=${encodeURIComponent(me.userid)}` : ""
    fetch(`/api/conversation/threads${uid}`)
      .then(r => r.json())
      .then(data => { if (data.threads) setThreads(data.threads); })
      .catch(() => {})
  }
  useEffect(() => { loadThreads() }, [activeThread, me?.userid])

  const handleRename = async (session_id: string) => {
    if (!renameValue.trim()) return
    await fetch("/api/conversation/threads", {
      method: "PATCH",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ session_id, title: renameValue.trim() })
    })
    setRenamingId(null)
    setRenameValue("")
    loadThreads()
  }

  const handleDelete = async (session_id: string) => {
    await fetch("/api/conversation/threads", {
      method: "DELETE",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ session_id })
    })
    setDeletingId(null)
    if (session_id === activeThread) newThread()
    else loadThreads()
  }

  const newThread = () => {
    const id = crypto.randomUUID();
    setActiveThread(id);
    router.push(`/portal?thread=${id}`);
  };
  const [showLedger, setShowLedger] = useState(false);
  const [ledger, setLedger] = useState<LedgerResponse | null>(null);
  const [ledgerLoading, setLedgerLoading] = useState(false);
  const [dateFrom, setDateFrom] = useState<string>("");
  const [dateTo, setDateTo] = useState<string>("");

  async function loadLedger(offset: number = 0) {
    setLedgerLoading(true);
    try {
      const data = await portalApi.myLedger(50, offset);
      setLedger(data);
    } catch {
      // fail silently — non-critical
    }
    setLedgerLoading(false);
  }

  const ems = balances?.ems_balance ?? 0;
  const pms = balances?.pms_balance ?? 0;

  return (
    <>
      {/* Hero — smaller than before */}
      <div className="text-center mb-10">
        <div className="flex justify-center mb-4">
          <HeartOrnament className="w-6 h-6 text-terracotta" />
        </div>
        <h1 className="font-display italic text-3xl md:text-4xl text-teal-deep mb-1">
          Welcome, {me?.userid ?? ""}
        </h1>
        <p className="font-body text-sm text-ink-fade italic">
          {me?.county ? `${me.county} County` : "—"}
          {me?.county ? " · " : ""}Community Champion
        </p>
      </div>

      {/* Founder Token + Balances row */}
      <section className="grid md:grid-cols-3 gap-4 mb-6">
        <div className="surface p-6 flex flex-col items-center justify-center text-center">
          {balances?.founder_token ? (
            <>
              <FounderToken
                serialNumber={balances.founder_token.serial_number}
                mintedAt={balances.founder_token.minted_at}
                cohort={balances.founder_token.cohort}
                size={112}
              />
              <p className="font-display text-base text-teal-deep mt-3">
                {balances.founder_token.display}
              </p>
              <p className="font-body text-xs text-ink-fade italic">Phase 0 token holder</p>
            </>
          ) : (
            <>
              <div
                className="rounded-full bg-cream-deep flex items-center justify-center"
                style={{ width: 112, height: 112 }}
              >
                <span className="font-display text-xs text-ink-fade italic">No token yet</span>
              </div>
              <p className="font-display text-base text-ink-fade mt-3 italic">Founder Token</p>
              <p className="font-body text-xs text-ink-fade italic">Coming soon</p>
            </>
          )}
        </div>

        <BalanceCard
          label="Earned MountainShares"
          shortLabel="EMS"
          amount={ems}
          accent="teal"
        />

        <BalanceCard
          label="Purchased MountainShares"
          shortLabel="PMS"
          amount={pms}
          accent="terracotta"
        />
      </section>

      {/* Region scaffolding row */}
      <section className="grid md:grid-cols-3 gap-4 mb-6">
        <PlaceholderCard
          title="Local businesses"
          subtitle={me?.county ? `${me.county} County directory` : "Your county"}
          note="Coming soon"
        />
        <PlaceholderCard
          title="Weather"
          subtitle="Real-time conditions"
          note="Coming soon"
        />
        <PlaceholderCard
          title="County resources"
          subtitle="Public services & support"
          note="Coming soon"
        />
      </section>

      {/* Action buttons */}
      <section className="flex flex-col sm:flex-row gap-3 mb-8 justify-center">
        <button
          onClick={() => setShowChat((v) => !v)}
          className="btn-primary"
        >
          {showChat ? "Hide Ms. Allis" : "Talk to Ms. Allis →"}
        </button>
        <button
          disabled
          className="font-display text-sm bg-cream-deep text-ink-fade py-3 px-6 cursor-not-allowed italic"
          title="Coming soon"
        >
          Enter The Commons →
        </button>
      </section>

      {/* Chat panel — toggles open/closed */}
      {showChat && (
        <section className="mb-6">
          <div className="flex gap-0 border border-border rounded-xl overflow-hidden" style={{height: "600px"}}>
            {/* Thread sidebar */}
            <aside className="w-56 shrink-0 flex flex-col border-r border-border bg-surface overflow-y-auto">
              <div className="flex items-center justify-between px-3 py-2 border-b border-border">
                <span className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">Conversations</span>
                <button
                  onClick={newThread}
                  title="New conversation"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M12 5v14M5 12h14"/>
                  </svg>
                </button>
              </div>
              <ul className="flex-1 overflow-y-auto py-1">
                {threads.length === 0 && (
                  <li className="px-3 py-4 text-xs text-muted-foreground text-center italic">No past conversations</li>
                )}
                {threads.map((t) => (
                  <li key={t.session_id} className="relative group">
                    {renamingId === t.session_id ? (
                      <div className="px-2 py-1.5 flex gap-1">
                        <input
                          autoFocus
                          value={renameValue}
                          onChange={e => setRenameValue(e.target.value)}
                          onKeyDown={e => {
                            if (e.key === "Enter") handleRename(t.session_id)
                            if (e.key === "Escape") { setRenamingId(null); setRenameValue("") }
                          }}
                          className="flex-1 min-w-0 px-1.5 py-0.5 text-xs border border-border rounded bg-surface focus:outline-none focus:border-primary"
                          placeholder="Thread name..."
                        />
                        <button onClick={() => handleRename(t.session_id)} className="text-[10px] text-primary hover:text-primary/80 font-medium px-1" title="Save">✓</button>
                        <button onClick={() => { setRenamingId(null); setRenameValue("") }} className="text-[10px] text-muted-foreground hover:text-foreground px-1" title="Cancel">✕</button>
                      </div>
                    ) : deletingId === t.session_id ? (
                      <div className="px-3 py-2 bg-red-50 border-l-2 border-red-400">
                        <p className="text-[10px] text-red-700 mb-1.5 font-medium">Delete this thread?</p>
                        <div className="flex gap-1.5">
                          <button onClick={() => handleDelete(t.session_id)} className="text-[10px] bg-red-500 text-white px-2 py-0.5 rounded hover:bg-red-600 transition-colors">Delete</button>
                          <button onClick={() => setDeletingId(null)} className="text-[10px] text-muted-foreground hover:text-foreground px-2 py-0.5 rounded border border-border">Cancel</button>
                        </div>
                      </div>
                    ) : (
                      <div className="flex items-center pr-1">
                        <button
                          onClick={() => { setActiveThread(t.session_id); setMenuOpenId(null); router.push(`/portal?thread=${t.session_id}`); }}
                          className={[
                            "flex-1 min-w-0 text-left px-3 py-2 text-xs transition-colors",
                            t.session_id === activeThread
                              ? "bg-primary/10 text-primary font-medium"
                              : "text-muted-foreground hover:bg-muted/50"
                          ].join(" ")}
                          title={t.preview ?? t.session_id}
                        >
                          <span className="block truncate">{t.title || t.preview || "New conversation"}</span>
                          <span className="block text-[10px] text-muted-foreground/60 mt-0.5">
                            {t.updated_at ? new Date(t.updated_at).toLocaleDateString() : ""}
                            {t.message_count ? ` · ${t.message_count} msg` : ""}
                          </span>
                        </button>
                        <div className="relative shrink-0">
                          <button
                            onClick={e => { e.stopPropagation(); setMenuOpenId(menuOpenId === t.session_id ? null : t.session_id) }}
                            className="opacity-0 group-hover:opacity-100 focus:opacity-100 w-6 h-6 flex items-center justify-center text-muted-foreground hover:text-foreground hover:bg-muted rounded transition-all"
                            title="Thread actions" aria-label="Thread actions"
                          >
                            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>
                          </button>
                          {menuOpenId === t.session_id && (
                            <div className="absolute right-0 top-7 z-50 w-32 bg-surface border border-border rounded-lg shadow-lg py-1 text-xs">
                              <button
                                onClick={() => { setRenamingId(t.session_id); setRenameValue(t.title || t.preview || ""); setMenuOpenId(null) }}
                                className="w-full text-left px-3 py-1.5 hover:bg-muted/60 transition-colors flex items-center gap-2"
                              >
                                <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
                                Rename
                              </button>
                              <button
                                onClick={() => { setDeletingId(t.session_id); setMenuOpenId(null) }}
                                className="w-full text-left px-3 py-1.5 hover:bg-red-50 text-red-600 transition-colors flex items-center gap-2"
                              >
                                <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14H6L5 6"/><path d="M10 11v6M14 11v6"/><path d="M9 6V4h6v2"/></svg>
                                Delete
                              </button>
                            </div>
                          )}
                        </div>
                      </div>
                    )}
                  </li>
                ))}
              </ul>
            </aside>

            {/* Chat area */}
            <div className="flex-1 min-w-0 overflow-hidden">
              <ChatPanel userId={me?.userid ?? ""} isAdmin={isAdmin} threadId={activeThread} />
            </div>
          </div>
        </section>
      )}

      {/* Transaction history */}
      <section className="surface mt-4">
        <button
          onClick={() => { setShowLedger(v => !v); if (!showLedger) loadLedger(); }}
          className="w-full px-6 py-4 flex items-center justify-between text-left hover:bg-bone transition-colors"
        >
          <span className="font-display text-base text-teal-deep">Transaction history</span>
          <span className="font-body text-xs text-ink-fade italic">
            {showLedger ? "▼ Hide" : "▶ Show"}{ledger ? ` · ${ledger.total} entries` : ""}
          </span>
        </button>
        {showLedger && (
          <div className="px-6 pb-6 border-t border-cream-deep">
            {ledgerLoading ? (
              <p className="font-body text-sm text-ink-fade italic mt-4">Loading…</p>
            ) : ledger && ledger.entries.length > 0 ? (
<>
                <div className="mt-4 mb-4 flex flex-wrap items-end gap-3 print:hidden">
                  <div>
                    <label className="block font-body text-xs text-ink-fade italic mb-1">From</label>
                    <input
                      type="date"
                      value={dateFrom}
                      onChange={(e) => setDateFrom(e.target.value)}
                      className="px-2 py-1 bg-bone border border-cream-deep focus:border-teal focus:outline-none font-body text-sm"
                    />
                  </div>
                  <div>
                    <label className="block font-body text-xs text-ink-fade italic mb-1">To</label>
                    <input
                      type="date"
                      value={dateTo}
                      onChange={(e) => setDateTo(e.target.value)}
                      className="px-2 py-1 bg-bone border border-cream-deep focus:border-teal focus:outline-none font-body text-sm"
                    />
                  </div>
                  {(dateFrom || dateTo) && (
                    <button
                      type="button"
                      onClick={() => { setDateFrom(""); setDateTo(""); }}
                      className="font-body text-xs text-ink-fade hover:text-terracotta transition-colors underline decoration-cream-deep hover:decoration-terracotta underline-offset-4"
                    >
                      Clear
                    </button>
                  )}
                  <div className="ml-auto">
                    <button
                      type="button"
                      onClick={() => window.print()}
                      className="font-display text-sm bg-teal-deep text-cream-light px-4 py-1.5 hover:bg-teal transition-colors"
                    >
                      Print
                    </button>
                  </div>
                </div>
                {(() => {
                  const filteredEntries = ledger.entries.filter((e) => {
                    if (!dateFrom && !dateTo) return true;
                    const ts = new Date(e.created_at).getTime();
                    if (dateFrom) {
                      const fromTs = new Date(dateFrom + "T00:00:00").getTime();
                      if (ts < fromTs) return false;
                    }
                    if (dateTo) {
                      const toTs = new Date(dateTo + "T23:59:59").getTime();
                      if (ts > toTs) return false;
                    }
                    return true;
                  });
                  return filteredEntries.length === 0 ? (
                    <p className="font-body text-sm text-ink-fade italic">
                      No transactions in this date range.
                    </p>
                  ) : (
                    <div id="ledger-print-area">
                      <div className="hidden print:block mb-4">
                        <h2 className="font-display text-xl text-teal-deep">Transaction history</h2>
                        <p className="font-body text-xs text-ink-fade italic">
                          {me?.userid ?? ""} {dateFrom || dateTo ? `· ${dateFrom || "earliest"} to ${dateTo || "latest"}` : ""}
                        </p>
                      </div>
                      <table className="w-full font-body text-sm">
                        <thead>
                          <tr className="text-left text-ink-fade text-xs uppercase tracking-wider border-b border-cream-deep">
                            <th className="pb-2 pr-4">Date</th>
                            <th className="pb-2 pr-4">Type</th>
                            <th className="pb-2 pr-4">Token</th>
                            <th className="pb-2 text-right">Amount</th>
                          </tr>
                        </thead>
                        <tbody>
                          {filteredEntries.map((e) => (
                            <tr key={e.id} className="border-b border-cream-deep/50 hover:bg-bone transition-colors">
                              <td className="py-2 pr-4 text-ink-fade text-xs">
                                {new Date(e.created_at).toLocaleDateString(undefined, { month: "short", day: "numeric", year: "numeric" })}
                              </td>
                              <td className="py-2 pr-4 text-ink italic">{e.transaction_type.replace(/_/g, " ")}</td>
                              <td className="py-2 pr-4">
                                <span className={e.token_class === "EMS" ? "text-teal-deep font-display text-xs" : "text-terracotta font-display text-xs"}>
                                  {e.token_class}
                                </span>
                              </td>
                              <td className="py-2 text-right font-mono text-xs text-ink">
                                +{parseFloat(e.amount).toLocaleString(undefined, { minimumFractionDigits: 4 })}
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                      {(dateFrom || dateTo) && (
                        <p className="font-body text-xs text-ink-fade italic mt-3">
                          Showing {filteredEntries.length} of {ledger.entries.length} transactions in selected range.
                        </p>
                      )}
                    </div>
                  );
                })()}
              </>
            ) : (
              <p className="font-body text-sm text-ink-fade italic mt-4">No transactions yet.</p>
            )}
            {ledger && ledger.total > ledger.limit && (
              <div className="flex items-center justify-between mt-4 print:hidden">
                <p className="font-body text-xs text-ink-fade italic">
                  Page {Math.floor(ledger.offset / ledger.limit) + 1} of {Math.ceil(ledger.total / ledger.limit)}
                  {" · "}
                  showing {ledger.offset + 1}–{Math.min(ledger.offset + ledger.entries.length, ledger.total)} of {ledger.total}
                </p>
                <div className="flex gap-2">
                  <button
                    type="button"
                    onClick={() => loadLedger(Math.max(0, ledger.offset - ledger.limit))}
                    disabled={ledgerLoading || ledger.offset === 0}
                    className="font-display text-sm bg-bone border border-cream-deep text-teal-deep px-3 py-1 hover:bg-cream-deep transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
                  >
                    « Prev
                  </button>
                  <button
                    type="button"
                    onClick={() => loadLedger(ledger.offset + ledger.limit)}
                    disabled={ledgerLoading || ledger.offset + ledger.entries.length >= ledger.total}
                    className="font-display text-sm bg-bone border border-cream-deep text-teal-deep px-3 py-1 hover:bg-cream-deep transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
                  >
                    Next »
                  </button>
                </div>
              </div>
            )}
          </div>
        )}
      </section>

      {/* Identity — collapsed accordion at bottom */}
      <section className="surface mt-4">
        <button
          onClick={() => setShowIdentity((v) => !v)}
          className="w-full px-6 py-4 flex items-center justify-between text-left hover:bg-bone transition-colors"
        >
          <span className="font-display text-base text-teal-deep">Your identity</span>
          <span className="font-body text-xs text-ink-fade italic">
            {showIdentity ? "▼ Hide" : "▶ Show"}
          </span>
        </button>
        {showIdentity && (
          <div className="px-6 pb-6 border-t border-cream-deep">
            <dl className="grid sm:grid-cols-2 gap-4 mt-4 font-body text-sm">
              <Field label="Userid" value={me?.userid ?? "—"} mono />
              <Field label="UEID" value={me?.uei || "—"} mono small />
              <Field label="County" value={me?.county ?? "—"} />
              <Field label="Roles" value={me?.roles?.join(", ") || "user"} />
              {balances?.balance_last_updated && (
                <Field
                  label="Balances updated"
                  value={new Date(balances.balance_last_updated).toLocaleString()}
                  small
                />
              )}
            </dl>
            <p className="font-body text-xs text-ink-fade italic mt-4 leading-relaxed">
              Your data is private. Only you can see this — no other Champion or admin
              can view your balances, UEID, or wallet. If anything looks wrong, email{" "}
              <a
                href="mailto:kiddstechnical@gmail.com"
                className="text-terracotta hover:text-terracotta-deep underline decoration-terracotta/30 hover:decoration-terracotta underline-offset-4 transition-colors"
              >
                kiddstechnical@gmail.com
              </a>.
            </p>
          </div>
        )}
      </section>
    </>
  );
}

function BalanceCard({
  label,
  shortLabel,
  amount,
  accent,
}: {
  label: string;
  shortLabel: string;
  amount: number;
  accent: "teal" | "terracotta";
}) {
  const color = accent === "teal" ? "text-teal-deep" : "text-terracotta-deep";
  const formatted = amount.toLocaleString(undefined, {
    minimumFractionDigits: 0,
    maximumFractionDigits: 4,
  });
  return (
    <div className="surface p-6 flex flex-col items-center justify-center text-center">
      <p className="font-body text-xs text-ink-fade italic uppercase tracking-wider">
        {shortLabel}
      </p>
      <p className={`font-display italic text-5xl ${color} my-2`}>{formatted}</p>
      <p className="font-body text-xs text-ink-fade italic">{label}</p>
    </div>
  );
}

function PlaceholderCard({
  title,
  subtitle,
  note,
}: {
  title: string;
  subtitle: string;
  note: string;
}) {
  return (
    <div className="surface p-6 flex flex-col items-center justify-center text-center opacity-60">
      <p className="font-display text-base text-teal-deep">{title}</p>
      <p className="font-body text-xs text-ink-fade italic mt-1">{subtitle}</p>
      <p className="font-body text-xs text-terracotta/70 italic mt-3">{note}</p>
    </div>
  );
}

function Field({
  label,
  value,
  mono = false,
  small = false,
}: {
  label: string;
  value: string;
  mono?: boolean;
  small?: boolean;
}) {
  return (
    <div>
      <dt className="text-ink-fade italic text-xs uppercase tracking-wider">{label}</dt>
      <dd className={`text-ink ${mono ? "font-mono" : ""} ${small ? "text-xs break-all" : ""}`}>
        {value}
      </dd>
    </div>
  );
}

// ────────────────────────────────────────────────────────────────────
// Admin queue — unchanged from previous version
// ────────────────────────────────────────────────────────────────────

function AdminQueue({
  applications,
  state,
  error,
  actingOn,
  denyingId,
  denyReason,
  setDenyingId,
  setDenyReason,
  onApprove,
  onDeny,
  onClearError,
}: {
  applications: ApplicationListItem[];
  state: "idle" | "loading" | "ready" | "error";
  error: string;
  actingOn: string | null;
  denyingId: string | null;
  denyReason: string;
  setDenyingId: (id: string | null) => void;
  setDenyReason: (r: string) => void;
  onApprove: (id: string) => void;
  onDeny: (id: string) => void;
  onClearError: () => void;
}) {
  return (
    <>
      <div className="flex justify-center mb-6">
        <HeartOrnament className="w-7 h-7 text-terracotta" />
      </div>
      <h1 className="font-display italic text-display text-teal-deep text-center mb-2">
        Pending applications
      </h1>
      <p className="font-body text-sm text-ink-fade text-center mb-10 italic">
        {state === "loading"
          ? "Loading…"
          : applications.length === 0
            ? "Nothing waiting right now."
            : applications.length === 1
              ? "1 application waiting"
              : `${applications.length} applications waiting`}
      </p>

      {error && (
        <div className="max-w-2xl mx-auto mb-6 font-body text-sm text-terracotta-deep bg-terracotta/10 border border-terracotta/30 p-3 italic flex items-baseline justify-between">
          <span>{error}</span>
          <button onClick={onClearError} className="text-xs text-terracotta-deep hover:underline ml-3">
            dismiss
          </button>
        </div>
      )}

      <div className="space-y-6 max-w-3xl mx-auto">
        {applications.map((a) => (
          <div key={a.application_id} className="surface p-6">
            <div className="flex items-baseline justify-between mb-4">
              <div>
                <h2 className="font-display text-xl text-teal-deep">{a.name}</h2>
                <p className="font-body text-sm text-ink-fade italic">
                  {a.county} County ·{" "}
                  {new Date(a.submitted_at).toLocaleDateString(undefined, {
                    month: "short",
                    day: "numeric",
                    year: "numeric",
                    hour: "numeric",
                    minute: "2-digit",
                  })}
                </p>
              </div>
              <p className="font-body text-xs text-ink-fade font-mono">
                {a.application_id.slice(0, 8)}…
              </p>
            </div>

            <p className="font-body text-sm text-ink mb-1">{a.email}</p>
            <p className="font-body text-xs text-ink-fade mb-4 font-mono">
              proposed_userid: {a.proposed_userid} · {a.agreement_version}
            </p>

            {a.county_warning && (
              <div className="bg-terracotta/10 border border-terracotta/30 px-4 py-2 mb-4 font-body text-xs text-terracotta-deep italic">
                {a.county_warning}
              </div>
            )}

            <div className="bg-bone border border-cream-deep p-4 mb-4">
              <p className="font-display text-sm text-teal-deep mb-1">Why they want to participate</p>
              <p className="font-body text-sm text-ink leading-relaxed whitespace-pre-wrap">
                {a.motivation}
              </p>
            </div>

            {denyingId === a.application_id ? (
              <div className="space-y-3">
                <textarea
                  value={denyReason}
                  onChange={(e) => setDenyReason(e.target.value)}
                  placeholder="Reason for denial (5+ characters)…"
                  className="w-full px-3 py-2 bg-bone border border-cream-deep focus:border-terracotta focus:outline-none font-body text-sm"
                  rows={3}
                  autoFocus
                />
                <div className="flex gap-2">
                  <button
                    onClick={() => onDeny(a.application_id)}
                    disabled={actingOn === a.application_id}
                    className="btn-terracotta text-sm flex-1"
                  >
                    Confirm deny
                  </button>
                  <button
                    onClick={() => {
                      setDenyingId(null);
                      setDenyReason("");
                      onClearError();
                    }}
                    className="btn-secondary text-sm flex-1"
                  >
                    Cancel
                  </button>
                </div>
              </div>
            ) : (
              <div className="flex gap-3">
                <button
                  onClick={() => onApprove(a.application_id)}
                  disabled={actingOn === a.application_id}
                  className="btn-primary"
                >
                  {actingOn === a.application_id ? "Approving…" : "Approve"}
                </button>
                <button
                  onClick={() => {
                    setDenyingId(a.application_id);
                    onClearError();
                  }}
                  disabled={actingOn !== null}
                  className="font-display text-sm text-ink-fade hover:text-terracotta transition-colors underline decoration-cream-deep hover:decoration-terracotta underline-offset-4 px-4"
                >
                  Deny
                </button>
              </div>
            )}
          </div>
        ))}
      </div>
    </>
  );
}
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend-tsx$ 

