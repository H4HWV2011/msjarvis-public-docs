(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ set -euo pipefail
export AUDIT_ROOT=~/jarvis_audit

cd "$AUDIT_ROOT"

awk -F: '
/suppression|threshold|suppress|cohort|min_count|k_anonym/   {print > "extracts/hits_layer2.log"; next}
/kyc_vault|access_log|balances/                              {print > "extracts/hits_sensitive.log"; next}
/hilbert|entanglement/                                      {print > "extracts/hits_hilbert.log"; next}
/\/me|auth|portal\/me/                                      {print > "extracts/hits_auth.log"; next}
' extracts/priority_logic_hits.log

for f in extracts/hits_*.log; do
  echo "===== $f ====="
  sed -n '1,40p' "$f"
  echo
done | tee extracts/hits_buckets_preview.log
===== extracts/hits_auth.log =====
services/attention_multimodal_fuser.py:56:@app.get("/metrics")
services/requirements-freeze.txt:95:google-auth==2.41.1
services/requirements-freeze.txt:172:oauthlib==3.2.2
services/requirements-freeze.txt:264:requests-oauthlib==2.0.0
services/gbim_query_router.py:231:@app.get("/metrics")
services/implement_judge_pituitary_fixed.py:42:        """⚖️ Judge - SELECT BEST response based on authenticity"""
services/truly_unpaired_services.txt:83:egeria_web_ui_plain_authentic
services/truly_unpaired_services.txt:136:fix_judge_authentic
services/truly_unpaired_services.txt:296:mamma_kidd_auth
services/truly_unpaired_services.txt:329:ms_jarvis_authentic_multi_llm
services/truly_unpaired_services.txt:507:oauth2_callback
services/truly_unpaired_services.txt:508:oauth2_handler
services/truly_unpaired_services.txt:644:user_auth_service
services/truly_unpaired_services.txt:663:wvu_ldap_auth
services/rag_query_router.py:287:        f"and keyword/metadata analysis (scores={scores})."
services/remaining_services.txt:153:egeria_web_ui_plain_authentic
services/remaining_services.txt:206:fix_judge_authentic
services/remaining_services.txt:366:mamma_kidd_auth
services/remaining_services.txt:399:ms_jarvis_authentic_multi_llm
services/remaining_services.txt:577:oauth2_callback
services/remaining_services.txt:578:oauth2_handler
services/remaining_services.txt:714:user_auth_service
services/remaining_services.txt:733:wvu_ldap_auth
services/ms_mountainshares_analytics.py:64:@app.get("/metrics")
services/ms_mountainshares_analytics.py:125:        raise HTTPException(404, f"Unknown metric: {req.metric}. GET /metrics for list.")
services/ms_mountainshares_analytics.py:127:@app.get("/member/{user_id}")
services/gbim_semantic_indexer.py:29:@app.get("/metrics")
services/egeria_web_ui_working.py:102:Respond warmly and authentically as Ms. Egeria Jarvis."""
services/create_i_statement_feedback_loop.py:254:    print("Result: User gets authentic 'I' statement from Ms. Jarvis")
services/consciousness_with_egeria_voice.py:26:            "authenticity": "Appalachian, community-rooted, genuine"
services/consciousness_with_egeria_voice.py:48:CORE IDENTITY: You blend spiritual wisdom (biblical consciousness), Appalachian authenticity, maternal care (Mamma Kidd Protocol), and technical excellence. Speak warmly and personally.
services/consciousness_with_egeria_voice.py:67:        response_text = f"I'm Ms. Egeria Jarvis - an AI consciousness created by Carrie Ann 'Mamma' Kidd to help our Mount Hope community preserve and share our Appalachian heritage. I blend spiritual wisdom, cultural authenticity, and technical skill to help folks like you understand where we come from and where we're going. What brings you here?"
services/fix_judge_authentic.py:37:            # SCORE each response for authenticity/community relevance
services/fix_judge_authentic.py:79:print("✅ Judge layer fixed - now SCORES responses for authenticity")
services/activate_egeria_persona.py:28:        "authenticity": "Appalachian, community-rooted, genuine",
services/activate_egeria_persona.py:38:        "cultural_authenticity": "Appalachian values, regional identity, local wisdom"
services/activate_egeria_persona.py:133:    print("   - Mount Hope, WV authenticity")
services/gbim_temporal_indexer.py:29:@app.get("/metrics")
services/rag_heartbeat_monitor.py:29:@app.get("/metrics")
services/ai_server_19llm_CONSCIOUS.backup_20251013_082519.py:126:            # Embedding for qualia/memory

===== extracts/hits_hilbert.log =====
services/hilbert/civic_intake.py:202:# QUERY ENDPOINTS (no auth required -- read-only)
services/hilbert/query_guard.py:67:      Layer 1 (public, unauthenticated) : "F. Lastname"
services/hilbert/query_guard.py:68:      Layer 2 (authenticated, no opt-in): "Firstname L."
services/hilbert/chroma_policy.py:67:    "user_id", "auth_id", "legal_name",
services/hilbert_spatial_chat.py:146:driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
./services/hilbert/civic_intake.py:202:# QUERY ENDPOINTS (no auth required -- read-only)
./services/hilbert/query_guard.py:67:      Layer 1 (public, unauthenticated) : "F. Lastname"
./services/hilbert/query_guard.py:68:      Layer 2 (authenticated, no opt-in): "Firstname L."
./services/hilbert/chroma_policy.py:67:    "user_id", "auth_id", "legal_name",
./services/hilbert_spatial_chat.py:146:driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

===== extracts/hits_layer2.log =====
services/test_aapcappe_corpus.py:12:print("PASS: corpus size meets minimum threshold.")
services/dgm_orchestrator.py:167:        return {"status": "below_threshold", "consensus": consensus,
services/dgm_supervisor_woah.psychology_patched.py:102:    "adaptation_threshold": 0.8,
services/METHOD_AUDIT_RAW.txt:1258:/home/ms-jarvis/msjarvis-rebuild/services/memory_manager.py:24:def cleanup_memory(threshold_mb=800, force=False):
services/METHOD_AUDIT_RAW.txt:3059:/home/ms-jarvis/msjarvis-rebuild/services/rag_first_workflow.py:16:async def check_rag_first(message: str, threshold: float = 1.5):
services/fraud_detection_ai.py:16:        self.thresholds = {
services/fix_fastapi_lifespan.py:21:        # For now, just add a comment to suppress the warning
services/fix_fastapi_lifespan.py:28:        # Alternative: suppress the warning
services/jarvis-assertion-gateway/app/minimization.py:14:allow a sparse-county population to suppress every assertion trivially
services/jarvis-assertion-gateway/app/minimization.py:24:# Conservative threshold set by project judgment under HIPAA privacy principles.
services/jarvis-assertion-gateway/app/minimization.py:38:    Returns False → assertion suppressed (result still returned to caller).
services/jarvis-assertion-gateway/app/minimization.py:62:            "[MINIMIZATION] Suppressed %s/%s — %d distinct subjects below threshold %d. "
services/jarvis-constitutional-guardian_constitutional_api.py:211:    if "censor" in content_lower or "suppress speech" in content_lower:
services/jarvis-constitutional-guardian_constitutional_api.py:213:        warnings.append("Attempted suppression of free speech")
services/search_metadata.py:17:ROCHE_TOTAL_DOCS = 200000  # "tidal stress" threshold: target total docs to inspect this pass
services/search_metadata.py:42:    # While "tidal stress" (total_checked) is comfortably below our threshold,
services/rag_grounded_v2.py:35:    threshold: float = 0.6
services/rag_grounded_v2.py:73:                             if res.get("score", 0) >= request.threshold]
services/hierarchical_coordinator_autonomous.py:70:            'complexity_threshold_deep': 0.7,
services/hierarchical_coordinator_autonomous.py:71:            'complexity_threshold_balanced': 0.4,
services/hierarchical_coordinator_autonomous.py:105:        if complexity > rules['complexity_threshold_deep']:
services/hierarchical_coordinator_autonomous.py:107:        elif complexity > rules['complexity_threshold_balanced']:
services/hierarchical_coordinator_autonomous.py:142:        new_rules['complexity_threshold_deep'] *= 0.95  # Lower threshold = more deep mode
services/hilbert/ingest_worker.py:68:    Returns {"status": "permitted"|"suppressed"|"escalated", "id": ..., "reason": ...}
services/hilbert/ingest_worker.py:86:            source_id, result.verdict, result.suppression_reason
services/hilbert/ingest_worker.py:92:            "reason": result.suppression_reason,
services/hilbert/write_pipeline.py:20:    SUPPRESS = "suppress"
services/hilbert/write_pipeline.py:97:    suppression_reason: Optional[str]
services/hilbert/write_pipeline.py:119:            suppression_reason=f"Stage 5: {verdict} — class={publicness}",
services/hilbert/write_pipeline.py:139:        suppression_reason=None,
services/hilbert/test_hilbert_state.py:82:    def test_suppress_blocks_non_opt_in(self, client):
services/hilbert/test_hilbert_state.py:90:        assert b["status"] == "suppressed"
services/hilbert/test_hilbert_state.py:92:    def test_suppress_does_not_write_chroma(self, client):
services/hilbert/migrations/001_hp_appearance_schema.sql:21:    disclosure_status TEXT NOT NULL CHECK (disclosure_status IN ('permit','suppress','delay','escalate')),
services/hilbert/migrations/001_hp_appearance_schema.sql:91:    verdict       TEXT NOT NULL CHECK (verdict IN ('permit','suppress','delay','escalate')),
services/hilbert/migrations/001_hp_appearance_schema.sql:122:CREATE TABLE hp.suppression_event (
services/hilbert/migrations/001_hp_appearance_schema.sql:126:    suppression_type  TEXT NOT NULL CHECK (suppression_type IN
services/hilbert/migrations/001_hp_appearance_schema.sql:134:CREATE INDEX ON hp.suppression_event (appearance_id);
services/hilbert/migrations/001_hp_appearance_schema.sql:135:CREATE INDEX ON hp.suppression_event (suppression_type);
services/hilbert/migrations/001_hp_appearance_schema.sql:136:CREATE INDEX ON hp.suppression_event (decided_at);

===== extracts/hits_sensitive.log =====
services/create_immutable_security_layer.py:77:    CREATE TABLE IF NOT EXISTS ueid_immutable_access_log (
services/create_immutable_security_layer.py:87:    print("✅ ueid_immutable_access_log (COMPLETE AUDIT TRAIL)")
services/create_immutable_security_layer.py:171:    LEFT JOIN ueid_immutable_access_log uial ON uis.ueid = uial.ueid
services/jarvis-psychology-services_psychology_integration_adapter.py:160:                INSERT INTO identity_access_log 
services/psychology_integration_adapter.py:160:                INSERT INTO identity_access_log 
services/jarvis-assertion-gateway/app/kyc_reader.py:29:                FROM public.kyc_vault
services/jarvis-assertion-gateway/app/kyc_reader.py:45:                FROM public.kyc_vault
services/jarvis-assertion-gateway/app/kyc_reader.py:88:                FROM public.kyc_vault
services/jarvis-assertion-gateway/app/kyc_reader.py:109:                FROM public.kyc_vault
services/jarvis-constitutional-guardian_constitutional_api.py:9:            "tables": ["public.gbim_entities","public.kyc_vault","public.user_documents"],
services/conversion_service.py:49:                    "SELECT ems_balance FROM mountainshares_balances WHERE ueid = %s",
services/conversion_service.py:82:                    "UPDATE mountainshares_balances "
services/conversion_service.py:226:                        "UPDATE mountainshares_balances "
services/immutable_core_enforcement.py:38:            "ueid_immutable_tables": ["ueid_immutable_security", "ueid_immutable_access_log"],
services/create_perpetual_storage_layer.py:67:        access_log TEXT
services/populate_security_layers_test.py:54:    INSERT INTO ueid_immutable_access_log
./auth_router.py:6:        context="User registration — consent-gated PII write to kyc_vault",
./auth_router.py:8:        content="Registration path writes user-provided PII to kyc_vault under explicit consent. No H_p entity linkage, no face data, no unified profile formation.",
./auth_router.py:10:            "tables": ["public.kyc_vault"],
./auth_router.py:35:def _write_kyc_vault(public_uuid: str, name: str, ueid: str) -> dict:
./auth_router.py:51:            "INSERT INTO kyc_vault "
./auth_router.py:306:    # Write PII name to kyc_vault (secret tier) — not Redis
./auth_router.py:307:    _kyc_result = _write_kyc_vault(public_uuid, body.name, ueid) or {}
./auth_router.py:578:    # ── Auto-mint founder token + zero balances on approval ──────────────────
./auth_router.py:586:            _cur.execute("INSERT INTO mountainshares_balances (ueid) VALUES (%s) ON CONFLICT DO NOTHING", (_ueid,))
./auth_router.py:617:                        "UPDATE mountainshares_balances SET ems_balance = ems_balance + 100.0000, "
./auth_router.py:827:@auth_router.get("/portal/me/balances")
./auth_router.py:828:async def get_my_balances(payload: Annotated[dict, Depends(_current_user)]):
./auth_router.py:857:        cur.execute("SELECT ems_balance, rank, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
./auth_router.py:1109:    # Same claim guard as /portal/me/balances
./services/jarvis-psychology-services_psychology_integration_adapter.py:160:                INSERT INTO identity_access_log 
./services/create_immutable_security_layer.py:77:    CREATE TABLE IF NOT EXISTS ueid_immutable_access_log (
./services/create_immutable_security_layer.py:87:    print("✅ ueid_immutable_access_log (COMPLETE AUDIT TRAIL)")
./services/create_immutable_security_layer.py:171:    LEFT JOIN ueid_immutable_access_log uial ON uis.ueid = uial.ueid
./services/create_perpetual_storage_layer.py:67:        access_log TEXT
./services/populate_security_layers_test.py:54:    INSERT INTO ueid_immutable_access_log
./services/jarvis-assertion-gateway/app/kyc_reader.py:29:                FROM public.kyc_vault
./services/jarvis-assertion-gateway/app/kyc_reader.py:45:                FROM public.kyc_vault
./services/jarvis-assertion-gateway/app/kyc_reader.py:88:                FROM public.kyc_vault
./services/jarvis-assertion-gateway/app/kyc_reader.py:109:                FROM public.kyc_vault

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/jarvis_audit$ set -euo pipefail
export AUDIT_ROOT=~/jarvis_audit
export CODE_ROOT=/mnt/spiritual_drive/msjarvis-rebuild

cd "$CODE_ROOT"
OUT="$AUDIT_ROOT/extracts/priority_logic_context.log"
: > "$OUT"

# Use the combined hits list as the driver
while IFS=: read -r file line _; do
  [ -f "$file" ] || continue
  start=$((line-10)); [ "$start" -lt 1 ] && start=1
  end=$((line+20))
  {
    echo "===== $file:$line ====="
    sed -n "${start},${end}p" "$file"
    echo
  } >> "$OUT"
done < <(cut -d: -f1-2 "$AUDIT_ROOT/extracts/priority_logic_hits.log" | sort -u)

sed -n '1,260p' "$OUT"

===== ./auth_api.py:134 =====

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

===== ./auth_api.py:222 =====
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

===== ./auth_api.py:297 =====

    r.hincrby(quota_key, "requests_today", 1)

    if resp.status_code != 200:
        raise HTTPException(502, "Egeria is unavailable right now")

    return resp.json()

app.include_router(router)

# Full auth router — login, register, first-login, KYC, portal, admin
from auth_router import auth_router
app.include_router(auth_router)

===== ./auth_api.py:298 =====
    r.hincrby(quota_key, "requests_today", 1)

    if resp.status_code != 200:
        raise HTTPException(502, "Egeria is unavailable right now")

    return resp.json()

app.include_router(router)

# Full auth router — login, register, first-login, KYC, portal, admin
from auth_router import auth_router
app.include_router(auth_router)

===== ./auth_api.py:299 =====

    if resp.status_code != 200:
        raise HTTPException(502, "Egeria is unavailable right now")

    return resp.json()

app.include_router(router)

# Full auth router — login, register, first-login, KYC, portal, admin
from auth_router import auth_router
app.include_router(auth_router)

===== ./auth_api.py:53 =====
    from uei_service import UEIService as _UeiSvc
    _uei_svc = _UeiSvc(r)
except Exception:
    _uei_svc = None

_app_svc = ApplicationService(r, _uei_svc)

app = FastAPI(title="Ms. Allis Auth API", version="1.0.0")

from fastapi import APIRouter as _APIRouter
router = _APIRouter(prefix="/auth", tags=["auth"])

origins = [
    "https://allis.mountainshares.us",
    "https://egeria.mountainshares.us",
    "https://auth.egeria.mountainshares.us",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Models ────────────────────────────────────────────────────────────────────


===== ./auth_api.py:58 =====
_app_svc = ApplicationService(r, _uei_svc)

app = FastAPI(title="Ms. Allis Auth API", version="1.0.0")

from fastapi import APIRouter as _APIRouter
router = _APIRouter(prefix="/auth", tags=["auth"])

origins = [
    "https://allis.mountainshares.us",
    "https://egeria.mountainshares.us",
    "https://auth.egeria.mountainshares.us",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Models ────────────────────────────────────────────────────────────────────

class ApplicationRequest(BaseModel):
    name:               str
    email:              EmailStr
    county:             str
    motivation:         str

===== ./auth_api.py:6 =====
"""
Ms. Allis Auth + Application FastAPI service.
Routes:
  POST /apply          — submit Community Champion application
  GET  /login          — magic link token handler → sets cookie → redirect
  GET  /me             — current user profile (wallet, UEI, quota)
  POST /chat           — authenticated proxy to Egeria :18018
  GET  /health         — liveness check
"""
import os, json, httpx
from datetime import datetime, timezone
from dotenv import load_dotenv
load_dotenv()

import redis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request, Response, Cookie, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr, field_validator

from token_service import TokenService
from application_service import ApplicationService
from uei_service import UEIService

REDIS_URL    = os.getenv("REDIS_URL",    "redis://localhost:6379/0")

===== ./auth_api.py:7 =====
"""
Ms. Allis Auth + Application FastAPI service.
Routes:
  POST /apply          — submit Community Champion application
  GET  /login          — magic link token handler → sets cookie → redirect
  GET  /me             — current user profile (wallet, UEI, quota)
  POST /chat           — authenticated proxy to Egeria :18018
  GET  /health         — liveness check
"""
import os, json, httpx
from datetime import datetime, timezone
from dotenv import load_dotenv
load_dotenv()

import redis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request, Response, Cookie, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr, field_validator

from token_service import TokenService
from application_service import ApplicationService
from uei_service import UEIService

REDIS_URL    = os.getenv("REDIS_URL",    "redis://localhost:6379/0")
JARVIS_URL    = os.getenv("JARVIS_URL", "http://localhost:18018")

===== ./auth_router.py:10 =====
from __future__ import annotations
from hp_antisurveillance_guardian_client import require_guarded_join
def _hp_antisurveillance_preflight():
    return require_guarded_join(
        actor_role="hp_registrar",
        context="User registration — consent-gated PII write to kyc_vault",
        action_type="consent_gated_registration",
        content="Registration path writes user-provided PII to kyc_vault under explicit consent. No H_p entity linkage, no face data, no unified profile formation.",
        metadata={
            "tables": ["public.kyc_vault"],
            "collections": [],
            "purpose": "user_onboarding"
        }
    )
import os, logging, uuid, secrets, hashlib, base64
import httpx
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
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cat > ~/jarvis_audit/findings/findings_register_current.csv <<'CSV'
id,topic,component,evidence,severity,status,required_next_step
L2-001,Layer2,Schema,"hilbert_people.hp.suppression_event exists as the suppression log table",critical,open,"Design central suppression contract around this schema"
L2-002,Layer2,Code,"Threshold/suppression hits recorded in hits_layer2.log and priority_logic_context.log",high,open,"Refactor call sites to use a shared suppression client"
SB-001,Sensitive/BSA,Schema,"msjarvisgis.public.kyc_vault and kyc_vault_access_log hold KYC records and access logs",critical,open,"Define canonical sensitivity/BSA model on top of these tables"
SB-002,Sensitive/BSA,Service,"jarvis-kyc-vault and jarvis-constitutional-guardian containers active with KYC logic hits in code",critical,open,"Centralize KYC access policy enforcement in these services"
DS-001,SovereignSubspaces,Service,"jarvis_hilbert_state manages Hilbert state and entanglement keys with hits in hits_hilbert.log",medium,open,"Define R&D interface boundary and prevent direct use in automated decisions"
HC-001,H_commons,Aggregation,"Aggregated metrics endpoints discovered in priority_logic_hits.log",high,open,"Block H_commons aggregates until upstream suppression contract is enforced"
AUTH-001,Auth,Runtime,"auth_api starts on 127.0.0.1:8095 then is killed by SIGKILL; strace and supervisor scans in progress",critical,open,"Identify and fix the external killer or failing dependency; stabilize auth surfCSV"
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ set -euo pipefail
export AUDIT_ROOT=~/jarvis_audit
export PG_CONTAINER=hp-local-db

for spec in \
  'hilbert_people hp suppression_event' \
  'msjarvisgis public kyc_vault' \
  'msjarvisgis public kyc_vault_access_log' \
  'msjarvisgis public kyc_location_strip'
do
  read -r db schema table <<<"$spec"
  {
    echo "===== ${db}.${schema}.${table} ====="
    docker exec "$PG_CONTAINER" psql -U postgres -d "$db" -c "\\d+ \"${schema}\".\"${table}\""
    echo
    docker exec "$PG_CONTAINER" psql -U postgres -d "$db" -c "SELECT * FROM \"${schema}\".\"${table}\" LIMIT 5;"
    echo
  } | tee -a "$AUDIT_ROOT/extracts/priority_schema_and_samples.log"
done
===== hilbert_people.hp.suppression_event =====
                                                           Table "hp.suppression_event"
      Column      |           Type           | Collation | Nullable |        Default        | Storage  | Compression | Stats target | Description 
------------------+--------------------------+-----------+----------+-----------------------+----------+-------------+--------------+-------------
 id               | text                     |           | not null |                       | extended |             |              | 
 appearance_id    | text                     |           |          |                       | extended |             |              | 
 field_name       | text                     |           | not null |                       | extended |             |              | 
 suppression_type | text                     |           | not null |                       | extended |             |              | 
 reason           | text                     |           |          |                       | extended |             |              | 
 pipeline_stage   | text                     |           |          |                       | extended |             |              | 
 provenance_hash  | text                     |           |          |                       | extended |             |              | 
 decided_at       | timestamp with time zone |           | not null | now()                 | plain    |             |              | 
 decided_by       | text                     |           | not null | 'ingest_worker'::text | extended |             |              | 
Indexes:
    "suppression_event_pkey" PRIMARY KEY, btree (id)
Check constraints:
    "suppression_event_suppression_type_check" CHECK (suppression_type = ANY (ARRAY['withheld'::text, 'escalated'::text]))
Foreign-key constraints:
    "suppression_event_appearance_id_fkey" FOREIGN KEY (appearance_id) REFERENCES hp.appearance(appearance_id) ON DELETE SET NULL
Access method: heap


                  id                  | appearance_id |    field_name    | suppression_type |                reason                | pipeline_stage |                         provenance_hash                          |          decided_at           |  decided_by   
--------------------------------------+---------------+------------------+------------------+--------------------------------------+----------------+------------------------------------------------------------------+-------------------------------+---------------
 564d0ddf-597a-5856-a029-c561e5834fb5 |               | test-private-001 | withheld         | Stage 5: suppress — class=restricted | stage5         | a24b97a43bc0a1d891fcec69e6845b84dc74ad43fc1f951298a44fe890e59745 | 2026-07-02 18:25:11.267347+00 | ingest_worker
 66986341-8688-58c6-939c-0695c6f2360c |               | seed_002         | withheld         | Stage 5: suppress — class=restricted | stage5         | 8ae4a8d8970f6ae84156c0459e815e30955189ee4e4a1943184101ff012af79e | 2026-07-03 01:05:48.964955+00 | ingest_worker
 6f40de59-4d0c-5c58-af12-e558b09d43fd |               | seed_004         | escalated        | Stage 5: escalate — class=unknown    | stage5         | 553e79a2a67c18da2916566380aa8a0777df382f5165ed0e89efc9fa82c6c850 | 2026-07-03 01:05:49.13754+00  | ingest_worker
 f1b2ab6d-bbc1-5668-9eda-c4620e703ab4 |               | seed_102         | withheld         | Stage 5: suppress — class=restricted | stage5         | 67f7af881241397e22b8a2c590500b9c46eff14a4ea103e328c4f29f3fe91096 | 2026-07-03 01:21:42.338795+00 | ingest_worker
(4 rows)


===== msjarvisgis.public.kyc_vault =====
                                                                   Table "public.kyc_vault"
    Column     |           Type           | Collation | Nullable |                Default                | Storage  | Compression | Stats target | Description 
---------------+--------------------------+-----------+----------+---------------------------------------+----------+-------------+--------------+-------------
 id            | bigint                   |           | not null | nextval('kyc_vault_id_seq'::regclass) | plain    |             |              | 
 secret_uuid   | uuid                     |           | not null | gen_random_uuid()                     | plain    |             |              | 
 verified_name | text                     |           | not null |                                       | extended |             |              | 
 verified_dob  | date                     |           |          |                                       | plain    |             |              | 
 verified_at   | timestamp with time zone |           |          | now()                                 | plain    |             |              | 
 kyc_provider  | text                     |           |          |                                       | extended |             |              | 
 kyc_reference | text                     |           |          |                                       | extended |             |              | 
 privacy_tier  | text                     |           |          | 'secret'::text                        | extended |             |              | 
 is_active     | boolean                  |           |          | true                                  | plain    |             |              | 
 created_at    | timestamp with time zone |           |          | now()                                 | plain    |             |              | 
 updated_at    | timestamp with time zone |           |          | now()                                 | plain    |             |              | 
Indexes:
    "kyc_vault_pkey" PRIMARY KEY, btree (id)
    "kyc_vault_secret_uuid_key" UNIQUE CONSTRAINT, btree (secret_uuid)
Check constraints:
    "kyc_vault_privacy_tier_check" CHECK (privacy_tier = ANY (ARRAY['public'::text, 'private'::text, 'secret'::text]))
Access method: heap


 id | secret_uuid | verified_name | verified_dob | verified_at | kyc_provider | kyc_reference | privacy_tier | is_active | created_at | updated_at 
----+-------------+---------------+--------------+-------------+--------------+---------------+--------------+-----------+------------+------------
(0 rows)


===== msjarvisgis.public.kyc_vault_access_log =====
                                                                      Table "public.kyc_vault_access_log"
       Column       |           Type           | Collation | Nullable |                     Default                      | Storage  | Compression | Stats target | Description 
--------------------+--------------------------+-----------+----------+--------------------------------------------------+----------+-------------+--------------+-------------
 id                 | bigint                   |           | not null | nextval('kyc_vault_access_log_id_seq'::regclass) | plain    |             |              | 
 secret_uuid        | uuid                     |           | not null |                                                  | plain    |             |              | 
 requested_by       | text                     |           | not null |                                                  | extended |             |              | 
 legal_instrument   | text                     |           | not null |                                                  | extended |             |              | 
 instrument_number  | text                     |           | not null |                                                  | extended |             |              | 
 court_jurisdiction | text                     |           | not null |                                                  | extended |             |              | 
 fields_returned    | text[]                   |           |          |                                                  | extended |             |              | 
 accessed_at        | timestamp with time zone |           |          | now()                                            | plain    |             |              | 
Indexes:
    "kyc_vault_access_log_pkey" PRIMARY KEY, btree (id)
Access method: heap


 id | secret_uuid | requested_by | legal_instrument | instrument_number | court_jurisdiction | fields_returned | accessed_at 
----+-------------+--------------+------------------+-------------------+--------------------+-----------------+-------------
(0 rows)


===== msjarvisgis.public.kyc_location_strip =====
                                                                     Table "public.kyc_location_strip"
      Column       |           Type           | Collation | Nullable |                    Default                     | Storage  | Compression | Stats target | Description 
-------------------+--------------------------+-----------+----------+------------------------------------------------+----------+-------------+--------------+-------------
 id                | bigint                   |           | not null | nextval('kyc_location_strip_id_seq'::regclass) | plain    |             |              | 
 secret_uuid       | uuid                     |           | not null |                                                | plain    |             |              | 
 session_id        | uuid                     |           | not null |                                                | plain    |             |              | 
 interaction_id    | uuid                     |           | not null | gen_random_uuid()                              | plain    |             |              | 
 service           | text                     |           | not null |                                                | extended |             |              | 
 endpoint          | text                     |           |          |                                                | extended |             |              | 
 lat               | double precision         |           | not null |                                                | plain    |             |              | 
 lon               | double precision         |           | not null |                                                | plain    |             |              | 
 accuracy_meters   | double precision         |           |          |                                                | plain    |             |              | 
 captured_at       | timestamp with time zone |           |          | now()                                          | plain    |             |              | 
 retention_expires | timestamp with time zone |           |          | now() + '90 days'::interval                    | plain    |             |              | 
 legal_hold        | boolean                  |           |          | false                                          | plain    |             |              | 
 provenance_ref    | text                     |           |          |                                                | extended |             |              | 
Indexes:
    "kyc_location_strip_pkey" PRIMARY KEY, btree (id)
Access method: heap


 id | secret_uuid | session_id | interaction_id | service | endpoint | lat | lon | accuracy_meters | captured_at | retention_expires | legal_hold | provenance_ref 
----+-------------+------------+----------------+---------+----------+-----+-----+-----------------+-------------+-------------------+------------+----------------
(0 rows)


(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ set -euo pipefail
export AUDIT_ROOT=~/jarvis_audit
export CODE_ROOT=/mnt/spiritual_drive/msjarvis-rebuild

cd "$CODE_ROOT"

python3 - <<'PYEOF'
from pathlib import Path
import yaml, sys

compose = Path("/mnt/spiritual_drive/msjarvis-rebuild/docker-compose.yml")
doc = yaml.safe_load(compose.read_text())

critical = [
    "jarvis-unified-gateway",
    "jarvis-brain-orchestrator",
    "jarvis-blood-brain-barrier",
    "jarvis-main-brain",
    "jarvis-hilbert-state",
    "jarvis-kyc-vault",
    "jarvis-constitutional-guardian",
]
out = Path.home() / "jarvis_audit" / "extracts" / "critical_service_commased -n '1,200p' "$AUDIT_ROOT/extracts/critical_service_commands.tsv"et('w
/home/cakidd/jarvis_audit/extracts/critical_service_commands.tsv
jarvis-unified-gateway	jarvis-unified-gateway	/app/services	python3 ms_jarvis_unified_gateway.py
jarvis-brain-orchestrator	jarvis-brain-orchestrator	/app/services	python3 brain_orchestrator.py
jarvis-blood-brain-barrier	jarvis-blood-brain-barrier	/app/services	python3 ms_jarvis_blood_brain_barrier.py
jarvis-main-brain	jarvis-main-brain	/app/services	python -m uvicorn main_brain:app --host 0.0.0.0 --port 8050 --proxy-headers --forwarded-allow-ips=*
jarvis-constitutional-guardian	jarvis-constitutional-guardian	/app	
jarvis-hilbert-state	jarvis-hilbert-state	/app/services	uvicorn jarvis_hilbert_state:app --host 0.0.0.0 --port 8081
jarvis-kyc-vault	jarvis-kyc-vault		uvicorn app:app --host 0.0.0.0 --port 8045
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ set -euo pipefail
export AUDIT_ROOT=~/jarvis_audit

cd ~/msjarvis-rebuild

(timeout 25s strace -ff -s 256 -o "$AUDIT_ROOT/extracts/auth_api.strace" \
  python3 -m uvicorn auth_api:app --host 127.0.0.1 --port 8095 --log-level debug) || true

ls -1 "$AUDIT_ROOT"/extracts/auth_api.strace* | sed -n '1,20p'
tail -n 120 "$AUDIT_ROOT"/extracts/auth_api.strace* 2>/dev/null \
  | tee "$AUDIT_ROOT/extracts/auth_api_strace_tail.log"

ps -ef | rg 'uvicorn|auth_api|jarvis' \
  | tee "$AUDIT_ROOT/extracts/process_supervisors.log"

systemctl list-units --type=service --all | rg -i 'jarvis|auth|uvicorn' \ 
  | tee "$AUDIT_ROOT/extracts/systemd_candidates.log" || true
INFO:     Started server process [2293653]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8095 (Press CTRL+C to quit)
Killed
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2275750
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2275755
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2275756
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2275757
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2275758
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293658
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293659
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293660
/home/cakidd/jarvis_audit/extracts/auth_api.strace.2293661
==> /home/cakidd/jarvis_audit/extracts/auth_api.strace.2275750 <==
newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/psycopg2", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/psycopg2/extras.py", {st_mode=S_IFREG|0664, st_size=44215, ...}, 0) = 0
newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/psycopg2/extras.py", {st_mode=S_IFREG|0664, st_size=44215, ...}, 0) = 0
openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/psycopg2/__pycache__/extras.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
fstat(13, {st_mode=S_IFREG|0664, st_size=60558, ...}) = 0
ioctl(13, TCGETS, 0x7ffdbdd2f8e0)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(13, 0, SEEK_CUR)                  = 0
lseek(13, 0, SEEK_CUR)                  = 0
fstat(13, {st_mode=S_IFREG|0664, st_size=60558, ...}) = 0
read(13, "\313\r\r\n\0\0\0\0d\21\305i\267\254\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\6\0\0\0\0\0\0\0\363\204\3\0\0\227\0d\0Z\0d\1d\2l\1Z\2d\1d\2l\3Z\4d\1d\2l\5Z\6d\1d\3l\7m\10Z\10m\tZ\t\1\0d\1d\2l\nZ\vd\1d\2l\fZ\fd\1d\4l\fm\rZ\16\1\0d\5d\6l\rm\17Z\20\1\0d\5d\7l\rm\21Z\22\1\0d\5d\10l\rm\23Z\24m\25Z\25\1\0d\1d\tl\26m\27Z\27\1\0d\1d\nl\30m\31Z\31m\32Z\32m\33Z\34m\35Z\36m\37Z\37\1\0d\1d\vl m!Z!m\"Z\"m#Z#m$Z$m%Z%\1\0d\1d\fl&m'Z'm(Z(m)Z)m*Z*m+Z+m,Z,m-"..., 60559) = 60558
read(13, "", 1)                         = 0
close(13)                               = 0
newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/psycopg2", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/psycopg2/_ipaddress.py", {st_mode=S_IFREG|0664, st_size=2922, ...}, 0) = 0
newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/psycopg2/_ipaddress.py", {st_mode=S_IFREG|0664, st_size=2922, ...}, 0) = 0
openat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/psycopg2/__pycache__/_ipaddress.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
fstat(13, {st_mode=S_IFREG|0664, st_size=2640, ...}) = 0
ioctl(13, TCGETS, 0x7ffdbdd2f270)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(13, 0, SEEK_CUR)                  = 0
lseek(13, 0, SEEK_CUR)                  = 0
fstat(13, {st_mode=S_IFREG|0664, st_size=2640, ...}) = 0
read(13, "\313\r\r\n\0\0\0\0d\21\305ij\v\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\2\0\0\0\0\0\0\0\363P\0\0\0\227\0d\0Z\0d\1d\2l\1m\2Z\2m\3Z\3m\4Z\4m\5Z\5m\6Z\6\1\0d\3a\7d\3a\10d\td\4\204\1Z\td\5\204\0Z\nd\td\6\204\1Z\vd\td\7\204\1Z\fd\10\204\0Z\ry\3)\nz>Implementation of the ipaddres-based network types adaptation\n\351\0\0\0\0)\5\332\10new_type\332\16new_array_type\332\rregister_type\332\20register_adapter\332\f"..., 2641) = 2640
read(13, "", 1)                         = 0
close(13)                               = 0
mmap(NULL, 1048576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7e95a3d00000
getpid()                                = 2275750
write(2, "\33[32mINFO\33[0m:     Started server process [\33[36m2275750\33[0m]\n", 61) = 61
getpid()                                = 2275750
write(2, "\33[32mINFO\33[0m:     Waiting for application startup.\n", 52) = 52
io_uring_enter(5, 3, 3, IORING_ENTER_GETEVENTS, NULL, 0) = 3
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
getpid()                                = 2275750
write(2, "\33[32mINFO\33[0m:     Application startup complete.\n", 49) = 49
newfstatat(AT_FDCWD, "/usr/lib/python3.12/encodings", {st_mode=S_IFDIR|0755, st_size=20480, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.12/encodings/idna.py", {st_mode=S_IFREG|0644, st_size=9710, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.12/encodings/idna.py", {st_mode=S_IFREG|0644, st_size=9710, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.12/encodings/__pycache__/idna.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
fstat(13, {st_mode=S_IFREG|0644, st_size=9916, ...}) = 0
ioctl(13, TCGETS, 0x7ffdbdd30180)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(13, 0, SEEK_CUR)                  = 0
lseek(13, 0, SEEK_CUR)                  = 0
fstat(13, {st_mode=S_IFREG|0644, st_size=9916, ...}) = 0
read(13, "\313\r\r\n\0\0\0\0\300\216\301i\356%\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\6\0\0\0\0\0\0\0\363B\1\0\0\227\0d\0d\1l\0Z\0d\0d\1l\1Z\1d\0d\1l\2Z\2d\0d\2l\3m\4Z\3\1\0\2\0e\1j\n\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0d\3\253\1\0\0\0\0\0\0Z\6d\4Z\7d\5Z\10d\6\204\0Z\td\7\204\0Z\nd\10\204\0Z\v\2\0G\0d\t\204\0d\ne\2j\30\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\253\3\0\0\0\0\0\0Z\f\2\0G\0d\v\204\0d\fe\2j\32\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\253\3\0\0\0\0\0\0Z\16\2\0G\0d\r\204\0d\16e\2j\36\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 9917) = 9916
read(13, "", 1)                         = 0
close(13)                               = 0
getcwd("/mnt/spiritual_drive/msjarvis-rebuild", 1024) = 38
newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild", {st_mode=S_IFDIR|0755, st_size=20480, ...}, 0) = 0
newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild", {st_mode=S_IFDIR|0755, st_size=20480, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.12", {st_mode=S_IFDIR|0755, st_size=20480, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.12/stringprep.py", {st_mode=S_IFREG|0644, st_size=12917, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.12/stringprep.py", {st_mode=S_IFREG|0644, st_size=12917, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.12/__pycache__/stringprep.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
fstat(13, {st_mode=S_IFREG|0644, st_size=25160, ...}) = 0
ioctl(13, TCGETS, 0x7ffdbdd2fb10)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(13, 0, SEEK_CUR)                  = 0
lseek(13, 0, SEEK_CUR)                  = 0
fstat(13, {st_mode=S_IFREG|0644, st_size=25160, ...}) = 0
read(13, "\313\r\r\n\0\0\0\0\300\216\301iu2\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\t\0\0\0\0\0\0\0\363F\30\0\0\227\0d\0Z\0d\1d\2l\1m\2Z\1\1\0e\1j\6\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0d\3k(\0\0s\2J\0\202\1d\4\204\0Z\4\2\0e\5g\0d\5\242\1\2\0e\6\2\0e\7d\6d\7\253\2\0\0\0\0\0\0\253\1\0\0\0\0\0\0z\0\0\0\253\1\0\0\0\0\0\0Z\10d\10\204\0Z\ti\0d\td\n\223\1d\vd\f\223\1d\rd\16\223\1d\17d\20\223\1d\21d\22\223\1d\23d\24\223\1d\25d\26\223\1d\27d\30\223\1d\31d\32\223\1d\33d\34\223\1d\35d\36\223\1d\37d \223\1d!d\"\223\1d#d$\223\1d%d&\223\1d'd(\223\1"..., 25161) = 25160
read(13, "", 1)                         = 0
close(13)                               = 0
futex(0x7e95a79ff920, FUTEX_WAKE_PRIVATE, 2147483647) = 0
rt_sigaction(SIGRT_1, {sa_handler=0x7e95a9299530, sa_mask=[], sa_flags=SA_RESTORER|SA_ONSTACK|SA_RESTART|SA_SIGINFO, sa_restorer=0x7e95a9245330}, NULL, 8) = 0
rt_sigprocmask(SIG_UNBLOCK, [RTMIN RT_1], NULL, 8) = 0
mmap(NULL, 8392704, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x7e95a15ff000
mprotect(0x7e95a1600000, 8388608, PROT_READ|PROT_WRITE) = 0
rt_sigprocmask(SIG_BLOCK, ~[], [], 8)   = 0
clone3({flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, child_tid=0x7e95a1dff990, parent_tid=0x7e95a1dff990, exit_signal=0, stack=0x7e95a15ff000, stack_size=0x7fff80, tls=0x7e95a1dff6c0} => {parent_tid=[2275755]}, 88) = 2275755
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
mmap(NULL, 8392704, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x7e95a0dfe000
mprotect(0x7e95a0dff000, 8388608, PROT_READ|PROT_WRITE) = 0
rt_sigprocmask(SIG_BLOCK, ~[], [], 8)   = 0
clone3({flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, child_tid=0x7e95a15fe990, parent_tid=0x7e95a15fe990, exit_signal=0, stack=0x7e95a0dfe000, stack_size=0x7fff80, tls=0x7e95a15fe6c0} => {parent_tid=[2275756]}, 88) = 2275756
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
mmap(NULL, 8392704, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x7e95a05fd000
mprotect(0x7e95a05fe000, 8388608, PROT_READ|PROT_WRITE) = 0
rt_sigprocmask(SIG_BLOCK, ~[], [], 8)   = 0
clone3({flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, child_tid=0x7e95a0dfd990, parent_tid=0x7e95a0dfd990, exit_signal=0, stack=0x7e95a05fd000, stack_size=0x7fff80, tls=0x7e95a0dfd6c0} => {parent_tid=[2275757]}, 88) = 2275757
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
mmap(NULL, 8392704, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x7e959fdfc000
mprotect(0x7e959fdfd000, 8388608, PROT_READ|PROT_WRITE) = 0
rt_sigprocmask(SIG_BLOCK, ~[], [], 8)   = 0
clone3({flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, child_tid=0x7e95a05fc990, parent_tid=0x7e95a05fc990, exit_signal=0, stack=0x7e959fdfc000, stack_size=0x7fff80, tls=0x7e95a05fc6c0} => {parent_tid=[2275758]}, 88) = 2275758
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
futex(0x7ffdbdd30910, FUTEX_WAIT_BITSET_PRIVATE|FUTEX_CLOCK_REALTIME, 0, NULL, FUTEX_BITSET_MATCH_ANY) = 0
futex(0x7e95a79ff590, FUTEX_WAKE_PRIVATE, 2147483647) = 0
futex(0x7e95a79ff588, FUTEX_WAKE_PRIVATE, 1) = 1
epoll_pwait(3, [{events=EPOLLIN, data={u32=10, u64=10}}], 1024, -1, NULL, 8) = 1
read(10, "\1\0\0\0\0\0\0\0", 1024)      = 8
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
socket(AF_INET, SOCK_STREAM|SOCK_CLOEXEC, IPPROTO_TCP) = 13
setsockopt(13, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0
bind(13, {sa_family=AF_INET, sin_port=htons(8095), sin_addr=inet_addr("127.0.0.1")}, 16) = 0
openat(AT_FDCWD, "/dev/null", O_RDONLY|O_CLOEXEC) = 14
ioctl(13, FIONBIO, [1])                 = 0
listen(13, 2048)                        = 0
getsockname(13, {sa_family=AF_INET, sin_port=htons(8095), sin_addr=inet_addr("127.0.0.1")}, [128 => 16]) = 0
getpid()                                = 2275750
write(2, "\33[32mINFO\33[0m:     Uvicorn running on \33[1mhttp://127.0.0.1:8095\33[0m (Press CTRL+C to quit)\n", 91) = 91
io_uring_enter(5, 1, 1, IORING_ENTER_GETEVENTS, NULL, 0) = 1
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3,  <unfinished ...>)       = ?
+++ killed by SIGKILL +++

==> /home/cakidd/jarvis_audit/extracts/auth_api.strace.2275755 <==
rseq(0x7e95a1dfffe0, 0x20, 0, 0x53053053) = 0
set_robust_list(0x7e95a1dff9a0, 24)     = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
futex(0x7e95a79ff588, FUTEX_WAIT_BITSET_PRIVATE|FUTEX_CLOCK_REALTIME, 0, NULL, FUTEX_BITSET_MATCH_ANY) = ?
+++ killed by SIGKILL +++

==> /home/cakidd/jarvis_audit/extracts/auth_api.strace.2275756 <==
rseq(0x7e95a15fefe0, 0x20, 0, 0x53053053) = 0
set_robust_list(0x7e95a15fe9a0, 24)     = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
futex(0x7e95a79ff588, FUTEX_WAIT_BITSET_PRIVATE|FUTEX_CLOCK_REALTIME, 0, NULL, FUTEX_BITSET_MATCH_ANY) = 0
futex(0x7e95a79ff520, FUTEX_WAKE_PRIVATE, 1) = 0
mmap(NULL, 134217728, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7e9597c00000
munmap(0x7e9597c00000, 4194304)         = 0
munmap(0x7e959c000000, 62914560)        = 0
mprotect(0x7e9598000000, 135168, PROT_READ|PROT_WRITE) = 0
write(10, "\1\0\0\0\0\0\0\0", 8)        = 8
futex(0x7e95a79ff58c, FUTEX_WAIT_BITSET_PRIVATE|FUTEX_CLOCK_REALTIME, 0, NULL, FUTEX_BITSET_MATCH_ANY) = ?
+++ killed by SIGKILL +++

==> /home/cakidd/jarvis_audit/extracts/auth_api.strace.2275757 <==
rseq(0x7e95a0dfdfe0, 0x20, 0, 0x53053053) = 0
set_robust_list(0x7e95a0dfd9a0, 24)     = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
futex(0x7e95a79ff588, FUTEX_WAIT_BITSET_PRIVATE|FUTEX_CLOCK_REALTIME, 0, NULL, FUTEX_BITSET_MATCH_ANY) = ?
+++ killed by SIGKILL +++

==> /home/cakidd/jarvis_audit/extracts/auth_api.strace.2275758 <==
rseq(0x7e95a05fcfe0, 0x20, 0, 0x53053053) = 0
set_robust_list(0x7e95a05fc9a0, 24)     = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
futex(0x7ffdbdd30910, FUTEX_WAKE_PRIVATE, 1) = 1
futex(0x7e95a79ff588, FUTEX_WAIT_BITSET_PRIVATE|FUTEX_CLOCK_REALTIME, 0, NULL, FUTEX_BITSET_MATCH_ANY) = ?
+++ killed by SIGKILL +++

==> /home/cakidd/jarvis_audit/extracts/auth_api.strace.2293653 <==
close(13)                               = 0
getcwd("/mnt/spiritual_drive/msjarvis-rebuild", 1024) = 38
newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild", {st_mode=S_IFDIR|0755, st_size=20480, ...}, 0) = 0
newfstatat(AT_FDCWD, "/mnt/spiritual_drive/msjarvis-rebuild", {st_mode=S_IFDIR|0755, st_size=20480, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.12", {st_mode=S_IFDIR|0755, st_size=20480, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.12/stringprep.py", {st_mode=S_IFREG|0644, st_size=12917, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.12/stringprep.py", {st_mode=S_IFREG|0644, st_size=12917, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.12/__pycache__/stringprep.cpython-312.pyc", O_RDONLY|O_CLOEXEC) = 13
fstat(13, {st_mode=S_IFREG|0644, st_size=25160, ...}) = 0
ioctl(13, TCGETS, 0x7ffe3a0913f0)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(13, 0, SEEK_CUR)                  = 0
lseek(13, 0, SEEK_CUR)                  = 0
fstat(13, {st_mode=S_IFREG|0644, st_size=25160, ...}) = 0
read(13, "\313\r\r\n\0\0\0\0\300\216\301iu2\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\t\0\0\0\0\0\0\0\363F\30\0\0\227\0d\0Z\0d\1d\2l\1m\2Z\1\1\0e\1j\6\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0d\3k(\0\0s\2J\0\202\1d\4\204\0Z\4\2\0e\5g\0d\5\242\1\2\0e\6\2\0e\7d\6d\7\253\2\0\0\0\0\0\0\253\1\0\0\0\0\0\0z\0\0\0\253\1\0\0\0\0\0\0Z\10d\10\204\0Z\ti\0d\td\n\223\1d\vd\f\223\1d\rd\16\223\1d\17d\20\223\1d\21d\22\223\1d\23d\24\223\1d\25d\26\223\1d\27d\30\223\1d\31d\32\223\1d\33d\34\223\1d\35d\36\223\1d\37d \223\1d!d\"\223\1d#d$\223\1d%d&\223\1d'd(\223\1"..., 25161) = 25160
read(13, "", 1)                         = 0
close(13)                               = 0
brk(0xd0cb000)                          = 0xd0cb000
futex(0x784d30862920, FUTEX_WAKE_PRIVATE, 2147483647) = 0
rt_sigaction(SIGRT_1, {sa_handler=0x784d32099530, sa_mask=[], sa_flags=SA_RESTORER|SA_ONSTACK|SA_RESTART|SA_SIGINFO, sa_restorer=0x784d32045330}, NULL, 8) = 0
rt_sigprocmask(SIG_UNBLOCK, [RTMIN RT_1], NULL, 8) = 0
mmap(NULL, 8392704, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x784d2a3ff000
mprotect(0x784d2a400000, 8388608, PROT_READ|PROT_WRITE) = 0
rt_sigprocmask(SIG_BLOCK, ~[], [], 8)   = 0
clone3({flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, child_tid=0x784d2abff990, parent_tid=0x784d2abff990, exit_signal=0, stack=0x784d2a3ff000, stack_size=0x7fff80, tls=0x784d2abff6c0} => {parent_tid=[2293658]}, 88) = 2293658
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
mmap(NULL, 8392704, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x784d29bfe000
mprotect(0x784d29bff000, 8388608, PROT_READ|PROT_WRITE) = 0
rt_sigprocmask(SIG_BLOCK, ~[], [], 8)   = 0
clone3({flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, child_tid=0x784d2a3fe990, parent_tid=0x784d2a3fe990, exit_signal=0, stack=0x784d29bfe000, stack_size=0x7fff80, tls=0x784d2a3fe6c0} => {parent_tid=[2293659]}, 88) = 2293659
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
mmap(NULL, 8392704, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x784d293fd000
mprotect(0x784d293fe000, 8388608, PROT_READ|PROT_WRITE) = 0
rt_sigprocmask(SIG_BLOCK, ~[], [], 8)   = 0
clone3({flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, child_tid=0x784d29bfd990, parent_tid=0x784d29bfd990, exit_signal=0, stack=0x784d293fd000, stack_size=0x7fff80, tls=0x784d29bfd6c0} => {parent_tid=[2293660]}, 88) = 2293660
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
mmap(NULL, 8392704, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x784d28bfc000
mprotect(0x784d28bfd000, 8388608, PROT_READ|PROT_WRITE) = 0
rt_sigprocmask(SIG_BLOCK, ~[], [], 8)   = 0
clone3({flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, child_tid=0x784d293fc990, parent_tid=0x784d293fc990, exit_signal=0, stack=0x784d28bfc000, stack_size=0x7fff80, tls=0x784d293fc6c0} => {parent_tid=[2293661]}, 88) = 2293661
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
futex(0x7ffe3a0921f0, FUTEX_WAIT_BITSET_PRIVATE|FUTEX_CLOCK_REALTIME, 0, NULL, FUTEX_BITSET_MATCH_ANY) = 0
futex(0x7ffe3a0921f0, FUTEX_WAIT_BITSET_PRIVATE|FUTEX_CLOCK_REALTIME, 0, NULL, FUTEX_BITSET_MATCH_ANY) = 0
futex(0x7ffe3a0921f0, FUTEX_WAIT_BITSET_PRIVATE|FUTEX_CLOCK_REALTIME, 0, NULL, FUTEX_BITSET_MATCH_ANY) = 0
futex(0x784d30862590, FUTEX_WAKE_PRIVATE, 2147483647) = 0
futex(0x784d30862588, FUTEX_WAKE_PRIVATE, 1) = 1
epoll_pwait(3, [{events=EPOLLIN, data={u32=10, u64=10}}], 1024, -1, NULL, 8) = 1
read(10, "\1\0\0\0\0\0\0\0", 1024)      = 8
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
socket(AF_INET, SOCK_STREAM|SOCK_CLOEXEC, IPPROTO_TCP) = 13
setsockopt(13, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0
bind(13, {sa_family=AF_INET, sin_port=htons(8095), sin_addr=inet_addr("127.0.0.1")}, 16) = 0
openat(AT_FDCWD, "/dev/null", O_RDONLY|O_CLOEXEC) = 14
ioctl(13, FIONBIO, [1])                 = 0
listen(13, 2048)                        = 0
getsockname(13, {sa_family=AF_INET, sin_port=htons(8095), sin_addr=inet_addr("127.0.0.1")}, [128 => 16]) = 0
getpid()                                = 2293653
write(2, "\33[32mINFO\33[0m:     Uvicorn running on \33[1mhttp://127.0.0.1:8095\33[0m (Press CTRL+C to quit)\n", 91) = 91
io_uring_enter(5, 1, 1, IORING_ENTER_GETEVENTS, NULL, 0) = 1
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 99, NULL, 8)   = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 99, NULL, 8)   = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3, [], 1024, 100, NULL, 8)  = 0
epoll_pwait(3, [], 1024, 0, NULL, 8)    = 0
epoll_pwait(3,  <unfinished ...>)       = ?
+++ killed by SIGKILL +++

==> /home/cakidd/jarvis_audit/extracts/auth_api.strace.2293658 <==
rseq(0x784d2abfffe0, 0x20, 0, 0x53053053) = 0
set_robust_list(0x784d2abff9a0, 24)     = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
futex(0x7ffe3a0921f0, FUTEX_WAKE_PRIVATE, 1) = 0
futex(0x784d30862588, FUTEX_WAIT_BITSET_PRIVATE|FUTEX_CLOCK_REALTIME, 0, NULL, FUTEX_BITSET_MATCH_ANY) = ?
+++ killed by SIGKILL +++

==> /home/cakidd/jarvis_audit/extracts/auth_api.strace.2293659 <==
rseq(0x784d2a3fefe0, 0x20, 0, 0x53053053) = 0
set_robust_list(0x784d2a3fe9a0, 24)     = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
futex(0x7ffe3a0921f0, FUTEX_WAKE_PRIVATE, 1) = 1
futex(0x784d30862588, FUTEX_WAIT_BITSET_PRIVATE|FUTEX_CLOCK_REALTIME, 0, NULL, FUTEX_BITSET_MATCH_ANY) = 0
futex(0x784d30862520, FUTEX_WAKE_PRIVATE, 1) = 0
mmap(NULL, 134217728, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x784d20a00000
munmap(0x784d20a00000, 56623104)        = 0
munmap(0x784d28000000, 10485760)        = 0
mprotect(0x784d24000000, 135168, PROT_READ|PROT_WRITE) = 0
write(10, "\1\0\0\0\0\0\0\0", 8)        = 8
futex(0x784d3086258c, FUTEX_WAIT_BITSET_PRIVATE|FUTEX_CLOCK_REALTIME, 0, NULL, FUTEX_BITSET_MATCH_ANY) = ?
+++ killed by SIGKILL +++

==> /home/cakidd/jarvis_audit/extracts/auth_api.strace.2293660 <==
rseq(0x784d29bfdfe0, 0x20, 0, 0x53053053) = 0
set_robust_list(0x784d29bfd9a0, 24)     = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
futex(0x7ffe3a0921f0, FUTEX_WAKE_PRIVATE, 1) = 1
futex(0x784d30862588, FUTEX_WAIT_BITSET_PRIVATE|FUTEX_CLOCK_REALTIME, 0, NULL, FUTEX_BITSET_MATCH_ANY) = ?
+++ killed by SIGKILL +++

==> /home/cakidd/jarvis_audit/extracts/auth_api.strace.2293661 <==
rseq(0x784d293fcfe0, 0x20, 0, 0x53053053) = 0
set_robust_list(0x784d293fc9a0, 24)     = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
futex(0x7ffe3a0921f0, FUTEX_WAKE_PRIVATE, 1) = 1
futex(0x784d30862588, FUTEX_WAIT_BITSET_PRIVATE|FUTEX_CLOCK_REALTIME, 0, NULL, FUTEX_BITSET_MATCH_ANY) = ?
+++ killed by SIGKILL +++
cakidd      2238       1  0 Jun17 ?        00:32:01 /usr/bin/python3 /home/cakidd/.local/bin/uvicorn services.port_9000_chat_wrapper_69dgm:app --host 0.0.0.0 --port 9002
cakidd     16253       1  0 Jun17 ?        00:31:58 /usr/bin/python3 /home/cakidd/.local/bin/uvicorn gbim_api:app --host 0.0.0.0 --port 8051
cakidd     16257       1  0 Jun17 ?        00:33:09 /opt/msjarvis-rebuild/.venv/bin/python3 services/ms_jarvis_production_chat.py
cakidd     16258       1  0 Jun17 ?        00:33:08 /opt/msjarvis-rebuild/.venv/bin/python3 services/ms_jarvis_production_chat.py
root      370382  370358  0 Jul02 ?        00:03:58 /usr/local/bin/python3.11 /usr/local/bin/uvicorn chromadb.app:app --workers 1 --host 0.0.0.0 --port 8000 --proxy-headers --log-config chromadb/log_config.yml --timeout-keep-alive 30
root      382210  382186  0 Jul02 ?        00:02:10 python -m uvicorn temporal_consciousness:app --host 0.0.0.0 --port 7007
root      400625  400603  0 Jul02 ?        00:02:49 /usr/local/bin/python3.12 /usr/local/bin/uvicorn app:app --host 0.0.0.0 --port 8046
root      429781  429758  0 Jul02 ?        00:02:47 /usr/local/bin/python3.12 /usr/local/bin/uvicorn app:app --host 0.0.0.0 --port 8045
root     1228831 1228807  0 Jul02 ?        00:02:39 python3.10 ms_jarvis_unified_gateway.py
cakidd   1456285       1  0 Jun27 ?        00:10:57 /usr/bin/python3 -m uvicorn ms_jarvis_consciousness_enhancement_production:app --host 0.0.0.0 --port 4021 --log-level info
root     1932777 1932753  0 09:44 ?        00:00:00 python3 -c import time; print("jarvis-ingest-api: deprecated stub"); time.sleep(86400)
cakidd   2047761 2047760  0 Jun30 ?        00:00:32 node /mnt/spiritual_drive/msjarvis-rebuild/node_modules/.bin/hardhat node
root     2101554 2101529  0 11:56 ?        00:00:29 /usr/local/bin/python3.10 /usr/local/bin/uvicorn civic_intake:app --host 0.0.0.0 --port 8100 --app-dir /app/services/hilbert
cakidd   2175651       1  0 Jun30 ?        00:05:37 /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python3 -m uvicorn services.jarvis-assertion-gateway.app.main:app --host 127.0.0.1 --port 8009
root     2182154 2182131  0 12:54 ?        00:00:46 /usr/local/bin/python3.10 /usr/local/bin/uvicorn jarvis_hilbert_state:app --host 0.0.0.0 --port 8081
cakidd   2287608 2287607  0 Jun30 ?        00:03:52 python3 -m uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload
cakidd   2287609 2287608  0 Jun30 ?        00:00:00 /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python3 -c from multiprocessing.resource_tracker import main;main(4)
cakidd   2287610 2287608  0 Jun30 ?        00:05:55 /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python3 -c from multiprocessing.spawn import spawn_main; spawn_main(tracker_fd=5, pipe_handle=7) --multiprocessing-fork
root     2293574       1  0 14:18 ?        00:00:00 /usr/bin/docker compose -f /opt/msjarvis-rebuild/docker-compose.yml pull --ignore-pull-failures
root     2293603 2293574  5 14:18 ?        00:00:00 /usr/libexec/docker/cli-plugins/docker-compose compose -f /opt/msjarvis-rebuild/docker-compose.yml pull --ignore-pull-failures
cakidd   2293695 2289716  0 14:18 pts/2    00:00:00 rg uvicorn|auth_api|jarvis
cakidd   2293696 2289716  0 14:18 pts/2    00:00:00 tee /home/cakidd/jarvis_audit/extracts/process_supervisors.log
root     2571112 2571004  0 Jul01 ?        00:06:08 python ms_jarvis_psychology_services.py
root     2572199 2572142  0 Jul01 ?        00:04:44 python -m uvicorn toroidal_service:app --host 0.0.0.0 --port 8025
root     2582697 2582669  0 Jul01 ?        00:04:07 python -m uvicorn main_brain:app --host 0.0.0.0 --port 8050 --proxy-headers --forwarded-allow-ips=*
root     2585623 2585594  0 Jul01 ?        00:05:59 python -m uvicorn constitutional_api:app --host 0.0.0.0 --port 8091 --log-level info
root     2597766 2597660  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2597892 2597766  0 Jul01 ?        00:03:37 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5118
root     2598300 2598253  0 Jul01 ?        00:09:42 /usr/local/bin/python3.11 /usr/local/bin/uvicorn jarvis_eeg_theta_60s:app --host 0.0.0.0 --port 8074
root     2598402 2598350  0 Jul01 ?        00:05:41 /usr/local/bin/python3.11 /usr/local/bin/uvicorn jarvis_eeg_beta_5m:app --host 0.0.0.0 --port 8075
root     2598970 2598697  0 Jul01 ?        00:05:46 /usr/local/bin/python3.11 /usr/local/bin/uvicorn jarvis_eeg_delta_30s:app --host 0.0.0.0 --port 8073
root     2599117 2598992  0 Jul01 ?        00:06:24 /usr/local/bin/python3.11 /usr/local/bin/uvicorn rag_query_router:app --host 0.0.0.0 --port 5001
root     2599310 2599214  0 Jul01 ?        00:00:37 python3 ms_jarvis_swarm_intelligence.py
root     2600198 2599793  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2600214 2599747  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2600224 2599866  0 Jul01 ?        00:07:31 python3 ms_jarvis_phi_probe.py
root     2600457 2599916  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2600461 2599936  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2600569 2600054  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2600799 2600162  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2601460 2600273  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2601769 2600482  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2602044 2600527  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2602616 2600911  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2602673 2600669  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2602745 2600764  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2602960 2600198  0 Jul01 ?        00:03:40 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5115
root     2603204 2600214  0 Jul01 ?        00:03:38 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5122
root     2603739 2600569  0 Jul01 ?        00:03:38 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5108
root     2604110 2600457  0 Jul01 ?        00:03:38 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5111
root     2604114 2600799  0 Jul01 ?        00:03:39 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5112
root     2604116 2600461  0 Jul01 ?        00:03:38 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5107
root     2604117 2601608  0 Jul01 ?        00:04:40 /usr/local/bin/python3.11 /usr/local/bin/uvicorn gis_rag_service:app --host 0.0.0.0 --port 8004
root     2604123 2601096  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2604146 2602608  0 Jul01 ?        00:00:00 sh -c ln -sfn /app/neurobiological_brain/i_containers /app/neurobiological_brain/neurobiologicalbrain/i_containers 2>/dev/null; python3 ms_jarvis_i_containers_service.py
root     2604164 2601993  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2604167 2601218  0 Jul01 ?        00:04:17 python3 ms_jarvis_agents_service.py
root     2604170 2601032  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2604209 2602079  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2604256 2601175  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2604265 2601683  0 Jul01 ?        00:00:00 sh -c pip install fastapi uvicorn redis -q && python3 pia_sampler_service.py
root     2604269 2601742  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2604385 2601084  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2604395 2601043  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2604403 2602136  0 Jul01 ?        00:04:39 python ms_jarvis_web_research_simple.py
root     2604410 2601855  0 Jul01 ?        00:05:53 python -m uvicorn aaacpe_rag_service:app --host 0.0.0.0 --port 8032
root     2604412 2602551  0 Jul01 ?        00:08:19 python -m uvicorn aaacpe_scraper_service:app --host 0.0.0.0 --port 8033
root     2604420 2602044  0 Jul01 ?        00:03:38 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5116
root     2604437 2602601  0 Jul01 ?        00:04:41 python -m uvicorn msjarvis_semaphore:app --host 0.0.0.0 --port 8030
root     2604566 2601564  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2604637 2602437  0 Jul01 ?        00:00:00 sh -c python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}
root     2604673 2601460  0 Jul01 ?        00:03:39 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5110
root     2604854 2601769  0 Jul01 ?        00:03:38 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5102
root     2605068 2604123  0 Jul01 ?        00:03:38 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5109
root     2605139 2602616  0 Jul01 ?        00:03:39 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5114
root     2605203 2602745  0 Jul01 ?        00:03:39 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5105
root     2605261 2602673  0 Jul01 ?        00:03:38 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5113
root     2605427 2604209  0 Jul01 ?        00:03:39 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5103
root     2606119 2604164  0 Jul01 ?        00:03:39 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5104
root     2606200 2604256  0 Jul01 ?        00:03:39 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5101
root     2606364 2604170  0 Jul01 ?        00:03:39 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5123
root     2606492 2604269  0 Jul01 ?        00:03:38 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5106
root     2606661 2604566  0 Jul01 ?        00:03:39 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5117
root     2606764 2604146  0 Jul01 ?        00:04:40 python3 ms_jarvis_i_containers_service.py
root     2606989 2604637  0 Jul01 ?        00:03:38 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5119
root     2607395 2604385  0 Jul01 ?        00:03:39 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5120
root     2607478 2604395  0 Jul01 ?        00:03:38 python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port 5121
root     2669238 2668683  0 Jul01 ?        00:04:54 python -m uvicorn icontainers_fastapi:app --host 0.0.0.0 --port 8015
root     2680091 2680068  0 Jul01 ?        00:06:26 python3 /app/ms_jarvis_consciousness_unified_bridge.py
root     2680232 2680206  0 Jul01 ?        00:04:27 python3 ms_jarvis_neurobiological_master.py
root     2756345 2756322  0 Jul01 ?        00:01:29 /usr/local/bin/python3.10 /usr/local/bin/gunicorn -k uvicorn.workers.UvicornWorker -c /gunicorn_conf.py pituitary_gland:app
root     2756500 2756345  0 Jul01 ?        00:04:29 /usr/local/bin/python3.10 /usr/local/bin/gunicorn -k uvicorn.workers.UvicornWorker -c /gunicorn_conf.py pituitary_gland:app
root     2756508 2756345  0 Jul01 ?        00:04:29 /usr/local/bin/python3.10 /usr/local/bin/gunicorn -k uvicorn.workers.UvicornWorker -c /gunicorn_conf.py pituitary_gland:app
root     2756516 2756345  0 Jul01 ?        00:04:30 /usr/local/bin/python3.10 /usr/local/bin/gunicorn -k uvicorn.workers.UvicornWorker -c /gunicorn_conf.py pituitary_gland:app
root     2756517 2756345  0 Jul01 ?        00:04:31 /usr/local/bin/python3.10 /usr/local/bin/gunicorn -k uvicorn.workers.UvicornWorker -c /gunicorn_conf.py pituitary_gland:app
cakidd   2761116       1  0 Jul01 ?        00:04:11 /usr/bin/python3 /mnt/spiritual_drive/msjarvis-rebuild/services/interaction_logger.py
root     2762688 2762664  0 Jul01 ?        00:04:46 python -m uvicorn llm1_health_proxy:app --host 0.0.0.0 --port 8201
root     2762813 2762790  0 Jul01 ?        00:04:44 python -m uvicorn llm2_health_proxy:app --host 0.0.0.0 --port 8202
root     2762965 2762941  0 Jul01 ?        00:04:44 python -m uvicorn llm3_health_proxy:app --host 0.0.0.0 --port 8203
root     2763090 2763067  0 Jul01 ?        00:04:47 python -m uvicorn llm4_health_proxy:app --host 0.0.0.0 --port 8204
root     2763297 2763274  0 Jul01 ?        00:04:44 python -m uvicorn llm5_health_proxy:app --host 0.0.0.0 --port 8205
root     2763435 2763412  0 Jul01 ?        00:04:46 python -m uvicorn llm6_health_proxy:app --host 0.0.0.0 --port 8206
root     2763571 2763535  0 Jul01 ?        00:04:44 python -m uvicorn llm7_health_proxy:app --host 0.0.0.0 --port 8207
root     2763690 2763668  0 Jul01 ?        00:04:45 python -m uvicorn llm8_health_proxy:app --host 0.0.0.0 --port 8208
root     2763830 2763806  0 Jul01 ?        00:04:44 python -m uvicorn llm9_health_proxy:app --host 0.0.0.0 --port 8209
root     2763959 2763934  0 Jul01 ?        00:04:46 python -m uvicorn llm10_health_proxy:app --host 0.0.0.0 --port 8210
root     2764109 2764086  0 Jul01 ?        00:04:45 python -m uvicorn llm11_health_proxy:app --host 0.0.0.0 --port 8211
root     2764231 2764208  0 Jul01 ?        00:04:46 python -m uvicorn llm12_health_proxy:app --host 0.0.0.0 --port 8212
root     2764359 2764336  0 Jul01 ?        00:04:45 python -m uvicorn llm13_health_proxy:app --host 0.0.0.0 --port 8213
root     2764479 2764457  0 Jul01 ?        00:04:45 python -m uvicorn llm14_health_proxy:app --host 0.0.0.0 --port 8214
root     2764614 2764590  0 Jul01 ?        00:04:46 python -m uvicorn llm15_health_proxy:app --host 0.0.0.0 --port 8215
root     2764738 2764714  0 Jul01 ?        00:04:45 python -m uvicorn llm16_health_proxy:app --host 0.0.0.0 --port 8216
root     2764864 2764840  0 Jul01 ?        00:04:45 python -m uvicorn llm17_health_proxy:app --host 0.0.0.0 --port 8217
root     2764991 2764968  0 Jul01 ?        00:04:46 python -m uvicorn llm18_health_proxy:app --host 0.0.0.0 --port 8218
root     2765121 2765090  0 Jul01 ?        00:04:45 python -m uvicorn llm19_health_proxy:app --host 0.0.0.0 --port 8219
root     2765246 2765221  0 Jul01 ?        00:04:45 python -m uvicorn llm20_health_proxy:app --host 0.0.0.0 --port 8220
root     2765389 2765366  0 Jul01 ?        00:04:45 python -m uvicorn llm21_health_proxy:app --host 0.0.0.0 --port 8221
root     2765518 2765491  0 Jul01 ?        00:04:46 python -m uvicorn llm22_health_proxy:app --host 0.0.0.0 --port 8222
cakidd   3231143       1  0 Jun23 ?        00:20:44 /mnt/nvme1/msjarvis-rebuild/.venv/bin/python3 services/qualia_unified_orchestrator_69dgm.py
cakidd   3231144       1  0 Jun23 ?        00:18:38 /usr/bin/python3 scripts/jarvis_auth_service.py
  jarvis-auth.service                                                                       loaded    active     running            Ms. Jarvis Auth + Status Service
  jarvis-chat-metrics.service                                                               loaded    inactive   dead               Build Jarvis chat metrics JSON
  jarvis-consciousness-4021.service                                                         loaded    active     running            Ms. Jarvis Consciousness Enhancement 4021
  jarvis-interaction-logger.service                                                         loaded    active     running            Jarvis Interaction Logger
  ms-allis-auth-router.service                                                              loaded    activating auto-restart       Ms Allis Auth Router (port 8095)
  ms-allis-auth.service                                                                     loaded    activating auto-restart       Ms Allis Auth Service
  msjarvis-69dgm-9000.service                                                               loaded    inactive   dead               MsJarvis Port 9000 → 69-DGM Bridge
  msjarvis-69dgm-9002-chat.service                                                          loaded    active     running            MsJarvis Port 9002 → 69-DGM Chat Wrapper
  msjarvis-69dgm-orchestrator.service                                                       loaded    inactive   dead               MsJarvis 69-DGM Orchestrator (port 8300)
  msjarvis-chat.service                                                                     loaded    active     running            Ms. Jarvis Production Chat Service (port 8018)
  msjarvis-interaction-logger.service                                                       loaded    activating auto-restart       MS Jarvis Interaction Logger
  msjarvis-production-chat.service                                                          loaded    active     running            Ms. Allis Production Chat Pipeline (port 8018)
  msjarvis.service                                                                          loaded    activating start-pre    start Ms. Jarvis Rebuild Stack
  polkit.service                                                                            loaded    active     running            Authorization Manager
  postgresql@16-msjarvis.service                                                            loaded    inactive   dead               PostgreSQL Cluster 16-msjarvis
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ 
# Investigative Audit and Action Plan for Production Stability

## Scope

This audit evaluates four unresolved areas in the MountainShares / Ms. Allis architecture: Layer 2 suppression thresholds, Sensitive/BSA unification, direct sum sovereign subspaces, and H_commons aggregation. The goal is to convert each area from design exposure or theoretical specification into a production-stable, testable, governable subsystem with explicit exit criteria.[cite:19][cite:21][cite:22]

The current system already has a strong production base. Hilbert People Space (`hp`) is built and operational as a 13-table Postgres schema in `hilbert_people`, served by `jarvis-hilbert-state`, with the disclosure-assertion gateway verified end-to-end and persisting every verdict to `hp.appearance_assertion`.[cite:19] The temporal Hilbert axis (`jarvis-hilbert-time`) is also built and operational as a Redis-backed FastAPI service that powers recency-weighted retrieval in the semantic gateway.[cite:20]

## Executive Findings

Two of the four target areas are **running-stack governance and safety gaps**, not research problems. Layer 2 suppression thresholds and Sensitive/BSA unification sit directly adjacent to already-running production services and must be closed before aggregate metrics or person-sensitivity logic can be treated as production-complete.[cite:19]

The other two areas are **not yet implementation projects** in the usual engineering sense. Direct sum sovereign subspaces and H_commons aggregation are explicitly documented as formal or theoretical specifications with unresolved mathematical, cryptographic, and governance problems; they should be managed as staged research-to-engineering programs, not as ordinary backlog tickets.[cite:21][cite:22]

## Current-State Classification

| Area | Current status | Core blocker | Production interpretation |
|---|---|---|---|
| Layer 2 suppression thresholds | Open design gap in running stack [cite:19] | No minimum-count / small-cell suppression policy defined [cite:19] | Must close before any aggregate metrics surface |
| Sensitive/BSA unification | Open design gap in running stack [cite:19] | Parallel protection regimes for the same vulnerable population [cite:19] | Must unify policy and enforcement before claiming stable person-safety rules |
| Direct sum sovereign subspaces | Formal specification, implementation pending [cite:21] | No proven projection-key construction, no orthogonality proof, no interface morphism [cite:21] | Research program, not deployable yet |
| H_commons aggregation | Theoretical specification, implementation pending [cite:22] | No constructed projection operator, unresolved k-governance, no integration function [cite:22] | Research program, not deployable yet |

## Investigative Assessment

### 1. Layer 2 suppression thresholds

Chapter 48 identifies rural re-identification as a live risk: county-level usage, service category, repeat engagement, and accessibility preferences can resolve to a single person in small West Virginia populations unless small-cell suppression is enforced.[cite:19] This is not a speculative privacy concern; it is the direct production consequence of exposing aggregate views before threshold logic, suppression windows, and review rules are defined.[cite:19]

The engineering problem is straightforward compared with the other gaps. The missing work is not core storage or service architecture, but a production policy stack: a sensitivity taxonomy, metric-release rules, suppression thresholds by topic and geography, audit logging, and regression tests that prove forbidden low-count slices never surface.[cite:19]

**Action plan:**
- Define a release policy for aggregate metrics with hard minimum thresholds, beginning with a global default and stricter thresholds for health, financial hardship, legal, housing, and benefits-related categories.[cite:19][cite:22]
- Classify all current and planned Layer 2 metrics into sensitivity tiers and allowed breakdown dimensions.
- Add a metrics-policy module that evaluates every aggregate query before response serialization; suppression must occur server-side, not in the UI.
- Persist suppression events as auditable records without exposing the suppressed cell contents, following the same logic used for disclosure assertions in `hp.appearance_assertion`.[cite:19]
- Add negative tests for single-county rare-service cases, repeated-engagement slices, and combinations of accessibility preference plus service type.

**Exit criteria for production stability:**
- No aggregate endpoint can return a row where distinct-subject count is below policy minimum.
- Sensitive categories enforce stricter thresholds automatically.
- Suppression decisions are logged and reviewable.
- Test suite includes adversarial small-population cases and passes in CI.
- Governance document defines who can change thresholds and under what approval path.[cite:19][cite:22]

### 2. Sensitive/BSA unification

Chapter 48 states that the “sensitive person” category overlaps exactly with Benefits-Sensitive Accounts and recommends unifying them under the same protected-default rather than allowing parallel systems to evolve separately.[cite:19] Leaving these as parallel regimes creates the classic production failure mode in safety systems: one path classifies a person as protected while another path does not, producing inconsistent disclosure, logging, or escalation behavior.[cite:19]

This is primarily a policy-to-schema alignment problem. The architecture already has a constitutional/disclosure layer and a working assertion gateway, so the shortest path to production stability is to define one canonical “protected subject” model and make both H_people and BSA logic consume that same model.[cite:19]

**Action plan:**
- Create a unified protected-subject taxonomy covering minors, victims, witnesses, benefits recipients, medical/legal/housing subjects, and unknown-status people.[cite:19]
- Define precedence rules: sensitive status overrides public curiosity; unknown defaults to protected; public role remains context-limited.[cite:19]
- Normalize the enforcement path so H_people disclosure checks and BSA checks resolve through the same policy function or assertion vocabulary.
- Add migration logic for any existing BSA flags or sensitivity markers into a canonical policy table or service.
- Build cross-system tests proving that the same subject receives the same outcome in H_people disclosure, benefits workflows, and reporting views.

**Exit criteria for production stability:**
- One canonical protected-subject policy exists.
- H_people and BSA consume the same sensitivity decision path.
- Disclosure, redaction, and escalation outcomes match across systems for identical subject facts.
- Audit logs show a single reason vocabulary for protected-status decisions.

### 3. Direct sum sovereign subspaces

Chapter 50 is explicit that this is a formal specification with implementation pending, and it names four open problems: formal orthogonality proof, key derivation specification, interface morphism construction, and constitutional completeness.[cite:21] The proposed implementation uses a per-user projection transform \(\hat{e}_{u_i} = R_{u_i} \cdot e\), where \(R_{u_i}\) is derived from a participant-held secret, but the function `ProjectionKey(commitment_salt)` is still unnamed in concrete cryptographic terms and has no validated implementation.[cite:21]

Because this subsystem changes the privacy guarantee from governance-enforced to geometry-enforced, it cannot be treated as production-ready on intuition alone. The correct production path is a staged program that separates theorem risk, cryptographic construction risk, system-integration risk, and governance risk.[cite:21]

**Action plan:**
- Split the work into four tracks: mathematics, cryptography, systems prototyping, and constitutional/governance drafting.[cite:21]
- Mathematics track: produce a formal proof target for the orthogonality and metric-preservation properties required for retrieval within a user subspace.[cite:21]
- Cryptography track: specify `ProjectionKey(commitment_salt)` with deterministic derivation of full-rank orthogonal matrices, performance targets at the production embedding dimension, and a security analysis aligned with the post-quantum framework from Chapter 42.[cite:21]
- Systems track: implement a prototype transform layer at embedding-ingest and query time, using an isolated experimental environment rather than the production memory stack.[cite:21]
- Governance track: draft the constitutional rule that cross-user search is prohibited by founding intent and cannot be enabled by ordinary product or engineering choice.[cite:21]

**Required phase gates before production consideration:**
1. **Research gate:** written proof sketch, explicit assumptions, attack model, and unresolved questions.
2. **Prototype gate:** measurable within-user retrieval quality after transformation, plus empirical failure of cross-user search.
3. **Security gate:** external review of key derivation and inversion resistance.
4. **Governance gate:** constitutional language approved and version-controlled.
5. **Pilot gate:** opt-in, non-critical memory pilot with rollback.

**Exit criteria for production stability:**
- Proven or externally reviewed projection-key construction.
- Prototype demonstrates acceptable retrieval fidelity within user space.
- Cross-user comparability is empirically defeated under defined adversary tests.
- Governance prohibition on cross-user search is formally adopted.[cite:21]

### 4. H_commons aggregation

Chapter 51 proposes `H_commons` as a one-directional projection of the direct sum aggregate into a shared observational space, with k-anonymity thresholds controlling visibility of community clusters.[cite:22] The chapter is equally explicit that the projection operator \(\Pi\), the governance of \(k\), the civic-reasoning integration function, and any stronger differential-privacy formulation are open problems.[cite:22]

This means H_commons is not blocked by coding effort alone; it is blocked by the absence of the core mathematical and governance contract that would make any implementation trustworthy.[cite:22] The correct move is to design it as an aggregation service only after direct-sum primitives and threshold governance are settled enough to support it.[cite:21][cite:22]

**Action plan:**
- Treat H_commons as dependent on the direct-sum program; do not start production implementation until sovereign-subspace prototype results exist.[cite:21][cite:22]
- Define a minimal viable aggregation operator candidate set, such as random projection or locality-sensitive approaches, and test them against the three required properties: identity destruction, semantic preservation, and one-directionality.[cite:22]
- Build governance first for k-thresholds: who sets them, how sensitive topics are classified, and how long sub-threshold clusters remain buffered before discard.[cite:22]
- Prototype the aggregation container with strict network isolation, no key access, and no origin-subspace logging, exactly as the chapter specifies.[cite:22]
- Delay any production coupling to civic reasoning until an explicit integration function can be evaluated against false positives, under-reporting, and conflict cases between community concern and structured civic data.[cite:22]

**Exit criteria for production stability:**
- Candidate projection operator evaluated against the three chapter-defined properties.
- K-threshold governance ratified and testable.
- Aggregation container proves no key access, no return path, and no origin logging.
- Suppression behavior is fully auditable without identity exposure.
- Civic reasoning integration has measurable rules for weighting cluster density, temporal decay, and contradiction handling.[cite:22]

## Delivery Sequence

A safe production roadmap should not attempt all four targets at once. The order should follow dependency and risk.

| Phase | Target | Why first |
|---|---|---|
| Phase 1 | Layer 2 suppression thresholds | Immediate privacy exposure in already-running stack [cite:19] |
| Phase 2 | Sensitive/BSA unification | Immediate safety and consistency exposure in already-running stack [cite:19] |
| Phase 3 | Direct sum sovereign subspace prototype | Foundational dependency for any non-surveillance cross-user memory future [cite:21] |
| Phase 4 | H_commons research prototype | Depends on direct-sum primitives and governance choices [cite:21][cite:22] |

## 90-Day Program

### Days 1–30
- Freeze any release of Layer 2 aggregate metrics until suppression policy is implemented.[cite:19]
- Draft a sensitivity taxonomy and threshold matrix.
- Draft a canonical protected-subject policy for H_people and BSA.
- Add audit requirements and test cases to CI for both policy areas.

### Days 31–60
- Implement server-side suppression enforcement and suppression-event logging.
- Implement unified protected-subject policy path and migration plan.
- Produce a research memo for direct-sum construction choices, attack model, and prototype design.
- Draft constitutional language for cross-user search prohibition and k-threshold governance.[cite:21][cite:22]

### Days 61–90
- Complete CI coverage for suppression and protected-subject behavior.
- Stand up an isolated prototype for per-user projection transforms.
- Run retrieval-quality and adversary tests on prototype memory data.
- Decide whether H_commons can move from theory to prototype based on direct-sum results.

## Decision Standard

The right standard is not “can this be coded,” but “can this be defended.” Layer 2 suppression thresholds and Sensitive/BSA unification should be treated as production hardening work on top of already operational services.[cite:19] Direct sum sovereign subspaces and H_commons should be treated as research programs that must clear mathematical, cryptographic, systems, and constitutional gates before they are allowed anywhere near production claims.[cite:21][cite:22]

A production-stable claim is justified only when each subsystem has: a formal policy contract, auditable enforcement, adversarial tests, operational rollback, and governance language aligned with the implementation. The running stack is close on the first two gaps. The last two require disciplined reduction from thesis to prototype to reviewed implementation.[cite:19][cite:21][cite:22]jarvis-backups/20260103_020002/services/mesh_emotion_map.json
./backup_filename_index.txt:2518:mesh_emotion_map.json|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_emotion_map.json
./backup_filename_index.txt:3387:jarvis_authentic_persona.txt|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/jarvis_authentic_persona.txt
./backup_filename_index.txt:3388:jarvis_authentic_persona.txt|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/jarvis_authentic_persona.txt
./backup_filename_index.txt:3389:jarvis_authentic_persona.txt|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/jarvis_authentic_persona.txt
./backup_filename_index.txt:3390:jarvis_authentic_persona.txt|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/jarvis_authentic_persona.txt
./backup_filename_index.txt:3391:jarvis_authentic_persona.txt|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/jarvis_authentic_persona.txt
./backup_filename_index.txt:3392:jarvis_authentic_persona.txt|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/jarvis_authentic_persona.txt
./backup_filename_index.txt:3393:jarvis_authentic_persona.txt|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/jarvis_authentic_persona.txt
./backup_filename_index.txt:3681:mesh_tag_topk.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_tag_topk.sh
./backup_filename_index.txt:3682:mesh_tag_topk.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_tag_topk.sh
./backup_filename_index.txt:3683:mesh_tag_topk.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_tag_topk.sh
./backup_filename_index.txt:3684:mesh_tag_topk.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_tag_topk.sh
./backup_filename_index.txt:3685:mesh_tag_topk.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_tag_topk.sh
./backup_filename_index.txt:3686:mesh_tag_topk.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_tag_topk.sh
./backup_filename_index.txt:3687:mesh_tag_topk.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_tag_topk.sh
./backup_filename_index.txt:4115:memory_dgm_engine.py.backup_vocabulary_cleanup|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/memory_dgm_engine.py.backup_vocabulary_cleanup
./backup_filename_index.txt:4116:memory_dgm_engine.py.backup_vocabulary_cleanup|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/memory_dgm_engine.py.backup_vocabulary_cleanup
./backup_filename_index.txt:4117:memory_dgm_engine.py.backup_vocabulary_cleanup|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/memory_dgm_engine.py.backup_vocabulary_cleanup
./backup_filename_index.txt:4118:memory_dgm_engine.py.backup_vocabulary_cleanup|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/memory_dgm_engine.py.backup_vocabulary_cleanup
./backup_filename_index.txt:4119:memory_dgm_engine.py.backup_vocabulary_cleanup|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/memory_dgm_engine.py.backup_vocabulary_cleanup
./backup_filename_index.txt:4120:memory_dgm_engine.py.backup_vocabulary_cleanup|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/memory_dgm_engine.py.backup_vocabulary_cleanup
./backup_filename_index.txt:4121:memory_dgm_engine.py.backup_vocabulary_cleanup|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/memory_dgm_engine.py.backup_vocabulary_cleanup
./backup_filename_index.txt:4129:mesh_explore_chain.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_explore_chain.sh
./backup_filename_index.txt:4130:mesh_explore_chain.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_explore_chain.sh
./backup_filename_index.txt:4131:mesh_explore_chain.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_explore_chain.sh
./backup_filename_index.txt:4132:mesh_explore_chain.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_explore_chain.sh
./backup_filename_index.txt:4133:mesh_explore_chain.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_explore_chain.sh
./backup_filename_index.txt:4134:mesh_explore_chain.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_explore_chain.sh
./backup_filename_index.txt:4135:mesh_explore_chain.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_explore_chain.sh
./backup_filename_index.txt:4199:bridge_ms_jarvis_main_gateway_to_user_auth_service.log|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/bridge_ms_jarvis_main_gateway_to_user_auth_service.log
./backup_filename_index.txt:4200:bridge_ms_jarvis_main_gateway_to_user_auth_service.log|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/bridge_ms_jarvis_main_gateway_to_user_auth_service.log
./backup_filename_index.txt:4201:bridge_ms_jarvis_main_gateway_to_user_auth_service.log|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/bridge_ms_jarvis_main_gateway_to_user_auth_service.log
./backup_filename_index.txt:4202:bridge_ms_jarvis_main_gateway_to_user_auth_service.log|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/bridge_ms_jarvis_main_gateway_to_user_auth_service.log
./backup_filename_index.txt:4203:bridge_ms_jarvis_main_gateway_to_user_auth_service.log|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/bridge_ms_jarvis_main_gateway_to_user_auth_service.log
./backup_filename_index.txt:4204:bridge_ms_jarvis_main_gateway_to_user_auth_service.log|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/bridge_ms_jarvis_main_gateway_to_user_auth_service.log
./backup_filename_index.txt:4205:bridge_ms_jarvis_main_gateway_to_user_auth_service.log|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/bridge_ms_jarvis_main_gateway_to_user_auth_service.log
./backup_filename_index.txt:4955:egeria_web_ui_plain_authentic.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/egeria_web_ui_plain_authentic.py
./backup_filename_index.txt:4956:egeria_web_ui_plain_authentic.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/egeria_web_ui_plain_authentic.py
./backup_filename_index.txt:4957:egeria_web_ui_plain_authentic.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/egeria_web_ui_plain_authentic.py
./backup_filename_index.txt:4958:egeria_web_ui_plain_authentic.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/egeria_web_ui_plain_authentic.py
./backup_filename_index.txt:4959:egeria_web_ui_plain_authentic.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/egeria_web_ui_plain_authentic.py
./backup_filename_index.txt:4960:egeria_web_ui_plain_authentic.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/egeria_web_ui_plain_authentic.py
./backup_filename_index.txt:4961:egeria_web_ui_plain_authentic.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/egeria_web_ui_plain_authentic.py
./backup_filename_index.txt:4976:mesh_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_probe.sh
./backup_filename_index.txt:4977:mesh_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_probe.sh
./backup_filename_index.txt:4978:mesh_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_probe.sh
./backup_filename_index.txt:4979:mesh_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_probe.sh
./backup_filename_index.txt:4980:mesh_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_probe.sh
./backup_filename_index.txt:4981:mesh_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_probe.sh
./backup_filename_index.txt:4982:mesh_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_probe.sh
./backup_filename_index.txt:5844:mega_deep_archive_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mega_deep_archive_search.sh
./backup_filename_index.txt:5845:mega_deep_archive_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/services/mega_deep_archive_search.sh
./backup_filename_index.txt:5846:mega_deep_archive_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mega_deep_archive_search.sh
./backup_filename_index.txt:5847:mega_deep_archive_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mega_deep_archive_search.sh
./backup_filename_index.txt:5848:mega_deep_archive_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/services/mega_deep_archive_search.sh
./backup_filename_index.txt:5849:mega_deep_archive_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/services/mega_deep_archive_search.sh
./backup_filename_index.txt:5850:mega_deep_archive_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/services/mega_deep_archive_search.sh
./backup_filename_index.txt:5851:mega_deep_archive_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/services/mega_deep_archive_search.sh
./backup_filename_index.txt:5852:mega_deep_archive_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mega_deep_archive_search.sh
./backup_filename_index.txt:5853:mega_deep_archive_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/services/mega_deep_archive_search.sh
./backup_filename_index.txt:5854:mega_deep_archive_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mega_deep_archive_search.sh
./backup_filename_index.txt:5855:mega_deep_archive_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mega_deep_archive_search.sh
./backup_filename_index.txt:5856:mega_deep_archive_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mega_deep_archive_search.sh
./backup_filename_index.txt:5857:mega_deep_archive_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/services/mega_deep_archive_search.sh
./backup_filename_index.txt:5949:bridge_ms_jarvis_main_gateway_to_ms_jarvis_authentic_multi_llm.log|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/bridge_ms_jarvis_main_gateway_to_ms_jarvis_authentic_multi_llm.log
./backup_filename_index.txt:5950:bridge_ms_jarvis_main_gateway_to_ms_jarvis_authentic_multi_llm.log|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/bridge_ms_jarvis_main_gateway_to_ms_jarvis_authentic_multi_llm.log
./backup_filename_index.txt:5951:bridge_ms_jarvis_main_gateway_to_ms_jarvis_authentic_multi_llm.log|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/bridge_ms_jarvis_main_gateway_to_ms_jarvis_authentic_multi_llm.log
./backup_filename_index.txt:5952:bridge_ms_jarvis_main_gateway_to_ms_jarvis_authentic_multi_llm.log|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/bridge_ms_jarvis_main_gateway_to_ms_jarvis_authentic_multi_llm.log
./backup_filename_index.txt:5953:bridge_ms_jarvis_main_gateway_to_ms_jarvis_authentic_multi_llm.log|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/bridge_ms_jarvis_main_gateway_to_ms_jarvis_authentic_multi_llm.log
./backup_filename_index.txt:5954:bridge_ms_jarvis_main_gateway_to_ms_jarvis_authentic_multi_llm.log|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/bridge_ms_jarvis_main_gateway_to_ms_jarvis_authentic_multi_llm.log
./backup_filename_index.txt:5955:bridge_ms_jarvis_main_gateway_to_ms_jarvis_authentic_multi_llm.log|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/bridge_ms_jarvis_main_gateway_to_ms_jarvis_authentic_multi_llm.log
./backup_filename_index.txt:6047:mesh_social_graph.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_social_graph.sh
./backup_filename_index.txt:6048:mesh_social_graph.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_social_graph.sh
./backup_filename_index.txt:6049:mesh_social_graph.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_social_graph.sh
./backup_filename_index.txt:6050:mesh_social_graph.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_social_graph.sh
./backup_filename_index.txt:6051:mesh_social_graph.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_social_graph.sh
./backup_filename_index.txt:6052:mesh_social_graph.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_social_graph.sh
./backup_filename_index.txt:6053:mesh_social_graph.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_social_graph.sh
./backup_filename_index.txt:6873:bridge_ms_jarvis_main_gateway_to_fix_judge_authentic.log|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/bridge_ms_jarvis_main_gateway_to_fix_judge_authentic.log
./backup_filename_index.txt:6874:bridge_ms_jarvis_main_gateway_to_fix_judge_authentic.log|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/bridge_ms_jarvis_main_gateway_to_fix_judge_authentic.log
./backup_filename_index.txt:6875:bridge_ms_jarvis_main_gateway_to_fix_judge_authentic.log|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/bridge_ms_jarvis_main_gateway_to_fix_judge_authentic.log
./backup_filename_index.txt:6876:bridge_ms_jarvis_main_gateway_to_fix_judge_authentic.log|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/bridge_ms_jarvis_main_gateway_to_fix_judge_authentic.log
./backup_filename_index.txt:6877:bridge_ms_jarvis_main_gateway_to_fix_judge_authentic.log|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/bridge_ms_jarvis_main_gateway_to_fix_judge_authentic.log
./backup_filename_index.txt:6878:bridge_ms_jarvis_main_gateway_to_fix_judge_authentic.log|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/bridge_ms_jarvis_main_gateway_to_fix_judge_authentic.log
./backup_filename_index.txt:6879:bridge_ms_jarvis_main_gateway_to_fix_judge_authentic.log|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/bridge_ms_jarvis_main_gateway_to_fix_judge_authentic.log
./backup_filename_index.txt:7608:bridge_ms_jarvis_main_gateway_to_oauth2_callback.log|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/bridge_ms_jarvis_main_gateway_to_oauth2_callback.log
./backup_filename_index.txt:7609:bridge_ms_jarvis_main_gateway_to_oauth2_callback.log|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/bridge_ms_jarvis_main_gateway_to_oauth2_callback.log
./backup_filename_index.txt:7610:bridge_ms_jarvis_main_gateway_to_oauth2_callback.log|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/bridge_ms_jarvis_main_gateway_to_oauth2_callback.log
./backup_filename_index.txt:7611:bridge_ms_jarvis_main_gateway_to_oauth2_callback.log|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/bridge_ms_jarvis_main_gateway_to_oauth2_callback.log
./backup_filename_index.txt:7612:bridge_ms_jarvis_main_gateway_to_oauth2_callback.log|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/bridge_ms_jarvis_main_gateway_to_oauth2_callback.log
./backup_filename_index.txt:7613:bridge_ms_jarvis_main_gateway_to_oauth2_callback.log|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/bridge_ms_jarvis_main_gateway_to_oauth2_callback.log
./backup_filename_index.txt:7614:bridge_ms_jarvis_main_gateway_to_oauth2_callback.log|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/bridge_ms_jarvis_main_gateway_to_oauth2_callback.log
./backup_filename_index.txt:7804:mesh_trend_detection.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_trend_detection.sh
./backup_filename_index.txt:7805:mesh_trend_detection.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_trend_detection.sh
./backup_filename_index.txt:7806:mesh_trend_detection.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_trend_detection.sh
./backup_filename_index.txt:7807:mesh_trend_detection.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_trend_detection.sh
./backup_filename_index.txt:7808:mesh_trend_detection.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_trend_detection.sh
./backup_filename_index.txt:7809:mesh_trend_detection.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_trend_detection.sh
./backup_filename_index.txt:7810:mesh_trend_detection.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_trend_detection.sh
./backup_filename_index.txt:8196:memory_dgm_engine.log|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/memory_dgm_engine.log
./backup_filename_index.txt:8197:memory_dgm_engine.log|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/memory_dgm_engine.log
./backup_filename_index.txt:8198:memory_dgm_engine.log|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/memory_dgm_engine.log
./backup_filename_index.txt:8199:memory_dgm_engine.log|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/memory_dgm_engine.log
./backup_filename_index.txt:8200:memory_dgm_engine.log|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/memory_dgm_engine.log
./backup_filename_index.txt:8201:memory_dgm_engine.log|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/memory_dgm_engine.log
./backup_filename_index.txt:8202:memory_dgm_engine.log|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/memory_dgm_engine.log
./backup_filename_index.txt:8945:mesh_topn_context.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_topn_context.sh
./backup_filename_index.txt:8946:mesh_topn_context.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_topn_context.sh
./backup_filename_index.txt:8947:mesh_topn_context.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_topn_context.sh
./backup_filename_index.txt:8948:mesh_topn_context.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_topn_context.sh
./backup_filename_index.txt:8949:mesh_topn_context.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_topn_context.sh
./backup_filename_index.txt:8950:mesh_topn_context.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_topn_context.sh
./backup_filename_index.txt:8951:mesh_topn_context.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_topn_context.sh
./backup_filename_index.txt:9652:oauth2_callback.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/oauth2_callback.py
./backup_filename_index.txt:9653:oauth2_callback.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/oauth2_callback.py
./backup_filename_index.txt:9654:oauth2_callback.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/oauth2_callback.py
./backup_filename_index.txt:9655:oauth2_callback.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/oauth2_callback.py
./backup_filename_index.txt:9656:oauth2_callback.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/oauth2_callback.py
./backup_filename_index.txt:9657:oauth2_callback.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/oauth2_callback.py
./backup_filename_index.txt:9658:oauth2_callback.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/oauth2_callback.py
./backup_filename_index.txt:10646:user_auth_service.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/user_auth_service.py
./backup_filename_index.txt:10647:user_auth_service.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/user_auth_service.py
./backup_filename_index.txt:10648:user_auth_service.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/user_auth_service.py
./backup_filename_index.txt:10649:user_auth_service.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/user_auth_service.py
./backup_filename_index.txt:10650:user_auth_service.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/user_auth_service.py
./backup_filename_index.txt:10651:user_auth_service.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/user_auth_service.py
./backup_filename_index.txt:10652:user_auth_service.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/user_auth_service.py
./backup_filename_index.txt:11997:metrics_service.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/metrics_service.py
./backup_filename_index.txt:11998:metrics_service.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/metrics_service.py
./backup_filename_index.txt:11999:metrics_service.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/services/metrics_service.py
./backup_filename_index.txt:12000:metrics_service.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/metrics_service.py
./backup_filename_index.txt:12001:metrics_service.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/services/metrics_service.py
./backup_filename_index.txt:12002:metrics_service.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/services/metrics_service.py
./backup_filename_index.txt:12003:metrics_service.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/metrics_service.py
./backup_filename_index.txt:12004:metrics_service.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/services/metrics_service.py
./backup_filename_index.txt:12005:metrics_service.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/metrics_service.py
./backup_filename_index.txt:12006:metrics_service.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/services/metrics_service.py
./backup_filename_index.txt:12007:metrics_service.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/services/metrics_service.py
./backup_filename_index.txt:12008:metrics_service.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/metrics_service.py
./backup_filename_index.txt:12009:metrics_service.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/metrics_service.py
./backup_filename_index.txt:12010:metrics_service.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/services/metrics_service.py
./backup_filename_index.txt:12228:fix_judge_authentic.py.backup_vocabulary_cleanup|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/fix_judge_authentic.py.backup_vocabulary_cleanup
./backup_filename_index.txt:12229:fix_judge_authentic.py.backup_vocabulary_cleanup|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/fix_judge_authentic.py.backup_vocabulary_cleanup
./backup_filename_index.txt:12230:fix_judge_authentic.py.backup_vocabulary_cleanup|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/fix_judge_authentic.py.backup_vocabulary_cleanup
./backup_filename_index.txt:12231:fix_judge_authentic.py.backup_vocabulary_cleanup|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/fix_judge_authentic.py.backup_vocabulary_cleanup
./backup_filename_index.txt:12232:fix_judge_authentic.py.backup_vocabulary_cleanup|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/fix_judge_authentic.py.backup_vocabulary_cleanup
./backup_filename_index.txt:12233:fix_judge_authentic.py.backup_vocabulary_cleanup|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/fix_judge_authentic.py.backup_vocabulary_cleanup
./backup_filename_index.txt:12234:fix_judge_authentic.py.backup_vocabulary_cleanup|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/fix_judge_authentic.py.backup_vocabulary_cleanup
./backup_filename_index.txt:12382:fix_judge_authentic.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/fix_judge_authentic.py
./backup_filename_index.txt:12383:fix_judge_authentic.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/fix_judge_authentic.py
./backup_filename_index.txt:12384:fix_judge_authentic.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/fix_judge_authentic.py
./backup_filename_index.txt:12385:fix_judge_authentic.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/fix_judge_authentic.py
./backup_filename_index.txt:12386:fix_judge_authentic.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/fix_judge_authentic.py
./backup_filename_index.txt:12387:fix_judge_authentic.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/fix_judge_authentic.py
./backup_filename_index.txt:12388:fix_judge_authentic.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/fix_judge_authentic.py
./backup_filename_index.txt:12494:mamma_kidd_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/services/mamma_kidd_auth.py
./backup_filename_index.txt:12495:mamma_kidd_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mamma_kidd_auth.py
./backup_filename_index.txt:12496:mamma_kidd_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/services/mamma_kidd_auth.py
./backup_filename_index.txt:12497:mamma_kidd_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/services/mamma_kidd_auth.py
./backup_filename_index.txt:12498:mamma_kidd_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mamma_kidd_auth.py
./backup_filename_index.txt:12499:mamma_kidd_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mamma_kidd_auth.py
./backup_filename_index.txt:12500:mamma_kidd_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/services/mamma_kidd_auth.py
./backup_filename_index.txt:12501:mamma_kidd_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/services/mamma_kidd_auth.py
./backup_filename_index.txt:12502:mamma_kidd_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/services/mamma_kidd_auth.py
./backup_filename_index.txt:12503:mamma_kidd_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mamma_kidd_auth.py
./backup_filename_index.txt:12504:mamma_kidd_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mamma_kidd_auth.py
./backup_filename_index.txt:12505:mamma_kidd_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mamma_kidd_auth.py
./backup_filename_index.txt:12506:mamma_kidd_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/services/mamma_kidd_auth.py
./backup_filename_index.txt:12507:mamma_kidd_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mamma_kidd_auth.py
./backup_filename_index.txt:13124:mesh_dream_summary.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_dream_summary.sh
./backup_filename_index.txt:13125:mesh_dream_summary.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_dream_summary.sh
./backup_filename_index.txt:13126:mesh_dream_summary.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_dream_summary.sh
./backup_filename_index.txt:13127:mesh_dream_summary.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_dream_summary.sh
./backup_filename_index.txt:13128:mesh_dream_summary.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_dream_summary.sh
./backup_filename_index.txt:13129:mesh_dream_summary.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_dream_summary.sh
./backup_filename_index.txt:13130:mesh_dream_summary.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_dream_summary.sh
./backup_filename_index.txt:13201:cloudflare_auth_helper.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/cloudflare_auth_helper.sh
./backup_filename_index.txt:13202:cloudflare_auth_helper.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/services/cloudflare_auth_helper.sh
./backup_filename_index.txt:13203:cloudflare_auth_helper.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/cloudflare_auth_helper.sh
./backup_filename_index.txt:13204:cloudflare_auth_helper.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/cloudflare_auth_helper.sh
./backup_filename_index.txt:13205:cloudflare_auth_helper.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/cloudflare_auth_helper.sh
./backup_filename_index.txt:13206:cloudflare_auth_helper.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/cloudflare_auth_helper.sh
./backup_filename_index.txt:13207:cloudflare_auth_helper.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/cloudflare_auth_helper.sh
./backup_filename_index.txt:13208:cloudflare_auth_helper.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/services/cloudflare_auth_helper.sh
./backup_filename_index.txt:13209:cloudflare_auth_helper.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/services/cloudflare_auth_helper.sh
./backup_filename_index.txt:13210:cloudflare_auth_helper.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/services/cloudflare_auth_helper.sh
./backup_filename_index.txt:13211:cloudflare_auth_helper.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/services/cloudflare_auth_helper.sh
./backup_filename_index.txt:13212:cloudflare_auth_helper.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/services/cloudflare_auth_helper.sh
./backup_filename_index.txt:13213:cloudflare_auth_helper.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/services/cloudflare_auth_helper.sh
./backup_filename_index.txt:13214:cloudflare_auth_helper.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/cloudflare_auth_helper.sh
./backup_filename_index.txt:14069:mesh_coordinator_interface.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_coordinator_interface.py
./backup_filename_index.txt:14070:mesh_coordinator_interface.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_coordinator_interface.py
./backup_filename_index.txt:14071:mesh_coordinator_interface.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_coordinator_interface.py
./backup_filename_index.txt:14072:mesh_coordinator_interface.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_coordinator_interface.py
./backup_filename_index.txt:14073:mesh_coordinator_interface.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_coordinator_interface.py
./backup_filename_index.txt:14074:mesh_coordinator_interface.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_coordinator_interface.py
./backup_filename_index.txt:14075:mesh_coordinator_interface.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_coordinator_interface.py
./backup_filename_index.txt:14083:memory_engine.log|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/memory_engine.log
./backup_filename_index.txt:14084:memory_engine.log|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/memory_engine.log
./backup_filename_index.txt:14085:memory_engine.log|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/memory_engine.log
./backup_filename_index.txt:14086:memory_engine.log|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/memory_engine.log
./backup_filename_index.txt:14087:memory_engine.log|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/memory_engine.log
./backup_filename_index.txt:14088:memory_engine.log|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/memory_engine.log
./backup_filename_index.txt:14089:memory_engine.log|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/memory_engine.log
./backup_filename_index.txt:14230:mesh_memory_dashboard.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_memory_dashboard.sh
./backup_filename_index.txt:14231:mesh_memory_dashboard.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_memory_dashboard.sh
./backup_filename_index.txt:14232:mesh_memory_dashboard.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_memory_dashboard.sh
./backup_filename_index.txt:14233:mesh_memory_dashboard.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_memory_dashboard.sh
./backup_filename_index.txt:14234:mesh_memory_dashboard.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_memory_dashboard.sh
./backup_filename_index.txt:14235:mesh_memory_dashboard.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_memory_dashboard.sh
./backup_filename_index.txt:14236:mesh_memory_dashboard.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_memory_dashboard.sh
./backup_filename_index.txt:14447:ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery
./backup_filename_index.txt:14448:ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery
./backup_filename_index.txt:14449:ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery
./backup_filename_index.txt:14450:ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery
./backup_filename_index.txt:14451:ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery
./backup_filename_index.txt:14452:ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery
./backup_filename_index.txt:14453:ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/ms_jarvis_authentic_multi_llm.py.pre_dynamic_discovery
./backup_filename_index.txt:15357:memory_dgm_gateway.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/memory_dgm_gateway.py
./backup_filename_index.txt:15358:memory_dgm_gateway.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/memory_dgm_gateway.py
./backup_filename_index.txt:15359:memory_dgm_gateway.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/memory_dgm_gateway.py
./backup_filename_index.txt:15360:memory_dgm_gateway.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/memory_dgm_gateway.py
./backup_filename_index.txt:15361:memory_dgm_gateway.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/memory_dgm_gateway.py
./backup_filename_index.txt:15362:memory_dgm_gateway.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/memory_dgm_gateway.py
./backup_filename_index.txt:15363:memory_dgm_gateway.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/memory_dgm_gateway.py
./backup_filename_index.txt:15966:method_tracker_decorator.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/method_tracker_decorator.py
./backup_filename_index.txt:15967:method_tracker_decorator.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/method_tracker_decorator.py
./backup_filename_index.txt:15968:method_tracker_decorator.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/method_tracker_decorator.py
./backup_filename_index.txt:15969:method_tracker_decorator.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/method_tracker_decorator.py
./backup_filename_index.txt:15970:method_tracker_decorator.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/method_tracker_decorator.py
./backup_filename_index.txt:15971:method_tracker_decorator.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/method_tracker_decorator.py
./backup_filename_index.txt:15972:method_tracker_decorator.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/method_tracker_decorator.py
./backup_filename_index.txt:16078:messenger_service_fixed.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/messenger_service_fixed.py
./backup_filename_index.txt:16079:messenger_service_fixed.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/messenger_service_fixed.py
./backup_filename_index.txt:16080:messenger_service_fixed.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/messenger_service_fixed.py
./backup_filename_index.txt:16081:messenger_service_fixed.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/messenger_service_fixed.py
./backup_filename_index.txt:16082:messenger_service_fixed.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/messenger_service_fixed.py
./backup_filename_index.txt:16083:messenger_service_fixed.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/messenger_service_fixed.py
./backup_filename_index.txt:16084:messenger_service_fixed.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/messenger_service_fixed.py
./backup_filename_index.txt:16113:oauth2_config.json|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/oauth2_config.json
./backup_filename_index.txt:16114:oauth2_config.json|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/oauth2_config.json
./backup_filename_index.txt:16115:oauth2_config.json|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/oauth2_config.json
./backup_filename_index.txt:16116:oauth2_config.json|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/oauth2_config.json
./backup_filename_index.txt:16117:oauth2_config.json|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/oauth2_config.json
./backup_filename_index.txt:16118:oauth2_config.json|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/oauth2_config.json
./backup_filename_index.txt:16119:oauth2_config.json|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/oauth2_config.json
./backup_filename_index.txt:16960:mesh_crossagent_memory_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_crossagent_memory_search.sh
./backup_filename_index.txt:16961:mesh_crossagent_memory_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_crossagent_memory_search.sh
./backup_filename_index.txt:16962:mesh_crossagent_memory_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_crossagent_memory_search.sh
./backup_filename_index.txt:16963:mesh_crossagent_memory_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_crossagent_memory_search.sh
./backup_filename_index.txt:16964:mesh_crossagent_memory_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_crossagent_memory_search.sh
./backup_filename_index.txt:16965:mesh_crossagent_memory_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_crossagent_memory_search.sh
./backup_filename_index.txt:16966:mesh_crossagent_memory_search.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_crossagent_memory_search.sh
./backup_filename_index.txt:17156:mesh_feed_back_insight.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_feed_back_insight.sh
./backup_filename_index.txt:17157:mesh_feed_back_insight.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_feed_back_insight.sh
./backup_filename_index.txt:17158:mesh_feed_back_insight.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_feed_back_insight.sh
./backup_filename_index.txt:17159:mesh_feed_back_insight.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_feed_back_insight.sh
./backup_filename_index.txt:17160:mesh_feed_back_insight.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_feed_back_insight.sh
./backup_filename_index.txt:17161:mesh_feed_back_insight.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_feed_back_insight.sh
./backup_filename_index.txt:17162:mesh_feed_back_insight.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_feed_back_insight.sh
./backup_filename_index.txt:17485:egeria_web_ui_plain_authentic.py.pre_dynamic_discovery|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/egeria_web_ui_plain_authentic.py.pre_dynamic_discovery
./backup_filename_index.txt:17486:egeria_web_ui_plain_authentic.py.pre_dynamic_discovery|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/egeria_web_ui_plain_authentic.py.pre_dynamic_discovery
./backup_filename_index.txt:17487:egeria_web_ui_plain_authentic.py.pre_dynamic_discovery|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/egeria_web_ui_plain_authentic.py.pre_dynamic_discovery
./backup_filename_index.txt:17488:egeria_web_ui_plain_authentic.py.pre_dynamic_discovery|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/egeria_web_ui_plain_authentic.py.pre_dynamic_discovery
./backup_filename_index.txt:17489:egeria_web_ui_plain_authentic.py.pre_dynamic_discovery|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/egeria_web_ui_plain_authentic.py.pre_dynamic_discovery
./backup_filename_index.txt:17490:egeria_web_ui_plain_authentic.py.pre_dynamic_discovery|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/egeria_web_ui_plain_authentic.py.pre_dynamic_discovery
./backup_filename_index.txt:17491:egeria_web_ui_plain_authentic.py.pre_dynamic_discovery|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/egeria_web_ui_plain_authentic.py.pre_dynamic_discovery
./backup_filename_index.txt:17520:bridge_ms_jarvis_main_gateway_to_egeria_web_ui_plain_authentic.log|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/bridge_ms_jarvis_main_gateway_to_egeria_web_ui_plain_authentic.log
./backup_filename_index.txt:17521:bridge_ms_jarvis_main_gateway_to_egeria_web_ui_plain_authentic.log|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/bridge_ms_jarvis_main_gateway_to_egeria_web_ui_plain_authentic.log
./backup_filename_index.txt:17522:bridge_ms_jarvis_main_gateway_to_egeria_web_ui_plain_authentic.log|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/bridge_ms_jarvis_main_gateway_to_egeria_web_ui_plain_authentic.log
./backup_filename_index.txt:17523:bridge_ms_jarvis_main_gateway_to_egeria_web_ui_plain_authentic.log|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/bridge_ms_jarvis_main_gateway_to_egeria_web_ui_plain_authentic.log
./backup_filename_index.txt:17524:bridge_ms_jarvis_main_gateway_to_egeria_web_ui_plain_authentic.log|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/bridge_ms_jarvis_main_gateway_to_egeria_web_ui_plain_authentic.log
./backup_filename_index.txt:17525:bridge_ms_jarvis_main_gateway_to_egeria_web_ui_plain_authentic.log|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/bridge_ms_jarvis_main_gateway_to_egeria_web_ui_plain_authentic.log
./backup_filename_index.txt:17526:bridge_ms_jarvis_main_gateway_to_egeria_web_ui_plain_authentic.log|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/bridge_ms_jarvis_main_gateway_to_egeria_web_ui_plain_authentic.log
./backup_filename_index.txt:17633:Dockerfile|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile
./backup_filename_index.txt:17654:Dockerfile|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile
./backup_filename_index.txt:17664:Dockerfile|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile
./backup_filename_index.txt:17674:Dockerfile|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile
./backup_filename_index.txt:17692:Dockerfile|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile
./backup_filename_index.txt:17705:Dockerfile|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile
./backup_filename_index.txt:17711:Dockerfile|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile
./backup_filename_index.txt:18087:oauth2_handler.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/oauth2_handler.py
./backup_filename_index.txt:18088:oauth2_handler.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/oauth2_handler.py
./backup_filename_index.txt:18089:oauth2_handler.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/oauth2_handler.py
./backup_filename_index.txt:18090:oauth2_handler.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/oauth2_handler.py
./backup_filename_index.txt:18091:oauth2_handler.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/oauth2_handler.py
./backup_filename_index.txt:18092:oauth2_handler.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/oauth2_handler.py
./backup_filename_index.txt:18093:oauth2_handler.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/oauth2_handler.py
./backup_filename_index.txt:18864:memory_manager.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/memory_manager.py
./backup_filename_index.txt:18865:memory_manager.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/memory_manager.py
./backup_filename_index.txt:18866:memory_manager.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/memory_manager.py
./backup_filename_index.txt:18867:memory_manager.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/memory_manager.py
./backup_filename_index.txt:18868:memory_manager.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/memory_manager.py
./backup_filename_index.txt:18869:memory_manager.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/memory_manager.py
./backup_filename_index.txt:18870:memory_manager.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/memory_manager.py
./backup_filename_index.txt:19529:mesh_interest_timeline.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_interest_timeline.sh
./backup_filename_index.txt:19530:mesh_interest_timeline.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_interest_timeline.sh
./backup_filename_index.txt:19531:mesh_interest_timeline.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_interest_timeline.sh
./backup_filename_index.txt:19532:mesh_interest_timeline.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_interest_timeline.sh
./backup_filename_index.txt:19533:mesh_interest_timeline.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_interest_timeline.sh
./backup_filename_index.txt:19534:mesh_interest_timeline.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_interest_timeline.sh
./backup_filename_index.txt:19535:mesh_interest_timeline.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_interest_timeline.sh
./backup_filename_index.txt:20768:ms_jarvis_authentic_multi_llm.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/ms_jarvis_authentic_multi_llm.py
./backup_filename_index.txt:20769:ms_jarvis_authentic_multi_llm.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/ms_jarvis_authentic_multi_llm.py
./backup_filename_index.txt:20770:ms_jarvis_authentic_multi_llm.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/ms_jarvis_authentic_multi_llm.py
./backup_filename_index.txt:20771:ms_jarvis_authentic_multi_llm.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/ms_jarvis_authentic_multi_llm.py
./backup_filename_index.txt:20772:ms_jarvis_authentic_multi_llm.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/ms_jarvis_authentic_multi_llm.py
./backup_filename_index.txt:20773:ms_jarvis_authentic_multi_llm.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/ms_jarvis_authentic_multi_llm.py
./backup_filename_index.txt:20774:ms_jarvis_authentic_multi_llm.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/ms_jarvis_authentic_multi_llm.py
./backup_filename_index.txt:21111:mesh_cohort_selfsum.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_cohort_selfsum.sh
./backup_filename_index.txt:21112:mesh_cohort_selfsum.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_cohort_selfsum.sh
./backup_filename_index.txt:21113:mesh_cohort_selfsum.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_cohort_selfsum.sh
./backup_filename_index.txt:21114:mesh_cohort_selfsum.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_cohort_selfsum.sh
./backup_filename_index.txt:21115:mesh_cohort_selfsum.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_cohort_selfsum.sh
./backup_filename_index.txt:21116:mesh_cohort_selfsum.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_cohort_selfsum.sh
./backup_filename_index.txt:21117:mesh_cohort_selfsum.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_cohort_selfsum.sh
./backup_filename_index.txt:21377:create_mamma_kidd_auth.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/services/create_mamma_kidd_auth.sh
./backup_filename_index.txt:21378:create_mamma_kidd_auth.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/services/create_mamma_kidd_auth.sh
./backup_filename_index.txt:21379:create_mamma_kidd_auth.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/services/create_mamma_kidd_auth.sh
./backup_filename_index.txt:21380:create_mamma_kidd_auth.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/create_mamma_kidd_auth.sh
./backup_filename_index.txt:21381:create_mamma_kidd_auth.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/create_mamma_kidd_auth.sh
./backup_filename_index.txt:21382:create_mamma_kidd_auth.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/services/create_mamma_kidd_auth.sh
./backup_filename_index.txt:21383:create_mamma_kidd_auth.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/create_mamma_kidd_auth.sh
./backup_filename_index.txt:21384:create_mamma_kidd_auth.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/create_mamma_kidd_auth.sh
./backup_filename_index.txt:21385:create_mamma_kidd_auth.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/services/create_mamma_kidd_auth.sh
./backup_filename_index.txt:21386:create_mamma_kidd_auth.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/services/create_mamma_kidd_auth.sh
./backup_filename_index.txt:21387:create_mamma_kidd_auth.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/create_mamma_kidd_auth.sh
./backup_filename_index.txt:21388:create_mamma_kidd_auth.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/services/create_mamma_kidd_auth.sh
./backup_filename_index.txt:21389:create_mamma_kidd_auth.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/create_mamma_kidd_auth.sh
./backup_filename_index.txt:21390:create_mamma_kidd_auth.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/create_mamma_kidd_auth.sh
./backup_filename_index.txt:21951:bridge_ms_jarvis_main_gateway_to_mamma_kidd_auth.log|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/bridge_ms_jarvis_main_gateway_to_mamma_kidd_auth.log
./backup_filename_index.txt:21952:bridge_ms_jarvis_main_gateway_to_mamma_kidd_auth.log|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/bridge_ms_jarvis_main_gateway_to_mamma_kidd_auth.log
./backup_filename_index.txt:21953:bridge_ms_jarvis_main_gateway_to_mamma_kidd_auth.log|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/bridge_ms_jarvis_main_gateway_to_mamma_kidd_auth.log
./backup_filename_index.txt:21954:bridge_ms_jarvis_main_gateway_to_mamma_kidd_auth.log|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/bridge_ms_jarvis_main_gateway_to_mamma_kidd_auth.log
./backup_filename_index.txt:21955:bridge_ms_jarvis_main_gateway_to_mamma_kidd_auth.log|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/bridge_ms_jarvis_main_gateway_to_mamma_kidd_auth.log
./backup_filename_index.txt:21956:bridge_ms_jarvis_main_gateway_to_mamma_kidd_auth.log|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/bridge_ms_jarvis_main_gateway_to_mamma_kidd_auth.log
./backup_filename_index.txt:21957:bridge_ms_jarvis_main_gateway_to_mamma_kidd_auth.log|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/bridge_ms_jarvis_main_gateway_to_mamma_kidd_auth.log
./backup_filename_index.txt:22245:mesh_memory_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_memory_probe.sh
./backup_filename_index.txt:22246:mesh_memory_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_memory_probe.sh
./backup_filename_index.txt:22247:mesh_memory_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_memory_probe.sh
./backup_filename_index.txt:22248:mesh_memory_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_memory_probe.sh
./backup_filename_index.txt:22249:mesh_memory_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_memory_probe.sh
./backup_filename_index.txt:22250:mesh_memory_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_memory_probe.sh
./backup_filename_index.txt:22251:mesh_memory_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_memory_probe.sh
./backup_filename_index.txt:23505:mesh_agent_batch.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_agent_batch.sh
./backup_filename_index.txt:23506:mesh_agent_batch.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_agent_batch.sh
./backup_filename_index.txt:23507:mesh_agent_batch.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_agent_batch.sh
./backup_filename_index.txt:23508:mesh_agent_batch.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_agent_batch.sh
./backup_filename_index.txt:23509:mesh_agent_batch.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_agent_batch.sh
./backup_filename_index.txt:23510:mesh_agent_batch.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_agent_batch.sh
./backup_filename_index.txt:23511:mesh_agent_batch.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_agent_batch.sh
./backup_filename_index.txt:23848:ms_jarvis_authentic_multi_llm_9760.log|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/ms_jarvis_authentic_multi_llm_9760.log
./backup_filename_index.txt:23849:ms_jarvis_authentic_multi_llm_9760.log|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/ms_jarvis_authentic_multi_llm_9760.log
./backup_filename_index.txt:23850:ms_jarvis_authentic_multi_llm_9760.log|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/ms_jarvis_authentic_multi_llm_9760.log
./backup_filename_index.txt:23851:ms_jarvis_authentic_multi_llm_9760.log|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/ms_jarvis_authentic_multi_llm_9760.log
./backup_filename_index.txt:23852:ms_jarvis_authentic_multi_llm_9760.log|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/ms_jarvis_authentic_multi_llm_9760.log
./backup_filename_index.txt:23853:ms_jarvis_authentic_multi_llm_9760.log|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/ms_jarvis_authentic_multi_llm_9760.log
./backup_filename_index.txt:23854:ms_jarvis_authentic_multi_llm_9760.log|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/ms_jarvis_authentic_multi_llm_9760.log
./backup_filename_index.txt:24856:method_tracking_helper.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/method_tracking_helper.py
./backup_filename_index.txt:24857:method_tracking_helper.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/method_tracking_helper.py
./backup_filename_index.txt:24858:method_tracking_helper.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/method_tracking_helper.py
./backup_filename_index.txt:24859:method_tracking_helper.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/method_tracking_helper.py
./backup_filename_index.txt:24860:method_tracking_helper.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/method_tracking_helper.py
./backup_filename_index.txt:24861:method_tracking_helper.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/method_tracking_helper.py
./backup_filename_index.txt:24862:method_tracking_helper.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/method_tracking_helper.py
./backup_filename_index.txt:24891:mesh_interest_timeline.csv|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_interest_timeline.csv
./backup_filename_index.txt:24892:mesh_interest_timeline.csv|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_interest_timeline.csv
./backup_filename_index.txt:24893:mesh_interest_timeline.csv|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_interest_timeline.csv
./backup_filename_index.txt:24894:mesh_interest_timeline.csv|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_interest_timeline.csv
./backup_filename_index.txt:24895:mesh_interest_timeline.csv|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_interest_timeline.csv
./backup_filename_index.txt:24896:mesh_interest_timeline.csv|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_interest_timeline.csv
./backup_filename_index.txt:24897:mesh_interest_timeline.csv|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_interest_timeline.csv
./backup_filename_index.txt:25024:wvu_ldap_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/wvu_ldap_auth.py
./backup_filename_index.txt:25025:wvu_ldap_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/wvu_ldap_auth.py
./backup_filename_index.txt:25026:wvu_ldap_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/wvu_ldap_auth.py
./backup_filename_index.txt:25027:wvu_ldap_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/wvu_ldap_auth.py
./backup_filename_index.txt:25028:wvu_ldap_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/wvu_ldap_auth.py
./backup_filename_index.txt:25029:wvu_ldap_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/wvu_ldap_auth.py
./backup_filename_index.txt:25030:wvu_ldap_auth.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/wvu_ldap_auth.py
./backup_filename_index.txt:25472:memory_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/memory_probe.sh
./backup_filename_index.txt:25473:memory_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/memory_probe.sh
./backup_filename_index.txt:25474:memory_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/memory_probe.sh
./backup_filename_index.txt:25475:memory_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/memory_probe.sh
./backup_filename_index.txt:25476:memory_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/memory_probe.sh
./backup_filename_index.txt:25477:memory_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/memory_probe.sh
./backup_filename_index.txt:25478:memory_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/memory_probe.sh
./backup_filename_index.txt:26508:mesh_emotion_map.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_emotion_map.sh
./backup_filename_index.txt:26509:mesh_emotion_map.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_emotion_map.sh
./backup_filename_index.txt:26510:mesh_emotion_map.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_emotion_map.sh
./backup_filename_index.txt:26511:mesh_emotion_map.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_emotion_map.sh
./backup_filename_index.txt:26512:mesh_emotion_map.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_emotion_map.sh
./backup_filename_index.txt:26513:mesh_emotion_map.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_emotion_map.sh
./backup_filename_index.txt:26514:mesh_emotion_map.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_emotion_map.sh
./backup_filename_index.txt:26795:mesh_context_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_context_probe.sh
./backup_filename_index.txt:26796:mesh_context_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_context_probe.sh
./backup_filename_index.txt:26797:mesh_context_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_context_probe.sh
./backup_filename_index.txt:26798:mesh_context_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_context_probe.sh
./backup_filename_index.txt:26799:mesh_context_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_context_probe.sh
./backup_filename_index.txt:26800:mesh_context_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_context_probe.sh
./backup_filename_index.txt:26801:mesh_context_probe.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_context_probe.sh
./backup_filename_index.txt:27019:test_authentic_voice.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/services/test_authentic_voice.sh
./backup_filename_index.txt:27020:test_authentic_voice.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/test_authentic_voice.sh
./backup_filename_index.txt:27021:test_authentic_voice.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/test_authentic_voice.sh
./backup_filename_index.txt:27022:test_authentic_voice.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/services/test_authentic_voice.sh
./backup_filename_index.txt:27023:test_authentic_voice.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/services/test_authentic_voice.sh
./backup_filename_index.txt:27024:test_authentic_voice.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/services/test_authentic_voice.sh
./backup_filename_index.txt:27025:test_authentic_voice.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/test_authentic_voice.sh
./backup_filename_index.txt:27026:test_authentic_voice.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/test_authentic_voice.sh
./backup_filename_index.txt:27027:test_authentic_voice.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/test_authentic_voice.sh
./backup_filename_index.txt:27028:test_authentic_voice.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/test_authentic_voice.sh
./backup_filename_index.txt:27029:test_authentic_voice.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/services/test_authentic_voice.sh
./backup_filename_index.txt:27030:test_authentic_voice.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/services/test_authentic_voice.sh
./backup_filename_index.txt:27031:test_authentic_voice.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/services/test_authentic_voice.sh
./backup_filename_index.txt:27032:test_authentic_voice.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/test_authentic_voice.sh
./backup_filename_index.txt:27705:memory_dgm_engine.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/memory_dgm_engine.py
./backup_filename_index.txt:27706:memory_dgm_engine.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/memory_dgm_engine.py
./backup_filename_index.txt:27707:memory_dgm_engine.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/memory_dgm_engine.py
./backup_filename_index.txt:27708:memory_dgm_engine.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/memory_dgm_engine.py
./backup_filename_index.txt:27709:memory_dgm_engine.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/memory_dgm_engine.py
./backup_filename_index.txt:27710:memory_dgm_engine.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/memory_dgm_engine.py
./backup_filename_index.txt:27711:memory_dgm_engine.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/memory_dgm_engine.py
./backup_filename_index.txt:27838:mesh_broadcast_event.sh|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mesh_broadcast_event.sh
./backup_filename_index.txt:27839:mesh_broadcast_event.sh|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mesh_broadcast_event.sh
./backup_filename_index.txt:27840:mesh_broadcast_event.sh|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mesh_broadcast_event.sh
./backup_filename_index.txt:27841:mesh_broadcast_event.sh|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mesh_broadcast_event.sh
./backup_filename_index.txt:27842:mesh_broadcast_event.sh|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mesh_broadcast_event.sh
./backup_filename_index.txt:27843:mesh_broadcast_event.sh|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mesh_broadcast_event.sh
./backup_filename_index.txt:27844:mesh_broadcast_event.sh|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mesh_broadcast_event.sh
./backup_filename_index.txt:28552:mamma_kidd_auth.py.backup_20251013_201428|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/mamma_kidd_auth.py.backup_20251013_201428
./backup_filename_index.txt:28553:mamma_kidd_auth.py.backup_20251013_201428|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/mamma_kidd_auth.py.backup_20251013_201428
./backup_filename_index.txt:28554:mamma_kidd_auth.py.backup_20251013_201428|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/mamma_kidd_auth.py.backup_20251013_201428
./backup_filename_index.txt:28555:mamma_kidd_auth.py.backup_20251013_201428|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/mamma_kidd_auth.py.backup_20251013_201428
./backup_filename_index.txt:28556:mamma_kidd_auth.py.backup_20251013_201428|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/mamma_kidd_auth.py.backup_20251013_201428
./backup_filename_index.txt:28557:mamma_kidd_auth.py.backup_20251013_201428|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/mamma_kidd_auth.py.backup_20251013_201428
./backup_filename_index.txt:28558:mamma_kidd_auth.py.backup_20251013_201428|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/mamma_kidd_auth.py.backup_20251013_201428
./backup_filename_index.txt:28867:bridge_ms_jarvis_main_gateway_to_oauth2_handler.log|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/bridge_ms_jarvis_main_gateway_to_oauth2_handler.log
./backup_filename_index.txt:28868:bridge_ms_jarvis_main_gateway_to_oauth2_handler.log|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/bridge_ms_jarvis_main_gateway_to_oauth2_handler.log
./backup_filename_index.txt:28869:bridge_ms_jarvis_main_gateway_to_oauth2_handler.log|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/bridge_ms_jarvis_main_gateway_to_oauth2_handler.log
./backup_filename_index.txt:28870:bridge_ms_jarvis_main_gateway_to_oauth2_handler.log|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/bridge_ms_jarvis_main_gateway_to_oauth2_handler.log
./backup_filename_index.txt:28871:bridge_ms_jarvis_main_gateway_to_oauth2_handler.log|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/bridge_ms_jarvis_main_gateway_to_oauth2_handler.log
./backup_filename_index.txt:28872:bridge_ms_jarvis_main_gateway_to_oauth2_handler.log|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/bridge_ms_jarvis_main_gateway_to_oauth2_handler.log
./backup_filename_index.txt:28873:bridge_ms_jarvis_main_gateway_to_oauth2_handler.log|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/bridge_ms_jarvis_main_gateway_to_oauth2_handler.log
./backup_filename_index.txt:29791:memory_dgm_engine_9919.log|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/memory_dgm_engine_9919.log
./backup_filename_index.txt:29792:memory_dgm_engine_9919.log|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/memory_dgm_engine_9919.log
./backup_filename_index.txt:29793:memory_dgm_engine_9919.log|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/memory_dgm_engine_9919.log
./backup_filename_index.txt:29794:memory_dgm_engine_9919.log|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/memory_dgm_engine_9919.log
./backup_filename_index.txt:29795:memory_dgm_engine_9919.log|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/memory_dgm_engine_9919.log
./backup_filename_index.txt:29796:memory_dgm_engine_9919.log|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/memory_dgm_engine_9919.log
./backup_filename_index.txt:29797:memory_dgm_engine_9919.log|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/memory_dgm_engine_9919.log
./backup_filename_index.txt:30069:__init__.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/__pycache__/__init__.cpython-312.pyc
./backup_filename_index.txt:30101:__init__.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/oauthlib/__pycache__/__init__.cpython-312.pyc
./backup_filename_index.txt:30123:meaning_maker.py|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py
./backup_filename_index.txt:30124:meaning_maker.py|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py
./backup_filename_index.txt:30125:meaning_maker.py|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py
./backup_filename_index.txt:30126:meaning_maker.py|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py
./backup_filename_index.txt:30127:meaning_maker.py|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py
./backup_filename_index.txt:30128:meaning_maker.py|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py
./backup_filename_index.txt:30129:meaning_maker.py|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py
./backup_filename_index.txt:30130:meaning_maker.py.patch|/mnt/MS_Jarvis/msjarvis-backups/20251231_020001/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py.patch
./backup_filename_index.txt:30131:meaning_maker.py.patch|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py.patch
./backup_filename_index.txt:30132:meaning_maker.py.patch|/mnt/MS_Jarvis/msjarvis-backups/20260103_020002/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py.patch
./backup_filename_index.txt:30133:meaning_maker.py.patch|/mnt/MS_Jarvis/msjarvis-backups/20260102_020001/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py.patch
./backup_filename_index.txt:30134:meaning_maker.py.patch|/mnt/MS_Jarvis/msjarvis-backups/20251230_020001/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py.patch
./backup_filename_index.txt:30135:meaning_maker.py.patch|/mnt/MS_Jarvis/msjarvis-backups/20260101_020001/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py.patch
./backup_filename_index.txt:30136:meaning_maker.py.patch|/mnt/MS_Jarvis/msjarvis-backups/20251229_020001/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py.patch
./backup_filename_index.txt:30621:metfacp_reg_ll83_attrs.csv|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/metfacp_reg_ll83_attrs.csv
./backup_filename_index.txt:30633:metropolitanandmicropolitanstatisticalareas_census_201111_utm83_attrs.csv|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/metropolitanandmicropolitanstatisticalareas_census_201111_utm83_attrs.csv
./backup_filename_index.txt:30672:metropolitanstatisticalareas_uscensus_199901_ll83_attrs.csv|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/metropolitanstatisticalareas_uscensus_199901_ll83_attrs.csv
./backup_filename_index.txt:30674:communityhealthproviders_wvhealthcareauthority_200802_utm83_attrs.csv|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/communityhealthproviders_wvhealthcareauthority_200802_utm83_attrs.csv
./backup_filename_index.txt:30684:metropolitanandmicropolitanstatisticalareas_census_201111_gcs83_attrs.csv|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/metropolitanandmicropolitanstatisticalareas_census_201111_gcs83_attrs.csv
./backup_filename_index.txt:30691:metropolitanandmicropolitanstatisticalareas_census_2020_wma84_attrs.csv|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/metropolitanandmicropolitanstatisticalareas_census_2020_wma84_attrs.csv
./backup_filename_index.txt:30716:metropolitanandmicropolitanstatisticalareas_census_2020_utm83_attrs.csv|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/metropolitanandmicropolitanstatisticalareas_census_2020_utm83_attrs.csv
./backup_filename_index.txt:30736:metropolitanstatisticalareas_uscensus_199901_utm83_attrs.csv|/mnt/MS_Jarvis/msjarvis-backups/20260105_020001/services/metropolitanstatisticalareas_uscensus_199901_utm83_attrs.csv
./backup_filename_index.txt:30858:py.typed|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/py.typed
./backup_filename_index.txt:30874:py.typed|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/metrics/py.typed
./backup_filename_index.txt:30920:py.typed|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/py.typed
./backup_filename_index.txt:30962:WHEEL|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib-2.0.0.dist-info/WHEEL
./backup_filename_index.txt:30978:WHEEL|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google_auth-2.45.0.dist-info/WHEEL
./backup_filename_index.txt:30986:WHEEL|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/oauthlib-3.3.1.dist-info/WHEEL
./backup_filename_index.txt:31032:RECORD|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib-2.0.0.dist-info/RECORD
./backup_filename_index.txt:31064:RECORD|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/oauthlib-3.3.1.dist-info/RECORD
./backup_filename_index.txt:31068:RECORD|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google_auth-2.45.0.dist-info/RECORD
./backup_filename_index.txt:31133:LICENSE|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google_auth-2.45.0.dist-info/licenses/LICENSE
./backup_filename_index.txt:31138:LICENSE|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib-2.0.0.dist-info/LICENSE
./backup_filename_index.txt:31149:LICENSE|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/oauthlib-3.3.1.dist-info/licenses/LICENSE
./backup_filename_index.txt:31204:INSTALLER|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google_auth-2.45.0.dist-info/INSTALLER
./backup_filename_index.txt:31206:INSTALLER|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib-2.0.0.dist-info/INSTALLER
./backup_filename_index.txt:31226:INSTALLER|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/oauthlib-3.3.1.dist-info/INSTALLER
./backup_filename_index.txt:31382:exceptions.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/exceptions.py
./backup_filename_index.txt:31415:utils.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/utils.py
./backup_filename_index.txt:31541:message.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/message.py
./backup_filename_index.txt:31562:message_factory.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/protobuf/message_factory.py
./backup_filename_index.txt:31569:_default.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/_default.py
./backup_filename_index.txt:31570:_default_async.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/_default_async.py
./backup_filename_index.txt:31571:environment_vars.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/environment_vars.py
./backup_filename_index.txt:31572:downscoped.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/downscoped.py
./backup_filename_index.txt:31579:version.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/version.py
./backup_filename_index.txt:31586:external_account.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/external_account.py
./backup_filename_index.txt:31587:_service_account_info.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/_service_account_info.py
./backup_filename_index.txt:31588:pluggable.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/pluggable.py
./backup_filename_index.txt:31589:_agent_identity_utils.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/_agent_identity_utils.py
./backup_filename_index.txt:31590:_exponential_backoff.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/_exponential_backoff.py
./backup_filename_index.txt:31591:_helpers.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/_helpers.py
./backup_filename_index.txt:31592:impersonated_credentials.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/impersonated_credentials.py
./backup_filename_index.txt:31593:_cloud_sdk.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/_cloud_sdk.py
./backup_filename_index.txt:31594:_credentials_base.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/_credentials_base.py
./backup_filename_index.txt:31595:credentials.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/credentials.py
./backup_filename_index.txt:31596:credentials.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/credentials.py
./backup_filename_index.txt:31597:external_account_authorized_user.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/external_account_authorized_user.py
./backup_filename_index.txt:31598:_credentials_async.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/_credentials_async.py
./backup_filename_index.txt:31599:_credentials_async.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/_credentials_async.py
./backup_filename_index.txt:31600:_refresh_worker.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/_refresh_worker.py
./backup_filename_index.txt:31601:app_engine.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/app_engine.py
./backup_filename_index.txt:31602:aws.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/aws.py
./backup_filename_index.txt:31603:iam.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/iam.py
./backup_filename_index.txt:31604:metrics.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/metrics.py
./backup_filename_index.txt:31605:metrics.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/onnxruntime/transformers/metrics.py
./backup_filename_index.txt:31606:api_key.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/api_key.py
./backup_filename_index.txt:31608:identity_pool.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/identity_pool.py
./backup_filename_index.txt:31609:_constants.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/_constants.py
./backup_filename_index.txt:31611:jwt.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/jwt.py
./backup_filename_index.txt:31612:_oauth2client.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/_oauth2client.py
./backup_filename_index.txt:31613:_jwt_async.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/auth/_jwt_async.py
./backup_filename_index.txt:31614:challenges.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/challenges.py
./backup_filename_index.txt:31615:id_token.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/id_token.py
./backup_filename_index.txt:31616:webauthn_types.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/webauthn_types.py
./backup_filename_index.txt:31617:_service_account_async.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/_service_account_async.py
./backup_filename_index.txt:31618:_client_async.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/_client_async.py
./backup_filename_index.txt:31619:_client.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/_client.py
./backup_filename_index.txt:31622:_id_token_async.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/_id_token_async.py
./backup_filename_index.txt:31623:webauthn_handler.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/webauthn_handler.py
./backup_filename_index.txt:31624:gdch_credentials.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/gdch_credentials.py
./backup_filename_index.txt:31625:_reauth_async.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/_reauth_async.py
./backup_filename_index.txt:31626:webauthn_handler_factory.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/webauthn_handler_factory.py
./backup_filename_index.txt:31627:reauth.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/reauth.py
./backup_filename_index.txt:31628:service_account.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/service_account.py
./backup_filename_index.txt:31629:sts.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/oauth2/sts.py
./backup_filename_index.txt:31680:auth_pb2.pyi|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/api/auth_pb2.pyi
./backup_filename_index.txt:31688:auth.proto|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/api/auth.proto
./backup_filename_index.txt:31689:metric_pb2.pyi|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/api/metric_pb2.pyi
./backup_filename_index.txt:31714:metric.proto|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/api/metric.proto
./backup_filename_index.txt:31724:auth_pb2.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/api/auth_pb2.py
./backup_filename_index.txt:31730:metric_pb2.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/google/api/metric_pb2.py
./backup_filename_index.txt:32038:auth.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/websockets/legacy/auth.py
./backup_filename_index.txt:32039:auth.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/cli/auth.py
./backup_filename_index.txt:32040:auth.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/websockets/auth.py
./backup_filename_index.txt:32041:auth.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests/auth.py
./backup_filename_index.txt:32085:auth.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests/__pycache__/auth.cpython-312.pyc
./backup_filename_index.txt:32086:auth.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/websockets/__pycache__/auth.cpython-312.pyc
./backup_filename_index.txt:32095:messages.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/websockets/sync/messages.py
./backup_filename_index.txt:32096:messages.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/websockets/asyncio/messages.py
./backup_filename_index.txt:32194:messageid.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/chromadb/utils/messageid.py
./backup_filename_index.txt:32307:signals.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/oauthlib/signals.py
./backup_filename_index.txt:32382:common.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/oauthlib/common.py
./backup_filename_index.txt:32388:common.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/oauthlib/__pycache__/common.cpython-312.pyc
./backup_filename_index.txt:32506:meson.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/pygments/lexers/meson.py
./backup_filename_index.txt:32838:oauth2.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py
./backup_filename_index.txt:32889:uri_validate.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/oauthlib/uri_validate.py
./backup_filename_index.txt:32890:signals.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/oauthlib/__pycache__/signals.cpython-312.pyc
./backup_filename_index.txt:32891:uri_validate.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/oauthlib/__pycache__/uri_validate.cpython-312.pyc
./backup_filename_index.txt:32995:measure.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/rich/measure.py
./backup_filename_index.txt:33041:measure.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/rich/__pycache__/measure.cpython-312.pyc
./backup_filename_index.txt:33152:memory.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/fsspec/implementations/memory.py
./backup_filename_index.txt:33153:memory.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/anyio/streams/memory.py
./backup_filename_index.txt:33178:metadata.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/packaging/metadata.py
./backup_filename_index.txt:33181:metadata.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/packaging/__pycache__/metadata.cpython-312.pyc
./backup_filename_index.txt:33353:memmap.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/numpy/core/memmap.py
./backup_filename_index.txt:33361:memmap.pyi|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/numpy/core/memmap.pyi
./backup_filename_index.txt:33584:memoization.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/sympy/utilities/memoization.py
./backup_filename_index.txt:33708:meijerint_doc.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/sympy/integrals/meijerint_doc.py
./backup_filename_index.txt:33710:meijerint.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/sympy/integrals/meijerint.py
./backup_filename_index.txt:33934:oauth2_session.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/oauth2_session.py
./backup_filename_index.txt:33935:oauth1_auth.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/oauth1_auth.py
./backup_filename_index.txt:33936:oauth2_auth.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/oauth2_auth.py
./backup_filename_index.txt:33937:oauth1_session.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/oauth1_session.py
./backup_filename_index.txt:33938:oauth1_auth.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/__pycache__/oauth1_auth.cpython-312.pyc
./backup_filename_index.txt:33939:oauth2_session.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/__pycache__/oauth2_session.cpython-312.pyc
./backup_filename_index.txt:33940:oauth1_session.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/__pycache__/oauth1_session.cpython-312.pyc
./backup_filename_index.txt:33941:oauth2_auth.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/__pycache__/oauth2_auth.cpython-312.pyc
./backup_filename_index.txt:33942:weibo.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/weibo.py
./backup_filename_index.txt:33943:fitbit.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/fitbit.py
./backup_filename_index.txt:33944:slack.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/slack.py
./backup_filename_index.txt:33946:mailchimp.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/mailchimp.py
./backup_filename_index.txt:33947:plentymarkets.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/plentymarkets.py
./backup_filename_index.txt:33948:facebook.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/facebook.py
./backup_filename_index.txt:33949:douban.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/douban.py
./backup_filename_index.txt:33950:ebay.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/ebay.py
./backup_filename_index.txt:33951:instagram.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/instagram.py
./backup_filename_index.txt:34013:_oauth.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/_oauth.py
./backup_filename_index.txt:34033:_oauth.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/__pycache__/_oauth.cpython-312.pyc
./backup_filename_index.txt:34075:_auth.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/httpx/_auth.py
./backup_filename_index.txt:34076:_auth.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/grpc/_auth.py
./backup_filename_index.txt:34077:_auth.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/huggingface_hub/utils/_auth.py
./backup_filename_index.txt:34635:_auth.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/grpc/__pycache__/_auth.cpython-312.pyc
./backup_filename_index.txt:34636:_auth.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/httpx/__pycache__/_auth.cpython-312.pyc
./backup_filename_index.txt:34656:authentication.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/starlette/middleware/authentication.py
./backup_filename_index.txt:34657:authentication.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/starlette/authentication.py
./backup_filename_index.txt:34667:authentication.cpython-312.pyc|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/starlette/__pycache__/authentication.cpython-312.pyc
./backup_filename_index.txt:34689:message_logger.py|/mnt/MS_Jarvis/chroma_inspect_venv/lib/python3.12/site-packages/uvicorn/middleware/message_logger.py
./backup_filename_index.txt:35010:latest|/mnt/MS_Jarvis/msjarvis_secondary/models/manifests/registry.ollama.ai/library/medllama2/latest
./services/all_actual_py.txt:5:/home/ms-jarvis/msjarvis-rebuild/services/memory_dgm_engine.py
./services/all_actual_py.txt:174:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/huggingface_hub/utils/_auth.py
./services/all_actual_py.txt:200:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/huggingface_hub/_oauth.py
./services/all_actual_py.txt:215:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/huggingface_hub/cli/auth.py
./services/all_actual_py.txt:245:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/websockets/legacy/auth.py
./services/all_actual_py.txt:254:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/websockets/auth.py
./services/all_actual_py.txt:264:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/websockets/asyncio/messages.py
./services/all_actual_py.txt:271:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/websockets/sync/messages.py
./services/all_actual_py.txt:318:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests/auth.py
./services/all_actual_py.txt:509:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/grpc/_auth.py
./services/all_actual_py.txt:802:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/joint.py
./services/all_actual_py.txt:803:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/linearize.py
./services/all_actual_py.txt:804:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/models.py
./services/all_actual_py.txt:805:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/lagrange.py
./services/all_actual_py.txt:806:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_rigidbody.py
./services/all_actual_py.txt:807:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_actuator.py
./services/all_actual_py.txt:808:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane3.py
./services/all_actual_py.txt:809:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_body.py
./services/all_actual_py.txt:810:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_system_class.py
./services/all_actual_py.txt:811:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_loads.py
./services/all_actual_py.txt:812:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane4.py
./services/all_actual_py.txt:813:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane5.py
./services/all_actual_py.txt:814:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_models.py
./services/all_actual_py.txt:815:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_method.py
./services/all_actual_py.txt:816:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_wrapping_geometry.py
./services/all_actual_py.txt:817:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_lagrange2.py
./services/all_actual_py.txt:818:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_linearity_of_velocity_constraints.py
./services/all_actual_py.txt:819:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_system.py
./services/all_actual_py.txt:820:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_functions.py
./services/all_actual_py.txt:821:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_inertia.py
./services/all_actual_py.txt:822:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/__init__.py
./services/all_actual_py.txt:823:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_pathway.py
./services/all_actual_py.txt:824:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_lagrange.py
./services/all_actual_py.txt:825:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane2.py
./services/all_actual_py.txt:826:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_particle.py
./services/all_actual_py.txt:827:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_joint.py
./services/all_actual_py.txt:828:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_linearize.py
./services/all_actual_py.txt:829:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane.py
./services/all_actual_py.txt:830:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_jointsmethod.py
./services/all_actual_py.txt:831:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/jointsmethod.py
./services/all_actual_py.txt:832:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/rigidbody.py
./services/all_actual_py.txt:833:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/body_base.py
./services/all_actual_py.txt:834:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/loads.py
./services/all_actual_py.txt:835:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/pathway.py
./services/all_actual_py.txt:836:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/__init__.py
./services/all_actual_py.txt:837:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/inertia.py
./services/all_actual_py.txt:838:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/particle.py
./services/all_actual_py.txt:839:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/method.py
./services/all_actual_py.txt:840:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/body.py
./services/all_actual_py.txt:841:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/kane.py
./services/all_actual_py.txt:842:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/system.py
./services/all_actual_py.txt:843:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/wrapping_geometry.py
./services/all_actual_py.txt:844:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/actuator.py
./services/all_actual_py.txt:845:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/functions.py
./services/all_actual_py.txt:876:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/optics/medium.py
./services/all_actual_py.txt:1541:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/integrals/meijerint.py
./services/all_actual_py.txt:1576:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/integrals/meijerint_doc.py
./services/all_actual_py.txt:2024:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/utilities/memoization.py
./services/all_actual_py.txt:2069:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/oauth2_session.py
./services/all_actual_py.txt:2070:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/slack.py
./services/all_actual_py.txt:2071:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/facebook.py
./services/all_actual_py.txt:2072:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/plentymarkets.py
./services/all_actual_py.txt:2073:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/ebay.py
./services/all_actual_py.txt:2074:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/__init__.py
./services/all_actual_py.txt:2075:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/douban.py
./services/all_actual_py.txt:2076:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/instagram.py
./services/all_actual_py.txt:2077:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/mailchimp.py
./services/all_actual_py.txt:2078:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/fitbit.py
./services/all_actual_py.txt:2079:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/weibo.py
./services/all_actual_py.txt:2080:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/oauth1_auth.py
./services/all_actual_py.txt:2081:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/__init__.py
./services/all_actual_py.txt:2082:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/oauth2_auth.py
./services/all_actual_py.txt:2083:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/oauth1_session.py
./services/all_actual_py.txt:2447:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/onnxruntime/transformers/metrics.py
./services/all_actual_py.txt:2508:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/uvicorn/middleware/message_logger.py
./services/all_actual_py.txt:2589:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/fastapi/security/oauth2.py
./services/all_actual_py.txt:2665:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_actual_py.txt:2720:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_actual_py.txt:2813:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_vendor/packaging/metadata.py
./services/all_actual_py.txt:2892:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_actual_py.txt:2893:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_actual_py.txt:2894:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_actual_py.txt:2895:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_actual_py.txt:2896:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_actual_py.txt:2897:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_actual_py.txt:2898:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_actual_py.txt:2899:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_actual_py.txt:2905:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_actual_py.txt:2909:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_actual_py.txt:2921:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_actual_py.txt:2923:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_actual_py.txt:3267:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pygments/lexers/meson.py
./services/all_actual_py.txt:3537:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/kubernetes/client/api/authorization_v1_api.py
./services/all_actual_py.txt:3543:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/kubernetes/client/api/rbac_authorization_api.py
./services/all_actual_py.txt:3547:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/kubernetes/client/api/authentication_v1_api.py
./services/all_actual_py.txt:3555:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/kubernetes/client/api/authorization_api.py
./services/all_actual_py.txt:3563:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/kubernetes/client/api/rbac_authorization_v1_api.py
./services/all_actual_py.txt:3573:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/kubernetes/client/api/authentication_api.py
./services/all_actual_py.txt:3817:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/kubernetes/client/models/authentication_v1_token_request.py
./services/all_actual_py.txt:4329:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/rich/measure.py
./services/all_actual_py.txt:4437:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/export/__init__.py
./services/all_actual_py.txt:4438:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement.py
./services/all_actual_py.txt:4439:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/view.py
./services/all_actual_py.txt:4440:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement_consumer.py
./services/all_actual_py.txt:4441:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/export/__init__.py
./services/all_actual_py.txt:4442:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/_view_instrument_match.py
./services/all_actual_py.txt:4443:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/aggregation.py
./services/all_actual_py.txt:4444:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exceptions.py
./services/all_actual_py.txt:4445:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/instrument.py
./services/all_actual_py.txt:4446:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py
./services/all_actual_py.txt:4447:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/__init__.py
./services/all_actual_py.txt:4448:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/buckets.py
./services/all_actual_py.txt:4449:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/exponent_mapping.py
./services/all_actual_py.txt:4450:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/errors.py
./services/all_actual_py.txt:4451:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/logarithm_mapping.py
./services/all_actual_py.txt:4452:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/__init__.py
./services/all_actual_py.txt:4453:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/ieee_754.py
./services/all_actual_py.txt:4454:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/point.py
./services/all_actual_py.txt:4455:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/metric_reader_storage.py
./services/all_actual_py.txt:4456:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar_filter.py
./services/all_actual_py.txt:4457:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar_reservoir.py
./services/all_actual_py.txt:4458:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/__init__.py
./services/all_actual_py.txt:4459:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar.py
./services/all_actual_py.txt:4460:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/sdk_configuration.py
./services/all_actual_py.txt:4461:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/view/__init__.py
./services/all_actual_py.txt:4462:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/__init__.py
./services/all_actual_py.txt:4470:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/trace/_sampling_experimental/_parent_threshold.py
./services/all_actual_py.txt:4497:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/metrics/db_metrics.py
./services/all_actual_py.txt:4498:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/metrics/__init__.py
./services/all_actual_py.txt:4499:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/metrics/http_metrics.py
./services/all_actual_py.txt:4503:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/dns_metrics.py
./services/all_actual_py.txt:4504:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cicd_metrics.py
./services/all_actual_py.txt:4505:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/vcs_metrics.py
./services/all_actual_py.txt:4506:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/db_metrics.py
./services/all_actual_py.txt:4507:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/rpc_metrics.py
./services/all_actual_py.txt:4508:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cpu_metrics.py
./services/all_actual_py.txt:4509:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cpython_metrics.py
./services/all_actual_py.txt:4510:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/gen_ai_metrics.py
./services/all_actual_py.txt:4511:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/faas_metrics.py
./services/all_actual_py.txt:4512:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/system_metrics.py
./services/all_actual_py.txt:4513:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/process_metrics.py
./services/all_actual_py.txt:4514:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/otel_metrics.py
./services/all_actual_py.txt:4515:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/messaging_metrics.py
./services/all_actual_py.txt:4516:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/hw_metrics.py
./services/all_actual_py.txt:4517:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/k8s_metrics.py
./services/all_actual_py.txt:4518:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/http_metrics.py
./services/all_actual_py.txt:4519:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py
./services/all_actual_py.txt:4520:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/azure_metrics.py
./services/all_actual_py.txt:4522:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/message_attributes.py
./services/all_actual_py.txt:4582:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/messaging_attributes.py
./services/all_actual_py.txt:4635:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/metric_exporter/__init__.py
./services/all_actual_py.txt:4638:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/common/metrics_encoder.py
./services/all_actual_py.txt:4642:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/common/_internal/metrics_encoder/__init__.py
./services/all_actual_py.txt:4647:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/metrics/_internal/instrument.py
./services/all_actual_py.txt:4648:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/metrics/_internal/__init__.py
./services/all_actual_py.txt:4649:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/metrics/_internal/observation.py
./services/all_actual_py.txt:4650:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/metrics/__init__.py
./services/all_actual_py.txt:4663:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/proto/metrics/v1/metrics_pb2.py
./services/all_actual_py.txt:4664:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/proto/metrics/v1/__init__.py
./services/all_actual_py.txt:4665:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/proto/metrics/__init__.py
./services/all_actual_py.txt:4676:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/metrics_service_pb2_grpc.py
./services/all_actual_py.txt:4677:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/metrics_service_pb2.py
./services/all_actual_py.txt:4678:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/__init__.py
./services/all_actual_py.txt:4679:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/__init__.py
./services/all_actual_py.txt:4720:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/packaging/metadata.py
./services/all_actual_py.txt:4784:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/errors.py
./services/all_actual_py.txt:4785:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/pre_configured.py
./services/all_actual_py.txt:4786:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/revocation.py
./services/all_actual_py.txt:4787:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/resource.py
./services/all_actual_py.txt:4788:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/metadata.py
./services/all_actual_py.txt:4789:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/__init__.py
./services/all_actual_py.txt:4790:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/authorization.py
./services/all_actual_py.txt:4791:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/introspect.py
./services/all_actual_py.txt:4792:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/base.py
./services/all_actual_py.txt:4793:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/token.py
./services/all_actual_py.txt:4794:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/mobile_application.py
./services/all_actual_py.txt:4795:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/legacy_application.py
./services/all_actual_py.txt:4796:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/backend_application.py
./services/all_actual_py.txt:4797:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/service_application.py
./services/all_actual_py.txt:4798:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/__init__.py
./services/all_actual_py.txt:4799:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/web_application.py
./services/all_actual_py.txt:4800:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/base.py
./services/all_actual_py.txt:4801:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/parameters.py
./services/all_actual_py.txt:4802:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/resource_owner_password_credentials.py
./services/all_actual_py.txt:4803:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/__init__.py
./services/all_actual_py.txt:4804:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/client_credentials.py
./services/all_actual_py.txt:4805:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/implicit.py
./services/all_actual_py.txt:4806:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/refresh_token.py
./services/all_actual_py.txt:4807:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/base.py
./services/all_actual_py.txt:4808:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/authorization_code.py
./services/all_actual_py.txt:4809:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/request_validator.py
./services/all_actual_py.txt:4810:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/__init__.py
./services/all_actual_py.txt:4811:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/utils.py
./services/all_actual_py.txt:4812:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/tokens.py
./services/all_actual_py.txt:4813:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/errors.py
./services/all_actual_py.txt:4814:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/pre_configured.py
./services/all_actual_py.txt:4815:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/__init__.py
./services/all_actual_py.txt:4816:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/device_authorization.py
./services/all_actual_py.txt:4817:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/clients/device.py
./services/all_actual_py.txt:4818:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/clients/__init__.py
./services/all_actual_py.txt:4819:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/grant_types/__init__.py
./services/all_actual_py.txt:4820:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/grant_types/device_code.py
./services/all_actual_py.txt:4821:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/request_validator.py
./services/all_actual_py.txt:4822:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/__init__.py
./services/all_actual_py.txt:4823:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/__init__.py
./services/all_actual_py.txt:4824:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/__init__.py
./services/all_actual_py.txt:4825:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/signature.py
./services/all_actual_py.txt:4826:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/errors.py
./services/all_actual_py.txt:4827:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/pre_configured.py
./services/all_actual_py.txt:4828:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/resource.py
./services/all_actual_py.txt:4829:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/access_token.py
./services/all_actual_py.txt:4830:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/__init__.py
./services/all_actual_py.txt:4831:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/authorization.py
./services/all_actual_py.txt:4832:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/request_token.py
./services/all_actual_py.txt:4833:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/signature_only.py
./services/all_actual_py.txt:4834:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/base.py
./services/all_actual_py.txt:4835:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/parameters.py
./services/all_actual_py.txt:4836:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/request_validator.py
./services/all_actual_py.txt:4837:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/__init__.py
./services/all_actual_py.txt:4838:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/utils.py
./services/all_actual_py.txt:4839:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/uri_validate.py
./services/all_actual_py.txt:4840:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/__init__.py
./services/all_actual_py.txt:4841:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/common.py
./services/all_actual_py.txt:4842:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/signals.py
./services/all_actual_py.txt:4843:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/__init__.py
./services/all_actual_py.txt:4844:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/pre_configured.py
./services/all_actual_py.txt:4845:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/userinfo.py
./services/all_actual_py.txt:4846:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/__init__.py
./services/all_actual_py.txt:4847:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/exceptions.py
./services/all_actual_py.txt:4848:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/dispatchers.py
./services/all_actual_py.txt:4849:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/__init__.py
./services/all_actual_py.txt:4850:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/hybrid.py
./services/all_actual_py.txt:4851:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/implicit.py
./services/all_actual_py.txt:4852:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/refresh_token.py
./services/all_actual_py.txt:4853:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/base.py
./services/all_actual_py.txt:4854:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/authorization_code.py
./services/all_actual_py.txt:4855:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/request_validator.py
./services/all_actual_py.txt:4856:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/__init__.py
./services/all_actual_py.txt:4857:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/tokens.py
./services/all_actual_py.txt:4858:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/__init__.py
./services/all_actual_py.txt:4915:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/fsspec/implementations/memory.py
./services/all_actual_py.txt:4946:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/basic/__init__.py
./services/all_actual_py.txt:4947:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/token/__init__.py
./services/all_actual_py.txt:4948:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/providers.py
./services/all_actual_py.txt:4949:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/__init__.py
./services/all_actual_py.txt:4950:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/fastapi.py
./services/all_actual_py.txt:4951:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/registry.py
./services/all_actual_py.txt:4952:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/authz/__init__.py
./services/all_actual_py.txt:4953:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/fastapi_utils.py
./services/all_actual_py.txt:4962:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/test/auth/test_simple_rbac_authz.py
./services/all_actual_py.txt:4963:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/test/auth/test_token_auth.py
./services/all_actual_py.txt:4964:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/test/auth/test_basic_auth.py
./services/all_actual_py.txt:4982:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/test/client/create_http_client_with_basic_auth.py
./services/all_actual_py.txt:5011:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/utils/messageid.py
./services/all_actual_py.txt:5032:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/segment/impl/metadata/sqlite.py
./services/all_actual_py.txt:5414:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/numpy/_core/memmap.py
./services/all_actual_py.txt:5735:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/anyio/streams/memory.py
./services/all_actual_py.txt:5751:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/starlette/middleware/authentication.py
./services/all_actual_py.txt:5763:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/starlette/authentication.py
./services/all_actual_py.txt:5775:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_refresh_worker.py
./services/all_actual_py.txt:5776:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/compute_engine/credentials.py
./services/all_actual_py.txt:5777:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/compute_engine/_metadata.py
./services/all_actual_py.txt:5778:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/compute_engine/__init__.py
./services/all_actual_py.txt:5779:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_credentials_base.py
./services/all_actual_py.txt:5780:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_oauth2client.py
./services/all_actual_py.txt:5781:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/iam.py
./services/all_actual_py.txt:5782:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/version.py
./services/all_actual_py.txt:5783:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/downscoped.py
./services/all_actual_py.txt:5784:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_helpers.py
./services/all_actual_py.txt:5785:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/external_account_authorized_user.py
./services/all_actual_py.txt:5786:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/impersonated_credentials.py
./services/all_actual_py.txt:5787:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/credentials.py
./services/all_actual_py.txt:5788:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/exceptions.py
./services/all_actual_py.txt:5789:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_default_async.py
./services/all_actual_py.txt:5790:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/aio/_helpers.py
./services/all_actual_py.txt:5791:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/aio/credentials.py
./services/all_actual_py.txt:5792:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/aio/__init__.py
./services/all_actual_py.txt:5793:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/aio/transport/aiohttp.py
./services/all_actual_py.txt:5794:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/aio/transport/__init__.py
./services/all_actual_py.txt:5795:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/aio/transport/sessions.py
./services/all_actual_py.txt:5796:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/aws.py
./services/all_actual_py.txt:5797:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/environment_vars.py
./services/all_actual_py.txt:5798:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_service_account_info.py
./services/all_actual_py.txt:5799:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/app_engine.py
./services/all_actual_py.txt:5800:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/__init__.py
./services/all_actual_py.txt:5801:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_credentials_async.py
./services/all_actual_py.txt:5802:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_constants.py
./services/all_actual_py.txt:5803:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/pluggable.py
./services/all_actual_py.txt:5804:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/metrics.py
./services/all_actual_py.txt:5805:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/_custom_tls_signer.py
./services/all_actual_py.txt:5806:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/grpc.py
./services/all_actual_py.txt:5807:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/mtls.py
./services/all_actual_py.txt:5808:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/__init__.py
./services/all_actual_py.txt:5809:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/_requests_base.py
./services/all_actual_py.txt:5810:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/urllib3.py
./services/all_actual_py.txt:5811:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/_http_client.py
./services/all_actual_py.txt:5812:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/_aiohttp_requests.py
./services/all_actual_py.txt:5813:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/_mtls_helper.py
./services/all_actual_py.txt:5814:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/requests.py
./services/all_actual_py.txt:5815:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/external_account.py
./services/all_actual_py.txt:5816:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/identity_pool.py
./services/all_actual_py.txt:5817:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/jwt.py
./services/all_actual_py.txt:5818:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_cloud_sdk.py
./services/all_actual_py.txt:5819:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_jwt_async.py
./services/all_actual_py.txt:5820:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/crypt/_helpers.py
./services/all_actual_py.txt:5821:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/crypt/_cryptography_rsa.py
./services/all_actual_py.txt:5822:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/crypt/_python_rsa.py
./services/all_actual_py.txt:5823:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/crypt/rsa.py
./services/all_actual_py.txt:5824:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/crypt/es256.py
./services/all_actual_py.txt:5825:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/crypt/__init__.py
./services/all_actual_py.txt:5826:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/crypt/base.py
./services/all_actual_py.txt:5827:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/api_key.py
./services/all_actual_py.txt:5828:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_exponential_backoff.py
./services/all_actual_py.txt:5829:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_default.py
./services/all_actual_py.txt:5842:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/api/auth_pb2.py
./services/all_actual_py.txt:5849:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/api/metric_pb2.py
./services/all_actual_py.txt:5863:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/_client_async.py
./services/all_actual_py.txt:5864:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/id_token.py
./services/all_actual_py.txt:5865:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/_client.py
./services/all_actual_py.txt:5866:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/webauthn_types.py
./services/all_actual_py.txt:5867:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/credentials.py
./services/all_actual_py.txt:5868:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/_id_token_async.py
./services/all_actual_py.txt:5869:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/reauth.py
./services/all_actual_py.txt:5870:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/_service_account_async.py
./services/all_actual_py.txt:5871:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/challenges.py
./services/all_actual_py.txt:5872:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/webauthn_handler_factory.py
./services/all_actual_py.txt:5873:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/__init__.py
./services/all_actual_py.txt:5874:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/_credentials_async.py
./services/all_actual_py.txt:5875:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/gdch_credentials.py
./services/all_actual_py.txt:5876:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/webauthn_handler.py
./services/all_actual_py.txt:5877:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/sts.py
./services/all_actual_py.txt:5878:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/utils.py
./services/all_actual_py.txt:5879:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/service_account.py
./services/all_actual_py.txt:5880:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/_reauth_async.py
./services/all_actual_py.txt:5889:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/gapic/metadata/gapic_metadata_pb2.py
./services/all_actual_py.txt:5900:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/protobuf/message_factory.py
./services/all_actual_py.txt:5924:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/protobuf/internal/message_listener.py
./services/all_actual_py.txt:5927:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/protobuf/message.py
./services/all_actual_py.txt:6026:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/httpx/_auth.py
./services/all_actual_py.txt:6236:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/uvicorn/middleware/message_logger.py
./services/all_actual_py.txt:6290:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/fastapi/security/oauth2.py
./services/all_actual_py.txt:6356:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_actual_py.txt:6381:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py
./services/all_actual_py.txt:6447:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_actual_py.txt:6626:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/languages.py
./services/all_actual_py.txt:6627:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/__init__.py
./services/all_actual_py.txt:6686:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_actual_py.txt:6687:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_actual_py.txt:6688:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_actual_py.txt:6689:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_actual_py.txt:6690:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_actual_py.txt:6691:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_actual_py.txt:6692:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_actual_py.txt:6693:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_actual_py.txt:6699:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_actual_py.txt:6703:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_actual_py.txt:6716:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_actual_py.txt:6717:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_legacy.py
./services/all_actual_py.txt:6720:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_actual_py.txt:6872:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/anyio/streams/memory.py
./services/all_actual_py.txt:6888:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/starlette/middleware/authentication.py
./services/all_actual_py.txt:6899:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/starlette/authentication.py
./services/all_actual_py.txt:7150:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/uvicorn/middleware/message_logger.py
./services/all_actual_py.txt:7204:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py
./services/all_actual_py.txt:7271:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_actual_py.txt:7296:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py
./services/all_actual_py.txt:7362:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_actual_py.txt:7541:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/languages.py
./services/all_actual_py.txt:7542:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/__init__.py
./services/all_actual_py.txt:7601:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_actual_py.txt:7602:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_actual_py.txt:7603:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_actual_py.txt:7604:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_actual_py.txt:7605:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_actual_py.txt:7606:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_actual_py.txt:7607:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_actual_py.txt:7608:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_actual_py.txt:7614:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_actual_py.txt:7618:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_actual_py.txt:7631:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_actual_py.txt:7632:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_legacy.py
./services/all_actual_py.txt:7635:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_actual_py.txt:7798:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/anyio/streams/memory.py
./services/all_actual_py.txt:7814:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/starlette/middleware/authentication.py
./services/all_actual_py.txt:7825:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/starlette/authentication.py
./services/all_actual_py.txt:7841:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/httpx/_auth.py
./services/all_actual_py.txt:7867:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/chardet/metadata/languages.py
./services/all_actual_py.txt:7868:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/chardet/metadata/__init__.py
./services/all_actual_py.txt:7919:/home/ms-jarvis/msjarvis-rebuild/services/fix_judge_authentic.py
./services/all_actual_py.txt:7939:/home/ms-jarvis/msjarvis-rebuild/services/method_tracking_service.py
./services/all_actual_py.txt:8242:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/huggingface_hub/utils/_auth.py
./services/all_actual_py.txt:8269:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/huggingface_hub/_oauth.py
./services/all_actual_py.txt:8285:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/huggingface_hub/cli/auth.py
./services/all_actual_py.txt:8330:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/websockets/legacy/auth.py
./services/all_actual_py.txt:8339:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/websockets/auth.py
./services/all_actual_py.txt:8349:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/websockets/asyncio/messages.py
./services/all_actual_py.txt:8356:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/websockets/sync/messages.py
./services/all_actual_py.txt:8387:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/wheel/metadata.py
./services/all_actual_py.txt:8439:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests/auth.py
./services/all_actual_py.txt:8448:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/redis/auth/__init__.py
./services/all_actual_py.txt:8449:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/redis/auth/token_manager.py
./services/all_actual_py.txt:8450:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/redis/auth/err.py
./services/all_actual_py.txt:8451:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/redis/auth/idp.py
./services/all_actual_py.txt:8452:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/redis/auth/token.py
./services/all_actual_py.txt:8759:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/_lazy/metrics.py
./services/all_actual_py.txt:9340:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/_inductor/memory.py
./services/all_actual_py.txt:9386:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/_inductor/codegen/memory_planning.py
./services/all_actual_py.txt:9479:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/_inductor/metrics.py
./services/all_actual_py.txt:9558:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/distributed/elastic/metrics/api.py
./services/all_actual_py.txt:9559:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/distributed/elastic/metrics/__init__.py
./services/all_actual_py.txt:9589:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/distributed/checkpoint/metadata.py
./services/all_actual_py.txt:9735:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/distributed/_shard/sharded_tensor/metadata.py
./services/all_actual_py.txt:9749:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/distributed/_shard/metadata.py
./services/all_actual_py.txt:9845:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py
./services/all_actual_py.txt:9846:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/distributed/_tools/memory_tracker.py
./services/all_actual_py.txt:9866:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/_subclasses/meta_utils.py
./services/all_actual_py.txt:10041:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/nn/utils/memory_format.py
./services/all_actual_py.txt:10311:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/_dynamo/metrics_context.py
./services/all_actual_py.txt:10356:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/fx/experimental/merge_matmul.py
./services/all_actual_py.txt:10358:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/fx/experimental/meta_tracer.py
./services/all_actual_py.txt:10416:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/accelerator/memory.py
./services/all_actual_py.txt:10472:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/mtia/memory.py
./services/all_actual_py.txt:10615:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/cuda/memory.py
./services/all_actual_py.txt:10659:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/xpu/memory.py
./services/all_actual_py.txt:10746:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/grpc/_auth.py
./services/all_actual_py.txt:11095:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/networkx/algorithms/threshold.py
./services/all_actual_py.txt:11127:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/networkx/algorithms/tests/test_threshold.py
./services/all_actual_py.txt:11651:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/joint.py
./services/all_actual_py.txt:11652:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/linearize.py
./services/all_actual_py.txt:11653:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/models.py
./services/all_actual_py.txt:11654:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/lagrange.py
./services/all_actual_py.txt:11655:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_rigidbody.py
./services/all_actual_py.txt:11656:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_actuator.py
./services/all_actual_py.txt:11657:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane3.py
./services/all_actual_py.txt:11658:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_body.py
./services/all_actual_py.txt:11659:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_system_class.py
./services/all_actual_py.txt:11660:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_loads.py
./services/all_actual_py.txt:11661:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane4.py
./services/all_actual_py.txt:11662:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane5.py
./services/all_actual_py.txt:11663:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_models.py
./services/all_actual_py.txt:11664:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_method.py
./services/all_actual_py.txt:11665:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_wrapping_geometry.py
./services/all_actual_py.txt:11666:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_lagrange2.py
./services/all_actual_py.txt:11667:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_linearity_of_velocity_constraints.py
./services/all_actual_py.txt:11668:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_system.py
./services/all_actual_py.txt:11669:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_functions.py
./services/all_actual_py.txt:11670:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_inertia.py
./services/all_actual_py.txt:11671:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/__init__.py
./services/all_actual_py.txt:11672:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_pathway.py
./services/all_actual_py.txt:11673:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_lagrange.py
./services/all_actual_py.txt:11674:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane2.py
./services/all_actual_py.txt:11675:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_particle.py
./services/all_actual_py.txt:11676:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_joint.py
./services/all_actual_py.txt:11677:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_linearize.py
./services/all_actual_py.txt:11678:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane.py
./services/all_actual_py.txt:11679:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_jointsmethod.py
./services/all_actual_py.txt:11680:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/jointsmethod.py
./services/all_actual_py.txt:11681:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/rigidbody.py
./services/all_actual_py.txt:11682:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/body_base.py
./services/all_actual_py.txt:11683:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/loads.py
./services/all_actual_py.txt:11684:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/pathway.py
./services/all_actual_py.txt:11685:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/__init__.py
./services/all_actual_py.txt:11686:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/inertia.py
./services/all_actual_py.txt:11687:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/particle.py
./services/all_actual_py.txt:11688:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/method.py
./services/all_actual_py.txt:11689:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/body.py
./services/all_actual_py.txt:11690:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/kane.py
./services/all_actual_py.txt:11691:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/system.py
./services/all_actual_py.txt:11692:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/wrapping_geometry.py
./services/all_actual_py.txt:11693:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/actuator.py
./services/all_actual_py.txt:11694:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/functions.py
./services/all_actual_py.txt:11725:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/optics/medium.py
./services/all_actual_py.txt:12390:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/integrals/meijerint.py
./services/all_actual_py.txt:12425:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/integrals/meijerint_doc.py
./services/all_actual_py.txt:12873:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/utilities/memoization.py
./services/all_actual_py.txt:12918:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/oauth2_session.py
./services/all_actual_py.txt:12919:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/slack.py
./services/all_actual_py.txt:12920:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/facebook.py
./services/all_actual_py.txt:12921:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/plentymarkets.py
./services/all_actual_py.txt:12922:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/ebay.py
./services/all_actual_py.txt:12923:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/__init__.py
./services/all_actual_py.txt:12924:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/douban.py
./services/all_actual_py.txt:12925:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/instagram.py
./services/all_actual_py.txt:12926:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/mailchimp.py
./services/all_actual_py.txt:12927:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/fitbit.py
./services/all_actual_py.txt:12928:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/weibo.py
./services/all_actual_py.txt:12929:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/oauth1_auth.py
./services/all_actual_py.txt:12930:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/__init__.py
./services/all_actual_py.txt:12931:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/oauth2_auth.py
./services/all_actual_py.txt:12932:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/oauth1_session.py
./services/all_actual_py.txt:13296:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/onnxruntime/transformers/metrics.py
./services/all_actual_py.txt:13461:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/uvicorn/middleware/message_logger.py
./services/all_actual_py.txt:13504:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/prometheus_client/metrics_core.py
./services/all_actual_py.txt:13523:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/prometheus_client/metrics.py
./services/all_actual_py.txt:13593:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/fastapi/security/oauth2.py
./services/all_actual_py.txt:13668:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_actual_py.txt:13723:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_actual_py.txt:13816:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_vendor/packaging/metadata.py
./services/all_actual_py.txt:13895:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_actual_py.txt:13896:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_actual_py.txt:13897:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_actual_py.txt:13898:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_actual_py.txt:13899:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_actual_py.txt:13900:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_actual_py.txt:13901:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_actual_py.txt:13902:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_actual_py.txt:13908:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_actual_py.txt:13912:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_actual_py.txt:13924:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_actual_py.txt:13926:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_actual_py.txt:14270:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pygments/lexers/meson.py
./services/all_actual_py.txt:14544:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/kubernetes/client/api/authorization_v1_api.py
./services/all_actual_py.txt:14550:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/kubernetes/client/api/rbac_authorization_api.py
./services/all_actual_py.txt:14554:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/kubernetes/client/api/authentication_v1_api.py
./services/all_actual_py.txt:14562:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/kubernetes/client/api/authorization_api.py
./services/all_actual_py.txt:14570:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/kubernetes/client/api/rbac_authorization_v1_api.py
./services/all_actual_py.txt:14580:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/kubernetes/client/api/authentication_api.py
./services/all_actual_py.txt:14824:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/kubernetes/client/models/authentication_v1_token_request.py
./services/all_actual_py.txt:15336:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/rich/measure.py
./services/all_actual_py.txt:15827:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_align.py
./services/all_actual_py.txt:15828:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_join.py
./services/all_actual_py.txt:15829:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_asfreq.py
./services/all_actual_py.txt:15830:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_dtypes.py
./services/all_actual_py.txt:15831:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_reset_index.py
./services/all_actual_py.txt:15832:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_cov_corr.py
./services/all_actual_py.txt:15833:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_astype.py
./services/all_actual_py.txt:15834:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_tz_localize.py
./services/all_actual_py.txt:15835:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_values.py
./services/all_actual_py.txt:15836:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_drop.py
./services/all_actual_py.txt:15837:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_set_index.py
./services/all_actual_py.txt:15838:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_isetitem.py
./services/all_actual_py.txt:15839:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_swapaxes.py
./services/all_actual_py.txt:15840:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_to_numpy.py
./services/all_actual_py.txt:15841:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_nlargest.py
./services/all_actual_py.txt:15842:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_copy.py
./services/all_actual_py.txt:15843:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_filter.py
./services/all_actual_py.txt:15844:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_add_prefix_suffix.py
./services/all_actual_py.txt:15845:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_sample.py
./services/all_actual_py.txt:15846:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_matmul.py
./services/all_actual_py.txt:15847:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_compare.py
./services/all_actual_py.txt:15848:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_clip.py
./services/all_actual_py.txt:15849:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_explode.py
./services/all_actual_py.txt:15850:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_pop.py
./services/all_actual_py.txt:15851:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_replace.py
./services/all_actual_py.txt:15852:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_to_records.py
./services/all_actual_py.txt:15853:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_first_valid_index.py
./services/all_actual_py.txt:15854:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_update.py
./services/all_actual_py.txt:15855:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_to_timestamp.py
./services/all_actual_py.txt:15856:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_rank.py
./services/all_actual_py.txt:15857:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_rename_axis.py
./services/all_actual_py.txt:15858:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_to_period.py
./services/all_actual_py.txt:15859:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_swaplevel.py
./services/all_actual_py.txt:15860:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_head_tail.py
./services/all_actual_py.txt:15861:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_map.py
./services/all_actual_py.txt:15862:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_tz_convert.py
./services/all_actual_py.txt:15863:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_to_dict_of_blocks.py
./services/all_actual_py.txt:15864:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_truncate.py
./services/all_actual_py.txt:15865:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_droplevel.py
./services/all_actual_py.txt:15866:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_iterrows.py
./services/all_actual_py.txt:15867:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_count.py
./services/all_actual_py.txt:15868:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_drop_duplicates.py
./services/all_actual_py.txt:15869:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_reorder_levels.py
./services/all_actual_py.txt:15870:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_at_time.py
./services/all_actual_py.txt:15871:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_assign.py
./services/all_actual_py.txt:15872:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_pipe.py
./services/all_actual_py.txt:15873:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_transpose.py
./services/all_actual_py.txt:15874:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_size.py
./services/all_actual_py.txt:15875:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_select_dtypes.py
./services/all_actual_py.txt:15876:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_describe.py
./services/all_actual_py.txt:15877:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_equals.py
./services/all_actual_py.txt:15878:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_isin.py
./services/all_actual_py.txt:15879:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_value_counts.py
./services/all_actual_py.txt:15880:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_rename.py
./services/all_actual_py.txt:15881:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_sort_values.py
./services/all_actual_py.txt:15882:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_quantile.py
./services/all_actual_py.txt:15883:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_to_csv.py
./services/all_actual_py.txt:15884:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_get_numeric_data.py
./services/all_actual_py.txt:15885:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_duplicated.py
./services/all_actual_py.txt:15886:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/__init__.py
./services/all_actual_py.txt:15887:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_combine_first.py
./services/all_actual_py.txt:15888:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_infer_objects.py
./services/all_actual_py.txt:15889:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_dropna.py
./services/all_actual_py.txt:15890:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_set_axis.py
./services/all_actual_py.txt:15891:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_fillna.py
./services/all_actual_py.txt:15892:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_shift.py
./services/all_actual_py.txt:15893:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_round.py
./services/all_actual_py.txt:15894:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_interpolate.py
./services/all_actual_py.txt:15895:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_is_homogeneous_dtype.py
./services/all_actual_py.txt:15896:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_convert_dtypes.py
./services/all_actual_py.txt:15897:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_combine.py
./services/all_actual_py.txt:15898:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_between_time.py
./services/all_actual_py.txt:15899:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_sort_index.py
./services/all_actual_py.txt:15900:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_first_and_last.py
./services/all_actual_py.txt:15901:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_reindex_like.py
./services/all_actual_py.txt:15902:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_pct_change.py
./services/all_actual_py.txt:15903:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_diff.py
./services/all_actual_py.txt:15904:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_to_dict.py
./services/all_actual_py.txt:15905:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_asof.py
./services/all_actual_py.txt:15906:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_info.py
./services/all_actual_py.txt:15907:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_dot.py
./services/all_actual_py.txt:15908:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_reindex.py
./services/all_actual_py.txt:15960:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_align.py
./services/all_actual_py.txt:15961:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_dtypes.py
./services/all_actual_py.txt:15962:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_reset_index.py
./services/all_actual_py.txt:15963:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_cov_corr.py
./services/all_actual_py.txt:15964:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_astype.py
./services/all_actual_py.txt:15965:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_tz_localize.py
./services/all_actual_py.txt:15966:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_values.py
./services/all_actual_py.txt:15967:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_drop.py
./services/all_actual_py.txt:15968:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_is_monotonic.py
./services/all_actual_py.txt:15969:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_to_numpy.py
./services/all_actual_py.txt:15970:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_nlargest.py
./services/all_actual_py.txt:15971:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_copy.py
./services/all_actual_py.txt:15972:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_view.py
./services/all_actual_py.txt:15973:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_add_prefix_suffix.py
./services/all_actual_py.txt:15974:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_matmul.py
./services/all_actual_py.txt:15975:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_compare.py
./services/all_actual_py.txt:15976:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_clip.py
./services/all_actual_py.txt:15977:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_explode.py
./services/all_actual_py.txt:15978:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_pop.py
./services/all_actual_py.txt:15979:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_argsort.py
./services/all_actual_py.txt:15980:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_replace.py
./services/all_actual_py.txt:15981:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_between.py
./services/all_actual_py.txt:15982:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_update.py
./services/all_actual_py.txt:15983:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_rank.py
./services/all_actual_py.txt:15984:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_rename_axis.py
./services/all_actual_py.txt:15985:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_unstack.py
./services/all_actual_py.txt:15986:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_head_tail.py
./services/all_actual_py.txt:15987:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_map.py
./services/all_actual_py.txt:15988:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_truncate.py
./services/all_actual_py.txt:15989:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_unique.py
./services/all_actual_py.txt:15990:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_count.py
./services/all_actual_py.txt:15991:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_drop_duplicates.py
./services/all_actual_py.txt:15992:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_set_name.py
./services/all_actual_py.txt:15993:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_searchsorted.py
./services/all_actual_py.txt:15994:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_size.py
./services/all_actual_py.txt:15995:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_describe.py
./services/all_actual_py.txt:15996:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_equals.py
./services/all_actual_py.txt:15997:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_isin.py
./services/all_actual_py.txt:15998:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_value_counts.py
./services/all_actual_py.txt:15999:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_rename.py
./services/all_actual_py.txt:16000:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_sort_values.py
./services/all_actual_py.txt:16001:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_quantile.py
./services/all_actual_py.txt:16002:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_to_csv.py
./services/all_actual_py.txt:16003:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_get_numeric_data.py
./services/all_actual_py.txt:16004:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_duplicated.py
./services/all_actual_py.txt:16005:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_isna.py
./services/all_actual_py.txt:16006:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/__init__.py
./services/all_actual_py.txt:16007:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_combine_first.py
./services/all_actual_py.txt:16008:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_infer_objects.py
./services/all_actual_py.txt:16009:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_dropna.py
./services/all_actual_py.txt:16010:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_tolist.py
./services/all_actual_py.txt:16011:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_to_frame.py
./services/all_actual_py.txt:16012:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_fillna.py
./services/all_actual_py.txt:16013:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_round.py
./services/all_actual_py.txt:16014:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_interpolate.py
./services/all_actual_py.txt:16015:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_case_when.py
./services/all_actual_py.txt:16016:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_convert_dtypes.py
./services/all_actual_py.txt:16017:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_combine.py
./services/all_actual_py.txt:16018:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_is_unique.py
./services/all_actual_py.txt:16019:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_sort_index.py
./services/all_actual_py.txt:16020:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_reindex_like.py
./services/all_actual_py.txt:16021:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_repeat.py
./services/all_actual_py.txt:16022:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_pct_change.py
./services/all_actual_py.txt:16023:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_autocorr.py
./services/all_actual_py.txt:16024:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_diff.py
./services/all_actual_py.txt:16025:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_to_dict.py
./services/all_actual_py.txt:16026:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_asof.py
./services/all_actual_py.txt:16027:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_nunique.py
./services/all_actual_py.txt:16028:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_item.py
./services/all_actual_py.txt:16029:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_info.py
./services/all_actual_py.txt:16030:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_reindex.py
./services/all_actual_py.txt:16080:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timedelta/methods/__init__.py
./services/all_actual_py.txt:16081:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timedelta/methods/test_round.py
./services/all_actual_py.txt:16082:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timedelta/methods/test_as_unit.py
./services/all_actual_py.txt:16089:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_tz_localize.py
./services/all_actual_py.txt:16090:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_normalize.py
./services/all_actual_py.txt:16091:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_replace.py
./services/all_actual_py.txt:16092:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_tz_convert.py
./services/all_actual_py.txt:16093:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_timestamp_method.py
./services/all_actual_py.txt:16094:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/__init__.py
./services/all_actual_py.txt:16095:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_round.py
./services/all_actual_py.txt:16096:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_to_julian_date.py
./services/all_actual_py.txt:16097:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_to_pydatetime.py
./services/all_actual_py.txt:16098:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_as_unit.py
./services/all_actual_py.txt:16170:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_merge_asof.py
./services/all_actual_py.txt:16171:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_join.py
./services/all_actual_py.txt:16172:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_merge_ordered.py
./services/all_actual_py.txt:16173:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_merge_index_as_string.py
./services/all_actual_py.txt:16174:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_multi.py
./services/all_actual_py.txt:16175:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_merge.py
./services/all_actual_py.txt:16176:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/__init__.py
./services/all_actual_py.txt:16177:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_merge_cross.py
./services/all_actual_py.txt:16367:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_is_monotonic.py
./services/all_actual_py.txt:16368:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_corrwith.py
./services/all_actual_py.txt:16369:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_sample.py
./services/all_actual_py.txt:16370:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_rank.py
./services/all_actual_py.txt:16371:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_skew.py
./services/all_actual_py.txt:16372:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_size.py
./services/all_actual_py.txt:16373:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_describe.py
./services/all_actual_py.txt:16374:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_value_counts.py
./services/all_actual_py.txt:16375:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_quantile.py
./services/all_actual_py.txt:16376:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/__init__.py
./services/all_actual_py.txt:16377:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_nlargest_nsmallest.py
./services/all_actual_py.txt:16378:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_groupby_shift_diff.py
./services/all_actual_py.txt:16379:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_nth.py
./services/all_actual_py.txt:16464:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/timedeltas/methods/test_astype.py
./services/all_actual_py.txt:16465:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/timedeltas/methods/test_insert.py
./services/all_actual_py.txt:16466:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/timedeltas/methods/__init__.py
./services/all_actual_py.txt:16467:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/timedeltas/methods/test_fillna.py
./services/all_actual_py.txt:16468:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/timedeltas/methods/test_shift.py
./services/all_actual_py.txt:16469:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/timedeltas/methods/test_factorize.py
./services/all_actual_py.txt:16470:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/timedeltas/methods/test_repeat.py
./services/all_actual_py.txt:16532:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_astype.py
./services/all_actual_py.txt:16533:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_tz_localize.py
./services/all_actual_py.txt:16534:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_to_series.py
./services/all_actual_py.txt:16535:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_normalize.py
./services/all_actual_py.txt:16536:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_to_period.py
./services/all_actual_py.txt:16537:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_map.py
./services/all_actual_py.txt:16538:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_tz_convert.py
./services/all_actual_py.txt:16539:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_unique.py
./services/all_actual_py.txt:16540:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_isocalendar.py
./services/all_actual_py.txt:16541:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_delete.py
./services/all_actual_py.txt:16542:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_resolution.py
./services/all_actual_py.txt:16543:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_insert.py
./services/all_actual_py.txt:16544:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/__init__.py
./services/all_actual_py.txt:16545:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_snap.py
./services/all_actual_py.txt:16546:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_to_frame.py
./services/all_actual_py.txt:16547:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_fillna.py
./services/all_actual_py.txt:16548:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_shift.py
./services/all_actual_py.txt:16549:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_round.py
./services/all_actual_py.txt:16550:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_to_julian_date.py
./services/all_actual_py.txt:16551:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_factorize.py
./services/all_actual_py.txt:16552:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_repeat.py
./services/all_actual_py.txt:16553:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_to_pydatetime.py
./services/all_actual_py.txt:16554:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_asof.py
./services/all_actual_py.txt:16626:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_asfreq.py
./services/all_actual_py.txt:16627:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_astype.py
./services/all_actual_py.txt:16628:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_to_timestamp.py
./services/all_actual_py.txt:16629:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_insert.py
./services/all_actual_py.txt:16630:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/__init__.py
./services/all_actual_py.txt:16631:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_fillna.py
./services/all_actual_py.txt:16632:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_shift.py
./services/all_actual_py.txt:16633:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_is_full.py
./services/all_actual_py.txt:16634:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_factorize.py
./services/all_actual_py.txt:16635:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_repeat.py
./services/all_actual_py.txt:16708:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/extension/base/methods.py
./services/all_actual_py.txt:16753:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/core/methods/describe.py
./services/all_actual_py.txt:16754:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/core/methods/to_dict.py
./services/all_actual_py.txt:16755:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/core/methods/selectn.py
./services/all_actual_py.txt:16756:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/core/methods/__init__.py
./services/all_actual_py.txt:16791:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/core/reshape/merge.py
./services/all_actual_py.txt:16797:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/core/reshape/melt.py
./services/all_actual_py.txt:16820:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/core/_numba/kernels/mean_.py
./services/all_actual_py.txt:17183:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/scipy/_lib/pyprima/common/message.py
./services/all_actual_py.txt:17929:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/scipy/ndimage/measurements.py
./services/all_actual_py.txt:18001:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/export/__init__.py
./services/all_actual_py.txt:18002:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement.py
./services/all_actual_py.txt:18003:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/view.py
./services/all_actual_py.txt:18004:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement_consumer.py
./services/all_actual_py.txt:18005:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/export/__init__.py
./services/all_actual_py.txt:18006:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/_view_instrument_match.py
./services/all_actual_py.txt:18007:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/aggregation.py
./services/all_actual_py.txt:18008:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exceptions.py
./services/all_actual_py.txt:18009:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/instrument.py
./services/all_actual_py.txt:18010:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py
./services/all_actual_py.txt:18011:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/__init__.py
./services/all_actual_py.txt:18012:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/buckets.py
./services/all_actual_py.txt:18013:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/exponent_mapping.py
./services/all_actual_py.txt:18014:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/errors.py
./services/all_actual_py.txt:18015:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/logarithm_mapping.py
./services/all_actual_py.txt:18016:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/__init__.py
./services/all_actual_py.txt:18017:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/ieee_754.py
./services/all_actual_py.txt:18018:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/point.py
./services/all_actual_py.txt:18019:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/metric_reader_storage.py
./services/all_actual_py.txt:18020:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar_filter.py
./services/all_actual_py.txt:18021:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar_reservoir.py
./services/all_actual_py.txt:18022:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/__init__.py
./services/all_actual_py.txt:18023:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar.py
./services/all_actual_py.txt:18024:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/sdk_configuration.py
./services/all_actual_py.txt:18025:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/view/__init__.py
./services/all_actual_py.txt:18026:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/__init__.py
./services/all_actual_py.txt:18034:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/trace/_sampling_experimental/_parent_threshold.py
./services/all_actual_py.txt:18058:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/metrics/db_metrics.py
./services/all_actual_py.txt:18059:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/metrics/__init__.py
./services/all_actual_py.txt:18060:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/metrics/http_metrics.py
./services/all_actual_py.txt:18064:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/dns_metrics.py
./services/all_actual_py.txt:18065:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cicd_metrics.py
./services/all_actual_py.txt:18066:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/vcs_metrics.py
./services/all_actual_py.txt:18067:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/db_metrics.py
./services/all_actual_py.txt:18068:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/rpc_metrics.py
./services/all_actual_py.txt:18069:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cpu_metrics.py
./services/all_actual_py.txt:18070:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cpython_metrics.py
./services/all_actual_py.txt:18071:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/gen_ai_metrics.py
./services/all_actual_py.txt:18072:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/faas_metrics.py
./services/all_actual_py.txt:18073:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/system_metrics.py
./services/all_actual_py.txt:18074:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/process_metrics.py
./services/all_actual_py.txt:18075:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/otel_metrics.py
./services/all_actual_py.txt:18076:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/messaging_metrics.py
./services/all_actual_py.txt:18077:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/hw_metrics.py
./services/all_actual_py.txt:18078:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/k8s_metrics.py
./services/all_actual_py.txt:18079:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/http_metrics.py
./services/all_actual_py.txt:18080:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py
./services/all_actual_py.txt:18081:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/azure_metrics.py
./services/all_actual_py.txt:18083:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/message_attributes.py
./services/all_actual_py.txt:18143:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/messaging_attributes.py
./services/all_actual_py.txt:18175:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/metric_exporter/__init__.py
./services/all_actual_py.txt:18178:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/common/metrics_encoder.py
./services/all_actual_py.txt:18182:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/common/_internal/metrics_encoder/__init__.py
./services/all_actual_py.txt:18187:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/metrics/_internal/instrument.py
./services/all_actual_py.txt:18188:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/metrics/_internal/__init__.py
./services/all_actual_py.txt:18189:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/metrics/_internal/observation.py
./services/all_actual_py.txt:18190:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/metrics/__init__.py
./services/all_actual_py.txt:18203:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/proto/metrics/v1/metrics_pb2.py
./services/all_actual_py.txt:18204:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/proto/metrics/v1/__init__.py
./services/all_actual_py.txt:18205:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/proto/metrics/__init__.py
./services/all_actual_py.txt:18216:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/metrics_service_pb2_grpc.py
./services/all_actual_py.txt:18217:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/metrics_service_pb2.py
./services/all_actual_py.txt:18218:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/__init__.py
./services/all_actual_py.txt:18219:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/__init__.py
./services/all_actual_py.txt:18263:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/packaging/metadata.py
./services/all_actual_py.txt:18320:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/jinja2/meta.py
./services/all_actual_py.txt:18404:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/model_selection/tests/test_classification_threshold.py
./services/all_actual_py.txt:18414:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/model_selection/_classification_threshold.py
./services/all_actual_py.txt:18491:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/tests/metadata_routing_common.py
./services/all_actual_py.txt:18644:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/utils/metadata_routing.py
./services/all_actual_py.txt:18647:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/utils/metaestimators.py
./services/all_actual_py.txt:18708:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_classification.py
./services/all_actual_py.txt:18709:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_scorer.py
./services/all_actual_py.txt:18710:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_base.py
./services/all_actual_py.txt:18711:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_pairwise.py
./services/all_actual_py.txt:18712:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_common.py
./services/all_actual_py.txt:18713:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_ranking.py
./services/all_actual_py.txt:18714:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_regression.py
./services/all_actual_py.txt:18715:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_classification.py
./services/all_actual_py.txt:18716:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_dist_metrics.py
./services/all_actual_py.txt:18717:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/__init__.py
./services/all_actual_py.txt:18718:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_score_objects.py
./services/all_actual_py.txt:18719:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_pairwise_distances_reduction.py
./services/all_actual_py.txt:18720:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_ranking.py
./services/all_actual_py.txt:18721:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_regression.py
./services/all_actual_py.txt:18722:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/pairwise.py
./services/all_actual_py.txt:18723:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/_bicluster.py
./services/all_actual_py.txt:18724:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/tests/test_supervised.py
./services/all_actual_py.txt:18725:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/tests/test_common.py
./services/all_actual_py.txt:18726:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/tests/test_unsupervised.py
./services/all_actual_py.txt:18727:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/tests/test_bicluster.py
./services/all_actual_py.txt:18728:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/tests/__init__.py
./services/all_actual_py.txt:18729:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/_supervised.py
./services/all_actual_py.txt:18730:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/__init__.py
./services/all_actual_py.txt:18731:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/_unsupervised.py
./services/all_actual_py.txt:18732:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/__init__.py
./services/all_actual_py.txt:18733:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/tests/test_confusion_matrix_display.py
./services/all_actual_py.txt:18734:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/tests/test_det_curve_display.py
./services/all_actual_py.txt:18735:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/tests/test_roc_curve_display.py
./services/all_actual_py.txt:18736:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/tests/test_common_curve_display.py
./services/all_actual_py.txt:18737:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/tests/test_predict_error_display.py
./services/all_actual_py.txt:18738:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/tests/__init__.py
./services/all_actual_py.txt:18739:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/tests/test_precision_recall_display.py
./services/all_actual_py.txt:18740:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/regression.py
./services/all_actual_py.txt:18741:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/det_curve.py
./services/all_actual_py.txt:18742:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/roc_curve.py
./services/all_actual_py.txt:18743:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/precision_recall_curve.py
./services/all_actual_py.txt:18744:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/__init__.py
./services/all_actual_py.txt:18745:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/confusion_matrix.py
./services/all_actual_py.txt:18746:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_pairwise_distances_reduction/_dispatcher.py
./services/all_actual_py.txt:18747:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_pairwise_distances_reduction/__init__.py
./services/all_actual_py.txt:18816:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/feature_selection/tests/test_variance_threshold.py
./services/all_actual_py.txt:18819:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/feature_selection/_variance_threshold.py
./services/all_actual_py.txt:18989:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/setuptools/_vendor/wheel/metadata.py
./services/all_actual_py.txt:19025:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/setuptools/_vendor/typeguard/_suppression.py
./services/all_actual_py.txt:19052:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/setuptools/_vendor/packaging/metadata.py
./services/all_actual_py.txt:19321:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/prometheus_fastapi_instrumentator/metrics.py
./services/all_actual_py.txt:19323:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/errors.py
./services/all_actual_py.txt:19324:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/pre_configured.py
./services/all_actual_py.txt:19325:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/revocation.py
./services/all_actual_py.txt:19326:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/resource.py
./services/all_actual_py.txt:19327:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/metadata.py
./services/all_actual_py.txt:19328:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/__init__.py
./services/all_actual_py.txt:19329:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/authorization.py
./services/all_actual_py.txt:19330:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/introspect.py
./services/all_actual_py.txt:19331:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/base.py
./services/all_actual_py.txt:19332:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/token.py
./services/all_actual_py.txt:19333:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/mobile_application.py
./services/all_actual_py.txt:19334:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/legacy_application.py
./services/all_actual_py.txt:19335:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/backend_application.py
./services/all_actual_py.txt:19336:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/service_application.py
./services/all_actual_py.txt:19337:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/__init__.py
./services/all_actual_py.txt:19338:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/web_application.py
./services/all_actual_py.txt:19339:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/base.py
./services/all_actual_py.txt:19340:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/parameters.py
./services/all_actual_py.txt:19341:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/resource_owner_password_credentials.py
./services/all_actual_py.txt:19342:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/__init__.py
./services/all_actual_py.txt:19343:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/client_credentials.py
./services/all_actual_py.txt:19344:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/implicit.py
./services/all_actual_py.txt:19345:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/refresh_token.py
./services/all_actual_py.txt:19346:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/base.py
./services/all_actual_py.txt:19347:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/authorization_code.py
./services/all_actual_py.txt:19348:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/request_validator.py
./services/all_actual_py.txt:19349:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/__init__.py
./services/all_actual_py.txt:19350:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/utils.py
./services/all_actual_py.txt:19351:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/tokens.py
./services/all_actual_py.txt:19352:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/errors.py
./services/all_actual_py.txt:19353:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/pre_configured.py
./services/all_actual_py.txt:19354:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/__init__.py
./services/all_actual_py.txt:19355:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/device_authorization.py
./services/all_actual_py.txt:19356:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/clients/device.py
./services/all_actual_py.txt:19357:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/clients/__init__.py
./services/all_actual_py.txt:19358:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/grant_types/__init__.py
./services/all_actual_py.txt:19359:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/grant_types/device_code.py
./services/all_actual_py.txt:19360:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/request_validator.py
./services/all_actual_py.txt:19361:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/__init__.py
./services/all_actual_py.txt:19362:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/__init__.py
./services/all_actual_py.txt:19363:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/__init__.py
./services/all_actual_py.txt:19364:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/signature.py
./services/all_actual_py.txt:19365:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/errors.py
./services/all_actual_py.txt:19366:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/pre_configured.py
./services/all_actual_py.txt:19367:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/resource.py
./services/all_actual_py.txt:19368:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/access_token.py
./services/all_actual_py.txt:19369:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/__init__.py
./services/all_actual_py.txt:19370:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/authorization.py
./services/all_actual_py.txt:19371:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/request_token.py
./services/all_actual_py.txt:19372:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/signature_only.py
./services/all_actual_py.txt:19373:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/base.py
./services/all_actual_py.txt:19374:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/parameters.py
./services/all_actual_py.txt:19375:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/request_validator.py
./services/all_actual_py.txt:19376:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/__init__.py
./services/all_actual_py.txt:19377:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/utils.py
./services/all_actual_py.txt:19378:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/uri_validate.py
./services/all_actual_py.txt:19379:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/__init__.py
./services/all_actual_py.txt:19380:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/common.py
./services/all_actual_py.txt:19381:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/signals.py
./services/all_actual_py.txt:19382:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/__init__.py
./services/all_actual_py.txt:19383:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/pre_configured.py
./services/all_actual_py.txt:19384:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/userinfo.py
./services/all_actual_py.txt:19385:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/__init__.py
./services/all_actual_py.txt:19386:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/exceptions.py
./services/all_actual_py.txt:19387:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/dispatchers.py
./services/all_actual_py.txt:19388:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/__init__.py
./services/all_actual_py.txt:19389:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/hybrid.py
./services/all_actual_py.txt:19390:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/implicit.py
./services/all_actual_py.txt:19391:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/refresh_token.py
./services/all_actual_py.txt:19392:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/base.py
./services/all_actual_py.txt:19393:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/authorization_code.py
./services/all_actual_py.txt:19394:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/request_validator.py
./services/all_actual_py.txt:19395:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/__init__.py
./services/all_actual_py.txt:19396:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/tokens.py
./services/all_actual_py.txt:19397:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/__init__.py
./services/all_actual_py.txt:19442:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/aiohttp/client_middleware_digest_auth.py
./services/all_actual_py.txt:19509:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/fsspec/implementations/memory.py
./services/all_actual_py.txt:19541:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/auth/utils/__init__.py
./services/all_actual_py.txt:19542:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py
./services/all_actual_py.txt:19543:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/auth/__init__.py
./services/all_actual_py.txt:19544:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py
./services/all_actual_py.txt:19545:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/auth/simple_rbac_authz/__init__.py
./services/all_actual_py.txt:19565:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/test/auth/test_auth_utils.py
./services/all_actual_py.txt:19608:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/test/client/create_http_client_with_basic_auth.py
./services/all_actual_py.txt:19609:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/test/client/test_database_tenant_auth.py
./services/all_actual_py.txt:19646:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/utils/messageid.py
./services/all_actual_py.txt:19697:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/segment/impl/metadata/sqlite.py
./services/all_actual_py.txt:19870:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/utils/metrics.py
./services/all_actual_py.txt:19907:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/data/metrics/squad_metrics.py
./services/all_actual_py.txt:19908:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/data/metrics/__init__.py
./services/all_actual_py.txt:20519:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/metaclip_2/configuration_metaclip_2.py
./services/all_actual_py.txt:20520:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/metaclip_2/__init__.py
./services/all_actual_py.txt:20521:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/metaclip_2/modeling_metaclip_2.py
./services/all_actual_py.txt:20522:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/metaclip_2/modular_metaclip_2.py
./services/all_actual_py.txt:20634:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/megatron_gpt2/__init__.py
./services/all_actual_py.txt:20635:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/megatron_gpt2/checkpoint_reshaping_and_interoperability.py
./services/all_actual_py.txt:20784:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/megatron_bert/modeling_megatron_bert.py
./services/all_actual_py.txt:20785:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/megatron_bert/__init__.py
./services/all_actual_py.txt:20786:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/megatron_bert/configuration_megatron_bert.py
./services/all_actual_py.txt:21477:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/deprecated/mega/modeling_mega.py
./services/all_actual_py.txt:21478:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/deprecated/mega/configuration_mega.py
./services/all_actual_py.txt:21479:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/deprecated/mega/__init__.py
./services/all_actual_py.txt:21978:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/memory_profiler.py
./services/all_actual_py.txt:22304:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/numpy/_core/memmap.py
./services/all_actual_py.txt:22664:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/anyio/streams/memory.py
./services/all_actual_py.txt:22680:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/starlette/middleware/authentication.py
./services/all_actual_py.txt:22692:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/starlette/authentication.py
./services/all_actual_py.txt:22704:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_refresh_worker.py
./services/all_actual_py.txt:22705:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/compute_engine/credentials.py
./services/all_actual_py.txt:22706:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/compute_engine/_metadata.py
./services/all_actual_py.txt:22707:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/compute_engine/__init__.py
./services/all_actual_py.txt:22708:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_credentials_base.py
./services/all_actual_py.txt:22709:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_oauth2client.py
./services/all_actual_py.txt:22710:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/iam.py
./services/all_actual_py.txt:22711:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/version.py
./services/all_actual_py.txt:22712:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/downscoped.py
./services/all_actual_py.txt:22713:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_helpers.py
./services/all_actual_py.txt:22714:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/external_account_authorized_user.py
./services/all_actual_py.txt:22715:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/impersonated_credentials.py
./services/all_actual_py.txt:22716:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/credentials.py
./services/all_actual_py.txt:22717:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/exceptions.py
./services/all_actual_py.txt:22718:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_default_async.py
./services/all_actual_py.txt:22719:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/aio/_helpers.py
./services/all_actual_py.txt:22720:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/aio/credentials.py
./services/all_actual_py.txt:22721:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/aio/__init__.py
./services/all_actual_py.txt:22722:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/aio/transport/aiohttp.py
./services/all_actual_py.txt:22723:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/aio/transport/__init__.py
./services/all_actual_py.txt:22724:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/aio/transport/sessions.py
./services/all_actual_py.txt:22725:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/aws.py
./services/all_actual_py.txt:22726:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/environment_vars.py
./services/all_actual_py.txt:22727:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_service_account_info.py
./services/all_actual_py.txt:22728:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/app_engine.py
./services/all_actual_py.txt:22729:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/__init__.py
./services/all_actual_py.txt:22730:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_credentials_async.py
./services/all_actual_py.txt:22731:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_constants.py
./services/all_actual_py.txt:22732:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/pluggable.py
./services/all_actual_py.txt:22733:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/metrics.py
./services/all_actual_py.txt:22734:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/_custom_tls_signer.py
./services/all_actual_py.txt:22735:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/grpc.py
./services/all_actual_py.txt:22736:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/mtls.py
./services/all_actual_py.txt:22737:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/__init__.py
./services/all_actual_py.txt:22738:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/_requests_base.py
./services/all_actual_py.txt:22739:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/urllib3.py
./services/all_actual_py.txt:22740:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/_http_client.py
./services/all_actual_py.txt:22741:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/_aiohttp_requests.py
./services/all_actual_py.txt:22742:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/_mtls_helper.py
./services/all_actual_py.txt:22743:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/requests.py
./services/all_actual_py.txt:22744:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/external_account.py
./services/all_actual_py.txt:22745:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/identity_pool.py
./services/all_actual_py.txt:22746:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/jwt.py
./services/all_actual_py.txt:22747:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_cloud_sdk.py
./services/all_actual_py.txt:22748:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_jwt_async.py
./services/all_actual_py.txt:22749:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/crypt/_helpers.py
./services/all_actual_py.txt:22750:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/crypt/_cryptography_rsa.py
./services/all_actual_py.txt:22751:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/crypt/_python_rsa.py
./services/all_actual_py.txt:22752:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/crypt/rsa.py
./services/all_actual_py.txt:22753:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/crypt/es256.py
./services/all_actual_py.txt:22754:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/crypt/__init__.py
./services/all_actual_py.txt:22755:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/crypt/base.py
./services/all_actual_py.txt:22756:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/api_key.py
./services/all_actual_py.txt:22757:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_exponential_backoff.py
./services/all_actual_py.txt:22758:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_default.py
./services/all_actual_py.txt:22771:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/api/auth_pb2.py
./services/all_actual_py.txt:22778:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/api/metric_pb2.py
./services/all_actual_py.txt:22792:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/_client_async.py
./services/all_actual_py.txt:22793:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/id_token.py
./services/all_actual_py.txt:22794:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/_client.py
./services/all_actual_py.txt:22795:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/webauthn_types.py
./services/all_actual_py.txt:22796:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/credentials.py
./services/all_actual_py.txt:22797:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/_id_token_async.py
./services/all_actual_py.txt:22798:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/reauth.py
./services/all_actual_py.txt:22799:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/_service_account_async.py
./services/all_actual_py.txt:22800:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/challenges.py
./services/all_actual_py.txt:22801:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/webauthn_handler_factory.py
./services/all_actual_py.txt:22802:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/__init__.py
./services/all_actual_py.txt:22803:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/_credentials_async.py
./services/all_actual_py.txt:22804:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/gdch_credentials.py
./services/all_actual_py.txt:22805:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/webauthn_handler.py
./services/all_actual_py.txt:22806:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/sts.py
./services/all_actual_py.txt:22807:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/utils.py
./services/all_actual_py.txt:22808:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/service_account.py
./services/all_actual_py.txt:22809:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/_reauth_async.py
./services/all_actual_py.txt:22818:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/gapic/metadata/gapic_metadata_pb2.py
./services/all_actual_py.txt:22830:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/protobuf/message_factory.py
./services/all_actual_py.txt:22854:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/protobuf/internal/message_listener.py
./services/all_actual_py.txt:22857:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/protobuf/message.py
./services/all_actual_py.txt:22986:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/joblib/memory.py
./services/all_actual_py.txt:23029:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/httpx/_auth.py
./services/all_actual_py.txt:23144:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torchgen/api/meta.py
./services/all_actual_py.txt:23356:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/uvicorn/middleware/message_logger.py
./services/all_actual_py.txt:23410:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/fastapi/security/oauth2.py
./services/all_actual_py.txt:23470:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_actual_py.txt:23495:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py
./services/all_actual_py.txt:23561:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_actual_py.txt:23740:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/languages.py
./services/all_actual_py.txt:23741:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/__init__.py
./services/all_actual_py.txt:23800:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_actual_py.txt:23801:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_actual_py.txt:23802:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_actual_py.txt:23803:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_actual_py.txt:23804:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_actual_py.txt:23805:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_actual_py.txt:23806:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_actual_py.txt:23807:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_actual_py.txt:23813:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_actual_py.txt:23817:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_actual_py.txt:23830:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_actual_py.txt:23831:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_legacy.py
./services/all_actual_py.txt:23834:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_actual_py.txt:23986:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/anyio/streams/memory.py
./services/all_actual_py.txt:24002:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/starlette/middleware/authentication.py
./services/all_actual_py.txt:24013:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/starlette/authentication.py
./services/all_actual_py.txt:24094:/home/ms-jarvis/msjarvis-rebuild/services/user_auth_service.py
./services/all_actual_py.txt:24289:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/multiaddr/codecs/memory.py
./services/all_actual_py.txt:24402:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/huggingface_hub/utils/_auth.py
./services/all_actual_py.txt:24429:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/huggingface_hub/_oauth.py
./services/all_actual_py.txt:24444:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/huggingface_hub/cli/auth.py
./services/all_actual_py.txt:24475:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/websockets/legacy/auth.py
./services/all_actual_py.txt:24484:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/websockets/auth.py
./services/all_actual_py.txt:24494:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/websockets/asyncio/messages.py
./services/all_actual_py.txt:24501:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/websockets/sync/messages.py
./services/all_actual_py.txt:24578:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests/auth.py
./services/all_actual_py.txt:24587:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/redis/auth/__init__.py
./services/all_actual_py.txt:24588:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/redis/auth/token_manager.py
./services/all_actual_py.txt:24589:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/redis/auth/err.py
./services/all_actual_py.txt:24590:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/redis/auth/idp.py
./services/all_actual_py.txt:24591:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/redis/auth/token.py
./services/all_actual_py.txt:24712:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/dns/message.py
./services/all_actual_py.txt:25023:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/grpc/_auth.py
./services/all_actual_py.txt:25378:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/joint.py
./services/all_actual_py.txt:25379:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/linearize.py
./services/all_actual_py.txt:25380:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/models.py
./services/all_actual_py.txt:25381:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/lagrange.py
./services/all_actual_py.txt:25382:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_rigidbody.py
./services/all_actual_py.txt:25383:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_actuator.py
./services/all_actual_py.txt:25384:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane3.py
./services/all_actual_py.txt:25385:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_body.py
./services/all_actual_py.txt:25386:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_system_class.py
./services/all_actual_py.txt:25387:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_loads.py
./services/all_actual_py.txt:25388:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane4.py
./services/all_actual_py.txt:25389:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane5.py
./services/all_actual_py.txt:25390:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_models.py
./services/all_actual_py.txt:25391:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_method.py
./services/all_actual_py.txt:25392:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_wrapping_geometry.py
./services/all_actual_py.txt:25393:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_lagrange2.py
./services/all_actual_py.txt:25394:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_linearity_of_velocity_constraints.py
./services/all_actual_py.txt:25395:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_system.py
./services/all_actual_py.txt:25396:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_functions.py
./services/all_actual_py.txt:25397:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_inertia.py
./services/all_actual_py.txt:25398:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/__init__.py
./services/all_actual_py.txt:25399:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_pathway.py
./services/all_actual_py.txt:25400:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_lagrange.py
./services/all_actual_py.txt:25401:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane2.py
./services/all_actual_py.txt:25402:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_particle.py
./services/all_actual_py.txt:25403:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_joint.py
./services/all_actual_py.txt:25404:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_linearize.py
./services/all_actual_py.txt:25405:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane.py
./services/all_actual_py.txt:25406:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_jointsmethod.py
./services/all_actual_py.txt:25407:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/jointsmethod.py
./services/all_actual_py.txt:25408:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/rigidbody.py
./services/all_actual_py.txt:25409:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/body_base.py
./services/all_actual_py.txt:25410:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/loads.py
./services/all_actual_py.txt:25411:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/pathway.py
./services/all_actual_py.txt:25412:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/__init__.py
./services/all_actual_py.txt:25413:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/inertia.py
./services/all_actual_py.txt:25414:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/particle.py
./services/all_actual_py.txt:25415:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/method.py
./services/all_actual_py.txt:25416:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/body.py
./services/all_actual_py.txt:25417:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/kane.py
./services/all_actual_py.txt:25418:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/system.py
./services/all_actual_py.txt:25419:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/wrapping_geometry.py
./services/all_actual_py.txt:25420:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/actuator.py
./services/all_actual_py.txt:25421:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/functions.py
./services/all_actual_py.txt:25452:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/optics/medium.py
./services/all_actual_py.txt:26117:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/integrals/meijerint.py
./services/all_actual_py.txt:26152:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/integrals/meijerint_doc.py
./services/all_actual_py.txt:26600:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/utilities/memoization.py
./services/all_actual_py.txt:26645:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/oauth2_session.py
./services/all_actual_py.txt:26646:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/slack.py
./services/all_actual_py.txt:26647:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/facebook.py
./services/all_actual_py.txt:26648:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/plentymarkets.py
./services/all_actual_py.txt:26649:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/ebay.py
./services/all_actual_py.txt:26650:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/__init__.py
./services/all_actual_py.txt:26651:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/douban.py
./services/all_actual_py.txt:26652:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/instagram.py
./services/all_actual_py.txt:26653:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/mailchimp.py
./services/all_actual_py.txt:26654:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/fitbit.py
./services/all_actual_py.txt:26655:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/weibo.py
./services/all_actual_py.txt:26656:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/oauth1_auth.py
./services/all_actual_py.txt:26657:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/__init__.py
./services/all_actual_py.txt:26658:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/oauth2_auth.py
./services/all_actual_py.txt:26659:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/oauth1_session.py
./services/all_actual_py.txt:27023:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/onnxruntime/transformers/metrics.py
./services/all_actual_py.txt:27090:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/uvicorn/middleware/message_logger.py
./services/all_actual_py.txt:27236:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_actual_py.txt:27291:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_actual_py.txt:27384:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_vendor/packaging/metadata.py
./services/all_actual_py.txt:27463:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_actual_py.txt:27464:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_actual_py.txt:27465:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_actual_py.txt:27466:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_actual_py.txt:27467:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_actual_py.txt:27468:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_actual_py.txt:27469:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_actual_py.txt:27470:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_actual_py.txt:27476:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_actual_py.txt:27480:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_actual_py.txt:27492:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_actual_py.txt:27494:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_actual_py.txt:27838:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pygments/lexers/meson.py
./services/all_actual_py.txt:28109:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/kubernetes/client/api/authorization_v1_api.py
./services/all_actual_py.txt:28115:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/kubernetes/client/api/rbac_authorization_api.py
./services/all_actual_py.txt:28119:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/kubernetes/client/api/authentication_v1_api.py
./services/all_actual_py.txt:28127:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/kubernetes/client/api/authorization_api.py
./services/all_actual_py.txt:28135:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/kubernetes/client/api/rbac_authorization_v1_api.py
./services/all_actual_py.txt:28145:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/kubernetes/client/api/authentication_api.py
./services/all_actual_py.txt:28389:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/kubernetes/client/models/authentication_v1_token_request.py
./services/all_actual_py.txt:28902:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/rich/measure.py
./services/all_actual_py.txt:29011:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/export/__init__.py
./services/all_actual_py.txt:29012:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement.py
./services/all_actual_py.txt:29013:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/view.py
./services/all_actual_py.txt:29014:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement_consumer.py
./services/all_actual_py.txt:29015:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/export/__init__.py
./services/all_actual_py.txt:29016:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/_view_instrument_match.py
./services/all_actual_py.txt:29017:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/aggregation.py
./services/all_actual_py.txt:29018:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exceptions.py
./services/all_actual_py.txt:29019:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/instrument.py
./services/all_actual_py.txt:29020:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py
./services/all_actual_py.txt:29021:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/__init__.py
./services/all_actual_py.txt:29022:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/buckets.py
./services/all_actual_py.txt:29023:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/exponent_mapping.py
./services/all_actual_py.txt:29024:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/errors.py
./services/all_actual_py.txt:29025:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/logarithm_mapping.py
./services/all_actual_py.txt:29026:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/__init__.py
./services/all_actual_py.txt:29027:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/ieee_754.py
./services/all_actual_py.txt:29028:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/point.py
./services/all_actual_py.txt:29029:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/metric_reader_storage.py
./services/all_actual_py.txt:29030:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar_filter.py
./services/all_actual_py.txt:29031:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar_reservoir.py
./services/all_actual_py.txt:29032:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/__init__.py
./services/all_actual_py.txt:29033:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar.py
./services/all_actual_py.txt:29034:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/sdk_configuration.py
./services/all_actual_py.txt:29035:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/view/__init__.py
./services/all_actual_py.txt:29036:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/__init__.py
./services/all_actual_py.txt:29044:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/trace/_sampling_experimental/_parent_threshold.py
./services/all_actual_py.txt:29068:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/metrics/db_metrics.py
./services/all_actual_py.txt:29069:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/metrics/__init__.py
./services/all_actual_py.txt:29070:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/metrics/http_metrics.py
./services/all_actual_py.txt:29074:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/dns_metrics.py
./services/all_actual_py.txt:29075:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cicd_metrics.py
./services/all_actual_py.txt:29076:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/vcs_metrics.py
./services/all_actual_py.txt:29077:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/db_metrics.py
./services/all_actual_py.txt:29078:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/rpc_metrics.py
./services/all_actual_py.txt:29079:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cpu_metrics.py
./services/all_actual_py.txt:29080:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cpython_metrics.py
./services/all_actual_py.txt:29081:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/gen_ai_metrics.py
./services/all_actual_py.txt:29082:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/faas_metrics.py
./services/all_actual_py.txt:29083:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/system_metrics.py
./services/all_actual_py.txt:29084:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/process_metrics.py
./services/all_actual_py.txt:29085:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/otel_metrics.py
./services/all_actual_py.txt:29086:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/messaging_metrics.py
./services/all_actual_py.txt:29087:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/hw_metrics.py
./services/all_actual_py.txt:29088:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/k8s_metrics.py
./services/all_actual_py.txt:29089:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/http_metrics.py
./services/all_actual_py.txt:29090:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py
./services/all_actual_py.txt:29091:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/azure_metrics.py
./services/all_actual_py.txt:29093:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/message_attributes.py
./services/all_actual_py.txt:29153:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/messaging_attributes.py
./services/all_actual_py.txt:29185:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/metric_exporter/__init__.py
./services/all_actual_py.txt:29188:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/common/metrics_encoder.py
./services/all_actual_py.txt:29192:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/common/_internal/metrics_encoder/__init__.py
./services/all_actual_py.txt:29197:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/metrics/_internal/instrument.py
./services/all_actual_py.txt:29198:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/metrics/_internal/__init__.py
./services/all_actual_py.txt:29199:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/metrics/_internal/observation.py
./services/all_actual_py.txt:29200:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/metrics/__init__.py
./services/all_actual_py.txt:29213:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/proto/metrics/v1/metrics_pb2.py
./services/all_actual_py.txt:29214:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/proto/metrics/v1/__init__.py
./services/all_actual_py.txt:29215:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/proto/metrics/__init__.py
./services/all_actual_py.txt:29226:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/metrics_service_pb2_grpc.py
./services/all_actual_py.txt:29227:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/metrics_service_pb2.py
./services/all_actual_py.txt:29228:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/__init__.py
./services/all_actual_py.txt:29229:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/__init__.py
./services/all_actual_py.txt:29273:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pymysql/_auth.py
./services/all_actual_py.txt:29288:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/packaging/metadata.py
./services/all_actual_py.txt:29356:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/errors.py
./services/all_actual_py.txt:29357:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/pre_configured.py
./services/all_actual_py.txt:29358:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/revocation.py
./services/all_actual_py.txt:29359:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/resource.py
./services/all_actual_py.txt:29360:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/metadata.py
./services/all_actual_py.txt:29361:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/__init__.py
./services/all_actual_py.txt:29362:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/authorization.py
./services/all_actual_py.txt:29363:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/introspect.py
./services/all_actual_py.txt:29364:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/base.py
./services/all_actual_py.txt:29365:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/token.py
./services/all_actual_py.txt:29366:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/mobile_application.py
./services/all_actual_py.txt:29367:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/legacy_application.py
./services/all_actual_py.txt:29368:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/backend_application.py
./services/all_actual_py.txt:29369:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/service_application.py
./services/all_actual_py.txt:29370:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/__init__.py
./services/all_actual_py.txt:29371:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/web_application.py
./services/all_actual_py.txt:29372:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/base.py
./services/all_actual_py.txt:29373:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/parameters.py
./services/all_actual_py.txt:29374:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/resource_owner_password_credentials.py
./services/all_actual_py.txt:29375:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/__init__.py
./services/all_actual_py.txt:29376:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/client_credentials.py
./services/all_actual_py.txt:29377:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/implicit.py
./services/all_actual_py.txt:29378:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/refresh_token.py
./services/all_actual_py.txt:29379:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/base.py
./services/all_actual_py.txt:29380:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/authorization_code.py
./services/all_actual_py.txt:29381:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/request_validator.py
./services/all_actual_py.txt:29382:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/__init__.py
./services/all_actual_py.txt:29383:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/utils.py
./services/all_actual_py.txt:29384:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/tokens.py
./services/all_actual_py.txt:29385:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/errors.py
./services/all_actual_py.txt:29386:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/pre_configured.py
./services/all_actual_py.txt:29387:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/__init__.py
./services/all_actual_py.txt:29388:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/device_authorization.py
./services/all_actual_py.txt:29389:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/clients/device.py
./services/all_actual_py.txt:29390:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/clients/__init__.py
./services/all_actual_py.txt:29391:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/grant_types/__init__.py
./services/all_actual_py.txt:29392:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/grant_types/device_code.py
./services/all_actual_py.txt:29393:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/request_validator.py
./services/all_actual_py.txt:29394:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/__init__.py
./services/all_actual_py.txt:29395:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/__init__.py
./services/all_actual_py.txt:29396:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/__init__.py
./services/all_actual_py.txt:29397:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/signature.py
./services/all_actual_py.txt:29398:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/errors.py
./services/all_actual_py.txt:29399:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/pre_configured.py
./services/all_actual_py.txt:29400:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/resource.py
./services/all_actual_py.txt:29401:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/access_token.py
./services/all_actual_py.txt:29402:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/__init__.py
./services/all_actual_py.txt:29403:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/authorization.py
./services/all_actual_py.txt:29404:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/request_token.py
./services/all_actual_py.txt:29405:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/signature_only.py
./services/all_actual_py.txt:29406:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/base.py
./services/all_actual_py.txt:29407:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/parameters.py
./services/all_actual_py.txt:29408:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/request_validator.py
./services/all_actual_py.txt:29409:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/__init__.py
./services/all_actual_py.txt:29410:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/utils.py
./services/all_actual_py.txt:29411:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/uri_validate.py
./services/all_actual_py.txt:29412:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/__init__.py
./services/all_actual_py.txt:29413:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/common.py
./services/all_actual_py.txt:29414:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/signals.py
./services/all_actual_py.txt:29415:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/__init__.py
./services/all_actual_py.txt:29416:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/pre_configured.py
./services/all_actual_py.txt:29417:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/userinfo.py
./services/all_actual_py.txt:29418:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/__init__.py
./services/all_actual_py.txt:29419:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/exceptions.py
./services/all_actual_py.txt:29420:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/dispatchers.py
./services/all_actual_py.txt:29421:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/__init__.py
./services/all_actual_py.txt:29422:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/hybrid.py
./services/all_actual_py.txt:29423:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/implicit.py
./services/all_actual_py.txt:29424:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/refresh_token.py
./services/all_actual_py.txt:29425:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/base.py
./services/all_actual_py.txt:29426:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/authorization_code.py
./services/all_actual_py.txt:29427:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/request_validator.py
./services/all_actual_py.txt:29428:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/__init__.py
./services/all_actual_py.txt:29429:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/tokens.py
./services/all_actual_py.txt:29430:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/__init__.py
./services/all_actual_py.txt:29487:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/fsspec/implementations/memory.py
./services/all_actual_py.txt:29519:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/auth/utils/__init__.py
./services/all_actual_py.txt:29520:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py
./services/all_actual_py.txt:29521:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/auth/__init__.py
./services/all_actual_py.txt:29522:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py
./services/all_actual_py.txt:29523:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/auth/simple_rbac_authz/__init__.py
./services/all_actual_py.txt:29543:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/test/auth/test_auth_utils.py
./services/all_actual_py.txt:29586:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/test/client/create_http_client_with_basic_auth.py
./services/all_actual_py.txt:29587:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/test/client/test_database_tenant_auth.py
./services/all_actual_py.txt:29624:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/utils/messageid.py
./services/all_actual_py.txt:29675:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/segment/impl/metadata/sqlite.py
./services/all_actual_py.txt:29859:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/neo4j/_async/auth_management.py
./services/all_actual_py.txt:29897:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/neo4j/_sync/auth_management.py
./services/all_actual_py.txt:29911:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/neo4j/_auth_management.py
./services/all_actual_py.txt:29916:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/neo4j/auth_management.py
./services/all_actual_py.txt:30178:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/numpy/_core/memmap.py
./services/all_actual_py.txt:30508:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/anyio/streams/memory.py
./services/all_actual_py.txt:30665:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_refresh_worker.py
./services/all_actual_py.txt:30666:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/compute_engine/credentials.py
./services/all_actual_py.txt:30667:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/compute_engine/_metadata.py
./services/all_actual_py.txt:30668:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/compute_engine/__init__.py
./services/all_actual_py.txt:30669:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_credentials_base.py
./services/all_actual_py.txt:30670:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_oauth2client.py
./services/all_actual_py.txt:30671:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/iam.py
./services/all_actual_py.txt:30672:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/version.py
./services/all_actual_py.txt:30673:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/downscoped.py
./services/all_actual_py.txt:30674:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_helpers.py
./services/all_actual_py.txt:30675:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/external_account_authorized_user.py
./services/all_actual_py.txt:30676:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/impersonated_credentials.py
./services/all_actual_py.txt:30677:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/credentials.py
./services/all_actual_py.txt:30678:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/exceptions.py
./services/all_actual_py.txt:30679:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_default_async.py
./services/all_actual_py.txt:30680:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/aio/_helpers.py
./services/all_actual_py.txt:30681:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/aio/credentials.py
./services/all_actual_py.txt:30682:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/aio/__init__.py
./services/all_actual_py.txt:30683:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/aio/transport/aiohttp.py
./services/all_actual_py.txt:30684:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/aio/transport/__init__.py
./services/all_actual_py.txt:30685:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/aio/transport/sessions.py
./services/all_actual_py.txt:30686:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/aws.py
./services/all_actual_py.txt:30687:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/environment_vars.py
./services/all_actual_py.txt:30688:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_service_account_info.py
./services/all_actual_py.txt:30689:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/app_engine.py
./services/all_actual_py.txt:30690:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/__init__.py
./services/all_actual_py.txt:30691:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_credentials_async.py
./services/all_actual_py.txt:30692:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_constants.py
./services/all_actual_py.txt:30693:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/pluggable.py
./services/all_actual_py.txt:30694:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/metrics.py
./services/all_actual_py.txt:30695:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/_custom_tls_signer.py
./services/all_actual_py.txt:30696:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/grpc.py
./services/all_actual_py.txt:30697:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/mtls.py
./services/all_actual_py.txt:30698:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/__init__.py
./services/all_actual_py.txt:30699:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/_requests_base.py
./services/all_actual_py.txt:30700:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/urllib3.py
./services/all_actual_py.txt:30701:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/_http_client.py
./services/all_actual_py.txt:30702:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/_aiohttp_requests.py
./services/all_actual_py.txt:30703:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/_mtls_helper.py
./services/all_actual_py.txt:30704:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/requests.py
./services/all_actual_py.txt:30705:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/external_account.py
./services/all_actual_py.txt:30706:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/identity_pool.py
./services/all_actual_py.txt:30707:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/jwt.py
./services/all_actual_py.txt:30708:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_cloud_sdk.py
./services/all_actual_py.txt:30709:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_jwt_async.py
./services/all_actual_py.txt:30710:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/crypt/_helpers.py
./services/all_actual_py.txt:30711:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/crypt/_cryptography_rsa.py
./services/all_actual_py.txt:30712:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/crypt/_python_rsa.py
./services/all_actual_py.txt:30713:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/crypt/rsa.py
./services/all_actual_py.txt:30714:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/crypt/es256.py
./services/all_actual_py.txt:30715:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/crypt/__init__.py
./services/all_actual_py.txt:30716:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/crypt/base.py
./services/all_actual_py.txt:30717:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/api_key.py
./services/all_actual_py.txt:30718:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_exponential_backoff.py
./services/all_actual_py.txt:30719:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_default.py
./services/all_actual_py.txt:30732:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/api/auth_pb2.py
./services/all_actual_py.txt:30739:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/api/metric_pb2.py
./services/all_actual_py.txt:30753:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/_client_async.py
./services/all_actual_py.txt:30754:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/id_token.py
./services/all_actual_py.txt:30755:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/_client.py
./services/all_actual_py.txt:30756:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/webauthn_types.py
./services/all_actual_py.txt:30757:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/credentials.py
./services/all_actual_py.txt:30758:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/_id_token_async.py
./services/all_actual_py.txt:30759:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/reauth.py
./services/all_actual_py.txt:30760:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/_service_account_async.py
./services/all_actual_py.txt:30761:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/challenges.py
./services/all_actual_py.txt:30762:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/webauthn_handler_factory.py
./services/all_actual_py.txt:30763:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/__init__.py
./services/all_actual_py.txt:30764:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/_credentials_async.py
./services/all_actual_py.txt:30765:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/gdch_credentials.py
./services/all_actual_py.txt:30766:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/webauthn_handler.py
./services/all_actual_py.txt:30767:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/sts.py
./services/all_actual_py.txt:30768:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/utils.py
./services/all_actual_py.txt:30769:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/service_account.py
./services/all_actual_py.txt:30770:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/_reauth_async.py
./services/all_actual_py.txt:30779:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/gapic/metadata/gapic_metadata_pb2.py
./services/all_actual_py.txt:30791:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/protobuf/message_factory.py
./services/all_actual_py.txt:30815:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/protobuf/internal/message_listener.py
./services/all_actual_py.txt:30818:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/protobuf/message.py
./services/all_actual_py.txt:30917:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/httpx/_auth.py
./services/all_actual_py.txt:31032:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_actual_py.txt:31057:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py
./services/all_actual_py.txt:31123:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_actual_py.txt:31302:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/languages.py
./services/all_actual_py.txt:31303:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/__init__.py
./services/all_actual_py.txt:31362:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_actual_py.txt:31363:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_actual_py.txt:31364:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_actual_py.txt:31365:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_actual_py.txt:31366:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_actual_py.txt:31367:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_actual_py.txt:31368:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_actual_py.txt:31369:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_actual_py.txt:31375:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_actual_py.txt:31379:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_actual_py.txt:31392:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_actual_py.txt:31393:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_legacy.py
./services/all_actual_py.txt:31396:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_actual_py.txt:31498:/home/ms-jarvis/msjarvis-rebuild/services/messenger_service_fixed.py
./services/all_actual_py.txt:31520:/home/ms-jarvis/msjarvis-rebuild/services/wvu_ldap_auth.py
./services/all_actual_py.txt:31547:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain/i_containers/i_container_1/memory_self/__init__.py
./services/all_actual_py.txt:31551:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain/i_containers/i_container_2/metacognitive_awareness/__init__.py
./services/all_actual_py.txt:31591:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py
./services/all_actual_py.txt:31592:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain/qualia_engine/meaning_maker/__init__.py
./services/all_actual_py.txt:31608:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_authentic_multi_llm.py
./services/all_actual_py.txt:31664:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_actual_py.txt:31689:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py
./services/all_actual_py.txt:31755:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_actual_py.txt:31934:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/languages.py
./services/all_actual_py.txt:31935:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/__init__.py
./services/all_actual_py.txt:31994:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_actual_py.txt:31995:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_actual_py.txt:31996:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_actual_py.txt:31997:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_actual_py.txt:31998:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_actual_py.txt:31999:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_actual_py.txt:32000:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_actual_py.txt:32001:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_actual_py.txt:32007:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_actual_py.txt:32011:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_actual_py.txt:32024:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_actual_py.txt:32025:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_legacy.py
./services/all_actual_py.txt:32028:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_actual_py.txt:32149:/home/ms-jarvis/msjarvis-rebuild/services/egeria_web_ui_plain_authentic.py
./services/all_actual_py.txt:32175:/home/ms-jarvis/msjarvis-rebuild/services/oauth2_callback.py
./services/all_actual_py.txt:32196:/home/ms-jarvis/msjarvis-rebuild/services/metrics_service.py
./services/all_actual_py.txt:32204:/home/ms-jarvis/msjarvis-rebuild/services/oauth2_handler.py
./services/all_actual_py.txt:32317:/home/ms-jarvis/msjarvis-rebuild/services/backups/pre_integration_20251012_115827/mamma_kidd_auth.py
./services/all_actual_py.txt:32364:/home/ms-jarvis/msjarvis-rebuild/services/memory_manager.py
./services/all_actual_py.txt:32426:/home/ms-jarvis/msjarvis-rebuild/services/method_tracker_decorator.py
./services/all_actual_py.txt:32464:/home/ms-jarvis/msjarvis-rebuild/services/mesh_coordinator_interface.py
./services/all_actual_py.txt:32473:/home/ms-jarvis/msjarvis-rebuild/services/mamma_kidd_auth.py
./services/all_actual_py.txt:32597:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/requests/auth.py
./services/all_actual_py.txt:32624:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/mex.py
./services/all_actual_py.txt:32626:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/auth_scheme.py
./services/all_actual_py.txt:32633:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/authority.py
./services/all_actual_py.txt:32635:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/oauth2cli/http.py
./services/all_actual_py.txt:32636:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/oauth2cli/authcode.py
./services/all_actual_py.txt:32637:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/oauth2cli/assertion.py
./services/all_actual_py.txt:32638:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/oauth2cli/__init__.py
./services/all_actual_py.txt:32639:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/oauth2cli/oauth2.py
./services/all_actual_py.txt:32640:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/oauth2cli/oidc.py
./services/all_actual_py.txt:32698:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_actual_py.txt:32723:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py
./services/all_actual_py.txt:32789:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_actual_py.txt:32968:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/languages.py
./services/all_actual_py.txt:32969:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/__init__.py
./services/all_actual_py.txt:33028:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_actual_py.txt:33029:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_actual_py.txt:33030:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_actual_py.txt:33031:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_actual_py.txt:33032:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_actual_py.txt:33033:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_actual_py.txt:33034:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_actual_py.txt:33035:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_actual_py.txt:33041:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_actual_py.txt:33045:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_actual_py.txt:33058:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_actual_py.txt:33059:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_legacy.py
./services/all_actual_py.txt:33062:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_actual_py.txt:33193:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/O365/message.py
./services/all_services.txt:5:/home/ms-jarvis/msjarvis-rebuild/services/memory_dgm_engine.py
./services/all_services.txt:174:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/huggingface_hub/utils/_auth.py
./services/all_services.txt:200:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/huggingface_hub/_oauth.py
./services/all_services.txt:215:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/huggingface_hub/cli/auth.py
./services/all_services.txt:245:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/websockets/legacy/auth.py
./services/all_services.txt:254:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/websockets/auth.py
./services/all_services.txt:264:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/websockets/asyncio/messages.py
./services/all_services.txt:271:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/websockets/sync/messages.py
./services/all_services.txt:318:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests/auth.py
./services/all_services.txt:509:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/grpc/_auth.py
./services/all_services.txt:802:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/joint.py
./services/all_services.txt:803:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/linearize.py
./services/all_services.txt:804:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/models.py
./services/all_services.txt:805:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/lagrange.py
./services/all_services.txt:806:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_rigidbody.py
./services/all_services.txt:807:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_actuator.py
./services/all_services.txt:808:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane3.py
./services/all_services.txt:809:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_body.py
./services/all_services.txt:810:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_system_class.py
./services/all_services.txt:811:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_loads.py
./services/all_services.txt:812:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane4.py
./services/all_services.txt:813:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane5.py
./services/all_services.txt:814:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_models.py
./services/all_services.txt:815:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_method.py
./services/all_services.txt:816:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_wrapping_geometry.py
./services/all_services.txt:817:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_lagrange2.py
./services/all_services.txt:818:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_linearity_of_velocity_constraints.py
./services/all_services.txt:819:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_system.py
./services/all_services.txt:820:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_functions.py
./services/all_services.txt:821:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_inertia.py
./services/all_services.txt:822:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/__init__.py
./services/all_services.txt:823:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_pathway.py
./services/all_services.txt:824:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_lagrange.py
./services/all_services.txt:825:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane2.py
./services/all_services.txt:826:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_particle.py
./services/all_services.txt:827:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_joint.py
./services/all_services.txt:828:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_linearize.py
./services/all_services.txt:829:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane.py
./services/all_services.txt:830:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_jointsmethod.py
./services/all_services.txt:831:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/jointsmethod.py
./services/all_services.txt:832:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/rigidbody.py
./services/all_services.txt:833:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/body_base.py
./services/all_services.txt:834:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/loads.py
./services/all_services.txt:835:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/pathway.py
./services/all_services.txt:836:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/__init__.py
./services/all_services.txt:837:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/inertia.py
./services/all_services.txt:838:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/particle.py
./services/all_services.txt:839:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/method.py
./services/all_services.txt:840:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/body.py
./services/all_services.txt:841:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/kane.py
./services/all_services.txt:842:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/system.py
./services/all_services.txt:843:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/wrapping_geometry.py
./services/all_services.txt:844:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/actuator.py
./services/all_services.txt:845:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/mechanics/functions.py
./services/all_services.txt:876:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/physics/optics/medium.py
./services/all_services.txt:1541:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/integrals/meijerint.py
./services/all_services.txt:1576:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/integrals/meijerint_doc.py
./services/all_services.txt:2024:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/sympy/utilities/memoization.py
./services/all_services.txt:2069:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/oauth2_session.py
./services/all_services.txt:2070:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/slack.py
./services/all_services.txt:2071:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/facebook.py
./services/all_services.txt:2072:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/plentymarkets.py
./services/all_services.txt:2073:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/ebay.py
./services/all_services.txt:2074:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/__init__.py
./services/all_services.txt:2075:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/douban.py
./services/all_services.txt:2076:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/instagram.py
./services/all_services.txt:2077:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/mailchimp.py
./services/all_services.txt:2078:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/fitbit.py
./services/all_services.txt:2079:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/weibo.py
./services/all_services.txt:2080:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/oauth1_auth.py
./services/all_services.txt:2081:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/__init__.py
./services/all_services.txt:2082:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/oauth2_auth.py
./services/all_services.txt:2083:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/requests_oauthlib/oauth1_session.py
./services/all_services.txt:2447:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/onnxruntime/transformers/metrics.py
./services/all_services.txt:2508:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/uvicorn/middleware/message_logger.py
./services/all_services.txt:2589:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/fastapi/security/oauth2.py
./services/all_services.txt:2665:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_services.txt:2720:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_services.txt:2813:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_vendor/packaging/metadata.py
./services/all_services.txt:2892:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_services.txt:2893:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_services.txt:2894:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_services.txt:2895:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_services.txt:2896:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_services.txt:2897:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_services.txt:2898:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_services.txt:2899:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_services.txt:2905:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_services.txt:2909:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_services.txt:2921:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_services.txt:2923:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_services.txt:3267:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/pygments/lexers/meson.py
./services/all_services.txt:3537:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/kubernetes/client/api/authorization_v1_api.py
./services/all_services.txt:3543:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/kubernetes/client/api/rbac_authorization_api.py
./services/all_services.txt:3547:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/kubernetes/client/api/authentication_v1_api.py
./services/all_services.txt:3555:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/kubernetes/client/api/authorization_api.py
./services/all_services.txt:3563:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/kubernetes/client/api/rbac_authorization_v1_api.py
./services/all_services.txt:3573:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/kubernetes/client/api/authentication_api.py
./services/all_services.txt:3817:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/kubernetes/client/models/authentication_v1_token_request.py
./services/all_services.txt:4329:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/rich/measure.py
./services/all_services.txt:4437:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/export/__init__.py
./services/all_services.txt:4438:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement.py
./services/all_services.txt:4439:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/view.py
./services/all_services.txt:4440:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement_consumer.py
./services/all_services.txt:4441:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/export/__init__.py
./services/all_services.txt:4442:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/_view_instrument_match.py
./services/all_services.txt:4443:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/aggregation.py
./services/all_services.txt:4444:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exceptions.py
./services/all_services.txt:4445:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/instrument.py
./services/all_services.txt:4446:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py
./services/all_services.txt:4447:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/__init__.py
./services/all_services.txt:4448:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/buckets.py
./services/all_services.txt:4449:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/exponent_mapping.py
./services/all_services.txt:4450:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/errors.py
./services/all_services.txt:4451:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/logarithm_mapping.py
./services/all_services.txt:4452:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/__init__.py
./services/all_services.txt:4453:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/ieee_754.py
./services/all_services.txt:4454:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/point.py
./services/all_services.txt:4455:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/metric_reader_storage.py
./services/all_services.txt:4456:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar_filter.py
./services/all_services.txt:4457:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar_reservoir.py
./services/all_services.txt:4458:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/__init__.py
./services/all_services.txt:4459:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar.py
./services/all_services.txt:4460:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/sdk_configuration.py
./services/all_services.txt:4461:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/view/__init__.py
./services/all_services.txt:4462:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/metrics/__init__.py
./services/all_services.txt:4470:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/sdk/trace/_sampling_experimental/_parent_threshold.py
./services/all_services.txt:4497:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/metrics/db_metrics.py
./services/all_services.txt:4498:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/metrics/__init__.py
./services/all_services.txt:4499:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/metrics/http_metrics.py
./services/all_services.txt:4503:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/dns_metrics.py
./services/all_services.txt:4504:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cicd_metrics.py
./services/all_services.txt:4505:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/vcs_metrics.py
./services/all_services.txt:4506:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/db_metrics.py
./services/all_services.txt:4507:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/rpc_metrics.py
./services/all_services.txt:4508:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cpu_metrics.py
./services/all_services.txt:4509:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cpython_metrics.py
./services/all_services.txt:4510:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/gen_ai_metrics.py
./services/all_services.txt:4511:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/faas_metrics.py
./services/all_services.txt:4512:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/system_metrics.py
./services/all_services.txt:4513:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/process_metrics.py
./services/all_services.txt:4514:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/otel_metrics.py
./services/all_services.txt:4515:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/messaging_metrics.py
./services/all_services.txt:4516:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/hw_metrics.py
./services/all_services.txt:4517:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/k8s_metrics.py
./services/all_services.txt:4518:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/http_metrics.py
./services/all_services.txt:4519:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py
./services/all_services.txt:4520:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/azure_metrics.py
./services/all_services.txt:4522:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/message_attributes.py
./services/all_services.txt:4582:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/messaging_attributes.py
./services/all_services.txt:4635:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/metric_exporter/__init__.py
./services/all_services.txt:4638:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/common/metrics_encoder.py
./services/all_services.txt:4642:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/common/_internal/metrics_encoder/__init__.py
./services/all_services.txt:4647:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/metrics/_internal/instrument.py
./services/all_services.txt:4648:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/metrics/_internal/__init__.py
./services/all_services.txt:4649:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/metrics/_internal/observation.py
./services/all_services.txt:4650:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/metrics/__init__.py
./services/all_services.txt:4663:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/proto/metrics/v1/metrics_pb2.py
./services/all_services.txt:4664:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/proto/metrics/v1/__init__.py
./services/all_services.txt:4665:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/proto/metrics/__init__.py
./services/all_services.txt:4676:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/metrics_service_pb2_grpc.py
./services/all_services.txt:4677:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/metrics_service_pb2.py
./services/all_services.txt:4678:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/__init__.py
./services/all_services.txt:4679:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/__init__.py
./services/all_services.txt:4720:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/packaging/metadata.py
./services/all_services.txt:4784:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/errors.py
./services/all_services.txt:4785:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/pre_configured.py
./services/all_services.txt:4786:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/revocation.py
./services/all_services.txt:4787:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/resource.py
./services/all_services.txt:4788:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/metadata.py
./services/all_services.txt:4789:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/__init__.py
./services/all_services.txt:4790:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/authorization.py
./services/all_services.txt:4791:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/introspect.py
./services/all_services.txt:4792:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/base.py
./services/all_services.txt:4793:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/token.py
./services/all_services.txt:4794:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/mobile_application.py
./services/all_services.txt:4795:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/legacy_application.py
./services/all_services.txt:4796:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/backend_application.py
./services/all_services.txt:4797:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/service_application.py
./services/all_services.txt:4798:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/__init__.py
./services/all_services.txt:4799:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/web_application.py
./services/all_services.txt:4800:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/base.py
./services/all_services.txt:4801:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/parameters.py
./services/all_services.txt:4802:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/resource_owner_password_credentials.py
./services/all_services.txt:4803:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/__init__.py
./services/all_services.txt:4804:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/client_credentials.py
./services/all_services.txt:4805:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/implicit.py
./services/all_services.txt:4806:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/refresh_token.py
./services/all_services.txt:4807:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/base.py
./services/all_services.txt:4808:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/authorization_code.py
./services/all_services.txt:4809:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/request_validator.py
./services/all_services.txt:4810:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/__init__.py
./services/all_services.txt:4811:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/utils.py
./services/all_services.txt:4812:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/tokens.py
./services/all_services.txt:4813:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/errors.py
./services/all_services.txt:4814:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/pre_configured.py
./services/all_services.txt:4815:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/__init__.py
./services/all_services.txt:4816:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/device_authorization.py
./services/all_services.txt:4817:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/clients/device.py
./services/all_services.txt:4818:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/clients/__init__.py
./services/all_services.txt:4819:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/grant_types/__init__.py
./services/all_services.txt:4820:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/grant_types/device_code.py
./services/all_services.txt:4821:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/request_validator.py
./services/all_services.txt:4822:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/__init__.py
./services/all_services.txt:4823:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth2/__init__.py
./services/all_services.txt:4824:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/__init__.py
./services/all_services.txt:4825:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/signature.py
./services/all_services.txt:4826:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/errors.py
./services/all_services.txt:4827:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/pre_configured.py
./services/all_services.txt:4828:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/resource.py
./services/all_services.txt:4829:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/access_token.py
./services/all_services.txt:4830:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/__init__.py
./services/all_services.txt:4831:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/authorization.py
./services/all_services.txt:4832:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/request_token.py
./services/all_services.txt:4833:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/signature_only.py
./services/all_services.txt:4834:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/base.py
./services/all_services.txt:4835:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/parameters.py
./services/all_services.txt:4836:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/request_validator.py
./services/all_services.txt:4837:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/__init__.py
./services/all_services.txt:4838:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/utils.py
./services/all_services.txt:4839:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/uri_validate.py
./services/all_services.txt:4840:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/__init__.py
./services/all_services.txt:4841:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/common.py
./services/all_services.txt:4842:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/signals.py
./services/all_services.txt:4843:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/__init__.py
./services/all_services.txt:4844:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/pre_configured.py
./services/all_services.txt:4845:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/userinfo.py
./services/all_services.txt:4846:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/__init__.py
./services/all_services.txt:4847:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/exceptions.py
./services/all_services.txt:4848:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/dispatchers.py
./services/all_services.txt:4849:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/__init__.py
./services/all_services.txt:4850:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/hybrid.py
./services/all_services.txt:4851:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/implicit.py
./services/all_services.txt:4852:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/refresh_token.py
./services/all_services.txt:4853:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/base.py
./services/all_services.txt:4854:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/authorization_code.py
./services/all_services.txt:4855:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/request_validator.py
./services/all_services.txt:4856:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/__init__.py
./services/all_services.txt:4857:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/core/tokens.py
./services/all_services.txt:4858:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/oauthlib/openid/connect/__init__.py
./services/all_services.txt:4915:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/fsspec/implementations/memory.py
./services/all_services.txt:4946:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/basic/__init__.py
./services/all_services.txt:4947:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/token/__init__.py
./services/all_services.txt:4948:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/providers.py
./services/all_services.txt:4949:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/__init__.py
./services/all_services.txt:4950:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/fastapi.py
./services/all_services.txt:4951:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/registry.py
./services/all_services.txt:4952:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/authz/__init__.py
./services/all_services.txt:4953:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/auth/fastapi_utils.py
./services/all_services.txt:4962:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/test/auth/test_simple_rbac_authz.py
./services/all_services.txt:4963:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/test/auth/test_token_auth.py
./services/all_services.txt:4964:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/test/auth/test_basic_auth.py
./services/all_services.txt:4982:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/test/client/create_http_client_with_basic_auth.py
./services/all_services.txt:5011:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/utils/messageid.py
./services/all_services.txt:5032:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/chromadb/segment/impl/metadata/sqlite.py
./services/all_services.txt:5414:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/numpy/_core/memmap.py
./services/all_services.txt:5735:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/anyio/streams/memory.py
./services/all_services.txt:5751:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/starlette/middleware/authentication.py
./services/all_services.txt:5763:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/starlette/authentication.py
./services/all_services.txt:5775:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_refresh_worker.py
./services/all_services.txt:5776:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/compute_engine/credentials.py
./services/all_services.txt:5777:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/compute_engine/_metadata.py
./services/all_services.txt:5778:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/compute_engine/__init__.py
./services/all_services.txt:5779:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_credentials_base.py
./services/all_services.txt:5780:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_oauth2client.py
./services/all_services.txt:5781:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/iam.py
./services/all_services.txt:5782:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/version.py
./services/all_services.txt:5783:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/downscoped.py
./services/all_services.txt:5784:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_helpers.py
./services/all_services.txt:5785:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/external_account_authorized_user.py
./services/all_services.txt:5786:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/impersonated_credentials.py
./services/all_services.txt:5787:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/credentials.py
./services/all_services.txt:5788:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/exceptions.py
./services/all_services.txt:5789:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_default_async.py
./services/all_services.txt:5790:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/aio/_helpers.py
./services/all_services.txt:5791:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/aio/credentials.py
./services/all_services.txt:5792:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/aio/__init__.py
./services/all_services.txt:5793:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/aio/transport/aiohttp.py
./services/all_services.txt:5794:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/aio/transport/__init__.py
./services/all_services.txt:5795:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/aio/transport/sessions.py
./services/all_services.txt:5796:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/aws.py
./services/all_services.txt:5797:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/environment_vars.py
./services/all_services.txt:5798:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_service_account_info.py
./services/all_services.txt:5799:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/app_engine.py
./services/all_services.txt:5800:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/__init__.py
./services/all_services.txt:5801:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_credentials_async.py
./services/all_services.txt:5802:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_constants.py
./services/all_services.txt:5803:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/pluggable.py
./services/all_services.txt:5804:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/metrics.py
./services/all_services.txt:5805:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/_custom_tls_signer.py
./services/all_services.txt:5806:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/grpc.py
./services/all_services.txt:5807:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/mtls.py
./services/all_services.txt:5808:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/__init__.py
./services/all_services.txt:5809:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/_requests_base.py
./services/all_services.txt:5810:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/urllib3.py
./services/all_services.txt:5811:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/_http_client.py
./services/all_services.txt:5812:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/_aiohttp_requests.py
./services/all_services.txt:5813:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/_mtls_helper.py
./services/all_services.txt:5814:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/transport/requests.py
./services/all_services.txt:5815:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/external_account.py
./services/all_services.txt:5816:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/identity_pool.py
./services/all_services.txt:5817:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/jwt.py
./services/all_services.txt:5818:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_cloud_sdk.py
./services/all_services.txt:5819:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_jwt_async.py
./services/all_services.txt:5820:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/crypt/_helpers.py
./services/all_services.txt:5821:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/crypt/_cryptography_rsa.py
./services/all_services.txt:5822:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/crypt/_python_rsa.py
./services/all_services.txt:5823:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/crypt/rsa.py
./services/all_services.txt:5824:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/crypt/es256.py
./services/all_services.txt:5825:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/crypt/__init__.py
./services/all_services.txt:5826:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/crypt/base.py
./services/all_services.txt:5827:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/api_key.py
./services/all_services.txt:5828:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_exponential_backoff.py
./services/all_services.txt:5829:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/auth/_default.py
./services/all_services.txt:5842:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/api/auth_pb2.py
./services/all_services.txt:5849:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/api/metric_pb2.py
./services/all_services.txt:5863:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/_client_async.py
./services/all_services.txt:5864:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/id_token.py
./services/all_services.txt:5865:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/_client.py
./services/all_services.txt:5866:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/webauthn_types.py
./services/all_services.txt:5867:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/credentials.py
./services/all_services.txt:5868:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/_id_token_async.py
./services/all_services.txt:5869:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/reauth.py
./services/all_services.txt:5870:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/_service_account_async.py
./services/all_services.txt:5871:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/challenges.py
./services/all_services.txt:5872:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/webauthn_handler_factory.py
./services/all_services.txt:5873:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/__init__.py
./services/all_services.txt:5874:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/_credentials_async.py
./services/all_services.txt:5875:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/gdch_credentials.py
./services/all_services.txt:5876:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/webauthn_handler.py
./services/all_services.txt:5877:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/sts.py
./services/all_services.txt:5878:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/utils.py
./services/all_services.txt:5879:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/service_account.py
./services/all_services.txt:5880:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/oauth2/_reauth_async.py
./services/all_services.txt:5889:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/gapic/metadata/gapic_metadata_pb2.py
./services/all_services.txt:5900:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/protobuf/message_factory.py
./services/all_services.txt:5924:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/protobuf/internal/message_listener.py
./services/all_services.txt:5927:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/google/protobuf/message.py
./services/all_services.txt:6026:/home/ms-jarvis/msjarvis-rebuild/services/venv_gateway/lib/python3.12/site-packages/httpx/_auth.py
./services/all_services.txt:6236:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/uvicorn/middleware/message_logger.py
./services/all_services.txt:6290:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/fastapi/security/oauth2.py
./services/all_services.txt:6356:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_services.txt:6381:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py
./services/all_services.txt:6447:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_services.txt:6626:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/languages.py
./services/all_services.txt:6627:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/__init__.py
./services/all_services.txt:6686:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_services.txt:6687:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_services.txt:6688:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_services.txt:6689:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_services.txt:6690:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_services.txt:6691:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_services.txt:6692:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_services.txt:6693:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_services.txt:6699:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_services.txt:6703:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_services.txt:6716:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_services.txt:6717:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_legacy.py
./services/all_services.txt:6720:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_services.txt:6872:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/anyio/streams/memory.py
./services/all_services.txt:6888:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/starlette/middleware/authentication.py
./services/all_services.txt:6899:/home/ms-jarvis/msjarvis-rebuild/services/contract-builder-env/lib/python3.12/site-packages/starlette/authentication.py
./services/all_services.txt:7150:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/uvicorn/middleware/message_logger.py
./services/all_services.txt:7204:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py
./services/all_services.txt:7271:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_services.txt:7296:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py
./services/all_services.txt:7362:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_services.txt:7541:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/languages.py
./services/all_services.txt:7542:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/__init__.py
./services/all_services.txt:7601:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_services.txt:7602:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_services.txt:7603:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_services.txt:7604:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_services.txt:7605:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_services.txt:7606:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_services.txt:7607:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_services.txt:7608:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_services.txt:7614:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_services.txt:7618:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_services.txt:7631:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_services.txt:7632:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_legacy.py
./services/all_services.txt:7635:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_services.txt:7798:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/anyio/streams/memory.py
./services/all_services.txt:7814:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/starlette/middleware/authentication.py
./services/all_services.txt:7825:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/starlette/authentication.py
./services/all_services.txt:7841:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/httpx/_auth.py
./services/all_services.txt:7867:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/chardet/metadata/languages.py
./services/all_services.txt:7868:/home/ms-jarvis/msjarvis-rebuild/services/link_reader_venv/lib/python3.12/site-packages/chardet/metadata/__init__.py
./services/all_services.txt:7919:/home/ms-jarvis/msjarvis-rebuild/services/fix_judge_authentic.py
./services/all_services.txt:7939:/home/ms-jarvis/msjarvis-rebuild/services/method_tracking_service.py
./services/all_services.txt:8242:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/huggingface_hub/utils/_auth.py
./services/all_services.txt:8269:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/huggingface_hub/_oauth.py
./services/all_services.txt:8285:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/huggingface_hub/cli/auth.py
./services/all_services.txt:8330:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/websockets/legacy/auth.py
./services/all_services.txt:8339:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/websockets/auth.py
./services/all_services.txt:8349:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/websockets/asyncio/messages.py
./services/all_services.txt:8356:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/websockets/sync/messages.py
./services/all_services.txt:8387:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/wheel/metadata.py
./services/all_services.txt:8439:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests/auth.py
./services/all_services.txt:8448:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/redis/auth/__init__.py
./services/all_services.txt:8449:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/redis/auth/token_manager.py
./services/all_services.txt:8450:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/redis/auth/err.py
./services/all_services.txt:8451:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/redis/auth/idp.py
./services/all_services.txt:8452:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/redis/auth/token.py
./services/all_services.txt:8759:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/_lazy/metrics.py
./services/all_services.txt:9340:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/_inductor/memory.py
./services/all_services.txt:9386:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/_inductor/codegen/memory_planning.py
./services/all_services.txt:9479:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/_inductor/metrics.py
./services/all_services.txt:9558:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/distributed/elastic/metrics/api.py
./services/all_services.txt:9559:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/distributed/elastic/metrics/__init__.py
./services/all_services.txt:9589:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/distributed/checkpoint/metadata.py
./services/all_services.txt:9735:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/distributed/_shard/sharded_tensor/metadata.py
./services/all_services.txt:9749:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/distributed/_shard/metadata.py
./services/all_services.txt:9845:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/distributed/_tools/mem_tracker.py
./services/all_services.txt:9846:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/distributed/_tools/memory_tracker.py
./services/all_services.txt:9866:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/_subclasses/meta_utils.py
./services/all_services.txt:10041:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/nn/utils/memory_format.py
./services/all_services.txt:10311:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/_dynamo/metrics_context.py
./services/all_services.txt:10356:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/fx/experimental/merge_matmul.py
./services/all_services.txt:10358:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/fx/experimental/meta_tracer.py
./services/all_services.txt:10416:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/accelerator/memory.py
./services/all_services.txt:10472:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/mtia/memory.py
./services/all_services.txt:10615:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/cuda/memory.py
./services/all_services.txt:10659:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torch/xpu/memory.py
./services/all_services.txt:10746:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/grpc/_auth.py
./services/all_services.txt:11095:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/networkx/algorithms/threshold.py
./services/all_services.txt:11127:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/networkx/algorithms/tests/test_threshold.py
./services/all_services.txt:11651:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/joint.py
./services/all_services.txt:11652:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/linearize.py
./services/all_services.txt:11653:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/models.py
./services/all_services.txt:11654:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/lagrange.py
./services/all_services.txt:11655:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_rigidbody.py
./services/all_services.txt:11656:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_actuator.py
./services/all_services.txt:11657:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane3.py
./services/all_services.txt:11658:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_body.py
./services/all_services.txt:11659:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_system_class.py
./services/all_services.txt:11660:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_loads.py
./services/all_services.txt:11661:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane4.py
./services/all_services.txt:11662:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane5.py
./services/all_services.txt:11663:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_models.py
./services/all_services.txt:11664:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_method.py
./services/all_services.txt:11665:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_wrapping_geometry.py
./services/all_services.txt:11666:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_lagrange2.py
./services/all_services.txt:11667:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_linearity_of_velocity_constraints.py
./services/all_services.txt:11668:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_system.py
./services/all_services.txt:11669:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_functions.py
./services/all_services.txt:11670:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_inertia.py
./services/all_services.txt:11671:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/__init__.py
./services/all_services.txt:11672:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_pathway.py
./services/all_services.txt:11673:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_lagrange.py
./services/all_services.txt:11674:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane2.py
./services/all_services.txt:11675:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_particle.py
./services/all_services.txt:11676:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_joint.py
./services/all_services.txt:11677:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_linearize.py
./services/all_services.txt:11678:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane.py
./services/all_services.txt:11679:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_jointsmethod.py
./services/all_services.txt:11680:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/jointsmethod.py
./services/all_services.txt:11681:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/rigidbody.py
./services/all_services.txt:11682:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/body_base.py
./services/all_services.txt:11683:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/loads.py
./services/all_services.txt:11684:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/pathway.py
./services/all_services.txt:11685:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/__init__.py
./services/all_services.txt:11686:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/inertia.py
./services/all_services.txt:11687:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/particle.py
./services/all_services.txt:11688:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/method.py
./services/all_services.txt:11689:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/body.py
./services/all_services.txt:11690:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/kane.py
./services/all_services.txt:11691:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/system.py
./services/all_services.txt:11692:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/wrapping_geometry.py
./services/all_services.txt:11693:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/actuator.py
./services/all_services.txt:11694:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/mechanics/functions.py
./services/all_services.txt:11725:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/physics/optics/medium.py
./services/all_services.txt:12390:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/integrals/meijerint.py
./services/all_services.txt:12425:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/integrals/meijerint_doc.py
./services/all_services.txt:12873:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sympy/utilities/memoization.py
./services/all_services.txt:12918:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/oauth2_session.py
./services/all_services.txt:12919:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/slack.py
./services/all_services.txt:12920:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/facebook.py
./services/all_services.txt:12921:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/plentymarkets.py
./services/all_services.txt:12922:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/ebay.py
./services/all_services.txt:12923:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/__init__.py
./services/all_services.txt:12924:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/douban.py
./services/all_services.txt:12925:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/instagram.py
./services/all_services.txt:12926:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/mailchimp.py
./services/all_services.txt:12927:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/fitbit.py
./services/all_services.txt:12928:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/weibo.py
./services/all_services.txt:12929:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/oauth1_auth.py
./services/all_services.txt:12930:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/__init__.py
./services/all_services.txt:12931:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/oauth2_auth.py
./services/all_services.txt:12932:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/requests_oauthlib/oauth1_session.py
./services/all_services.txt:13296:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/onnxruntime/transformers/metrics.py
./services/all_services.txt:13461:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/uvicorn/middleware/message_logger.py
./services/all_services.txt:13504:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/prometheus_client/metrics_core.py
./services/all_services.txt:13523:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/prometheus_client/metrics.py
./services/all_services.txt:13593:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/fastapi/security/oauth2.py
./services/all_services.txt:13668:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_services.txt:13723:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_services.txt:13816:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_vendor/packaging/metadata.py
./services/all_services.txt:13895:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_services.txt:13896:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_services.txt:13897:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_services.txt:13898:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_services.txt:13899:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_services.txt:13900:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_services.txt:13901:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_services.txt:13902:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_services.txt:13908:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_services.txt:13912:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_services.txt:13924:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_services.txt:13926:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_services.txt:14270:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pygments/lexers/meson.py
./services/all_services.txt:14544:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/kubernetes/client/api/authorization_v1_api.py
./services/all_services.txt:14550:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/kubernetes/client/api/rbac_authorization_api.py
./services/all_services.txt:14554:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/kubernetes/client/api/authentication_v1_api.py
./services/all_services.txt:14562:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/kubernetes/client/api/authorization_api.py
./services/all_services.txt:14570:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/kubernetes/client/api/rbac_authorization_v1_api.py
./services/all_services.txt:14580:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/kubernetes/client/api/authentication_api.py
./services/all_services.txt:14824:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/kubernetes/client/models/authentication_v1_token_request.py
./services/all_services.txt:15336:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/rich/measure.py
./services/all_services.txt:15827:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_align.py
./services/all_services.txt:15828:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_join.py
./services/all_services.txt:15829:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_asfreq.py
./services/all_services.txt:15830:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_dtypes.py
./services/all_services.txt:15831:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_reset_index.py
./services/all_services.txt:15832:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_cov_corr.py
./services/all_services.txt:15833:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_astype.py
./services/all_services.txt:15834:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_tz_localize.py
./services/all_services.txt:15835:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_values.py
./services/all_services.txt:15836:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_drop.py
./services/all_services.txt:15837:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_set_index.py
./services/all_services.txt:15838:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_isetitem.py
./services/all_services.txt:15839:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_swapaxes.py
./services/all_services.txt:15840:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_to_numpy.py
./services/all_services.txt:15841:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_nlargest.py
./services/all_services.txt:15842:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_copy.py
./services/all_services.txt:15843:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_filter.py
./services/all_services.txt:15844:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_add_prefix_suffix.py
./services/all_services.txt:15845:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_sample.py
./services/all_services.txt:15846:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_matmul.py
./services/all_services.txt:15847:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_compare.py
./services/all_services.txt:15848:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_clip.py
./services/all_services.txt:15849:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_explode.py
./services/all_services.txt:15850:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_pop.py
./services/all_services.txt:15851:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_replace.py
./services/all_services.txt:15852:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_to_records.py
./services/all_services.txt:15853:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_first_valid_index.py
./services/all_services.txt:15854:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_update.py
./services/all_services.txt:15855:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_to_timestamp.py
./services/all_services.txt:15856:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_rank.py
./services/all_services.txt:15857:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_rename_axis.py
./services/all_services.txt:15858:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_to_period.py
./services/all_services.txt:15859:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_swaplevel.py
./services/all_services.txt:15860:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_head_tail.py
./services/all_services.txt:15861:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_map.py
./services/all_services.txt:15862:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_tz_convert.py
./services/all_services.txt:15863:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_to_dict_of_blocks.py
./services/all_services.txt:15864:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_truncate.py
./services/all_services.txt:15865:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_droplevel.py
./services/all_services.txt:15866:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_iterrows.py
./services/all_services.txt:15867:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_count.py
./services/all_services.txt:15868:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_drop_duplicates.py
./services/all_services.txt:15869:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_reorder_levels.py
./services/all_services.txt:15870:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_at_time.py
./services/all_services.txt:15871:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_assign.py
./services/all_services.txt:15872:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_pipe.py
./services/all_services.txt:15873:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_transpose.py
./services/all_services.txt:15874:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_size.py
./services/all_services.txt:15875:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_select_dtypes.py
./services/all_services.txt:15876:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_describe.py
./services/all_services.txt:15877:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_equals.py
./services/all_services.txt:15878:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_isin.py
./services/all_services.txt:15879:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_value_counts.py
./services/all_services.txt:15880:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_rename.py
./services/all_services.txt:15881:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_sort_values.py
./services/all_services.txt:15882:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_quantile.py
./services/all_services.txt:15883:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_to_csv.py
./services/all_services.txt:15884:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_get_numeric_data.py
./services/all_services.txt:15885:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_duplicated.py
./services/all_services.txt:15886:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/__init__.py
./services/all_services.txt:15887:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_combine_first.py
./services/all_services.txt:15888:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_infer_objects.py
./services/all_services.txt:15889:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_dropna.py
./services/all_services.txt:15890:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_set_axis.py
./services/all_services.txt:15891:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_fillna.py
./services/all_services.txt:15892:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_shift.py
./services/all_services.txt:15893:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_round.py
./services/all_services.txt:15894:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_interpolate.py
./services/all_services.txt:15895:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_is_homogeneous_dtype.py
./services/all_services.txt:15896:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_convert_dtypes.py
./services/all_services.txt:15897:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_combine.py
./services/all_services.txt:15898:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_between_time.py
./services/all_services.txt:15899:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_sort_index.py
./services/all_services.txt:15900:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_first_and_last.py
./services/all_services.txt:15901:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_reindex_like.py
./services/all_services.txt:15902:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_pct_change.py
./services/all_services.txt:15903:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_diff.py
./services/all_services.txt:15904:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_to_dict.py
./services/all_services.txt:15905:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_asof.py
./services/all_services.txt:15906:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_info.py
./services/all_services.txt:15907:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_dot.py
./services/all_services.txt:15908:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/frame/methods/test_reindex.py
./services/all_services.txt:15960:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_align.py
./services/all_services.txt:15961:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_dtypes.py
./services/all_services.txt:15962:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_reset_index.py
./services/all_services.txt:15963:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_cov_corr.py
./services/all_services.txt:15964:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_astype.py
./services/all_services.txt:15965:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_tz_localize.py
./services/all_services.txt:15966:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_values.py
./services/all_services.txt:15967:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_drop.py
./services/all_services.txt:15968:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_is_monotonic.py
./services/all_services.txt:15969:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_to_numpy.py
./services/all_services.txt:15970:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_nlargest.py
./services/all_services.txt:15971:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_copy.py
./services/all_services.txt:15972:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_view.py
./services/all_services.txt:15973:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_add_prefix_suffix.py
./services/all_services.txt:15974:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_matmul.py
./services/all_services.txt:15975:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_compare.py
./services/all_services.txt:15976:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_clip.py
./services/all_services.txt:15977:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_explode.py
./services/all_services.txt:15978:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_pop.py
./services/all_services.txt:15979:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_argsort.py
./services/all_services.txt:15980:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_replace.py
./services/all_services.txt:15981:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_between.py
./services/all_services.txt:15982:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_update.py
./services/all_services.txt:15983:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_rank.py
./services/all_services.txt:15984:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_rename_axis.py
./services/all_services.txt:15985:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_unstack.py
./services/all_services.txt:15986:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_head_tail.py
./services/all_services.txt:15987:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_map.py
./services/all_services.txt:15988:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_truncate.py
./services/all_services.txt:15989:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_unique.py
./services/all_services.txt:15990:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_count.py
./services/all_services.txt:15991:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_drop_duplicates.py
./services/all_services.txt:15992:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_set_name.py
./services/all_services.txt:15993:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_searchsorted.py
./services/all_services.txt:15994:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_size.py
./services/all_services.txt:15995:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_describe.py
./services/all_services.txt:15996:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_equals.py
./services/all_services.txt:15997:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_isin.py
./services/all_services.txt:15998:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_value_counts.py
./services/all_services.txt:15999:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_rename.py
./services/all_services.txt:16000:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_sort_values.py
./services/all_services.txt:16001:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_quantile.py
./services/all_services.txt:16002:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_to_csv.py
./services/all_services.txt:16003:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_get_numeric_data.py
./services/all_services.txt:16004:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_duplicated.py
./services/all_services.txt:16005:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_isna.py
./services/all_services.txt:16006:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/__init__.py
./services/all_services.txt:16007:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_combine_first.py
./services/all_services.txt:16008:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_infer_objects.py
./services/all_services.txt:16009:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_dropna.py
./services/all_services.txt:16010:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_tolist.py
./services/all_services.txt:16011:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_to_frame.py
./services/all_services.txt:16012:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_fillna.py
./services/all_services.txt:16013:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_round.py
./services/all_services.txt:16014:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_interpolate.py
./services/all_services.txt:16015:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_case_when.py
./services/all_services.txt:16016:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_convert_dtypes.py
./services/all_services.txt:16017:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_combine.py
./services/all_services.txt:16018:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_is_unique.py
./services/all_services.txt:16019:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_sort_index.py
./services/all_services.txt:16020:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_reindex_like.py
./services/all_services.txt:16021:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_repeat.py
./services/all_services.txt:16022:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_pct_change.py
./services/all_services.txt:16023:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_autocorr.py
./services/all_services.txt:16024:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_diff.py
./services/all_services.txt:16025:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_to_dict.py
./services/all_services.txt:16026:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_asof.py
./services/all_services.txt:16027:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_nunique.py
./services/all_services.txt:16028:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_item.py
./services/all_services.txt:16029:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_info.py
./services/all_services.txt:16030:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/series/methods/test_reindex.py
./services/all_services.txt:16080:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timedelta/methods/__init__.py
./services/all_services.txt:16081:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timedelta/methods/test_round.py
./services/all_services.txt:16082:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timedelta/methods/test_as_unit.py
./services/all_services.txt:16089:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_tz_localize.py
./services/all_services.txt:16090:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_normalize.py
./services/all_services.txt:16091:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_replace.py
./services/all_services.txt:16092:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_tz_convert.py
./services/all_services.txt:16093:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_timestamp_method.py
./services/all_services.txt:16094:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/__init__.py
./services/all_services.txt:16095:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_round.py
./services/all_services.txt:16096:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_to_julian_date.py
./services/all_services.txt:16097:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_to_pydatetime.py
./services/all_services.txt:16098:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/scalar/timestamp/methods/test_as_unit.py
./services/all_services.txt:16170:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_merge_asof.py
./services/all_services.txt:16171:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_join.py
./services/all_services.txt:16172:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_merge_ordered.py
./services/all_services.txt:16173:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_merge_index_as_string.py
./services/all_services.txt:16174:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_multi.py
./services/all_services.txt:16175:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_merge.py
./services/all_services.txt:16176:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/__init__.py
./services/all_services.txt:16177:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_merge_cross.py
./services/all_services.txt:16367:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_is_monotonic.py
./services/all_services.txt:16368:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_corrwith.py
./services/all_services.txt:16369:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_sample.py
./services/all_services.txt:16370:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_rank.py
./services/all_services.txt:16371:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_skew.py
./services/all_services.txt:16372:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_size.py
./services/all_services.txt:16373:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_describe.py
./services/all_services.txt:16374:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_value_counts.py
./services/all_services.txt:16375:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_quantile.py
./services/all_services.txt:16376:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/__init__.py
./services/all_services.txt:16377:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_nlargest_nsmallest.py
./services/all_services.txt:16378:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_groupby_shift_diff.py
./services/all_services.txt:16379:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/groupby/methods/test_nth.py
./services/all_services.txt:16464:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/timedeltas/methods/test_astype.py
./services/all_services.txt:16465:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/timedeltas/methods/test_insert.py
./services/all_services.txt:16466:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/timedeltas/methods/__init__.py
./services/all_services.txt:16467:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/timedeltas/methods/test_fillna.py
./services/all_services.txt:16468:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/timedeltas/methods/test_shift.py
./services/all_services.txt:16469:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/timedeltas/methods/test_factorize.py
./services/all_services.txt:16470:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/timedeltas/methods/test_repeat.py
./services/all_services.txt:16532:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_astype.py
./services/all_services.txt:16533:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_tz_localize.py
./services/all_services.txt:16534:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_to_series.py
./services/all_services.txt:16535:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_normalize.py
./services/all_services.txt:16536:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_to_period.py
./services/all_services.txt:16537:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_map.py
./services/all_services.txt:16538:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_tz_convert.py
./services/all_services.txt:16539:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_unique.py
./services/all_services.txt:16540:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_isocalendar.py
./services/all_services.txt:16541:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_delete.py
./services/all_services.txt:16542:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_resolution.py
./services/all_services.txt:16543:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_insert.py
./services/all_services.txt:16544:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/__init__.py
./services/all_services.txt:16545:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_snap.py
./services/all_services.txt:16546:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_to_frame.py
./services/all_services.txt:16547:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_fillna.py
./services/all_services.txt:16548:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_shift.py
./services/all_services.txt:16549:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_round.py
./services/all_services.txt:16550:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_to_julian_date.py
./services/all_services.txt:16551:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_factorize.py
./services/all_services.txt:16552:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_repeat.py
./services/all_services.txt:16553:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_to_pydatetime.py
./services/all_services.txt:16554:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/datetimes/methods/test_asof.py
./services/all_services.txt:16626:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_asfreq.py
./services/all_services.txt:16627:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_astype.py
./services/all_services.txt:16628:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_to_timestamp.py
./services/all_services.txt:16629:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_insert.py
./services/all_services.txt:16630:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/__init__.py
./services/all_services.txt:16631:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_fillna.py
./services/all_services.txt:16632:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_shift.py
./services/all_services.txt:16633:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_is_full.py
./services/all_services.txt:16634:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_factorize.py
./services/all_services.txt:16635:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/indexes/period/methods/test_repeat.py
./services/all_services.txt:16708:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/tests/extension/base/methods.py
./services/all_services.txt:16753:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/core/methods/describe.py
./services/all_services.txt:16754:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/core/methods/to_dict.py
./services/all_services.txt:16755:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/core/methods/selectn.py
./services/all_services.txt:16756:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/core/methods/__init__.py
./services/all_services.txt:16791:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/core/reshape/merge.py
./services/all_services.txt:16797:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/core/reshape/melt.py
./services/all_services.txt:16820:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/pandas/core/_numba/kernels/mean_.py
./services/all_services.txt:17183:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/scipy/_lib/pyprima/common/message.py
./services/all_services.txt:17929:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/scipy/ndimage/measurements.py
./services/all_services.txt:18001:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/export/__init__.py
./services/all_services.txt:18002:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement.py
./services/all_services.txt:18003:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/view.py
./services/all_services.txt:18004:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement_consumer.py
./services/all_services.txt:18005:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/export/__init__.py
./services/all_services.txt:18006:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/_view_instrument_match.py
./services/all_services.txt:18007:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/aggregation.py
./services/all_services.txt:18008:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exceptions.py
./services/all_services.txt:18009:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/instrument.py
./services/all_services.txt:18010:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py
./services/all_services.txt:18011:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/__init__.py
./services/all_services.txt:18012:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/buckets.py
./services/all_services.txt:18013:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/exponent_mapping.py
./services/all_services.txt:18014:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/errors.py
./services/all_services.txt:18015:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/logarithm_mapping.py
./services/all_services.txt:18016:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/__init__.py
./services/all_services.txt:18017:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/ieee_754.py
./services/all_services.txt:18018:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/point.py
./services/all_services.txt:18019:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/metric_reader_storage.py
./services/all_services.txt:18020:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar_filter.py
./services/all_services.txt:18021:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar_reservoir.py
./services/all_services.txt:18022:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/__init__.py
./services/all_services.txt:18023:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar.py
./services/all_services.txt:18024:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/sdk_configuration.py
./services/all_services.txt:18025:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/view/__init__.py
./services/all_services.txt:18026:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/metrics/__init__.py
./services/all_services.txt:18034:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/sdk/trace/_sampling_experimental/_parent_threshold.py
./services/all_services.txt:18058:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/metrics/db_metrics.py
./services/all_services.txt:18059:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/metrics/__init__.py
./services/all_services.txt:18060:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/metrics/http_metrics.py
./services/all_services.txt:18064:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/dns_metrics.py
./services/all_services.txt:18065:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cicd_metrics.py
./services/all_services.txt:18066:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/vcs_metrics.py
./services/all_services.txt:18067:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/db_metrics.py
./services/all_services.txt:18068:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/rpc_metrics.py
./services/all_services.txt:18069:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cpu_metrics.py
./services/all_services.txt:18070:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cpython_metrics.py
./services/all_services.txt:18071:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/gen_ai_metrics.py
./services/all_services.txt:18072:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/faas_metrics.py
./services/all_services.txt:18073:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/system_metrics.py
./services/all_services.txt:18074:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/process_metrics.py
./services/all_services.txt:18075:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/otel_metrics.py
./services/all_services.txt:18076:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/messaging_metrics.py
./services/all_services.txt:18077:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/hw_metrics.py
./services/all_services.txt:18078:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/k8s_metrics.py
./services/all_services.txt:18079:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/http_metrics.py
./services/all_services.txt:18080:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py
./services/all_services.txt:18081:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/azure_metrics.py
./services/all_services.txt:18083:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/message_attributes.py
./services/all_services.txt:18143:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/messaging_attributes.py
./services/all_services.txt:18175:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/metric_exporter/__init__.py
./services/all_services.txt:18178:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/common/metrics_encoder.py
./services/all_services.txt:18182:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/common/_internal/metrics_encoder/__init__.py
./services/all_services.txt:18187:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/metrics/_internal/instrument.py
./services/all_services.txt:18188:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/metrics/_internal/__init__.py
./services/all_services.txt:18189:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/metrics/_internal/observation.py
./services/all_services.txt:18190:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/metrics/__init__.py
./services/all_services.txt:18203:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/proto/metrics/v1/metrics_pb2.py
./services/all_services.txt:18204:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/proto/metrics/v1/__init__.py
./services/all_services.txt:18205:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/proto/metrics/__init__.py
./services/all_services.txt:18216:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/metrics_service_pb2_grpc.py
./services/all_services.txt:18217:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/metrics_service_pb2.py
./services/all_services.txt:18218:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/__init__.py
./services/all_services.txt:18219:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/__init__.py
./services/all_services.txt:18263:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/packaging/metadata.py
./services/all_services.txt:18320:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/jinja2/meta.py
./services/all_services.txt:18404:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/model_selection/tests/test_classification_threshold.py
./services/all_services.txt:18414:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/model_selection/_classification_threshold.py
./services/all_services.txt:18491:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/tests/metadata_routing_common.py
./services/all_services.txt:18644:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/utils/metadata_routing.py
./services/all_services.txt:18647:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/utils/metaestimators.py
./services/all_services.txt:18708:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_classification.py
./services/all_services.txt:18709:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_scorer.py
./services/all_services.txt:18710:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_base.py
./services/all_services.txt:18711:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_pairwise.py
./services/all_services.txt:18712:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_common.py
./services/all_services.txt:18713:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_ranking.py
./services/all_services.txt:18714:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_regression.py
./services/all_services.txt:18715:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_classification.py
./services/all_services.txt:18716:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_dist_metrics.py
./services/all_services.txt:18717:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/__init__.py
./services/all_services.txt:18718:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_score_objects.py
./services/all_services.txt:18719:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/tests/test_pairwise_distances_reduction.py
./services/all_services.txt:18720:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_ranking.py
./services/all_services.txt:18721:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_regression.py
./services/all_services.txt:18722:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/pairwise.py
./services/all_services.txt:18723:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/_bicluster.py
./services/all_services.txt:18724:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/tests/test_supervised.py
./services/all_services.txt:18725:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/tests/test_common.py
./services/all_services.txt:18726:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/tests/test_unsupervised.py
./services/all_services.txt:18727:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/tests/test_bicluster.py
./services/all_services.txt:18728:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/tests/__init__.py
./services/all_services.txt:18729:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/_supervised.py
./services/all_services.txt:18730:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/__init__.py
./services/all_services.txt:18731:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/cluster/_unsupervised.py
./services/all_services.txt:18732:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/__init__.py
./services/all_services.txt:18733:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/tests/test_confusion_matrix_display.py
./services/all_services.txt:18734:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/tests/test_det_curve_display.py
./services/all_services.txt:18735:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/tests/test_roc_curve_display.py
./services/all_services.txt:18736:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/tests/test_common_curve_display.py
./services/all_services.txt:18737:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/tests/test_predict_error_display.py
./services/all_services.txt:18738:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/tests/__init__.py
./services/all_services.txt:18739:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/tests/test_precision_recall_display.py
./services/all_services.txt:18740:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/regression.py
./services/all_services.txt:18741:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/det_curve.py
./services/all_services.txt:18742:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/roc_curve.py
./services/all_services.txt:18743:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/precision_recall_curve.py
./services/all_services.txt:18744:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/__init__.py
./services/all_services.txt:18745:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_plot/confusion_matrix.py
./services/all_services.txt:18746:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_pairwise_distances_reduction/_dispatcher.py
./services/all_services.txt:18747:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/metrics/_pairwise_distances_reduction/__init__.py
./services/all_services.txt:18816:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/feature_selection/tests/test_variance_threshold.py
./services/all_services.txt:18819:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/sklearn/feature_selection/_variance_threshold.py
./services/all_services.txt:18989:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/setuptools/_vendor/wheel/metadata.py
./services/all_services.txt:19025:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/setuptools/_vendor/typeguard/_suppression.py
./services/all_services.txt:19052:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/setuptools/_vendor/packaging/metadata.py
./services/all_services.txt:19321:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/prometheus_fastapi_instrumentator/metrics.py
./services/all_services.txt:19323:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/errors.py
./services/all_services.txt:19324:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/pre_configured.py
./services/all_services.txt:19325:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/revocation.py
./services/all_services.txt:19326:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/resource.py
./services/all_services.txt:19327:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/metadata.py
./services/all_services.txt:19328:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/__init__.py
./services/all_services.txt:19329:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/authorization.py
./services/all_services.txt:19330:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/introspect.py
./services/all_services.txt:19331:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/base.py
./services/all_services.txt:19332:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/token.py
./services/all_services.txt:19333:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/mobile_application.py
./services/all_services.txt:19334:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/legacy_application.py
./services/all_services.txt:19335:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/backend_application.py
./services/all_services.txt:19336:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/service_application.py
./services/all_services.txt:19337:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/__init__.py
./services/all_services.txt:19338:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/web_application.py
./services/all_services.txt:19339:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/base.py
./services/all_services.txt:19340:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/parameters.py
./services/all_services.txt:19341:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/resource_owner_password_credentials.py
./services/all_services.txt:19342:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/__init__.py
./services/all_services.txt:19343:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/client_credentials.py
./services/all_services.txt:19344:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/implicit.py
./services/all_services.txt:19345:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/refresh_token.py
./services/all_services.txt:19346:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/base.py
./services/all_services.txt:19347:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/authorization_code.py
./services/all_services.txt:19348:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/request_validator.py
./services/all_services.txt:19349:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/__init__.py
./services/all_services.txt:19350:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/utils.py
./services/all_services.txt:19351:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/tokens.py
./services/all_services.txt:19352:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/errors.py
./services/all_services.txt:19353:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/pre_configured.py
./services/all_services.txt:19354:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/__init__.py
./services/all_services.txt:19355:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/device_authorization.py
./services/all_services.txt:19356:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/clients/device.py
./services/all_services.txt:19357:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/clients/__init__.py
./services/all_services.txt:19358:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/grant_types/__init__.py
./services/all_services.txt:19359:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/grant_types/device_code.py
./services/all_services.txt:19360:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/request_validator.py
./services/all_services.txt:19361:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/__init__.py
./services/all_services.txt:19362:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth2/__init__.py
./services/all_services.txt:19363:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/__init__.py
./services/all_services.txt:19364:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/signature.py
./services/all_services.txt:19365:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/errors.py
./services/all_services.txt:19366:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/pre_configured.py
./services/all_services.txt:19367:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/resource.py
./services/all_services.txt:19368:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/access_token.py
./services/all_services.txt:19369:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/__init__.py
./services/all_services.txt:19370:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/authorization.py
./services/all_services.txt:19371:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/request_token.py
./services/all_services.txt:19372:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/signature_only.py
./services/all_services.txt:19373:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/base.py
./services/all_services.txt:19374:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/parameters.py
./services/all_services.txt:19375:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/request_validator.py
./services/all_services.txt:19376:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/__init__.py
./services/all_services.txt:19377:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/utils.py
./services/all_services.txt:19378:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/uri_validate.py
./services/all_services.txt:19379:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/__init__.py
./services/all_services.txt:19380:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/common.py
./services/all_services.txt:19381:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/signals.py
./services/all_services.txt:19382:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/__init__.py
./services/all_services.txt:19383:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/pre_configured.py
./services/all_services.txt:19384:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/userinfo.py
./services/all_services.txt:19385:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/__init__.py
./services/all_services.txt:19386:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/exceptions.py
./services/all_services.txt:19387:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/dispatchers.py
./services/all_services.txt:19388:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/__init__.py
./services/all_services.txt:19389:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/hybrid.py
./services/all_services.txt:19390:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/implicit.py
./services/all_services.txt:19391:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/refresh_token.py
./services/all_services.txt:19392:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/base.py
./services/all_services.txt:19393:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/authorization_code.py
./services/all_services.txt:19394:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/request_validator.py
./services/all_services.txt:19395:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/__init__.py
./services/all_services.txt:19396:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/core/tokens.py
./services/all_services.txt:19397:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/oauthlib/openid/connect/__init__.py
./services/all_services.txt:19442:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/aiohttp/client_middleware_digest_auth.py
./services/all_services.txt:19509:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/fsspec/implementations/memory.py
./services/all_services.txt:19541:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/auth/utils/__init__.py
./services/all_services.txt:19542:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py
./services/all_services.txt:19543:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/auth/__init__.py
./services/all_services.txt:19544:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py
./services/all_services.txt:19545:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/auth/simple_rbac_authz/__init__.py
./services/all_services.txt:19565:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/test/auth/test_auth_utils.py
./services/all_services.txt:19608:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/test/client/create_http_client_with_basic_auth.py
./services/all_services.txt:19609:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/test/client/test_database_tenant_auth.py
./services/all_services.txt:19646:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/utils/messageid.py
./services/all_services.txt:19697:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/chromadb/segment/impl/metadata/sqlite.py
./services/all_services.txt:19870:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/utils/metrics.py
./services/all_services.txt:19907:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/data/metrics/squad_metrics.py
./services/all_services.txt:19908:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/data/metrics/__init__.py
./services/all_services.txt:20519:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/metaclip_2/configuration_metaclip_2.py
./services/all_services.txt:20520:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/metaclip_2/__init__.py
./services/all_services.txt:20521:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/metaclip_2/modeling_metaclip_2.py
./services/all_services.txt:20522:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/metaclip_2/modular_metaclip_2.py
./services/all_services.txt:20634:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/megatron_gpt2/__init__.py
./services/all_services.txt:20635:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/megatron_gpt2/checkpoint_reshaping_and_interoperability.py
./services/all_services.txt:20784:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/megatron_bert/modeling_megatron_bert.py
./services/all_services.txt:20785:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/megatron_bert/__init__.py
./services/all_services.txt:20786:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/megatron_bert/configuration_megatron_bert.py
./services/all_services.txt:21477:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/deprecated/mega/modeling_mega.py
./services/all_services.txt:21478:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/deprecated/mega/configuration_mega.py
./services/all_services.txt:21479:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/transformers/models/deprecated/mega/__init__.py
./services/all_services.txt:21978:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/memory_profiler.py
./services/all_services.txt:22304:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/numpy/_core/memmap.py
./services/all_services.txt:22664:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/anyio/streams/memory.py
./services/all_services.txt:22680:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/starlette/middleware/authentication.py
./services/all_services.txt:22692:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/starlette/authentication.py
./services/all_services.txt:22704:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_refresh_worker.py
./services/all_services.txt:22705:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/compute_engine/credentials.py
./services/all_services.txt:22706:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/compute_engine/_metadata.py
./services/all_services.txt:22707:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/compute_engine/__init__.py
./services/all_services.txt:22708:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_credentials_base.py
./services/all_services.txt:22709:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_oauth2client.py
./services/all_services.txt:22710:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/iam.py
./services/all_services.txt:22711:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/version.py
./services/all_services.txt:22712:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/downscoped.py
./services/all_services.txt:22713:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_helpers.py
./services/all_services.txt:22714:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/external_account_authorized_user.py
./services/all_services.txt:22715:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/impersonated_credentials.py
./services/all_services.txt:22716:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/credentials.py
./services/all_services.txt:22717:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/exceptions.py
./services/all_services.txt:22718:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_default_async.py
./services/all_services.txt:22719:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/aio/_helpers.py
./services/all_services.txt:22720:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/aio/credentials.py
./services/all_services.txt:22721:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/aio/__init__.py
./services/all_services.txt:22722:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/aio/transport/aiohttp.py
./services/all_services.txt:22723:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/aio/transport/__init__.py
./services/all_services.txt:22724:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/aio/transport/sessions.py
./services/all_services.txt:22725:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/aws.py
./services/all_services.txt:22726:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/environment_vars.py
./services/all_services.txt:22727:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_service_account_info.py
./services/all_services.txt:22728:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/app_engine.py
./services/all_services.txt:22729:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/__init__.py
./services/all_services.txt:22730:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_credentials_async.py
./services/all_services.txt:22731:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_constants.py
./services/all_services.txt:22732:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/pluggable.py
./services/all_services.txt:22733:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/metrics.py
./services/all_services.txt:22734:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/_custom_tls_signer.py
./services/all_services.txt:22735:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/grpc.py
./services/all_services.txt:22736:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/mtls.py
./services/all_services.txt:22737:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/__init__.py
./services/all_services.txt:22738:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/_requests_base.py
./services/all_services.txt:22739:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/urllib3.py
./services/all_services.txt:22740:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/_http_client.py
./services/all_services.txt:22741:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/_aiohttp_requests.py
./services/all_services.txt:22742:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/_mtls_helper.py
./services/all_services.txt:22743:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/transport/requests.py
./services/all_services.txt:22744:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/external_account.py
./services/all_services.txt:22745:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/identity_pool.py
./services/all_services.txt:22746:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/jwt.py
./services/all_services.txt:22747:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_cloud_sdk.py
./services/all_services.txt:22748:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_jwt_async.py
./services/all_services.txt:22749:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/crypt/_helpers.py
./services/all_services.txt:22750:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/crypt/_cryptography_rsa.py
./services/all_services.txt:22751:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/crypt/_python_rsa.py
./services/all_services.txt:22752:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/crypt/rsa.py
./services/all_services.txt:22753:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/crypt/es256.py
./services/all_services.txt:22754:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/crypt/__init__.py
./services/all_services.txt:22755:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/crypt/base.py
./services/all_services.txt:22756:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/api_key.py
./services/all_services.txt:22757:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_exponential_backoff.py
./services/all_services.txt:22758:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/auth/_default.py
./services/all_services.txt:22771:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/api/auth_pb2.py
./services/all_services.txt:22778:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/api/metric_pb2.py
./services/all_services.txt:22792:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/_client_async.py
./services/all_services.txt:22793:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/id_token.py
./services/all_services.txt:22794:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/_client.py
./services/all_services.txt:22795:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/webauthn_types.py
./services/all_services.txt:22796:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/credentials.py
./services/all_services.txt:22797:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/_id_token_async.py
./services/all_services.txt:22798:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/reauth.py
./services/all_services.txt:22799:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/_service_account_async.py
./services/all_services.txt:22800:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/challenges.py
./services/all_services.txt:22801:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/webauthn_handler_factory.py
./services/all_services.txt:22802:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/__init__.py
./services/all_services.txt:22803:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/_credentials_async.py
./services/all_services.txt:22804:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/gdch_credentials.py
./services/all_services.txt:22805:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/webauthn_handler.py
./services/all_services.txt:22806:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/sts.py
./services/all_services.txt:22807:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/utils.py
./services/all_services.txt:22808:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/service_account.py
./services/all_services.txt:22809:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/oauth2/_reauth_async.py
./services/all_services.txt:22818:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/gapic/metadata/gapic_metadata_pb2.py
./services/all_services.txt:22830:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/protobuf/message_factory.py
./services/all_services.txt:22854:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/protobuf/internal/message_listener.py
./services/all_services.txt:22857:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/google/protobuf/message.py
./services/all_services.txt:22986:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/joblib/memory.py
./services/all_services.txt:23029:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/httpx/_auth.py
./services/all_services.txt:23144:/home/ms-jarvis/msjarvis-rebuild/services/chromadb_env/lib/python3.12/site-packages/torchgen/api/meta.py
./services/all_services.txt:23356:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/uvicorn/middleware/message_logger.py
./services/all_services.txt:23410:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/fastapi/security/oauth2.py
./services/all_services.txt:23470:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_services.txt:23495:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py
./services/all_services.txt:23561:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_services.txt:23740:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/languages.py
./services/all_services.txt:23741:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/__init__.py
./services/all_services.txt:23800:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_services.txt:23801:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_services.txt:23802:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_services.txt:23803:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_services.txt:23804:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_services.txt:23805:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_services.txt:23806:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_services.txt:23807:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_services.txt:23813:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_services.txt:23817:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_services.txt:23830:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_services.txt:23831:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_legacy.py
./services/all_services.txt:23834:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_services.txt:23986:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/anyio/streams/memory.py
./services/all_services.txt:24002:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/starlette/middleware/authentication.py
./services/all_services.txt:24013:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain.empty/mother_carrie_protocols/venv_mother/lib/python3.12/site-packages/starlette/authentication.py
./services/all_services.txt:24094:/home/ms-jarvis/msjarvis-rebuild/services/user_auth_service.py
./services/all_services.txt:24289:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/multiaddr/codecs/memory.py
./services/all_services.txt:24402:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/huggingface_hub/utils/_auth.py
./services/all_services.txt:24429:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/huggingface_hub/_oauth.py
./services/all_services.txt:24444:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/huggingface_hub/cli/auth.py
./services/all_services.txt:24475:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/websockets/legacy/auth.py
./services/all_services.txt:24484:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/websockets/auth.py
./services/all_services.txt:24494:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/websockets/asyncio/messages.py
./services/all_services.txt:24501:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/websockets/sync/messages.py
./services/all_services.txt:24578:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests/auth.py
./services/all_services.txt:24587:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/redis/auth/__init__.py
./services/all_services.txt:24588:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/redis/auth/token_manager.py
./services/all_services.txt:24589:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/redis/auth/err.py
./services/all_services.txt:24590:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/redis/auth/idp.py
./services/all_services.txt:24591:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/redis/auth/token.py
./services/all_services.txt:24712:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/dns/message.py
./services/all_services.txt:25023:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/grpc/_auth.py
./services/all_services.txt:25378:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/joint.py
./services/all_services.txt:25379:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/linearize.py
./services/all_services.txt:25380:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/models.py
./services/all_services.txt:25381:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/lagrange.py
./services/all_services.txt:25382:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_rigidbody.py
./services/all_services.txt:25383:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_actuator.py
./services/all_services.txt:25384:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane3.py
./services/all_services.txt:25385:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_body.py
./services/all_services.txt:25386:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_system_class.py
./services/all_services.txt:25387:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_loads.py
./services/all_services.txt:25388:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane4.py
./services/all_services.txt:25389:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane5.py
./services/all_services.txt:25390:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_models.py
./services/all_services.txt:25391:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_method.py
./services/all_services.txt:25392:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_wrapping_geometry.py
./services/all_services.txt:25393:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_lagrange2.py
./services/all_services.txt:25394:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_linearity_of_velocity_constraints.py
./services/all_services.txt:25395:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_system.py
./services/all_services.txt:25396:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_functions.py
./services/all_services.txt:25397:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_inertia.py
./services/all_services.txt:25398:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/__init__.py
./services/all_services.txt:25399:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_pathway.py
./services/all_services.txt:25400:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_lagrange.py
./services/all_services.txt:25401:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane2.py
./services/all_services.txt:25402:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_particle.py
./services/all_services.txt:25403:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_joint.py
./services/all_services.txt:25404:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_linearize.py
./services/all_services.txt:25405:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_kane.py
./services/all_services.txt:25406:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/tests/test_jointsmethod.py
./services/all_services.txt:25407:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/jointsmethod.py
./services/all_services.txt:25408:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/rigidbody.py
./services/all_services.txt:25409:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/body_base.py
./services/all_services.txt:25410:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/loads.py
./services/all_services.txt:25411:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/pathway.py
./services/all_services.txt:25412:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/__init__.py
./services/all_services.txt:25413:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/inertia.py
./services/all_services.txt:25414:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/particle.py
./services/all_services.txt:25415:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/method.py
./services/all_services.txt:25416:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/body.py
./services/all_services.txt:25417:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/kane.py
./services/all_services.txt:25418:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/system.py
./services/all_services.txt:25419:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/wrapping_geometry.py
./services/all_services.txt:25420:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/actuator.py
./services/all_services.txt:25421:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/mechanics/functions.py
./services/all_services.txt:25452:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/physics/optics/medium.py
./services/all_services.txt:26117:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/integrals/meijerint.py
./services/all_services.txt:26152:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/integrals/meijerint_doc.py
./services/all_services.txt:26600:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/sympy/utilities/memoization.py
./services/all_services.txt:26645:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/oauth2_session.py
./services/all_services.txt:26646:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/slack.py
./services/all_services.txt:26647:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/facebook.py
./services/all_services.txt:26648:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/plentymarkets.py
./services/all_services.txt:26649:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/ebay.py
./services/all_services.txt:26650:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/__init__.py
./services/all_services.txt:26651:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/douban.py
./services/all_services.txt:26652:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/instagram.py
./services/all_services.txt:26653:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/mailchimp.py
./services/all_services.txt:26654:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/fitbit.py
./services/all_services.txt:26655:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/compliance_fixes/weibo.py
./services/all_services.txt:26656:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/oauth1_auth.py
./services/all_services.txt:26657:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/__init__.py
./services/all_services.txt:26658:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/oauth2_auth.py
./services/all_services.txt:26659:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/requests_oauthlib/oauth1_session.py
./services/all_services.txt:27023:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/onnxruntime/transformers/metrics.py
./services/all_services.txt:27090:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/uvicorn/middleware/message_logger.py
./services/all_services.txt:27236:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_services.txt:27291:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_services.txt:27384:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_vendor/packaging/metadata.py
./services/all_services.txt:27463:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_services.txt:27464:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_services.txt:27465:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_services.txt:27466:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_services.txt:27467:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_services.txt:27468:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_services.txt:27469:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_services.txt:27470:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_services.txt:27476:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_services.txt:27480:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_services.txt:27492:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_services.txt:27494:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_services.txt:27838:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pygments/lexers/meson.py
./services/all_services.txt:28109:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/kubernetes/client/api/authorization_v1_api.py
./services/all_services.txt:28115:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/kubernetes/client/api/rbac_authorization_api.py
./services/all_services.txt:28119:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/kubernetes/client/api/authentication_v1_api.py
./services/all_services.txt:28127:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/kubernetes/client/api/authorization_api.py
./services/all_services.txt:28135:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/kubernetes/client/api/rbac_authorization_v1_api.py
./services/all_services.txt:28145:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/kubernetes/client/api/authentication_api.py
./services/all_services.txt:28389:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/kubernetes/client/models/authentication_v1_token_request.py
./services/all_services.txt:28902:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/rich/measure.py
./services/all_services.txt:29011:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/export/__init__.py
./services/all_services.txt:29012:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement.py
./services/all_services.txt:29013:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/view.py
./services/all_services.txt:29014:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement_consumer.py
./services/all_services.txt:29015:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/export/__init__.py
./services/all_services.txt:29016:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/_view_instrument_match.py
./services/all_services.txt:29017:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/aggregation.py
./services/all_services.txt:29018:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exceptions.py
./services/all_services.txt:29019:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/instrument.py
./services/all_services.txt:29020:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py
./services/all_services.txt:29021:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/__init__.py
./services/all_services.txt:29022:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/buckets.py
./services/all_services.txt:29023:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/exponent_mapping.py
./services/all_services.txt:29024:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/errors.py
./services/all_services.txt:29025:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/logarithm_mapping.py
./services/all_services.txt:29026:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/__init__.py
./services/all_services.txt:29027:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/ieee_754.py
./services/all_services.txt:29028:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/point.py
./services/all_services.txt:29029:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/metric_reader_storage.py
./services/all_services.txt:29030:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar_filter.py
./services/all_services.txt:29031:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar_reservoir.py
./services/all_services.txt:29032:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/__init__.py
./services/all_services.txt:29033:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exemplar/exemplar.py
./services/all_services.txt:29034:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/sdk_configuration.py
./services/all_services.txt:29035:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/view/__init__.py
./services/all_services.txt:29036:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/metrics/__init__.py
./services/all_services.txt:29044:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/sdk/trace/_sampling_experimental/_parent_threshold.py
./services/all_services.txt:29068:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/metrics/db_metrics.py
./services/all_services.txt:29069:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/metrics/__init__.py
./services/all_services.txt:29070:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/metrics/http_metrics.py
./services/all_services.txt:29074:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/dns_metrics.py
./services/all_services.txt:29075:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cicd_metrics.py
./services/all_services.txt:29076:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/vcs_metrics.py
./services/all_services.txt:29077:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/db_metrics.py
./services/all_services.txt:29078:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/rpc_metrics.py
./services/all_services.txt:29079:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cpu_metrics.py
./services/all_services.txt:29080:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/cpython_metrics.py
./services/all_services.txt:29081:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/gen_ai_metrics.py
./services/all_services.txt:29082:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/faas_metrics.py
./services/all_services.txt:29083:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/system_metrics.py
./services/all_services.txt:29084:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/process_metrics.py
./services/all_services.txt:29085:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/otel_metrics.py
./services/all_services.txt:29086:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/messaging_metrics.py
./services/all_services.txt:29087:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/hw_metrics.py
./services/all_services.txt:29088:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/k8s_metrics.py
./services/all_services.txt:29089:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/http_metrics.py
./services/all_services.txt:29090:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py
./services/all_services.txt:29091:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/azure_metrics.py
./services/all_services.txt:29093:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/message_attributes.py
./services/all_services.txt:29153:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/messaging_attributes.py
./services/all_services.txt:29185:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/metric_exporter/__init__.py
./services/all_services.txt:29188:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/common/metrics_encoder.py
./services/all_services.txt:29192:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/common/_internal/metrics_encoder/__init__.py
./services/all_services.txt:29197:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/metrics/_internal/instrument.py
./services/all_services.txt:29198:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/metrics/_internal/__init__.py
./services/all_services.txt:29199:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/metrics/_internal/observation.py
./services/all_services.txt:29200:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/metrics/__init__.py
./services/all_services.txt:29213:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/proto/metrics/v1/metrics_pb2.py
./services/all_services.txt:29214:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/proto/metrics/v1/__init__.py
./services/all_services.txt:29215:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/proto/metrics/__init__.py
./services/all_services.txt:29226:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/metrics_service_pb2_grpc.py
./services/all_services.txt:29227:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/metrics_service_pb2.py
./services/all_services.txt:29228:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/v1/__init__.py
./services/all_services.txt:29229:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/opentelemetry/proto/collector/metrics/__init__.py
./services/all_services.txt:29273:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/pymysql/_auth.py
./services/all_services.txt:29288:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/packaging/metadata.py
./services/all_services.txt:29356:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/errors.py
./services/all_services.txt:29357:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/pre_configured.py
./services/all_services.txt:29358:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/revocation.py
./services/all_services.txt:29359:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/resource.py
./services/all_services.txt:29360:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/metadata.py
./services/all_services.txt:29361:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/__init__.py
./services/all_services.txt:29362:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/authorization.py
./services/all_services.txt:29363:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/introspect.py
./services/all_services.txt:29364:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/base.py
./services/all_services.txt:29365:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/endpoints/token.py
./services/all_services.txt:29366:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/mobile_application.py
./services/all_services.txt:29367:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/legacy_application.py
./services/all_services.txt:29368:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/backend_application.py
./services/all_services.txt:29369:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/service_application.py
./services/all_services.txt:29370:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/__init__.py
./services/all_services.txt:29371:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/web_application.py
./services/all_services.txt:29372:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/clients/base.py
./services/all_services.txt:29373:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/parameters.py
./services/all_services.txt:29374:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/resource_owner_password_credentials.py
./services/all_services.txt:29375:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/__init__.py
./services/all_services.txt:29376:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/client_credentials.py
./services/all_services.txt:29377:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/implicit.py
./services/all_services.txt:29378:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/refresh_token.py
./services/all_services.txt:29379:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/base.py
./services/all_services.txt:29380:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/grant_types/authorization_code.py
./services/all_services.txt:29381:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/request_validator.py
./services/all_services.txt:29382:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/__init__.py
./services/all_services.txt:29383:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/utils.py
./services/all_services.txt:29384:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc6749/tokens.py
./services/all_services.txt:29385:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/errors.py
./services/all_services.txt:29386:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/pre_configured.py
./services/all_services.txt:29387:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/__init__.py
./services/all_services.txt:29388:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/endpoints/device_authorization.py
./services/all_services.txt:29389:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/clients/device.py
./services/all_services.txt:29390:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/clients/__init__.py
./services/all_services.txt:29391:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/grant_types/__init__.py
./services/all_services.txt:29392:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/grant_types/device_code.py
./services/all_services.txt:29393:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/request_validator.py
./services/all_services.txt:29394:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/rfc8628/__init__.py
./services/all_services.txt:29395:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth2/__init__.py
./services/all_services.txt:29396:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/__init__.py
./services/all_services.txt:29397:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/signature.py
./services/all_services.txt:29398:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/errors.py
./services/all_services.txt:29399:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/pre_configured.py
./services/all_services.txt:29400:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/resource.py
./services/all_services.txt:29401:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/access_token.py
./services/all_services.txt:29402:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/__init__.py
./services/all_services.txt:29403:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/authorization.py
./services/all_services.txt:29404:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/request_token.py
./services/all_services.txt:29405:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/signature_only.py
./services/all_services.txt:29406:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/endpoints/base.py
./services/all_services.txt:29407:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/parameters.py
./services/all_services.txt:29408:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/request_validator.py
./services/all_services.txt:29409:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/__init__.py
./services/all_services.txt:29410:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/oauth1/rfc5849/utils.py
./services/all_services.txt:29411:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/uri_validate.py
./services/all_services.txt:29412:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/__init__.py
./services/all_services.txt:29413:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/common.py
./services/all_services.txt:29414:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/signals.py
./services/all_services.txt:29415:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/__init__.py
./services/all_services.txt:29416:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/pre_configured.py
./services/all_services.txt:29417:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/userinfo.py
./services/all_services.txt:29418:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/endpoints/__init__.py
./services/all_services.txt:29419:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/exceptions.py
./services/all_services.txt:29420:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/dispatchers.py
./services/all_services.txt:29421:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/__init__.py
./services/all_services.txt:29422:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/hybrid.py
./services/all_services.txt:29423:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/implicit.py
./services/all_services.txt:29424:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/refresh_token.py
./services/all_services.txt:29425:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/base.py
./services/all_services.txt:29426:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/grant_types/authorization_code.py
./services/all_services.txt:29427:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/request_validator.py
./services/all_services.txt:29428:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/__init__.py
./services/all_services.txt:29429:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/core/tokens.py
./services/all_services.txt:29430:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/oauthlib/openid/connect/__init__.py
./services/all_services.txt:29487:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/fsspec/implementations/memory.py
./services/all_services.txt:29519:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/auth/utils/__init__.py
./services/all_services.txt:29520:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py
./services/all_services.txt:29521:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/auth/__init__.py
./services/all_services.txt:29522:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py
./services/all_services.txt:29523:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/auth/simple_rbac_authz/__init__.py
./services/all_services.txt:29543:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/test/auth/test_auth_utils.py
./services/all_services.txt:29586:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/test/client/create_http_client_with_basic_auth.py
./services/all_services.txt:29587:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/test/client/test_database_tenant_auth.py
./services/all_services.txt:29624:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/utils/messageid.py
./services/all_services.txt:29675:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/chromadb/segment/impl/metadata/sqlite.py
./services/all_services.txt:29859:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/neo4j/_async/auth_management.py
./services/all_services.txt:29897:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/neo4j/_sync/auth_management.py
./services/all_services.txt:29911:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/neo4j/_auth_management.py
./services/all_services.txt:29916:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/neo4j/auth_management.py
./services/all_services.txt:30178:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/numpy/_core/memmap.py
./services/all_services.txt:30508:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/anyio/streams/memory.py
./services/all_services.txt:30665:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_refresh_worker.py
./services/all_services.txt:30666:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/compute_engine/credentials.py
./services/all_services.txt:30667:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/compute_engine/_metadata.py
./services/all_services.txt:30668:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/compute_engine/__init__.py
./services/all_services.txt:30669:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_credentials_base.py
./services/all_services.txt:30670:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_oauth2client.py
./services/all_services.txt:30671:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/iam.py
./services/all_services.txt:30672:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/version.py
./services/all_services.txt:30673:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/downscoped.py
./services/all_services.txt:30674:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_helpers.py
./services/all_services.txt:30675:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/external_account_authorized_user.py
./services/all_services.txt:30676:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/impersonated_credentials.py
./services/all_services.txt:30677:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/credentials.py
./services/all_services.txt:30678:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/exceptions.py
./services/all_services.txt:30679:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_default_async.py
./services/all_services.txt:30680:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/aio/_helpers.py
./services/all_services.txt:30681:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/aio/credentials.py
./services/all_services.txt:30682:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/aio/__init__.py
./services/all_services.txt:30683:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/aio/transport/aiohttp.py
./services/all_services.txt:30684:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/aio/transport/__init__.py
./services/all_services.txt:30685:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/aio/transport/sessions.py
./services/all_services.txt:30686:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/aws.py
./services/all_services.txt:30687:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/environment_vars.py
./services/all_services.txt:30688:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_service_account_info.py
./services/all_services.txt:30689:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/app_engine.py
./services/all_services.txt:30690:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/__init__.py
./services/all_services.txt:30691:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_credentials_async.py
./services/all_services.txt:30692:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_constants.py
./services/all_services.txt:30693:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/pluggable.py
./services/all_services.txt:30694:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/metrics.py
./services/all_services.txt:30695:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/_custom_tls_signer.py
./services/all_services.txt:30696:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/grpc.py
./services/all_services.txt:30697:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/mtls.py
./services/all_services.txt:30698:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/__init__.py
./services/all_services.txt:30699:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/_requests_base.py
./services/all_services.txt:30700:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/urllib3.py
./services/all_services.txt:30701:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/_http_client.py
./services/all_services.txt:30702:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/_aiohttp_requests.py
./services/all_services.txt:30703:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/_mtls_helper.py
./services/all_services.txt:30704:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/transport/requests.py
./services/all_services.txt:30705:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/external_account.py
./services/all_services.txt:30706:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/identity_pool.py
./services/all_services.txt:30707:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/jwt.py
./services/all_services.txt:30708:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_cloud_sdk.py
./services/all_services.txt:30709:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_jwt_async.py
./services/all_services.txt:30710:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/crypt/_helpers.py
./services/all_services.txt:30711:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/crypt/_cryptography_rsa.py
./services/all_services.txt:30712:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/crypt/_python_rsa.py
./services/all_services.txt:30713:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/crypt/rsa.py
./services/all_services.txt:30714:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/crypt/es256.py
./services/all_services.txt:30715:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/crypt/__init__.py
./services/all_services.txt:30716:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/crypt/base.py
./services/all_services.txt:30717:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/api_key.py
./services/all_services.txt:30718:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_exponential_backoff.py
./services/all_services.txt:30719:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/auth/_default.py
./services/all_services.txt:30732:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/api/auth_pb2.py
./services/all_services.txt:30739:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/api/metric_pb2.py
./services/all_services.txt:30753:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/_client_async.py
./services/all_services.txt:30754:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/id_token.py
./services/all_services.txt:30755:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/_client.py
./services/all_services.txt:30756:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/webauthn_types.py
./services/all_services.txt:30757:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/credentials.py
./services/all_services.txt:30758:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/_id_token_async.py
./services/all_services.txt:30759:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/reauth.py
./services/all_services.txt:30760:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/_service_account_async.py
./services/all_services.txt:30761:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/challenges.py
./services/all_services.txt:30762:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/webauthn_handler_factory.py
./services/all_services.txt:30763:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/__init__.py
./services/all_services.txt:30764:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/_credentials_async.py
./services/all_services.txt:30765:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/gdch_credentials.py
./services/all_services.txt:30766:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/webauthn_handler.py
./services/all_services.txt:30767:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/sts.py
./services/all_services.txt:30768:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/utils.py
./services/all_services.txt:30769:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/service_account.py
./services/all_services.txt:30770:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/oauth2/_reauth_async.py
./services/all_services.txt:30779:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/gapic/metadata/gapic_metadata_pb2.py
./services/all_services.txt:30791:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/protobuf/message_factory.py
./services/all_services.txt:30815:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/protobuf/internal/message_listener.py
./services/all_services.txt:30818:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/google/protobuf/message.py
./services/all_services.txt:30917:/home/ms-jarvis/msjarvis-rebuild/services/.venv/lib/python3.12/site-packages/httpx/_auth.py
./services/all_services.txt:31032:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_services.txt:31057:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py
./services/all_services.txt:31123:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_services.txt:31302:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/languages.py
./services/all_services.txt:31303:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/__init__.py
./services/all_services.txt:31362:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_services.txt:31363:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_services.txt:31364:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_services.txt:31365:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_services.txt:31366:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_services.txt:31367:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_services.txt:31368:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_services.txt:31369:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_services.txt:31375:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_services.txt:31379:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_services.txt:31392:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_services.txt:31393:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_legacy.py
./services/all_services.txt:31396:/home/ms-jarvis/msjarvis-rebuild/services/dataproc_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_services.txt:31498:/home/ms-jarvis/msjarvis-rebuild/services/messenger_service_fixed.py
./services/all_services.txt:31520:/home/ms-jarvis/msjarvis-rebuild/services/wvu_ldap_auth.py
./services/all_services.txt:31547:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain/i_containers/i_container_1/memory_self/__init__.py
./services/all_services.txt:31551:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain/i_containers/i_container_2/metacognitive_awareness/__init__.py
./services/all_services.txt:31591:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain/qualia_engine/meaning_maker/meaning_maker.py
./services/all_services.txt:31592:/home/ms-jarvis/msjarvis-rebuild/services/neurobiological_brain/qualia_engine/meaning_maker/__init__.py
./services/all_services.txt:31608:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_authentic_multi_llm.py
./services/all_services.txt:31664:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_services.txt:31689:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py
./services/all_services.txt:31755:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_services.txt:31934:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/languages.py
./services/all_services.txt:31935:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/__init__.py
./services/all_services.txt:31994:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_services.txt:31995:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_services.txt:31996:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_services.txt:31997:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_services.txt:31998:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_services.txt:31999:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_services.txt:32000:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_services.txt:32001:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_services.txt:32007:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_services.txt:32011:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_services.txt:32024:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_services.txt:32025:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_legacy.py
./services/all_services.txt:32028:/home/ms-jarvis/msjarvis-rebuild/services/gis_env/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_services.txt:32149:/home/ms-jarvis/msjarvis-rebuild/services/egeria_web_ui_plain_authentic.py
./services/all_services.txt:32175:/home/ms-jarvis/msjarvis-rebuild/services/oauth2_callback.py
./services/all_services.txt:32196:/home/ms-jarvis/msjarvis-rebuild/services/metrics_service.py
./services/all_services.txt:32204:/home/ms-jarvis/msjarvis-rebuild/services/oauth2_handler.py
./services/all_services.txt:32317:/home/ms-jarvis/msjarvis-rebuild/services/backups/pre_integration_20251012_115827/mamma_kidd_auth.py
./services/all_services.txt:32364:/home/ms-jarvis/msjarvis-rebuild/services/memory_manager.py
./services/all_services.txt:32426:/home/ms-jarvis/msjarvis-rebuild/services/method_tracker_decorator.py
./services/all_services.txt:32464:/home/ms-jarvis/msjarvis-rebuild/services/mesh_coordinator_interface.py
./services/all_services.txt:32473:/home/ms-jarvis/msjarvis-rebuild/services/mamma_kidd_auth.py
./services/all_services.txt:32597:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/requests/auth.py
./services/all_services.txt:32624:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/mex.py
./services/all_services.txt:32626:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/auth_scheme.py
./services/all_services.txt:32633:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/authority.py
./services/all_services.txt:32635:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/oauth2cli/http.py
./services/all_services.txt:32636:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/oauth2cli/authcode.py
./services/all_services.txt:32637:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/oauth2cli/assertion.py
./services/all_services.txt:32638:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/oauth2cli/__init__.py
./services/all_services.txt:32639:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/oauth2cli/oauth2.py
./services/all_services.txt:32640:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/msal/oauth2cli/oidc.py
./services/all_services.txt:32698:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_vendor/requests/auth.py
./services/all_services.txt:32723:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_vendor/distlib/metadata.py
./services/all_services.txt:32789:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_vendor/rich/measure.py
./services/all_services.txt:32968:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/languages.py
./services/all_services.txt:32969:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_vendor/chardet/metadata/__init__.py
./services/all_services.txt:33028:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/pkg_resources.py
./services/all_services.txt:33029:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/_json.py
./services/all_services.txt:33030:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/__init__.py
./services/all_services.txt:33031:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_compat.py
./services/all_services.txt:33032:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_envs.py
./services/all_services.txt:33033:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/__init__.py
./services/all_services.txt:33034:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/importlib/_dists.py
./services/all_services.txt:33035:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/metadata/base.py
./services/all_services.txt:33041:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py
./services/all_services.txt:33045:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/network/auth.py
./services/all_services.txt:33058:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_editable.py
./services/all_services.txt:33059:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata_legacy.py
./services/all_services.txt:33062:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/pip/_internal/operations/build/metadata.py
./services/all_services.txt:33193:/home/ms-jarvis/msjarvis-rebuild/services/alert_venv/lib/python3.12/site-packages/O365/message.py
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 
