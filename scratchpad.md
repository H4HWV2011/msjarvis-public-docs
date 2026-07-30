(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ grep -RInE 'state/get|state/set|hilbert|kyc|vault|person|identity|userid|role' \
  . \
  --include='*.py' \
  --include='*.yml' \
  --include='*.yaml' \
  2>/dev/null | head -n 400
./enrich_where.py:9:# Collect distinct source tables from BOTH key variants in identity
./enrich_where.py:12:        identity->>'source_table',
./enrich_where.py:13:        identity->>'sourcetable'
./enrich_where.py:16:    WHERE identity IS NOT NULL
./enrich_where.py:20:print(f"Found {len(source_tables)} distinct source tables in identity")
./enrich_where.py:45:                b.identity->>'source_table',
./enrich_where.py:46:                b.identity->>'sourcetable'
./enrich_where.py:49:                b.identity->>'source_pk',
./enrich_where.py:50:                b.identity->>'sourcepk'
./gisgeodb_storage.py:29:def get_hilbert_collection():
./token_service.py:8:        userid:     "first_last",
./token_service.py:10:        role:       "user" | "carrie_admin",
./token_service.py:14:    redteam:quota:<userid> = hash {
./token_service.py:40:    def issue_token(self, *, userid: str, label: str, role: str = "newcomer", rank: str = "newcomer") -> str:
./token_service.py:43:        if role not in _ARCH + _GAMIFIED:
./token_service.py:44:            raise ValueError(f'unknown role {role!r}')
./token_service.py:56:            "userid":     userid,
./token_service.py:58:            "role":       role,    # architectural: admin|user|carrie_admin
./token_service.py:62:            "sub":        userid,
./token_service.py:67:        # Quota hash — matches existing schema. Idempotent on userid.
./token_service.py:68:        if not self.redis.exists(f"redteam:quota:{userid}"):
./token_service.py:69:            self.redis.hset(f"redteam:quota:{userid}", mapping={
./token_service.py:101:    def list_tokens_for_userid(self, userid: str) -> list[str]:
./token_service.py:102:        """Useful for revoke-all-by-userid flows. Scans redteam:token:* keys."""
./token_service.py:107:            record_userid = record.get("userid") or record.get(b"userid")
./token_service.py:108:            if isinstance(record_userid, bytes):
./token_service.py:109:                record_userid = record_userid.decode()
./token_service.py:110:            if record_userid == userid:
./token_service.py:122:        Expected Redis key: user:{userid}  fields: password_hash, roles, county, uei
./token_service.py:129:        # If not found, scan for matching proposed_userid (UUID-keyed records)
./token_service.py:133:                if rec.get("proposed_userid", "").lower() == username_clean:
./token_service.py:150:        roles = [r for r in record.get("roles", "user").split(",") if r]
./token_service.py:151:        arch_roles = [r for r in roles if r in ("admin", "user", "carrie_admin")]
./token_service.py:154:            userid=record.get("userid") or username.strip().lower(),
./token_service.py:156:            role=arch_roles[0] if arch_roles else "user",
./token_service.py:163:            "roles": roles,
./token_service.py:171:        Payload keys: sub, roles, uei, county, label.
./token_service.py:177:            "sub": record.get("userid", ""),
./token_service.py:178:            "roles": [r for r in record.get("roles", record.get("role", "user")).split(",") if r],
./token_service.py:187:        Refresh tokens are stored as: refresh:{token} -> userid
./token_service.py:189:        userid = self.redis.get(f"refresh:{refresh_token}")
./token_service.py:190:        if not userid:
./token_service.py:193:        token = self.issue_token(userid=userid, label="refresh", role="user")
./thesis_chapter_gates/probes/ch23_dual_tracks_meaning_analysis_probe.py:10:from services.hilbert.dual_track_meaning_analysis import COLLECTION_NAME, run_contract_probe
./thesis_chapter_gates/probes/ch23_dual_tracks_meaning_analysis_probe.py:15:    "hilbert_state": "http://127.0.0.1:18092/health",
./thesis_chapter_gates/probes/ch23_dual_tracks_meaning_analysis_probe.py:16:    "hilbert_time": "http://127.0.0.1:18094/health",
./thesis_chapter_gates/probes/ch23_dual_tracks_meaning_analysis_probe.py:62:    source = ROOT / "services/hilbert/dual_track_meaning_analysis.py"
./thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:12:from services.hilbert.per_user_direct_sum_memory import direct_sum_contract
./thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:30:        "services/hilbert/per_user_direct_sum_memory.py": [
./thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:39:        "services/hilbert/conversation_retention_worker.py": [
./thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:43:        "services/hilbert/conversation_manifest.py": [
./thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:47:        "services/hilbert/people_session_promotion.py": [
./thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:137:        "hilbert_state": http_json("http://127.0.0.1:18092/health"),
./thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:138:        "hilbert_time": http_json("http://127.0.0.1:18094/health"),
./thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:192:                "role, purpose, permitted-use, and legal-authority fields are projected into the routing verdict",
./thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:12:from services.hilbert.mountainshares_dao_governance import demo_contract
./thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:30:        "services/hilbert/mountainshares_dao_governance.py": [
./thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:36:            "community_hilbert_commons",
./thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:38:        "services/hilbert/community_commons_aggregation.py": [
./thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:41:            "community_hilbert_commons",
./thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:43:        "services/hilbert/continuous_validation_harness.py": [
./thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:87:    for name in ["commons_rag", "community_hilbert_commons", valid["collection"]]:
./thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:96:            "community_hilbert_commons": "community_hilbert_commons" in after,
./thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:115:        "hilbert_state": http_json("http://127.0.0.1:18092/health"),
./thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:144:        if not chroma["families"]["community_hilbert_commons"]:
./thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:145:            blockers.append("community_hilbert_commons_not_visible")
./thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:163:                "proposal admission requires role, place, community scope, public benefit, evidence, and consent where required",
./thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:166:                "commons_rag and community_hilbert_commons are runtime-visible supporting collections",
./thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:174:                "unconsented identity disclosure",
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:14:from services.hilbert.temporal_hilbert_axis import demo_contract
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:60:    out["existing_temporal_keys"] = run_cmd(["bash", "-lc", "redis-cli -p 6380 keys 'hilbert:time:*' | sort | head -20"])
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:61:    out["existing_ephemeral_keys"] = run_cmd(["bash", "-lc", "redis-cli -p 6380 keys 'hilbert:ephemeral:*' | sort | head -20"])
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:62:    out["existing_staged_keys"] = run_cmd(["bash", "-lc", "redis-cli -p 6380 keys 'hilbert:staged:*' | sort | head -20"])
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:95:            "jarvis_hilbert_time",
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:96:            "hilbert_time",
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:112:        "services/hilbert/temporal_hilbert_axis.py": [
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:113:            "hilbert:time:",
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:114:            "hilbert:ephemeral:",
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:115:            "hilbert:staged:",
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:122:        "services/hilbert/recurrent_epistemic_runner.py": [
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:125:            "identity",
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:164:        "hilbert_time": http_json("http://127.0.0.1:18094/health"),
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:165:        "hilbert_state": http_json("http://127.0.0.1:18092/health"),
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:174:    ht = endpoints["hilbert_time"].get("body", {})
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:178:            blockers.append(f"hilbert_time_{tier}_not_connected")
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:212:        if rel.endswith("temporal_hilbert_axis.py") and missing:
./thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:219:        "name": "temporal_hilbert_axis",
./thesis_chapter_gates/probes/appendix_a_probe.py:24:      "Commons gateway live on port 8055 with community_hilbert_commons collection",
./thesis_chapter_gates/probes/appendix_a_probe.py:25:      "Temporal keys confirmed under hilbert:time:* (admitted + staged) in Redis",
./thesis_chapter_gates/probes/appendix_a_probe.py:26:      "DGM cycle, retention worker, identity promotion are live scheduled runners",
./thesis_chapter_gates/probes/appendix_a_probe.py:61:    "hilbert_time":         "http://127.0.0.1:18094/health",
./thesis_chapter_gates/probes/appendix_a_probe.py:62:    "hilbert_state":        "http://127.0.0.1:18092/health",
./thesis_chapter_gates/probes/appendix_a_probe.py:77:    r = subprocess.run(["redis-cli","-p","6380","keys","hilbert:*"],
./thesis_chapter_gates/probes/appendix_a_probe.py:83:        r2 = subprocess.run(["redis-cli","keys","hilbert:*"],
./thesis_chapter_gates/probes/appendix_a_probe.py:87:result["redis_hilbert_keys"] = redis_keys
./thesis_chapter_gates/probes/appendix_a_probe.py:88:result["redis_hilbert_key_count"] = len(redis_keys)
./thesis_chapter_gates/probes/appendix_a_probe.py:140:    "hilbert_time":         ["jarvis-hilbert-time"],
./thesis_chapter_gates/probes/appendix_a_probe.py:141:    "hilbert_state":        ["jarvis-hilbert-state"],
./thesis_chapter_gates/probes/appendix_a_probe.py:170:    "epistemic_loop_scheduled":    re.compile(r"dgm_cycle\.sh|conversation_retention_worker|identity_promotion\.py", re.I),
./thesis_chapter_gates/probes/appendix_a_probe.py:171:    "hilbert_time_port_named":     re.compile(r"18094|hilbert.time.*18094|jarvis-hilbert-time", re.I),
./thesis_chapter_gates/probes/overview_docs_probe.py:15:    "04/44 (hilbert/phi-probe)", "05/06 (chromadb/geodb)", "07 (rag-pipeline)",
./thesis_chapter_gates/probes/overview_docs_probe.py:20:    "21 (background-store)", "22 (identity-retention)", "23 (dual-tracks)",
./thesis_chapter_gates/probes/overview_docs_probe.py:24:    "33/35 (llm-ensemble/swarm)", "34 (spiritual-root)", "36 (identity-registration)",
./thesis_chapter_gates/probes/overview_docs_probe.py:26:    "41 (test-harness)", "42/43 (post-quantum/role-gated)", "45/46 (H_geo/tensor)",
./thesis_chapter_gates/probes/overview_docs_probe.py:27:    "47/48 (hilbert-people)", "49 (temporal-hilbert-axis)", "50 (per-user-direct-sum)",
./thesis_chapter_gates/probes/overview_docs_probe.py:28:    "51 (community-hilbert-commons)", "52 (recurrent-epistemic-loop)",
./thesis_chapter_gates/probes/overview_docs_probe.py:63:      "Ms. Allis is not a simulation of WV identity — it is architecturally constrained by it"
./thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:12:from services.hilbert.external_communication_authority import demo_contract
./thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:30:        "services/hilbert/external_communication_authority.py": [
./thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:38:        "services/hilbert/per_user_direct_sum_memory.py": [
./thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:43:        "services/hilbert/mountainshares_dao_governance.py": [
./thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:47:        "services/hilbert/broader_layer_feedback.py": [
./thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:105:            "community_hilbert_commons": "community_hilbert_commons" in after,
./thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:119:        "hilbert_state": http_json("http://127.0.0.1:18092/health"),
./thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:168:                "private or person-linked external disclosure requires retention consent plus public opt-in or legal authority and human review",
./thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:12:from services.hilbert.broader_layer_feedback import demo_contract
./thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:30:        "services/hilbert/broader_layer_feedback.py": [
./thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:39:        "services/hilbert/background_pattern_store.py": [
./thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:44:        "services/hilbert/automated_learning_gap_review.py": [
./thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:49:        "services/hilbert/continuous_validation_harness.py": [
./thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:53:        "services/hilbert/recurrent_epistemic_runner.py": [
./thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:55:            "identity",
./thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:111:        "community_hilbert_commons": "community_hilbert_commons" in after,
./thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:129:        "hilbert_state": http_json("http://127.0.0.1:18092/health"),
./thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:130:        "hilbert_time": http_json("http://127.0.0.1:18094/health"),
./thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py:15:    "jarvis-hilbert-state": {"host_port": "18092", "health": "http://127.0.0.1:18092/health"},
./thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py:16:    "jarvis-hilbert-time": {"host_port": "18094", "health": "http://127.0.0.1:18094/health"},
./thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py:182:        "services/hilbert/recurrent_epistemic_runner.py",
./thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py:198:        "hilbert_time_route_present": "18094" in source_text or "jarvis-hilbert-time" in source_text,
./thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py:199:        "hilbert_state_route_present": "18092" in source_text or "jarvis-hilbert-state" in source_text,
./thesis_chapter_gates/probes/ch34_spiritual_root_mother_carrie_probe.py:194:                "spiritual language is treated as identity/support/governance vocabulary rather than supernatural authority",
./thesis_chapter_gates/probes/ch27_probe.py:21:      "R != K and R != G: retrieval is never identity with governed knowledge or approved guidance",
./thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:13:from services.hilbert.quantum_inspired_entanglement import demo_contract
./thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:52:    out["existing_entanglement_keys"] = run_cmd(["bash", "-lc", "redis-cli -p 6380 keys 'hilbert:entanglement:*' | sort | head -50"])
./thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:95:            "hilbert_entanglement_associations_ch08": contract["collection"] in after,
./thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:106:        "services/hilbert/quantum_inspired_entanglement.py": [
./thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:113:        "services/hilbert/hilbert_phi_closure_probe.py": [
./thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:117:        "services/hilbert/tensor_geo_bridge.py": [
./thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:121:        "services/hilbert/per_user_direct_sum_memory.py": [
./thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:139:        "hilbert_state": http_json("http://127.0.0.1:18092/health"),
./thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:140:        "hilbert_time": http_json("http://127.0.0.1:18094/health"),
./thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:172:        if not chroma["families"]["hilbert_entanglement_associations_ch08"]:
./auth_api.patched.py:173:Proposed userid: {proposed}
./auth_api.patched.py:212:    userid = user["userid"]
./auth_api.patched.py:214:    uei    = r.get(f"uei:by_user:{userid}")
./auth_api.patched.py:215:    wallet = ws.get_wallet_public(userid)
./auth_api.patched.py:216:    quota  = r.hgetall(f"redteam:quota:{userid}") or {}
./auth_api.patched.py:217:    profile= r.hgetall(f"user:{userid}") or {}
./auth_api.patched.py:220:        "userid":  userid,
./auth_api.patched.py:221:        "name":    profile.get("name", userid),
./auth_api.patched.py:223:        "role":    user.get("role", "user"),
./auth_api.patched.py:240:    userid = user["userid"]
./auth_api.patched.py:241:    role   = user.get("role", "user")
./auth_api.patched.py:244:    quota_key = f"redteam:quota:{userid}"
./auth_api.patched.py:252:    if count >= limit and role not in ("carrie_admin", "admin"):
./auth_api.patched.py:267:            json={"message": req.message, "user_id": userid, "role": role},
./merkle_identity.py:2:merkle_identity.py
./merkle_identity.py:4:Sparse Merkle Tree-backed identity commitment for MountainShares.
./merkle_identity.py:168:    print("✅ merkle_identity self-test passed")
./layer3_opt_in.py:4:Grants Layer 3 opt-in on all H_p + hilbert_time collections.
./layer3_opt_in.py:8:sys.path.insert(0, '/app/services/hilbert')
./layer3_opt_in.py:53:    for cname in ["public_civic_roles", "public_civic_events",
./layer3_opt_in.py:54:                  "public_civic_sources", "hilbert_time"]:
./ms_jarvis_psychology_services.py:116:            "Reach out to a trusted person nearby and tell them what is happening."
./hp_antisurveillance_guardian_client.py:7:    "person_analytics_request",
./hp_antisurveillance_guardian_client.py:8:    "identity_linkage_attempt",
./hp_antisurveillance_guardian_client.py:9:    "unified_person_profile",
./hp_antisurveillance_guardian_client.py:12:    "person_analytics",
./hp_antisurveillance_guardian_client.py:13:    "identity_linkage",
./hp_antisurveillance_guardian_client.py:17:    "public.kyc_vault",
./hp_antisurveillance_guardian_client.py:18:    "public.kyc_location_strip",
./hp_antisurveillance_guardian_client.py:19:    "public.kyc_vault_access_log",
./hp_antisurveillance_guardian_client.py:30:def _hp_antisurveillance_deny_fast(actor_role, context, action_type, content, metadata):
./hp_antisurveillance_guardian_client.py:61:            "reason": "Client-side anti-surveillance: identity tables may not be linked to H_p entities or faces.",
./hp_antisurveillance_guardian_client.py:65:        "profile" in content_l or "unified person" in content_l or "linking faces" in content_l
./hp_antisurveillance_guardian_client.py:72:            "reason": "Client-side anti-surveillance: forbidden use of private/person-identifying collection.",
./hp_antisurveillance_guardian_client.py:77:def constitutional_check(actor_role, context, action_type, content, metadata=None):
./hp_antisurveillance_guardian_client.py:79:    deny = _hp_antisurveillance_deny_fast(actor_role, context, action_type, content, metadata)
./hp_antisurveillance_guardian_client.py:84:        "actor_role": actor_role,
./hp_antisurveillance_guardian_client.py:121:def require_guarded_join(actor_role, context, action_type, content, metadata=None):
./hp_antisurveillance_guardian_client.py:122:    result = constitutional_check(actor_role, context, action_type, content, metadata)
./bootstrap_gbim_beliefs_eq1.py:188:        INSERT INTO gbim_belief_evidence (belief_id, evidence_id, role)
./bootstrap_gbim_beliefs_eq1.py:192:            'primary' AS role
./email_service.py:24:def send_approval_email(to: str, name: str, userid: str, temp_password: str = "", magic_link: str = "") -> bool:
./email_service.py:32:            f"<p>This link expires in 72 hours. Your username: <strong>{userid}</strong></p>"
./email_service.py:38:            f"This link expires in 72 hours.\nUsername: {userid}\nEmail: {to}\n"
./email_service.py:41:        body = APPROVAL_TEMPLATE.format(name=name, userid=userid, temp_password=temp_password, to=to)
./email_service.py:55:            logger.warning(f"[EMAIL] preparing send to={to} subject={subject!r} html_len={len(body)} text_len={len(text_body)} userid={userid}")
./email_service.py:64:                    {"name": "userid", "value": str(userid)}
./email_service.py:67:                    "X-Entity-Ref-ID": f"approval-{userid}"
./email_service.py:79:        "userid": userid,
./tmp_rag_slice.py:120:                    "userid": "auto_system",
./hilbert_coherence_monitor.py:10:log = logging.getLogger("hilbert-monitor")
./hilbert_coherence_monitor.py:59:    rdb.set("hilbert:coherence:latest", json.dumps(payload))
./hilbert_coherence_monitor.py:60:    rdb.lpush("hilbert:coherence:history", json.dumps(payload))
./hilbert_coherence_monitor.py:61:    rdb.ltrim("hilbert:coherence:history", 0, 1439)  # keep 24h at 60s intervals
./hilbert_coherence_monitor.py:62:    rdb.set("hilbert:coherence:system_score", system_score)
./hilbert_coherence_monitor.py:72:    # Verify hilbert-state is up
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/enrich_where.py:9:# Collect distinct source tables from BOTH key variants in identity
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/enrich_where.py:12:        identity->>'source_table',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/enrich_where.py:13:        identity->>'sourcetable'
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/enrich_where.py:16:    WHERE identity IS NOT NULL
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/enrich_where.py:20:print(f"Found {len(source_tables)} distinct source tables in identity")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/enrich_where.py:45:                b.identity->>'source_table',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/enrich_where.py:46:                b.identity->>'sourcetable'
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/enrich_where.py:49:                b.identity->>'source_pk',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/enrich_where.py:50:                b.identity->>'sourcepk'
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/gisgeodb_storage.py:29:def get_hilbert_collection():
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:8:        userid:     "first_last",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:10:        role:       "user" | "carrie_admin",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:14:    redteam:quota:<userid> = hash {
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:40:    def issue_token(self, *, userid: str, label: str, role: str = "newcomer", rank: str = "newcomer") -> str:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:43:        if role not in _ARCH + _GAMIFIED:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:44:            raise ValueError(f'unknown role {role!r}')
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:56:            "userid":     userid,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:58:            "role":       role,    # architectural: admin|user|carrie_admin
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:62:            "sub":        userid,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:67:        # Quota hash — matches existing schema. Idempotent on userid.
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:68:        if not self.redis.exists(f"redteam:quota:{userid}"):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:69:            self.redis.hset(f"redteam:quota:{userid}", mapping={
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:101:    def list_tokens_for_userid(self, userid: str) -> list[str]:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:102:        """Useful for revoke-all-by-userid flows. Scans redteam:token:* keys."""
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:107:            record_userid = record.get("userid") or record.get(b"userid")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:108:            if isinstance(record_userid, bytes):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:109:                record_userid = record_userid.decode()
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:110:            if record_userid == userid:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:122:        Expected Redis key: user:{userid}  fields: password_hash, roles, county, uei
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:129:        # If not found, scan for matching proposed_userid (UUID-keyed records)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:133:                if rec.get("proposed_userid", "").lower() == username_clean:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:150:        roles = [r for r in record.get("roles", "user").split(",") if r]
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:151:        arch_roles = [r for r in roles if r in ("admin", "user", "carrie_admin")]
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:154:            userid=record.get("userid") or username.strip().lower(),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:156:            role=arch_roles[0] if arch_roles else "user",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:163:            "roles": roles,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:171:        Payload keys: sub, roles, uei, county, label.
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:177:            "sub": record.get("userid", ""),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:178:            "roles": [r for r in record.get("roles", record.get("role", "user")).split(",") if r],
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:187:        Refresh tokens are stored as: refresh:{token} -> userid
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:189:        userid = self.redis.get(f"refresh:{refresh_token}")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:190:        if not userid:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:193:        token = self.issue_token(userid=userid, label="refresh", role="user")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch23_dual_tracks_meaning_analysis_probe.py:10:from services.hilbert.dual_track_meaning_analysis import COLLECTION_NAME, run_contract_probe
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch23_dual_tracks_meaning_analysis_probe.py:15:    "hilbert_state": "http://127.0.0.1:18092/health",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch23_dual_tracks_meaning_analysis_probe.py:16:    "hilbert_time": "http://127.0.0.1:18094/health",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch23_dual_tracks_meaning_analysis_probe.py:62:    source = ROOT / "services/hilbert/dual_track_meaning_analysis.py"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:12:from services.hilbert.per_user_direct_sum_memory import direct_sum_contract
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:30:        "services/hilbert/per_user_direct_sum_memory.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:39:        "services/hilbert/conversation_retention_worker.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:43:        "services/hilbert/conversation_manifest.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:47:        "services/hilbert/people_session_promotion.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:137:        "hilbert_state": http_json("http://127.0.0.1:18092/health"),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:138:        "hilbert_time": http_json("http://127.0.0.1:18094/health"),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:192:                "role, purpose, permitted-use, and legal-authority fields are projected into the routing verdict",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:12:from services.hilbert.mountainshares_dao_governance import demo_contract
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:30:        "services/hilbert/mountainshares_dao_governance.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:36:            "community_hilbert_commons",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:38:        "services/hilbert/community_commons_aggregation.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:41:            "community_hilbert_commons",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:43:        "services/hilbert/continuous_validation_harness.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:87:    for name in ["commons_rag", "community_hilbert_commons", valid["collection"]]:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:96:            "community_hilbert_commons": "community_hilbert_commons" in after,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:115:        "hilbert_state": http_json("http://127.0.0.1:18092/health"),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:144:        if not chroma["families"]["community_hilbert_commons"]:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:145:            blockers.append("community_hilbert_commons_not_visible")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:163:                "proposal admission requires role, place, community scope, public benefit, evidence, and consent where required",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:166:                "commons_rag and community_hilbert_commons are runtime-visible supporting collections",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch03_mountainshares_dao_probe.py:174:                "unconsented identity disclosure",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:14:from services.hilbert.temporal_hilbert_axis import demo_contract
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:60:    out["existing_temporal_keys"] = run_cmd(["bash", "-lc", "redis-cli -p 6380 keys 'hilbert:time:*' | sort | head -20"])
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:61:    out["existing_ephemeral_keys"] = run_cmd(["bash", "-lc", "redis-cli -p 6380 keys 'hilbert:ephemeral:*' | sort | head -20"])
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:62:    out["existing_staged_keys"] = run_cmd(["bash", "-lc", "redis-cli -p 6380 keys 'hilbert:staged:*' | sort | head -20"])
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:95:            "jarvis_hilbert_time",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:96:            "hilbert_time",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:112:        "services/hilbert/temporal_hilbert_axis.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:113:            "hilbert:time:",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:114:            "hilbert:ephemeral:",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:115:            "hilbert:staged:",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:122:        "services/hilbert/recurrent_epistemic_runner.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:125:            "identity",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:164:        "hilbert_time": http_json("http://127.0.0.1:18094/health"),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:165:        "hilbert_state": http_json("http://127.0.0.1:18092/health"),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:174:    ht = endpoints["hilbert_time"].get("body", {})
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:178:            blockers.append(f"hilbert_time_{tier}_not_connected")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:212:        if rel.endswith("temporal_hilbert_axis.py") and missing:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch49_temporal_hilbert_axis_probe.py:219:        "name": "temporal_hilbert_axis",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/appendix_a_probe.py:24:      "Commons gateway live on port 8055 with community_hilbert_commons collection",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/appendix_a_probe.py:25:      "Temporal keys confirmed under hilbert:time:* (admitted + staged) in Redis",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/appendix_a_probe.py:26:      "DGM cycle, retention worker, identity promotion are live scheduled runners",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/appendix_a_probe.py:61:    "hilbert_time":         "http://127.0.0.1:18094/health",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/appendix_a_probe.py:62:    "hilbert_state":        "http://127.0.0.1:18092/health",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/appendix_a_probe.py:77:    r = subprocess.run(["redis-cli","-p","6380","keys","hilbert:*"],
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/appendix_a_probe.py:83:        r2 = subprocess.run(["redis-cli","keys","hilbert:*"],
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/appendix_a_probe.py:87:result["redis_hilbert_keys"] = redis_keys
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/appendix_a_probe.py:88:result["redis_hilbert_key_count"] = len(redis_keys)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/appendix_a_probe.py:140:    "hilbert_time":         ["jarvis-hilbert-time"],
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/appendix_a_probe.py:141:    "hilbert_state":        ["jarvis-hilbert-state"],
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/appendix_a_probe.py:170:    "epistemic_loop_scheduled":    re.compile(r"dgm_cycle\.sh|conversation_retention_worker|identity_promotion\.py", re.I),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/appendix_a_probe.py:171:    "hilbert_time_port_named":     re.compile(r"18094|hilbert.time.*18094|jarvis-hilbert-time", re.I),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/overview_docs_probe.py:15:    "04/44 (hilbert/phi-probe)", "05/06 (chromadb/geodb)", "07 (rag-pipeline)",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/overview_docs_probe.py:20:    "21 (background-store)", "22 (identity-retention)", "23 (dual-tracks)",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/overview_docs_probe.py:24:    "33/35 (llm-ensemble/swarm)", "34 (spiritual-root)", "36 (identity-registration)",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/overview_docs_probe.py:26:    "41 (test-harness)", "42/43 (post-quantum/role-gated)", "45/46 (H_geo/tensor)",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/overview_docs_probe.py:27:    "47/48 (hilbert-people)", "49 (temporal-hilbert-axis)", "50 (per-user-direct-sum)",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/overview_docs_probe.py:28:    "51 (community-hilbert-commons)", "52 (recurrent-epistemic-loop)",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/overview_docs_probe.py:63:      "Ms. Allis is not a simulation of WV identity — it is architecturally constrained by it"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:12:from services.hilbert.external_communication_authority import demo_contract
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:30:        "services/hilbert/external_communication_authority.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:38:        "services/hilbert/per_user_direct_sum_memory.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:43:        "services/hilbert/mountainshares_dao_governance.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:47:        "services/hilbert/broader_layer_feedback.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:105:            "community_hilbert_commons": "community_hilbert_commons" in after,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:119:        "hilbert_state": http_json("http://127.0.0.1:18092/health"),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py:168:                "private or person-linked external disclosure requires retention consent plus public opt-in or legal authority and human review",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:12:from services.hilbert.broader_layer_feedback import demo_contract
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:30:        "services/hilbert/broader_layer_feedback.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:39:        "services/hilbert/background_pattern_store.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:44:        "services/hilbert/automated_learning_gap_review.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:49:        "services/hilbert/continuous_validation_harness.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:53:        "services/hilbert/recurrent_epistemic_runner.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:55:            "identity",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:111:        "community_hilbert_commons": "community_hilbert_commons" in after,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:129:        "hilbert_state": http_json("http://127.0.0.1:18092/health"),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:130:        "hilbert_time": http_json("http://127.0.0.1:18094/health"),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py:15:    "jarvis-hilbert-state": {"host_port": "18092", "health": "http://127.0.0.1:18092/health"},
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py:16:    "jarvis-hilbert-time": {"host_port": "18094", "health": "http://127.0.0.1:18094/health"},
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py:182:        "services/hilbert/recurrent_epistemic_runner.py",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py:198:        "hilbert_time_route_present": "18094" in source_text or "jarvis-hilbert-time" in source_text,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch19_container_architecture_routing_probe.py:199:        "hilbert_state_route_present": "18092" in source_text or "jarvis-hilbert-state" in source_text,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch34_spiritual_root_mother_carrie_probe.py:194:                "spiritual language is treated as identity/support/governance vocabulary rather than supernatural authority",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch27_probe.py:21:      "R != K and R != G: retrieval is never identity with governed knowledge or approved guidance",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:13:from services.hilbert.quantum_inspired_entanglement import demo_contract
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:52:    out["existing_entanglement_keys"] = run_cmd(["bash", "-lc", "redis-cli -p 6380 keys 'hilbert:entanglement:*' | sort | head -50"])
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:95:            "hilbert_entanglement_associations_ch08": contract["collection"] in after,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:106:        "services/hilbert/quantum_inspired_entanglement.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:113:        "services/hilbert/hilbert_phi_closure_probe.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:117:        "services/hilbert/tensor_geo_bridge.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:121:        "services/hilbert/per_user_direct_sum_memory.py": [
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:139:        "hilbert_state": http_json("http://127.0.0.1:18092/health"),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:140:        "hilbert_time": http_json("http://127.0.0.1:18094/health"),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:172:        if not chroma["families"]["hilbert_entanglement_associations_ch08"]:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:173:Proposed userid: {proposed}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:212:    userid = user["userid"]
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:214:    uei    = r.get(f"uei:by_user:{userid}")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:215:    wallet = ws.get_wallet_public(userid)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:216:    quota  = r.hgetall(f"redteam:quota:{userid}") or {}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:217:    profile= r.hgetall(f"user:{userid}") or {}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:220:        "userid":  userid,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:221:        "name":    profile.get("name", userid),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:223:        "role":    user.get("role", "user"),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:240:    userid = user["userid"]
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:241:    role   = user.get("role", "user")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:244:    quota_key = f"redteam:quota:{userid}"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:252:    if count >= limit and role not in ("carrie_admin", "admin"):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:267:            json={"message": req.message, "user_id": userid, "role": role},
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/merkle_identity.py:2:merkle_identity.py
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/merkle_identity.py:4:Sparse Merkle Tree-backed identity commitment for MountainShares.
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/merkle_identity.py:168:    print("✅ merkle_identity self-test passed")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/layer3_opt_in.py:4:Grants Layer 3 opt-in on all H_p + hilbert_time collections.
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/layer3_opt_in.py:8:sys.path.insert(0, '/app/services/hilbert')
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/layer3_opt_in.py:53:    for cname in ["public_civic_roles", "public_civic_events",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/layer3_opt_in.py:54:                  "public_civic_sources", "hilbert_time"]:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/ms_jarvis_psychology_services.py:116:            "Reach out to a trusted person nearby and tell them what is happening."
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:7:    "person_analytics_request",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:8:    "identity_linkage_attempt",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:9:    "unified_person_profile",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:12:    "person_analytics",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:13:    "identity_linkage",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:17:    "public.kyc_vault",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:18:    "public.kyc_location_strip",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:19:    "public.kyc_vault_access_log",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:30:def _hp_antisurveillance_deny_fast(actor_role, context, action_type, content, metadata):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:61:            "reason": "Client-side anti-surveillance: identity tables may not be linked to H_p entities or faces.",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:65:        "profile" in content_l or "unified person" in content_l or "linking faces" in content_l
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:72:            "reason": "Client-side anti-surveillance: forbidden use of private/person-identifying collection.",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:77:def constitutional_check(actor_role, context, action_type, content, metadata=None):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:79:    deny = _hp_antisurveillance_deny_fast(actor_role, context, action_type, content, metadata)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:84:        "actor_role": actor_role,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:121:def require_guarded_join(actor_role, context, action_type, content, metadata=None):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:122:    result = constitutional_check(actor_role, context, action_type, content, metadata)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/bootstrap_gbim_beliefs_eq1.py:188:        INSERT INTO gbim_belief_evidence (belief_id, evidence_id, role)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/bootstrap_gbim_beliefs_eq1.py:192:            'primary' AS role
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/email_service.py:24:def send_approval_email(to: str, name: str, userid: str, temp_password: str = "", magic_link: str = "") -> bool:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/email_service.py:32:            f"<p>This link expires in 72 hours. Your username: <strong>{userid}</strong></p>"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/email_service.py:38:            f"This link expires in 72 hours.\nUsername: {userid}\nEmail: {to}\n"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/email_service.py:41:        body = APPROVAL_TEMPLATE.format(name=name, userid=userid, temp_password=temp_password, to=to)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/email_service.py:55:            logger.warning(f"[EMAIL] preparing send to={to} subject={subject!r} html_len={len(body)} text_len={len(text_body)} userid={userid}")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/email_service.py:64:                    {"name": "userid", "value": str(userid)}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/email_service.py:67:                    "X-Entity-Ref-ID": f"approval-{userid}"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/email_service.py:79:        "userid": userid,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/tmp_rag_slice.py:120:                    "userid": "auto_system",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hilbert_coherence_monitor.py:10:log = logging.getLogger("hilbert-monitor")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hilbert_coherence_monitor.py:59:    rdb.set("hilbert:coherence:latest", json.dumps(payload))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hilbert_coherence_monitor.py:60:    rdb.lpush("hilbert:coherence:history", json.dumps(payload))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hilbert_coherence_monitor.py:61:    rdb.ltrim("hilbert:coherence:history", 0, 1439)  # keep 24h at 60s intervals
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hilbert_coherence_monitor.py:62:    rdb.set("hilbert:coherence:system_score", system_score)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hilbert_coherence_monitor.py:72:    # Verify hilbert-state is up
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/output/47_inline_projection_logic_patch.py:16:def enforce_projection(purpose: str, role: str, consent_tags: list[str], legal_authority: bool = False):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/output/47_inline_projection_logic_patch.py:22:        "allowed_roles": ["case_worker", "benefit_admin"],
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/output/47_inline_projection_logic_patch.py:28:    if role not in set(policy["allowed_roles"]):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/output/47_patch_projection_eligibility_route.py:46:    x_role: str = Header(...),
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

