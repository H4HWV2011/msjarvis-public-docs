crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ cat /opt/msjarvis-rebuild/ms-allis-frontend/app/portal/founder-equity/page.tsx
echo "---"
cat /opt/msjarvis-rebuild/ms-allis-frontend/components/FounderToken.tsx
echo "---"
cat /opt/msjarvis-rebuild/ms-allis-frontend/lib/api.ts
import TransactionHistory from "@/app/components/TransactionHistory";

export const metadata = {
    title: "Founder Equity Ledger | Ms. Allis",
    description: "Founder time-and-equity contributions to Harmony for Hope Inc.",
};

export default function FounderEquityPage() {
    return <TransactionHistory />;
}
---
"use client";
interface FounderTokenProps { serialNumber: string; mintedAt: string; cohort: string; size?: number; }
export function FounderToken({ serialNumber, mintedAt, cohort, size = 112 }: FounderTokenProps) {
  const year = new Date(mintedAt).getFullYear();
  const shortSerial = String(serialNumber ?? "").padStart(6, "0").slice(-6) || "??????";
  const r = size / 2;
  const innerR = r * 0.82;
  const textR = r * 0.68;
  function toXY(radius: number, angleDeg: number) { const rad = ((angleDeg - 90) * Math.PI) / 180; return { x: radius * Math.cos(rad), y: radius * Math.sin(rad) }; }
  function arcPath(radius: number, startAngle: number, endAngle: number) { const s = toXY(radius, startAngle); const e = toXY(radius, endAngle); const large = endAngle - startAngle > 180 ? 1 : 0; return `M ${r + s.x} ${r + s.y} A ${radius} ${radius} 0 ${large} 1 ${r + e.x} ${r + e.y}`; }
  return (
    <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`} aria-label={`Founder Token — ${cohort}, serial ${serialNumber}`} role="img">
      <defs>
        <radialGradient id="tokenGrad" cx="40%" cy="35%"><stop offset="0%" stopColor="#c9943a"/><stop offset="60%" stopColor="#b04830"/><stop offset="100%" stopColor="#7a2e18"/></radialGradient>
        <path id="topArc" d={arcPath(textR,-140,-40)}/>
        <path id="bottomArc" d={arcPath(textR,40,140)}/>
      </defs>
      <circle cx={r} cy={r} r={r-1} fill="url(#tokenGrad)"/>
      <circle cx={r} cy={r} r={innerR} fill="none" stroke="#f5e6c8" strokeWidth="1.5" strokeDasharray="3 2" opacity="0.6"/>
      <text x={r} y={r - size*0.04} textAnchor="middle" dominantBaseline="middle" fontFamily="Georgia,serif" fontStyle="italic" fontSize={size*0.22} fill="#f5e6c8" fontWeight="bold">WV</text>
      <text x={r} y={r + size*0.14} textAnchor="middle" dominantBaseline="middle" fontFamily="monospace" fontSize={size*0.09} fill="#f5e6c8" opacity="0.85">#{shortSerial}</text>
      <text fontFamily="Georgia,serif" fontStyle="italic" fontSize={size*0.085} fill="#f5e6c8" opacity="0.9"><textPath href="#topArc" startOffset="50%" textAnchor="middle">{cohort}</textPath></text>
      <text fontFamily="Georgia,serif" fontSize={size*0.08} fill="#f5e6c8" opacity="0.8"><textPath href="#bottomArc" startOffset="50%" textAnchor="middle">{year}</textPath></text>
      <text x={r} y={r + r*0.72} textAnchor="middle" dominantBaseline="middle" fontSize={size*0.1} fill="#f5e6c8" opacity="0.7">♥</text>
    </svg>
  );
}
---
// API client for auth_router (the canonical auth system).
// All endpoints under /auth/*, OAuth2 Bearer tokens, JSON bodies.

const SESSION_KEY = "msallis_session_token";
const SESSION_NAME_KEY = "msallis_session_name";

export const session = {
  get: () => (typeof window === "undefined" ? null : sessionStorage.getItem(SESSION_KEY)),
  getName: () => (typeof window === "undefined" ? null : sessionStorage.getItem(SESSION_NAME_KEY)),
  set: (token: string, name: string) => {
    sessionStorage.setItem(SESSION_KEY, token);
    sessionStorage.setItem(SESSION_NAME_KEY, name);
  },
  clear: () => {
    sessionStorage.removeItem(SESSION_KEY);
    sessionStorage.removeItem(SESSION_NAME_KEY);
  },
};

export interface ApplicationListItem {
  application_id: string;
  proposed_userid: string;
  ueid?: string;
  name: string;
  email: string;
  county: string;
  motivation: string;
  agreement_version: string;
  submitted_at: string;
  status: string;
  ip_address?: string;
  county_warning?: string;
  notes?: string;
}

export interface RegisterResponse {
  application_id: string;
  proposed_userid: string;
  agreement_version: string;
  message: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
  expires_in: number;
}

export interface FirstLoginResponse {
  access_token: string;
  token_type: string;
  public_uuid: string;
  wallet_address: string;
}

export interface MeResponse {
  userid: string;
  uei: string | null;
  roles: string[];
  county: string | null;
}

export interface PendingResponse {
  applications: ApplicationListItem[];
  pending: PendingApplication[];   // alias used by admin/page.tsx
  count: number;
}

export interface ApproveResponse {
  application_id: string;
  public_uuid: string;
  email: string;
  message: string;
}

export class ApiError extends Error {
  status: number;
  detail: string;
  constructor(status: number, detail: string) {
    super(detail);
    this.status = status;
    this.detail = detail;
    this.name = "ApiError";
  }
}

async function fileToBase64(file: File): Promise<string> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => {
      const result = reader.result as string;
      // Strip the "data:image/jpeg;base64," prefix
      const comma = result.indexOf(",");
      resolve(comma >= 0 ? result.slice(comma + 1) : result);
    };
    reader.onerror = () => reject(reader.error || new Error("file read failed"));
    reader.readAsDataURL(file);
  });
}

async function request<T>(
  path: string,
  options: RequestInit = {},
  expectedStatuses: number[] = [200]
): Promise<T> {
  const response = await fetch(path, options);
  if (!expectedStatuses.includes(response.status)) {
    let detail = response.statusText;
    try {
      const body = await response.json();
      detail = body.detail || body.message || detail;
    } catch {
      // body wasn't JSON
    }
    throw new ApiError(response.status, detail);
  }
  const text = await response.text();
  if (!text) return {} as T;
  return JSON.parse(text);
}

export const api = {
  /**
   * POST /auth/register
   * Creates user account (pending_first_login), runs registration_pipeline (DL OCR,
   * UEID, immutable record), generates wallet. Application sits in pending queue
   * until an admin approves.
   */
  apply: async (data: {
    name: string;
    email: string;
    county: string;
    motivation: string;
    agreement_version: string;
    agreement_hash: string;  // kept for parity with frontend; auth_router accepts agreement_accepted boolean
    selfie_image: File;
    dl_image: File;
  }): Promise<RegisterResponse> => {
    const dl_image_b64 = await fileToBase64(data.dl_image);
    const selfie_b64 = await fileToBase64(data.selfie_image);
    return request<RegisterResponse>(
      "/auth/register",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: data.name,
          email: data.email,
          county: data.county,
          motivation: data.motivation,
          agreement_accepted: true,
          agreement_version: data.agreement_version,
          dl_image_b64,
          selfie_b64,
        }),
      },
      [201]
    );
  },

  /** Static county list — auth_router doesn't expose this so we hardcode. */
  countyList: async (): Promise<{ counties: string[] }> => ({
    counties: [
      "Barbour", "Berkeley", "Boone", "Braxton", "Brooke", "Cabell",
      "Calhoun", "Clay", "Doddridge", "Fayette", "Gilmer", "Grant",
      "Greenbrier", "Hampshire", "Hancock", "Hardy", "Harrison",
      "Jackson", "Jefferson", "Kanawha", "Lewis", "Lincoln", "Logan",
      "Marion", "Marshall", "Mason", "McDowell", "Mercer", "Mineral",
      "Mingo", "Monongalia", "Monroe", "Morgan", "Nicholas", "Ohio",
      "Pendleton", "Pleasants", "Pocahontas", "Preston", "Putnam",
      "Raleigh", "Randolph", "Ritchie", "Roane", "Summers", "Taylor",
      "Tucker", "Tyler", "Upshur", "Wayne", "Webster", "Wetzel",
      "Wirt", "Wood", "Wyoming",
    ],
  }),

  /**
   * POST /auth/login (OAuth2 password form, application/x-www-form-urlencoded)
   * Used by both admin (carrie_admin) and Champions after first-login.
   */
  signIn: async (username: string, password: string): Promise<LoginResponse> => {
    const form = new URLSearchParams();
    form.set("username", username);
    form.set("password", password);
    return request<LoginResponse>(
      "/auth/login",
      {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: form.toString(),
      },
      [200]
    );
  },

  /**
   * POST /auth/first-login — exchange temp password for permanent password.
   * Used after admin approval; user has temp password from the approval email.
   */
  firstLogin: async (data: {
    email: string;
    temp_password: string;
    new_password: string;
  }): Promise<FirstLoginResponse> => {
    return request<FirstLoginResponse>(
      "/auth/first-login",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      },
      [200]
    );
  },

  /** GET /auth/me — current user info from token */
  me: async (): Promise<MeResponse> => {
    const token = session.get();
    if (!token) throw new ApiError(401, "no session");
    return request<MeResponse>("/auth/me", {
      headers: { Authorization: `Bearer ${token}` },
    });
  },

  /** GET /auth/applications/pending — admin only */
  pending: async (): Promise<PendingResponse> => {
    const token = session.get();
    if (!token) throw new ApiError(401, "no session");
    return request<PendingResponse>("/auth/applications/pending", {
      headers: { Authorization: `Bearer ${token}` },
    });
  },

  /** POST /auth/approve/{application_id} — admin only */
  approve: async (applicationId: string): Promise<ApproveResponse> => {
    const token = session.get();
    if (!token) throw new ApiError(401, "no session");
    return request<ApproveResponse>(
      `/auth/approve/${encodeURIComponent(applicationId)}`,
      {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
      }
    );
  },

  /** POST /auth/deny/{application_id} — admin only, requires reason */
  deny: async (applicationId: string, reason: string): Promise<{ application_id: string; status: string; reason: string }> => {
    const token = session.get();
    if (!token) throw new ApiError(401, "no session");
    return request(
      `/auth/deny/${encodeURIComponent(applicationId)}`,
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ reason }),
      }
    );
  },
};

// ── Convenience named exports for auth pages ──────────────────────

/** signIn(email, password) → stores session, returns LoginResponse */
export async function signIn(email: string, password: string): Promise<LoginResponse> {
  const result = await api.signIn(email, password);
  session.set(result.access_token, email);
  return result;
}

/** forgotPassword — POST /auth/forgot-password */
export async function forgotPassword(email: string): Promise<{ message: string }> {
  return request<{ message: string }>(
    "/auth/forgot-password",
    { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ email }) },
    [200, 202]
  );
}

/** setupPassword — POST /auth/setup-password (first-login flow) */
export async function setupPassword(data: {
  email: string; temp_password: string; new_password: string;
}): Promise<FirstLoginResponse> {
  return api.firstLogin(data);
}

/** setupPasswordWithToken — token-based first-login flow */
export async function setupPasswordWithToken(data: {
  token: string; new_password: string; username?: string;
}): Promise<FirstLoginResponse> {
  return request<FirstLoginResponse>("/auth/setup-password", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  }, [200]);
}

/** hasPassword / resolveToken — used by setup-password page */
export async function hasPassword(email: string): Promise<{ has_password: boolean }> {
  return request<{ has_password: boolean }>(
    `/auth/has-password?email=${encodeURIComponent(email)}`, {}, [200]
  );
}

export async function resolveToken(token: string): Promise<{ email: string; valid: boolean; ueid?: string }> {
  return request<{ email: string; valid: boolean; ueid?: string }>(
    `/auth/resolve-token?token=${encodeURIComponent(token)}`, {}, [200]
  );
}

/** adminKey — used by admin page for privileged operations */
const ADMIN_KEY = "msallis_admin_key";
export const adminKey = {
  get: () => (typeof window === "undefined" ? null : sessionStorage.getItem(ADMIN_KEY)),
  set: (k: string) => sessionStorage.setItem(ADMIN_KEY, k),
  clear: () => sessionStorage.removeItem(ADMIN_KEY),
};

// ── Admin types ───────────────────────────────────────────────────

export type PendingApplication = ApplicationListItem;
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ cat /opt/msjarvis-rebuild/ms-allis-frontend/app/components/TransactionHistory.tsx
echo "---"
cat /opt/msjarvis-rebuild/ms-allis-frontend/app/portal/page.tsx
echo "---"
cat /opt/msjarvis-rebuild/ms-allis-frontend/lib/portal.ts
"use client";

/**
 * TransactionHistory.tsx
 * --------------------------------------------------------------------------
 * Founder Equity Ledger (EMS / Earned MountainShares)
 * Kidd's Technical Services, LLC  →  Harmony for Hope, Inc.
 *
 * Drop-in client component for the Ms. Allis dashboard.
 * Source-of-truth JSON: /public/data/kts-timesheet.json (fetched at runtime)
 * No backend required — editable without rebuild.
 *
 * Aesthetic: refined editorial / audit-ready archival.
 * Brand tokens: Old Gold #CFB53B + Royal Navy #1e3a8a.
 * Typography: Crimson Pro (display) · IBM Plex Sans (body) · IBM Plex Mono (numerals).
 *   If those families are not loaded by the host app, fonts fall back to
 *   reasonable system equivalents — no breakage.
 * --------------------------------------------------------------------------
 */

import { useEffect, useMemo, useState } from "react";

type Transaction = {
  id: string;
  date: string;          // YYYY-MM-DD
  day_of_week: string;
  hours: number;
  ems: number;
  usd: number;
  description: string;
  milestone: boolean;
  critical: boolean;
  day_off: boolean;
};

type LedgerDoc = {
  metadata: {
    prepared_for: string;
    entity: string;
    period_start: string;
    period_end: string;
    rate_per_hour_usd: number;
    ems_per_hour: number;
    ftis_total_hours: number;
    ftis_total_usd: number;
    ftis_total_ems: number;
    per_day_total_hours: number;
    per_day_total_usd: number;
    per_day_total_ems: number;
  };
  transactions: Transaction[];
};

const PAGE_SIZE = 25;

const fmtInt = new Intl.NumberFormat("en-US");
const fmtUsd = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
  maximumFractionDigits: 0,
});
const fmtHrs = (h: number) =>
  Number.isInteger(h) ? fmtInt.format(h) : h.toFixed(1);

function formatDateLong(iso: string): string {
  const [y, m, d] = iso.split("-").map(Number);
  const dt = new Date(Date.UTC(y, m - 1, d));
  return dt.toLocaleDateString("en-US", {
    timeZone: "UTC",
    month: "short",
    day: "2-digit",
    year: "numeric",
  });
}

export default function TransactionHistory() {
  const [doc, setDoc] = useState<LedgerDoc | null>(null);
  const [err, setErr] = useState<string | null>(null);
  const [startDate, setStartDate] = useState<string>("");
  const [endDate, setEndDate] = useState<string>("");
  const [page, setPage] = useState<number>(1);

  // Fetch
  useEffect(() => {
    let cancelled = false;
    fetch("/data/kts-timesheet.json", { cache: "no-store" })
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then((j: LedgerDoc) => {
        if (!cancelled) setDoc(j);
      })
      .catch((e) => !cancelled && setErr(String(e)));
    return () => {
      cancelled = true;
    };
  }, []);

  // Filter
  const filtered = useMemo<Transaction[]>(() => {
    if (!doc) return [];
    const rows = doc.transactions.filter((t) => {
      if (startDate && t.date < startDate) return false;
      if (endDate && t.date > endDate) return false;
      return true;
    });
    return rows.sort((a, b) => a.date.localeCompare(b.date));
  }, [doc, startDate, endDate]);

  // Filtered totals (for display)
  const filteredTotals = useMemo(() => {
    const hours = filtered.reduce((s, t) => s + t.hours, 0);
    const usd = filtered.reduce((s, t) => s + t.usd, 0);
    return { hours, usd, ems: usd, count: filtered.length };
  }, [filtered]);

  // Pagination
  const pageCount = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
  useEffect(() => {
    if (page > pageCount) setPage(1);
  }, [page, pageCount]);
  const pageRows = filtered.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE);

  const resetFilters = () => {
    setStartDate("");
    setEndDate("");
    setPage(1);
  };

  if (err) {
    return (
      <div className="th-root">
        <div className="th-error">
          Unable to load the ledger ({err}). Verify{" "}
          <code>/public/data/kts-timesheet.json</code> is in place.
        </div>
        <Styles />
      </div>
    );
  }

  if (!doc) {
    return (
      <div className="th-root">
        <div className="th-loading">Loading founder equity ledger…</div>
        <Styles />
      </div>
    );
  }

  const md = doc.metadata;

  return (
    <div className="th-root">
      {/* HEADER */}
      <header className="th-header">
        <div className="th-eyebrow">Founder Equity · Earned MountainShares</div>
        <h1 className="th-title">Transaction History</h1>
        <div className="th-subtitle">
          <span>{md.entity}</span>
          <span className="th-dot" aria-hidden>·</span>
          <span>Prepared for {md.prepared_for}</span>
          <span className="th-dot" aria-hidden>·</span>
          <span>
            {formatDateLong(md.period_start)} – {formatDateLong(md.period_end)}
          </span>
        </div>

        {/* SUMMARY BAND */}
        <div className="th-summary">
          <Stat
            label="FTIS-001 Total"
            primary={`${fmtInt.format(md.ftis_total_ems)} EMS`}
            secondary={`${fmtInt.format(md.ftis_total_hours)} hrs · ${fmtUsd.format(md.ftis_total_usd)}`}
            tone="navy"
          />
          <Stat
            label="Logged to Date"
            primary={`${fmtInt.format(md.per_day_total_ems)} EMS`}
            secondary={`${fmtHrs(md.per_day_total_hours)} hrs · ${fmtUsd.format(md.per_day_total_usd)}`}
            tone="gold"
          />
          <Stat
            label={`Rate · ${fmtInt.format(md.ems_per_hour)} EMS/hr`}
            primary={`${fmtUsd.format(md.rate_per_hour_usd)}/hr`}
            secondary="1 EMS = $1 USD"
            tone="plain"
          />
        </div>
      </header>

      {/* CONTROLS */}
      <div className="th-controls th-no-print">
        <div className="th-search">
          <label className="th-field">
            <span>From</span>
            <input
              type="date"
              value={startDate}
              min={md.period_start}
              max={md.period_end}
              onChange={(e) => {
                setStartDate(e.target.value);
                setPage(1);
              }}
            />
          </label>
          <label className="th-field">
            <span>To</span>
            <input
              type="date"
              value={endDate}
              min={md.period_start}
              max={md.period_end}
              onChange={(e) => {
                setEndDate(e.target.value);
                setPage(1);
              }}
            />
          </label>
          <button
            type="button"
            className="th-btn-ghost"
            onClick={resetFilters}
            disabled={!startDate && !endDate}
          >
            Reset
          </button>
        </div>

        <div className="th-actions">
          <div className="th-result-count">
            {fmtInt.format(filteredTotals.count)} entries
            {(startDate || endDate) && (
              <>
                {" "}· {fmtHrs(filteredTotals.hours)} hrs ·{" "}
                {fmtUsd.format(filteredTotals.usd)}
              </>
            )}
          </div>
          <button
            type="button"
            className="th-btn-print"
            onClick={() => window.print()}
            aria-label="Print ledger"
          >
            <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden>
              <path
                d="M6 9V3h12v6M6 18H4a1 1 0 0 1-1-1v-5a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3v5a1 1 0 0 1-1 1h-2M6 14h12v7H6z"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.6"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
            Print
          </button>
        </div>
      </div>

      {/* TABLE */}
      <div className="th-table-wrap">
        <table className="th-table">
          <thead>
            <tr>
              <th scope="col" className="th-c-date">Date</th>
              <th scope="col" className="th-c-day">Day</th>
              <th scope="col" className="th-c-desc">Description</th>
              <th scope="col" className="th-c-num">Hours</th>
              <th scope="col" className="th-c-num">EMS</th>
              <th scope="col" className="th-c-num">USD</th>
            </tr>
          </thead>
          <tbody>
            {pageRows.length === 0 && (
              <tr>
                <td colSpan={6} className="th-empty">
                  No entries match the selected dates.
                </td>
              </tr>
            )}
            {pageRows.map((t) => (
              <tr
                key={t.id}
                className={[
                  "th-row",
                  t.milestone && "th-row--milestone",
                  t.critical && "th-row--critical",
                  t.day_off && "th-row--off",
                ]
                  .filter(Boolean)
                  .join(" ")}
              >
                <td className="th-c-date th-mono">{t.date}</td>
                <td className="th-c-day">{t.day_of_week}</td>
                <td className="th-c-desc">
                  {t.milestone && <span className="th-tag th-tag--gold">Milestone</span>}
                  {t.critical && <span className="th-tag th-tag--red">Incident</span>}
                  {t.day_off ? (
                    <span className="th-muted">Day Off</span>
                  ) : (
                    t.description
                  )}
                </td>
                <td className="th-c-num th-mono">
                  {t.day_off ? "—" : fmtHrs(t.hours)}
                </td>
                <td className="th-c-num th-mono">
                  {t.day_off ? "—" : fmtInt.format(t.ems)}
                </td>
                <td className="th-c-num th-mono">
                  {t.day_off ? "—" : fmtUsd.format(t.usd)}
                </td>
              </tr>
            ))}
          </tbody>
          <tfoot>
            <tr>
              <td colSpan={3} className="th-foot-label">
                {startDate || endDate ? "Range subtotal" : "Logged total"}
              </td>
              <td className="th-c-num th-mono th-foot-num">
                {fmtHrs(filteredTotals.hours)}
              </td>
              <td className="th-c-num th-mono th-foot-num">
                {fmtInt.format(filteredTotals.ems)}
              </td>
              <td className="th-c-num th-mono th-foot-num">
                {fmtUsd.format(filteredTotals.usd)}
              </td>
            </tr>
          </tfoot>
        </table>
      </div>

      {/* PAGINATION */}
      <nav className="th-pagination th-no-print" aria-label="Ledger pages">
        <button
          type="button"
          className="th-page-arrow"
          onClick={() => setPage((p) => Math.max(1, p - 1))}
          disabled={page === 1}
          aria-label="Previous page"
        >
          ‹
        </button>
        <PageNumbers page={page} pageCount={pageCount} onJump={setPage} />
        <button
          type="button"
          className="th-page-arrow"
          onClick={() => setPage((p) => Math.min(pageCount, p + 1))}
          disabled={page === pageCount}
          aria-label="Next page"
        >
          ›
        </button>
        <span className="th-page-meta">
          Page {page} of {pageCount}
        </span>
      </nav>

      <Styles />
    </div>
  );
}

/* ----------------------------- subcomponents ---------------------------- */

function Stat({
  label,
  primary,
  secondary,
  tone,
}: {
  label: string;
  primary: string;
  secondary: string;
  tone: "navy" | "gold" | "plain";
}) {
  return (
    <div className={`th-stat th-stat--${tone}`}>
      <div className="th-stat-label">{label}</div>
      <div className="th-stat-primary th-mono">{primary}</div>
      <div className="th-stat-secondary">{secondary}</div>
    </div>
  );
}

function PageNumbers({
  page,
  pageCount,
  onJump,
}: {
  page: number;
  pageCount: number;
  onJump: (p: number) => void;
}) {
  // Show first, last, current ±1, with ellipses
  const pages: (number | "…")[] = [];
  const add = (p: number | "…") => pages.push(p);
  const window = new Set<number>([1, pageCount, page - 1, page, page + 1]);
  let prev = 0;
  for (let p = 1; p <= pageCount; p++) {
    if (window.has(p)) {
      if (prev && p - prev > 1) add("…");
      add(p);
      prev = p;
    }
  }
  return (
    <ul className="th-page-list">
      {pages.map((p, idx) =>
        p === "…" ? (
          <li key={`e-${idx}`} className="th-page-ellipsis">…</li>
        ) : (
          <li key={p}>
            <button
              type="button"
              className={`th-page-num ${p === page ? "is-current" : ""}`}
              onClick={() => onJump(p)}
              aria-current={p === page ? "page" : undefined}
            >
              {p}
            </button>
          </li>
        ),
      )}
    </ul>
  );
}

/* ----------------------------------- CSS ---------------------------------- */

function Styles() {
  return (
    <style jsx>{`
      .th-root {
        --gold: #cfb53b;
        --gold-soft: #f4ecc6;
        --gold-deep: #a8911f;
        --navy: #1e3a8a;
        --navy-deep: #142563;
        --ink: #1c1c1c;
        --ink-soft: #4b4b4b;
        --muted: #8a8a8a;
        --line: #e6e1d4;
        --line-strong: #d6cfb9;
        --paper: #fbf8ef;
        --paper-card: #ffffff;
        --red: #9c1f1f;

        --f-display: "Crimson Pro", "Cormorant Garamond", "Iowan Old Style",
          "Palatino Linotype", Georgia, serif;
        --f-body: "IBM Plex Sans", "Helvetica Neue", -apple-system,
          BlinkMacSystemFont, "Segoe UI", sans-serif;
        --f-mono: "IBM Plex Mono", "JetBrains Mono", "SFMono-Regular", Menlo,
          Consolas, monospace;

        background: var(--paper);
        color: var(--ink);
        font-family: var(--f-body);
        font-size: 14px;
        line-height: 1.5;
        padding: 32px clamp(16px, 4vw, 48px);
        border: 1px solid var(--line);
        border-radius: 2px;
        max-width: 1240px;
        margin: 0 auto;
        position: relative;
      }
      .th-root::before {
        content: "";
        position: absolute;
        inset: 6px;
        border: 1px solid var(--line);
        border-radius: 2px;
        pointer-events: none;
      }

      .th-loading,
      .th-error {
        padding: 64px 0;
        text-align: center;
        color: var(--ink-soft);
        font-family: var(--f-body);
      }
      .th-error code {
        font-family: var(--f-mono);
        background: var(--gold-soft);
        padding: 1px 6px;
        border-radius: 2px;
      }

      .th-mono {
        font-family: var(--f-mono);
        font-variant-numeric: tabular-nums;
        font-feature-settings: "tnum" 1;
      }

      /* HEADER */
      .th-header {
        border-bottom: 2px solid var(--navy);
        padding-bottom: 24px;
        margin-bottom: 24px;
        position: relative;
      }
      .th-eyebrow {
        font-family: var(--f-body);
        font-size: 10px;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: var(--gold-deep);
        font-weight: 600;
        margin-bottom: 6px;
      }
      .th-title {
        font-family: var(--f-display);
        font-weight: 500;
        font-size: clamp(28px, 4vw, 40px);
        line-height: 1.1;
        margin: 0 0 10px 0;
        color: var(--navy-deep);
        letter-spacing: -0.01em;
      }
      .th-subtitle {
        color: var(--ink-soft);
        font-size: 13px;
        display: flex;
        flex-wrap: wrap;
        gap: 6px 10px;
        align-items: baseline;
      }
      .th-dot { color: var(--gold-deep); }

      /* SUMMARY */
      .th-summary {
        margin-top: 22px;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 0;
        border: 1px solid var(--line-strong);
        background: var(--paper-card);
      }
      .th-stat {
        padding: 16px 20px;
        border-right: 1px solid var(--line);
        position: relative;
      }
      .th-stat:last-child { border-right: 0; }
      .th-stat--navy { background: linear-gradient(180deg, #fff, #f4f5fb); }
      .th-stat--gold {
        background: linear-gradient(180deg, #fffdf3, #faf2cc);
        border-top: 3px solid var(--gold);
        padding-top: 13px;
      }
      .th-stat-label {
        font-size: 10px;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--ink-soft);
        font-weight: 600;
      }
      .th-stat-primary {
        font-size: 22px;
        font-weight: 500;
        margin-top: 6px;
        color: var(--navy-deep);
      }
      .th-stat--gold .th-stat-primary { color: var(--gold-deep); }
      .th-stat-secondary {
        font-size: 12px;
        color: var(--ink-soft);
        margin-top: 2px;
        font-family: var(--f-mono);
        font-variant-numeric: tabular-nums;
      }

      /* CONTROLS */
      .th-controls {
        display: flex;
        flex-wrap: wrap;
        gap: 16px;
        justify-content: space-between;
        align-items: flex-end;
        margin-bottom: 14px;
      }
      .th-search { display: flex; flex-wrap: wrap; gap: 12px; align-items: flex-end; }
      .th-field { display: flex; flex-direction: column; gap: 4px; font-size: 12px; }
      .th-field span {
        font-size: 10px;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: var(--ink-soft);
        font-weight: 600;
      }
      .th-field input[type="date"] {
        font-family: var(--f-mono);
        font-size: 13px;
        padding: 7px 10px;
        border: 1px solid var(--line-strong);
        background: var(--paper-card);
        border-radius: 2px;
        color: var(--ink);
        min-width: 150px;
      }
      .th-field input[type="date"]:focus {
        outline: 2px solid var(--gold);
        outline-offset: -1px;
      }
      .th-btn-ghost {
        font-family: var(--f-body);
        font-size: 12px;
        letter-spacing: 0.04em;
        padding: 7px 14px;
        background: transparent;
        border: 1px solid var(--line-strong);
        color: var(--ink-soft);
        cursor: pointer;
        border-radius: 2px;
      }
      .th-btn-ghost:hover:not(:disabled) {
        background: var(--gold-soft);
        border-color: var(--gold);
        color: var(--ink);
      }
      .th-btn-ghost:disabled { opacity: 0.5; cursor: not-allowed; }

      .th-actions { display: flex; align-items: center; gap: 16px; }
      .th-result-count {
        font-family: var(--f-mono);
        font-size: 12px;
        color: var(--ink-soft);
      }
      .th-btn-print {
        font-family: var(--f-body);
        font-size: 12px;
        letter-spacing: 0.04em;
        padding: 8px 14px;
        background: var(--navy);
        border: 1px solid var(--navy-deep);
        color: #fff;
        cursor: pointer;
        border-radius: 2px;
        display: inline-flex;
        align-items: center;
        gap: 6px;
      }
      .th-btn-print:hover { background: var(--navy-deep); }

      /* TABLE */
      .th-table-wrap { overflow-x: auto; border: 1px solid var(--line-strong); }
      .th-table {
        width: 100%;
        border-collapse: collapse;
        background: var(--paper-card);
        font-size: 13px;
      }
      .th-table thead th {
        background: var(--navy);
        color: var(--gold-soft);
        font-family: var(--f-body);
        font-weight: 600;
        font-size: 10px;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        text-align: left;
        padding: 11px 14px;
        border-bottom: 2px solid var(--gold);
      }
      .th-c-num { text-align: right; white-space: nowrap; }
      .th-c-date { white-space: nowrap; width: 110px; }
      .th-c-day { width: 90px; color: var(--ink-soft); }
      .th-row td {
        padding: 12px 14px;
        border-bottom: 1px solid var(--line);
        vertical-align: top;
      }
      .th-row:hover td { background: #fffceb; }
      .th-row--milestone {
        border-left: 3px solid var(--gold);
      }
      .th-row--milestone td:first-child { padding-left: 11px; }
      .th-row--milestone:hover td { background: #fff6c9; }
      .th-row--critical {
        border-left: 3px solid var(--red);
      }
      .th-row--critical td:first-child { padding-left: 11px; }
      .th-row--off td { color: var(--muted); }
      .th-empty {
        padding: 28px !important;
        text-align: center;
        color: var(--ink-soft);
        font-style: italic;
      }
      .th-tag {
        display: inline-block;
        font-size: 9px;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        font-weight: 700;
        padding: 2px 7px;
        border-radius: 2px;
        margin-right: 8px;
        vertical-align: 1px;
        font-family: var(--f-body);
      }
      .th-tag--gold { background: var(--gold); color: var(--navy-deep); }
      .th-tag--red { background: var(--red); color: #fff; }
      .th-muted { color: var(--muted); font-style: italic; }

      .th-table tfoot td {
        padding: 13px 14px;
        background: #fdfaf0;
        border-top: 2px solid var(--navy);
        font-weight: 600;
      }
      .th-foot-label {
        font-size: 10px;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--ink-soft);
      }
      .th-foot-num { color: var(--navy-deep); font-size: 14px; }

      /* PAGINATION */
      .th-pagination {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-top: 18px;
        flex-wrap: wrap;
      }
      .th-page-arrow {
        font-family: var(--f-display);
        font-size: 22px;
        width: 32px;
        height: 32px;
        line-height: 1;
        padding: 0;
        border: 1px solid var(--line-strong);
        background: var(--paper-card);
        color: var(--navy);
        cursor: pointer;
        border-radius: 2px;
      }
      .th-page-arrow:hover:not(:disabled) {
        background: var(--gold);
        border-color: var(--gold-deep);
        color: var(--navy-deep);
      }
      .th-page-arrow:disabled { opacity: 0.35; cursor: not-allowed; }
      .th-page-list {
        list-style: none;
        margin: 0;
        padding: 0;
        display: flex;
        gap: 4px;
      }
      .th-page-num {
        font-family: var(--f-mono);
        font-size: 12px;
        min-width: 32px;
        height: 32px;
        padding: 0 10px;
        border: 1px solid var(--line-strong);
        background: var(--paper-card);
        color: var(--ink-soft);
        cursor: pointer;
        border-radius: 2px;
      }
      .th-page-num:hover { background: var(--gold-soft); color: var(--ink); }
      .th-page-num.is-current {
        background: var(--navy);
        border-color: var(--navy-deep);
        color: var(--gold);
        font-weight: 600;
      }
      .th-page-ellipsis {
        align-self: center;
        color: var(--muted);
        font-family: var(--f-mono);
        padding: 0 4px;
      }
      .th-page-meta {
        margin-left: auto;
        font-family: var(--f-mono);
        font-size: 11px;
        color: var(--ink-soft);
      }

      /* MOBILE */
      @media (max-width: 720px) {
        .th-root { padding: 20px 16px; }
        .th-c-day { display: none; }
        .th-row td:nth-child(2) { display: none; }
        .th-table thead th { padding: 9px 10px; }
        .th-row td { padding: 10px; font-size: 12.5px; }
      }

      /* PRINT */
      @media print {
        .th-root {
          background: #fff;
          padding: 0;
          border: none;
          max-width: none;
        }
        .th-root::before { display: none; }
        .th-no-print { display: none !important; }
        .th-table thead th {
          background: #fff !important;
          color: var(--ink) !important;
          border-bottom: 2px solid var(--ink) !important;
          -webkit-print-color-adjust: exact;
          print-color-adjust: exact;
        }
        .th-stat--gold,
        .th-stat--navy {
          background: #fff !important;
        }
        .th-row:hover td { background: transparent !important; }
        .th-table { font-size: 10.5px; }
        .th-row td { padding: 6px 10px; }
        a { color: inherit; text-decoration: none; }
        .th-row--milestone, .th-row--critical {
          border-left-width: 2px;
        }
        thead { display: table-header-group; }
        tfoot { display: table-footer-group; }
        tr { page-break-inside: avoid; }
      }
    `}</style>
  );
}
---
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
    if (!session.get()) {
      router.push("/sign-in");
      return;
    }
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
        router.push("/sign-in");
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
        <Link
          href="/commons"
          className="btn-primary text-center"
        >
          Enter The Commons →
        </Link>
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
            <div className="flex-1 min-w-0 overflow-y-auto">
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
---
import { session, ApiError } from "@/lib/api";
export interface FounderTokenData { serial_number: string; minted_at: string; cohort: string; display: string; }
export interface BalancesResponse { ems_balance: number; pms_balance: number; founder_token: FounderTokenData | null; balance_last_updated: string | null; }
export interface LedgerEntry { id: string; token_class: "EMS" | "PMS" | string; transaction_type: string; amount: string; created_at: string; note?: string; }
export interface LedgerResponse { entries: LedgerEntry[]; total: number; limit: number; offset: number; }
async function portalRequest<T>(path: string, options: RequestInit = {}, expectedStatuses: number[] = [200]): Promise<T> {
  const token = session.get();
  const headers: Record<string,string> = { ...(options.headers as Record<string,string> ?? {}) };
  if (token) headers["Authorization"] = `Bearer ${token}`;
  const response = await fetch(path, { ...options, headers });
  if (!expectedStatuses.includes(response.status)) { let detail = response.statusText; try { const body = await response.json(); detail = body.detail || body.message || detail; } catch {} throw new ApiError(response.status, detail); }
  const text = await response.text(); if (!text) return {} as T; return JSON.parse(text);
}
export const portalApi = {
  myBalances: async (): Promise<BalancesResponse> => portalRequest<BalancesResponse>("/auth/portal/me/balances"),
  myLedger: async (limit = 50, offset = 0): Promise<LedgerResponse> => portalRequest<LedgerResponse>(`/auth/portal/me/ledger?limit=${limit}&offset=${offset}`),
};
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ 

