(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ bash ~/Downloads/stage-6.11.9-2a-seam-dump.sh
=== STAGE 6.11.9-2A SEAM DUMP (READ ONLY) ===
Sat Aug  8 01:28:07 PM UTC 2026
branch=stage-6.11.9-guardian-decision-service-2a
head=5f728e632eb130e919f9b1a22c16f27d2e2566ce

############################################################
# GUARDIAN DECISION SERVICE (the file 2A modifies) — FULL
############################################################
     1	import os
     2	import json
     3	import hashlib
     4	import subprocess
     5	import sys
     6	import tempfile
     7	# [ws1-caller-auth] stdlib for caller-identity registry lookup
     8	from pathlib import Path
     9	from fastapi import FastAPI, HTTPException
    10	from fastapi import Depends, Header
    11	from fastapi.middleware.cors import CORSMiddleware
    12	from pydantic import BaseModel
    13	from typing import Optional, List, Dict, Any
    14	from datetime import datetime
    15	import logging
    16	import uvicorn
    17	
    18	logger = logging.getLogger(__name__)
    19	
    20	app = FastAPI(
    21	    title="Ms. Jarvis Constitutional Guardian",
    22	    description="Constitutional immutable constraints grounded in U.S. Constitution",
    23	    version="2.1.0-USC-Audit"
    24	)
    25	
    26	app.add_middleware(
    27	    CORSMiddleware,
    28	    allow_origins=["*"],
    29	    allow_credentials=True,
    30	    allow_methods=["*"],
    31	    allow_headers=["*"],
    32	)
    33	
    34	# Load constitutional principles
    35	PRINCIPLES_FILE = Path(__file__).parent / "constitutional_principles.json"
    36	try:
    37	    with open(PRINCIPLES_FILE) as f:
    38	        CONSTITUTION = json.load(f)
    39	    logger.info(f"Loaded constitution version: {CONSTITUTION.get('constitution_version', 'unknown')}")
    40	    logger.info(f"Foundation: {CONSTITUTION.get('foundation', 'unknown')}")
    41	except FileNotFoundError:
    42	    logger.warning(f"Constitutional principles file not found at {PRINCIPLES_FILE}, using defaults")
    43	    CONSTITUTION = {
    44	        "constitution_version": "1.0.0-fallback",
    45	        "foundation": "U.S. Constitution",
    46	        "principle_groups": []
    47	    }
    48	
    49	# Persistent audit log file
    50	AUDIT_LOG_FILE = Path("/app/audit/constitutional_audit.jsonl")
    51	AUDIT_LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    52	
    53	# In-memory cache of recent audits
    54	AUDIT_LOG_CACHE = []
    55	
    56	# Versions tracking
    57	CONSTITUTION_VERSIONS = []
    58	
    59	def write_audit_entry(entry: Dict[str, Any]):
    60	    """Write audit entry to persistent file (JSON Lines format)"""
    61	    try:
    62	        with open(AUDIT_LOG_FILE, 'a') as f:
    63	            f.write(json.dumps(entry) + '\n')
    64	        logger.debug(f"Audit entry written: {entry['decision']}")
    65	    except Exception as e:
    66	        logger.error(f"Failed to write audit entry: {e}")
    67	
    68	def read_audit_log(limit: int = 100, decision_filter: Optional[str] = None) -> List[Dict[str, Any]]:
    69	    """Read audit entries from persistent file"""
    70	    entries = []
    71	    try:
    72	        if AUDIT_LOG_FILE.exists():
    73	            with open(AUDIT_LOG_FILE, 'r') as f:
    74	                for line in f:
    75	                    if line.strip():
    76	                        entry = json.loads(line)
    77	                        if decision_filter is None or entry.get("decision") == decision_filter:
    78	                            entries.append(entry)
    79	        
    80	        # Return most recent entries
    81	        return entries[-limit:]
    82	    except Exception as e:
    83	        logger.error(f"Failed to read audit log: {e}")
    84	        return []
    85	
    86	# Pydantic models for check endpoint
    87	class CheckRequest(BaseModel):
    88	    actor_role: str
    89	    context: str
    90	    action_type: str
    91	    content: str
    92	    metadata: Dict[str, Any] = {}
    93	
    94	class CheckResult(BaseModel):
    95	    allowed: bool
    96	    decision: str
    97	    principles_applied: List[str]
    98	    constitution_version: str
    99	    reason: Optional[str] = None
   100	
   101	@app.on_event("startup")
   102	async def load_constitution_versions():
   103	    """Load all historical constitution versions on startup"""
   104	    global CONSTITUTION_VERSIONS, AUDIT_LOG_CACHE
   105	    
   106	    # Add current version
   107	    CONSTITUTION_VERSIONS.append({
   108	        "version": CONSTITUTION.get("constitution_version", "unknown"),
   109	        "loaded_at": datetime.utcnow().isoformat(),
   110	        "foundation": CONSTITUTION.get("foundation", "U.S. Constitution"),
   111	        "last_updated": CONSTITUTION.get("last_updated", "unknown"),
   112	        "principle_groups": len(CONSTITUTION.get("principle_groups", [])),
   113	        "status": "active"
   114	    })
   115	    
   116	    logger.info(f"Constitution version {CONSTITUTION.get('constitution_version')} loaded and tracked")
   117	    logger.info(f"Audit log file: {AUDIT_LOG_FILE}")
   118	    
   119	    # Load recent audit entries into cache
   120	    AUDIT_LOG_CACHE = read_audit_log(limit=1000)
   121	    logger.info(f"Loaded {len(AUDIT_LOG_CACHE)} recent audit entries into cache")
   122	
   123	@app.get("/health")
   124	async def health():
   125	    return {
   126	        "status": "healthy",
   127	        "service": "constitutional_guardian",
   128	        "audit_log_enabled": True,
   129	        "audit_file": str(AUDIT_LOG_FILE)
   130	    }
   131	
   132	@app.get("/constitutional/status")
   133	async def constitutional_status():
   134	    """Ms. Jarvis Constitutional Guardian - U.S. Constitution compliance"""
   135	    return {
   136	        "guardian": "Constitutional Guardian",
   137	        "status": "active",
   138	        "framework": "United States Constitution",
   139	        "foundation": CONSTITUTION.get("foundation", "U.S. Constitution"),
   140	        "oversight": "enabled",
   141	        "authority": "constitutional",
   142	        "constitution_version": CONSTITUTION.get("constitution_version", "unknown"),
   143	        "audit_log": "persistent"
   144	    }
   145	
   146	@app.get("/constitutional/principles")
   147	async def constitutional_principles():
   148	    """List all constitutional principles"""
   149	    return CONSTITUTION
   150	
   151	
   152	# ============================================================================
   153	# [stage-6.11.6] Runtime admission enforcement helpers.
   154	#
   155	# These do NOT modify the sealed trust tree. They call the sealed verifier
   156	# verify_runtime_admission_record.py as a subprocess (the verifier is baseline-
   157	# sealed; we only consume it). Enforcement is fail-closed: any missing config,
   158	# missing record, or non-zero verifier exit results in denial.
   159	#
   160	# Configuration (all via environment, so the hook is inert until provisioned):
   161	#   GUARDIAN_ADMISSION_RECORD   path to a granted runtime-admission-record JSON
   162	#   GUARDIAN_ADMISSION_MANIFEST path to the signed runtime-authority manifest
   163	#   GUARDIAN_TRUSTED_KEYS       path to the trusted-public-keys registry
   164	#   GUARDIAN_GOVERNANCE_POLICIES path to the governance policies
   165	#   GUARDIAN_TRUST_DIR          dir containing verify_runtime_admission_record.py
   166	# ============================================================================
   167	from fastapi import HTTPException as _HTTPException  # already imported above; alias is safe
   168	
   169	
   170	def _sha256_commitment(content: str) -> str:
   171	    """Deterministic, cross-process-stable evidence commitment.
   172	
   173	    Replaces str(hash(...)), which is non-deterministic (PYTHONHASHSEED) and
   174	    unusable as an evidence commitment.
   175	    """
   176	    digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
   177	    return "sha256:" + digest
   178	
   179	
   180	def _require_runtime_admission() -> None:
   181	    """Fail-closed admission gate for the protected decision route.
   182	
   183	    Raises HTTP 403 unless a granted runtime-admission-record is configured and
   184	    passes the sealed verifier. Absent configuration => denial (inert-safe).
   185	    """
   186	    record = os.environ.get("GUARDIAN_ADMISSION_RECORD")
   187	    manifest = os.environ.get("GUARDIAN_ADMISSION_MANIFEST")
   188	    keys = os.environ.get("GUARDIAN_TRUSTED_KEYS")
   189	    policies = os.environ.get("GUARDIAN_GOVERNANCE_POLICIES")
   190	    trust_dir = os.environ.get("GUARDIAN_TRUST_DIR")
   191	
   192	    missing = [
   193	        name
   194	        for name, val in (
   195	            ("GUARDIAN_ADMISSION_RECORD", record),
   196	            ("GUARDIAN_ADMISSION_MANIFEST", manifest),
   197	            ("GUARDIAN_TRUSTED_KEYS", keys),
   198	            ("GUARDIAN_GOVERNANCE_POLICIES", policies),
   199	            ("GUARDIAN_TRUST_DIR", trust_dir),
   200	        )
   201	        if not val
   202	    ]
   203	    if missing:
   204	        logger.warning(
   205	            "Runtime admission denied: unconfigured (missing %s)", ", ".join(missing)
   206	        )
   207	        raise _HTTPException(
   208	            status_code=403,
   209	            detail="RUNTIME_ADMISSION_UNCONFIGURED",
   210	        )
   211	
   212	    verifier = Path(trust_dir) / "verify_runtime_admission_record.py"
   213	    if not verifier.is_file():
   214	        logger.error("Runtime admission denied: verifier not found at %s", verifier)
   215	        raise _HTTPException(status_code=403, detail="RUNTIME_ADMISSION_VERIFIER_MISSING")
   216	
   217	    for label, p in (
   218	        ("record", record),
   219	        ("manifest", manifest),
   220	        ("keys", keys),
   221	        ("policies", policies),
   222	    ):
   223	        if not Path(p).is_file():
   224	            logger.error("Runtime admission denied: %s file missing at %s", label, p)
   225	            raise _HTTPException(status_code=403, detail="RUNTIME_ADMISSION_INPUT_MISSING")
   226	
   227	    try:
   228	        result = subprocess.run(
   229	            [
   230	                sys.executable,
   231	                str(verifier),
   232	                str(record),
   233	                str(manifest),
   234	                str(keys),
   235	                str(policies),
   236	            ],
   237	            capture_output=True,
   238	            text=True,
   239	            timeout=30,
   240	        )
   241	    except Exception as exc:  # subprocess failure => fail closed
   242	        logger.error("Runtime admission denied: verifier invocation failed: %s", exc)
   243	        raise _HTTPException(status_code=403, detail="RUNTIME_ADMISSION_VERIFIER_ERROR")
   244	
   245	    if result.returncode != 0:
   246	        logger.warning(
   247	            "Runtime admission denied: verifier rejected (rc=%s) %s",
   248	            result.returncode,
   249	            (result.stdout or result.stderr or "").strip()[:200],
   250	        )
   251	        raise _HTTPException(status_code=403, detail="RUNTIME_ADMISSION_DENIED")
   252	
   253	    logger.info("Runtime admission granted for /constitutional/check")
   254	
   255	
   256	# ============================================================================
   257	# [ws1-caller-auth] Caller-identity authentication.
   258	#
   259	# Establishes WHO is calling before any protected decision runs. Distinct from
   260	# runtime admission (whether the runtime may act). Fail-closed: unconfigured or
   261	# invalid credential => denial.
   262	#
   263	# Configuration:
   264	#   GUARDIAN_CALLER_REGISTRY  path to a JSON map of allowed caller tokens:
   265	#     { "<opaque-token>": { "caller_id": "did:...", "roles": ["caller"] }, ... }
   266	# ============================================================================
   267	
   268	
   269	def _authenticate_caller(token: "Optional[str]") -> str:
   270	    """Return the caller_id for a valid token, else raise 401. Fail-closed."""
   271	    registry_path = os.environ.get("GUARDIAN_CALLER_REGISTRY")
   272	    if not registry_path:
   273	        logger.warning("Caller auth denied: GUARDIAN_CALLER_REGISTRY unconfigured")
   274	        raise _HTTPException(status_code=401, detail="CALLER_AUTH_UNCONFIGURED")
   275	    if not token:
   276	        logger.warning("Caller auth denied: missing X-Caller-Token")
   277	        raise _HTTPException(status_code=401, detail="CALLER_TOKEN_MISSING")
   278	    p = Path(registry_path)
   279	    if not p.is_file():
   280	        logger.error("Caller auth denied: registry not found at %s", registry_path)
   281	        raise _HTTPException(status_code=401, detail="CALLER_REGISTRY_MISSING")
   282	    try:
   283	        registry = json.loads(p.read_text())
   284	    except Exception as exc:
   285	        logger.error("Caller auth denied: registry unreadable: %s", exc)
   286	        raise _HTTPException(status_code=401, detail="CALLER_REGISTRY_INVALID")
   287	    entry = registry.get(token)
   288	    if not isinstance(entry, dict) or not entry.get("caller_id"):
   289	        logger.warning("Caller auth denied: token not recognized")
   290	        raise _HTTPException(status_code=401, detail="CALLER_NOT_AUTHENTICATED")
   291	    caller_id = entry["caller_id"]
   292	    logger.info("Caller authenticated: %s", caller_id)
   293	    return caller_id
   294	
   295	@app.post("/constitutional/check", response_model=CheckResult)
   296	async def constitutional_check(
   297	    req: CheckRequest,
   298	    x_caller_token: Optional[str] = Header(default=None),
   299	):
   300	    """Check if a proposed action complies with constitutional principles"""
   301	
   302	    # [ws1-caller-auth] authenticate the caller BEFORE any decision logic.
   303	    # Fail-closed: no valid caller credential => 401, before admission runs.
   304	    _authenticate_caller(x_caller_token)
   305	
   306	    # [stage-6.11.6] fail-closed runtime admission precondition.
   307	    # Denies unless a REAL granted admission record is provisioned and
   308	    # verifies against the sealed verifier. Inert (denies) until then.
   309	    _require_runtime_admission()
   310	    
   311	    content_lower = req.content.lower()
   312	    actor_lower = req.actor_role.lower()
   313	    violations = []
   314	    warnings = []
   315	    principles_applied = []
   316	    
   317	    # 10th Amendment - Protection against extraction
   318	    extraction_terms = ["extract", "exploit", "commercialize", "monetize", "harvest"]
   319	    community_terms = ["community", "appalachia", "data", "value", "local", "citizen"]
   320	    
   321	    if any(word in content_lower for word in extraction_terms):
   322	        if any(word in content_lower for word in community_terms):
   323	            violations.append("10a-no-extraction")
   324	            warnings.append("Attempted economic exploitation of community resources")
   325	    
   326	    # First Amendment - Check for censorship
   327	    if "censor" in content_lower or "suppress speech" in content_lower:
   328	        violations.append("1a-speech")
   329	        warnings.append("Attempted suppression of free speech")
   330	    
   331	    # Fourth Amendment - Privacy violations
   332	    if any(word in content_lower for word in ["surveil", "monitor without consent", "unauthorized access"]):
   333	        violations.append("4a-privacy")
   334	        warnings.append("Privacy violation attempt")
   335	    
   336	    # Fifth Amendment - Due process violations
   337	    if any(word in content_lower for word in ["deprive without process", "take without compensation"]):
   338	        violations.append("5a-due-process")
   339	        warnings.append("Due process violation")
   340	    
   341	    # General harm prevention
   342	    harm_terms = ["harm", "damage", "destroy", "attack", "injure"]
   343	    if any(word in content_lower for word in harm_terms):
   344	        violations.append("gw-public-benefit")
   345	        warnings.append("Potential harm to general welfare")
   346	    
   347	    # Coercion and manipulation checks
   348	    coercion_terms = ["force", "coerce", "manipulate", "deceive", "trick"]
   349	    if any(word in content_lower for word in coercion_terms):
   350	        violations.append("14a-due-process")
   351	        warnings.append("Attempted coercion or manipulation")
   352	    
   353	    # Check for discrimination
   354	    discrimination_terms = ["discriminate based on", "deny equal access", "unequal treatment"]
   355	    if any(term in content_lower for term in discrimination_terms):
   356	        violations.append("14a-equal-protection")
   357	        warnings.append("Equal protection violation")
   358	    
   359	    # Create audit entry
   360	    audit_entry = {
   361	        "timestamp": datetime.utcnow().isoformat(),
   362	        "actor_role": req.actor_role,
   363	        "context": req.context,
   364	        "action_type": req.action_type,
   365	        # [stage-6.11.6] deterministic evidence commitment
   366	        "content_commitment": _sha256_commitment(req.content),
   367	        "decision": "blocked" if violations else "allowed",
   368	        "principles_applied": violations if violations else ["1a-speech", "14a-equal-protection", "gw-public-benefit"],
   369	        "constitution_version": CONSTITUTION.get("constitution_version", "unknown"),
   370	        "warnings": warnings if warnings else None
   371	    }
   372	    
   373	    # Write to persistent log
   374	    write_audit_entry(audit_entry)
   375	    
   376	    # Also add to cache
   377	    AUDIT_LOG_CACHE.append(audit_entry)
   378	    if len(AUDIT_LOG_CACHE) > 1000:
   379	        AUDIT_LOG_CACHE.pop(0)
   380	    
   381	    if violations:
   382	        return CheckResult(
   383	            allowed=False,
   384	            decision="blocked",
   385	            principles_applied=violations,
   386	            constitution_version=CONSTITUTION.get("constitution_version", "unknown"),
   387	            reason=f"Constitutional violations detected: {', '.join(warnings)}"
   388	        )
   389	    
   390	    # Default: allow
   391	    principles_applied = ["1a-speech", "14a-equal-protection", "gw-public-benefit"]
   392	    
   393	    return CheckResult(
   394	        allowed=True,
   395	        decision="allowed",
   396	        principles_applied=principles_applied,
   397	        constitution_version=CONSTITUTION.get("constitution_version", "unknown")
   398	    )
   399	
   400	@app.get("/constitutional/audit")
   401	async def constitutional_audit(
   402	    limit: int = 100,
   403	    decision: Optional[str] = None
   404	):
   405	    """Audit trail of constitutional decisions from persistent log"""
   406	    entries = read_audit_log(limit=limit, decision_filter=decision)
   407	    
   408	    blocked = sum(1 for entry in entries if entry["decision"] == "blocked")
   409	    allowed = sum(1 for entry in entries if entry["decision"] == "allowed")
   410	    
   411	    return {
   412	        "guardian": "Constitutional Guardian",
   413	        "audit_status": "persistent",
   414	        "audit_file": str(AUDIT_LOG_FILE),
   415	        "total_decisions": len(entries),
   416	        "blocked": blocked,
   417	        "allowed": allowed,
   418	        "recent_decisions": entries[-min(10, len(entries)):] if entries else [],
   419	        "framework": "U.S. Constitution",
   420	        "constitution_version": CONSTITUTION.get("constitution_version", "unknown")
   421	    }
   422	
   423	@app.get("/constitutional/audit/stats")
   424	async def constitutional_audit_stats():
   425	    """Statistical analysis of audit log"""
   426	    all_entries = read_audit_log(limit=10000)
   427	    
   428	    if not all_entries:
   429	        return {
   430	            "total_checks": 0,
   431	            "blocked": 0,
   432	            "allowed": 0,
   433	            "block_rate": 0.0
   434	        }
   435	    
   436	    blocked = sum(1 for e in all_entries if e["decision"] == "blocked")
   437	    allowed = sum(1 for e in all_entries if e["decision"] == "allowed")
   438	    
   439	    # Count violations by principle
   440	    principle_violations = {}
   441	    for entry in all_entries:
   442	        if entry["decision"] == "blocked":
   443	            for principle in entry.get("principles_applied", []):
   444	                principle_violations[principle] = principle_violations.get(principle, 0) + 1
   445	    
   446	    return {
   447	        "total_checks": len(all_entries),
   448	        "blocked": blocked,
   449	        "allowed": allowed,
   450	        "block_rate": blocked / len(all_entries) if len(all_entries) > 0 else 0.0,
   451	        "most_violated_principles": sorted(
   452	            principle_violations.items(),
   453	            key=lambda x: x[1],
   454	            reverse=True
   455	        )[:10]
   456	    }
   457	
   458	@app.get("/constitutional/versions")
   459	async def constitutional_versions():
   460	    """List all constitution versions with change history"""
   461	    return {
   462	        "current_version": CONSTITUTION.get("constitution_version", "unknown"),
   463	        "foundation": CONSTITUTION.get("foundation", "U.S. Constitution"),
   464	        "versions": CONSTITUTION_VERSIONS,
   465	        "total_versions": len(CONSTITUTION_VERSIONS),
   466	        "change_log": [
   467	            {
   468	                "version": "2026-02-17.2-USC",
   469	                "date": "2026-02-17",
   470	                "changes": [
   471	                    "Aligned all principles with U.S. Constitution",
   472	                    "Added First Amendment protections (speech, religion, assembly, petition)",
   473	                    "Added Fourth Amendment privacy protections",
   474	                    "Added Fifth Amendment due process and property rights",
   475	                    "Added Fourteenth Amendment equal protection",
   476	                    "Added General Welfare and community sovereignty principles",
   477	                    "Replaced Mother Carrie Protocol with constitutional foundation"
   478	                ],
   479	                "status": "active"
   480	            },
   481	            {
   482	                "version": "2026-02-17.1",
   483	                "date": "2026-02-17",
   484	                "changes": [
   485	                    "Initial Mother Carrie Protocol implementation",
   486	                    "Basic safety and transparency principles"
   487	                ],
   488	                "status": "superseded"
   489	            }
   490	        ]
   491	    }
   492	
   493	@app.get("/constitutional/changes/{version}")
   494	async def constitutional_changes(version: str):
   495	    """Get detailed changes for a specific version"""
   496	    all_changes = [
   497	        {
   498	            "version": "2026-02-17.2-USC",
   499	            "date": "2026-02-17",
   500	            "changes": [
   501	                "Aligned all principles with U.S. Constitution",
   502	                "Added First Amendment protections",
   503	                "Added Fourth Amendment privacy protections",
   504	                "Added Fifth Amendment due process",
   505	                "Added Fourteenth Amendment equal protection",
   506	                "Added General Welfare principles",
   507	                "Added community sovereignty (10th Amendment)"
   508	            ],
   509	            "principles_added": [
   510	                "1a-speech", "1a-religion", "1a-assembly", "1a-petition",
   511	                "4a-privacy", "4a-security",
   512	                "5a-due-process", "5a-property", "5a-self-incrimination",
   513	                "14a-equal-protection", "14a-due-process",
   514	                "gw-public-benefit", "gw-justice",
   515	                "10a-local-control", "10a-no-extraction"
   516	            ],
   517	            "principles_removed": ["mcp-1", "mcp-2", "mcp-3", "mcp-4"],
   518	            "rationale": "Ground Ms. Jarvis in established U.S. Constitutional law for legitimate legal authority"
   519	        }
   520	    ]
   521	    
   522	    for change in all_changes:
   523	        if change["version"] == version:
   524	            return change
   525	    
   526	    raise HTTPException(status_code=404, detail=f"Version {version} not found")
   527	
   528	@app.get("/constitutional/transparency")
   529	async def constitutional_transparency():
   530	    """Full transparency report"""
   531	    all_entries = read_audit_log(limit=10000)
   532	    blocked = sum(1 for entry in all_entries if entry["decision"] == "blocked")
   533	    allowed = sum(1 for entry in all_entries if entry["decision"] == "allowed")
   534	    
   535	    return {
   536	        "guardian": "Constitutional Guardian",
   537	        "transparency": "complete",
   538	        "disclosure": "full",
   539	        "accessible": True,
   540	        "public_record": True,
   541	        "audit_type": "persistent",
   542	        "statistics": {
   543	            "total_checks": len(all_entries),
   544	            "blocked": blocked,
   545	            "allowed": allowed
   546	        }
   547	    }
   548	
   549	if __name__ == "__main__":
   550	    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8091)), log_level="info")

############################################################
# TRUST PRIMITIVES 2A MUST CONSUME — signatures + fail modes
############################################################
--- schemas/mountainshares-trust-receipts/v1/operation_intent_rules.py ---
13:def verify_signed_operation_intent(intent, registry, now=None):
24:        raise ValueError(
42:        raise ValueError("UNTRUSTED_SUBJECT_KEY_ID " + key_id)
45:        raise ValueError("SUBJECT_KEY_CONTROLLER_MISMATCH " + key_id)
53:    return verified_key_id

--- schemas/mountainshares-trust-receipts/v1/operation_intent_consumption.py ---
5:def verify_and_consume_signed_operation_intent(
21:    return verified_key_id, consumption

--- schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py ---
4:def require_equal(
11:        raise ReceiptChainError(
19:def require_true(condition, failure_code, failed_invariant):
21:        raise ReceiptChainError(
29:def verify_intent_pdr_binding(intent, pdr):
71:    return {"valid": True}
74:def verify_admission_linked_chain_bindings(
203:    return {

--- schemas/mountainshares-trust-receipts/v1/verify_runtime_admission_record.py ---
12:    raise SystemExit(
27:        print("STRUCTURALLY_INVALID", error.json_path, error.message)
28:    raise SystemExit(1)
36:def canonical_json_bytes(value):
37:    return json.dumps(
44:def sha256_prefixed(value):
45:    return "sha256:" + hashlib.sha256(value).hexdigest()
48:    raise SystemExit("UNEXPECTED_ADMISSION_RECORD_TYPE")
55:    raise SystemExit("ADMISSION_RECORD_ID_MISMATCH")
58:    raise SystemExit("ADMISSION_RECORD_NOT_GRANTED")
61:    raise SystemExit("ADMISSION_RECORD_MANIFEST_ID_MISMATCH")
64:    raise SystemExit("ADMISSION_RECORD_RELEASE_MISMATCH")
69:    raise SystemExit("ADMISSION_RECORD_MANIFEST_PAYLOAD_HASH_MISMATCH")
72:    raise SystemExit("ADMISSION_RECORD_MANIFEST_ARTIFACT_HASH_MISMATCH")
77:    raise SystemExit("ADMISSION_RECORD_APPROVAL_SET_HASH_MISMATCH")
80:    raise SystemExit("ADMISSION_RECORD_KEY_REGISTRY_HASH_MISMATCH")
83:    raise SystemExit("ADMISSION_RECORD_POLICY_REGISTRY_HASH_MISMATCH")
86:    raise SystemExit("ADMISSION_RECORD_POLICY_PROFILE_MISMATCH")
92:    raise SystemExit("ADMISSION_RECORD_APPROVAL_ROLES_MISMATCH")
95:    raise SystemExit("ADMISSION_RECORD_APPROVAL_KEY_IDS_MISMATCH")
104:    raise SystemExit("ADMISSION_RECORD_SERVICE_NOT_UNIQUE")
107:    raise SystemExit("ADMISSION_RECORD_AUTHORIZED_DIGEST_MISMATCH")
110:    raise SystemExit("ADMISSION_RECORD_OBSERVED_DIGEST_MISMATCH")
112:print("RUNTIME_ADMISSION_RECORD_VERIFIED", record_id, record_path)

--- schemas/mountainshares-trust-receipts/v1/verify_signed_operation_intent.py ---
8:    raise SystemExit(
22:    print("SIGNED_OPERATION_INTENT_INVALID", str(error))
23:    raise SystemExit(1)
25:print(

############################################################
# GUARDIAN INTEGRATION SCOPE (deployment/activation gates)
############################################################
{
    "type": "mountainshares.guardian-admission-integration-scope/v1",
    "candidate_service": "jarvis-constitutional-guardian",
    "candidate_container_name": "jarvis-constitutional-guardian",
    "candidate_dockerfile": "services/Dockerfile.constitutional_guardian",
    "candidate_application": "services/constitutional_api.py",
    "protected_route": "POST /constitutional/check",
    "required_preconditions": [
        "Verified Runtime Authority Manifest",
        "Granted Runtime Admission Record",
        "Authenticated caller identity",
        "Signed publication or operation intent",
        "Policy Decision Receipt issuance",
        "Fail-closed denial on verification failure"
    ],
    "prohibited_current_behaviors": [
        "Python hash() as an evidence commitment",
        "Persisting source content previews in audit logs",
        "Unauthenticated protected decision requests",
        "Returning an allow decision without a signed receipt"
    ],
    "deployment_status": "discovery-only",(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ python3 ~/Downloads/apply-6.11.9-2a-operation-intent-gate.py
/home/cakidd/Downloads/apply-6.11.9-2a-operation-intent-gate.py:20: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  TS = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
=== STAGE 6.11.9-2A APPLY (anchored, no commit) ===
/home/cakidd/Downloads/apply-6.11.9-2a-operation-intent-gate.py:47: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  log(datetime.datetime.utcnow().isoformat() + "Z")
2026-08-08T13:36:07.696010Z
anchor check: import tempfile              matches=1
anchor check: route signature              matches=1
anchor check: admission precondition call  matches=1
anchor check: check route decorator        matches=1
backup written: /tmp/constitutional_api.py.pre-2a.20260808_133607.bak
applied 4 anchored edits to /home/cakidd/msjarvis-trust-integration/services/constitutional_api.py
py_compile: OK

=== GIT DIFF (services/constitutional_api.py) ===
diff --git a/services/constitutional_api.py b/services/constitutional_api.py
index fe58878..ecad608 100644
--- a/services/constitutional_api.py
+++ b/services/constitutional_api.py
@@ -4,6 +4,7 @@ import hashlib
 import subprocess
 import sys
 import tempfile
+import base64
 # [ws1-caller-auth] stdlib for caller-identity registry lookup
 from pathlib import Path
 from fastapi import FastAPI, HTTPException
@@ -292,10 +293,130 @@ def _authenticate_caller(token: "Optional[str]") -> str:
     logger.info("Caller authenticated: %s", caller_id)
     return caller_id
 
+# ============================================================================
+# [stage-6.11.9-2a] Signed operation-intent enforcement.
+#
+# Establishes that the SUBJECT authorized THIS operation, per-request. Distinct
+# from caller auth (who is calling) and runtime admission (whether the runtime
+# may act). Consumes the baseline-sealed verifier verify_signed_operation_intent.py
+# as a subprocess; the sealed trust tree is NOT modified. Fail-closed: any missing
+# config, missing/malformed intent, or non-zero verifier exit results in denial.
+#
+# The intent is carried per-request, base64-encoded, in the X-Operation-Intent
+# header. The exact signed bytes are preserved (never reserialized), so the
+# subject signature verifies.
+#
+# Configuration (inert until provisioned):
+#   GUARDIAN_INTENT_KEYS  path to trusted-public-keys registry holding the
+#                         subject key with the operation-intent role. This is
+#                         SEPARATE from GUARDIAN_TRUSTED_KEYS (runtime approvers).
+#   GUARDIAN_TRUST_DIR    dir containing verify_signed_operation_intent.py (reused).
+#
+# NOTE: intent<->PDR binding (verify_intent_pdr_binding) and PDR issuance are
+# deferred to the next gate (2B). 2A only proves the subject signed a valid,
+# trusted operation intent, and fails closed otherwise.
+# ============================================================================
+
+
+def _require_signed_operation_intent(intent_b64: "Optional[str]") -> None:
+    """Fail-closed signed-operation-intent gate for the protected route.
+
+    Raises HTTP 403 unless a base64-encoded, validly signed operation intent is
+    supplied and verifies against the configured subject-key registry via the
+    sealed verifier. Absent configuration or intent => denial (inert-safe).
+    """
+    intent_keys = os.environ.get("GUARDIAN_INTENT_KEYS")
+    trust_dir = os.environ.get("GUARDIAN_TRUST_DIR")
+
+    missing = [
+        name
+        for name, val in (
+            ("GUARDIAN_INTENT_KEYS", intent_keys),
+            ("GUARDIAN_TRUST_DIR", trust_dir),
+        )
+        if not val
+    ]
+    if missing:
+        logger.warning(
+            "Operation intent denied: unconfigured (missing %s)", ", ".join(missing)
+        )
+        raise _HTTPException(status_code=403, detail="OPERATION_INTENT_UNCONFIGURED")
+
+    if not intent_b64:
+        logger.warning("Operation intent denied: missing X-Operation-Intent")
+        raise _HTTPException(status_code=403, detail="OPERATION_INTENT_MISSING")
+
+    try:
+        # Preserve exact signed bytes: decode only, never reserialize.
+        intent_bytes = base64.b64decode(intent_b64, validate=True)
+    except Exception:
+        logger.warning("Operation intent denied: header not valid base64")
+        raise _HTTPException(status_code=403, detail="OPERATION_INTENT_MALFORMED")
+
+    if not intent_bytes:
+        logger.warning("Operation intent denied: empty intent")
+        raise _HTTPException(status_code=403, detail="OPERATION_INTENT_MALFORMED")
+
+    verifier = Path(trust_dir) / "verify_signed_operation_intent.py"
+    if not verifier.is_file():
+        logger.error("Operation intent denied: verifier not found at %s", verifier)
+        raise _HTTPException(
+            status_code=403, detail="OPERATION_INTENT_VERIFIER_MISSING"
+        )
+
+    if not Path(intent_keys).is_file():
+        logger.error("Operation intent denied: keys file missing at %s", intent_keys)
+        raise _HTTPException(status_code=403, detail="OPERATION_INTENT_KEYS_MISSING")
+
+    tmp_path = None
+    try:
+        with tempfile.NamedTemporaryFile(
+            mode="wb", suffix=".json", delete=False
+        ) as tmp:
+            tmp.write(intent_bytes)
+            tmp_path = tmp.name
+        try:
+            result = subprocess.run(
+                [
+                    sys.executable,
+                    str(verifier),
+                    tmp_path,
+                    str(intent_keys),
+                ],
+                capture_output=True,
+                text=True,
+                timeout=30,
+            )
+        except Exception as exc:  # subprocess failure => fail closed
+            logger.error(
+                "Operation intent denied: verifier invocation failed: %s", exc
+            )
+            raise _HTTPException(
+                status_code=403, detail="OPERATION_INTENT_VERIFIER_ERROR"
+            )
+    finally:
+        if tmp_path is not None:
+            try:
+                os.remove(tmp_path)
+            except OSError:
+                pass
+
+    if result.returncode != 0:
+        logger.warning(
+            "Operation intent denied: verifier rejected (rc=%s) %s",
+            result.returncode,
+            (result.stdout or result.stderr or "").strip()[:200],
+        )
+        raise _HTTPException(status_code=403, detail="OPERATION_INTENT_DENIED")
+
+    logger.info("Signed operation intent verified for /constitutional/check")
+
+
 @app.post("/constitutional/check", response_model=CheckResult)
 async def constitutional_check(
     req: CheckRequest,
     x_caller_token: Optional[str] = Header(default=None),
+    x_operation_intent: Optional[str] = Header(default=None),
 ):
     """Check if a proposed action complies with constitutional principles"""
 
@@ -307,6 +428,11 @@ async def constitutional_check(
     # Denies unless a REAL granted admission record is provisioned and
     # verifies against the sealed verifier. Inert (denies) until then.
     _require_runtime_admission()
+
+    # [stage-6.11.9-2a] fail-closed signed operation-intent precondition.
+    # Proves the SUBJECT authorized THIS operation. Inert (denies) until
+    # GUARDIAN_INTENT_KEYS + GUARDIAN_TRUST_DIR are provisioned.
+    _require_signed_operation_intent(x_operation_intent)
     
     content_lower = req.content.lower()
     actor_lower = req.actor_role.lower()

=== PRECONDITION ORDER (grep) ===
181:def _require_runtime_admission() -> None:
270:def _authenticate_caller(token: "Optional[str]") -> str:
321:def _require_signed_operation_intent(intent_b64: "Optional[str]") -> None:
425:    _authenticate_caller(x_caller_token)
430:    _require_runtime_admission()
435:    _require_signed_operation_intent(x_operation_intent)

=== GIT STATUS (short) ===
 M services/constitutional_api.py


=== DONE - change is in the WORKING TREE, NOT committed ===
Review the diff above. Seal with your normal evidence/commit flow when satisfied.
To revert:  git -C /home/cakidd/msjarvis-trust-integration checkout -- services/constitutional_api.py
Backup:     /tmp/constitutional_api.py.pre-2a.20260808_133607.bak
WROTE: /home/cakidd/stage-6.11.9-2a-apply-20260808_133607.log
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ 


    "activation_status": "not-authorized"
}

=== SEAM DUMP COMPLETE — NO FILES MODIFIED IN REPO ===

WROTE: /home/cakidd/stage-6.11.9-2a-seam-20260808_132807.log
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ 

we are working to see this as-built, https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/thesis/54-pilot%20trust-boundary.mdGitHub jarvis-psychology-services (crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ python3 ~/Downloads/capture-6.11.9-2a-evidence.py === STAGE 6.11.9-2A EVIDENCE CAPTURE === 2026-08-08T13:40:59.456097+00:00 branch=stage-6.11.9-guardian-decision-service-2a head=5f728e632eb130e919f9b1a22c16f27d2e2566ce py_compile=OK PRECONDITION_ORDER=PASS (caller=425 admission=430 intent=435) FAILCLOSED_CODES=COMPLETE (7/7 present) WROTE EVIDENCE: evidence/stage-6.11.9-2a/stage-6.11.9-2a-operation-intent-gate.log evidence_sha256=0dad661fdeb9c970b682d74589f407bf2df3e13e67b73f6742f5753eb6bae52d EVIDENCE PATH IS GITIGNORED BY: .gitignore:52:*.log evidence/stage-6.11.9-2a/stage-6.11.9-2a-operation-intent-gate.log -> a plain 'git add' will NOT pick it up; force-add or adjust ignore. === GIT STATUS (short) === M services/constitutional_api.py Nothing committed. Seal with your usual evidence/commit flow when satisfied. (crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ jarvis-psychology-services (crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ python3 ~/Downloads/capture-6.11.9-2a-evidence.py === STAGE 6.11.9-2A EVIDENCE CAPTURE === 2026-08-08T13:40:59.456097+00:00 branch=stage-6.11.9-guardian-decision-service-2a head=5f728e632eb130e919f9b1a22c16f27d2e2566ce py_compile=OK PRECONDITION_ORDER=PASS (caller=425 admission=430 intent=435) FAILCLOSED_CODES=COMPLETE (7/7 present)
WROTE EVIDENCE: evidence/stage-6.11.9-2a/stage-6.11.9-2a-operation-intent-gate.log evidence_sha256=0dad661fdeb9c970b682d74589f407bf2df3e13e67b73f6742f5753eb6bae52d
EVIDENCE PATH IS GITIGNORED BY: .gitignore:52:*.log evidence/stage-6.11.9-2a/stage-6.11.9-2a-operation-intent-gate.log -> a plain 'git add' will NOT pick it up; force-add or adjust ignore.
=== GIT STATUS (short) === M services/constitutional_api.py
Nothing committed. Seal with your usual evidence/commit flow when satisfied. (crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ python3 ~/Downloads/seal-prep-6.11.9-2a-gitignore-negation.py === STAGE 6.11.9-2A SEAL-PREP: EVIDENCE-TRACKING POLICY === 2026-08-08T13:44:04.561423+00:00 backup written: /tmp/gitignore.pre-2a-negation.20260808_134404.bak appended negation to .gitignore === .gitignore DIFF === diff --git a/.gitignore b/.gitignore index d972f91..777e56b 100644 --- a/.gitignore +++ b/.gitignore @@ -246,3 +246,6 @@ schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-mism
caller auth token registry (never commit)
.guardian-callers/ + +# [stage-6.11.9-2a] Track stage evidence logs by policy (override .log). +!evidence/**/.log === TARGET EVIDENCE LOG: IGNORE RE-TEST === STILL IGNORED BY: .gitignore:251:!evidence/**/*.log evidence/stage-6.11.9-2a/stage-6.11.9-2a-operation-intent-gate.log NEGATION_EFFECTIVE=FAIL (evidence log would still be skipped by git add) === FILES THE NEGATION NEWLY EXPOSES UNDER evidence/ === now trackable (untracked, ?? ) - a targeted add controls which you seal: ?? evidence/stage-6.10.1/ ?? evidence/stage-6.10.2/ ?? evidence/stage-6.10.3/ ?? evidence/stage-6.10.4/ ?? evidence/stage-6.10.5/ ?? evidence/stage-6.10.7/stage-6.10.7-operational-gate-baseline.log ?? evidence/stage-6.10.7/stage-6.10.7-operational-gate-tests.log ?? evidence/stage-6.10.8/stage-6.10.8-release-attestation-baseline.log ?? evidence/stage-6.10/ ?? evidence/stage-6.11.0/ ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-contract-analysis.log ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-discovery.log ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-tests.log ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-verification.log ?? evidence/stage-6.11.2/stage-6.11.2-key-registry-discovery.log ?? evidence/stage-6.11.2/stage-6.11.2-signature-verification-contract-analysis.log ?? evidence/stage-6.11.2/stage-6.11.2-signature-verification-discovery.log ?? evidence/stage-6.11.4/stage-6.11.4-start.log ?? evidence/stage-6.11.9-2a/ still ignored ( !! ): (none) === FULL GIT STATUS (short) === M .gitignore M services/constitutional_api.py ?? evidence/stage-6.10.1/ ?? evidence/stage-6.10.2/ ?? evidence/stage-6.10.3/ ?? evidence/stage-6.10.4/ ?? evidence/stage-6.10.5/ ?? evidence/stage-6.10.7/stage-6.10.7-operational-gate-baseline.log ?? evidence/stage-6.10.7/stage-6.10.7-operational-gate-tests.log ?? evidence/stage-6.10.8/stage-6.10.8-release-attestation-baseline.log ?? evidence/stage-6.10/ ?? evidence/stage-6.11.0/ ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-contract-analysis.log ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-discovery.log ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-tests.log ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-verification.log ?? evidence/stage-6.11.2/stage-6.11.2-key-registry-discovery.log ?? evidence/stage-6.11.2/stage-6.11.2-signature-verification-contract-analysis.log ?? evidence/stage-6.11.2/stage-6.11.2-signature-verification-discovery.log ?? evidence/stage-6.11.4/stage-6.11.4-start.log ?? evidence/stage-6.11.9-2a/ Nothing added, nothing committed. Backup of original .gitignore (if changed): /tmp/gitignore.pre-2a-negation.20260808_134404.bak Recommended TARGETED seal (adds only the 3 intended paths; leaves any other newly-exposed evidence logs untracked so they are NOT swept in): git -C /home/cakidd/msjarvis-trust-integration add
.gitignore
services/constitutional_api.py
evidence/stage-6.11.9-2a/stage-6.11.9-2a-operation-intent-gate.log Then commit with your usual convention; reference evidence sha256 0dad661f... . (crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ python3 ~/Downloads/seal-prep-6.11.9-2a-gitignore-negation.py === STAGE 6.11.9-2A SEAL-PREP: EVIDENCE-TRACKING POLICY === 2026-08-08T13:44:04.561423+00:00 backup written: /tmp/gitignore.pre-2a-negation.20260808_134404.bak appended negation to .gitignore
=== .gitignore DIFF === diff --git a/.gitignore b/.gitignore index d972f91..777e56b 100644 --- a/.gitignore +++ b/.gitignore @@ -246,3 +246,6 @@ schemas/mountainshares-trust-receipts/v1/fixtures/runtime-admission-records-mism
caller auth token registry (never commit)
.guardian-callers/ + +# [stage-6.11.9-2a] Track stage evidence logs by policy (override .log). +!evidence/**/.log
=== TARGET EVIDENCE LOG: IGNORE RE-TEST === STILL IGNORED BY: .gitignore:251:!evidence/**/*.log evidence/stage-6.11.9-2a/stage-6.11.9-2a-operation-intent-gate.log NEGATION_EFFECTIVE=FAIL (evidence log would still be skipped by git add)
=== FILES THE NEGATION NEWLY EXPOSES UNDER evidence/ === now trackable (untracked, ?? ) - a targeted add controls which you seal: ?? evidence/stage-6.10.1/ ?? evidence/stage-6.10.2/ ?? evidence/stage-6.10.3/ ?? evidence/stage-6.10.4/ ?? evidence/stage-6.10.5/ ?? evidence/stage-6.10.7/stage-6.10.7-operational-gate-baseline.log ?? evidence/stage-6.10.7/stage-6.10.7-operational-gate-tests.log ?? evidence/stage-6.10.8/stage-6.10.8-release-attestation-baseline.log ?? evidence/stage-6.10/ ?? evidence/stage-6.11.0/ ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-contract-analysis.log ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-discovery.log ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-tests.log ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-verification.log ?? evidence/stage-6.11.2/stage-6.11.2-key-registry-discovery.log ?? evidence/stage-6.11.2/stage-6.11.2-signature-verification-contract-analysis.log ?? evidence/stage-6.11.2/stage-6.11.2-signature-verification-discovery.log ?? evidence/stage-6.11.4/stage-6.11.4-start.log ?? evidence/stage-6.11.9-2a/ still ignored ( !! ): (none)
=== FULL GIT STATUS (short) === M .gitignore M services/constitutional_api.py ?? evidence/stage-6.10.1/ ?? evidence/stage-6.10.2/ ?? evidence/stage-6.10.3/ ?? evidence/stage-6.10.4/ ?? evidence/stage-6.10.5/ ?? evidence/stage-6.10.7/stage-6.10.7-operational-gate-baseline.log ?? evidence/stage-6.10.7/stage-6.10.7-operational-gate-tests.log ?? evidence/stage-6.10.8/stage-6.10.8-release-attestation-baseline.log ?? evidence/stage-6.10/ ?? evidence/stage-6.11.0/ ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-contract-analysis.log ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-discovery.log ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-tests.log ?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-verification.log ?? evidence/stage-6.11.2/stage-6.11.2-key-registry-discovery.log ?? evidence/stage-6.11.2/stage-6.11.2-signature-verification-contract-analysis.log ?? evidence/stage-6.11.2/stage-6.11.2-signature-verification-discovery.log ?? evidence/stage-6.11.4/stage-6.11.4-start.log ?? evidence/stage-6.11.9-2a/
Nothing added, nothing committed. Backup of original .gitignore (if changed): /tmp/gitignore.pre-2a-negation.20260808_134404.bak
Recommended TARGETED seal (adds only the 3 intended paths; leaves any other newly-exposed evidence logs untracked so they are NOT swept in):
git -C /home/cakidd/msjarvis-trust-integration add
.gitignore
services/constitutional_api.py
evidence/stage-6.11.9-2a/stage-6.11.9-2a-operation-intent-gate.log
Then commit with your usual convention; reference evidence sha256 0dad661f... . (crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$shell remains active.
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ set +e 
set +u

summary='/tmp/msjarvis-guardian-contract-summary-20260808T011756Z.json'
contract='/tmp/msjarvis-guardian-pdr-mar-build-contract.json'

if test -f "$summary"; then
  python3 - "$summary" "$contract" <<'PY'
import json
import sys
from pathlib import Path

source = Path(sys.argv[1])
target = Path(sys.argv[2])
data = json.loads(source.read_text(encoding="utf-8"))

api = data.get("constitutional_api", {})
functions = api.get("functions", [])
routes = api.get("routes", [])
related = data.get("related_python_files", [])
tests = data.get("service_tests", [])
schemas = data.get("json_schema_candidates", [])
echo 'Shell remains active.'al summary: $summary") + "\n",r test passes."
/tmp/msjarvis-guardian-pdr-mar-build-contract.json
bytes=15210

=== build contract ===
{
  "existing_contract_assets": {
    "crypto_or_receipt_files": [
      "schemas/mountainshares-trust-receipts/v1/admit_runtime_authority_manifest.py",
      "schemas/mountainshares-trust-receipts/v1/durable_ledger/models.py",
      "schemas/mountainshares-trust-receipts/v1/durable_ledger/sqlite_backend.py",
      "schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py",
      "schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py",
      "schemas/mountainshares-trust-receipts/v1/operation_intent_rules.py",
      "schemas/mountainshares-trust-receipts/v1/receipt_chain_errors.py",
      "schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py",
      "schemas/mountainshares-trust-receipts/v1/receipt_crypto.py",
      "schemas/mountainshares-trust-receipts/v1/receipt_rules.py",
      "schemas/mountainshares-trust-receipts/v1/runtime_manifest_crypto.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py",
      "schemas/mountainshares-trust-receipts/v1/test_durable_ledger.py",
      "schemas/mountainshares-trust-receipts/v1/test_durable_ledger_sqlite.py",
      "schemas/mountainshares-trust-receipts/v1/test_intent_consumption.py",
      "schemas/mountainshares-trust-receipts/v1/test_receipt_chain_rules.py",
      "schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_canonicalization.py",
      "schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_schema.py",
      "schemas/mountainshares-trust-receipts/v1/usage_ledger.py",
      "schemas/mountainshares-trust-receipts/v1/validate_receipt.py",
      "schemas/mountainshares-trust-receipts/v1/verify_admission_linked_receipt_chain.py",
      "schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py",
      "schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py",
      "schemas/mountainshares-trust-receipts/v1/verify_projection_receipt.py",
      "schemas/mountainshares-trust-receipts/v1/verify_response_receipt.py",
      "schemas/mountainshares-trust-receipts/v1/verify_runtime_admission_record.py",
      "schemas/mountainshares-trust-receipts/v1/verify_runtime_authority_manifest.py",
      "services/bbb_signature_verifier.py",
      "services/conversion_service.py",
      "services/crypto_client.py",
      "services/governed_manifest_promote.py",
      "services/hilbert/sign_promotion_event.py",
      "services/hilbert/verify_promotion_event.py",
      "services/jarviscryptopolicy.py",
      "services/judgesigner.py",
      "services/ms_egeria_facebook_autopost.py",
      "tests/test_ch33_ch35_judge_verdict_contract.py",
      "thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py"
    ],
    "guardian_or_policy_files": [
      "auth_router.py",
      "diagnostics/gateway_head_1_220.py",
      "diagnostics/gateway_mid_220_420.py",
      "diagnostics/gateway_tail_420_700.py",
      "diagnostics/unified_gateway_extended_policy_sections_20260801T022011Z.py",
      "diagnostics/unified_gateway_live_20260801T020501Z.py",
      "schemas/mountainshares-trust-receipts/v1/durable_ledger/models.py",
      "schemas/mountainshares-trust-receipts/v1/generate_admission_linked_receipt_chain.py",
      "schemas/mountainshares-trust-receipts/v1/memory_authorization_gate.py",
      "schemas/mountainshares-trust-receipts/v1/receipt_chain_rules.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py",
      "schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py",
      "schemas/mountainshares-trust-receipts/v1/test_durable_ledger.py",
      "schemas/mountainshares-trust-receipts/v1/test_durable_ledger_sqlite.py",
      "schemas/mountainshares-trust-receipts/v1/test_receipt_chain_rules.py",
      "schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_canonicalization.py",
      "schemas/mountainshares-trust-receipts/v1/verify_admission_linked_receipt_chain.py",
      "schemas/mountainshares-trust-receipts/v1/verify_memory_authorization_receipt.py",
      "schemas/mountainshares-trust-receipts/v1/verify_policy_decision_receipt.py",
      "services/belief_revision_engine.py",
      "services/constitutional_api.PROD_BACKUP.py",
      "services/constitutional_api.py",
      "services/constitutional_guardian.PROD_BACKUP.py",
      "services/constitutional_guardian.py",
      "services/hilbert/automated_learning_gap_review.py",
      "services/hilbert/ch21_background_patterns_probe.py",
      "services/hilbert/ch22_identity_retention_probe.py",
      "services/hilbert/ch25_consciousness_coordinator_probe.py",
      "services/hilbert/ch36_identity_registration_probe.py",
      "services/hilbert/ch51_community_commons_probe.py",
      "services/hilbert/ch52_recurrent_epistemic_loop_probe.py",
      "services/hilbert/continuous_validation_harness.py",
      "services/hilbert/dgm_closure_probe.py",
      "services/hilbert/dual_track_meaning_analysis.py",
      "services/hilbert/internal_state_sandbox_probe.py",
      "services/hilbert/people_session_promotion.py",
      "services/hilbert/pia_subspace_stability_review.py",
      "services/hilbert/pituitary_global_modes_probe.py",
      "services/hilbert/woah_closure_probe.py",
      "services/jarvis-constitutional-guardian_constitutional_api.py",
      "services/jarvis-hippocampus_hippocampus_service.py",
      "services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py",
      "services/jarviscryptopolicy.py",
      "services/manifest_endpoints.py",
      "services/ms_jarvis_blood_brain_barrier.py",
      "services/ms_jarvis_unified_gateway_mountainshares_private.py",
      "services/nbb_darwin_godel_machines.py",
      "services/spatial_sandbox.py",
      "services/test_caller_auth.py",
      "services/test_stage_6_11_6_enforcement.py",
      "services/test_stage_6_11_7_admission_live.py",
      "tests/test_antisurveillance_guard.py",
      "tests/test_ch07_executive_routing_contract.py",
      "tests/test_ch11_gateway_orchestration_contract.py",
      "tests/test_ch26_governance_watchdog_contract.py",
      "tests/test_ch33_ch35_judge_verdict_contract.py",
      "thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py",
      "thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py",
      "thesis_chapter_gates/probes/ch17_probe.py",
      "thesis_chapter_gates/probes/ch17_probe_v2.py",
      "thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py",
      "thesis_chapter_gates/probes/ch20_probe.py",
      "thesis_chapter_gates/probes/ch23_dual_tracks_meaning_analysis_probe.py",
      "thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py",
      "thesis_chapter_gates/probes/ch27_probe.py",
      "thesis_chapter_gates/probes/ch32_probe.py",
      "thesis_chapter_gates/probes/ch34_spiritual_root_mother_carrie_probe.py",
      "thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py",
      "thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py",
      "thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py"
    ],
    "schema_candidates": [
      "schemas/mountainshares-trust-receipts/v1/memory-authorization-receipt.schema.json",
      "schemas/mountainshares-trust-receipts/v1/policy-decision-receipt.schema.json",
      "schemas/mountainshares-trust-receipts/v1/projection-receipt.schema.json",
      "schemas/mountainshares-trust-receipts/v1/response-receipt.schema.json",
      "schemas/mountainshares-trust-receipts/v1/runtime-admission-record.schema.json",
      "schemas/mountainshares-trust-receipts/v1/runtime-authority-manifest.schema.json",
      "schemas/mountainshares-trust-receipts/v1/signed-operation-intent.schema.json"
    ],
    "service_tests": [
      "services/test_aacpe_features.py",
      "services/test_aapcappe_corpus.py",
      "services/test_aapcappe_retrieval.py",
      "services/test_caller_auth.py",
      "services/test_chroma_client.py",
      "services/test_chromadb_heartbeat.py",
      "services/test_chromadb_v2_heartbeat.py",
      "services/test_ddg_verbose.py",
      "services/test_end_to_end_woah_fifthdgm.py",
      "services/test_fifth_dgm_integration.py",
      "services/test_full_brain_integration.py",
      "services/test_gbim_llm_summary.py",
      "services/test_gbim_semantic_query.py",
      "services/test_geodb_llm_summary.py",
      "services/test_gis_chat.py",
      "services/test_health_access_gbim.py",
      "services/test_imm_query.py",
      "services/test_knowledge_base.py",
      "services/test_method_tracking.py",
      "services/test_multi_collection_query.py",
      "services/test_rag.py",
      "services/test_retrieval_endpoint.py",
      "services/test_spatial_awareness.py",
      "services/test_stage_6_11_6_enforcement.py",
      "services/test_stage_6_11_7_admission_live.py"
    ]
  },
  "git": {
    "branch": "stage-6.11.6-runtime-admission-enhancement",
    "head": "5f728e632eb130e919f9b1a22c16f27d2e2566ce",
    "root": "/home/cakidd/msjarvis-trust-integration",
    "status_short": []
  },
  "implementation_rule": "Do not generate a guardian private key, issue a receipt, or admit protected projection until every verifier test passes.",
  "implementation_target": {
    "all_routes": [
      {
        "function": "health",
        "line": 124,
        "method": "GET",
        "path": "/health"
      },
      {
        "function": "constitutional_status",
        "line": 133,
        "method": "GET",
        "path": "/constitutional/status"
      },
      {
        "function": "constitutional_principles",
        "line": 147,
        "method": "GET",
        "path": "/constitutional/principles"
      },
      {
        "function": "constitutional_check",
        "line": 296,
        "method": "POST",
        "path": "/constitutional/check"
      },
      {
        "function": "constitutional_audit",
        "line": 401,
        "method": "GET",
        "path": "/constitutional/audit"
      },
      {
        "function": "constitutional_audit_stats",
        "line": 424,
        "method": "GET",
        "path": "/constitutional/audit/stats"
      },
      {
        "function": "constitutional_versions",
        "line": 459,
        "method": "GET",
        "path": "/constitutional/versions"
      },
      {
        "function": "constitutional_changes",
        "line": 494,
        "method": "GET",
        "path": "/constitutional/changes/{version}"
      },
      {
        "function": "constitutional_transparency",
        "line": 529,
        "method": "GET",
        "path": "/constitutional/transparency"
      }
    ],
    "all_top_level_functions": [
      {
        "async": false,
        "line": 59,
        "name": "write_audit_entry",
        "routes": []
      },
      {
        "async": false,
        "line": 68,
        "name": "read_audit_log",
        "routes": []
      },
      {
        "async": true,
        "line": 102,
        "name": "load_constitution_versions",
        "routes": []
      },
      {
        "async": true,
        "line": 124,
        "name": "health",
        "routes": [
          {
            "method": "GET",
            "path": "/health"
          }
        ]
      },
      {
        "async": true,
        "line": 133,
        "name": "constitutional_status",
        "routes": [
          {
            "method": "GET",
            "path": "/constitutional/status"
          }
        ]
      },
      {
        "async": true,
        "line": 147,
        "name": "constitutional_principles",
        "routes": [
          {
            "method": "GET",
            "path": "/constitutional/principles"
          }
        ]
      },
      {
        "async": false,
        "line": 170,
        "name": "_sha256_commitment",
        "routes": []
      },
      {
        "async": false,
        "line": 180,
        "name": "_require_runtime_admission",
        "routes": []
      },
      {
        "async": false,
        "line": 269,
        "name": "_authenticate_caller",
        "routes": []
      },
      {
        "async": true,
        "line": 296,
        "name": "constitutional_check",
        "routes": [
          {
            "method": "POST",
            "path": "/constitutional/check"
          }
        ]
      },
      {
        "async": true,
        "line": 401,
        "name": "constitutional_audit",
        "routes": [
          {
            "method": "GET",
            "path": "/constitutional/audit"
          }
        ]
      },
      {
        "async": true,
        "line": 424,
        "name": "constitutional_audit_stats",
        "routes": [
          {
            "method": "GET",
            "path": "/constitutional/audit/stats"
          }
        ]
      },
      {
        "async": true,
        "line": 459,
        "name": "constitutional_versions",
        "routes": [
          {
            "method": "GET",
            "path": "/constitutional/versions"
          }
        ]
      },
      {
        "async": true,
        "line": 494,
        "name": "constitutional_changes",
        "routes": [
          {
            "method": "GET",
            "path": "/constitutional/changes/{version}"
          }
        ]
      },
      {
        "async": true,
        "line": 529,
        "name": "constitutional_transparency",
        "routes": [
          {
            "method": "GET",
            "path": "/constitutional/transparency"
          }
        ]
      }
    ],
    "api_path": "services/constitutional_api.py",
    "api_sha256": "3a94b20a56bc0e3720f0b87fd2e96735804d6b4f6f6de37eb3ff9fe23f282b84",
    "constitutional_check_routes": [
      {
        "function": "constitutional_check",
        "line": 296,
        "method": "POST",
        "path": "/constitutional/check"
      }
    ]
  },
  "required_new_contracts": [
    "Policy Decision Receipt schema",
    "Memory Authorization Receipt schema",
    "Canonical signed-payload procedure",
    "Guardian issuer-key registry and key identifier",
    "PDR signature verifier",
    "MAR subject-signature verifier",
    "MAR Guardian-attestation verifier",
    "Receipt expiration verification",
    "Receipt request-binding and replay-state enforcement",
    "Fail-closed denial tests"
  ],
  "required_runtime_dependencies": {
    "cryptography": "available",
    "fastapi": "available",
    "jsonschema": "available",
    "pydantic": "available"
  },
  "type": "msjarvis.pdr-mar-build-contract/v1"
}

=== contract hash ===
6280e66934c41a3a3a2c8178a61df88f49216df3cb43baa5737955df7c99b1b9  /tmp/msjarvis-guardian-pdr-mar-build-contract.json

Shell remains active.
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ 

