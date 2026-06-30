(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend-tsx$ ls /opt/msjarvis-rebuild/ms-allis-frontend-tsx/app/api/apply/
# Should show: route.ts
ls: cannot access '/opt/msjarvis-rebuild/ms-allis-frontend-tsx/app/api/apply/': No such file or directory
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend-tsx$ # Check if the API route handler exists
ls -la /opt/msjarvis-rebuild/ms-allis-frontend-tsx/app/api/
ls -la /opt/msjarvis-rebuild/ms-allis-frontend-tsx/app/api/apply/ 2>/dev/null || echo "MISSING"

# Show the agreement lib
cat /opt/msjarvis-rebuild/ms-allis-frontend-tsx/lib/agreement.ts

# Show the portal/login page
cat /opt/msjarvis-rebuild/ms-allis-frontend-tsx/app/portal/page.tsx 2>/dev/null || \
cat /opt/msjarvis-rebuild/ms-allis-frontend-tsx/app/login/page.tsx 2>/dev/null

# What's running on port 8050 (the Python backend)?
curl -s http://127.0.0.1:8050/docs | head -20
ls: cannot access '/opt/msjarvis-rebuild/ms-allis-frontend-tsx/app/api/': No such file or directory
MISSING
// The Community Champion Agreement, embedded.
// IMPORTANT: this text IS the legal record. The hash below is verified at submit time
// by application_service.py to prove byte-for-byte what the user agreed to.
//
// To update the agreement:
//   1. Edit AGREEMENT_TEXT below
//   2. Bump AGREEMENT_VERSION to today's date
//   3. The hash auto-computes at runtime — backend regenerates and verifies on submit
//   4. Bump CURRENT_AGREEMENT_VERSION in services/application_service.py to match
//   5. Existing pending applications retain their old version stamp (don't migrate)

export const AGREEMENT_VERSION = "2026-04-25";

export const AGREEMENT_TITLE =
  "Community Champion / Red Team Participation Agreement";

// The full agreement body. Keep it in this file as a single source of truth.
// Headings are H3-level (rendered with <h3>), paragraphs are plain.
export const AGREEMENT_TEXT = `# ${AGREEMENT_TITLE}

## Who this is between

This is an agreement between you (the "Community Champion" or "Participant") and Harmony for Hope, Inc., a West Virginia 501(c)(3) nonprofit (EIN 81-1907024), located at 704 Main St., Mount Hope, WV ("Harmony for Hope" or "we"). It governs your participation in the MS.ALLIS Phase 0 invite-only beta — testing and providing feedback on Ms. Allis (the MountainShares Artificial Learning & Location Intelligence System), the MountainShares ecosystem, and related community infrastructure.

## What you're agreeing to do

As a Community Champion you'll receive access to Ms. Allis and may be asked to test features, identify issues, share community-resource information, or provide feedback on the experience. Participation is voluntary at all times. You may stop participating whenever you want, for any reason, by replying to any email from us or by emailing carrie@mountainshares.us.

## What this is not

This is not employment. You are not an employee, contractor, agent, or representative of Harmony for Hope. We are not paying you a wage and you are not earning hours toward any benefit other than what's explicitly described in the MountainShares program documents. Nothing here creates a partnership or joint venture.

## Your privacy

We will collect your name, email address, county of residence, and the information you choose to share when you apply, including your driver license image used for identity verification. We use this only to operate the program — verifying you are a real person, communicating with you, and ensuring the integrity of the system. We do not sell your data. We do not share it with third parties except as legally required.

Your driver license image is processed for identity verification and the verification result (a yes/no plus an immutability hash) is recorded in our system. The image itself is encrypted at rest. You may request that we delete it at any time.

Your conversations with Ms. Allis are stored in two tiers: a private tier accessible only to you and Ms. Allis, and an anonymized public tier that may inform community knowledge over time. The private tier can be muted (hidden from future retrieval) on request. Anonymization in the public tier means your name, address, and personally identifying details are stripped before any community-level use.

## Your MountainShares wallet

When your application is approved, the system generates a custodial cryptocurrency wallet on the Arbitrum One network on your behalf. Custodial means Ms. Allis holds the encryption key for the wallet's private key in our infrastructure. The wallet's public address is yours and visible to you; the encrypted private key is held safely on your behalf. As Phase 0 progresses you will have the option to take direct custody of the wallet (we hand you the private key, we delete our copy). Until you do that, we are responsible for the safekeeping of the wallet's encryption keys.

The wallet may, at our discretion, hold MountainShares tokens earned through participation according to program rules in effect at the time. MountainShares tokens are not legal tender, are not investments, and are not redeemable for currency outside the program's defined exchange mechanisms.

## What you're NOT signing up for

You are not agreeing to:
- Be available at any particular time or for any minimum duration
- Provide labor, services, or content for free outside of voluntary feedback
- Transfer ownership of any pre-existing intellectual property you create
- Be identified publicly without your separate written consent
- Hold us harmless for our own gross negligence or willful misconduct

## What we ask

We ask that you:
- Provide accurate information when you apply
- Treat the system, the team, and other Champions with basic respect
- Report bugs, problems, or concerning behavior so we can fix them
- Not use the system to attempt to harm others, exfiltrate other Champions' private data, or attack the underlying infrastructure
- Keep your magic-link login URL reasonably secure (treat it like a password)

## Intellectual property

You retain ownership of any feedback, ideas, or content you contribute. By submitting feedback to us, you grant Harmony for Hope a non-exclusive, royalty-free, worldwide license to use that feedback to improve Ms. Allis, the MountainShares ecosystem, and our community programs. We don't claim ownership of your ideas — just permission to use what you tell us to make the system better.

## Liability

The system is provided as-is. It's a community-built AI; it sometimes makes mistakes, retrieves wrong information, or behaves in unexpected ways. Don't rely on it for medical, legal, financial, or emergency advice — those are not its purpose. To the maximum extent permitted by West Virginia law, Harmony for Hope is not liable for indirect or consequential damages arising from your use of the system. Our maximum liability to you for direct damages is limited to one hundred U.S. dollars ($100), which both parties agree is a reasonable allocation of risk for a no-cost participation in a community program.

## Ending the agreement

You can end this agreement at any time by emailing us — your account will be deactivated and your tokens, if any, will follow the program rules in effect at the time. We can end the agreement at any time too, including if you violate these terms or if we discontinue the program. If we end it, we'll tell you in writing and explain why.

## Governing law

This agreement is governed by the laws of the State of West Virginia. Any dispute that can't be resolved by talking it out goes to the state or federal courts located in Fayette County, West Virginia.

## Acknowledgment

By checking the acceptance box on the application form, you confirm:
- You are at least 18 years old
- You have read this agreement and understand it
- You are entering into it voluntarily
- The information you've provided in your application is accurate
- A cryptographic hash of this exact agreement text, version ${AGREEMENT_VERSION}, will be stored alongside your application as proof of what you agreed to

If anything in this agreement is unclear, please email carrie@mountainshares.us before submitting your application. We'd rather answer questions than have anyone agree to something they didn't understand.

— Harmony for Hope, Inc.
   Mount Hope, West Virginia
   Agreement version ${AGREEMENT_VERSION}
`;

/**
 * Compute the SHA-256 hash of the agreement text in-browser.
 * The same hash is computed server-side at submission time and stored with the
 * application record, providing byte-for-byte proof of what the applicant agreed to.
 */
export async function hashAgreement(text: string): Promise<string> {
  const encoder = new TextEncoder();
  const data = encoder.encode(text);
  const hashBuffer = await crypto.subtle.digest("SHA-256", data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map((b) => b.toString(16).padStart(2, "0")).join("");
}
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

