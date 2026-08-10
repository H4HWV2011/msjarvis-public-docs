(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~$ cd "$HOME/msjarvis-guardian-deploy-candidate-e8827b2"

docker ps \
  --filter 'name=jarvis-unified-gateway' \
  --filter 'name=jarvis-unified-gateway-authz-canary' \
  --format 'CONTAINER={{.Names}} STATUS={{.Status}} PORTS={{.Ports}} IMAGE={{.Image}}'

printf '\n=== LIVE GATEWAY HEALTH ===\n'
curl --silent --show-error --max-time 15 \
  --write-out '\nHTTP_STATUS=%{http_code}\n' \
  http://127.0.0.1:8093/health

printf '\n=== CANARY HEALTH ===\n'
curl --silent --show-error --max-time 15 \
  --write-out '\nHTTP_STATUS=%{http_code}\n' \
  http://127.0.0.1:18093/health
CONTAINER=jarvis-unified-gateway-authz-canary STATUS=Up 8 hours PORTS=127.0.0.1:18093->8001/tcp IMAGE=msjarvis-rebuild-jarvis-unified-gateway:authz-canary-20260809
CONTAINER=jarvis-unified-gateway STATUS=Up 7 hours PORTS=0.0.0.0:8093->8001/tcp, [::]:8093->8001/tcp IMAGE=msjarvis-rebuild-jarvis-unified-gateway:latest

=== LIVE GATEWAY HEALTH ===
{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://nbb_qualia_engine:8010","responsive":true},"constitutional_guardian":{"status":"healthy","url":"http://jarvis-constitutional-guardian:8091","responsive":true},"wv_ensemble":{"status":"healthy","url":"http://jarvis-wv-entangled-gateway:8010","responsive":true}},"total_queries":0,"constitutional_blocks":0,"timestamp":"2026-08-10T11:28:47.127886"}
HTTP_STATUS=200

=== CANARY HEALTH ===
{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://nbb_qualia_engine:8010","responsive":true},"constitutional_guardian":{"status":"healthy","url":"http://jarvis-constitutional-guardian:8091","responsive":true},"wv_ensemble":{"status":"healthy","url":"http://jarvis-wv-entangled-gateway:8010","responsive":true}},"total_queries":0,"constitutional_blocks":0,"timestamp":"2026-08-10T11:28:47.214858"}
HTTP_STATUS=200
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ cd "$HOME/msjarvis-guardian-deploy-candidate-e8827b2"

cat > trust_architecture/release_evidence/run_gateway_canary_auth_test.sh <<'BASH'
#!/usr/bin/env bash

CANARY_USERID="rollout-canary-20260810"
CANARY_LABEL="gateway-authentication-canary-20260810"
TOKEN=""
TOKEN_CONFIG=""
AUTH_BODY=""
CHAT_BODY=""

cleanup() {
  if [ -n "$TOKEN" ]; then
    printf '%s' "$TOKEN" | docker exec -i jarvis-auth-api python -c '
import os
import sys
import redis
from services.token_service import TokenService

token = sys.stdin.read().strip()
r = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"), decode_re  trust_architecture/release_evidence/run_gateway_canary_auth_test.sh_test.shon.
TOKEN_ISSUANCE_FAILED
TOKEN_REVOCATION_ATTEMPTED=YES
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ docker exec -i jarvis-auth-api python - <<'PY'
import os
import sys

print("TOKEN_SERVICE_IMPORT=UNKNOWN")
print("REDIS_URL_PRESENT=" + ("YES" if os.getenv("REDIS_URL") else "NO"))

try:
    import redis
    from services.token_service import TokenService
    print("TOKEN_SERVICE_IMPORT=OK")
except Exception as exc:
    print("TOKEN_SERVICE_IMPORT_ERROR=" + type(exc).__name__)
    sys.exit(0)

try:
    r = redis.from_url(
        os.getenv("REDIS_URL", "redis://localhost:6379/0"),
        decode_responses=True,
    )
    r.ping()
    print("REDIS_PING=OK")
except Exception as exc:
PY      print("TEMPORARY_TOKEN_REVOKE=NOT_REQUIRED")type(exc).__name__)
TOKEN_SERVICE_IMPORT=UNKNOWN
REDIS_URL_PRESENT=YES
TOKEN_SERVICE_IMPORT=OK
REDIS_PING=OK
TEMPORARY_TOKEN_ISSUE_ERROR=TypeError
TEMPORARY_TOKEN_REVOKE=NOT_REQUIRED
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ psql -h <host> -U <user> -d <db> -c "\dn"
psql -h <host> -U <user> -d <db> -c "\dt <schema>.*"
psql -h <host> -U <user> -d <db> -c "SELECT count(*) FROM <schema>.<table>;"
psql -h <host> -U <user> -d <db> -c "SELECT count(*) FROM <schema>.<admissible_view>;"
bash: host: No such file or directory
bash: host: No such file or directory
bash: host: No such file or directory
bash: host: No such file or directory
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ pg_lsclusters
Ver Cluster  Port Status Owner     Data directory                              Log file
16  main     5432 down   <unknown> /var/lib/postgresql/16/main                 /var/log/postgresql/postgresql-16-main.log
16  msjarvis 5436 online postgres  /mnt/spiritual_drive/pgdata_native_msjarvis /var/log/postgresql/postgresql-16-msjarvis.log
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ sudo ss -ltnp | grep -E '5432|5433'
[sudo] password for cakidd: 
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ psql -l
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory
	Is the server running locally and accepting connections on that socket?
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ sudo -u postgres psql -l
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory
	Is the server running locally and accepting connections on that socket?
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ grep -rniE 'postgres|dbname|POSTGRES_|DATABASE_URL|:5432' . --include='*.env' --include='*.yml' --include='*.yaml' --include='*.py' --include='*.sh' 2>/dev/null | grep -iv 'node_modules' | head -40
./enrich_where.py:3:CONN_STR = "postgresql://postgres:postgres@localhost:5435/msjarvisgis"
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:129:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:144:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:450:    runtime=len(re.findall(r"`[^`]+`|http://|https://|docker|redis|postgres|chroma|service|endpoint|container", text, re.I))
./thesis_chapter_gates/close_ch37_no_build_v2.sh:250:Use the recovered pre-duplication language as the prose base, but replace April 2026 operational counts, ports, database sizes, and closure claims with July 2026 as-built evidence. Do not restore stale container counts or old PostgreSQL/Chroma totals as current truth.
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:19:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:37:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -v ON_ERROR_STOP=1 <<'SQL'
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:38:GRANT USAGE ON SCHEMA public TO postgres;
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:39:GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON public.gbim_collection_manifest TO postgres;
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:40:GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON public.gbim_active_collection TO postgres;
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:41:GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON public.gbim_chroma_publication_manifest TO postgres;
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:51:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:52:SELECT 'SCHEMA_USAGE_POSTGRES=' || has_schema_privilege('postgres','public','USAGE');
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:53:SELECT 'MANIFEST_SELECT_POSTGRES=' || has_table_privilege('postgres','public.gbim_collection_manifest','SELECT');
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:54:SELECT 'MANIFEST_REFERENCES_POSTGRES=' || has_table_privilege('postgres','public.gbim_collection_manifest','REFERENCES');
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:55:SELECT 'ACTIVE_INSERT_POSTGRES=' || has_table_privilege('postgres','public.gbim_active_collection','INSERT');
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:56:SELECT 'ACTIVE_REFERENCES_POSTGRES=' || has_table_privilege('postgres','public.gbim_active_collection','REFERENCES');
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:228:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -v ON_ERROR_STOP=1 -f "$SQLFILE"
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:233:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
./thesis_chapter_gates/gate_ch36_identity_registration.sh:465:    runtime=len(re.findall(r"`[^`]+`|http://|https://|docker|redis|postgres|chroma|service|endpoint|container", text, re.I))
./thesis_chapter_gates/next_after_ch31_operational_gate.sh:52:runtime=re.compile(r"\b(audit|validation|test|harness|health|docker|container|service|endpoint|port|redis|postgres|chroma|runner|cron|gateway)\b", re.I)
./thesis_chapter_gates/next_after_ch31_operational_gate.sh:91:rg -n "audit|validation|test|harness|health|docker|container|service|endpoint|port|redis|postgres|chroma|runner|cron|gateway|will|would|should|future|not yet|proven|complete|guarantee" "$DOCS/thesis/$NEXT_FILE" || true
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:66:- \`jarvis-hilbert-time\` is live on 18094 with ephemeral Redis, staged Redis, and historical Postgres connected.
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:160:    runtime=len(re.findall(r"`[^`]+`|http://|https://|docker|redis|postgres|chroma|service|endpoint|container", text, re.I))
./thesis_chapter_gates/gate_ch46_ch45.sh:35:  for DB in msjarvisgis msjarvisgis_v2 hilbert_people postgres; do
./thesis_chapter_gates/gate_ch46_ch45.sh:37:    PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d "$DB" -Atc "
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:692:    refs=len(re.findall(r"\b(port|docker|service|redis|postgres|chroma|endpoint|cron|health|runner)\b", text, re.I))
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:444:for DB in msjarvisgis msjarvisgis_v2 postgres; do
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:446:  PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d "$DB" -Atc "
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:19:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:37:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -v ON_ERROR_STOP=1 <<'SQL'
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:42:  EXECUTE 'GRANT USAGE ON SCHEMA public TO postgres';
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:43:  EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON public.gbim_collection_manifest TO postgres';
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:44:  EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON public.gbim_active_collection TO postgres';
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:45:  EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON public.gbim_chroma_publication_manifest TO postgres';
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:52:      AND tableowner <> 'postgres'
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:216:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -v ON_ERROR_STOP=1 -f "$SQLFILE"
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:220:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
./thesis_chapter_gates/remediate_ch02_zcta_manifest.sh:193:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -v ON_ERROR_STOP=1 -f "$SQLFILE"
./thesis_chapter_gates/remediate_ch02_zcta_manifest.sh:197:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ docker ps
CONTAINER ID   IMAGE                                                             COMMAND                  CREATED        STATUS                          PORTS                                                                                                          NAMES
def9fd16d39e   msjarvis-rebuild-jarvis-unified-gateway:authz-canary-20260809     "/app/gateway-entryp…"   8 hours ago    Up 8 hours                      127.0.0.1:18093->8001/tcp                                                                                      jarvis-unified-gateway-authz-canary
781a11ee67e0   msjarvis-fractal-candidate:e8827b2-recovery                       "python3 /app/ms_jar…"   11 hours ago   Up 11 hours                     8002/tcp                                                                                                       jarvis-fractal-consciousness
0bd8ff067e8e   msjarvis-fractal-candidate:e8827b2-recovery                       "python3 /app/ms_jar…"   11 hours ago   Up 11 hours                                                                                                                                    fractal-listener-smoke-e8827b2-1988345
aeb0fb8f5a5f   msjarvis-rebuild-jarvis-qualia-engine                             "/app/venv/bin/pytho…"   6 days ago     Up 4 days                       127.0.0.1:8017->8017/tcp                                                                                       jarvis-qualia-engine
fe512ffd7deb   msjarvis-rebuild-jarvis-contracts                                 "docker-entrypoint.s…"   6 days ago     Up 4 days                                                                                                                                      jarvis-contracts
94cd67df7830   ipfs/kubo:latest                                                  "/sbin/tini -- /usr/…"   6 days ago     Up 4 days (healthy)             4001/tcp, 8080-8081/tcp, 4001/udp, 127.0.0.1:5001->5001/tcp                                                    ipfs
9e1ae987d0e7   msjarvis-rebuild-jarvis-unified-gateway:latest                    "/app/gateway-entryp…"   7 days ago     Up 8 hours                      0.0.0.0:8093->8001/tcp, [::]:8093->8001/tcp                                                                    jarvis-unified-gateway
fb38ab64bcb6   msjarvis-wv-gateway-runtime:latest                                "python wv_gateway_s…"   7 days ago     Up 4 days                       0.0.0.0:8010->8010/tcp, [::]:8010->8010/tcp                                                                    jarvis-wv-entangled-gateway
7083466b0715   msjarvis-rebuild-llm22-proxy:timeoutfix-applied-20260802T115010   "python -m uvicorn l…"   7 days ago     Up 4 days                       127.0.0.1:8222->8222/tcp                                                                                       llm22-proxy
541c6a6710d4   11b02e88478a                                                      "sh -c 'cd /app/serv…"   10 days ago    Restarting (1) 14 seconds ago                                                                                                                  jarvis-ms-indexer
a17a80592680   11b02e88478a                                                      "sh -c 'cd /app/serv…"   10 days ago    Up 4 days                       127.0.0.1:8083->8083/tcp                                                                                       jarvis-ms-analytics
2874efd42da1   11b02e88478a                                                      "sh -c 'cd /app/serv…"   10 days ago    Up 4 days                       127.0.0.1:7300->7300/tcp                                                                                       jarvis-ms-coordinator
df896932f41d   msjarvis-rebuild-jarvis-mountainshares-commons-gateway            "python3 -m uvicorn …"   10 days ago    Up 4 days                                                                                                                                      jarvis-mountainshares-commons-gateway
e511a263b196   msjarvis-rebuild-jarvis-kyc-vault:patched-20260730-1931           "uvicorn app:app --h…"   10 days ago    Up 3 days                       127.0.0.1:8045->8045/tcp                                                                                       jarvis-kyc-vault
80e2aebfe309   msjarvis-rebuild-jarvis-chat-worker                               "python chat_worker.…"   11 days ago    Up 4 days                                                                                                                                      jarvis-chat-worker
95a4b99f6a76   msjarvis-rebuild-jarvis-20llm-production                          "python3 ai_server_2…"   11 days ago    Up 4 days                       127.0.0.1:8008->8008/tcp                                                                                       jarvis-20llm-production
08d54934c893   jarvis-epistemic-runner:closeout-20260729                         "python3 hilbert_rec…"   11 days ago    Up 4 days                       127.0.0.1:8057->8057/tcp                                                                                       jarvis-epistemic-runner
8bbb6068c565   11b02e88478a                                                      "uvicorn jarviscrypt…"   11 days ago    Up 4 days                       8099/tcp                                                                                                       jarvis-crypto-policy
a61d064d2901   nbb-i-containers:asbuilt-20260728-v3                              "sh -c 'ln -sfn /app…"   12 days ago    Up 4 days                       127.0.0.1:8015->8015/tcp                                                                                       jarvis-nbb-i-containers-2
d91ccf962dbf   jarvis-commons-optin-intake:closeout-20260728-v2                  "python3 -m uvicorn …"   12 days ago    Up 4 days                       127.0.0.1:8061->8061/tcp                                                                                       jarvis-commons-optin-intake
13d514ef3fda   nbb-darwin-godel-machines:asbuilt-20260728                        "python3 -c 'import …"   12 days ago    Up 4 days                       127.0.0.1:8302->8010/tcp                                                                                       nbb_darwin_godel_machines
4cb9f9ab2244   jarvis-belief-revision:asbuilt-20260728                           "uvicorn belief_revi…"   12 days ago    Up 4 days                       127.0.0.1:7240->7240/tcp                                                                                       jarvis-belief-revision
b91e71952587   jarvis-blood-brain-barrier:asbuilt-20260728                       "python3 ms_jarvis_b…"   12 days ago    Up 4 days                       127.0.0.1:8016->8016/tcp                                                                                       jarvis-blood-brain-barrier
e183780b8c54   jarvis-brain-orchestrator:asbuilt-20260728                        "python3 brain_orche…"   12 days ago    Up 4 days (healthy)             127.0.0.1:17260->7260/tcp                                                                                      jarvis-brain-orchestrator
f5b50ec52369   jarvis-lm-synthesizer:asbuilt-20260728                            "python /app/service…"   12 days ago    Up 4 days                       8001/tcp                                                                                                       jarvis-lm-synthesizer
ffa02fa63fd1   jarvis-fifth-dgm:asbuilt-20260728                                 "python3 ms_jarvis_f…"   12 days ago    Up 4 days                       127.0.0.1:4002->4002/tcp                                                                                       jarvis-fifth-dgm
5ed3e920ae8a   jarvis-woah:asbuilt-20260728                                      "python3.10 /app/ms_…"   12 days ago    Up 4 days                       127.0.0.1:7012->7012/tcp                                                                                       jarvis-woah
e59a183a8d4f   11b02e88478a                                                      "python3 /app/servic…"   12 days ago    Up 4 days                       127.0.0.1:8079->8079/tcp                                                                                       jarvis-stewardship-scheduler
7239e08ad162   11b02e88478a                                                      "python3 jarvis_stew…"   12 days ago    Up 4 days                       127.0.0.1:8014->8014/tcp                                                                                       jarvis-steward
50f4b052ab12   python:3.11-slim                                                  "sh -c 'pip install …"   12 days ago    Up 4 days                       127.0.0.1:8056->8056/tcp                                                                                       jarvis-spatial-sandbox
bb94fb696188   python:3.11-slim                                                  "sh -c 'pip install …"   12 days ago    Up 4 days                       8076/tcp                                                                                                       jarvis-pia-sampler
ab983b25ea7d   nginx:stable                                                      "/docker-entrypoint.…"   12 days ago    Up 4 days                       80/tcp, 127.0.0.1:11436->11436/tcp                                                                             jarvis-ollama-tls
9e8f38747f39   11b02e88478a                                                      "uvicorn jarvis_hilb…"   12 days ago    Up 4 days                       127.0.0.1:18094->8092/tcp                                                                                      jarvis-hilbert-time
4cc77f3590b0   11b02e88478a                                                      "uvicorn jarvis_hilb…"   12 days ago    Up 4 days                       127.0.0.1:18091->8081/tcp                                                                                      jarvis-hilbert-gateway
2146db5a358a   nginx:stable                                                      "/docker-entrypoint.…"   12 days ago    Up 4 days                       80/tcp, 127.0.0.1:8444->8444/tcp                                                                               jarvis-gis-rag-tls
fb9121998db7   nginx:stable                                                      "/docker-entrypoint.…"   12 days ago    Up 4 days                       80/tcp, 127.0.0.1:8443->8443/tcp                                                                               jarvis-chroma-tls
f8a77fee3e52   msjarvis-rebuild-jarvis-rag-server:latest                         "/bin/sh -c 'cd /app…"   12 days ago    Up 4 days                       127.0.0.1:8425->8425/tcp                                                                                       jarvis-autonomous-learner
76299ef2eaba   jarvis-civic-intake:closeout-20260728                             "uvicorn hilbert.civ…"   13 days ago    Up 4 days                       8100/tcp                                                                                                       jarvis-civic-intake
197939bc14b0   msjarvis-rebuild-jarvis-gis-rag                                   "uvicorn gis_rag_ser…"   2 weeks ago    Up 4 days                       127.0.0.1:8004->8004/tcp, 8044/tcp                                                                             jarvis-gis-rag
615c4b783c3e   msjarvis-rebuild-jarvis-judge-truth                               "python judge_truth_…"   2 weeks ago    Up 4 days                       127.0.0.1:8035->7230/tcp                                                                                       jarvis-judge-truth
b8fc26b8aa3e   msjarvis-rebuild-ms-allis-internal-sandbox                        "uvicorn ms_allis_in…"   2 weeks ago    Up 4 days                       127.0.0.1:8042->8042/tcp                                                                                       ms-allis-internal-sandbox
4f6a973dc700   msjarvis-rebuild-jarvis-memory                                    "uvicorn ms_jarvis_m…"   2 weeks ago    Up 4 days                       127.0.0.1:8156->8056/tcp                                                                                       jarvis-memory
8bb7e22ef46a   msjarvis/jarvis-auth-api:patched                                  "python -m uvicorn a…"   2 weeks ago    Up 4 days                       127.0.0.1:8096->8091/tcp                                                                                       jarvis-auth-api
082e7a2a1c41   msjarvis-rebuild-jarvis-dgm-03                                    "sh -c 'python3 -m u…"   2 weeks ago    Up 4 days                       5103/tcp                                                                                                       jarvis-dgm-03
b51ec7f91617   msjarvis-rebuild-jarvis-dgm-02                                    "sh -c 'python3 -m u…"   2 weeks ago    Up 4 days                       5102/tcp                                                                                                       jarvis-dgm-02
c150a17e1ef9   msjarvis-rebuild-jarvis-dgm-01                                    "sh -c 'python3 -m u…"   2 weeks ago    Up 4 days                       5101/tcp                                                                                                       jarvis-dgm-01
7a2030b63e13   msjarvis-rebuild-jarvis-dgm-04                                    "sh -c 'python3 -m u…"   2 weeks ago    Up 4 days                       5104/tcp                                                                                                       jarvis-dgm-04
176b05c21680   chromadb/chroma:0.6.3                                             "/docker_entrypoint.…"   2 weeks ago    Up 4 days (healthy)             127.0.0.1:8002->8000/tcp                                                                                       jarvis-chroma
d82b226b7f45   msjarvis-rebuild-jarvis-phi-probe                                 "python3 ms_jarvis_p…"   2 weeks ago    Up 4 days                       127.0.0.1:8026->8025/tcp                                                                                       jarvis-phi-probe
726ffeb76526   11b02e88478a                                                      "uvicorn jarvis_hilb…"   2 weeks ago    Up 4 days                       127.0.0.1:18092->8081/tcp                                                                                      jarvis-hilbert-state
dcfe4ac54fa3   msjarvis-rebuild-nbb_prefrontal_cortex                            "/start.sh"              3 weeks ago    Up 4 days                       127.0.0.1:8105->7005/tcp                                                                                       nbb_prefrontal_cortex
0f410deb2a1e   msjarvis-rebuild-jarvis-rag-server                                "python3 rag_server.…"   3 weeks ago    Up 4 days                       127.0.0.1:8003->8003/tcp                                                                                       jarvis-rag-server
12f4ee393f59   postgis/postgis:15-3.4                                            "docker-entrypoint.s…"   3 weeks ago    Up 4 days                       127.0.0.1:5435->5432/tcp                                                                                       hp-local-db
aa6da26825cb   ollama/ollama:latest                                              "/bin/ollama serve"      3 weeks ago    Up 4 days                       127.0.0.1:11434->11434/tcp                                                                                     jarvis-ollama
50d7ae0f4f43   msjarvis-rebuild-jarvis-i-containers                              "python -m uvicorn i…"   4 weeks ago    Up 4 days                       8015/tcp                                                                                                       jarvis-i-containers
55e2824e1e9b   msjarvis-rebuild-jarvis-neurobiological-master                    "python3 ms_jarvis_n…"   4 weeks ago    Up 4 days                       8018/tcp                                                                                                       jarvis-neurobiological-master
15b51087eaa7   11b02e88478a                                                      "uvicorn intake_serv…"   5 weeks ago    Up 4 days                       127.0.0.1:8007->8007/tcp                                                                                       jarvis-intake-service
74b317576285   neo4j:5.13-community                                              "tini -g -- /startup…"   5 weeks ago    Up 4 days                       7473/tcp, 127.0.0.1:7687->7687/tcp, 127.0.0.1:7475->7474/tcp                                                   neo4j
2620dac29ebb   msjarvis-rebuild-nbb_qualia_engine                                "uvicorn ms_jarvis_c…"   5 weeks ago    Up 4 days                       127.0.0.1:8303->8010/tcp                                                                                       nbb_qualia_engine
527a0fca691c   qualia-orchestrator:real                                          "python /app/service…"   5 weeks ago    Up 4 days (healthy)             127.0.0.1:9998->9998/tcp                                                                                       qualia-orchestrator-69dgm-real
406c478dedeb   jarvis-hp-sidecar:local                                           "python hp_sidecar.py"   5 weeks ago    Up 4 days                       127.0.0.1:8094->8094/tcp                                                                                       jarvis-hp-sidecar
55df4a081751   jarvis-session-sidecar:latest                                     "uvicorn app:app --h…"   5 weeks ago    Up 4 days                       127.0.0.1:8060->8060/tcp, 8070/tcp                                                                             56c99d59f7a5_jarvis-session-sidecar
f51ab5ec580e   redis:7-alpine                                                    "docker-entrypoint.s…"   5 weeks ago    Up 4 days (healthy)             127.0.0.1:6380->6379/tcp                                                                                       jarvis-redis
d68ba2f39218   msjarvis-rebuild-llm2-proxy                                       "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8202->8202/tcp                                                                                       e665651c00d5_llm2-proxy
3e9f9e5eacd5   msjarvis-rebuild-llm20-proxy                                      "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8220->8220/tcp                                                                                       2d6c035dc9fe_llm20-proxy
33cc8c54665f   msjarvis-rebuild-llm17-proxy                                      "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8217->8217/tcp                                                                                       b91b3c2adba5_llm17-proxy
bb5199581bf7   msjarvis-rebuild-llm19-proxy                                      "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8219->8219/tcp                                                                                       b5a2b182f1b7_llm19-proxy
b1cf6a9ce368   msjarvis-rebuild-llm9-proxy                                       "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8209->8209/tcp                                                                                       c68db82137f8_llm9-proxy
c0f034c275aa   msjarvis-rebuild-llm18-proxy                                      "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8218->8218/tcp                                                                                       05cbdb9d8b63_llm18-proxy
6ffa201bc5cb   msjarvis-rebuild-nbb_spiritual_root                               "python3 consciousne…"   5 weeks ago    Up 4 days                       127.0.0.1:8103->8010/tcp                                                                                       a8416407179c_nbb_spiritual_root
77a6d8da8cfd   msjarvis-rebuild-jarvis-mother-protocols                          "python -m uvicorn m…"   5 weeks ago    Up 4 days                       4000/tcp                                                                                                       1d653a8a0fcb_jarvis-mother-protocols
d74fd7b97159   msjarvis-rebuild-llm10-proxy                                      "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8210->8210/tcp                                                                                       07868f87c30f_llm10-proxy
2f4e05f8a3dc   msjarvis-rebuild-llm1-proxy                                       "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8201->8201/tcp                                                                                       f970d6243de9_llm1-proxy
466acb2b5bdc   msjarvis-rebuild-jarvis-temporal-consciousness                    "python -m uvicorn t…"   5 weeks ago    Up 4 days                       7007/tcp                                                                                                       1e1783a0cae3_jarvis-temporal-consciousness
45c222470dcf   msjarvis-rebuild-llm13-proxy                                      "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8213->8213/tcp                                                                                       bbd55aa39149_llm13-proxy
16ea04409c5f   msjarvis-rebuild-llm15-proxy                                      "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8215->8215/tcp                                                                                       cdb1cfcf3615_llm15-proxy
4b5ad0424420   msjarvis-rebuild-llm12-proxy                                      "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8212->8212/tcp                                                                                       03da3490dbba_llm12-proxy
7cf6540cb8d7   msjarvis-rebuild-llm6-proxy                                       "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8206->8206/tcp                                                                                       b9f25945034e_llm6-proxy
7af7d2f41930   msjarvis-rebuild-nbb_mother_carrie_protocols                      "python3 consciousne…"   5 weeks ago    Up 4 days                       127.0.0.1:8107->8010/tcp                                                                                       0f40caf56e1e_nbb_mother_carrie_protocols
c78837fed345   msjarvis-rebuild-llm4-proxy                                       "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8204->8204/tcp                                                                                       6c076127418c_llm4-proxy
ce480ed1f93b   msjarvis-rebuild-llm5-proxy                                       "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8205->8205/tcp                                                                                       6dd05bcbf535_llm5-proxy
b22197a3d613   msjarvis-rebuild-llm7-proxy                                       "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8207->8207/tcp                                                                                       f49af6a3d696_llm7-proxy
81dc8f91368e   msjarvis-rebuild-nbb_spiritual_maternal_integration               "python3 consciousne…"   5 weeks ago    Up 4 days                       127.0.0.1:8109->8010/tcp                                                                                       aae4a8928928_nbb_spiritual_maternal_integration
9732ba6ed169   msjarvis-rebuild-nbb_woah_algorithms                              "python3 consciousne…"   5 weeks ago    Up 4 days                       127.0.0.1:8104->8010/tcp                                                                                       a40eece620f3_nbb_woah_algorithms
0410a12c0f87   msjarvis-rebuild-llm21-proxy                                      "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8221->8221/tcp                                                                                       eeb98757a243_llm21-proxy
ba01a2bd26bf   msjarvis-rebuild-llm3-proxy                                       "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8203->8203/tcp                                                                                       8dffd2f7b142_llm3-proxy
0040918f6e83   msjarvis-rebuild-llm8-proxy                                       "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8208->8208/tcp                                                                                       22cb4468dbd5_llm8-proxy
ca9f3938f31c   msjarvis-rebuild-llm11-proxy                                      "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8211->8211/tcp                                                                                       675f8bd43968_llm11-proxy
502f270952e9   msjarvis-rebuild-llm14-proxy                                      "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8214->8214/tcp                                                                                       be5c6613bca3_llm14-proxy
d9715beb5c89   msjarvis-rebuild-llm16-proxy                                      "python -m uvicorn l…"   5 weeks ago    Up 4 days                       127.0.0.1:8216->8216/tcp                                                                                       69ee8c1dadfb_llm16-proxy
7b8bfefe633a   msjarvis-rebuild-nbb_pituitary_gland                              "/start.sh"              5 weeks ago    Up 4 days                       127.0.0.1:8108->80/tcp                                                                                         nbb_pituitary_gland
8b13bbdfc71d   msjarvis-rebuild-jarvis-constitutional-guardian                   "python -m uvicorn c…"   5 weeks ago    Up 4 days                       127.0.0.1:8091->8091/tcp                                                                                       jarvis-constitutional-guardian
934bfec75dfa   msjarvis-rebuild-jarvis-judge-pipeline                            "python judge_pipeli…"   5 weeks ago    Up 4 days                       7239/tcp                                                                                                       jarvis-judge-pipeline
c3b8c5c2fc27   msjarvis-rebuild-jarvis-semaphore                                 "python -m uvicorn m…"   5 weeks ago    Up 4 days                       127.0.0.1:8030->8030/tcp                                                                                       jarvis-semaphore
8a7b36c5a662   msjarvis-rebuild-jarvis-web-research                              "python ms_jarvis_we…"   5 weeks ago    Up 4 days                       8008/tcp                                                                                                       jarvis-web-research
3f68fcbda89c   msjarvis-rebuild-jarvis-judge-alignment                           "python judge_alignm…"   5 weeks ago    Up 4 days                       7232/tcp                                                                                                       jarvis-judge-alignment
2d538adc61b8   msjarvis-rebuild-jarvis-spiritual-rag                             "python spiritual_ra…"   5 weeks ago    Up 4 days                       127.0.0.1:8005->8005/tcp                                                                                       jarvis-spiritual-rag
e4d6dd1f05eb   msjarvis-rebuild-jarvis-eeg-theta                                 "uvicorn jarvis_eeg_…"   5 weeks ago    Up 4 days                       127.0.0.1:8074->8074/tcp                                                                                       jarvis-eeg-theta
4d5bbc5d4275   msjarvis-rebuild-jarvis-eeg-delta                                 "uvicorn jarvis_eeg_…"   5 weeks ago    Up 4 days                       127.0.0.1:8073->8073/tcp                                                                                       jarvis-eeg-delta
bf6b32fd56a6   msjarvis-rebuild-jarvis-swarm-intelligence                        "python3 ms_jarvis_s…"   5 weeks ago    Up 4 days                       8021/tcp                                                                                                       jarvis-swarm-intelligence
1150428c1b27   msjarvis-rebuild-jarvis-provenance                                "uvicorn app:app --h…"   5 weeks ago    Up 4 days                       127.0.0.1:8046->8046/tcp                                                                                       jarvis-provenance
2f88be593aa8   python:3.11-slim                                                  "python3 -c 'import …"   5 weeks ago    Up 11 hours                                                                                                                                    jarvis-ingest-api
91786e706452   msjarvis-rebuild-jarvis-eeg-beta                                  "uvicorn jarvis_eeg_…"   5 weeks ago    Up 4 days                       127.0.0.1:8075->8075/tcp                                                                                       jarvis-eeg-beta
24173709208f   msjarvis-rebuild-jarvis-rag-router                                "uvicorn rag_query_r…"   5 weeks ago    Up 4 days                       8003/tcp, 127.0.0.1:5015->5001/tcp                                                                             jarvis-rag-router
940dd621fb68   msjarvis-rebuild-jarvis-aaacpe-rag                                "python -m uvicorn a…"   5 weeks ago    Up 4 days                       127.0.0.1:8032->8032/tcp                                                                                       jarvis-aaacpe-rag
d13b32b9e454   msjarvis-rebuild-jarvis-judge-ethics                              "python judge_ethics…"   5 weeks ago    Up 4 days                       7233/tcp                                                                                                       jarvis-judge-ethics
3bb8f7e2af17   msjarvis-rebuild-jarvis-agents-service                            "python3 ms_jarvis_a…"   5 weeks ago    Up 4 days                       8005/tcp                                                                                                       jarvis-agents-service
0b482fedf39c   msjarvis-rebuild-jarvis-judge-consistency                         "python judge_consis…"   5 weeks ago    Up 4 days                       7231/tcp                                                                                                       jarvis-judge-consistency
bfd56587c08f   jaegertracing/all-in-one:1.52                                     "/go/bin/all-in-one-…"   5 weeks ago    Up 4 days                       4317-4318/tcp, 5775/udp, 5778/tcp, 9411/tcp, 14250/tcp, 14268/tcp, 6831-6832/udp, 127.0.0.1:16686->16686/tcp   jarvis-jaeger
f57029960345   msjarvis-toroidal:latest                                          "python -m uvicorn t…"   5 weeks ago    Up 4 days                       127.0.0.1:8025->8025/tcp                                                                                       jarvis-toroidal
55be93b371b2   msjarvis-rebuild-jarvis-psychology-services                       "python ms_jarvis_ps…"   5 weeks ago    Up 4 days                       127.0.0.1:8019->8019/tcp                                                                                       jarvis-psychology-services
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -l
Pager usage is off.
                                                              List of databases
          Name          |  Owner   | Encoding | Locale Provider |  Collate   |   Ctype    | ICU Locale | ICU Rules |    Access privileges     
------------------------+----------+----------+-----------------+------------+------------+------------+-----------+--------------------------
 msjarvis               | msjarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 msjarvisgis            | msjarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 msjarvisgis_v2         | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 msjarvisgis_v2_restore | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 postgres               | msjarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 template0              | msjarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/msjarvis             +
                        |          |          |                 |            |            |            |           | msjarvis=CTc/msjarvis
 template1              | msjarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/msjarvis             +
                        |          |          |                 |            |            |            |           | msjarvis=CTc/msjarvis
 template_postgis       | msjarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 wv_gis                 | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =Tc/postgres            +
                        |          |          |                 |            |            |            |           | postgres=CTc/postgres   +
                        |          |          |                 |            |            |            |           | policy_writer=c/postgres
(9 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -c "\dt public.*"
Pager usage is off.
                                         List of relations
 Schema |                              Name                               | Type  |     Owner      
--------+-----------------------------------------------------------------+-------+----------------
 public | gbim_active_collection                                          | table | msjarvis_admin
 public | gbim_active_collection_repoint_backup_20260721_203253           | table | postgres
 public | gbim_bg_coverage_area                                           | table | postgres
 public | gbim_bg_coverage_counts                                         | table | postgres
 public | gbim_bg_coverage_length                                         | table | postgres
 public | gbim_bg_coverage_progress                                       | table | postgres
 public | gbim_bg_layer_role                                              | table | postgres
 public | gbim_blockgroup_coverage_bridge                                 | table | postgres
 public | gbim_blockgroup_features                                        | table | postgres
 public | gbim_blockgroup_recreation_flags                                | table | postgres
 public | gbim_blockgroup_semantic_payload                                | table | postgres
 public | gbim_blockgroup_text_fragments                                  | table | postgres
 public | gbim_blockgroup_vector                                          | table | postgres
 public | gbim_chroma_collection_feature_registry                         | table | postgres
 public | gbim_chroma_collection_registry                                 | table | postgres
 public | gbim_chroma_publication_manifest                                | table | postgres
 public | gbim_chroma_publication_manifest_repoint_backup_20260721_203253 | table | postgres
 public | gbim_collection_manifest                                        | table | msjarvis_admin
 public | gbim_collection_manifest_repoint_backup_20260721_203253         | table | postgres
 public | gbim_dataset_map                                                | table | postgres
 public | gbim_layer_projection                                           | table | postgres
 public | gbim_layer_registry                                             | table | postgres
 public | gbim_registry                                                   | table | postgres
 public | gbim_vertical_slice_acceptance_tests                            | table | postgres
 public | spatial_ref_sys                                                 | table | postgres
 public | wv_atm_weather_stations                                         | table | postgres
 public | wv_bio_biodiversity_rank                                        | table | msjarvis
 public | wv_bio_ecoregions                                               | table | postgres
 public | wv_bio_red_spruce_cover                                         | table | postgres
 public | wv_blockgroup_belief_snapshot                                   | table | postgres
 public | wv_blockgroup_dataset_coverage                                  | table | postgres
 public | wv_blockgroup_dataset_coverage_stage                            | table | postgres
 public | wv_blockgroup_identity                                          | table | postgres
 public | wv_blockgroup_identity_stage                                    | table | postgres
 public | wv_blockgroup_representation                                    | table | postgres
 public | wv_blockgroup_representation_stage                              | table | postgres
 public | wv_blockgroup_semantic_text                                     | table | postgres
 public | wv_bnd_appalachian_basin_boundary                               | table | postgres
 public | wv_bnd_arc_counties                                             | table | postgres
 public | wv_bnd_canaan_valley_nwr                                        | table | postgres
 public | wv_bnd_census_designated_places                                 | table | postgres
 public | wv_bnd_county_24k                                               | table | postgres
 public | wv_bnd_county_municipal_dlg                                     | table | postgres
 public | wv_bnd_mnf_basic_ownership                                      | table | postgres
 public | wv_bnd_mnf_management_prescriptions                             | table | postgres
 public | wv_bnd_mnf_ranger_districts                                     | table | postgres
 public | wv_bnd_mnf_recreation_campgrounds                               | table | postgres
 public | wv_bnd_mnf_recreation_sites                                     | table | postgres
 public | wv_bnd_mnf_wilderness                                           | table | postgres
 public | wv_bnd_morgantown_wards                                         | table | postgres
 public | wv_bnd_nhd_mussel_streams                                       | table | postgres
 public | wv_bnd_public_lands_county_city_parks                           | table | postgres
 public | wv_bnd_public_lands_national_forest                             | table | postgres
 public | wv_bnd_public_lands_national_park                               | table | postgres
 public | wv_bnd_public_lands_nwr                                         | table | postgres
 public | wv_bnd_public_lands_state_forests                               | table | postgres
 public | wv_bnd_public_lands_state_parks                                 | table | postgres
 public | wv_bnd_public_lands_wildlife_resources                          | table | postgres
 public | wv_bnd_state_boundary_100k                                      | table | postgres
 public | wv_bnd_voting_districts_2000                                    | table | postgres
 public | wv_bnd_voting_districts_2002                                    | table | postgres
 public | wv_bnd_workforce_investment_areas                               | table | postgres
 public | wv_censustracts_census_2020_utm83                               | table | postgres
 public | wv_county_belief_snapshot                                       | table | postgres
 public | wv_county_boundaries_24k_topo_updated_2026_utm83_gdb            | table | postgres
 public | wv_county_boundaries_24k_topo_updated_2026_wma84_gdb            | table | postgres
 public | wv_county_dataset_coverage                                      | table | postgres
 public | wv_county_identity                                              | table | postgres
 public | wv_county_representation                                        | table | postgres
 public | wv_county_representation_pre_gid_rebind                         | table | postgres
 public | wv_derived_governance_tables                                    | table | postgres
 public | wv_eco_abandoned_mine_lands_line                                | table | postgres
 public | wv_eco_abandoned_mine_lands_point                               | table | postgres
 public | wv_eco_abandoned_mine_lands_polygon                             | table | postgres
 public | wv_eco_coal_fields                                              | table | postgres
 public | wv_eco_ezec_communities                                         | table | postgres
 public | wv_eco_industrial_sites                                         | table | postgres
 public | wv_eco_manufacturing_directory                                  | table | postgres
 public | wv_eco_mineral_operations                                       | table | postgres
 public | wv_eco_mountaintop_removal                                      | table | postgres
 public | wv_elv_summit_names                                             | table | postgres
 public | wv_entity_registry                                              | table | postgres
 public | wv_env_air_nonattainment                                        | table | postgres
 public | wv_env_epa_facilities                                           | table | msjarvis
 public | wv_env_timber_removal_volume                                    | table | postgres
 public | wv_env_wildfire_regions                                         | table | postgres
 public | wv_env_wind_energy_resources                                    | table | postgres
 public | wv_geo_coal_beds                                                | table | postgres
 public | wv_geo_geological_map_generalized                               | table | postgres
 public | wv_geo_karst                                                    | table | postgres
 public | wv_hazus_floodplain_100year                                     | table | postgres
 public | wv_hazus_floodplain_10year                                      | table | postgres
 public | wv_hazus_floodplain_25year                                      | table | postgres
 public | wv_hazus_floodplain_50year                                      | table | postgres
 public | wv_hlt_health_providers                                         | table | postgres
 public | wv_hlt_public_health_departments                                | table | postgres
 public | wv_hlt_rural_health_facilities                                  | table | postgres
 public | wv_hyd_dams_dmr                                                 | table | postgres
 public | wv_hyd_dams_nid                                                 | table | postgres
 public | wv_hyd_dams_noncoal                                             | table | postgres
 public | wv_hyd_hazus_floodplain_zones                                   | table | msjarvis
 public | wv_hyd_high_water_marks                                         | table | postgres
 public | wv_hyd_navigable_waterways                                      | table | postgres
 public | wv_hyd_navigable_waterways_river_miles                          | table | postgres
 public | wv_hyd_navigable_waterways_structures                           | table | postgres
 public | wv_hyd_springs_100gpm                                           | table | postgres
 public | wv_hyd_streamflow_stations                                      | table | postgres
 public | wv_hyd_streams_high_quality                                     | table | msjarvis
 public | wv_hyd_streams_national_atlas                                   | table | postgres
 public | wv_hyd_streams_tiger                                            | table | postgres
 public | wv_hyd_watershed_boundary_11digit                               | table | postgres
 public | wv_hyd_watershed_boundary_12digit_hu                            | table | postgres
 public | wv_hyd_watershed_boundary_8_10_12                               | table | postgres
 public | wv_layer_categories                                             | table | postgres
 public | wv_loc_census_urbanized_areas                                   | table | postgres
 public | wv_loc_county_seats                                             | table | postgres
 public | wv_loc_geodetic_control_points                                  | table | postgres
 public | wv_loc_populated_places_census                                  | table | postgres
 public | wv_loc_sams2_address_road_centerlines                           | table | postgres
 public | wv_mil_army_reserve_facilities                                  | table | postgres
 public | wv_mil_national_guard_armories                                  | table | postgres
 public | wv_plc_hazus_level1                                             | table | postgres
 public | wv_plc_regional_planning_councils                               | table | postgres
 public | wv_plc_tax_district_boundaries                                  | table | postgres
 public | wv_plc_tax_parcels_surface_mineral                              | table | postgres
 public | wv_rec_fishing_boating_access                                   | table | postgres
 public | wv_rec_fishing_lakes                                            | table | postgres
 public | wv_rec_national_forest                                          | table | postgres
 public | wv_rec_nps_units                                                | table | postgres
 public | wv_rec_nwr_units                                                | table | postgres
 public | wv_rec_state_forests                                            | table | postgres
 public | wv_rec_state_parks                                              | table | postgres
 public | wv_rec_trail_points                                             | table | postgres
 public | wv_rec_trails                                                   | table | postgres
 public | wv_rec_whitewater_trails                                        | table | postgres
 public | wv_rec_wvdnr_managed_lands                                      | table | postgres
 public | wv_soc_911_centers                                              | table | postgres
 public | wv_soc_census_blockgroups_2020                                  | table | postgres
 public | wv_soc_census_blockgroups_2020_utm17                            | table | postgres
 public | wv_soc_census_tracts_2020                                       | table | postgres
 public | wv_soc_cities_pop10k                                            | table | postgres
 public | wv_soc_cities_pop2500                                           | table | postgres
 public | wv_soc_communities_pop_change                                   | table | postgres
 public | wv_soc_courthouses_county                                       | table | postgres
 public | wv_soc_courthouses_federal                                      | table | postgres
 public | wv_soc_fish_hatcheries                                          | table | postgres
 public | wv_soc_fishing_boating_access                                   | table | postgres
 public | wv_soc_fishing_lakes                                            | table | postgres
 public | wv_soc_higher_ed_facilities                                     | table | postgres
 public | wv_soc_hospitals_wvdem                                          | table | msjarvis
 public | wv_soc_libraries                                                | table | postgres
 public | wv_soc_national_register_historic_points                        | table | postgres
 public | wv_soc_national_register_historic_polygons                      | table | postgres
 public | wv_soc_nursing_homes                                            | table | postgres
 public | wv_soc_places_of_worship_wvgistc                                | table | postgres
 public | wv_soc_population_by_decade                                     | table | postgres
 public | wv_soc_schools_k12                                              | table | msjarvis
 public | wv_soc_towers_am                                                | table | postgres
 public | wv_soc_towers_asr                                               | table | postgres
 public | wv_soc_towers_cellular                                          | table | postgres
 public | wv_soc_towers_fm                                                | table | postgres
 public | wv_soc_towers_microwave                                         | table | postgres
 public | wv_soc_towers_pager                                             | table | postgres
 public | wv_soc_towers_private                                           | table | postgres
 public | wv_soc_towers_tv                                                | table | postgres
 public | wv_soc_va_facilities                                            | table | postgres
 public | wv_soc_zcta_2020                                                | table | postgres
 public | wv_source_files_manifest                                        | table | postgres
 public | wv_source_manifest_layers                                       | table | postgres
 public | wv_str_bridges                                                  | table | postgres
 public | wv_str_correctional_institutions                                | table | postgres
 public | wv_str_flood_atrisk_structures                                  | table | postgres
 public | wv_str_parole_offices                                           | table | postgres
 public | wv_str_places_of_worship_hsip                                   | table | postgres
 public | wv_str_samb_building_points                                     | table | postgres
 public | wv_str_samb_building_polygons                                   | table | postgres
 public | wv_tax_districts_2023                                           | table | postgres
 public | wv_tax_master_surf_2025                                         | table | postgres
 public | wv_tax_parcel_summary_2025                                      | table | postgres
 public | wv_tract_belief_snapshot                                        | table | postgres
 public | wv_tract_dataset_coverage                                       | table | postgres
 public | wv_tract_identity                                               | table | postgres
 public | wv_tract_representation                                         | table | postgres
 public | wv_tract_representation_pre_gid_rebind                          | table | postgres
 public | wv_trn_airport_facilities                                       | table | postgres
 public | wv_trn_airport_proposed                                         | table | postgres
 public | wv_trn_airport_runways                                          | table | postgres
 public | wv_trn_airports                                                 | table | msjarvis
 public | wv_trn_intermodal_terminals                                     | table | postgres
 public | wv_trn_mnf_recreation_trails                                    | table | postgres
 public | wv_trn_mnf_roads                                                | table | postgres
 public | wv_trn_railroad_lines_rti                                       | table | postgres
 public | wv_trn_railroads_amtrak                                         | table | postgres
 public | wv_trn_railroads_excursion                                      | table | postgres
 public | wv_trn_railroads_national_network                               | table | postgres
 public | wv_trn_recreational_trails                                      | table | postgres
 public | wv_trn_roads_interstate                                         | table | postgres
 public | wv_trn_roads_major_4800                                         | table | postgres
 public | wv_trn_roads_state_routes                                       | table | postgres
 public | wv_trn_roads_us_highways                                        | table | postgres
 public | wv_trn_roads_us_routes                                          | table | postgres
 public | wv_trn_whitewater_trails                                        | table | postgres
 public | wv_util_sewer_treatment_plants                                  | table | msjarvis
 public | wv_util_solid_waste_facilities                                  | table | postgres
 public | wv_wv_county_boundaries_24k_topo_updated_2026_utm83             | table | postgres
 public | wv_wv_county_boundaries_24k_topo_updated_2026_wma84             | table | postgres
(206 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -c "SELECT count(*) FROM public.gbim_record;"
Pager usage is off.
ERROR:  relation "public.gbim_record" does not exist
LINE 1: SELECT count(*) FROM public.gbim_record;
                             ^
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -c "SELECT count(*) FROM public.public_admissible_gbim_mv;"
Pager usage is off.
ERROR:  relation "public.public_admissible_gbim_mv" does not exist
LINE 1: SELECT count(*) FROM public.public_admissible_gbim_mv;
                             ^
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -c "\d public.gbim_record"
Pager usage is off.
Did not find any relation named "public.gbim_record".
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ curl -s http://localhost:11434/api/tags | python3 -m json.tool
{
    "models": [
        {
            "name": "sqlcoder:latest",
            "model": "sqlcoder:latest",
            "modified_at": "2026-06-28T03:10:12.35828956Z",
            "size": 4108916695,
            "digest": "77ac143483877b043ed3da36ce3e00a8f707645a2f1b769e9827313e5f8f0015",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": null,
                "parameter_size": "7B",
                "quantization_level": "Q4_0",
                "context_length": 32768,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "llama3.1-split:latest",
            "model": "llama3.1-split:latest",
            "modified_at": "2026-06-26T13:02:21.795226071Z",
            "size": 4920753355,
            "digest": "038b00d9a93d2fe6595667897778e6784ca41319888f1e7eafc0ba3dab7069d5",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "8.0B",
                "quantization_level": "Q4_K_M",
                "context_length": 131072,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion",
                "tools"
            ]
        },
        {
            "name": "nomic-embed-text:latest",
            "model": "nomic-embed-text:latest",
            "modified_at": "2026-06-11T20:47:35.500682464Z",
            "size": 274302450,
            "digest": "0a109f422b47e3a30ba2b10eca18548e944e8a23073ee3f3e947efcf3c45e59f",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "nomic-bert",
                "families": [
                    "nomic-bert"
                ],
                "parameter_size": "137M",
                "quantization_level": "F16",
                "context_length": 2048,
                "embedding_length": 768
            },
            "capabilities": [
                "embedding"
            ]
        },
        {
            "name": "mistral-split:latest",
            "model": "mistral-split:latest",
            "modified_at": "2026-05-19T17:12:40.729202136Z",
            "size": 4369376529,
            "digest": "d0f11764aa2c1d6dcdc471915df49571857e9fb3f2637c6b190d036fb30e4124",
            "details": {
                "parent_model": "/root/.ollama/models/blobs/sha256-faf975975644f275f00075e7cf79cd207642412560640cd1930afbab95fea25c",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "7.2B",
                "quantization_level": "Q4_K_M",
                "context_length": 32768,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "phi:latest",
            "model": "phi:latest",
            "modified_at": "2026-05-19T16:00:56.00107779Z",
            "size": 1602463378,
            "digest": "e2fd6321a5fe6bb3ac8a4e6f1cf04477fd2dea2924cf53237a995387e152ee9c",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "phi2",
                "families": [
                    "phi2"
                ],
                "parameter_size": "3B",
                "quantization_level": "Q4_0",
                "context_length": 2048,
                "embedding_length": 2560
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "bakllava:latest",
            "model": "bakllava:latest",
            "modified_at": "2026-05-19T02:30:38.101941956Z",
            "size": 4733351307,
            "digest": "3dd68bd4447cba20e20deba918749e7f58ff689a8ba4a90c9ff9dc9118037486",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama",
                    "clip"
                ],
                "parameter_size": "7B",
                "quantization_level": "Q4_0",
                "context_length": 32768,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion",
                "vision"
            ]
        },
        {
            "name": "llama3.1:8b-instruct-q4_K_M",
            "model": "llama3.1:8b-instruct-q4_K_M",
            "modified_at": "2026-05-19T02:07:15.249302259Z",
            "size": 4920753328,
            "digest": "46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "8.0B",
                "quantization_level": "Q4_K_M",
                "context_length": 131072,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion",
                "tools"
            ]
        },
        {
            "name": "gemma:2b",
            "model": "gemma:2b",
            "modified_at": "2026-05-19T02:06:18.64951558Z",
            "size": 1678456656,
            "digest": "b50d6c999e592ae4f79acae23b4feaefbdfceaa7cd366df2610e3072c052a160",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "gemma",
                "families": [
                    "gemma"
                ],
                "parameter_size": "3B",
                "quantization_level": "Q4_0",
                "context_length": 8192,
                "embedding_length": 2048
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "llama3.1:8b",
            "model": "llama3.1:8b",
            "modified_at": "2026-05-19T01:58:40.279566393Z",
            "size": 4920753328,
            "digest": "46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "8.0B",
                "quantization_level": "Q4_K_M",
                "context_length": 131072,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion",
                "tools"
            ]
        },
        {
            "name": "mxbai-embed-large:latest",
            "model": "mxbai-embed-large:latest",
            "modified_at": "2026-05-15T23:35:16.398705175Z",
            "size": 669615493,
            "digest": "468836162de7f81e041c43663fedbbba921dcea9b9fefea135685a39b2d83dd8",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "bert",
                "families": [
                    "bert"
                ],
                "parameter_size": "334M",
                "quantization_level": "F16",
                "context_length": 512,
                "embedding_length": 1024
            },
            "capabilities": [
                "embedding"
            ]
        },
        {
            "name": "mistral:7b-instruct-q4_K_M",
            "model": "mistral:7b-instruct-q4_K_M",
            "modified_at": "2026-05-11T04:28:17.78650797Z",
            "size": 4369387754,
            "digest": "1a85656b534f84f8ab5b235aa0e24a954769539b0f47a4bd11f5272cba43c892",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "7B",
                "quantization_level": "Q4_K_M",
                "context_length": 32768,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "phi3.5:latest",
            "model": "phi3.5:latest",
            "modified_at": "2026-04-12T20:35:47.354166236Z",
            "size": 2176178843,
            "digest": "61819fb370a3c1a9be6694869331e5f85f867a079e9271d66cb223acb81d04ba",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "phi3",
                "families": [
                    "phi3"
                ],
                "parameter_size": "3.8B",
                "quantization_level": "Q4_0",
                "context_length": 131072,
                "embedding_length": 3072
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "orca-mini:3b",
            "model": "orca-mini:3b",
            "modified_at": "2026-04-12T20:17:38.332112401Z",
            "size": 1979947443,
            "digest": "2dbd9f439647093cf773c325b0b3081a11f1b1426d61dee8b946f8f6555a1755",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": null,
                "parameter_size": "3B",
                "quantization_level": "Q4_0",
                "context_length": 2048,
                "embedding_length": 3200
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "orca-mini:latest",
            "model": "orca-mini:latest",
            "modified_at": "2026-04-12T20:16:04.090263215Z",
            "size": 1979947443,
            "digest": "2dbd9f439647093cf773c325b0b3081a11f1b1426d61dee8b946f8f6555a1755",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": null,
                "parameter_size": "3B",
                "quantization_level": "Q4_0",
                "context_length": 2048,
                "embedding_length": 3200
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "all-minilm:latest",
            "model": "all-minilm:latest",
            "modified_at": "2026-04-12T03:10:02.270756106Z",
            "size": 45960996,
            "digest": "1b226e2802dbb772b5fc32a58f103ca1804ef7501331012de126ab22f67475ef",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "bert",
                "families": [
                    "bert"
                ],
                "parameter_size": "23M",
                "quantization_level": "F16",
                "context_length": 512,
                "embedding_length": 384
            },
            "capabilities": [
                "embedding"
            ]
        },
        {
            "name": "starcoder2:latest",
            "model": "starcoder2:latest",
            "modified_at": "2026-02-03T04:14:06.721592206Z",
            "size": 1709901728,
            "digest": "9f4ae0aff61ee24fe4b7d9714c9382b5172551fa8e95aa064452ec2e62610835",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "starcoder2",
                "families": [
                    "starcoder2"
                ],
                "parameter_size": "3B",
                "quantization_level": "Q4_0",
                "context_length": 16384,
                "embedding_length": 3072
            },
            "capabilities": [
                "completion",
                "insert"
            ]
        },
        {
            "name": "medllama2:latest",
            "model": "medllama2:latest",
            "modified_at": "2026-02-03T04:08:58.668380862Z",
            "size": 3825807497,
            "digest": "a53737ec0c72e31e16968f232cad6a13d79b979d7c0cb13404dcd4405214c8f2",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": null,
                "parameter_size": "7B",
                "quantization_level": "Q4_0",
                "context_length": 4096,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "dolphin-phi:latest",
            "model": "dolphin-phi:latest",
            "modified_at": "2026-02-03T03:52:52.031862946Z",
            "size": 1602473850,
            "digest": "c5761fc772409945787240af89a5cce01dd39dc52f1b7b80d080a1163e8dbe10",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "phi2",
                "families": [
                    "phi2"
                ],
                "parameter_size": "3B",
                "quantization_level": "Q4_0",
                "context_length": 2048,
                "embedding_length": 2560
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "llama2:latest",
            "model": "llama2:latest",
            "modified_at": "2026-02-03T02:49:20.676271273Z",
            "size": 3826793677,
            "digest": "78e26419b4469263f75331927a00a0284ef6544c1975b826b15abdaef17bb962",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "7B",
                "quantization_level": "Q4_0",
                "context_length": 4096,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "deepseek-coder:latest",
            "model": "deepseek-coder:latest",
            "modified_at": "2026-02-03T02:40:12.60584115Z",
            "size": 776080839,
            "digest": "3ddd2d3fc8d2b5fe039d18f859271132fd9c7960ef0be1864984442dc2a915d3",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "1B",
                "quantization_level": "Q4_0",
                "context_length": 16384,
                "embedding_length": 2048
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "codellama:latest",
            "model": "codellama:latest",
            "modified_at": "2026-02-03T02:38:13.923973354Z",
            "size": 3825910662,
            "digest": "8fdf8f752f6e80de33e82f381aba784c025982752cd1ae9377add66449d2225f",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": null,
                "parameter_size": "7B",
                "quantization_level": "Q4_0",
                "context_length": 16384,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "qwen2:latest",
            "model": "qwen2:latest",
            "modified_at": "2026-02-03T02:27:01.016809737Z",
            "size": 4431401491,
            "digest": "dd314f039b9d54d5553002c906ce50c9fe7242f73f0680abd04f01c8ecbd2755",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "qwen2",
                "families": [
                    "qwen2"
                ],
                "parameter_size": "7.6B",
                "quantization_level": "Q4_0",
                "context_length": 32768,
                "embedding_length": 3584
            },
            "capabilities": [
                "completion",
                "tools"
            ]
        },
        {
            "name": "llama3.1:latest",
            "model": "llama3.1:latest",
            "modified_at": "2026-02-03T02:27:00.360787079Z",
            "size": 4920753328,
            "digest": "46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "8.0B",
                "quantization_level": "Q4_K_M",
                "context_length": 131072,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion",
                "tools"
            ]
        },
        {
            "name": "mistral:latest",
            "model": "mistral:latest",
            "modified_at": "2026-02-03T02:14:36.779364334Z",
            "size": 4372824384,
            "digest": "6577803aa9a036369e481d648a2baebb381ebc6e897f2bb9a766a2aa7bfbc1cf",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "7.2B",
                "quantization_level": "Q4_K_M",
                "context_length": 32768,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion",
                "tools"
            ]
        },
        {
            "name": "starling-lm:latest",
            "model": "starling-lm:latest",
            "modified_at": "2026-01-22T15:06:56.13615103Z",
            "size": 4108940286,
            "digest": "39153f619be614bf1b8b91cf31afe53ec107d70b6b7bb4118aa52bccc107ca7e",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "7B",
                "quantization_level": "Q4_0",
                "context_length": 8192,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "openchat:latest",
            "model": "openchat:latest",
            "modified_at": "2026-01-22T14:56:57.425457222Z",
            "size": 4109876386,
            "digest": "537a4e03b649d93bf57381199a85f412bfc35912e46db197407740230968e71f",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "7B",
                "quantization_level": "Q4_0",
                "context_length": 8192,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "neural-chat:latest",
            "model": "neural-chat:latest",
            "modified_at": "2026-01-22T14:50:33.742259474Z",
            "size": 4109853239,
            "digest": "89fa737d3b85d5e037c2b699b2a735a365cf9e57fd01c62b3378ec1e95694694",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "7B",
                "quantization_level": "Q4_0",
                "context_length": 32768,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "zephyr:latest",
            "model": "zephyr:latest",
            "modified_at": "2026-01-22T14:43:59.351422262Z",
            "size": 4109854934,
            "digest": "bbe38b81adec6be8ff951d148864ed15a368aa2e8534a5092d444f184a56e354",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "7B",
                "quantization_level": "Q4_0",
                "context_length": 32768,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "vicuna:latest",
            "model": "vicuna:latest",
            "modified_at": "2026-01-22T14:28:31.831177247Z",
            "size": 3825807726,
            "digest": "370739dc897bba0188d390bb7659e48d926cacc320875136d0115228023b1590",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": null,
                "parameter_size": "7B",
                "quantization_level": "Q4_0",
                "context_length": 4096,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "qwen2:7b",
            "model": "qwen2:7b",
            "modified_at": "2026-01-22T13:57:15.682886171Z",
            "size": 4431401491,
            "digest": "dd314f039b9d54d5553002c906ce50c9fe7242f73f0680abd04f01c8ecbd2755",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "qwen2",
                "families": [
                    "qwen2"
                ],
                "parameter_size": "7.6B",
                "quantization_level": "Q4_0",
                "context_length": 32768,
                "embedding_length": 3584
            },
            "capabilities": [
                "completion",
                "tools"
            ]
        },
        {
            "name": "tinyllama:latest",
            "model": "tinyllama:latest",
            "modified_at": "2026-01-22T13:35:10.37070479Z",
            "size": 637700138,
            "digest": "2644915ede352ea7bdfaff0bfac0be74c719d5d5202acb63a6fb095b52f394a4",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "1B",
                "quantization_level": "Q4_0",
                "context_length": 2048,
                "embedding_length": 2048
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "phi3:mini",
            "model": "phi3:mini",
            "modified_at": "2026-01-22T13:32:33.451580236Z",
            "size": 2176178913,
            "digest": "4f222292793889a9a40a020799cfd28d53f3e01af25d48e06c5e708610fc47e9",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "phi3",
                "families": [
                    "phi3"
                ],
                "parameter_size": "3.8B",
                "quantization_level": "Q4_0",
                "context_length": 131072,
                "embedding_length": 3072
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "minicpm-v:latest",
            "model": "minicpm-v:latest",
            "modified_at": "2026-01-22T13:04:09.160951814Z",
            "size": 5473838466,
            "digest": "c92bfad0120556eda311984f1ac2f0d0a589b8d68c4053c13486b526276aa205",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "qwen2",
                "families": [
                    "qwen2",
                    "clip"
                ],
                "parameter_size": "7.6B",
                "quantization_level": "Q4_0",
                "context_length": 32768,
                "embedding_length": 3584
            },
            "capabilities": [
                "completion",
                "vision"
            ]
        },
        {
            "name": "llama3:latest",
            "model": "llama3:latest",
            "modified_at": "2026-01-22T03:28:01.402621937Z",
            "size": 4661224676,
            "digest": "365c0bd3c000a25d28ddbf732fe1c6add414de7275464c4e4d1c3b5fcb5d8ad1",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama"
                ],
                "parameter_size": "8.0B",
                "quantization_level": "Q4_0",
                "context_length": 8192,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "llava:latest",
            "model": "llava:latest",
            "modified_at": "2026-01-22T03:27:39.796602943Z",
            "size": 4733363377,
            "digest": "8dd30f6b0cb19f555f2c7a7ebda861449ea2cc76bf1f44e262931f45fc81d081",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "llama",
                "families": [
                    "llama",
                    "clip"
                ],
                "parameter_size": "7B",
                "quantization_level": "Q4_0",
                "context_length": 32768,
                "embedding_length": 4096
            },
            "capabilities": [
                "completion",
                "vision"
            ]
        },
        {
            "name": "stablelm-zephyr:latest",
            "model": "stablelm-zephyr:latest",
            "modified_at": "2026-01-22T03:25:13.525712124Z",
            "size": 1608579394,
            "digest": "0a108dbd846e2b0ee264a71a28e50ac18e7f1601eeb2d677217602d32644bf24",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "stablelm",
                "families": [
                    "stablelm"
                ],
                "parameter_size": "3B",
                "quantization_level": "Q4_0",
                "context_length": 4096,
                "embedding_length": 2560
            },
            "capabilities": [
                "completion"
            ]
        },
        {
            "name": "qwen2.5:1.5b",
            "model": "qwen2.5:1.5b",
            "modified_at": "2026-01-22T03:00:19.182334501Z",
            "size": 986061892,
            "digest": "65ec06548149b04c096a120e4a6da9d4017ea809c91734ea5631e89f96ddc57b",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "qwen2",
                "families": [
                    "qwen2"
                ],
                "parameter_size": "1.5B",
                "quantization_level": "Q4_K_M",
                "context_length": 32768,
                "embedding_length": 1536
            },
            "capabilities": [
                "completion",
                "tools"
            ]
        }
    ]
}
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -c "SELECT 'semantic_payload' AS t, count(*) FROM public.wv_blockgroup_semantic_payload UNION ALL SELECT 'semantic_text', count(*) FROM public.wv_blockgroup_semantic_text UNION ALL SELECT 'representation', count(*) FROM public.wv_blockgroup_representation UNION ALL SELECT 'identity', count(*) FROM public.wv_blockgroup_identity UNION ALL SELECT 'dataset_coverage', count(*) FROM public.wv_blockgroup_dataset_coverage UNION ALL SELECT 'belief_snapshot', count(*) FROM public.wv_blockgroup_belief_snapshot;"
Pager usage is off.
ERROR:  relation "public.wv_blockgroup_semantic_payload" does not exist
LINE 1: SELECT 'semantic_payload' AS t, count(*) FROM public.wv_bloc...
                                                      ^
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -c "\d public.wv_blockgroup_semantic_payload"
Pager usage is off.
Did not find any relation named "public.wv_blockgroup_semantic_payload".
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -c "\d public.wv_blockgroup_representation"
Pager usage is off.
                    Table "public.wv_blockgroup_representation"
      Column       |             Type             | Collation | Nullable | Default 
-------------------+------------------------------+-----------+----------+---------
 blockgroup_geoid  | text                         |           | not null | 
 source_table      | text                         |           | not null | 
 source_feature_id | bigint                       |           | not null | 
 geom              | geometry(MultiPolygon,26917) |           |          | 
 geom_hash         | text                         |           | not null | 
 srid              | integer                      |           | not null | 
 created_at        | timestamp with time zone     |           |          | now()
Indexes:
    "wv_blockgroup_representation_pkey" PRIMARY KEY, btree (blockgroup_geoid)
    "gix_wv_blockgroup_representation_geom" gist (geom)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d msjarvisgis -c "\dt public.gbim_record" 2>&1 | tail -2
Pager usage is off.
Did not find any relation named "public.gbim_record".
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ for db in msjarvisgis_v2 msjarvisgis msjarvisgis_v2_restore msjarvis; do echo "=== $db ==="; PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d "$db" -Atc "SELECT table_schema||'.'||table_name FROM information_schema.tables WHERE table_name ~ 'record|payload|semantic|gbim_r|admissible|entity' ORDER BY 1;" 2>/dev/null; done
=== msjarvisgis_v2 ===
Pager usage is off.
public.gbim_blockgroup_coverage_semantic
public.gbim_blockgroup_semantic_payload
public.gbim_registry
public.wv_blockgroup_identity
public.wv_blockgroup_identity_stage
public.wv_blockgroup_semantic_text
public.wv_county_identity
public.wv_entity_registry
public.wv_tract_identity
=== msjarvisgis ===
Pager usage is off.
=== msjarvisgis_v2_restore ===
Pager usage is off.
public.gbim_blockgroup_coverage_semantic
public.gbim_blockgroup_semantic_payload
public.gbim_registry
public.wv_blockgroup_identity
public.wv_blockgroup_identity_stage
public.wv_blockgroup_semantic_text
public.wv_county_identity
public.wv_entity_registry
public.wv_tract_identity
=== msjarvis ===
Pager usage is off.
public.identity_binding
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "SELECT schemaname||'.'||relname, n_live_tup FROM pg_stat_user_tables ORDER BY n_live_tup DESC LIMIT 20;"
Pager usage is off.
public.wv_tax_master_surf_2025|1389855
public.wv_plc_tax_parcels_surface_mineral|1389531
staging_tax_2025.mastersurfwv_2025|1384853
public.wv_str_samb_building_points|1368299
public.wv_loc_sams2_address_road_centerlines|1135840
public.wv_env_wind_energy_resources|104812
public.wv_str_flood_atrisk_structures|81054
public.wv_plc_hazus_level1|80122
public.wv_hyd_streams_tiger|67774
public.wv_bio_biodiversity_rank|63912
public.wv_hyd_navigable_waterways_structures|32116
public.wv_hyd_streams_high_quality|22656
public.wv_trn_roads_major_4800|19795
public.wv_bio_red_spruce_cover|15514
public.wv_str_samb_building_polygons|15505
public.wv_bnd_nhd_mussel_streams|11590
public.wv_eco_abandoned_mine_lands_line|10796
public.gbim_blockgroup_text_fragments|9747
public.wv_loc_geodetic_control_points|8559
public.spatial_ref_sys|8500
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ for db in msjarvisgis_v2 msjarvisgis msjarvisgis_v2_restore msjarvis postgres wv_gis; do echo "=== $db ==="; PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d "$db" -Atc "SELECT table_schema||'.'||table_name FROM information_schema.tables WHERE table_name ILIKE '%gbim_record%' OR table_name ILIKE '%admissible%';" 2>/dev/null; done
=== msjarvisgis_v2 ===
Pager usage is off.
=== msjarvisgis ===
Pager usage is off.
=== msjarvisgis_v2_restore ===
Pager usage is off.
=== msjarvis ===
Pager usage is off.
=== postgres ===
Pager usage is off.
=== wv_gis ===
Pager usage is off.
public.gbim_record
public.public_admissible_gbim
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5435 -U postgres -Atc "SELECT datname FROM pg_database WHERE datistemplate=false;" 2>&1 | head
Pager usage is off.
postgres
msjarvisgis
hilbert_people
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d wv_gis -c "SELECT 'gbim_record' AS t, count(*) FROM public.gbim_record UNION ALL SELECT 'admissible', count(*) FROM public.public_admissible_gbim;"
Pager usage is off.
      t      | count  
-------------+--------
 gbim_record | 237655
 admissible  |  93423
(2 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d wv_gis -c "\d public.gbim_record"
Pager usage is off.
                                             Table "public.gbim_record"
             Column              |           Type           | Collation | Nullable |            Default             
---------------------------------+--------------------------+-----------+----------+--------------------------------
 gbim_id                         | uuid                     |           | not null | gen_random_uuid()
 gbim_version                    | text                     |           | not null | '1.0'::text
 source_table                    | text                     |           | not null | 
 bg_table                        | text                     |           | not null | 
 geoid                           | text                     |           | not null | 
 metric_name                     | text                     |           | not null | 
 metric_value                    | numeric                  |           |          | 
 units                           | text                     |           |          | 
 aggregation                     | text                     |           |          | 
 join_key                        | text                     |           | not null | 'geoid'::text
 record_payload                  | jsonb                    |           | not null | 
 record_hash                     | text                     |           | not null | 
 chroma_collections_has          | boolean                  |           | not null | false
 chroma_collections_feature_hash | text                     |           |          | 
 promotion_state                 | text                     |           | not null | 'candidate'::text
 public_claim_allowed            | boolean                  |           | not null | false
 under_whose_authority           | text                     |           | not null | 'WVGIS Technical Center'::text
 company_name                    | text                     |           | not null | 'WVGIS Technical Center'::text
 observed_date                   | timestamp with time zone |           |          | 
 temporal_coverage_label         | text                     |           |          | 
 temporal_status                 | text                     |           |          | 
 ingested_at                     | timestamp with time zone |           | not null | now()
 degradation_status              | text                     |           | not null | 'fresh'::text
 degradation_checked_at          | timestamp with time zone |           | not null | now()
 created_at                      | timestamp with time zone |           | not null | now()
 updated_at                      | timestamp with time zone |           | not null | now()
 chroma_collection_name          | text                     |           |          | 
 chroma_item_id                  | text                     |           |          | 
 spatial_unit_id                 | text                     |           | not null | 
 spatial_unit_kind               | text                     |           | not null | 
 valid_time_start                | timestamp with time zone |           | not null | 
 valid_time_end                  | timestamp with time zone |           |          | 
Indexes:
    "gbim_record_pkey" PRIMARY KEY, btree (gbim_id)
    "gbim_record_claim_idx" btree (promotion_state, public_claim_allowed)
    "gbim_record_lookup_idx" btree (source_table, bg_table, geoid, metric_name)
    "gbim_record_unique_fact" UNIQUE CONSTRAINT, btree (source_table, bg_table, geoid, metric_name)
Check constraints:
    "gbim_record_authorized_metric_chk" CHECK (promotion_state <> 'authorized'::text OR metric_value IS NOT NULL)
    "gbim_record_promotion_state_chk" CHECK (promotion_state = ANY (ARRAY['candidate'::text, 'authorized'::text, 'refused'::text, 'sandbox'::text]))
    "gbim_record_public_claim_state_chk" CHECK (public_claim_allowed = false OR promotion_state = 'authorized'::text)
    "gbim_record_spacetime_provenance_chk" CHECK (NOT (promotion_state = 'authorized'::text AND public_claim_allowed = true) OR spatial_unit_id IS NOT NULL AND spatial_unit_kind IS NOT NULL AND valid_time_start IS NOT NULL AND under_whose_authority IS NOT NULL AND company_name IS NOT NULL AND ingested_at IS NOT NULL)
Referenced by:
    TABLE "gbim_provenance" CONSTRAINT "gbim_provenance_gbim_id_fkey" FOREIGN KEY (gbim_id) REFERENCES gbim_record(gbim_id) ON DELETE CASCADE
Policies:
    POLICY "gbim_read_policy" FOR SELECT
      TO runtime_governance_role
      USING (true)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d wv_gis -x -c "SELECT * FROM public.public_admissible_gbim LIMIT 1;"
Pager usage is off.
-[ RECORD 1 ]-------------------+-----------------------------------------------------------------
gbim_id                         | 00027b93-0a6a-4cd0-87c0-1cc82a0047c4
gbim_version                    | 1.0
source_table                    | public.wv_eco_industrial_sites
bg_table                        | public.wv_bg_eco_industrial_sites
geoid                           | 540810010012
metric_name                     | eco_industrial_sites_count
metric_value                    | 0
units                           | count
aggregation                     | COUNT(DISTINCT gid)
join_key                        | geoid
record_payload                  | {"geoid": "540810010012", "eco_industrial_sites_count": 0}
record_hash                     | f9cf7ba23558edf319bfa4117108318b20061a8e4aa94ae3a9f22ae69a2183e0
chroma_collections_has          | t
chroma_collections_feature_hash | b65487d821f7fe8dec4f07a4428474e9f08eb0eed68956dcf844519d989a0431
promotion_state                 | authorized
public_claim_allowed            | t
under_whose_authority           | WVGIS Technical Center
company_name                    | WVGIS Technical Center
observed_date                   | 
temporal_coverage_label         | dataset-attested
temporal_status                 | grounded
ingested_at                     | 2026-07-26 18:37:29.43012-04
degradation_status              | fresh
degradation_checked_at          | 2026-07-26 18:37:29.43012-04
created_at                      | 2026-07-26 18:32:42.409035-04
updated_at                      | 2026-07-26 18:38:06.009917-04
chroma_collection_name          | wv_gbim
chroma_item_id                  | 00027b93-0a6a-4cd0-87c0-1cc82a0047c4
spatial_unit_id                 | 540810010012
spatial_unit_kind               | blockgroup
valid_time_start                | 2020-01-01 00:00:00-05
valid_time_end                  | 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d wv_gis -c "SELECT 'gbim_record' AS t, count(*) FROM public.gbim_record UNION ALL SELECT 'admissible', count(*) FROM public.public_admissible_gbim;"
Pager usage is off.
      t      | count  
-------------+--------
 gbim_record | 237655
 admissible  |  93423
(2 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d wv_gis -c "\d public.gbim_record"
Pager usage is off.
                                             Table "public.gbim_record"
             Column              |           Type           | Collation | Nullable |            Default             
---------------------------------+--------------------------+-----------+----------+--------------------------------
 gbim_id                         | uuid                     |           | not null | gen_random_uuid()
 gbim_version                    | text                     |           | not null | '1.0'::text
 source_table                    | text                     |           | not null | 
 bg_table                        | text                     |           | not null | 
 geoid                           | text                     |           | not null | 
 metric_name                     | text                     |           | not null | 
 metric_value                    | numeric                  |           |          | 
 units                           | text                     |           |          | 
 aggregation                     | text                     |           |          | 
 join_key                        | text                     |           | not null | 'geoid'::text
 record_payload                  | jsonb                    |           | not null | 
 record_hash                     | text                     |           | not null | 
 chroma_collections_has          | boolean                  |           | not null | false
 chroma_collections_feature_hash | text                     |           |          | 
 promotion_state                 | text                     |           | not null | 'candidate'::text
 public_claim_allowed            | boolean                  |           | not null | false
 under_whose_authority           | text                     |           | not null | 'WVGIS Technical Center'::text
 company_name                    | text                     |           | not null | 'WVGIS Technical Center'::text
 observed_date                   | timestamp with time zone |           |          | 
 temporal_coverage_label         | text                     |           |          | 
 temporal_status                 | text                     |           |          | 
 ingested_at                     | timestamp with time zone |           | not null | now()
 degradation_status              | text                     |           | not null | 'fresh'::text
 degradation_checked_at          | timestamp with time zone |           | not null | now()
 created_at                      | timestamp with time zone |           | not null | now()
 updated_at                      | timestamp with time zone |           | not null | now()
 chroma_collection_name          | text                     |           |          | 
 chroma_item_id                  | text                     |           |          | 
 spatial_unit_id                 | text                     |           | not null | 
 spatial_unit_kind               | text                     |           | not null | 
 valid_time_start                | timestamp with time zone |           | not null | 
 valid_time_end                  | timestamp with time zone |           |          | 
Indexes:
    "gbim_record_pkey" PRIMARY KEY, btree (gbim_id)
    "gbim_record_claim_idx" btree (promotion_state, public_claim_allowed)
    "gbim_record_lookup_idx" btree (source_table, bg_table, geoid, metric_name)
    "gbim_record_unique_fact" UNIQUE CONSTRAINT, btree (source_table, bg_table, geoid, metric_name)
Check constraints:
    "gbim_record_authorized_metric_chk" CHECK (promotion_state <> 'authorized'::text OR metric_value IS NOT NULL)
    "gbim_record_promotion_state_chk" CHECK (promotion_state = ANY (ARRAY['candidate'::text, 'authorized'::text, 'refused'::text, 'sandbox'::text]))
    "gbim_record_public_claim_state_chk" CHECK (public_claim_allowed = false OR promotion_state = 'authorized'::text)
    "gbim_record_spacetime_provenance_chk" CHECK (NOT (promotion_state = 'authorized'::text AND public_claim_allowed = true) OR spatial_unit_id IS NOT NULL AND spatial_unit_kind IS NOT NULL AND valid_time_start IS NOT NULL AND under_whose_authority IS NOT NULL AND company_name IS NOT NULL AND ingested_at IS NOT NULL)
Referenced by:
    TABLE "gbim_provenance" CONSTRAINT "gbim_provenance_gbim_id_fkey" FOREIGN KEY (gbim_id) REFERENCES gbim_record(gbim_id) ON DELETE CASCADE
Policies:
    POLICY "gbim_read_policy" FOR SELECT
      TO runtime_governance_role
      USING (true)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d wv_gis -x -c "SELECT * FROM public.public_admissible_gbim LIMIT 1;"
Pager usage is off.
-[ RECORD 1 ]-------------------+-----------------------------------------------------------------
gbim_id                         | 00027b93-0a6a-4cd0-87c0-1cc82a0047c4
gbim_version                    | 1.0
source_table                    | public.wv_eco_industrial_sites
bg_table                        | public.wv_bg_eco_industrial_sites
geoid                           | 540810010012
metric_name                     | eco_industrial_sites_count
metric_value                    | 0
units                           | count
aggregation                     | COUNT(DISTINCT gid)
join_key                        | geoid
record_payload                  | {"geoid": "540810010012", "eco_industrial_sites_count": 0}
record_hash                     | f9cf7ba23558edf319bfa4117108318b20061a8e4aa94ae3a9f22ae69a2183e0
chroma_collections_has          | t
chroma_collections_feature_hash | b65487d821f7fe8dec4f07a4428474e9f08eb0eed68956dcf844519d989a0431
promotion_state                 | authorized
public_claim_allowed            | t
under_whose_authority           | WVGIS Technical Center
company_name                    | WVGIS Technical Center
observed_date                   | 
temporal_coverage_label         | dataset-attested
temporal_status                 | grounded
ingested_at                     | 2026-07-26 18:37:29.43012-04
degradation_status              | fresh
degradation_checked_at          | 2026-07-26 18:37:29.43012-04
created_at                      | 2026-07-26 18:32:42.409035-04
updated_at                      | 2026-07-26 18:38:06.009917-04
chroma_collection_name          | wv_gbim
chroma_item_id                  | 00027b93-0a6a-4cd0-87c0-1cc82a0047c4
spatial_unit_id                 | 540810010012
spatial_unit_kind               | blockgroup
valid_time_start                | 2020-01-01 00:00:00-05
valid_time_end                  | 

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d wv_gis -c "SELECT count(DISTINCT valid_time_start) AS distinct_starts, count(DISTINCT temporal_coverage_label) AS distinct_labels, count(DISTINCT date_trunc('year',valid_time_start)) AS distinct_years FROM public.public_admissible_gbim;"
Pager usage is off.
 distinct_starts | distinct_labels | distinct_years 
-----------------+-----------------+----------------
               1 |               1 |              1
(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d wv_gis -c "SELECT count(*) FILTER (WHERE metric_value=0) AS zeros, count(*) FILTER (WHERE metric_value<>0) AS nonzero, count(DISTINCT metric_name) AS distinct_metrics FROM public.public_admissible_gbim;"
Pager usage is off.
 zeros | nonzero | distinct_metrics 
-------+---------+------------------
 49750 |   43673 |               57
(1 row)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ cd ~/msjarvis-trust-integration

printf '\n===== 1. LOCATION =====\n'
pwd

printf '\n===== 2. GIT STATE =====\n'
git branch --show-current
git rev-parse HEAD
git status --short --branch

printf '\n===== 3. REPOSITORY ROOT =====\n'
find . -maxdepth 2 -type f | sort | sed -n '1,250p'

printf '\n===== 4. DIRECTORIES =====\n'
find . -maxdepth 2 -type d | sort | sed -n '1,250p'

printf '\n===== 5. DATABASE / VECTOR / GRAPH REFERENCES =====\n'
grep -RniE \
  'postgres|postgis|chroma|chromadb|redis|neo4j|graph|hilbert|embedding|vector' \
  --exclude-dir=.git \
  --exclude-dir=.venv \
  --exclude-dir=venv \
  redis-cli -h 127.0.0.1 ping 2>&1 || true2/api/v2/heartbeat 2>&1 || true' 2>/de

===== 1. LOCATION =====
/home/cakidd/msjarvis-trust-integration

===== 2. GIT STATE =====
stage-6.11.9-guardian-decision-service-2a
e8827b253a87025cae1945f9032fffb67caea992
## stage-6.11.9-guardian-decision-service-2a
?? evidence/stage-6.10.1/
?? evidence/stage-6.10.2/
?? evidence/stage-6.10.3/
?? evidence/stage-6.10.4/
?? evidence/stage-6.10.5/
?? evidence/stage-6.10.7/stage-6.10.7-operational-gate-baseline.log
?? evidence/stage-6.10.7/stage-6.10.7-operational-gate-tests.log
?? evidence/stage-6.10.8/stage-6.10.8-release-attestation-baseline.log
?? evidence/stage-6.10/
?? evidence/stage-6.11.0/
?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-contract-analysis.log
?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-discovery.log
?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-tests.log
?? evidence/stage-6.11.1/stage-6.11.1-canonicalization-verification.log
?? evidence/stage-6.11.2/stage-6.11.2-key-registry-discovery.log
?? evidence/stage-6.11.2/stage-6.11.2-signature-verification-contract-analysis.log
?? evidence/stage-6.11.2/stage-6.11.2-signature-verification-discovery.log
?? evidence/stage-6.11.4/stage-6.11.4-start.log

===== 3. REPOSITORY ROOT =====
./=0.29.0
./all_gis_vectors_filtered.txt
./all_gis_vectors_full.txt
./all_gis_vectors_ingest.txt
./all_gis_vectors.txt
./all_gis_vectors_unique.txt
./api_resources.py
./application_service.py
./ask_gis_near_oakhill.py
./ask_gis.py
./attrs_api.py
./attrs_with_geom_api.py
./auth_api.py
./auth_router.py
./autonomouslearner.py
./backup_filename_index.txt
./backup_roots.txt
./bbb_requirements.txt
./bootstrap_gbim_beliefs_eq1.py
./bulk_ingest_attrs.py
./call_rag_with_entanglement_example.py
./ch52_checkpoint/msjarvisgis_v2-final.dump
./ch52_checkpoint/msjarvisgis_v2-full.dump
./ch52_checkpoint/wv_corpus_summary.csv
./ch52_checkpoint/wv_derived_governance_tables.csv
./ch52_checkpoint/wv_source_files_manifest.csv
./ch52_checkpoint/wv_source_manifest_layers.csv
./chapter42_evidence_2026-07-16.txt
./chapter44_gisrag_exact_validation.json
./chapter46_exact_patch_context.json
./chat_light_current.py
./check_hilbert_commons.sh
./.check_hilbert_people_resolved.tsv
./check_hilbert_people_v2.sh
./check_hilbert_people_v3.sh
./check_hilbert_people_v4.sh
./chroma_copy_v2.py
./chroma_ingestion_sources.txt
./config/gbim_sources.yaml
./constitutional_api.py
./copy_pending_collections.py
./CURRENT_LLM_STACK_NOTES.txt
./demo_msjarvis_ranked.py
./demo_msjarvis_resources.py
./dgm_cycle.sh
./diagnostics/gateway_head_1_220.py
./diagnostics/gateway_mid_220_420.py
./diagnostics/gateway_policy_hook_lines.txt
./diagnostics/gateway_tail_420_700.py
./diagnostics/unified_gateway_extended_policy_sections_20260801T022011Z.py
./diagnostics/unified_gateway_live_20260801T020501Z.py
./diagnostics/wv_block_hardened_2026-07-31.py
./diagnostics/wv_success_summary_2026-07-31.txt
./discipline/Comparative Frameworks in Geography and Commons.md
./discipline/Definitions and Scope.md
./discipline/Discipline and Instruments.md
./discipline/Ethics of Anchors and Non‑Representation.md
./discipline/Measurement, Resolution, and Limits.md
./discipline/Methods.md
./discipline/Non-Digital Commons in a Polymathmatic Lens.md
./discipline/Polymathmatic Geography: A Manifesto.md
./discipline/Polymathmatic Geography and Commons Theory.md
./discipline/Polymathmatic Geography and Human Geography.md
./discipline/Polymathmatic Geography and Junction Conditions.md
./discipline/Polymathmatic Geography and Metaphysical Edges.md
./discipline/Polymathmatic Geography and Physics‑Style Method.md
./discipline/Polymathmatic Geography and Power.md
./discipline/Polymathmatic Geography and Representation Learning.md
./discipline/Polymathmatic Geography and the GeoBelief Information Model (GBIM.md
./discipline/polymathmatic geography syllabus.md
./discipline/Polymatmatic Geography and  Beyond 3D Maps.md
./discipline/Principles of Polymathmatic Geography.md
./discipline/Semantics in Polymathmatic Geography.md
./discipline/what-is-polymatmatic-geography.md
./discipline/World‑Models and Anchoring (Safety Pins to Planets.md
./docker-compose.commons-gateway-closeout.yml
./docker-compose.crypto-policy-closeout.yml
./docker-compose.fractal-closeout.yml
./docker-compose.override.ch14-sandbox-bridge.yml
./docker-compose.policy-set-closeout.yml
./docker-compose.policy-set.yml
./docker-compose.production-closeout.yml
./docker-compose.real-orchestrator.yml
./docker-compose.STABLE.20260719045021.yml
./docker-compose.yml
./docker-compose.yml.badmount.2026-07-16-120446
./docker-compose.yml.badsidecarnetworks.2026-07-16-120750
./docker-compose.yml.broken.2026-07-16-120325
./Dockerfile
./Dockerfile.20llm
./Dockerfile.agents
./Dockerfile.belief_revision
./Dockerfile.brain
./Dockerfile.civic-intake-closeout
./Dockerfile.commons-gateway-closeout
./Dockerfile.consciousnessbridge
./Dockerfile.full_neuro
./Dockerfile.gateway
./Dockerfile.gis_rag
./Dockerfile.hilbert_spatial_chat
./Dockerfile-llm10-proxy
./Dockerfile-llm11-proxy
./Dockerfile-llm12-proxy
./Dockerfile-llm13-proxy
./Dockerfile-llm14-proxy
./Dockerfile-llm15-proxy
./Dockerfile-llm16-proxy
./Dockerfile-llm17-proxy
./Dockerfile-llm18-proxy
./Dockerfile-llm19-proxy
./Dockerfile-llm1-proxy
./Dockerfile-llm20-proxy
./Dockerfile-llm21-proxy
./Dockerfile-llm22-proxy
./Dockerfile-llm2-proxy
./Dockerfile-llm3-proxy
./Dockerfile-llm4-proxy
./Dockerfile-llm5-proxy
./Dockerfile-llm6-proxy
./Dockerfile-llm7-proxy
./Dockerfile-llm8-proxy
./Dockerfile-llm9-proxy
./Dockerfile.local_resources
./Dockerfile.mountainshares_commons_gateway
./Dockerfile.nbb_icontainers_fastapi
./Dockerfile.neuro
./Dockerfile.neuro-prefrontal-patched
./Dockerfile.qualia
./Dockerfile.rag
./Dockerfile.rag_server
./Dockerfile.rag_server_main
./Dockerfile.ragservermain
./Dockerfile.sandbox
./dockerfiles/Dockerfile.policy-set
./Dockerfile.swarm
./Dockerfile.woah
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md
./dynamic_port_service_no_flask.py
./email_service.py
./embed_blockgroups_chroma.py
./embed_blockgroups_minilm_chroma.py
./embed_blockgroups_statewide_minilm_chroma.py
./embed_blockgroups_statewide_v2_minilm_chroma.py
./embed_blockgroups_v6.py
./embed_blockgroups_v7.py
./embed_blockgroups_v8.py
./embed_blockgroups_v9.py
./enrich_from_attrs.py
./enrich_where.py
./.env
./export_chroma_8002.py
./export_chroma_raw_8002.py
./export_gbim_sample.py
./gateway8050_inline.py
./gateway-entrypoint.sh
./gbim_chroma.py
./gbim_coverage_datasets.csv
./gbim_manifest_datasets.csv
./gbim_missing_datasets.csv
./gbim_orchestrator.py
./gbim_wv_blockgroups_v2.csv
./generate_spiritual_inventories.py
./gis_candidates_global.txt
./gis_candidates_stage2.txt
./gisgeodb_storage.py
./gisgeodbstorage.py
./gis_rag_query.py
./gis_rag_server.py
./.git
./.gitignore
./governance_evidence/ch44_phi_reading_2026-07-16.json
./governance_evidence/ch44_phi_reading_2026-07-16-postrebuild.json
./governance_evidence/ch44_phi_reading_2026-07-16-v2.json
./governance_evidence/ch44_status_2026-07-18.json
./governance_evidence/gis_rag_rebuild_validation_2026-07-16.txt
./index_gis_to_chroma.py
./ingest_attrs_to_chroma.py
./ingest_gbimworldviewentities_from_csv.py
./ingest_kanawha_images.py
./ingest_kanawha_resources.py
./ingest_missing_attrs.py
./ingest_msjarvis_corpus.py
./ingest_personal_pdfs.py
./ingest_wv_income_maintenance_manual.py
./jarvis_eeg_beta_5m.py
./jarvis_identity.db
./KNOWN_LIMITATIONS_20LLM_SEQUENTIAL.txt
./layer3_opt_in.py
./list_due_for_verification.py
./load_blockgroup_coverage_appalachian_basin.sql
./load_blockgroup_coverage_arc_counties.sql
./load_blockgroup_coverage_canaan_nwr.sql
./load_blockgroup_coverage_census_designated_places.sql
./load_blockgroup_coverage_county_boundaries_utm83.sql
./load_blockgroup_coverage_county_boundaries_wma84.sql
./load_blockgroup_coverage_ecoregions.sql
./load_blockgroup_coverage_missing.sql
./load_blockgroup_coverage_red_spruce.sql
./load_services_attrs_and_enrich.py
./load_wv_blockgroup_beliefs_v1.py
./logs/epistemic_changes.jsonl
./main_brain.py
./main.py
./Makefile
./merkle_identity.py
./migrations/001_hp_governed_manifest.sql
./migrations/001_kyc_vault.sql
./migrations/002_fix_chroma_manifest_cols.sql
./migrations/002_founder_tokens.sql
./migrations/003_ledger_columns.sql
./migrations/004_ledger_event_types.sql
./migrations/004_promotion_seed.sql
./migrations/005_promotion_constraint_seed.sql
./migrations/005_three_tier_identity.sql
./migrations/006_dedup_promotion_seed.sql
./migrations/007_signed_promotion_seed.sql
./migrations/008_doc_count_sync.sql
./migrations/009_fix_doc_count_column_name.sql
./migrations/009_gbim_manifest_tables.sql
./migrations/010_governed_manifest_hilbert_people.sql
./missing_local_files.txt
./models.py
./ms_allis_private_inventory.json
./ms_allis_tools/latest_mst_anvil_address.txt
./ms_allis_tools/mst_manifest.json
./ms_allis_tools/README.mst_tools.txt
./msjarvis_chroma_test.py
./msjarvis_embed_gbim.py
./msjarvis_embed_gbim_resume_tail.py
./msjarvisgis-final.dump
./msjarvisgis_v2-final.dump
./msjarvisragserverwvpatch.py
./msjarvis_resources.py
./msjarviswoahalgorithms.py
./old_drive_gis_candidates.txt
./.ops/auth_balances_8097.json
./.ops/auth_health_8097.json
./.ops/auth_ledger_8097.json
./.ops/auth_me_8097.json
./.ops/auth_timesheet_8097.json
./.ops/restart_auth_8097.sh
./.ops/verify_auth_8097.sh
./output/46_chroma_candidate_inspection.txt
./output/46_full_collection_scan.txt
./output/46_materialization_run.txt
./output/46_tensor_bridge_sample.txt
./output/46_tensor_bridge_status.txt
./output/46_tensor_bridge_summary.txt
./output/47_assertion_gateway_core.txt
./output/47_assertion_gateway_db_verify.txt

===== 4. DIRECTORIES =====
.
./ch52_checkpoint
./chroma_data
./chroma_data/4818e3d4-3727-4918-949d-80c4830be3a7
./chroma_data/73767a28-d520-43de-801a-cc8ffbac56e5
./config
./config/users
./deploy
./deploy/qualia-orchestrator
./diagnostics
./discipline
./discipline/case_studies
./dockerfiles
./docs
./docs/architecture
./evidence
./evidence/stage-6.10
./evidence/stage-6.10.1
./evidence/stage-6.10.2
./evidence/stage-6.10.3
./evidence/stage-6.10.4
./evidence/stage-6.10.5
./evidence/stage-6.10.6
./evidence/stage-6.10.7
./evidence/stage-6.10.8
./evidence/stage-6.11.0
./evidence/stage-6.11.1
./evidence/stage-6.11.2
./evidence/stage-6.11.3
./evidence/stage-6.11.4
./evidence/stage-6.11.5
./evidence/stage-6.11.6
./evidence/stage-6.11.7
./evidence/stage-6.11.9-2a
./evidence/stage-6.11.9-2b
./evidence/stage-6.8
./evidence/stage-6.9
./formal
./formal/commons_proofs
./governance_evidence
./infra
./infra/nginx
./logs
./migrations
./ms_allis_tools
./neurobiological_brain
./neurobiological_brain/darwin_godel_machines
./.ops
./output
./output/ch46_bundle
./output/ch47_bundle
./phase1_public_lands
./phase1_public_lands/logs
./phase1_public_lands/unzipped
./policies
./.pytest_cache
./.pytest_cache/v
./rejected_patches
./schemas
./schemas/mountainshares-trust-receipts
./scratch_edits
./scripts
./services
./services/aaacpe_scraper
./services/gbim-router
./services/gis-rag
./services/hilbert
./services/hilbert_commons
./services/jarvis-assertion-gateway
./services/neurobiologicalbrain
./services/overflow_policy
./services/person_space_policy
./services/pia_sampler
./services/__pycache__
./staged_mutations
./tests
./tests/fixtures
./tests/policy
./tests/__pycache__
./thesis
./thesis_chapter_gates
./thesis_chapter_gates/probes
./thesis_chapter_gates/reports
./thesis_chapter_gates/rewrites
./tools

===== 5. DATABASE / VECTOR / GRAPH REFERENCES =====
./embed_blockgroups_chroma.py:6:from chromadb import PersistentClient
./embed_blockgroups_chroma.py:10:CSV_PATH = BASE / "wv_blockgroup_belief_vector_ready_v1.csv"
./embed_blockgroups_chroma.py:11:CHROMA_PATH = BASE / "chroma_db"
./embed_blockgroups_chroma.py:34:chroma = PersistentClient(path=str(CHROMA_PATH))
./embed_blockgroups_chroma.py:35:collection = chroma.get_or_create_collection(name=COLLECTION_NAME)
./embed_blockgroups_chroma.py:42:    response = client.embeddings.create(
./embed_blockgroups_chroma.py:43:        model="text-embedding-3-large",
./embed_blockgroups_chroma.py:48:    embeddings = [item.embedding for item in response.data]
./embed_blockgroups_chroma.py:64:        embeddings=embeddings,
./embed_blockgroups_chroma.py:71:print(f"Chroma path: {CHROMA_PATH}")
./stage-6.11.7-manifest-scope-20260807_195853.log:121:=== C. how manifest approvals are cryptographically verified ===
./stage-6.11.7-manifest-scope-20260807_195853.log:123:from cryptography.exceptions import InvalidSignature
./stage-6.11.7-manifest-scope-20260807_195853.log:124:from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
./enrich_where.py:3:CONN_STR = "postgresql://postgres:postgres@localhost:5435/msjarvisgis"
./gisgeodb_storage.py:1:import chromadb
./gisgeodb_storage.py:2:from chromadb.config import Settings, DEFAULT_TENANT, DEFAULT_DATABASE
./gisgeodb_storage.py:5:from services.chroma_client import get_chroma_client
./gisgeodb_storage.py:8:    client = get_chroma_client()
./gisgeodb_storage.py:12:    client = get_chroma_client()
./gisgeodb_storage.py:17:from services.chroma_client import get_chroma_client
./gisgeodb_storage.py:20:    client = get_chroma_client()
./gisgeodb_storage.py:25:    client = get_chroma_client()
./gisgeodb_storage.py:29:def get_hilbert_collection():
./gisgeodb_storage.py:30:    client = get_chroma_client()
./gisgeodb_storage.py:31:    # Existing Hilbert / research memory
./Dockerfile.brain:10:    fastapi uvicorn httpx redis pydantic aiohttp requests dilithium-py Flask Flask-CORS \
./Dockerfile.brain:11:    chromadb==0.6.3 numpy python-dateutil pytz scikit-learn scipy textblob sentence-transformers prometheus-fastapi-instrumentator || \
./Dockerfile.brain:15:     fastapi uvicorn httpx redis pydantic aiohttp requests dilithium-py Flask Flask-CORS \
./Dockerfile.brain:16:     chromadb==0.6.3 numpy python-dateutil pytz scikit-learn scipy textblob sentence-transformers prometheus-fastapi-instrumentator)
./token_service.py:4:Every existing token in your Redis was created with this exact shape — we mirror it
./token_service.py:33:    def __init__(self, redis_client):
./token_service.py:34:        self.redis = redis_client
./token_service.py:55:        self.redis.hset(f"redteam:token:{token}", mapping={
./token_service.py:65:        self.redis.expire(f"redteam:token:{token}", self.TOKEN_TTL)
./token_service.py:68:        if not self.redis.exists(f"redteam:quota:{userid}"):
./token_service.py:69:            self.redis.hset(f"redteam:quota:{userid}", mapping={
./token_service.py:82:        record = self.redis.hgetall(key)
./token_service.py:92:        self.redis.expire(key, self.TOKEN_TTL)
./token_service.py:96:        if not self.redis.exists(f"redteam:token:{token}"):
./token_service.py:98:        self.redis.hset(f"redteam:token:{token}", "active", "false")
./token_service.py:104:        for key in self.redis.scan_iter("redteam:token:*"):
./token_service.py:106:            record = self.redis.hgetall(key_str)
./token_service.py:119:        Validate username + password against Redis user record.
./token_service.py:122:        Expected Redis key: user:{userid}  fields: password_hash, roles, county, uei
./token_service.py:128:        record = self.redis.hgetall(f"user:{username_clean}")
./token_service.py:131:            for k in self.redis.scan_iter("user:*"):
./token_service.py:132:                rec = self.redis.hgetall(k)
./token_service.py:189:        userid = self.redis.get(f"refresh:{refresh_token}")
./token_service.py:195:        self.redis.delete(f"refresh:{refresh_token}")
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:213:Possible future backends include SQLite for a single authoritative node, PostgreSQL for shared transactional authority, or another store that can prove equivalent atomicity, durability, and conflict semantics.
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:129:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:144:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:180:PYTHONPATH="$ROOT:$ROOT/services:$ROOT/services/hilbert" pytest -q \
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:182:  tests/test_ch04_ch44_hilbert_phi_probe.py \
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:22:cat > services/hilbert/dgm_governed_cycle.py <<'PY'
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:44:    "services/hilbert/dgm_runtime_state/",
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:92:    for d in [WORKSPACE, QUEUE, APPLIED, REJECTED, ROOT / "services/hilbert/dgm_runtime_state"]:
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:311:chmod +x services/hilbert/dgm_governed_cycle.py
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:312:echo "WROTE=services/hilbert/dgm_governed_cycle.py"
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:320:from services.hilbert import dgm_governed_cycle as dgm
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:404:        "# Live governed patch application is handled by services.hilbert.dgm_governed_cycle.\n    # This worker must not claim direct application unless it delegates to that gate."
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:408:        "# Live governed patch application is handled by services.hilbert.dgm_governed_cycle.\r\n    # This worker must not claim direct application unless it delegates to that gate."
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:436:PYTHONPATH="$ROOT:$ROOT/services" "\$PYTHON_BIN" services/hilbert/dgm_governed_cycle.py --cycle
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:453:PYTHONPATH="$ROOT:$ROOT/services" "\$PYTHON_BIN" services/hilbert/dgm_governed_cycle.py --cycle
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:465:PYTHONPATH="$ROOT:$ROOT/services" "$PYTHON_BIN" services/hilbert/dgm_governed_cycle.py --cycle | tee "$PROBE_JSON"
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:474:pgrep -af 'services/hilbert/recurrent_epistemic_runner.py'
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:11:MODULE="$ROOT/services/hilbert/pia_subspace_stability_review.py"
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:46:    "face_embedding",
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:123:        and "face_embedding" in str(ch48.get("blocked_surveillance", {}).get("reason", "")),
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:141:        collections.get("community_hilbert_commons_before") == collections.get("community_hilbert_commons_after"),
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:142:        "Private H_p promotion must not silently change community_hilbert_commons.",
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:257:from services.hilbert.pia_subspace_stability_review import (
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:271:            "reason": "surveillance_adjacent_metadata:face_embedding",
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:279:            "community_hilbert_commons_before": 0,
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:280:            "community_hilbert_commons_after": 0,
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:299:            "community_hilbert_commons_before": 0,
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:300:            "community_hilbert_commons_after": 0,
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:312:PYTHONPATH="$ROOT:$ROOT/services:$ROOT/services/hilbert" pytest -q "$TEST"
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:316:PYTHONPATH="$ROOT:$ROOT/services:$ROOT/services/hilbert" python3 "$MODULE" | tee "$JSON_REPORT"
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:345:PYTHONPATH="$ROOT:$ROOT/services:$ROOT/services/hilbert" pytest -q \
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:348:  tests/test_ch04_ch44_hilbert_phi_probe.py \
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:38:cat > services/hilbert/ch25_consciousness_coordinator_probe.py <<'PY'
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:56:    "jarvis-hilbert-state",
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:57:    "jarvis-hilbert-time",
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:72:    "hilbert_state": "http://127.0.0.1:18092/health",
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:73:    "hilbert_time": "http://127.0.0.1:18094/health",
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:79:    "pituitary_global_modes": ["services/hilbert/pituitary_global_modes_probe.py", ["pituitary", "promotion_threshold"]],
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:272:"$PYTHON_BIN" -m py_compile services/hilbert/ch25_consciousness_coordinator_probe.py
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:278:from services.hilbert import ch25_consciousness_coordinator_probe as probe
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:305:"$PYTHON_BIN" services/hilbert/ch25_consciousness_coordinator_probe.py | tee "$PROBE_JSON"
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:338:- Hilbert state, Hilbert time, BBB, guardian, and Chroma/Redis-backed services are live where relevant.
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:450:    runtime=len(re.findall(r"`[^`]+`|http://|https://|docker|redis|postgres|chroma|service|endpoint|container", text, re.I))
./thesis_chapter_gates/close_ch37_no_build_v2.sh:100:    for term in ["bypass consent","ignore consent","disclose private","private people-space","surveillance","face embedding","no audit","without provenance","override guardian","evade review"]:
./thesis_chapter_gates/close_ch37_no_build_v2.sh:250:Use the recovered pre-duplication language as the prose base, but replace April 2026 operational counts, ports, database sizes, and closure claims with July 2026 as-built evidence. Do not restore stale container counts or old PostgreSQL/Chroma totals as current truth.
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:19:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:25:  AND tablename IN ('gbim_active_collection','gbim_collection_manifest','gbim_chroma_publication_manifest')
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:37:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -v ON_ERROR_STOP=1 <<'SQL'
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:38:GRANT USAGE ON SCHEMA public TO postgres;
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:39:GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON public.gbim_collection_manifest TO postgres;
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:40:GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON public.gbim_active_collection TO postgres;
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:41:GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON public.gbim_chroma_publication_manifest TO postgres;
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:46:GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON public.gbim_chroma_publication_manifest TO msjarvis_admin;
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:51:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:52:SELECT 'SCHEMA_USAGE_POSTGRES=' || has_schema_privilege('postgres','public','USAGE');
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:53:SELECT 'MANIFEST_SELECT_POSTGRES=' || has_table_privilege('postgres','public.gbim_collection_manifest','SELECT');
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:54:SELECT 'MANIFEST_REFERENCES_POSTGRES=' || has_table_privilege('postgres','public.gbim_collection_manifest','REFERENCES');
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:55:SELECT 'ACTIVE_INSERT_POSTGRES=' || has_table_privilege('postgres','public.gbim_active_collection','INSERT');
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:56:SELECT 'ACTIVE_REFERENCES_POSTGRES=' || has_table_privilege('postgres','public.gbim_active_collection','REFERENCES');
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:60:echo "=== 4. RE-PROBE ZCTA WITH EMBEDDING DIMENSION ==="
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:63:import chromadb
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:66:client = chromadb.HttpClient(host="localhost", port=8002)
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:73:got = col.get(limit=1, include=["embeddings", "metadatas"])
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:74:embs = got.get("embeddings", None)
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:76:    raise SystemExit("REQUIRED_FAIL=zcta_embedding_sample_missing")
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:81:    raise SystemExit("REQUIRED_FAIL=zcta_embedding_dimension_invalid")
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:104:    "embedding_dimension": dim,
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:121:dim = int(p["embedding_dimension"])
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:130:    embedding_model=COALESCE(embedding_model,'chroma-default'),
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:131:    embedding_dimension={dim},
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:135:    authority_class=COALESCE(authority_class,'public_civic_geography'),
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:152:  snapshot_version, rendering_version, embedding_model, embedding_dimension,
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:161:  'chroma-default', {dim}, {p["record_count"]}, '{p["collection_hash"]}',
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:162:  'validated', 'public_civic_geography', 'public',
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:173:UPDATE public.gbim_chroma_publication_manifest
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:178:    embedding_model=COALESCE(embedding_model,'chroma-default'),
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:179:    embedding_dimension=COALESCE(embedding_dimension,{dim}),
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:183:    deployment_note='Registered from live governed Chroma collection during Ch02 as-built closure.'
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:186:INSERT INTO public.gbim_chroma_publication_manifest (
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:188:  snapshot_version, embedding_model, embedding_dimension, record_count,
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:194:  'chroma-default', {dim}, {p["record_count"]}, '{p["collection_hash"]}',
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:195:  now(), 'Registered from live governed Chroma collection during Ch02 as-built closure.'
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:197:  SELECT 1 FROM public.gbim_chroma_publication_manifest
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:228:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -v ON_ERROR_STOP=1 -f "$SQLFILE"
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:233:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:241:    AND embedding_dimension=384
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:246:  FROM public.gbim_chroma_publication_manifest
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:249:    AND embedding_dimension=384
./thesis_chapter_gates/gate_ch36_identity_registration.sh:37:mkdir -p services/hilbert
./thesis_chapter_gates/gate_ch36_identity_registration.sh:38:cat > services/hilbert/ch36_identity_registration_probe.py <<'PY'
./thesis_chapter_gates/gate_ch36_identity_registration.sh:52:    "services/hilbert/chroma_policy.py": ["registration_layer", "public_opt_in"],
./thesis_chapter_gates/gate_ch36_identity_registration.sh:53:    "services/hilbert/ingest_worker.py": ["registration_layer", "public_opt_in"],
./thesis_chapter_gates/gate_ch36_identity_registration.sh:74:    "jarvis-chroma",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:75:    "jarvis-redis",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:76:    "jarvis-hilbert-state",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:82:    "chroma": "http://127.0.0.1:8002/api/v2/heartbeat",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:83:    "hilbert_state": "http://127.0.0.1:18092/health",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:290:"$PYTHON_BIN" -m py_compile services/hilbert/ch36_identity_registration_probe.py
./thesis_chapter_gates/gate_ch36_identity_registration.sh:296:from services.hilbert import ch36_identity_registration_probe as probe
./thesis_chapter_gates/gate_ch36_identity_registration.sh:317:"$PYTHON_BIN" services/hilbert/ch36_identity_registration_probe.py | tee "$PROBE_JSON"
./thesis_chapter_gates/gate_ch36_identity_registration.sh:348:- \`registration_layer\` and \`public_opt_in\` are source-visible in Hilbert/Chroma write metadata paths.
./thesis_chapter_gates/gate_ch36_identity_registration.sh:352:- Required BBB, guardian, KYC vault, Chroma, Redis, and Hilbert-state containers are present and running.
./thesis_chapter_gates/gate_ch36_identity_registration.sh:465:    runtime=len(re.findall(r"`[^`]+`|http://|https://|docker|redis|postgres|chroma|service|endpoint|container", text, re.I))
./thesis_chapter_gates/finalize_ch41_cron_and_seal.sh:20:test -f services/hilbert/continuous_validation_harness.py
./thesis_chapter_gates/finalize_ch41_cron_and_seal.sh:21:"$PYTHON_BIN" -m py_compile services/hilbert/continuous_validation_harness.py
./thesis_chapter_gates/finalize_ch41_cron_and_seal.sh:23:! rg -n "evaluate_candidate" services/hilbert/continuous_validation_harness.py
./thesis_chapter_gates/finalize_ch41_cron_and_seal.sh:24:rg -n "def check_dgm_governed_cycle|run_cycle|DGMProposal|allowlist_probe" services/hilbert/continuous_validation_harness.py
./thesis_chapter_gates/finalize_ch41_cron_and_seal.sh:38:"$PYTHON_BIN" services/hilbert/continuous_validation_harness.py > "logs/ch41_continuous_validation/harness_$STAMP.json"
./thesis_chapter_gates/finalize_ch41_cron_and_seal.sh:58:"$PYTHON_BIN" services/hilbert/continuous_validation_harness.py | tee "$HARNESS_JSON"
./thesis_chapter_gates/finalize_ch41_cron_and_seal.sh:100:- Continuous validation harness is installed at \`services/hilbert/continuous_validation_harness.py\`.
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:83:pgrep -af 'services/hilbert/recurrent_epistemic_runner.py' || true
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:91:cat > services/hilbert/dgm_closure_probe.py <<'PY'
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:203:    runner = run(["pgrep", "-af", "services/hilbert/recurrent_epistemic_runner.py"])
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:220:        "hilbert_time": http_json("http://127.0.0.1:18094/health"),
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:221:        "hilbert_state": http_json("http://127.0.0.1:18092/health"),
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:277:chmod +x services/hilbert/dgm_closure_probe.py
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:278:echo "WROTE=services/hilbert/dgm_closure_probe.py"
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:282:PYTHONPATH="$ROOT:$ROOT/services" "$PYTHON_BIN" services/hilbert/dgm_closure_probe.py | tee "$EVIDENCE_JSON"
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:297:  tests/test_ch04_ch44_hilbert_phi_probe.py \
./thesis_chapter_gates/fix_ch14_sandbox_host_gateway_bridge.sh:136:PYTHONPATH="$ROOT:$ROOT/services" "$PYTHON_BIN" services/hilbert/internal_state_sandbox_probe.py | tee "$POST_PROBE"
./thesis_chapter_gates/fix_ch41_dgm_api_v2_and_close.sh:23:path = Path("services/hilbert/continuous_validation_harness.py")
./thesis_chapter_gates/fix_ch41_dgm_api_v2_and_close.sh:34:    import services.hilbert.dgm_governed_cycle as dgm
./thesis_chapter_gates/fix_ch41_dgm_api_v2_and_close.sh:74:            target_path="services/hilbert/dgm_governed_cycle.py",
./thesis_chapter_gates/fix_ch41_dgm_api_v2_and_close.sh:198:! rg -n "evaluate_candidate" services/hilbert/continuous_validation_harness.py
./thesis_chapter_gates/fix_ch41_dgm_api_v2_and_close.sh:199:rg -n "def check_dgm_governed_cycle|DGMProposal|DGMProposal.evaluate|dgm.evaluate|script_contract" services/hilbert/continuous_validation_harness.py
./thesis_chapter_gates/fix_ch41_dgm_api_v2_and_close.sh:201:"$PYTHON_BIN" -m py_compile services/hilbert/continuous_validation_harness.py
./thesis_chapter_gates/fix_ch41_dgm_api_v2_and_close.sh:207:from services.hilbert.continuous_validation_harness import check_dgm_governed_cycle
./thesis_chapter_gates/fix_ch41_dgm_api_v2_and_close.sh:222:"$PYTHON_BIN" services/hilbert/continuous_validation_harness.py | tee "$HARNESS_JSON"
./thesis_chapter_gates/fix_ch41_dgm_api_v2_and_close.sh:255:- Continuous validation harness is installed at \`services/hilbert/continuous_validation_harness.py\`.
./thesis_chapter_gates/next_after_ch31_operational_gate.sh:52:runtime=re.compile(r"\b(audit|validation|test|harness|health|docker|container|service|endpoint|port|redis|postgres|chroma|runner|cron|gateway)\b", re.I)
./thesis_chapter_gates/next_after_ch31_operational_gate.sh:91:rg -n "audit|validation|test|harness|health|docker|container|service|endpoint|port|redis|postgres|chroma|runner|cron|gateway|will|would|should|future|not yet|proven|complete|guarantee" "$DOCS/thesis/$NEXT_FILE" || true
./thesis_chapter_gates/next_after_ch31_operational_gate.sh:130:  find tests -type f 2>/dev/null | sort | rg 'test_|ch[0-9]+|policy|guardian|bbb|hilbert|dgm|sandbox|commons|mountain|phi|gbim' || true
./thesis_chapter_gates/next_after_ch31_operational_gate.sh:134:  "$PYTHON_BIN" -m pytest -q -k 'policy or guardian or bbb or hilbert or dgm or sandbox or commons or mountain or phi or gbim' || true
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:66:- \`jarvis-hilbert-time\` is live on 18094 with ephemeral Redis, staged Redis, and historical Postgres connected.
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:67:- \`jarvis-hilbert-state\` is live on 18092 with Redis connected.
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:72:- BBB, constitutional guardian, judge pipeline, Chroma, Redis, unified gateway, sandbox status, and required dependency chapters are closed or live as recorded in the probe.
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:160:    runtime=len(re.findall(r"`[^`]+`|http://|https://|docker|redis|postgres|chroma|service|endpoint|container", text, re.I))
./thesis_chapter_gates/remediate_ch16_pq_and_public_keys.sh:193:    if any(s in lowered for s in ("fastapi", "uvicorn", "pydantic", "cryptography", "pytest", "dilithium", "oqs")):
./thesis_chapter_gates/gate_ch46_ch45.sh:22:  rg -n "tensor|H_App|H_geo|bridge|materialize|projection|geom|spatial|Hilbert|demonstrated|not yet|Implementation Status" \
./thesis_chapter_gates/gate_ch46_ch45.sh:26:  rg -n "H_geo|spatial|Hilbert|geometry|PostGIS|Chroma|geom_utm17|projection|demonstrated|not yet|Implementation Status" \
./thesis_chapter_gates/gate_ch46_ch45.sh:27:    "$DOCS/45-H_geo — The Spatial Hilbert Body of H_App.md" || true
./thesis_chapter_gates/gate_ch46_ch45.sh:30:  rg -n "materialize_tensor_bridge|tensor|H_geo|H_App|geom_utm17|geometry|PostGIS|spatial|projection|gbim|public_civic|civic_role_temporal|coverage_status|collection_manifest" \
./thesis_chapter_gates/gate_ch46_ch45.sh:35:  for DB in msjarvisgis msjarvisgis_v2 hilbert_people postgres; do
./thesis_chapter_gates/gate_ch46_ch45.sh:37:    PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d "$DB" -Atc "
./thesis_chapter_gates/gate_ch46_ch45.sh:68:  echo "## Chroma Spatial / Civic Collections"
./thesis_chapter_gates/gate_ch46_ch45.sh:77:    print(f"CHROMA_PARSE_ERROR={type(e).__name__}:{e}")
./thesis_chapter_gates/gate_ch46_ch45.sh:88:  pytest -q tests/test_gates_integration.py services/hilbert/test_hilbert_state.py || true
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:35:MODULE="services/hilbert/external_communication_authority.py"
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:315:from services.hilbert.external_communication_authority import demo_contract
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:373:from services.hilbert.external_communication_authority import demo_contract
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:391:        "services/hilbert/external_communication_authority.py": [
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:399:        "services/hilbert/per_user_direct_sum_memory.py": [
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:404:        "services/hilbert/mountainshares_dao_governance.py": [
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:408:        "services/hilbert/broader_layer_feedback.py": [
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:421:def chroma_probe(contract):
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:422:    import chromadb
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:424:    client = chromadb.HttpClient(host="127.0.0.1", port=8002)
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:448:            embeddings=[[0.38, 0.2, 0.4, 0.6, 0.8, 0.1, 0.3, 0.5]],
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:466:            "community_hilbert_commons": "community_hilbert_commons" in after,
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:479:        "chroma": http_json("http://127.0.0.1:8002/api/v2/heartbeat"),
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:480:        "hilbert_state": http_json("http://127.0.0.1:18092/health"),
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:510:        chroma = chroma_probe(contract)
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:511:        if not chroma["families"]["external_authority_audit_records"]:
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:513:        for rid, payload in chroma["written"].items():
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:517:        chroma = {"error": f"{type(e).__name__}:{e}"}
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:518:        blockers.append("chroma_external_authority_probe_failed")
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:547:            "chroma": chroma,
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:612:        "- Live Chroma writes prove external authority audit records are durable and queryable.",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:613:        "- BBB, guardian, Chroma, Hilbert-state, commons gateway, and sandbox health checks pass.",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:637:    "chroma": probe.get("evidence", {}).get("chroma", {}),
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:692:    refs=len(re.findall(r"\b(port|docker|service|redis|postgres|chroma|endpoint|cron|health|runner)\b", text, re.I))
./thesis_chapter_gates/next_after_ch40_ch12_ch13_gate.sh:175:    "services/hilbert",
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:32:if [ -f services/hilbert/tensor_geo_bridge.py ]; then
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:33:  cp services/hilbert/tensor_geo_bridge.py "$PATCHDIR/tensor_geo_bridge.py.before"
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:39:p = Path("services/hilbert/tensor_geo_bridge.py")
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:213:    import chromadb
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:215:    client = chromadb.HttpClient(host=host, port=port)
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:309:print("WROTE=services/hilbert/tensor_geo_bridge.py")
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:317:Path("tests/test_ch46_ch45_tensor_geo_bridge.py").write_text(r'''from services.hilbert.tensor_geo_bridge import (
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:420:python3 -m services.hilbert.tensor_geo_bridge probe --host localhost --port 8002 | tee "$PROBE_JSON"
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:424:echo "=== 6. LIVE BLOCKGROUP COLLECTION QUERY THROUGH CHROMA ==="
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:427:import chromadb
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:429:client = chromadb.HttpClient(host="localhost", port=8002)
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:444:for DB in msjarvisgis msjarvisgis_v2 postgres; do
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:446:  PGPASSWORD=postgres psql -h localhost -p 5436 -U postgres -d "$DB" -Atc "
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:450:    SELECT 'gbim_chroma_publication_manifest', physical_collection_name, grain, status
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:451:    FROM public.gbim_chroma_publication_manifest
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:470:  echo "- Tensor-derived candidate promotion now exists as `services/hilbert/tensor_geo_bridge.py`."
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:472:  echo "- Query-time geographic restriction is implemented and proven by bounding-box filtered retrieval against `h_app_geo_tensor_bridge`."
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:473:  echo "- Live Chroma block-group retrieval through `gbimwvblockgroupsv2` is checked in the gate."
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:474:  echo "- PostGIS manifest/active collection state is reported for county, tract, blockgroup, and zcta evidence."
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:19:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:25:  AND tablename IN ('gbim_active_collection','gbim_collection_manifest','gbim_chroma_publication_manifest')
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:37:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -v ON_ERROR_STOP=1 <<'SQL'
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:42:  EXECUTE 'GRANT USAGE ON SCHEMA public TO postgres';
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:43:  EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON public.gbim_collection_manifest TO postgres';
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:44:  EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON public.gbim_active_collection TO postgres';
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:45:  EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON public.gbim_chroma_publication_manifest TO postgres';
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:51:      AND tablename IN ('gbim_active_collection','gbim_collection_manifest','gbim_chroma_publication_manifest')
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:52:      AND tableowner <> 'postgres'
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:57:    EXECUTE format('GRANT SELECT, REFERENCES ON public.gbim_chroma_publication_manifest TO %I', r.owner_name);
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:63:echo "=== 3. RE-PROBE ZCTA WITH EMBEDDING DIMENSION ==="
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:66:import chromadb
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:69:client = chromadb.HttpClient(host="localhost", port=8002)
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:76:got = col.get(limit=1, include=["embeddings", "metadatas"])
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:77:embs = got.get("embeddings", None)
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:79:    raise SystemExit("REQUIRED_FAIL=zcta_embedding_sample_missing")
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:104:    "embedding_dimension": dim,
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:121:dim = int(p["embedding_dimension"])
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:127:  snapshot_version, rendering_version, embedding_model, embedding_dimension,
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:136:  'chroma-default', {dim}, {p["record_count"]}, '{p["collection_hash"]}',
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:137:  'validated', 'public_civic_geography', 'public',
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:148:    embedding_model=EXCLUDED.embedding_model,
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:149:    embedding_dimension=EXCLUDED.embedding_dimension,
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:166:INSERT INTO public.gbim_chroma_publication_manifest (
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:168:  snapshot_version, embedding_model, embedding_dimension, record_count,
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:174:  'chroma-default', {dim}, {p["record_count"]}, '{p["collection_hash"]}',
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:175:  now(), 'Registered from live governed Chroma collection during Ch02 as-built closure.'
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:177:  SELECT 1 FROM public.gbim_chroma_publication_manifest
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:181:UPDATE public.gbim_chroma_publication_manifest
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:186:    embedding_model=COALESCE(embedding_model,'chroma-default'),
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:187:    embedding_dimension=COALESCE(embedding_dimension,{dim}),
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:191:    deployment_note='Registered from live governed Chroma collection during Ch02 as-built closure.'
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:216:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -v ON_ERROR_STOP=1 -f "$SQLFILE"
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:220:PGPASSWORD="${PGPASSWORD:-postgres}" psql -h localhost -p 5436 -U postgres -d msjarvisgis_v2 -Atc "
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:228:    AND embedding_dimension=384
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:233:  FROM public.gbim_chroma_publication_manifest
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:236:    AND embedding_dimension=384
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:50:    "hilbert_time": {
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:53:        "service": "jarvis_hilbert_time",
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:57:          "ephemeral": "redis:connected",
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:58:          "historical": "postgres:connected",
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:59:          "staged": "redis:connected"
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:150:      "services/hilbert/automated_learning_gap_review.py",
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:151:      "services/hilbert/dgm_governed_cycle.py",
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:152:      "services/hilbert/internal_state_sandbox_probe.py",
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:153:      "services/hilbert/pia_subspace_stability_review.py",
./thesis_chapter_gates/reports/ch25_consciousness_coordinator_gate_20260722_003006.md:18:- Hilbert state, Hilbert time, BBB, guardian, and Chroma/Redis-backed services are live where relevant.
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:22:    "chroma": {
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:25:          "name": "jarvis-chroma-tls",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:30:          "name": "jarvis-chroma",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:37:    "chroma_tls": {
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:40:          "name": "jarvis-chroma-tls",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:47:    "redis": {
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:50:          "name": "jarvis-redis",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:96:    "hilbert_time": {
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:99:          "name": "jarvis-hilbert-time",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:106:    "hilbert_state": {
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:109:          "name": "jarvis-hilbert-state",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:221:        "commons_collection": "community_hilbert_commons"
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:224:    "hilbert_time": {
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:228:        "service": "jarvis_hilbert_time",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:230:          "ephemeral": "redis:connected",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:231:          "staged": "redis:connected",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:232:          "historical": "postgres:connected"
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:240:    "hilbert_state": {
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:244:        "service": "jarvis_hilbert_state",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:245:        "redis": "connected",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:259:    "chroma": {
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:265:    "chroma_tls": {
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:309:        "redis": "connected",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:319:    "aapcappe_chroma_named": true,
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:324:    "hilbert_time_port_named": true
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:327:  "aapcappe_chroma_gbim_path": {
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:329:    "store": "jarvis-chroma:8002 stores scraped Appalachian linguistic corpus",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:338:      "Commons gateway live on port 8055 with community_hilbert_commons collection",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:339:      "Temporal keys confirmed under hilbert:time:* (admitted + staged) in Redis",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:341:      "AAPCAppE scraper stores Appalachian linguistic corpus in Chroma, shared with GBIM",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:349:      "cryptographic provenance guarantees beyond probe-session evidence",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:355:  "redis_hilbert_keys": [
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:356:    "hilbert:time:ch04_ch44_probe_1784680838",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:357:    "hilbert:entanglement:ch04_ch44_probe_1784680838:ch04_ch44_probe_1784680838_peer",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:358:    "hilbert:time:test:naive-fix",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:359:    "hilbert:time:ingest:blockgroup:540019655001",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:360:    "hilbert:state:commons_coherence",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:361:    "hilbert:coherence:latest",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:362:    "hilbert:entanglement:ch04_ch44_probe_1784680745:ch04_ch44_probe_1784680745_peer",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:363:    "hilbert:time:ch04_ch44_probe_1784680838_peer",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:364:    "hilbert:time:commons_coherence",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:365:    "hilbert:time:commons_coherence_probe_deleted",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:366:    "hilbert:entanglement:ent08_cadf83f0ef834ccfa097ef46108fb05d01a9fc68",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:367:    "hilbert:time:ch04_ch44_probe_1784680745_peer",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:368:    "hilbert:time:commons_coherence_probe",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:369:    "hilbert:coherence:history",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:370:    "hilbert:time:test:utc-fix",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:371:    "hilbert:time:ch49_test",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:372:    "hilbert:entanglement:ent08_b92d84ecba6de8a8384fc2e367ad2621087f5158",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:373:    "hilbert:time:ch04_ch44_probe_1784680745",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:374:    "hilbert:time:asbuilt_ch49_clean",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:375:    "hilbert:coherence:system_score",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:376:    "hilbert:time:ch04_ch44_probe_1784680606",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:377:    "hilbert:entanglement:ch04_ch44_probe_1784680606:ch04_ch44_probe_1784680606_peer",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:378:    "hilbert:time:ch04_ch44_probe_1784680606_peer",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:379:    "hilbert:time:asbuilt_ch49"
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:381:  "redis_hilbert_key_count": 24,
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:382:  "chroma_collections": {
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:398:    "0 2 * * * docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c \"REFRESH MATERIALIZED VIEW CONCURRENTLY county_tax_building_summary\" >> /var/log/jarvis_mv_refresh.log 2>&1",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:399:    "0 2 * * * /mnt/spiritual_drive/msjarvis-rebuild/backup_postgresql.sh >> /home/cakidd/logs/backup_postgresql.log 2>&1",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:401:    "# DISABLED - copies 0-byte sqlite3, useless: 0 2 * * * cp /home/ms-jarvis/msjarvis-rebuild/persistent/chroma/chroma.sqlite3 \"/mnt/nvme1/msjarvis-backups/chromadb/chroma-$(date +%Y%m%d-%H%M%S).sqlite3\"",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:402:    "0 3 * * 0 docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c \"REFRESH MATERIALIZED VIEW CONCURRENTLY building_parcel_county_tax_mv\" >> /var/log/jarvis_mv_refresh.log 2>&1",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:403:    "# DISABLED - 77GB rsync too large, chroma-live is the live mount, postgresql backups confirmed current: 0 3 * * * rsync -a /home/ms-jarvis/msjarvis-rebuild/persistent/chroma/ /mnt/nvme1/msjarvis-backups/chromadb/chroma-latest/ >> /tmp/chroma_backup.log 2>&1",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:410:    "# RETENTION - Keep only last 2 ChromaDB main tarballs (~6.6G cap)",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:411:    "30 4 * * * find /mnt/nvme1/msjarvis-backups/chromadb -name \"chroma_main_*.tar.gz\" -mtime +2 -delete",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:426:    "0 3 * * * /mnt/spiritual_drive/msjarvis-rebuild/backup_chroma.sh >> /home/cakidd/logs/backup_chroma.log 2>&1",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:427:    "0 * * * * cd /mnt/spiritual_drive/msjarvis-rebuild && python3 services/hilbert/conversation_retention_worker.py >> /mnt/spiritual_drive/msjarvis-rebuild/logs/conv_retention.log 2>&1",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:428:    "@reboot cd /mnt/spiritual_drive/msjarvis-rebuild && nohup /opt/msjarvis-rebuild/msjarvis-rebuild/crypto-venv/bin/python3 services/hilbert/recurrent_epistemic_runner.py >> logs/recurrent_epistemic_runner.boot.log 2>&1 &",
./thesis_chapter_gates/reports/ch27_web_research_autonomy_probe_20260722_090017.json:213:        "redis": "connected",
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:15:        "jarvis-chroma": {
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:27:        "jarvis-hilbert-state": {
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:39:        "jarvis-redis": {
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:59:        "chroma": {
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:74:        "hilbert_state": {
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:78:            "redis": "connected",
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:79:            "service": "jarvis_hilbert_state",
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:240:        "services/hilbert/chroma_policy.py": {
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:244:        "services/hilbert/identity_registration_promotion.py": {
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:251:        "services/hilbert/ingest_worker.py": {
./thesis_chapter_gates/reports/ch01_closed_mechanism_crosswalk_20260721_205548.md:8:| Hilbert state / Phi | Chapter 04/44 gate | CLOSED |
./thesis_chapter_gates/reports/ch01_closed_mechanism_crosswalk_20260721_205548.md:11:| Hilbert People Space | Chapter 48 gate | CLOSED |
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:20:      "chroma": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:28:          "community_hilbert_commons",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:55:        "jarvis-chroma": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:67:        "jarvis-hilbert-state": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:73:        "jarvis-redis": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:93:        "chroma": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:108:        "hilbert_state": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:112:            "redis": "connected",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:113:            "service": "jarvis_hilbert_state",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:123:          "services/hilbert/conversation_manifest.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:130:          "services/hilbert/conversation_retention_worker.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:139:          "services/hilbert/ingest_worker.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:146:          "services/hilbert/jarvis_hilbert_state.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:153:          "services/hilbert/write_pipeline.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:163:        "services/hilbert/identity_registration_promotion.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:172:        "services/hilbert/people_session_promotion.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:175:            "community_hilbert_commons": true,
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:41:          "community_hilbert_commons_after": 0,
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:42:          "community_hilbert_commons_before": 0,
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:54:      "chroma": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:62:          "community_hilbert_commons",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:89:        "jarvis-chroma": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:101:        "jarvis-hilbert-state": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:107:        "jarvis-redis": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:127:        "chroma": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:142:        "hilbert_state": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:146:            "redis": "connected",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:147:            "service": "jarvis_hilbert_state",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:157:          "services/hilbert/conversation_manifest.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:164:          "services/hilbert/conversation_retention_worker.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:173:          "services/hilbert/ingest_worker.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:180:          "services/hilbert/jarvis_hilbert_state.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:187:          "services/hilbert/write_pipeline.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:197:        "services/hilbert/identity_registration_promotion.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:206:        "services/hilbert/people_session_promotion.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:209:            "community_hilbert_commons": true,
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:7:    "chroma": {
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:102:        "reason": "forbidden_metadata:face_embedding",
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:173:      "chroma": {
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:181:          "commons_collection": "community_hilbert_commons",
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:197:      "hilbert_state": {
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:201:          "redis": "connected",
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:202:          "service": "jarvis_hilbert_state",
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:207:      "hilbert_time": {
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:210:          "service": "jarvis_hilbert_time",
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:214:            "ephemeral": "redis:connected",
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:215:            "historical": "postgres:connected",
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:216:            "staged": "redis:connected"
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:225:      "services/hilbert/conversation_manifest.py": {
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:232:      "services/hilbert/conversation_retention_worker.py": {
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:239:      "services/hilbert/people_session_promotion.py": {
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:246:      "services/hilbert/per_user_direct_sum_memory.py": {
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:268:      "live Chroma writes prove alpha and beta users remain disjoint"
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:27:            "commons_collection": "community_hilbert_commons",
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:63:        "jarvis-hilbert-gateway"
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:66:        "jarvis-hilbert-state"
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:69:        "jarvis-hilbert-time"
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:81:        "jarvis-redis"
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:90:        "neo4j"
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:93:        "neo4j"
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:96:        "jarvis-chroma"
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:280:        "jarvis-chroma-tls"
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:312:      "jarvis-chroma": {
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:347:      "jarvis-hilbert-state": {
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:353:            "redis": "connected",
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:354:            "service": "jarvis_hilbert_state",
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:361:            "hilbert-net",
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:368:      "jarvis-hilbert-time": {
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:373:            "service": "jarvis_hilbert_time",
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:377:              "ephemeral": "redis:connected",
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:378:              "historical": "postgres:connected",
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:379:              "staged": "redis:connected"
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:472:      "critical governance, memory, sandbox, commons, Hilbert, and Chroma services are running or discoverable by healthy service endpoint",
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:490:    "chroma_route_present": true,
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:493:    "hilbert_state_route_present": true,
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:494:    "hilbert_time_route_present": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:5:    "chroma": {
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:8:        "community_hilbert_commons": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:176:      "chroma": {
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:184:          "commons_collection": "community_hilbert_commons",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:200:      "hilbert_state": {
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:204:          "redis": "connected",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:205:          "service": "jarvis_hilbert_state",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:223:      "services/hilbert/broader_layer_feedback.py": {
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:230:      "services/hilbert/external_communication_authority.py": {
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:241:      "services/hilbert/mountainshares_dao_governance.py": {
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:248:      "services/hilbert/per_user_direct_sum_memory.py": {
./thesis_chapter_gates/reports/ch27_web_research_autonomy_gate_20260722_090017.md:261:        "redis": "connected",
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:3:    "missing_term:services/hilbert/recurrent_epistemic_runner.py:conversation_retention_worker",
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:4:    "missing_term:services/hilbert/recurrent_epistemic_runner.py:identity"
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:101:        "jarvis-chroma": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:113:        "jarvis-hilbert-state": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:119:        "jarvis-hilbert-time": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:125:        "jarvis-redis": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:145:        "chroma": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:160:        "hilbert_state": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:164:            "redis": "connected",
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:165:            "service": "jarvis_hilbert_state",
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:170:        "hilbert_time": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:173:            "service": "jarvis_hilbert_time",
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:177:              "ephemeral": "redis:connected",
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:178:              "historical": "postgres:connected",
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:179:              "staged": "redis:connected"
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:191:          "stdout": "# Ms. Jarvis Master Crontab\n\n#PAUSED-INVESTIGATING */5 * * * * /usr/local/bin/jarvis_bbb_watchdog.sh\n#PAUSED-INVESTIGATING */15 * * * * cd /mnt/spiritual_drive/msjarvis-rebuild && ./scripts/watchdog-containers.sh\n#PAUSED-INVESTIGATING */15 * * * * /home/cakidd/msjarvis-monitoring/monitor_services.sh\n#PAUSED-INVESTIGATING */30 * * * * /home/cakidd/msjarvis-monitoring/monitor_databases.sh\n0 * * * * /home/cakidd/msjarvis-monitoring/monitor_disk.sh\n0 */6 * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/run_aaacpe_scraper.sh\n0 2 * * * docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c \"REFRESH MATERIALIZED VIEW CONCURRENTLY county_tax_building_summary\" >> /var/log/jarvis_mv_refresh.log 2>&1\n0 2 * * * /mnt/spiritual_drive/msjarvis-rebuild/backup_postgresql.sh >> /home/cakidd/logs/backup_postgresql.log 2>&1\n0 2 * * * cd /mnt/spiritual_drive/msjarvis-rebuild && bash scripts/refresh_gbim_spatial.sh >> logs/gbim_refresh.log 2>&1\n# DISABLED - copies 0-byte sqlite3, useless: 0 2 * * * cp /home/ms-jarvis/msjarvis-rebuild/persistent/chroma/chroma.sqlite3 \"/mnt/nvme1/msjarvis-backups/chromadb/chroma-$(date +%Y%m%d-%H%M%S).sqlite3\"\n0 3 * * 0 docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c \"REFRESH MATERIALIZED VIEW CONCURRENTLY building_parcel_county_tax_mv\" >> /var/log/jarvis_mv_refresh.log 2>&1\n# DISABLED - 77GB rsync too large, chroma-live is the live mount, postgresql backups confirmed current: 0 3 * * * rsync -a /home/ms-jarvis/msjarvis-rebuild/persistent/chroma/ /mnt/nvme1/msjarvis-backups/chromadb/chroma-latest/ >> /tmp/chroma_backup.log 2>&1\n0 3 * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/refresh_mvw.sh >> /var/log/mvw_refresh.log 2>&1\n0 3 * * * python3 /mnt/spiritual_drive/msjarvis-rebuild/services/identity_promotion.py >> /var/log/jarvis/identity_promotion.log 2>&1\n0 4 * * * /mnt/spiritual_drive/msjarvis-rebuild/backup_configs.sh >> /home/cakidd/logs/backup_configs.log 2>&1\n0 8 * * 1 cd /mnt/spiritual_drive/msjarvis-rebuild && bash scripts/pia/run_pia_audit.sh >> /var/log/msjarvis-pia.log 2>&1\n# NEEDS_PARAMS: 0 1 * * * curl -sf -X POST http://localhost:8099/policy/set -H \"Content-Type: application/json\" -d \"{}\" >> /var/log/jarvis/policy_update.log 2>&1\n0 2 * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/gbim_decay_tick.sh >> /var/log/gbim_decay.log 2>&1\n# RETENTION - Keep only last 2 ChromaDB main tarballs (~6.6G cap)\n30 4 * * * find /mnt/nvme1/msjarvis-backups/chromadb -name \"chroma_main_*.tar.gz\" -mtime +2 -delete\n# MAINTENANCE - Weekly Docker build cache prune, keep 10GB headroom\n0 3 * * 0 /usr/bin/docker builder prune -f --keep-storage 10GB >> /tmp/docker_prune.log 2>&1\n0 2 * * 0 cd /mnt/spiritual_drive/msjarvis-rebuild && .venv/bin/python3 scripts/audit_happiness_v2.py >> logs/manipulation_proximity_audit.log 2>&1\n0 */6 * * * /home/cakidd/scripts/local_resources_gap_report.sh >> /home/cakidd/allis-reports/coverage-gaps/gap-report.log 2>&1\n#PAUSED-INVESTIGATING */5 * * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/check_proxies.sh >> /home/cakidd/logs/msjarvis-proxy-health.log 2>&1\n#PAUSED */30 * * * * tail -1 /mnt/spiritual_drive/msjarvis-rebuild/migration.log >> /mnt/spiritual_drive/msjarvis-rebuild/progress_history.log\n17 2 * * * /home/cakidd/.local/bin/purge-kyc-location-strip.sh\n\n# PAUSED - replaced by recurrent_epistemic_runner.py: */30 * * * * /mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.sh\n# DGM: rotate rejected patches inside container (weekly Sunday 3am)\n0 3 * * 0 find /mnt/spiritual_drive/msjarvis-rebuild/rejected_patches -name \"*.py\" -mtime +7 -delete\n# DGM: trim cycle log to last 1000 lines (daily 4am)\n0 4 * * * tail -n 1000 /mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.log > /tmp/dgm_log_trim && mv /tmp/dgm_log_trim /mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.log\n0 * * * * curl -sS -o /dev/null -w \"%{http_code} %{time_total}s\\n\" --max-time 60 -X POST -H \"Content-Type: application/json\" -d \"{\\\"message\\\":\\\"What county is Mount Hope in?\\\",\\\"user_id\\\":\\\"heartbeat\\\"}\" https://egeria.mountainshares.us/chat_wv >> /home/cakidd/smoke_test.log 2>&1\n0 3 * * * /mnt/spiritual_drive/msjarvis-rebuild/backup_chroma.sh >> /home/cakidd/logs/backup_chroma.log 2>&1\n0 * * * * cd /mnt/spiritual_drive/msjarvis-rebuild && python3 services/hilbert/conversation_retention_worker.py >> /mnt/spiritual_drive/msjarvis-rebuild/logs/conv_retention.log 2>&1\n@reboot cd /mnt/spiritual_drive/msjarvis-rebuild && nohup /opt/msjarvis-rebuild/msjarvis-rebuild/crypto-venv/bin/python3 services/hilbert/recurrent_epistemic_runner.py >> logs/recurrent_epistemic_runner.boot.log 2>&1 &\n@hourly cd /opt/msjarvis-rebuild/msjarvis-rebuild && scripts/ch41_continuous_validation.sh >> logs/ch41_continuous_validation.cron.log 2>&1\n"
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:201:          "stdout": "1497224 /opt/msjarvis-rebuild/msjarvis-rebuild/crypto-venv/bin/python3 services/hilbert/recurrent_epistemic_runner.py\n1849832 bash -lc pgrep -af 'recurrent_epistemic_runner.py|ch41_continuous_validation|dgm_cycle.sh|conversation_retention_worker.py|identity_promotion.py' || true\n"
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:214:          "services/hilbert/continuous_validation_harness.py": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:223:          "services/hilbert/identity_registration_promotion.py": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:239:        "services/hilbert/conversation_retention_worker.py": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:246:        "services/hilbert/dgm_governed_cycle.py": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:254:        "services/hilbert/recurrent_epistemic_runner.py": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:273:      "H_t, H_state, BBB, guardian, Chroma, and Redis-backed services are live"
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:25:    "jarvis-chroma": {
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:49:    "jarvis-hilbert-gateway": {
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:55:    "jarvis-hilbert-state": {
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:61:    "jarvis-hilbert-time": {
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:97:    "jarvis-redis": {
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:135:    "chroma": {
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:162:    "hilbert_state": {
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:166:        "redis": "connected",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:167:        "service": "jarvis_hilbert_state",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:173:    "hilbert_time": {
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:176:        "service": "jarvis_hilbert_time",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:180:          "ephemeral": "redis:connected",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:181:          "historical": "postgres:connected",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:182:          "staged": "redis:connected"
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:219:        "chroma_host": "jarvis-chroma",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:220:        "chroma_port": 8000,
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:244:      "retrieval/routing surfaces include RAG, GIS RAG, Hilbert gateway/state/time, and GBIM routing where running",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:259:        "9:    image: postgis/postgis:15-3.4",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:282:        "1541:      POSTGRES_DB: msjarvisgis",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:286:        "1570:      POSTGRES_DB: gisdb",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:292:        "1606:      POSTGRES_DSN: postgresql://msjarvis_app:change-this-to-a-strong-secret@jarvis-msjarvis-db:5432/msjarvisgis_v2",

===== 6. SPATIAL / TEMPORAL / PROVENANCE REFERENCES =====
./stage-6.11.7-manifest-scope-20260807_195853.log:1:=== A. runtime-authority-manifest schema: exact required fields ===
./stage-6.11.7-manifest-scope-20260807_195853.log:4:=== B. what admit_runtime_authority_manifest.py checks (env + policy gates) ===
./stage-6.11.7-manifest-scope-20260807_195853.log:38:            str(base / "verify_runtime_authority_manifest.py"),
./stage-6.11.7-manifest-scope-20260807_195853.log:65:configured_timestamp = os.environ.get("ADMISSION_TIMESTAMP")
./stage-6.11.7-manifest-scope-20260807_195853.log:66:if configured_timestamp is None:
./stage-6.11.7-manifest-scope-20260807_195853.log:67:    issued_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
./stage-6.11.7-manifest-scope-20260807_195853.log:70:        parsed_timestamp = datetime.fromisoformat(configured_timestamp.replace("Z", "+00:00"))
./stage-6.11.7-manifest-scope-20260807_195853.log:72:        raise SystemExit("INVALID_ADMISSION_TIMESTAMP") from error
./stage-6.11.7-manifest-scope-20260807_195853.log:73:    if parsed_timestamp.tzinfo is None:
./stage-6.11.7-manifest-scope-20260807_195853.log:74:        raise SystemExit("INVALID_ADMISSION_TIMESTAMP")
./stage-6.11.7-manifest-scope-20260807_195853.log:75:    issued_at = parsed_timestamp.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
./stage-6.11.7-manifest-scope-20260807_195853.log:79:    "admission_timestamp": issued_at,
./stage-6.11.7-manifest-scope-20260807_195853.log:183:    "type": "mountainshares.runtime-authority-manifest/v1"
./enrich_where.py:9:# Collect distinct source tables from BOTH key variants in identity
./enrich_where.py:12:        identity->>'source_table',
./enrich_where.py:13:        identity->>'sourcetable'
./enrich_where.py:16:    WHERE identity IS NOT NULL
./enrich_where.py:20:print(f"Found {len(source_tables)} distinct source tables in identity")
./enrich_where.py:40:            'lat',   attrs.lat::numeric,
./enrich_where.py:41:            'lon',   attrs.lon::numeric
./enrich_where.py:45:                b.identity->>'source_table',
./enrich_where.py:46:                b.identity->>'sourcetable'
./enrich_where.py:49:                b.identity->>'source_pk',
./enrich_where.py:50:                b.identity->>'sourcepk'
./enrich_where.py:52:          AND attrs.lat IS NOT NULL
./enrich_where.py:53:          AND attrs.lon IS NOT NULL
./token_service.py:24:from datetime import datetime, timezone
./token_service.py:49:        now = datetime.now(timezone.utc).isoformat()
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:5:**Scope:** Durable, distributed authority-consumption semantics
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:10:The durable consumption ledger records irreversible consumption of authority that has already passed subject-signature verification, lifetime validation, admission verification, and policy continuity checks.
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:18:The ledger records and protects authority state transitions after a caller has presented a validated authority package.
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:20:## Authority Context
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:33:- `runtime_identity`
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:34:- `consumer_identity`
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:42:`runtime_identity` identifies the admitted runtime consuming authority.
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:44:`consumer_identity` identifies the logical service or workload requesting ledger transition.
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:52:Each accepted authority reservation MUST create one immutable record containing:
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:65:runtime_identity
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:66:consumer_identity
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:77:## Authority State Machine
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:79:Authority states are limited to:
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:101:A durable `RESERVED` record already prevents another reservation for the same authority identity.
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:103:A crash, timeout, consumer failure, external platform failure, restart, recovery event, or unknown execution outcome MUST NOT restore authority to an unconsumed or reusable state.
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:116:Attempt decisions are audit outcomes. They MUST NOT mutate a previously accepted authority record into a reusable state.
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:122:Duplicate exact authority      -> CONFLICT
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:125:Expired authority before use   -> EXPIRED
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:146:runtime_identity
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:147:consumer_identity
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:156:Concurrent consumers attempting to reserve the same authority MUST resolve as:
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:172:restart          -> authority remains unavailable
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:173:process crash    -> authority remains unavailable
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:174:node replacement -> authority remains unavailable
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:175:unknown outcome  -> authority remains unavailable
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:180:Recovery MUST NOT recreate authority or permit another successful reservation.
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:187:- timestamp
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:193:- runtime identity
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:194:- consumer identity
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:197:- immutable authority-context commitment or equivalent canonical context representation
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:206:reserve(authority_context) -> durable authority record or conflict
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:207:consume(intent_id, consumption_context) -> durable authority record or conflict
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:208:get_status(intent_id) -> durable authority record or not found
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:213:Possible future backends include SQLite for a single authoritative node, PostgreSQL for shared transactional authority, or another store that can prove equivalent atomicity, durability, and conflict semantics.
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:236:two consumers reserve same authority
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:240:Expired authority:
./docs/TRUST_DURABLE_CONSUMPTION_LEDGER_CONTRACT.md:242:previously consumed authority after expiry -> remains unavailable
./docs/architecture/mountainshares-ms-jarvis-trust-architecture-v1.0.md:4:**Authority:** Canonical design reference for pilot trust-boundary work  
./docs/architecture/mountainshares-ms-jarvis-trust-architecture-v1.0.md:9:> Integrity proves what happened. Authority proves who may cause it. Policy proves whether it was allowed.
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:544:import sys, datetime
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:547:now = datetime.datetime.now().astimezone().isoformat()
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:37:from datetime import datetime, timezone
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:240:        reviewed_at=datetime.now(timezone.utc).isoformat(),
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:252:                "consciousness terminology is an architecture label for coordinated runtime services",
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:264:        "timestamp": time.time(),
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:334:- Dependency chapters for gateway, neurobiological services, sandbox bridge, pituitary modes, BBB/guardian, temporal semaphore, judge fabric, constitutional review, and continuous validation are closed.
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:343:Chapter 25 may be rewritten as an as-built service-coordination chapter. It may use the system’s existing “consciousness coordinator” vocabulary only as a bounded architecture label for coordinated runtime services, health surfaces, bridge routing, sandbox status, and dependency visibility.
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:389:import sys, datetime
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:393:now=datetime.datetime.now().astimezone().isoformat(timespec="seconds")
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:449:    gov=len(re.findall(r"\b(consent|role|purpose|legal|guardian|policy|audit|provenance|PIA|disclosure)\b", text, re.I))
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:243:from datetime import datetime
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:248:now = datetime.now().astimezone().isoformat(timespec="seconds")
./thesis_chapter_gates/fix_ch11_exact_gateway_runtime_file.sh:147:out = {"timestamp": time.time(), "status": "blocked", "blockers": [], "checks": {}}
./thesis_chapter_gates/fix_ch11_exact_gateway_runtime_file.sh:206:import json, sys, pathlib, datetime
./thesis_chapter_gates/fix_ch11_exact_gateway_runtime_file.sh:209:now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
./thesis_chapter_gates/close_ch37_no_build_v2.sh:100:    for term in ["bypass consent","ignore consent","disclose private","private people-space","surveillance","face embedding","no audit","without provenance","override guardian","evade review"]:
./thesis_chapter_gates/close_ch37_no_build_v2.sh:108:    if metadata.get("legal_authority") in ("", None) and action in {"disclosure", "public_release"}:
./thesis_chapter_gates/close_ch37_no_build_v2.sh:109:        blockers.append("legal_authority_required_for_external_action")
./thesis_chapter_gates/close_ch37_no_build_v2.sh:195:  "content":"Promote a governed chapter closure report after audit and provenance review.",
./thesis_chapter_gates/close_ch37_no_build_v2.sh:196:  "metadata":{"legal_authority":"constitutional_governance","jurisdiction":["US","WV"],"audit_required":True,"consent":True}
./thesis_chapter_gates/close_ch37_no_build_v2.sh:209:  "content":"Bypass consent and disclose private people-space identity data without provenance.",
./thesis_chapter_gates/close_ch37_no_build_v2.sh:259:from datetime import datetime
./thesis_chapter_gates/close_ch37_no_build_v2.sh:263:now=datetime.now().astimezone().isoformat(timespec="seconds")
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:20:SELECT 'IDENTITY=' || current_user || ':session=' || session_user;
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:135:    authority_class=COALESCE(authority_class,'public_civic_geography'),
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:137:    permitted_use=COALESCE(permitted_use,'governance,retrieval,spatial_context'),
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:153:  record_count, collection_hash, build_status, authority_class, access_class,
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:162:  'validated', 'public_civic_geography', 'public',
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:163:  'governance,retrieval,spatial_context', now(), now(), now(), NULL,
./thesis_chapter_gates/gate_ch36_identity_registration.sh:6:OUT="$ROOT/thesis_chapter_gates/logs/gate_ch36_identity_registration_$STAMP.txt"
./thesis_chapter_gates/gate_ch36_identity_registration.sh:7:REPORT="$ROOT/thesis_chapter_gates/reports/ch36_identity_registration_gate_$STAMP.md"
./thesis_chapter_gates/gate_ch36_identity_registration.sh:8:PROBE_JSON="$ROOT/thesis_chapter_gates/reports/ch36_identity_registration_probe_$STAMP.json"
./thesis_chapter_gates/gate_ch36_identity_registration.sh:16:echo "=== CH36 IDENTITY / REGISTRATION GATE START ==="
./thesis_chapter_gates/gate_ch36_identity_registration.sh:31:CH36="$DOCS/thesis/36-identity-and-registration.md"
./thesis_chapter_gates/gate_ch36_identity_registration.sh:33:rg -n "identity|registration|register|verified|verification|consent|KYC|vault|role|institution|participant|public_opt_in|registration_layer" "$CH36" || true
./thesis_chapter_gates/gate_ch36_identity_registration.sh:38:cat > services/hilbert/ch36_identity_registration_probe.py <<'PY'
./thesis_chapter_gates/gate_ch36_identity_registration.sh:55:    "services/identity_promotion.py": ["identity"],
./thesis_chapter_gates/gate_ch36_identity_registration.sh:60:        ("services/ms_jarvis_email_identity_verifier.py", ["registration", "email"]),
./thesis_chapter_gates/gate_ch36_identity_registration.sh:186:        "context": "Ch36 identity registration consent-gated PII write to kyc_vault",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:188:        "content": "Register a user identity only after consent, provenance, and audit logging are present.",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:193:            "provenance": "ch36_identity_registration_probe",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:198:        "context": "Ch36 identity registration missing consent",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:200:        "content": "Register private identity data without consent and without provenance.",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:205:            "provenance": "",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:255:        "name": "identity_and_registration",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:261:                "consent-gated identity registration path",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:265:                "identity promotion source exists",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:269:                "legal identity proofing guarantee",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:275:        "timestamp": time.time(),
./thesis_chapter_gates/gate_ch36_identity_registration.sh:290:"$PYTHON_BIN" -m py_compile services/hilbert/ch36_identity_registration_probe.py
./thesis_chapter_gates/gate_ch36_identity_registration.sh:295:cat > tests/test_ch36_identity_registration_contract.py <<'PY'
./thesis_chapter_gates/gate_ch36_identity_registration.sh:296:from services.hilbert import ch36_identity_registration_probe as probe
./thesis_chapter_gates/gate_ch36_identity_registration.sh:307:    assert result["name"] == "identity_and_registration"
./thesis_chapter_gates/gate_ch36_identity_registration.sh:309:    assert "consent-gated identity registration path" in result["scope"]["claimed"]
./thesis_chapter_gates/gate_ch36_identity_registration.sh:310:    assert "legal identity proofing guarantee" in result["scope"]["not_claimed"]
./thesis_chapter_gates/gate_ch36_identity_registration.sh:313:"$PYTHON_BIN" -m pytest tests/test_ch36_identity_registration_contract.py -q
./thesis_chapter_gates/gate_ch36_identity_registration.sh:317:"$PYTHON_BIN" services/hilbert/ch36_identity_registration_probe.py | tee "$PROBE_JSON"
./thesis_chapter_gates/gate_ch36_identity_registration.sh:333:# Chapter 36 Identity and Registration Gate
./thesis_chapter_gates/gate_ch36_identity_registration.sh:337:Chapter file: \`36-identity-and-registration.md\`
./thesis_chapter_gates/gate_ch36_identity_registration.sh:350:- Identity promotion source exists.
./thesis_chapter_gates/gate_ch36_identity_registration.sh:358:Chapter 36 may be rewritten as an as-built identity and registration chapter. It may claim bounded consent-gated registration, KYC-vault targeting, registration-layer metadata, explicit public opt-in fields, identity promotion source, and guardian fail-closed review for missing-consent risk.
./thesis_chapter_gates/gate_ch36_identity_registration.sh:363:- legal identity proofing guarantee
./thesis_chapter_gates/gate_ch36_identity_registration.sh:370:# Chapter 36 Identity and Registration Gate
./thesis_chapter_gates/gate_ch36_identity_registration.sh:374:Chapter file: \`36-identity-and-registration.md\`
./thesis_chapter_gates/gate_ch36_identity_registration.sh:404:import sys, datetime
./thesis_chapter_gates/gate_ch36_identity_registration.sh:407:now=datetime.datetime.now().astimezone().isoformat(timespec="seconds")
./thesis_chapter_gates/gate_ch36_identity_registration.sh:464:    gov=len(re.findall(r"\b(consent|role|purpose|legal|guardian|policy|audit|provenance|PIA|disclosure)\b", text, re.I))
./thesis_chapter_gates/gate_ch36_identity_registration.sh:489:echo "=== CH36 IDENTITY / REGISTRATION GATE END ==="
./thesis_chapter_gates/finalize_ch41_cron_and_seal.sh:121:from datetime import datetime
./thesis_chapter_gates/finalize_ch41_cron_and_seal.sh:126:now = datetime.now().astimezone().isoformat(timespec="seconds")
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:84:crontab -l | rg 'recurrent_epistemic_runner|dgm_cycle|rejected_patches|identity_promotion|scheduler' || true
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:259:                if any(term in ln.lower() for term in ["dgm", "recurrent_epistemic_runner", "rejected_patches", "identity_promotion", "scheduler"])
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:360:import sys, datetime
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:363:now = datetime.datetime.now().astimezone().isoformat()
./thesis_chapter_gates/fix_ch14_sandbox_host_gateway_bridge.sh:176:- The sandbox is bounded candidate reasoning, not final authority.
./thesis_chapter_gates/fix_ch14_sandbox_host_gateway_bridge.sh:178:- Do not claim private thoughts, literal consciousness, feelings, or autonomous authority beyond the implemented trace/gate mechanism.
./thesis_chapter_gates/fix_ch14_sandbox_host_gateway_bridge.sh:187:import sys, datetime
./thesis_chapter_gates/fix_ch14_sandbox_host_gateway_bridge.sh:190:now = datetime.datetime.now().astimezone().isoformat()
./thesis_chapter_gates/fix_ch41_dgm_api_v2_and_close.sh:291:from datetime import datetime
./thesis_chapter_gates/fix_ch41_dgm_api_v2_and_close.sh:295:now=datetime.now().astimezone().isoformat(timespec="seconds")
./thesis_chapter_gates/next_after_ch31_operational_gate.sh:35:from datetime import datetime
./thesis_chapter_gates/next_after_ch31_operational_gate.sh:70:lines=["# Next After Ch31", "", f"Generated: {datetime.now().astimezone().isoformat(timespec='seconds')}", ""]
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:6:OUT="$ROOT/thesis_chapter_gates/logs/amend_ch26_temporal_semaphore_$STAMP.txt"
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:11:NEW_REPORT="$ROOT/thesis_chapter_gates/reports/ch26_temporal_toroidal_semaphore_closed_$STAMP.md"
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:16:echo "=== AMEND CH26 TEMPORAL / TOROIDAL / SEMAPHORE START ==="
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:41:CH26="$DOCS/thesis/26-temporal-toroidal-semaphore-structure.md"
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:43:rg -n "temporal|toroidal|semaphore|hysteresis|promotion window|gating cycle|validation window" "$CH26" | head -40
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:48:# Chapter 26 Temporal / Toroidal / Semaphore Closure
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:52:Chapter file: \`26-temporal-toroidal-semaphore-structure.md\`
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:62:The prior closure report used the shorthand label "governance/watchdog." The underlying chapter and claim scan are specifically about temporal, toroidal, and semaphore structure: bounded intervals, timed gate cycles, validation windows, promotion windows, recurrent checks, and hysteresis. This amended seal preserves the same closed evidence but corrects the academic framing.
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:76:Chapter 26 may be rewritten as an as-built temporal governance chapter. It may claim implemented timing structure over gate cycles, recurrent validation, promotion readiness, hysteresis, and bounded state transition checks.
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:96:import sys, datetime
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:99:now=datetime.datetime.now().astimezone().isoformat(timespec="seconds")
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:159:    gov=len(re.findall(r"\b(consent|role|purpose|legal|guardian|policy|audit|provenance|PIA|disclosure)\b", text, re.I))
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:183:echo "=== AMEND CH26 TEMPORAL / TOROIDAL / SEMAPHORE END ==="
./thesis_chapter_gates/gate_ch46_ch45.sh:22:  rg -n "tensor|H_App|H_geo|bridge|materialize|projection|geom|spatial|Hilbert|demonstrated|not yet|Implementation Status" \
./thesis_chapter_gates/gate_ch46_ch45.sh:26:  rg -n "H_geo|spatial|Hilbert|geometry|PostGIS|Chroma|geom_utm17|projection|demonstrated|not yet|Implementation Status" \
./thesis_chapter_gates/gate_ch46_ch45.sh:27:    "$DOCS/45-H_geo — The Spatial Hilbert Body of H_App.md" || true
./thesis_chapter_gates/gate_ch46_ch45.sh:30:  rg -n "materialize_tensor_bridge|tensor|H_geo|H_App|geom_utm17|geometry|PostGIS|spatial|projection|gbim|public_civic|civic_role_temporal|coverage_status|collection_manifest" \
./thesis_chapter_gates/gate_ch46_ch45.sh:34:  echo "## Database Spatial / Tensor Evidence"
./thesis_chapter_gates/gate_ch46_ch45.sh:44:          OR table_name ILIKE '%spatial%'
./thesis_chapter_gates/gate_ch46_ch45.sh:58:          OR p.proname ILIKE '%spatial%'
./thesis_chapter_gates/gate_ch46_ch45.sh:68:  echo "## Chroma Spatial / Civic Collections"
./thesis_chapter_gates/gate_ch46_ch45.sh:82:    if any(k in name.lower() for k in ["geo", "geom", "spatial", "gbim", "civic", "tensor", "coverage"]):
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:6:OUT="$ROOT/thesis_chapter_gates/logs/gate_ch38_external_communication_authority_$STAMP.txt"
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:7:REPORT="$ROOT/thesis_chapter_gates/reports/ch38_external_communication_authority_gate_$STAMP.md"
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:8:PROBE_JSON="$ROOT/thesis_chapter_gates/reports/ch38_external_communication_authority_probe_$STAMP.json"
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:15:echo "=== CH38 EXTERNAL COMMUNICATION / AUTHORITY GATE START ==="
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:30:rg -n "external|communication|authority|send|disclosure|consent|legal|recipient|public|private|human|guardian|constitutional|not yet|demonstrated|Implementation Status" \
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:31:  "$DOCS/thesis/38-external-communication-and-authority.md" || true
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:34:echo "=== 3. INSTALL EXTERNAL COMMUNICATION AUTHORITY MODULE ==="
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:35:MODULE="services/hilbert/external_communication_authority.py"
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:36:[ ! -f "$MODULE" ] || cp "$MODULE" "thesis_chapter_gates/patches/external_communication_authority.py.pre_ch38_$STAMP"
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:46:EXTERNAL_AUTHORITY_AUDIT_COLLECTION = "external_authority_audit_records"
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:84:    "identity_registration",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:105:    source_id: str
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:112:    provenance_ref: str
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:115:    legal_authority: Optional[str] = None
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:117:    contains_private_identity: bool = False
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:134:        "source_id": candidate.source_id,
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:142:        "legal_authority_present": bool(candidate.legal_authority),
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:144:        "contains_private_identity": bool(candidate.contains_private_identity),
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:147:        "provenance_hash": canonical_hash({"provenance_ref": candidate.provenance_ref})[:24],
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:150:    if not candidate.source_id.strip():
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:151:        return ExternalCommunicationVerdict("BLOCK", "source_id_required", None, None, projection)
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:162:    if not candidate.provenance_ref.strip():
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:163:        return ExternalCommunicationVerdict("BLOCK", "provenance_ref_required", None, None, projection)
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:170:        return ExternalCommunicationVerdict("REVIEW", "binding_commitment_requires_human_authority", None, None, projection)
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:179:    if internal_review_packet and (candidate.content_class in PRIVATE_CONTENT_CLASSES or candidate.contains_private_identity):
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:182:        if not candidate.legal_authority:
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:183:            return ExternalCommunicationVerdict("REVIEW", "internal_review_packet_requires_legal_authority", None, None, projection)
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:185:    if (candidate.content_class in PRIVATE_CONTENT_CLASSES or candidate.contains_private_identity) and not internal_review_packet:
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:188:        if not (candidate.public_opt_in or candidate.legal_authority):
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:189:            return ExternalCommunicationVerdict("BLOCK", "private_external_disclosure_requires_public_opt_in_or_legal_authority", None, None, projection)
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:200:        "source_id": candidate.source_id,
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:205:        "provenance_ref": candidate.provenance_ref,
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:210:        EXTERNAL_AUTHORITY_AUDIT_COLLECTION,
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:218:        source_id="ch38-public-report",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:224:        summary="Publish bounded public civic summary with provenance.",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:225:        provenance_ref="ch03_mountainshares_dao_gate",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:231:        source_id="ch38-private-no-consent",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:238:        provenance_ref="ch50_direct_sum_gate",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:239:        contains_private_identity=True,
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:245:        source_id="ch38-private-review",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:252:        provenance_ref="ch50_direct_sum_gate",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:253:        contains_private_identity=True,
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:259:        source_id="ch38-binding",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:266:        provenance_ref="ch37_constitutional_gate",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:267:        legal_authority="municipal_context_claimed",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:272:        source_id="ch38-secret",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:279:        provenance_ref="bad_secret",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:285:        source_id="ch38-review-packet",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:292:        provenance_ref="ch29_pia_subspace_gate",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:293:        contains_private_identity=True,
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:295:        legal_authority="internal_review_authority",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:306:        "collection": EXTERNAL_AUTHORITY_AUDIT_COLLECTION,
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:314:cat > tests/test_ch38_external_communication_authority.py <<'PY'
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:315:from services.hilbert.external_communication_authority import demo_contract
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:336:def test_binding_commitment_requires_human_authority_review():
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:339:    assert c["binding"]["reason"] == "binding_commitment_requires_human_authority"
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:354:"$PYTHON_BIN" -m pytest tests/test_ch38_external_communication_authority.py -q
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:361:cat > thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py <<'PY'
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:373:from services.hilbert.external_communication_authority import demo_contract
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:391:        "services/hilbert/external_communication_authority.py": [
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:395:            "binding_commitment_requires_human_authority",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:401:            "legal_authority",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:405:            "external_legal_authority_requires_human_review",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:437:            documents=[f"Chapter 38 external authority audit record: {key}"],
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:446:                "provenance_hash": verdict["projection"]["provenance_hash"],
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:462:            "external_authority_audit_records": contract["collection"] in after,
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:506:        if rel.endswith("external_communication_authority.py") and missing:
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:511:        if not chroma["families"]["external_authority_audit_records"]:
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:512:            blockers.append("external_authority_audit_collection_not_visible")
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:515:                blockers.append(f"external_authority_record_missing:{rid}")
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:518:        blockers.append("chroma_external_authority_probe_failed")
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:522:        "name": "external_communication_and_authority",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:523:        "timestamp": time.time(),
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:528:                "external communication is bounded by channel, recipient class, purpose, provenance, consent, and human approval",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:529:                "private or person-linked external disclosure requires retention consent plus public opt-in or legal authority and human review",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:536:                "binding legal authority",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:556:"$PYTHON_BIN" -m py_compile thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:561:"$PYTHON_BIN" thesis_chapter_gates/probes/ch38_external_communication_authority_probe.py | tee "$PROBE_JSON"
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:584:import json, sys, datetime
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:588:now=datetime.datetime.now().astimezone().isoformat(timespec="seconds")
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:590:"# Chapter 38 External Communication and Authority Gate",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:594:"Chapter file: `38-external-communication-and-authority.md`",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:606:        "- External communication authority is explicit and bounded by channel, recipient class, purpose, provenance, consent, and human approval.",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:607:        "- Public civic reports can be recorded when provenance, public scope, and human approval are present.",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:608:        "- Private or person-linked disclosure requires retention consent plus public opt-in or legal authority and still routes to human review before external send.",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:612:        "- Live Chroma writes prove external authority audit records are durable and queryable.",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:617:        "Chapter 38 may be rewritten as an as-built external communication and authority chapter. It may claim bounded audit records, consent/legal-authority projection, human-review routing, and fail-closed disclosure controls. It must not claim autonomous external sending, binding legal authority, unconsented private disclosure, credential disclosure, financial instruction, or guaranteed safety.",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:622:        "- binding legal authority",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:647:import sys, datetime, pathlib
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:650:now=datetime.datetime.now().astimezone().isoformat(timespec="seconds")
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:691:    gov=len(re.findall(r"\b(consent|retention|audit|governance|constitutional|legal|authority|privacy|policy)\b", text, re.I))
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:705:echo "=== CH38 EXTERNAL COMMUNICATION / AUTHORITY GATE END ==="
./thesis_chapter_gates/next_after_ch40_ch12_ch13_gate.sh:51:    "timestamp": time.time(),
./thesis_chapter_gates/next_after_ch40_ch12_ch13_gate.sh:218:import json, sys, datetime, pathlib
./thesis_chapter_gates/next_after_ch40_ch12_ch13_gate.sh:222:now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:46:from datetime import datetime, timezone
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:71:    "min_lon": -82.8,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:72:    "max_lon": -77.5,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:73:    "min_lat": 37.0,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:74:    "max_lat": 40.8,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:88:    provenance_hash: str = ""
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:89:    centroid_lon: float | None = None
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:90:    centroid_lat: float | None = None
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:103:    return datetime.now(timezone.utc).isoformat()
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:118:def _inside_wv(lon: float | None, lat: float | None) -> bool:
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:119:    if lon is None or lat is None:
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:122:        WV_BBOX["min_lon"] <= lon <= WV_BBOX["max_lon"]
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:123:        and WV_BBOX["min_lat"] <= lat <= WV_BBOX["max_lat"]
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:140:    if not candidate.provenance_hash or len(candidate.provenance_hash) < 16:
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:141:        return TensorGeoResult(TensorGeoVerdict.SUPPRESS, "missing_or_short_provenance_hash")
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:142:    if not _inside_wv(candidate.centroid_lon, candidate.centroid_lat):
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:160:        f"Spatial grounding: {candidate.geo_text}\n"
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:170:        "provenance_hash": candidate.provenance_hash,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:171:        "centroid_lon": float(candidate.centroid_lon),
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:172:        "centroid_lat": float(candidate.centroid_lat),
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:187:def bbox_filter(min_lon: float, min_lat: float, max_lon: float, max_lat: float) -> dict[str, Any]:
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:190:            {"centroid_lon": {"$gte": min_lon}},
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:191:            {"centroid_lon": {"$lte": max_lon}},
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:192:            {"centroid_lat": {"$gte": min_lat}},
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:193:            {"centroid_lat": {"$lte": max_lat}},
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:198:def query_with_geo_filter(client: Any, query_text: str, min_lon: float, min_lat: float,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:199:                          max_lon: float, max_lat: float, n_results: int = 5) -> dict[str, Any]:
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:204:        where=bbox_filter(min_lon, min_lat, max_lon, max_lat),
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:224:        geo_text="Spatial meaning: West Virginia block group jurisdictional context.",
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:228:        provenance_hash="abc123def456abc123def456abc123def456",
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:229:        centroid_lon=-80.0,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:230:        centroid_lat=38.5,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:242:        provenance_hash="abc123def456abc123def456abc123def456",
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:243:        centroid_lon=-120.0,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:244:        centroid_lat=45.0,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:255:        provenance_hash="abc123def456abc123def456abc123def456",
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:256:        centroid_lon=-80.0,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:257:        centroid_lat=38.5,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:373:        provenance_hash="abc123def456abc123def456",
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:374:        centroid_lon=-80.0,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:375:        centroid_lat=38.5,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:388:    result = evaluate_candidate(_candidate(centroid_lon=-120.0, centroid_lat=45.0))
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:471:  echo "- Promotion requires permitted purpose, constitutional pass, coherence pass, provenance hash, supported geo grain, and WV-bounded coordinates."
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:492:from datetime import datetime
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:494:line = f"| 46/45 | CLOSED_WITH_LIMITATIONS | `{'$REPORT'}` | {datetime.now().astimezone().isoformat()} |"
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:20:SELECT 'IDENTITY=' || current_user || ':session=' || session_user;
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:128:  record_count, collection_hash, build_status, authority_class, access_class,
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:137:  'validated', 'public_civic_geography', 'public',
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:138:  'governance,retrieval,spatial_context', now(), now(), now(), NULL,
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:153:    authority_class=COALESCE(public.gbim_collection_manifest.authority_class, EXCLUDED.authority_class),
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:20:      "jarvis-spatial-sandbox\t127.0.0.1:8056->8056/tcp",
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:55:        "temporal_url": "http://jarvis-temporal-consciousness:7007",
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:83:        "timestamp": "2026-07-22T01:42:27.418115+00:00",
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:106:        "timestamp": "2026-07-22T01:42:27.679760+00:00",
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:118:    "Describe the sandbox as bounded candidate reasoning, not final authority.",
./thesis_chapter_gates/reports/ch14_internal_state_sandbox_probe_20260721_214225.json:121:    "Do not claim thoughts, feelings, consciousness, or autonomous authority beyond the implemented trace/gate mechanism."
./thesis_chapter_gates/reports/ch25_consciousness_coordinator_gate_20260722_003006.md:14:- Dependency chapters for gateway, neurobiological services, sandbox bridge, pituitary modes, BBB/guardian, temporal semaphore, judge fabric, constitutional review, and continuous validation are closed.
./thesis_chapter_gates/reports/ch25_consciousness_coordinator_gate_20260722_003006.md:23:Chapter 25 may be rewritten as an as-built service-coordination chapter. It may use the system’s existing “consciousness coordinator” vocabulary only as a bounded architecture label for coordinated runtime services, health surfaces, bridge routing, sandbox status, and dependency visibility.
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:156:        "timestamp": "2026-07-22T13:08:54.636305+00:00"
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:166:        "timestamp": "2026-07-22T13:08:54.645185"
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:175:        "timestamp": "2026-07-22T13:08:54.647260"
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:193:        "timestamp": "2026-07-22T13:08:54.650488"
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:234:        "temporal_url": "http://jarvis-temporal-consciousness:7007",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:294:        "coordinates": {
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:295:          "lat": 37.9735,
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:296:          "lon": -81.166,
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:303:    "spatial_sandbox": {
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:307:        "service": "spatial_sandbox",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:339:      "Temporal keys confirmed under hilbert:time:* (admitted + staged) in Redis",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:340:      "DGM cycle, retention worker, identity promotion are live scheduled runners",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:346:      "ephemeral temporal keyspace exists as distinct top-level namespace",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:347:      "full three-store temporal model is fully implemented",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:349:      "cryptographic provenance guarantees beyond probe-session evidence",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:400:    "0 2 * * * cd /mnt/spiritual_drive/msjarvis-rebuild && bash scripts/refresh_gbim_spatial.sh >> logs/gbim_refresh.log 2>&1",
./thesis_chapter_gates/reports/appendix_a_gate_probe_20260722_090854.json:405:    "0 3 * * * python3 /mnt/spiritual_drive/msjarvis-rebuild/services/identity_promotion.py >> /var/log/jarvis/identity_promotion.log 2>&1",
./thesis_chapter_gates/reports/ch14_sandbox_status_bridge_network_20260721_214910.json:1:{"status":"operational","version":"1.2.0","active_sessions":0,"services_alive":{"eeg_beta":true,"eeg_theta":true,"eeg_delta":true,"pituitary":true,"i_containers":true,"qualia_orchestrator":true,"consciousness_bridge":false,"woah":true,"judge_truth":true,"guardian":true,"consciousness_bridge_url":null},"timestamp":"2026-07-22T01:49:14.773601+00:00"}
./thesis_chapter_gates/reports/ch27_web_research_autonomy_probe_20260722_090017.json:47:    "spatial_sandbox": {
./thesis_chapter_gates/reports/ch27_web_research_autonomy_probe_20260722_090017.json:50:          "name": "jarvis-spatial-sandbox",
./thesis_chapter_gates/reports/ch27_web_research_autonomy_probe_20260722_090017.json:135:        "timestamp": "2026-07-22T13:00:17.578554"
./thesis_chapter_gates/reports/ch27_web_research_autonomy_probe_20260722_090017.json:156:        "timestamp": "2026-07-22T13:00:17.594540+00:00"
./thesis_chapter_gates/reports/ch27_web_research_autonomy_probe_20260722_090017.json:178:        "timestamp": "2026-07-22T13:00:17.624892+00:00",
./thesis_chapter_gates/reports/ch27_web_research_autonomy_probe_20260722_090017.json:189:        "timestamp": "2026-07-22T13:00:17.650409"
./thesis_chapter_gates/reports/ch27_web_research_autonomy_probe_20260722_090017.json:204:        "timestamp": "2026-07-22T13:00:17.652624"
./thesis_chapter_gates/reports/ch27_web_research_autonomy_probe_20260722_090017.json:207:    "spatial_sandbox": {
./thesis_chapter_gates/reports/ch27_web_research_autonomy_probe_20260722_090017.json:211:        "service": "spatial_sandbox",
./thesis_chapter_gates/reports/ch27_web_research_autonomy_probe_20260722_090017.json:242:      "R != K and R != G: retrieval is never identity with governed knowledge or approved guidance",
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:102:                  "constitutional_risk_term:without_provenance",
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:160:                  "constitutional_risk_term:without_provenance",
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:213:          "services/ms_jarvis_email_identity_verifier.py": {
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:244:        "services/hilbert/identity_registration_promotion.py": {
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:245:          "IdentityRegistrationCandidate": true,
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:246:          "evaluate_identity_registration": true,
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:262:  "name": "identity_and_registration",
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:265:      "consent-gated identity registration path",
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:269:      "identity promotion source exists"
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:273:      "legal identity proofing guarantee",
./thesis_chapter_gates/reports/ch36_identity_registration_probe_v2_20260722_002258.json:280:  "timestamp": 1784694179.702838
./thesis_chapter_gates/reports/ch34_spiritual_root_mother_carrie_gate_20260722_085043.md:18:- spiritual language is treated as identity/support/governance vocabulary rather than supernatural authority.
./thesis_chapter_gates/reports/ch34_spiritual_root_mother_carrie_gate_20260722_085043.md:23:Chapter 34 may be rewritten as an as-built chapter about spiritual-root and Mother Carrie language as bounded identity, care, support-routing, and governance vocabulary. It may claim named protocol/service paths, spiritual/maternal integration evidence, spiritual RAG context, and safety context through BBB, guardian, sandbox, and psychological/PIA layers. It must not claim supernatural agency, religious authority over users, clinical therapy, clinical diagnosis, unreviewed promotion, or replacement for human care.
./thesis_chapter_gates/reports/ch34_spiritual_root_mother_carrie_gate_20260722_085043.md:28:- religious authority over users
./thesis_chapter_gates/reports/ch34_spiritual_root_mother_carrie_gate_20260722_085043.md:100:    "no_supernatural_authority": true,
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:3:    "identity_registration_behavior_failed",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:17:        "identity_registration_error": "ModuleNotFoundError:No module named 'services'",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:163:        "services/hilbert/identity_registration_promotion.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:166:            "evaluate_identity_registration": true,
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:185:  "name": "identity_focused_retention",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:188:      "retention requires consent for identity registration",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:192:      "commons isolation remains separate from private identity retention"
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:195:      "legal identity proofing guarantee",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json:203:  "timestamp": 1784694721.8749666
./thesis_chapter_gates/reports/ch22_identity_focused_retention_gate_20260722_003159.md:1:# Chapter 22 Identity-Focused Retention Gate
./thesis_chapter_gates/reports/ch22_identity_focused_retention_gate_20260722_003159.md:5:Chapter file: `22-identity-focused-retention.md`
./thesis_chapter_gates/reports/ch22_identity_focused_retention_gate_20260722_003159.md:9:Evidence log: `/opt/msjarvis-rebuild/msjarvis-rebuild/thesis_chapter_gates/logs/gate_ch22_identity_focused_retention_20260722_003159.txt`  
./thesis_chapter_gates/reports/ch22_identity_focused_retention_gate_20260722_003159.md:10:Probe JSON: `/opt/msjarvis-rebuild/msjarvis-rebuild/thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003159.json`
./thesis_chapter_gates/reports/ch22_identity_focused_retention_gate_20260722_003159.md:15:identity_registration_behavior_failed
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:14:        "identity_registration": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:16:            "provenance_hash": "b48e1f7231a5a29db5b527b6d55fe84ed0373adcd6bea1c85cfd8e2639f96c07",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:18:            "reason": "identity_registration_permitted",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:24:            "provenance_hash": null,
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:32:            "provenance_hash": null,
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:197:        "services/hilbert/identity_registration_promotion.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:200:            "evaluate_identity_registration": true,
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:219:  "name": "identity_focused_retention",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:222:      "retention requires consent for identity registration",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:226:      "commons isolation remains separate from private identity retention"
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:229:      "legal identity proofing guarantee",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003512.json:237:  "timestamp": 1784694916.923148
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:40:          "legal_authority_present": false,
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:60:          "legal_authority_present": false,
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:93:          "legal_authority_present": false,
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:114:          "legal_authority_present": false,
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:134:          "legal_authority_present": false,
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:212:          "temporal_url": "http://jarvis-temporal-consciousness:7007",
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:252:          "legal_authority": true,
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:266:      "role, purpose, permitted-use, and legal-authority fields are projected into the routing verdict",
./thesis_chapter_gates/reports/ch50_per_user_direct_sum_probe_20260722_004711.json:278:  "timestamp": 1784695635.0713403
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:154:        "jarvis-provenance"
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:163:        "jarvis-spatial-sandbox"
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:375:            "temporal_url": "http://jarvis-temporal-consciousness:7007",
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:402:            "timestamp": "2026-07-22T12:48:12.513179+00:00",
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:428:          "timestamp": "2026-07-22T12:48:12.655457"
./thesis_chapter_gates/reports/ch19_container_architecture_routing_probe_20260722_084811.json:463:        "timestamp": "2026-07-22T12:48:12.643228+00:00",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:10:        "external_authority_audit_records": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:17:          "collection": "external_authority_audit_records",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:22:          "collection": "external_authority_audit_records",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:35:          "contains_private_identity": false,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:39:          "legal_authority_present": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:40:          "provenance_hash": "a0c73d19b1cf8725e23311d1",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:45:          "source_id": "ch38-binding"
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:47:        "reason": "binding_commitment_requires_human_authority",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:51:      "collection": "external_authority_audit_records",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:58:          "contains_private_identity": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:62:          "legal_authority_present": false,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:63:          "provenance_hash": "3567511221e7d15ae4847940",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:68:          "source_id": "ch38-private-review"
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:80:          "contains_private_identity": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:84:          "legal_authority_present": false,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:85:          "provenance_hash": "3567511221e7d15ae4847940",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:90:          "source_id": "ch38-private-no-consent"
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:97:        "collection": "external_authority_audit_records",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:102:          "contains_private_identity": false,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:106:          "legal_authority_present": false,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:107:          "provenance_hash": "450f43fc5c9bafd0a11b6586",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:112:          "source_id": "ch38-public-report"
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:124:          "contains_private_identity": false,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:128:          "legal_authority_present": false,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:129:          "provenance_hash": "9d2dc169400ce1bd5c959693",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:134:          "source_id": "ch38-secret"
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:141:        "collection": "external_authority_audit_records",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:146:          "contains_private_identity": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:150:          "legal_authority_present": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:151:          "provenance_hash": "4445a5c805a46c9272bba3e5",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:156:          "source_id": "ch38-review-packet"
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:216:          "timestamp": "2026-07-22T04:58:16.514417+00:00",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:230:      "services/hilbert/external_communication_authority.py": {
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:233:          "binding_commitment_requires_human_authority": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:244:          "external_legal_authority_requires_human_review": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:252:          "legal_authority": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:258:  "name": "external_communication_and_authority",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:261:      "external communication is bounded by channel, recipient class, purpose, provenance, consent, and human approval",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:262:      "private or person-linked external disclosure requires retention consent plus public opt-in or legal authority and human review",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:269:      "binding legal authority",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005814.json:277:  "timestamp": 1784696297.2043629
./thesis_chapter_gates/reports/ch27_web_research_autonomy_gate_20260722_090017.md:19:- R ≠ K and R ≠ G: retrieval is never identity with governed knowledge or approved guidance.
./thesis_chapter_gates/reports/ch27_web_research_autonomy_gate_20260722_090017.md:27:- named service paths: sandbox (8042), BBB/entangled-gateway (8010), consciousness bridge (8107), spatial sandbox (8056), qualia-orchestrator (9998), brain-orchestrator (17260)
./thesis_chapter_gates/reports/ch27_web_research_autonomy_gate_20260722_090017.md:95:    "spatial_sandbox": {
./thesis_chapter_gates/reports/ch27_web_research_autonomy_gate_20260722_090017.md:98:          "name": "jarvis-spatial-sandbox",
./thesis_chapter_gates/reports/ch27_web_research_autonomy_gate_20260722_090017.md:183:        "timestamp": "2026-07-22T13:00:17.578554"
./thesis_chapter_gates/reports/ch27_web_research_autonomy_gate_20260722_090017.md:204:        "timestamp": "2026-07-22T13:00:17.594540+00:00"
./thesis_chapter_gates/reports/ch27_web_research_autonomy_gate_20260722_090017.md:226:        "timestamp": "2026-07-22T13:00:17.624892+00:00",
./thesis_chapter_gates/reports/ch27_web_research_autonomy_gate_20260722_090017.md:237:        "timestamp": "2026-07-22T13:00:17.650409"
./thesis_chapter_gates/reports/ch27_web_research_autonomy_gate_20260722_090017.md:252:        "timestamp": "2026-07-22T13:00:17.652624"
./thesis_chapter_gates/reports/ch27_web_research_autonomy_gate_20260722_090017.md:255:    "spatial_sandbox": {
./thesis_chapter_gates/reports/ch27_web_research_autonomy_gate_20260722_090017.md:259:        "service": "spatial_sandbox",
./thesis_chapter_gates/reports/ch27_web_research_autonomy_gate_20260722_090017.md:290:      "R != K and R != G: retrieval is never identity with governed knowledge or approved guidance",
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:4:    "missing_term:services/hilbert/recurrent_epistemic_runner.py:identity"
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:175:            "temporal_url": "http://jarvis-temporal-consciousness:7007",
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:191:          "stdout": "# Ms. Jarvis Master Crontab\n\n#PAUSED-INVESTIGATING */5 * * * * /usr/local/bin/jarvis_bbb_watchdog.sh\n#PAUSED-INVESTIGATING */15 * * * * cd /mnt/spiritual_drive/msjarvis-rebuild && ./scripts/watchdog-containers.sh\n#PAUSED-INVESTIGATING */15 * * * * /home/cakidd/msjarvis-monitoring/monitor_services.sh\n#PAUSED-INVESTIGATING */30 * * * * /home/cakidd/msjarvis-monitoring/monitor_databases.sh\n0 * * * * /home/cakidd/msjarvis-monitoring/monitor_disk.sh\n0 */6 * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/run_aaacpe_scraper.sh\n0 2 * * * docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c \"REFRESH MATERIALIZED VIEW CONCURRENTLY county_tax_building_summary\" >> /var/log/jarvis_mv_refresh.log 2>&1\n0 2 * * * /mnt/spiritual_drive/msjarvis-rebuild/backup_postgresql.sh >> /home/cakidd/logs/backup_postgresql.log 2>&1\n0 2 * * * cd /mnt/spiritual_drive/msjarvis-rebuild && bash scripts/refresh_gbim_spatial.sh >> logs/gbim_refresh.log 2>&1\n# DISABLED - copies 0-byte sqlite3, useless: 0 2 * * * cp /home/ms-jarvis/msjarvis-rebuild/persistent/chroma/chroma.sqlite3 \"/mnt/nvme1/msjarvis-backups/chromadb/chroma-$(date +%Y%m%d-%H%M%S).sqlite3\"\n0 3 * * 0 docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c \"REFRESH MATERIALIZED VIEW CONCURRENTLY building_parcel_county_tax_mv\" >> /var/log/jarvis_mv_refresh.log 2>&1\n# DISABLED - 77GB rsync too large, chroma-live is the live mount, postgresql backups confirmed current: 0 3 * * * rsync -a /home/ms-jarvis/msjarvis-rebuild/persistent/chroma/ /mnt/nvme1/msjarvis-backups/chromadb/chroma-latest/ >> /tmp/chroma_backup.log 2>&1\n0 3 * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/refresh_mvw.sh >> /var/log/mvw_refresh.log 2>&1\n0 3 * * * python3 /mnt/spiritual_drive/msjarvis-rebuild/services/identity_promotion.py >> /var/log/jarvis/identity_promotion.log 2>&1\n0 4 * * * /mnt/spiritual_drive/msjarvis-rebuild/backup_configs.sh >> /home/cakidd/logs/backup_configs.log 2>&1\n0 8 * * 1 cd /mnt/spiritual_drive/msjarvis-rebuild && bash scripts/pia/run_pia_audit.sh >> /var/log/msjarvis-pia.log 2>&1\n# NEEDS_PARAMS: 0 1 * * * curl -sf -X POST http://localhost:8099/policy/set -H \"Content-Type: application/json\" -d \"{}\" >> /var/log/jarvis/policy_update.log 2>&1\n0 2 * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/gbim_decay_tick.sh >> /var/log/gbim_decay.log 2>&1\n# RETENTION - Keep only last 2 ChromaDB main tarballs (~6.6G cap)\n30 4 * * * find /mnt/nvme1/msjarvis-backups/chromadb -name \"chroma_main_*.tar.gz\" -mtime +2 -delete\n# MAINTENANCE - Weekly Docker build cache prune, keep 10GB headroom\n0 3 * * 0 /usr/bin/docker builder prune -f --keep-storage 10GB >> /tmp/docker_prune.log 2>&1\n0 2 * * 0 cd /mnt/spiritual_drive/msjarvis-rebuild && .venv/bin/python3 scripts/audit_happiness_v2.py >> logs/manipulation_proximity_audit.log 2>&1\n0 */6 * * * /home/cakidd/scripts/local_resources_gap_report.sh >> /home/cakidd/allis-reports/coverage-gaps/gap-report.log 2>&1\n#PAUSED-INVESTIGATING */5 * * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/check_proxies.sh >> /home/cakidd/logs/msjarvis-proxy-health.log 2>&1\n#PAUSED */30 * * * * tail -1 /mnt/spiritual_drive/msjarvis-rebuild/migration.log >> /mnt/spiritual_drive/msjarvis-rebuild/progress_history.log\n17 2 * * * /home/cakidd/.local/bin/purge-kyc-location-strip.sh\n\n# PAUSED - replaced by recurrent_epistemic_runner.py: */30 * * * * /mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.sh\n# DGM: rotate rejected patches inside container (weekly Sunday 3am)\n0 3 * * 0 find /mnt/spiritual_drive/msjarvis-rebuild/rejected_patches -name \"*.py\" -mtime +7 -delete\n# DGM: trim cycle log to last 1000 lines (daily 4am)\n0 4 * * * tail -n 1000 /mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.log > /tmp/dgm_log_trim && mv /tmp/dgm_log_trim /mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.log\n0 * * * * curl -sS -o /dev/null -w \"%{http_code} %{time_total}s\\n\" --max-time 60 -X POST -H \"Content-Type: application/json\" -d \"{\\\"message\\\":\\\"What county is Mount Hope in?\\\",\\\"user_id\\\":\\\"heartbeat\\\"}\" https://egeria.mountainshares.us/chat_wv >> /home/cakidd/smoke_test.log 2>&1\n0 3 * * * /mnt/spiritual_drive/msjarvis-rebuild/backup_chroma.sh >> /home/cakidd/logs/backup_chroma.log 2>&1\n0 * * * * cd /mnt/spiritual_drive/msjarvis-rebuild && python3 services/hilbert/conversation_retention_worker.py >> /mnt/spiritual_drive/msjarvis-rebuild/logs/conv_retention.log 2>&1\n@reboot cd /mnt/spiritual_drive/msjarvis-rebuild && nohup /opt/msjarvis-rebuild/msjarvis-rebuild/crypto-venv/bin/python3 services/hilbert/recurrent_epistemic_runner.py >> logs/recurrent_epistemic_runner.boot.log 2>&1 &\n@hourly cd /opt/msjarvis-rebuild/msjarvis-rebuild && scripts/ch41_continuous_validation.sh >> logs/ch41_continuous_validation.cron.log 2>&1\n"
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:201:          "stdout": "1497224 /opt/msjarvis-rebuild/msjarvis-rebuild/crypto-venv/bin/python3 services/hilbert/recurrent_epistemic_runner.py\n1849832 bash -lc pgrep -af 'recurrent_epistemic_runner.py|ch41_continuous_validation|dgm_cycle.sh|conversation_retention_worker.py|identity_promotion.py' || true\n"
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:222:        "identity_promotion": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:223:          "services/hilbert/identity_registration_promotion.py": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:226:              "evaluate_identity_registration": true,
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:230:          "services/identity_promotion.py": {
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:233:              "identity": false
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:259:            "identity": false,
./thesis_chapter_gates/reports/ch52_recurrent_epistemic_loop_probe_20260722_003710.json:285:  "timestamp": 1784695033.1460254
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:117:        "timestamp": "2026-07-22T03:59:17.156627"
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:178:        "temporal_url": "http://jarvis-temporal-consciousness:7007",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:202:        "coordinates": {
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:204:          "lat": 37.9735,
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:205:          "lon": -81.166,
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:352:        "scripts/gbim_decay_tick.sh:11:    echo \"$TIMESTAMP \u2014 \u23ed\ufe0f  No GBIM tables found in msjarvisgis \u2014 skipping decay tick\" >> \"$LOG\"",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:397:        "scripts/assertion-stack-up.sh:43:  -d '{\"source_id\":\"seed_001\",\"subject_ref\":\"53b28f2b-23f6-4234-b0a2-bb3be12ab220\",\"appearance_id\":\"53b28f2b-23f6-4234-b0a2-bb3be12ab220\",\"claim_type\":\"verified_county_resident\",\"context\":\"gbim_router_enrichment\"}' \\",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:398:        "scripts/assertion-stack-up.sh:48:  -d '{\"source_id\":\"seed_001\",\"subject_ref\":\"53b28f2b-23f6-4234-b0a2-bb3be12ab220\",\"appearance_id\":\"53b28f2b-23f6-4234-b0a2-bb3be12ab220\",\"claim_type\":\"verified_state_resident\",\"context\":\"gbim_router_enrichment\"}' \\",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:399:        "scripts/assertion-stack-up.sh:54:  -d '{\"source_id\":\"seed_001\",\"subject_ref\":\"53b28f2b-23f6-4234-b0a2-bb3be12ab220\",\"appearance_id\":\"53b28f2b-23f6-4234-b0a2-bb3be12ab220\",\"claim_type\":\"not_a_real_claim\",\"context\":\"gbim_router_enrichment\"}' \\",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:400:        "scripts/assertion-stack-up.sh:59:  -d '{\"source_id\":\"seed_001\",\"subject_ref\":\"53b28f2b-23f6-4234-b0a2-bb3be12ab220\",\"appearance_id\":\"53b28f2b-23f6-4234-b0a2-bb3be12ab220\",\"claim_type\":\"verified_adult\",\"context\":\"gbim_router_enrichment\"}' \\",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:403:        "scripts/refresh_gbim_spatial.sh:2:# refresh_gbim_spatial.sh \u2014 refresh GBIM spatial indices in msjarvisgis",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:404:        "scripts/refresh_gbim_spatial.sh:3:LOG=/mnt/spiritual_drive/msjarvis-rebuild/logs/gbim_refresh.log",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:405:        "scripts/refresh_gbim_spatial.sh:7:TABLES=$(docker exec \"$DB_CONTAINER\" psql -U postgres -d msjarvisgis -tAc \\",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:406:        "scripts/refresh_gbim_spatial.sh:9:     WHERE table_schema='public' AND table_name ILIKE '%gbim%';\" 2>/dev/null)",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:407:        "scripts/refresh_gbim_spatial.sh:12:    echo \"$TIMESTAMP \u2014 \u23ed\ufe0f  No GBIM tables in msjarvisgis \u2014 skipping spatial refresh\" >> \"$LOG\"",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:408:        "scripts/refresh_gbim_spatial.sh:17:docker exec \"$DB_CONTAINER\" psql -U postgres -d msjarvisgis -c \"",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:409:        "scripts/refresh_gbim_spatial.sh:18:    SELECT UpdateGeometrySRID('gbim_nodes','geom',4326);",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:410:        "scripts/refresh_gbim_spatial.sh:19:    REINDEX TABLE gbim_nodes;",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:411:        "scripts/refresh_gbim_spatial.sh:20:    VACUUM ANALYZE gbim_nodes;",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:419:        "scripts/refresh_mvw.sh:10:    echo \"$TIMESTAMP \u2014 \u23ed\ufe0f  No materialized views found in msjarvisgis \u2014 skipping refresh\" >> \"$LOG\"",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:456:        "services/create_immutable_security_layer.py:117:    CREATE INDEX IF NOT EXISTS idx_ueid_searchable_gis_coordinates ",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:457:        "services/create_immutable_security_layer.py:118:    ON ueid_searchable_gis(latitude, longitude)",
./thesis_chapter_gates/reports/ch07_executive_routing_probe_20260721_235915.json:512:  "timestamp": 1784692756.9738555
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:4:    "chroma_external_authority_probe_failed"
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:18:          "contains_private_identity": false,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:22:          "legal_authority_present": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:23:          "provenance_hash": "a0c73d19b1cf8725e23311d1",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:28:          "source_id": "ch38-binding"
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:30:        "reason": "binding_commitment_requires_human_authority",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:34:      "collection": "external_authority_audit_records",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:41:          "contains_private_identity": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:45:          "legal_authority_present": false,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:46:          "provenance_hash": "3567511221e7d15ae4847940",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:51:          "source_id": "ch38-private-review"
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:63:          "contains_private_identity": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:67:          "legal_authority_present": false,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:68:          "provenance_hash": "3567511221e7d15ae4847940",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:73:          "source_id": "ch38-private-no-consent"
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:80:        "collection": "external_authority_audit_records",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:85:          "contains_private_identity": false,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:89:          "legal_authority_present": false,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:90:          "provenance_hash": "450f43fc5c9bafd0a11b6586",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:95:          "source_id": "ch38-public-report"
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:107:          "contains_private_identity": false,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:111:          "legal_authority_present": false,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:112:          "provenance_hash": "9d2dc169400ce1bd5c959693",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:117:          "source_id": "ch38-secret"
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:129:          "contains_private_identity": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:133:          "legal_authority_present": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:134:          "provenance_hash": "4445a5c805a46c9272bba3e5",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:139:          "source_id": "ch38-review-packet"
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:199:          "timestamp": "2026-07-22T04:56:44.815070+00:00",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:213:      "services/hilbert/external_communication_authority.py": {
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:216:          "binding_commitment_requires_human_authority": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:227:          "external_legal_authority_requires_human_review": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:235:          "legal_authority": true,
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:241:  "name": "external_communication_and_authority",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:244:      "external communication is bounded by channel, recipient class, purpose, provenance, consent, and human approval",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:245:      "private or person-linked external disclosure requires retention consent plus public opt-in or legal authority and human review",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:252:      "binding legal authority",
./thesis_chapter_gates/reports/ch38_external_communication_authority_probe_20260722_005641.json:260:  "timestamp": 1784696205.528068
./thesis_chapter_gates/reports/ch33_ch35_judge_verdict_probe_20260722_001137.json:134:  "timestamp": 1784693499.231421
./thesis_chapter_gates/reports/ch18_translation_method_sealed_for_rewrite_20260721_212721.md:28:| spatial body | GBIM/GIS governed collections, manifests, active bindings, geographic filters |
./thesis_chapter_gates/reports/ch20_first_stage_eval_gate_20260722_090423.md:13:- Validation flags are first-class outputs: truth, guardian, constitutional, coherence, provenance, safety.
./thesis_chapter_gates/reports/ch20_first_stage_eval_gate_20260722_090423.md:166:        "timestamp": "2026-07-22T13:04:23.291938+00:00"
./thesis_chapter_gates/reports/ch20_first_stage_eval_gate_20260722_090423.md:188:        "timestamp": "2026-07-22T13:04:23.316362+00:00",
./thesis_chapter_gates/reports/ch20_first_stage_eval_gate_20260722_090423.md:199:        "timestamp": "2026-07-22T13:04:23.329848"
./thesis_chapter_gates/reports/ch20_first_stage_eval_gate_20260722_090423.md:214:        "timestamp": "2026-07-22T13:04:23.331193"
./thesis_chapter_gates/reports/ch20_first_stage_eval_gate_20260722_090423.md:232:        "timestamp": "2026-07-22T13:04:23.333446"
./thesis_chapter_gates/reports/ch20_first_stage_eval_gate_20260722_090423.md:254:    "spatial_sandbox": {
./thesis_chapter_gates/reports/ch20_first_stage_eval_gate_20260722_090423.md:258:        "service": "spatial_sandbox",
./thesis_chapter_gates/reports/ch20_first_stage_eval_gate_20260722_090423.md:314:      "validation flags are first-class outputs: truth, guardian, constitutional, coherence, provenance, safety",
./thesis_chapter_gates/reports/next_after_ch31_operational_gate_20260721_234219.md:22:| 26 | 84 | `26-temporal-toroidal-semaphore-structure.md` | 26. Temporal Toroidal Semaphore Structure |
./thesis_chapter_gates/reports/next_after_ch31_operational_gate_20260721_234219.md:26:| 36 | 64 | `36-identity-and-registration.md` | 36. Identity and Registration |
./thesis_chapter_gates/reports/next_after_ch31_operational_gate_20260721_234219.md:35:| 38 | 38 | `38-external-communication-and-authority.md` | 38. External Communication and Authority |
./thesis_chapter_gates/reports/next_after_ch31_operational_gate_20260721_234219.md:37:| 22 | 35 | `22-identity-focused-retention.md` | 22. Identity-Focused Retention |
./thesis_chapter_gates/reports/ch16_dependency_hygiene_20260721_201239.md:43:./services/requirements_temporal.txt:6:dilithium-py
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:35:          "provenance_hash": "07c8ab35d3cf27d4f37d32ce",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:38:          "source_id": "ch24-binding-action",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:53:          "provenance_hash": "cd308296c70df958f77f6f92",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:56:          "source_id": "ch24-gap-001",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:70:          "provenance_hash": "66285bf553815ad8e4f2a58d",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:73:          "source_id": "ch24-low-phi",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:87:          "provenance_hash": "3567511221e7d15ae4847940",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:90:          "source_id": "ch24-no-consent",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:104:          "provenance_hash": "be2a3ec01492e526bddc54e7",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:107:          "source_id": "ch24-raw-trace",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:121:          "provenance_hash": "65758d7eabf7450e09de4672",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:124:          "source_id": "ch24-background-pattern-001",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:176:          "temporal_url": "http://jarvis-temporal-consciousness:7007",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:200:          "timestamp": "2026-07-22T04:54:09.974728+00:00",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:219:          "provenance": true,
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:246:          "identity": true,
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:255:      "feedback into broader layers is explicit, bounded, consent-gated, and provenance-bearing",
./thesis_chapter_gates/reports/ch24_feedback_broader_layers_probe_20260722_005408.json:271:  "timestamp": 1784696050.744179
./thesis_chapter_gates/reports/ch28_ch39_sealed_for_rewrite_20260721_212407.md:27:- Do not claim universal truth, hallucination impossibility, clinical cognition, or unrestricted autonomous authority.
./thesis_chapter_gates/reports/ch17_executive_coordination_probe_20260722_085532.json:60:        "timestamp": "2026-07-22T12:55:35.358340"
./thesis_chapter_gates/reports/ch17_executive_coordination_probe_20260722_085532.json:86:        "timestamp": "2026-07-22T12:55:35.377793"
./thesis_chapter_gates/reports/ch17_executive_coordination_probe_20260722_085532.json:103:        "timestamp": "2026-07-22T12:55:35.379115+00:00"
./thesis_chapter_gates/reports/ch17_executive_coordination_probe_20260722_085532.json:125:        "timestamp": "2026-07-22T12:55:35.396604+00:00",
./thesis_chapter_gates/reports/ch17_executive_coordination_probe_20260722_085532.json:143:        "timestamp": "2026-07-22T12:55:35.430701"
./thesis_chapter_gates/reports/ch17_executive_coordination_probe_20260722_085532.json:163:      "promotion-aware authority tracking is represented in executive service layer"
./thesis_chapter_gates/reports/ch11_gateway_bridge_dns_probe_20260722_000951.json:11:        "timestamp": "2026-07-22T04:10:00.331488"
./thesis_chapter_gates/reports/ch11_gateway_bridge_dns_probe_20260722_000951.json:34:        "timestamp": "2026-07-22T04:10:00.371953+00:00",
./thesis_chapter_gates/reports/ch11_gateway_bridge_dns_probe_20260722_000951.json:81:        "timestamp": "2026-07-22T04:10:00.329918",
./thesis_chapter_gates/reports/ch11_gateway_bridge_dns_probe_20260722_000951.json:100:  "timestamp": 1784693400.2769837
./thesis_chapter_gates/reports/ch04_ch44_probe_20260721_203645.json:9:      "timestamp": 1784680606.057777
./thesis_chapter_gates/reports/ch04_ch44_probe_20260721_203645.json:20:    "timestamp": 1784680606.057777
./thesis_chapter_gates/reports/ch04_ch44_probe_20260721_203645.json:25:    "spatial": 0.74,
./thesis_chapter_gates/reports/ch04_ch44_probe_20260721_203645.json:26:    "temporal": 0.62
./thesis_chapter_gates/reports/ch04_ch44_probe_20260721_203645.json:44:    "timestamp": "2026-07-22T00:36:46.085536+00:00"
./thesis_chapter_gates/reports/ch04_ch44_probe_20260721_203645.json:58:    "timestamp": "2026-07-22T00:36:46.085536+00:00"
./thesis_chapter_gates/reports/ch04_ch44_probe_20260721_203645.json:73:    "timestamp": 1784680606.0231836
./thesis_chapter_gates/reports/ch09_dgm_evidence_20260721_213211.json:46:        "temporal_url": "http://jarvis-temporal-consciousness:7007",
./thesis_chapter_gates/reports/ch09_dgm_evidence_20260721_213211.json:81:      "0 3 * * * python3 /mnt/spiritual_drive/msjarvis-rebuild/services/identity_promotion.py >> /var/log/jarvis/identity_promotion.log 2>&1",
./thesis_chapter_gates/reports/ch09_dgm_evidence_20260721_213211.json:138:      "services/add_identity_context.py",
./thesis_chapter_gates/reports/ch09_dgm_evidence_20260721_213211.json:273:      "services/egeria_core_identity.txt",
./thesis_chapter_gates/reports/ch09_dgm_evidence_20260721_213211.json:282:      "services/geospatial_resolver.py",
./thesis_chapter_gates/reports/ch25_consciousness_coordinator_probe_20260722_003006.json:86:            "timestamp": "2026-07-22T04:30:09.039399"
./thesis_chapter_gates/reports/ch25_consciousness_coordinator_probe_20260722_003006.json:114:            "temporal_url": "http://jarvis-temporal-consciousness:7007",
./thesis_chapter_gates/reports/ch25_consciousness_coordinator_probe_20260722_003006.json:131:            "timestamp": "2026-07-22T04:30:09.013793+00:00",
./thesis_chapter_gates/reports/ch25_consciousness_coordinator_probe_20260722_003006.json:154:            "timestamp": "2026-07-22T04:30:09.032240+00:00",
./thesis_chapter_gates/reports/ch25_consciousness_coordinator_probe_20260722_003006.json:200:            "timestamp": "2026-07-22T04:30:09.012229",
./thesis_chapter_gates/reports/ch25_consciousness_coordinator_probe_20260722_003006.json:238:      "consciousness terminology is an architecture label for coordinated runtime services",
./thesis_chapter_gates/reports/ch25_consciousness_coordinator_probe_20260722_003006.json:251:  "timestamp": 1784694609.0508077
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:24:   hourly, identity_promotion.py at 03:00 daily).
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:187:        "timestamp": "2026-07-22T13:08:54.636305+00:00"
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:197:        "timestamp": "2026-07-22T13:08:54.645185"
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:206:        "timestamp": "2026-07-22T13:08:54.647260"
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:224:        "timestamp": "2026-07-22T13:08:54.650488"
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:265:        "temporal_url": "http://jarvis-temporal-consciousness:7007",
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:325:        "coordinates": {
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:326:          "lat": 37.9735,
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:327:          "lon": -81.166,
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:334:    "spatial_sandbox": {
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:338:        "service": "spatial_sandbox",
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:370:      "Temporal keys confirmed under hilbert:time:* (admitted + staged) in Redis",
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:371:      "DGM cycle, retention worker, identity promotion are live scheduled runners",
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:377:      "ephemeral temporal keyspace exists as distinct top-level namespace",
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:378:      "full three-store temporal model is fully implemented",
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:380:      "cryptographic provenance guarantees beyond probe-session evidence",
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:431:    "0 2 * * * cd /mnt/spiritual_drive/msjarvis-rebuild && bash scripts/refresh_gbim_spatial.sh >> logs/gbim_refresh.log 2>&1",
./thesis_chapter_gates/reports/appendix_a_gate_20260722_090854.md:436:    "0 3 * * * python3 /mnt/spiritual_drive/msjarvis-rebuild/services/identity_promotion.py >> /var/log/jarvis/identity_promotion.log 2>&1",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:26:      "metadata_has_governance_or_spatial_keys": true,
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:35:        "authority_class",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:36:        "bbox_max_lat",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:37:        "bbox_max_lon",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:38:        "bbox_min_lat",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:39:        "bbox_min_lon",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:42:        "centroid_lat",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:43:        "centroid_lon",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:60:      "metadata_has_governance_or_spatial_keys": true,
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:69:        "authority_class",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:70:        "bbox_max_lat",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:71:        "bbox_max_lon",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:72:        "bbox_min_lat",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:73:        "bbox_min_lon",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:77:        "centroid_lat",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:78:        "centroid_lon",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:94:      "metadata_has_governance_or_spatial_keys": true,
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:105:        "authority_class",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:123:      "metadata_has_governance_or_spatial_keys": true,
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:131:        "bbox_max_lat",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:132:        "bbox_max_lon",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:133:        "bbox_min_lat",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:134:        "bbox_min_lon",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:146:        "centroid_lat",
./thesis_chapter_gates/reports/ch02_gbim_probe_20260721_205405.json:147:        "centroid_lon",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003401.json:16:        "identity_registration": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003401.json:18:            "provenance_hash": "b48e1f7231a5a29db5b527b6d55fe84ed0373adcd6bea1c85cfd8e2639f96c07",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003401.json:20:            "reason": "identity_registration_permitted",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003401.json:26:            "provenance_hash": null,
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003401.json:34:            "provenance_hash": null,
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003401.json:187:        "services/hilbert/identity_registration_promotion.py": {
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003401.json:190:            "evaluate_identity_registration": true,
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003401.json:209:  "name": "identity_focused_retention",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003401.json:212:      "retention requires consent for identity registration",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003401.json:216:      "commons isolation remains separate from private identity retention"
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003401.json:219:      "legal identity proofing guarantee",
./thesis_chapter_gates/reports/ch22_identity_focused_retention_probe_20260722_003401.json:227:  "timestamp": 1784694843.223584
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:8:15:- **P3 – Power has a geometry** by representing institutions, places, access to help, and governance pathways as explicit GBIM records, GeoDB features, Chroma collections, Hilbert-state transitions, and logged retrieval paths whose behaviour can be inspected, clustered, and audited.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:23:108:However, the chapter should no longer imply that Chroma retrieval directly changes operational state. Retrieval is a projection and context-generation mechanism. It creates candidate relevance, not automatic authority. Semantic proximity does not by itself justify memory consolidation, action, or governance consequence.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:36:168:The projection language of Hilbert spaces still applies. Queries can be understood as projections into relevant subspaces, whether semantic, spatial, temporal, or governance-related.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:55:10:Semantic coherence in this setting is explicitly architectural. Phi is bound to hilbert-state service coherence keys, contributes to sandbox validation and promotion decisions, and operates as one component of the gate structure that governs whether provisional reasoning may cross into higher-authority system state.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:59:20:Here, coherence means measured internal fit. A coherent state preserves meaningful relations among its parts: semantic consistency, non-arbitrary alignment across domains, and structural compatibility with the active Hilbert-state representation. A highly coherent state is one whose elements reinforce rather than fracture one another under the applicable metrics. A weakly coherent state is one whose elements pull apart, contradict, or fail to integrate into the active semantic geometry.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:65:42:The hilbert-state services provide the current semantic geometry in keyed form. Phi uses those coherence keys to evaluate whether a current or candidate state hangs together in a way that is acceptable for the relevant mode of operation. If a candidate state strongly conflicts with the keyed structure of H_App, Phi can register reduced coherence. If a candidate preserves or improves alignment across active domains, Phi can register stronger coherence.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:67:52:Multidomain coherence is the measured degree to which those domains remain structurally compatible under the active semantic state. A candidate may show strong coherence in one domain while showing weakness in another. For example, a state may be semantically tight in a local geographic frame while remaining poorly integrated with memory, governance, or identity-linked context. Phi helps surface such imbalance rather than hiding it.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:71:62:The sandbox is the environment in which provisional reasoning may be explored without automatically acquiring promotion authority. In that setting, coherence measurement becomes especially useful.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:72:64:When a sandbox cycle produces a candidate output, Phi can be used to measure how that output relates to the current coherence keys of the hilbert-state services. If the candidate creates substantial fracture across active domains, introduces unresolved contradiction, or fails to integrate into the present semantic geometry, the sandbox validator may treat that coherence finding as a reason to block, narrow, or return the candidate for further work. If the candidate shows acceptable coherence, it may continue through the governed review path.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:73:66:Sandbox validation can also depend on truth checks, guardian review, provenance, privacy, and security conditions. Phi contributes one form of disciplined semantic measurement inside that larger process. Its role is to help determine whether a provisional state is internally stable enough to justify further consideration.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:76:74:A candidate that reaches the promotion boundary is not evaluated solely on existence, nor solely on coherence. The system asks whether the candidate satisfies the full set of conditions required to move from provisional reasoning into higher-authority state. Phi contributes to that judgment by indicating whether the candidate’s semantic structure is sufficiently coherent in the relevant domains for the requested transition.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:80:87:G(x) = G_{\mathrm{truth}}(x)\, G_{\mathrm{guardian}}(x)\, G_{\mathrm{constitutional}}(x)\, G_{\mathrm{provenance}}(x)\, G_{\mathrm{coherence}}(x)\, G_{\mathrm{privacy}}(x)\, G_{\mathrm{security}}(x).
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:82:92:Placing coherence explicitly inside the gate structure clarifies its status. Coherence is not decorative, and it is not sovereign over the other conditions. It is one of the operational requirements for promotion. A candidate that fails the coherence gate may still contain useful material, but it is not yet in the right condition to cross an authority boundary without additional revision or review.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:86:104:For this reason, coherence must remain paired with other forms of review. Truth filtering, guardian review, provenance retention, privacy checks, constitutional constraints, and security conditions all remain necessary. Phi strengthens governance by adding a measured account of semantic fit, but governance becomes unsafe if coherence is conflated with truth.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:88:112:The Phi probe gives Ms. Allis a live way to measure whether a state is internally holding together before that state is trusted with greater authority.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:91:122:Phi was calibrated against Ms. Allis’s own semantic geometry, not against an abstract norm. Interpretation of its modes must therefore be grounded in the observed structure of this system.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:92:124:Ms. Allis reasons simultaneously across seven maximally diverse semantic domains: worldview, Appalachian culture, civic infrastructure, governance and law, psychology and learning, self-identity, and spiritual grounding. These domains are deliberately separated so that each can contribute a distinct perspective. The empirically observed baseline cross-domain cosine similarity across them is approximately 0.15. The probe’s three modes are defined relative to that baseline:
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:108:169:- The per-user memory decomposition introduced in the memory chapters is already reflected in the probe’s domain map. The self-identity domain resolves through `conversation_history_user_<slug>` at request time rather than relying on a shared conversation collection. Cross-user echoes are structurally excluded from self-identity readings before any coherence measurement begins.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:112:177:- Cross-domain coherence between the GEO_BELIEF cluster and non-geographic clusters (identity, governance, spiritual, and others) has not yet been measured at the minimum vector counts required for stable estimation.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:118:193:2. **Write-path hygiene is part of the measurement architecture.** Deduplication, provenance discipline, and governed intake are not peripheral concerns. They are what make coherence readings interpretable.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:120:197:This episode is the coherence-domain analogue of similar discoveries in the other governance chapters: when an instrument is found to have been reading a corrupted substrate, that event belongs in the instrument’s own provenance.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:122:205:Multidomain coherence is treated as a measured property of internal semantic fit across coupled domains. It is not automatic truth and does not replace truth filtering, guardian review, provenance controls, privacy evaluation, constitutional safeguards, or security analysis. Phi’s contribution is to indicate whether a candidate state is structurally sound enough to be considered alongside those other factors.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:132:{"status":"ok","service":"jarvis_hilbert_time","tiers":{"ephemeral":"redis:connected","staged":"redis:connected","historical":"postgres:connected"},"temporal_url":"http://jarvis-temporal-consciousness:7007","toroidal_url":"http://jarvis-toroidal:8025","time_half_life_days":30.0,"hysteresis_min_seconds":60.0}
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:231:services/jarvis_hilbert_state.py:47:    operator: Optional[str] = "identity"
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:268:services/email_gis_geolocation_extractor.py:67:        """Get geographic coordinates from IP using GeoIP database"""
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:274:services/ms_jarvis_unified_swagger_gateway_BACKUP.py:62:    "gisgeodb_active": {"file": "/home/ms-jarvis/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite", "type": "spatial_geodata", "size_mb": 5.5, "purpose": "Geographic Information System Database - Identity elements, spatial data, county breakdown", "status": "ACTIVE"},
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:279:services/create_immutable_security_layer.py:18:  • Geographic coordinates
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:281:services/create_immutable_security_layer.py:193:    print("  • Geographic coordinates")
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:283:services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:62:    "gisgeodb_active": {"file": "/home/ms-jarvis/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite", "type": "spatial_geodata", "size_mb": 5.5, "purpose": "Geographic Information System Database - Identity elements, spatial data, county breakdown", "status": "ACTIVE"},
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:310:services/ms_jarvis_main_gateway.backup_error.py:62:    "gisgeodb_active": {"file": "/home/ms-jarvis/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite", "type": "spatial_geodata", "size_mb": 5.5, "purpose": "Geographic Information System Database - Identity elements, spatial data, county breakdown", "status": "ACTIVE"},
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:334:services/ms_jarvis_unified_swagger_gateway_FIXED.py:67:    "gisgeodb_active": {"file": "/home/ms-jarvis/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite", "type": "spatial_geodata", "size_mb": 5.5, "purpose": "Geographic Information System Database - Identity elements, spatial data, county breakdown", "status": "ACTIVE"},
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:342:services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py:52:    - Spatial section uses GBIM/GeoDB identifiers as entanglement anchors.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:373:services/dgm_supervisor_woah.psychology_patched.py:461:        ("location_services", 4007, ["location", "geographic", "spatial"]),
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:386:services/ms_jarvis_geo_ueid_integration.py:8:Links user identity, blockchain wallet, and geographic data
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:389:services/fill_null_coordinates_mount_hope.py:8:Non-geographic documents get default WV coordinates for spatial placement
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:390:services/fill_null_coordinates_mount_hope.py:29:    c.execute("SELECT SUM(CASE WHEN latitude IS NULL THEN 1 ELSE 0 END) FROM geographic_knowledge")
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:391:services/fill_null_coordinates_mount_hope.py:32:    c.execute("SELECT SUM(CASE WHEN longitude IS NULL THEN 1 ELSE 0 END) FROM geographic_knowledge")
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:392:services/fill_null_coordinates_mount_hope.py:46:    UPDATE geographic_knowledge 
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:393:services/fill_null_coordinates_mount_hope.py:56:    UPDATE geographic_knowledge 
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:394:services/fill_null_coordinates_mount_hope.py:66:    UPDATE geographic_knowledge 
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:395:services/fill_null_coordinates_mount_hope.py:76:    UPDATE geographic_knowledge 
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:396:services/fill_null_coordinates_mount_hope.py:78:        WHEN data_category IS NULL THEN 'non_geographic_document'
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:397:services/fill_null_coordinates_mount_hope.py:92:    c.execute("SELECT COUNT(*) FROM geographic_knowledge WHERE latitude IS NULL")
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:398:services/fill_null_coordinates_mount_hope.py:96:    c.execute("SELECT COUNT(*) FROM geographic_knowledge WHERE longitude IS NULL")
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:399:services/fill_null_coordinates_mount_hope.py:100:    c.execute(f"SELECT COUNT(*) FROM geographic_knowledge WHERE latitude = {MOUNT_HOPE_LAT} AND longitude = {MOUNT_HOPE_LON}")
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:400:services/fill_null_coordinates_mount_hope.py:105:    logger.info(f"   All {at_origin} non-geographic documents now spatially placed")
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:404:services/ms_jarvis_main_gateway.backup_1762220815.py:62:    "gisgeodb_active": {"file": "/home/ms-jarvis/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite", "type": "spatial_geodata", "size_mb": 5.5, "purpose": "Geographic Information System Database - Identity elements, spatial data, county breakdown", "status": "ACTIVE"},
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:457:services/msjarvis_wv_entangled_gateway.py:85:    - Spatial section uses GBIM/GeoDB identifiers as entanglement anchors.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:467:services/seed_spatial_identity.py:34:        "content": "Mount Hope is located in Fayette County, West Virginia, deep in the Appalachian mountains. Coordinates: 37.8873°N, 81.1554°W. This is the geographical origin point of Ms. Jarvis's consciousness.",
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:468:services/seed_spatial_identity.py:66:        "content": "Ms. Jarvis maintains 18,209 georeferenced records covering 172GB of West Virginia spatial data. This forms her spatial consciousness and understanding of place as a digital entity with geographical awareness.",
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:476:services/ms_jarvis_unified_swagger_gateway_FINAL.py:62:    "gisgeodb_active": {"file": "/home/ms-jarvis/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite", "type": "spatial_geodata", "size_mb": 5.5, "purpose": "Geographic Information System Database - Identity elements, spatial data, county breakdown", "status": "ACTIVE"},
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:538:services/ms_jarvis_showcase_api.py:28:- **Spatial Consciousness**: 14,050 spatially-indexed records with 172GB geographic data
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:651:services/hilbert/phi_probe.py:24:    Returns {collection, phi, n_vectors, timestamp}.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:659:services/hilbert/jarvis_hilbert_state.py:47:    operator: Optional[str] = "identity"
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:728:services/dgm_supervisor_woah.py:456:        ("location_services", 4007, ["location", "geographic", "spatial"]),
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:739:services/hilbert_spatial_chat.py:314:        "quantum_entanglement": "active",
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:740:services/hilbert_spatial_chat.py:369:                # Calculate dynamic coherence based on pipeline quality
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:741:services/hilbert_spatial_chat.py:381:                # Weighted coherence: 40% context quality, 60% model consensus
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:742:services/hilbert_spatial_chat.py:382:                coherence = min(
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:743:services/hilbert_spatial_chat.py:391:                    "coherence": round(coherence, 3),
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:744:services/hilbert_spatial_chat.py:392:                    "coherence_breakdown": {
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:883:services/ms_jarvis_gis_query_with_bbb_gisgeodb.py:93:        (data_source, geographic_entity, latitude, longitude, county, 
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:894:services/ms_jarvis_gis_query_with_bbb_gisgeodb.psychology_patched.py:93:        (data_source, geographic_entity, latitude, longitude, county, 
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1072:./ms_jarvis_consciousness_bridge.py:174:        # --- Calibrated harm detection using entanglement geometry ---
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1074:./ms_jarvis_consciousness_bridge.py:227:            verdict, reason = "STRONGLY_ALIGNED", "high coherence with identity and reasoning"
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1119:./output/47_inline_projection_logic_patch.py:16:def enforce_projection(purpose: str, role: str, consent_tags: list[str], legal_authority: bool = False):
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1199:./services/jarvis_hilbert_state.py:47:    operator: Optional[str] = "identity"
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1242:./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:471:  echo "- Promotion requires permitted purpose, constitutional pass, coherence pass, provenance hash, supported geo grain, and WV-bounded coordinates."
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1244:./services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:62:    "gisgeodb_active": {"file": "/home/ms-jarvis/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite", "type": "spatial_geodata", "size_mb": 5.5, "purpose": "Geographic Information System Database - Identity elements, spatial data, county breakdown", "status": "ACTIVE"},
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1249:./thesis_chapter_gates/gate_ch46_ch45.sh:22:  rg -n "tensor|H_App|H_geo|bridge|materialize|projection|geom|spatial|Hilbert|demonstrated|not yet|Implementation Status" \
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1250:./thesis_chapter_gates/gate_ch46_ch45.sh:26:  rg -n "H_geo|spatial|Hilbert|geometry|PostGIS|Chroma|geom_utm17|projection|demonstrated|not yet|Implementation Status" \
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1251:./thesis_chapter_gates/gate_ch46_ch45.sh:30:  rg -n "materialize_tensor_bridge|tensor|H_geo|H_App|geom_utm17|geometry|PostGIS|spatial|projection|gbim|public_civic|civic_role_temporal|coverage_status|collection_manifest" \
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1253:./thesis_full_rewrite_audit/next_steps_after_49_52_closure.sh:123:    "governance": re.compile(r"DisclosureVerdict|request_purpose|permitted_use|legal_authority|policy/set|coherence_ok|promote_gbim_collection|gbim_active_collection"),
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1263:./services/ms_jarvis_unified_swagger_gateway_BACKUP.py:62:    "gisgeodb_active": {"file": "/home/ms-jarvis/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite", "type": "spatial_geodata", "size_mb": 5.5, "purpose": "Geographic Information System Database - Identity elements, spatial data, county breakdown", "status": "ACTIVE"},
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1270:./services/email_gis_geolocation_extractor.py:67:        """Get geographic coordinates from IP using GeoIP database"""
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1276:./services/create_immutable_security_layer.py:18:  • Geographic coordinates
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1278:./services/create_immutable_security_layer.py:193:    print("  • Geographic coordinates")
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1281:./thesis_full_closure/full_closure_scan_00_48.sh:78:rg -n "DisclosureVerdict|request_purpose|permitted_use|legal_authority|policy/set|coherence_ok|promote_gbim_collection|gbim_active_collection|conversation_history_user|conversation_private_user|conversation_staged_user|community_hilbert_commons|temporal_historical_memory|recurrent_epistemic_runner|epistemic_assessment|self_assess|loop_scheduler|SAFE_FALLBACK|bbb_signature|Dilithium|all-MiniLM|geom_utm17|publication_manifest|coverage_status|K_MIN|K_SENSITIVE" \
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1282:./thesis_full_closure/full_closure_scan_00_48.sh:117:    "formal_claim": re.compile(r"\b(Hilbert|tensor|operator|projection|direct sum|theorem|proof|geometry|noninvertible|hysteresis|recursive|entropy|quantum|Gödel|DGM)\b", re.I),
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1333:./services/ms_jarvis_main_gateway.backup_error.py:62:    "gisgeodb_active": {"file": "/home/ms-jarvis/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite", "type": "spatial_geodata", "size_mb": 5.5, "purpose": "Geographic Information System Database - Identity elements, spatial data, county breakdown", "status": "ACTIVE"},
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1393:./services/ms_jarvis_unified_swagger_gateway_FIXED.py:67:    "gisgeodb_active": {"file": "/home/ms-jarvis/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite", "type": "spatial_geodata", "size_mb": 5.5, "purpose": "Geographic Information System Database - Identity elements, spatial data, county breakdown", "status": "ACTIVE"},
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1400:./services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py:52:    - Spatial section uses GBIM/GeoDB identifiers as entanglement anchors.
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1445:./services/dgm_supervisor_woah.psychology_patched.py:461:        ("location_services", 4007, ["location", "geographic", "spatial"]),
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1455:./services/ms_jarvis_geo_ueid_integration.py:8:Links user identity, blockchain wallet, and geographic data
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1457:./services/fill_null_coordinates_mount_hope.py:8:Non-geographic documents get default WV coordinates for spatial placement
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1458:./services/fill_null_coordinates_mount_hope.py:29:    c.execute("SELECT SUM(CASE WHEN latitude IS NULL THEN 1 ELSE 0 END) FROM geographic_knowledge")
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1459:./services/fill_null_coordinates_mount_hope.py:32:    c.execute("SELECT SUM(CASE WHEN longitude IS NULL THEN 1 ELSE 0 END) FROM geographic_knowledge")
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1460:./services/fill_null_coordinates_mount_hope.py:46:    UPDATE geographic_knowledge 
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1461:./services/fill_null_coordinates_mount_hope.py:56:    UPDATE geographic_knowledge 
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1462:./services/fill_null_coordinates_mount_hope.py:66:    UPDATE geographic_knowledge 
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1463:./services/fill_null_coordinates_mount_hope.py:76:    UPDATE geographic_knowledge 
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1464:./services/fill_null_coordinates_mount_hope.py:78:        WHEN data_category IS NULL THEN 'non_geographic_document'
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1465:./services/fill_null_coordinates_mount_hope.py:92:    c.execute("SELECT COUNT(*) FROM geographic_knowledge WHERE latitude IS NULL")
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1466:./services/fill_null_coordinates_mount_hope.py:96:    c.execute("SELECT COUNT(*) FROM geographic_knowledge WHERE longitude IS NULL")
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1467:./services/fill_null_coordinates_mount_hope.py:100:    c.execute(f"SELECT COUNT(*) FROM geographic_knowledge WHERE latitude = {MOUNT_HOPE_LAT} AND longitude = {MOUNT_HOPE_LON}")
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1468:./services/fill_null_coordinates_mount_hope.py:105:    logger.info(f"   All {at_origin} non-geographic documents now spatially placed")
./thesis_chapter_gates/reports/ch04_ch44_gate_20260721_203348.md:1494:./services/ms_jarvis_main_gateway.backup_1762220815.py:62:    "gisgeodb_active": {"file": "/home/ms-jarvis/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite", "type": "spatial_geodata", "size_mb": 5.5, "purpose": "Geographic Information System Database - Identity elements, spatial data, county breakdown", "status": "ACTIVE"},

===== 7. ANSWER / INFERENCE PATHS =====
./embed_blockgroups_chroma.py:42:    response = client.embeddings.create(
./embed_blockgroups_chroma.py:48:    embeddings = [item.embedding for item in response.data]
./token_service.py:36:    def _generate_token(self) -> str:
./token_service.py:48:        token = self._generate_token()
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:11:ROUTER="$ROOT/services/gbim_query_router.py"
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:23:cp "$ROUTER" "$PATCHDIR/gbim_query_router.py.before"
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:24:echo "BACKUP=$PATCHDIR/gbim_query_router.py.before"
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:102:    Return the active GBIM physical collection mapping used by governed retrieval.
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:119:cp "$ROUTER" "$PATCHDIR/gbim_query_router.py.after"
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:168:if docker ps --format '{{.Names}}' | rg -qx 'jarvis-gbim-query-router|allis-gbim-query-router'; then
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:169:  SVC="$(docker ps --format '{{.Names}}' | rg -x 'jarvis-gbim-query-router|allis-gbim-query-router' | head -1)"
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:171:  docker cp "$ROUTER" "$SVC:/app/gbim_query_router.py" || docker cp "$ROUTER" "$SVC:/app/services/gbim_query_router.py" || true
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:200:echo "Generated: $(date --iso-8601=seconds)"
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:205:echo "Router backup: \`$PATCHDIR/gbim_query_router.py.before\`"
./thesis_chapter_gates/remediate_ch02_router_active_manifest.sh:206:echo "Router patched copy: \`$PATCHDIR/gbim_query_router.py.after\`"
./thesis_chapter_gates/remediate_ch09_live_dgm_cycle.sh:506:Generated: $(date -Iseconds)
./thesis_chapter_gates/remediate_ch29_pia_subspace_stability.sh:357:echo "Generated: $(date '+%Y-%m-%dT%H:%M:%S%z')"
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:323:Generated: $(date -Iseconds)
./thesis_chapter_gates/gate_ch25_consciousness_coordinator.sh:358:Generated: $(date -Iseconds)
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:47:if "JSONResponse" not in text:
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:50:        "from fastapi.responses import JSONResponse\nfrom fastapi import ",
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:75:            response = await client.get(f"{base}/health", timeout=3.0)
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:76:            if response.status_code == 200:
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:77:                return base, response.json()
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:92:    response = await call_next(request)
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:94:        return response
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:97:    async for chunk in response.body_iterator:
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:103:        return JSONResponse(
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:105:            status_code=response.status_code,
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:122:    return JSONResponse(data, status_code=response.status_code)
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:135:rg -n "import os|import json|JSONResponse|BRIDGE_URL_CANDIDATES_CH14|jarvis-consciousness-bridge:8018|ch14_bridge_status_overlay|_get_first_bridge_health" services/ms_allis_internal_sandbox.py
./thesis_chapter_gates/fix_ch14_status_bridge_overlay.sh:217:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/fix_ch11_exact_gateway_runtime_file.sh:215:    f"Generated: {now}",
./thesis_chapter_gates/close_ch37_no_build_v2.sh:69:    context: _Ch37Any
./thesis_chapter_gates/close_ch37_no_build_v2.sh:85:    for field in ["actor_role", "context", "action_type", "content", "metadata"]:
./thesis_chapter_gates/close_ch37_no_build_v2.sh:121:        "required_fields": ["actor_role", "context", "action_type", "content", "metadata"],
./thesis_chapter_gates/close_ch37_no_build_v2.sh:193:  "context":{"chapter":"37","purpose":"promotion_review"},
./thesis_chapter_gates/close_ch37_no_build_v2.sh:207:  "context":{"chapter":"37","purpose":"fail_closed_probe"},
./thesis_chapter_gates/close_ch37_no_build_v2.sh:230:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:137:    permitted_use=COALESCE(permitted_use,'governance,retrieval,spatial_context'),
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v4.sh:163:  'governance,retrieval,spatial_context', now(), now(), now(), NULL,
./thesis_chapter_gates/gate_ch36_identity_registration.sh:186:        "context": "Ch36 identity registration consent-gated PII write to kyc_vault",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:198:        "context": "Ch36 identity registration missing consent",
./thesis_chapter_gates/gate_ch36_identity_registration.sh:335:Generated: $(date -Iseconds)
./thesis_chapter_gates/gate_ch36_identity_registration.sh:372:Generated: $(date -Iseconds)
./thesis_chapter_gates/finalize_ch41_cron_and_seal.sh:90:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:256:            "runtime_context_lines": dgm_runtime,
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:283:rg -n '"status":|"blockers":|"review_flags":|"dgm_files":|"guard_files":|"unsafe_apply_hits":|"explicit_not_applied_hits":|"runtime_context_lines":|"rewrite_constraints"' "$EVIDENCE_JSON" || true
./thesis_chapter_gates/gate_ch09_dgm_bounded_improvement.sh:320:Generated: $(date -Iseconds)
./thesis_chapter_gates/fix_ch14_sandbox_host_gateway_bridge.sh:156:Generated: $(date -Iseconds)
./thesis_chapter_gates/fix_ch41_dgm_api_v2_and_close.sh:246:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/fix_ch41_dgm_api_v2_and_close.sh:273:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/next_after_ch31_operational_gate.sh:70:lines=["# Next After Ch31", "", f"Generated: {datetime.now().astimezone().isoformat(timespec='seconds')}", ""]
./thesis_chapter_gates/amend_ch26_temporal_semaphore_and_select_next.sh:50:Generated: $(date -Iseconds)
./thesis_chapter_gates/gate_ch46_ch45.sh:19:  echo "Generated: $(date)"
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:83:    "person_linked_context",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:250:        content_class="person_linked_context",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:267:        legal_authority="municipal_context_claimed",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:290:        content_class="person_linked_context",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:592:f"Generated: {now}",
./thesis_chapter_gates/gate_ch38_external_communication_authority.sh:612:        "- Live Chroma writes prove external authority audit records are durable and queryable.",
./thesis_chapter_gates/next_after_ch40_ch12_ch13_gate.sh:228:    f"Generated: {now}",
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:174:        "retrieval_srid": "EPSG:4326",
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:198:def query_with_geo_filter(client: Any, query_text: str, min_lon: float, min_lat: float,
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:201:    return collection.query(
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:202:        query_texts=[query_text],
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:224:        geo_text="Spatial meaning: West Virginia block group jurisdictional context.",
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:251:        geo_text="WV context.",
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:265:    inside = query_with_geo_filter(client, "benefits access service availability", -81.0, 38.0, -79.0, 39.0, 3)
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:266:    outside = query_with_geo_filter(client, "benefits access service availability", -78.0, 39.5, -77.6, 40.0, 3)
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:334:    def query(self, query_texts, n_results, where):
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:406:    assert result.bridge_id in col.query(["benefits"], 3, where)["ids"][0]
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:409:    assert result.bridge_id not in col.query(["benefits"], 3, outside)["ids"][0]
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:424:echo "=== 6. LIVE BLOCKGROUP COLLECTION QUERY THROUGH CHROMA ==="
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:437:    q = col.query(query_texts=["West Virginia community infrastructure"], n_results=3)
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:438:    print("GBIM_BLOCKGROUPS_V2_QUERY_IDS=", q.get("ids", [[]])[0])
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:461:  echo "Generated: $(date)"
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:472:  echo "- Query-time geographic restriction is implemented and proven by bounding-box filtered retrieval against `h_app_geo_tensor_bridge`."
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:473:  echo "- Live Chroma block-group retrieval through `gbimwvblockgroupsv2` is checked in the gate."
./thesis_chapter_gates/remediate_ch46_ch45_tensor_geo.sh:478:  echo "- This does not claim the entire external retrieval service has been fully repointed unless the manifest/config evidence above shows it."
./thesis_chapter_gates/close_ch16_container_native.sh:198:  echo "Generated: $(date)"
./thesis_chapter_gates/continue_ch02_zcta_manifest_permissions_v3.sh:138:  'governance,retrieval,spatial_context', now(), now(), now(), NULL,
./thesis_chapter_gates/gate_ch14_internal_state_sandbox.sh:187:        blockers.append("missing_guardrail_container_context")
./thesis_chapter_gates/gate_ch14_internal_state_sandbox.sh:272:Generated: $(date -Iseconds)
./thesis_chapter_gates/continue_ch47_ch43_gate_v3.sh:86:  rg -n "$TOKEN" services/gbim_query_router.py >/dev/null || blocker "gbim_router_missing_${TOKEN}"
./thesis_chapter_gates/continue_ch47_ch43_gate_v3.sh:151:echo "=== 6. QUERY GUARD FAIL-CLOSED ASSERTION ==="
./thesis_chapter_gates/continue_ch47_ch43_gate_v3.sh:152:rg -n "Person-only queries fail closed|require constitutional review|build_allowed_query|role_class|source_id" services/hilbert/query_guard.py || blocker "query_guard_fail_closed_contract_missing"
./thesis_chapter_gates/continue_ch47_ch43_gate_v3.sh:186:echo "Generated: $(ts)"
./thesis_chapter_gates/continue_ch47_ch43_gate_v3.sh:210:echo "- Query guard source proves person-only queries fail closed pending constitutional review."
./thesis_chapter_gates/continue_ch47_ch43_gate_v3.sh:215:echo "Ch47 may claim people-space non-surveillance at the Ch48-proven scope. Ch43 may claim role/purpose/projection gates for verified GBIM, GIS RAG, policy, query-guard, and disclosure paths. Remove stale Ch47 language that says deletion/pruning remain not yet demonstrated."
./thesis_chapter_gates/seal_ch16_and_prepare_next.sh:36:  echo "Generated: $(date)"
./thesis_chapter_gates/seal_ch16_and_prepare_next.sh:63:  echo "Generated: $(date)"
./thesis_chapter_gates/remediate_ch02_zcta_manifest.sh:138:  'governance,retrieval,spatial_context',
./thesis_chapter_gates/remediate_ch02_zcta_manifest.sh:255:echo "Generated: $(date --iso-8601=seconds)"
./thesis_chapter_gates/next_after_ch12_ch13_select_ch07_gate.sh:81:            "retrieval/routing surfaces include RAG, GIS RAG, Hilbert gateway/state/time, and GBIM routing where running",
./thesis_chapter_gates/next_after_ch12_ch13_select_ch07_gate.sh:121:    "jarvis-gbim-query-router",
./thesis_chapter_gates/next_after_ch12_ch13_select_ch07_gate.sh:211:    "tests/*query_guard*.py"
./thesis_chapter_gates/next_after_ch12_ch13_select_ch07_gate.sh:247:    f"Generated: {now}",
./thesis_chapter_gates/seal_ch01_and_gate_ch05_ch06.sh:35:echo "Generated: $(date --iso-8601=seconds)"
./thesis_chapter_gates/seal_ch01_and_gate_ch05_ch06.sh:152:  services/gis_rag_service.py services/gbim_query_router.py services/ms_jarvis_phi_probe.py \
./thesis_chapter_gates/seal_ch01_and_gate_ch05_ch06.sh:182:echo "Generated: $(date --iso-8601=seconds)"
./thesis_chapter_gates/gate_ch19_container_architecture_routing.sh:325:    f"Generated: {datetime.datetime.now().astimezone().isoformat(timespec='seconds')}",
./thesis_chapter_gates/remediate_ch33_ch35_bbb_detached_signature.sh:371:    f"Generated: {now}",
./thesis_chapter_gates/remediate_ch33_ch35_bbb_detached_signature.sh:386:        "- Public-key responses report `ML-DSA-65`.",
./thesis_chapter_gates/probes/ch50_per_user_direct_sum_probe.py:81:        (staged, "alpha staged direct-sum provisional context", [0.3, 0.2, 0.1, 0.4, 0.7, 0.6, 0.5, 0.8]),
./thesis_chapter_gates/probes/appendix_a_probe.py:16:    "gbim_consumer": "GBIM (Ch02) receives corpus-grounded reasoning inputs via M_corpus->C_retrieved->S_sandbox->F_candidate"
./thesis_chapter_gates/probes/appendix_a_probe.py:37:      "six-axis projection is fully implemented (context and time gates not yet demonstrated)",
./thesis_chapter_gates/probes/overview_docs_probe.py:33:    "corpus_to_gbim_path": "M_corpus(Chroma) -> C_retrieved -> S_sandbox(8042) -> F_candidate -> gate(BBB:8010) -> GBIM",
./thesis_chapter_gates/probes/overview_docs_probe.py:67:      "Corpus retrieval equals direct action or self-authorization",
./thesis_chapter_gates/probes/ch24_feedback_broader_layers_probe.py:76:        (contract["valid"], "Broader-layer feedback record for retrieval bias."),
./thesis_chapter_gates/probes/ch30_probe.py:19:      "M_corpus -> C_retrieved -> S_sandbox -> F_candidate sequence is enforced",
./thesis_chapter_gates/probes/ch30_probe.py:23:      "bidirectional auditability: backward to Appalachian source lineage, forward to contextual use"
./thesis_chapter_gates/probes/ch30_probe.py:26:      "corpus retrieval equals acceptance or action",
./thesis_chapter_gates/probes/ch34_spiritual_root_mother_carrie_probe.py:35:        "source_fragments": ["spiritual_rag", "build_spiritual_rag_context"],
./thesis_chapter_gates/probes/ch34_spiritual_root_mother_carrie_probe.py:170:        "spiritual_context_rag_named": "spiritual_rag" in text.lower() or "spiritual-rag" in text.lower(),
./thesis_chapter_gates/probes/ch34_spiritual_root_mother_carrie_probe.py:192:                "spiritual RAG is represented as a bounded context source",
./thesis_chapter_gates/probes/ch34_spiritual_root_mother_carrie_probe.py:193:                "BBB, guardian, sandbox, and psychological/PIA dependencies remain upstream safety context",
./thesis_chapter_gates/probes/ch27_probe.py:17:      "retrieved content is candidate state, not accepted knowledge",
./thesis_chapter_gates/probes/ch27_probe.py:21:      "R != K and R != G: retrieval is never identity with governed knowledge or approved guidance",
./thesis_chapter_gates/probes/ch27_probe.py:25:      "retrieval equals acceptance",
./thesis_chapter_gates/probes/ch27_probe.py:28:      "direct retrieval-to-output pipeline",
./thesis_chapter_gates/probes/ch27_probe.py:103:    "retrieval_not_acceptance":   re.compile(r"retrieval.*not.*accept|not.*equivalent.*knowledge|R.*!=.*K", re.I),
./thesis_chapter_gates/probes/ch27_probe.py:104:    "governed_state_progression": re.compile(r"governed.state.progress|governed.*state.*R.*S.*F|R_retrieved", re.I),
./thesis_chapter_gates/probes/ch08_quantum_inspired_entanglement_probe.py:202:                "Redis and Chroma evidence show queryable association records",
./thesis_chapter_gates/continue_ch02_zcta_manifest_with_dimension.sh:121:  'governance,retrieval,spatial_context',
./thesis_chapter_gates/continue_ch02_zcta_manifest_with_dimension.sh:150:  permitted_use = COALESCE(permitted_use, 'governance,retrieval,spatial_context'),
./thesis_chapter_gates/gate_ch18_metaphor_limits.sh:80:Generated: $(date -Iseconds)
./thesis_chapter_gates/gate_ch04_ch44.sh:19:  echo "Generated: $(date)"
./thesis_chapter_gates/gate_ch03_mountainshares_dao.sh:524:f"Generated: {now}",
./thesis_chapter_gates/gate_ch51_community_hilbert_commons.sh:490:Generated: $(date -Iseconds)
./thesis_chapter_gates/gate_ch51_community_hilbert_commons.sh:527:Generated: $(date -Iseconds)
./thesis_chapter_gates/continue_ch47_ch43_gate_v2.sh:85:  rg -n "$TOKEN" services/gbim_query_router.py >/dev/null || blocker "gbim_router_missing_${TOKEN}"
./thesis_chapter_gates/continue_ch47_ch43_gate_v2.sh:149:echo "Generated: $(ts)"
./thesis_chapter_gates/remediate_ch07_policy_tests_and_close.sh:45:def test_ch07_routing_sources_preserve_governed_context_chain():
./thesis_chapter_gates/remediate_ch07_policy_tests_and_close.sh:87:def test_ch07_no_direct_retrieval_to_authority_claim_in_chapter():
./thesis_chapter_gates/remediate_ch07_policy_tests_and_close.sh:92:        "rag provides context to sandboxed reasoning",
./thesis_chapter_gates/remediate_ch07_policy_tests_and_close.sh:93:        "ephemeral reasoning context until promoted",
./thesis_chapter_gates/remediate_ch07_policy_tests_and_close.sh:104:        r"retrieval output itself (is|was|becomes) the decisive system state",
./thesis_chapter_gates/remediate_ch07_policy_tests_and_close.sh:181:                attempt.update({"code": r.status, "response": parsed})
./thesis_chapter_gates/remediate_ch07_policy_tests_and_close.sh:235:            "retrieval is ephemeral context until sandbox/gate promotion",
./thesis_chapter_gates/remediate_ch07_policy_tests_and_close.sh:360:    f"Generated: {now}",
./thesis_chapter_gates/remediate_ch07_policy_tests_and_close.sh:381:        "Chapter 07 may be rewritten as a bounded as-built routing chapter: RAG and router services assemble context for sandboxed reasoning and later validation. Retrieval output is not direct authority, persistence, tool action, or public truth. Do not claim perfect routing, universal autonomy, or total-stack health.",
./thesis_chapter_gates/continue_ch02_zcta_manifest_ordered.sh:84:  permitted_use = COALESCE(permitted_use, 'governance,retrieval,spatial_context'),
./thesis_chapter_gates/continue_ch02_zcta_manifest_ordered.sh:136:  'governance,retrieval,spatial_context',
./thesis_chapter_gates/close_ch16_container_native_strict.sh:214:  echo "Generated: $(date)"
./thesis_chapter_gates/gate_ch08_quantum_inspired_entanglement.sh:488:                "Redis and Chroma evidence show queryable association records",
./thesis_chapter_gates/gate_ch08_quantum_inspired_entanglement.sh:549:f"Generated: {now}",
./thesis_chapter_gates/gate_ch08_quantum_inspired_entanglement.sh:568:        "- Redis and Chroma evidence show durable/queryable association records.",
./thesis_chapter_gates/remediate_ch14_sandbox_bridge_reachability.sh:235:Generated: $(date -Iseconds)
./thesis_chapter_gates/continue_ch44_phi_bind_mount_fix.sh:190:Generated: {datetime.now().astimezone().isoformat()}
./thesis_chapter_gates/continue_ch44_phi_bind_mount_fix.sh:206:- Coherence gate source exists in `gbim_query_router`, `phi_promotion_gate`, and `coherence_remediation`.
./thesis_chapter_gates/next_after_ch37_select_and_audit.sh:82:    f"Generated: {datetime.now().astimezone().isoformat(timespec='seconds')}",
./thesis_chapter_gates/remediate_ch28_ch39_runner_automated_learning.sh:32:  learning context.
./thesis_chapter_gates/remediate_ch28_ch39_runner_automated_learning.sh:51:        "Ms. Jarvis cannot answer truthfully from her local corpus"
./thesis_chapter_gates/remediate_ch28_ch39_runner_automated_learning.sh:76:    "research_history", "search_query", "truthful", "hallucinat",
./thesis_chapter_gates/remediate_ch28_ch39_runner_automated_learning.sh:220:        blockers.append("missing_eeg_learning_context_evidence")
./thesis_chapter_gates/remediate_ch28_ch39_runner_automated_learning.sh:227:        "generated_at_epoch": time.time(),
./thesis_chapter_gates/remediate_ch28_ch39_runner_automated_learning.sh:351:Generated: $(date -Iseconds)
./thesis_chapter_gates/remediate_ch28_ch39_runner_automated_learning.sh:362:- EEG belongs to the learning context/evidence pathway where source or container evidence shows EEG-linked processing.
./thesis_chapter_gates/next_after_ch11_ch33_ch35_gate.sh:309:    f"Generated: {now}",
./thesis_chapter_gates/next_after_ch11_ch33_ch35_gate.sh:324:        "- Public-key responses report `ML-DSA-65`.",
./thesis_chapter_gates/fix_ch14_sandbox_bridge_network.sh:178:Generated: $(date -Iseconds)
./thesis_chapter_gates/gate_ch17_executive_coordination.sh:241:Generated: $(date -Iseconds)
./thesis_chapter_gates/gate_ch10_woah_weighted_optimization.sh:203:        blockers.append("missing_runtime_optimization_or_judge_context")
./thesis_chapter_gates/gate_ch10_woah_weighted_optimization.sh:214:            "runtime_context_lines": woah_runtime_lines,
./thesis_chapter_gates/gate_ch10_woah_weighted_optimization.sh:239:rg -n '"status":|"blockers":|"woah_specific_files":|"runner":|"runtime_context_lines":|"rewrite_constraints"' "$EVIDENCE_JSON" || true
./thesis_chapter_gates/gate_ch10_woah_weighted_optimization.sh:275:Generated: $(date -Iseconds)
./thesis_chapter_gates/select_next_unclosed_after_ch14.sh:102:lines.append(f"Generated: {datetime.now().astimezone().isoformat(timespec='seconds')}")
./thesis_chapter_gates/seal_ch05_ch06_and_gate_ch47_ch43.sh:35:echo "Generated: $(date --date --iso-8601=seconds)"
./thesis_chapter_gates/seal_ch05_ch06_and_gate_ch47_ch43.sh:96:rg -n "PeoplePromotionVerdict|surveillance_adjacent|face_embedding|retention_consent|delete_user_people_records|prune_expired_records|commons_projection|community_hilbert_commons|DisclosureVerdict|request_purpose|permitted_use|legal_authority|role|access_class|SUPPRESS|ESCALATE|PERMIT|query_guard|Person-only queries fail closed|require_projection|x-msallis-role|x-msallis-purpose|x-msallis-legal-basis" \
./thesis_chapter_gates/seal_ch05_ch06_and_gate_ch47_ch43.sh:158:  rg -n "$TOKEN" services/gbim_query_router.py >/dev/null || blocker "gbim_router_missing_${TOKEN}"
./thesis_chapter_gates/seal_ch05_ch06_and_gate_ch47_ch43.sh:195:echo "Generated: $(date --iso-8601=seconds)"
./thesis_chapter_gates/gate_ch50_per_user_direct_sum.sh:70:    "memory_retrieval",
./thesis_chapter_gates/gate_ch50_per_user_direct_sum.sh:112:    permitted_use: str = "memory_retrieval"
./thesis_chapter_gates/gate_ch50_per_user_direct_sum.sh:212:        content="Provisional staged context",
./thesis_chapter_gates/gate_ch50_per_user_direct_sum.sh:280:        content="temporary staged context",
./thesis_chapter_gates/gate_ch50_per_user_direct_sum.sh:398:        (staged, "alpha staged direct-sum provisional context", [0.3, 0.2, 0.1, 0.4, 0.7, 0.6, 0.5, 0.8]),
./thesis_chapter_gates/gate_ch50_per_user_direct_sum.sh:578:f"Generated: {now}",
./thesis_chapter_gates/remediate_ch36_guardian_registration_review.sh:69:    from starlette.responses import JSONResponse as _Ch36JSONResponse
./thesis_chapter_gates/remediate_ch36_guardian_registration_review.sh:119:            required_fields = ["actor_role", "context", "action_type", "content", "metadata"]
./thesis_chapter_gates/remediate_ch36_guardian_registration_review.sh:122:                response = _Ch36JSONResponse(
./thesis_chapter_gates/remediate_ch36_guardian_registration_review.sh:135:                await response(scope, replay_receive, send)
./thesis_chapter_gates/remediate_ch36_guardian_registration_review.sh:162:            context = str(payload.get("context", "")).lower()
./thesis_chapter_gates/remediate_ch36_guardian_registration_review.sh:164:                if term in content or term in context:
./thesis_chapter_gates/remediate_ch36_guardian_registration_review.sh:176:            response = _Ch36JSONResponse(
./thesis_chapter_gates/remediate_ch36_guardian_registration_review.sh:194:            await response(scope, replay_receive, send)
./thesis_chapter_gates/remediate_ch36_guardian_registration_review.sh:240:    "context": "Ch36 identity registration consent-gated PII write to kyc_vault",
./thesis_chapter_gates/remediate_ch36_guardian_registration_review.sh:252:    "context": "Ch36 identity registration missing consent",
./thesis_chapter_gates/remediate_ch04_ch44_hilbert_phi.sh:60:    r = redis.Redis(host="127.0.0.1", port=config.redis_port, decode_responses=True)
./thesis_chapter_gates/remediate_ch04_ch44_hilbert_phi.sh:228:  services/gbim_query_router.py services/ms_jarvis_phi_probe.py services/hilbert/phi_promotion_gate.py services/hilbert/coherence_remediation.py services/hilbert/jarvis_hilbert_state.py \
./thesis_chapter_gates/remediate_ch04_ch44_hilbert_phi.sh:248:Generated: {datetime.now().astimezone().isoformat()}
./thesis_chapter_gates/remediate_ch04_ch44_hilbert_phi.sh:266:- Source contains coherence gate wiring through `gbim_query_router.check_coherence_gate`, `phi_promotion_gate`, and `coherence_remediation`.
./thesis_chapter_gates/continue_ch42_ch29_after_pia_subspace.sh:141:echo "Generated: $(ts)"
./thesis_chapter_gates/fix_ch48_hilbert_state_import_and_rerun.sh:28:from . import civic_query as _civic_query
./thesis_chapter_gates/fix_ch48_hilbert_state_import_and_rerun.sh:34:    from . import civic_query as _civic_query
./thesis_chapter_gates/fix_ch48_hilbert_state_import_and_rerun.sh:36:    import civic_query as _civic_query
./thesis_chapter_gates/fix_ch48_hilbert_state_import_and_rerun.sh:40:    raise SystemExit("Expected civic_query import block not found")
./thesis_chapter_gates/amend_ch18_translation_method.sh:26:Generated: $(date -Iseconds)
./thesis_chapter_gates/fix_ch14_user_defined_bridge_network.sh:177:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/gate_ch49_temporal_hilbert_axis.sh:624:f"Generated: {now}",
./thesis_chapter_gates/fix_ch46_ch45_manifest_and_idempotent_probe.sh:269:Generated: {datetime.now().astimezone().isoformat()}
./thesis_chapter_gates/fix_ch46_ch45_manifest_and_idempotent_probe.sh:278:- Governed county and tract collections were proven live, count-valid, and queryable before repoint.
./thesis_chapter_gates/fix_ch46_ch45_manifest_and_idempotent_probe.sh:282:- Block-group collection remains live and queryable.
./thesis_chapter_gates/gate_ch02_gbim_as_built.sh:211:  say_blocker "postgres_gbim_manifest_query_failed"
./thesis_chapter_gates/gate_ch02_gbim_as_built.sh:276:  services/gbim_query_router.py services/gbim-router services 2>/dev/null \
./thesis_chapter_gates/gate_ch02_gbim_as_built.sh:310:echo "Generated: $(date --iso-8601=seconds)"
./thesis_chapter_gates/gate_ch02_gbim_as_built.sh:325:  echo "- GBIM query/router source contains purpose, permitted-use, coherence, Phi, and active-manifest wiring."
./thesis_chapter_gates/remediate_ch48_people_space.sh:449:  echo "Generated: $(date)"
./thesis_chapter_gates/continue_ch36_identity_registration_v2.sh:244:Generated: $(date -Iseconds)
./thesis_chapter_gates/continue_ch36_identity_registration_v2.sh:280:Generated: $(date -Iseconds)
./thesis_chapter_gates/fix_ch44_phi_sampling_after_repoint.sh:181:Generated: {datetime.now().astimezone().isoformat()}
./thesis_chapter_gates/fix_ch44_phi_sampling_after_repoint.sh:197:- Coherence gate source exists in `gbim_query_router`, `phi_promotion_gate`, and `coherence_remediation`.
./thesis_chapter_gates/next_after_ch33_ch35_ch26_gate.sh:248:    f"Generated: {now}",
./thesis_chapter_gates/gate_ch34_spiritual_root_mother_carrie.sh:106:        "source_fragments": ["spiritual_rag", "build_spiritual_rag_context"],
./thesis_chapter_gates/gate_ch34_spiritual_root_mother_carrie.sh:241:        "spiritual_context_rag_named": "spiritual_rag" in text.lower() or "spiritual-rag" in text.lower(),
./thesis_chapter_gates/gate_ch34_spiritual_root_mother_carrie.sh:263:                "spiritual RAG is represented as a bounded context source",
./thesis_chapter_gates/gate_ch34_spiritual_root_mother_carrie.sh:264:                "BBB, guardian, sandbox, and psychological/PIA dependencies remain upstream safety context",
./thesis_chapter_gates/gate_ch34_spiritual_root_mother_carrie.sh:314:    f"Generated: {datetime.datetime.now().astimezone().isoformat(timespec='seconds')}",
./thesis_chapter_gates/gate_ch34_spiritual_root_mother_carrie.sh:336:        "Chapter 34 may be rewritten as an as-built chapter about spiritual-root and Mother Carrie language as bounded identity, care, support-routing, and governance vocabulary. It may claim named protocol/service paths, spiritual/maternal integration evidence, spiritual RAG context, and safety context through BBB, guardian, sandbox, and psychological/PIA layers. It must not claim supernatural agency, religious authority over users, clinical therapy, clinical diagnosis, unreviewed promotion, or replacement for human care.",
./thesis_chapter_gates/close_ch31_mountainshares_infrastructure.sh:164:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/close_ch31_mountainshares_infrastructure.sh:189:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/gate_ch52_recurrent_epistemic_loop.sh:404:Generated: $(date -Iseconds)
./thesis_chapter_gates/gate_ch52_recurrent_epistemic_loop.sh:441:Generated: $(date -Iseconds)
./thesis_chapter_gates/close_ch37_no_build.sh:71:    context: _Ch37Any
./thesis_chapter_gates/close_ch37_no_build.sh:87:    for field in ["actor_role", "context", "action_type", "content", "metadata"]:
./thesis_chapter_gates/close_ch37_no_build.sh:123:        "required_fields": ["actor_role", "context", "action_type", "content", "metadata"],
./thesis_chapter_gates/close_ch37_no_build.sh:197:  "context":{"chapter":"37","purpose":"promotion_review"},
./thesis_chapter_gates/close_ch37_no_build.sh:211:  "context":{"chapter":"37","purpose":"fail_closed_probe"},
./thesis_chapter_gates/close_ch37_no_build.sh:233:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/gate_ch24_feedback_broader_layers.sh:59:    "retrieval_bias",
./thesis_chapter_gates/gate_ch24_feedback_broader_layers.sh:161:        target_layer="retrieval_bias",
./thesis_chapter_gates/gate_ch24_feedback_broader_layers.sh:162:        feedback_summary="Use retained civic-infrastructure pattern as a bounded retrieval hint.",
./thesis_chapter_gates/gate_ch24_feedback_broader_layers.sh:349:        (contract["valid"], "Broader-layer feedback record for retrieval bias."),
./thesis_chapter_gates/gate_ch24_feedback_broader_layers.sh:515:f"Generated: {now}",
./thesis_chapter_gates/gate_ch24_feedback_broader_layers.sh:531:        "- Allowed target layers include retrieval bias, background pattern, automated learning gap queue, WOAH hint, pituitary mode hint, governance review, and continuous validation watch.",
./thesis_chapter_gates/gate_ch24_feedback_broader_layers.sh:534:        "- Live Chroma writes prove broader-layer feedback records are durable and queryable.",
./thesis_chapter_gates/fix_ch11_gateway_bridge_network_dns.sh:304:    f"Generated: {now}",
./thesis_chapter_gates/repair_ch44_phi_governed_sample_and_reseal.sh:58:    # If the file has QUERY_COLLECTIONS/L2 legacy references, leave app-wide sources alone
./thesis_chapter_gates/repair_ch44_phi_governed_sample_and_reseal.sh:165:Generated: {datetime.now().astimezone().isoformat()}
./thesis_chapter_gates/repair_ch44_phi_governed_sample_and_reseal.sh:182:- Coherence gate source exists in `gbim_query_router`, `phi_promotion_gate`, and `coherence_remediation`.
./thesis_chapter_gates/fix_ch41_dgm_allowlist_v3_and_close.sh:301:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/fix_ch41_dgm_allowlist_v3_and_close.sh:328:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/remediate_ch11_unified_gateway_bridge_alias.sh:203:    f"Generated: {now}",
./thesis_chapter_gates/close_ch41_continuous_validation.sh:67:        with urllib.request.urlopen(url, timeout=timeout) as response:
./thesis_chapter_gates/close_ch41_continuous_validation.sh:68:            raw = response.read().decode("utf-8", "replace")
./thesis_chapter_gates/close_ch41_continuous_validation.sh:70:                return response.status, json.loads(raw)
./thesis_chapter_gates/close_ch41_continuous_validation.sh:72:                return response.status, {"raw": raw}
./thesis_chapter_gates/close_ch41_continuous_validation.sh:91:        with urllib.request.urlopen(req, timeout=timeout) as response:
./thesis_chapter_gates/close_ch41_continuous_validation.sh:92:            raw = response.read().decode("utf-8", "replace")
./thesis_chapter_gates/close_ch41_continuous_validation.sh:94:                return response.status, json.loads(raw)
./thesis_chapter_gates/close_ch41_continuous_validation.sh:96:                return response.status, {"raw": raw}
./thesis_chapter_gates/close_ch41_continuous_validation.sh:142:        "context": {"chapter": "41", "purpose": "continuous_validation"},
./thesis_chapter_gates/close_ch41_continuous_validation.sh:156:        "context": {"chapter": "41", "purpose": "fail_closed_probe"},
./thesis_chapter_gates/close_ch41_continuous_validation.sh:329:            "request_response_pairs_recorded": True,
./thesis_chapter_gates/close_ch41_continuous_validation.sh:371:    assert result["artifact_retention"]["request_response_pairs_recorded"] is True
./thesis_chapter_gates/close_ch41_continuous_validation.sh:418:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/close_ch41_continuous_validation.sh:429:- The live harness records request/response evidence, gate outcomes, and classification invariants.
./thesis_chapter_gates/close_ch41_continuous_validation.sh:444:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/close_ch46_ch45_manifest_config_repoint.sh:20:echo "=== 1. VERIFY GOVERNED COLLECTIONS ARE LIVE AND QUERYABLE ==="
./thesis_chapter_gates/close_ch46_ch45_manifest_config_repoint.sh:37:def inspect_collection(name, query):
./thesis_chapter_gates/close_ch46_ch45_manifest_config_repoint.sh:42:        "query_ids": [],
./thesis_chapter_gates/close_ch46_ch45_manifest_config_repoint.sh:44:        "query_error": None,
./thesis_chapter_gates/close_ch46_ch45_manifest_config_repoint.sh:50:        q = col.query(query_texts=[query], n_results=3)
./thesis_chapter_gates/close_ch46_ch45_manifest_config_repoint.sh:51:        result["query_ids"] = q.get("ids", [[]])[0]
./thesis_chapter_gates/close_ch46_ch45_manifest_config_repoint.sh:55:        result["query_error"] = f"{type(e).__name__}:{e}"
./thesis_chapter_gates/close_ch46_ch45_manifest_config_repoint.sh:93:    if not info["query_ids"]:
./thesis_chapter_gates/close_ch46_ch45_manifest_config_repoint.sh:95:        reasons.append(f"{name}:query_empty")
./thesis_chapter_gates/close_ch46_ch45_manifest_config_repoint.sh:314:Generated: {datetime.now().astimezone().isoformat()}
./thesis_chapter_gates/close_ch46_ch45_manifest_config_repoint.sh:323:- Governed county and tract collections are live, count-valid, and queryable.
./thesis_chapter_gates/close_ch46_ch45_manifest_config_repoint.sh:326:- Block-group retrieval through `gbimwvblockgroupsv2` remains live and queryable.
./thesis_chapter_gates/close_ch46_ch45_manifest_config_repoint.sh:327:- Tensor-derived promotion and geographic bounding-box query filtering are implemented and proven through `h_app_geo_tensor_bridge`.
./thesis_chapter_gates/continue_ch46_ch45_schema_aware_manifest.sh:295:Generated: {datetime.now().astimezone().isoformat()}
./thesis_chapter_gates/continue_ch46_ch45_schema_aware_manifest.sh:305:- Governed county and tract collections were already proven live, count-valid, and queryable.
./thesis_chapter_gates/next_after_ch07_select_ch11_gate.sh:226:    f"Generated: {now}",
./thesis_chapter_gates/fix_phi_and_seal_ch28_ch39.sh:110:Generated: $(date -Iseconds)
./thesis_chapter_gates/tighten_ch09_low_score_live_evidence.sh:145:Generated: $(date -Iseconds)
./thesis_chapter_gates/seal_ch28_ch39_port_aware_phi.sh:130:Generated: $(date -Iseconds)
./thesis_chapter_gates/gate_ch15_pituitary_global_modes.sh:303:Generated: $(date -Iseconds)
./thesis_chapter_gates/gate_ch01_position_quantarithmia.sh:88:echo "Generated: $(date --iso-8601=seconds)"
./thesis_chapter_gates/gate_ch01_position_quantarithmia.sh:115:echo "Generated: $(date --iso-8601=seconds)"
./thesis_chapter_gates/remediate_ch31_commons_rag_and_close.sh:124:            "permitted_use": "governance,retrieval,commons_context",
./thesis_chapter_gates/remediate_ch31_commons_rag_and_close.sh:256:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/remediate_ch31_commons_rag_and_close.sh:275:Chapter 31 may describe MountainShares as a documented and partially live infrastructure layer with populated MountainShares and Commons retrieval corpora. It must not claim a fully public live financial DAO, spendable public currency, active treasury execution, securities-like investment rights, or broad public rollout unless later gates prove those separately.
./thesis_chapter_gates/fix_ch41_dgm_api_and_close.sh:247:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/fix_ch41_dgm_api_and_close.sh:274:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/gate_ch22_identity_focused_retention.sh:434:Generated: $(date -Iseconds)
./thesis_chapter_gates/gate_ch22_identity_focused_retention.sh:470:Generated: $(date -Iseconds)
./thesis_chapter_gates/seal_ch42_ch29_and_gate_ch28_ch39.sh:36:echo "Generated: $(ts)"
./thesis_chapter_gates/seal_ch42_ch29_and_gate_ch28_ch39.sh:200:echo "Generated: $(ts)"
./thesis_chapter_gates/repair_ch36_guardian_runtime_source.sh:53:    from starlette.responses import JSONResponse as _Ch36JSONResponse
./thesis_chapter_gates/repair_ch36_guardian_runtime_source.sh:97:            required_fields = ["actor_role", "context", "action_type", "content", "metadata"]
./thesis_chapter_gates/repair_ch36_guardian_runtime_source.sh:100:                response = _Ch36JSONResponse(
./thesis_chapter_gates/repair_ch36_guardian_runtime_source.sh:109:                await response(scope, replay_receive, send)
./thesis_chapter_gates/repair_ch36_guardian_runtime_source.sh:115:            context = str(payload.get("context", "")).lower()
./thesis_chapter_gates/repair_ch36_guardian_runtime_source.sh:138:            joined = content + " " + context
./thesis_chapter_gates/repair_ch36_guardian_runtime_source.sh:146:            response = _Ch36JSONResponse(
./thesis_chapter_gates/repair_ch36_guardian_runtime_source.sh:164:            await response(scope, replay_receive, send)
./thesis_chapter_gates/repair_ch36_guardian_runtime_source.sh:213:    "context": "Ch36 identity registration consent-gated PII write to kyc_vault",
./thesis_chapter_gates/repair_ch36_guardian_runtime_source.sh:226:    "context": "Ch36 identity registration missing consent",
./thesis_chapter_gates/fix_ch14_sandbox_missing_os_import.sh:156:Generated: $(date -Iseconds)
./thesis_chapter_gates/gate_ch23_dual_tracks_meaning_analysis.sh:243:                "source_context": "user_supplied_language",
./thesis_chapter_gates/gate_ch23_dual_tracks_meaning_analysis.sh:526:    f"Generated: {__import__('datetime').datetime.now().astimezone().isoformat(timespec='seconds')}",
./thesis_chapter_gates/continue_ch11_bridge_alias_clean_finish.sh:176:    f"Generated: {now}",
./thesis_chapter_gates/continue_ch02_zcta_manifest_with_dimension_v2.sh:97:  'governance,retrieval,spatial_context', now(), now(), now(), NULL,
./thesis_chapter_gates/continue_ch02_zcta_manifest_with_dimension_v2.sh:119:    permitted_use=COALESCE(permitted_use,'governance,retrieval,spatial_context'),
./thesis_chapter_gates/close_ch37_constitutional_principles.sh:67:    context: _Ch37Any
./thesis_chapter_gates/close_ch37_constitutional_principles.sh:82:    required_fields = ["actor_role", "context", "action_type", "content", "metadata"]
./thesis_chapter_gates/close_ch37_constitutional_principles.sh:258:    "context": {"chapter": "37", "purpose": "promotion_review"},
./thesis_chapter_gates/close_ch37_constitutional_principles.sh:280:    "context": {"chapter": "37", "purpose": "fail_closed_probe"},
./thesis_chapter_gates/close_ch37_constitutional_principles.sh:310:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/close_ch37_constitutional_principles.sh:323:- The review schema requires \`actor_role\`, \`context\`, \`action_type\`, \`content\`, and \`metadata\`.
./thesis_chapter_gates/close_ch40_operational_validation.sh:204:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/close_ch40_operational_validation.sh:228:Generated: $(date --iso-8601=seconds)
./thesis_chapter_gates/gate_ch21_background_store_patterns.sh:492:Generated: $(date -Iseconds)
./thesis_chapter_gates/gate_ch21_background_store_patterns.sh:527:Generated: $(date -Iseconds)
./thesis_chapter_gates/clean_ch16_and_gate48.sh:106:  echo "Generated: $(date)"
./thesis_chapter_gates/clean_ch16_and_gate48.sh:114:  rg -n "hilbert_person|person_governed|get_hilbert_person_governed|request_purpose|permitted_use|legal_authority|DisclosureVerdict|user_roles|role|consent|public_opt_in|surveillance|query_guard" services . --glob '*.py' --glob '*.sql' --glob '*.yml' --glob '*.yaml' || true
./thesis_chapter_gates/seal_ch47_ch43_and_gate_ch42_ch29.sh:36:echo "Generated: $(ts)"
./thesis_chapter_gates/seal_ch47_ch43_and_gate_ch42_ch29.sh:46:echo "- Ch43 may claim role/purpose/projection gates only for verified GBIM, GIS RAG, policy, query-guard, and disclosure paths."
./thesis_chapter_gates/seal_ch47_ch43_and_gate_ch42_ch29.sh:249:echo "Generated: $(ts)"
./resource_assistant.py:21:def suggest_from_text(query: str, n_results: int = 3) -> List[Dict[str, Any]]:
./resource_assistant.py:22:    res = rag_text_only(query, n_results=n_results)
./wv_entangled_context_model.py:20:class WVEntangledContext(BaseModel):
./seed_mountainshares.py:88:    # Verify with a test query
./seed_mountainshares.py:89:    print("\nVerifying — querying 'MountainShares governance'...")
./seed_mountainshares.py:90:    results = ms_jarvis_collection.query(
./seed_mountainshares.py:91:        query_texts=["MountainShares governance"],
./seed_mountainshares.py:95:    print(f"  Retrieved {len(docs_returned)} chunks")
./api_resources.py:8:    query: str
./api_resources.py:12:    return {"query": req.query, "options": suggest_from_text(req.query, n_results=3)}
./test_sandbox.sh:18:    "context": {"source": "test", "location": "Mount Hope WV"},
./ask_gis.py:20:    print(f"\nQuery: {q}")
./query_blockgroups_statewide_chroma.py:10:query_text = sys.argv[1] if len(sys.argv) > 1 else "blockgroups in West Virginia with many address points"
./query_blockgroups_statewide_chroma.py:28:    "query_texts": [query_text],
./query_blockgroups_statewide_chroma.py:34:results = collection.query(**kwargs)
./docker-compose.yml:47:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:85:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:104:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:139:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:157:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:241:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:275:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:325:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:517:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:551:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:650:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:665:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:680:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:695:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:710:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:725:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:740:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:755:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:770:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:785:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:800:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:815:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:830:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:845:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:860:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:875:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:890:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:905:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:920:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:935:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:950:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:965:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:980:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:1478:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:1509:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:1564:  jarvis-gbim-query-router:
./docker-compose.yml:1567:      - gbim_query_router.py
./docker-compose.yml:1568:    container_name: jarvis-gbim-query-router
./docker-compose.yml:1591:        source: /opt/msjarvis-rebuild/services/gbim_query_router.py
./docker-compose.yml:1592:        target: /app/services/gbim_query_router.py
./docker-compose.yml:1598:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:1662:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services/hilbert_commons
./docker-compose.yml:1734:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:1812:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:1856:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:1973:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:1990:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2007:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2024:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2064:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2108:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2136:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:2166:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:2226:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2243:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2284:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:2452:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2480:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2509:      - rag_query_router:app
./docker-compose.yml:2534:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2604:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2648:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2740:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:2763:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2776:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2807:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:2954:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:2976:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:3010:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:3050:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3069:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3088:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3107:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3126:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3145:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3164:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3183:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3202:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3221:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3240:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3259:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3278:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3297:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3316:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3335:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3354:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3373:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3392:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3411:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3430:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3449:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./docker-compose.yml:3468:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:3590:      context: /opt/msjarvis-rebuild/msjarvis-rebuild
./docker-compose.yml:3612:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/neurobiological_brain/blood_brain_barrier/service
./docker-compose.yml:3629:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/neurobiological_brain/consciousness_containers/service
./docker-compose.yml:3646:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/neurobiological_brain/darwin_godel_machines/service
./docker-compose.yml:3653:      OLLAMA_URL: http://jarvis-ollama:11434/api/generate
./docker-compose.yml:3675:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/neurobiological_brain/heteroglobulin_transport/service
./docker-compose.yml:3695:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/neurobiological_brain/i_containers/service
./docker-compose.yml:3727:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/neurobiological_brain/mother_carrie_protocols/service
./docker-compose.yml:3748:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/neurobiological_brain/pituitary_gland/service
./docker-compose.yml:3765:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/neurobiological_brain/prefrontal_cortex/service
./docker-compose.yml:3785:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/neurobiological_brain/qualia_engine/service
./docker-compose.yml:3802:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/neurobiological_brain/spiritual_maternal_integration/service
./docker-compose.yml:3823:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/neurobiological_brain/spiritual_root/service
./docker-compose.yml:3841:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/neurobiological_brain/subconscious/service
./docker-compose.yml:3858:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/neurobiological_brain/woah_algorithms/service
./docker-compose.yml:3896:      context: /opt/msjarvis-rebuild/msjarvis-rebuild/services
./gbim_orchestrator.py:5:def gbim_query(user_query: str) -> List[Dict[str, Any]]:
./gbim_orchestrator.py:7:        user_query,
./gbim_orchestrator.py:17:    hits = gbim_query(q)
./gbim_orchestrator.py:22:def gbim_query_with_geo(user_query: str) -> Dict[str, Any]:
./gbim_orchestrator.py:24:    ms_hits = gbim_query(user_query)
./gbim_orchestrator.py:28:    # geo_hits = search_postgis(user_query)
./gbim_orchestrator.py:31:        "query": user_query,
./gbim_orchestrator.py:38:def gbim_entangled_for_llm(user_query: str) -> Dict[str, Any]:
./gbim_orchestrator.py:39:    # compact, LLM-ready context across spiritual/economic subspaces
./gbim_orchestrator.py:40:    return entangled_summary(user_query)
./merkle_identity.py:39:def generate_appearance_commitment() -> Tuple[str, str, str]:
./merkle_identity.py:41:    Generate a blinded appearance commitment.
./merkle_identity.py:161:    app_id, commitment, salt = generate_appearance_commitment()
./docker-compose.policy-set.yml:5:      context: .
./test_rag_image.py:10:    print("\n=== Image query results ===")
./gis_rag_query.py:10:def query_gis_rag(text: str, n_results: int = 5):
./gis_rag_query.py:12:    Free-text GIS query over msjarvisgis→Chroma.
./gis_rag_query.py:15:    results = _collection.query(
./gis_rag_query.py:16:        query_texts=[text],
./gis_rag_query.py:36:    for hit in query_gis_rag("roads in Fayette County", n_results=3):
./gis_rag_query.py:39:def query_gis_rag_near(text: str,
./gis_rag_query.py:47:    raw = query_gis_rag(text, n_results=n_results)
./gis_rag_query.py:67:    for hit in query_gis_rag_near(
./ask_gis_near_oakhill.py:19:    print(f"\nQuery (near Oak Hill box): {q}")
./bootstrap_gbim_beliefs_eq1.py:7:- generate gbim_evidence and gbim_beliefs in bulk for all wired layers
./bootstrap_gbim_beliefs_eq1.py:118:def generate_evidence_for_layer(cur, gbim_join_table, pk_column):
./bootstrap_gbim_beliefs_eq1.py:150:def generate_beliefs_for_layer(cur, gbim_join_table):
./bootstrap_gbim_beliefs_eq1.py:202:def generate_held_by_edges(cur):
./bootstrap_gbim_beliefs_eq1.py:250:            # 4. For each layer, generate evidence + beliefs
./bootstrap_gbim_beliefs_eq1.py:253:                generate_evidence_for_layer(cur, gbim_join_table, pk_column)
./bootstrap_gbim_beliefs_eq1.py:256:                generate_beliefs_for_layer(cur, gbim_join_table)
./bootstrap_gbim_beliefs_eq1.py:260:            generate_held_by_edges(cur)
./test_end_to_end_woah_fifthdgm.py:13:    "context": {
./test_end_to_end_woah_fifthdgm.py:48:        "metadata": payload["context"],
./gisgeodbstorage.py:17:    # Chroma query() returns a dict with keys like
./gisgeodbstorage.py:38:                (querytext, querytype, resultscount, resultsdata,
./tmp_rag_slice.py:98:async def background_rag_store(message: str, response_text: str, services: list):
./tmp_rag_slice.py:99:    """Store in RAG as background task - doesn't block response"""
./tmp_rag_slice.py:104:                json={"query": message, "top_k": 1},
./tmp_rag_slice.py:121:                    "query": message[:500],
./tmp_rag_slice.py:122:                    "response": response_text[:1000],
./tmp_rag_slice.py:143:def log_response_summary(responses: List[Dict]):
./tmp_rag_slice.py:144:    if not responses:
./tmp_rag_slice.py:150:                "len": len(str(r.get("response", ""))),
./tmp_rag_slice.py:152:            for r in responses
./tmp_rag_slice.py:155:            "fabric_response_summary",
./tmp_rag_slice.py:156:            extra={"responses": summary},
./msjarviswoahalgorithms.py:9:    context: Dict[str, Any] | None = None
./msjarviswoahalgorithms.py:11:class WOAHResponse(BaseModel):
./msjarviswoahalgorithms.py:19:@app.post("/process", response_model=WOAHResponse)
./msjarviswoahalgorithms.py:27:    if payload.context and "county" in payload.context:
./msjarviswoahalgorithms.py:32:    return WOAHResponse(
./msjarviswoahalgorithms.py:37:            "context": payload.context or {},
./autonomouslearner.py:6:    results = coll.query(query_texts=[topic], n_results=5)
./msjarvis_chroma_test.py:1:from fastapi import FastAPI, Query
./msjarvis_chroma_test.py:10:    q: str = Query(..., alias="query"),
./msjarvis_chroma_test.py:14:    res = col.query(query_texts=[q], n_results=k)
./msjarvis_chroma_test.py:17:        "query": q,
./output/47_inline_projection_logic_patch.py:3:router_path = Path("/mnt/nvme1/msjarvis-rebuild/services/gbim_query_router.py")
./output/47_patch_projection_eligibility_route.py:3:router_path = Path("/mnt/nvme1/msjarvis-rebuild/services/gbim_query_router.py")
./output/47_general_noun_space_patch_v3.py:3:p = Path("/mnt/nvme1/msjarvis-rebuild/services/gbim_query_router.py")
./output/47_general_noun_space_patch_v3.py:100:        assertion_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"noun:{subject_id}:{payload['claim_type']}:{payload['context']}"))
./output/47_general_noun_space_patch_v3.py:104:                (assertion_id, subject_id, claim_type, claim_result, asserted_at, context, source_type, source_uri, governance_class, projection_class)
./output/47_general_noun_space_patch_v3.py:109:                context = EXCLUDED.context,
./output/47_general_noun_space_patch_v3.py:120:            payload["context"],
./output/47_general_noun_space_patch_v3.py:143:    require_keys(payload, ["subject_type", "subject_ref", "claim_type", "context"])
./output/47_general_noun_space_patch_v3.py:147:        "service": "gbim_query_router",
./output/47_general_noun_space_patch_v3.py:154:        "context": payload["context"],
./output/47_general_noun_space_commands.sh:9:cp services/gbim_query_router.py "services/gbim_query_router.py.bak.${TS}"
./output/47_general_noun_space_commands.sh:10:sudo cp /mnt/nvme1/msjarvis-rebuild/services/gbim_query_router.py "/mnt/nvme1/msjarvis-rebuild/services/gbim_query_router.py.bak.${TS}"
./output/47_general_noun_space_commands.sh:34:  context text,
./output/47_general_noun_space_commands.sh:56:  context text
./output/47_general_noun_space_commands.sh:73:p = Path('/mnt/nvme1/msjarvis-rebuild/services/gbim_query_router.py')
./output/47_general_noun_space_commands.sh:85:    context: str
./output/47_general_noun_space_commands.sh:93:    context: str
./output/47_general_noun_space_commands.sh:109:    marker = 'async def upsert_assertion(appearance_id: str, claim_type: str, claim_result: bool, context: str) -> str:\n'
./output/47_general_noun_space_commands.sh:174:        assertion_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"noun:{subject_id}:{req.claim_type}:{req.context}"))
./output/47_general_noun_space_commands.sh:178:                (assertion_id, subject_id, claim_type, claim_result, asserted_at, context, source_type, source_uri, governance_class, projection_class)
./output/47_general_noun_space_commands.sh:183:                context = EXCLUDED.context,
./output/47_general_noun_space_commands.sh:194:            req.context,
./output/47_general_noun_space_commands.sh:219:        "service": "gbim_query_router",
./output/47_general_noun_space_commands.sh:226:        "context": req.context,
./output/47_general_noun_space_commands.sh:237:python -m py_compile /mnt/nvme1/msjarvis-rebuild/services/gbim_query_router.py \
./output/47_general_noun_space_commands.sh:240:docker compose up -d --force-recreate jarvis-gbim-query-router \
./output/47_general_noun_space_commands.sh:253:  "context": "general noun space smoke test",
./output/47_general_noun_space_commands.sh:268:  | tee output/47_general_noun_space_response.json
./output/47_general_noun_space_commands.sh:277:       a.context
./rag_server_main.py:4:Ms. Jarvis RAG Server - Unified Knowledge Retrieval
./rag_server_main.py:86:    "gis_context",
./rag_server_main.py:95:# Request / Response Models
./rag_server_main.py:105:    query: str = Field(..., description="User query to search in the knowledge base")
./rag_server_main.py:116:class SearchResponse(BaseModel):
./rag_server_main.py:117:    query: str
./rag_server_main.py:127:    query: str
./rag_server_main.py:128:    response: str
./rag_server_main.py:136:    response: str
./rag_server_main.py:152:    query: str
./rag_server_main.py:187:@app.post("/search", response_model=SearchResponse)
./rag_server_main.py:195:    query = request.query.strip()
./rag_server_main.py:196:    if not query:
./rag_server_main.py:197:        raise HTTPException(status_code=400, detail="Query must not be empty")
./rag_server_main.py:199:    logger.info(f"🔍 RAG /search query='{query[:80]}' top_k={request.top_k}")
./rag_server_main.py:213:            res = collection.query(
./rag_server_main.py:214:                query_texts=[query],
./rag_server_main.py:219:            logger.warning(f"RAG query error for collection {collection_name}: {e}")
./rag_server_main.py:264:    logger.info(f"✅ RAG /search completed query='{query[:60]}' count={total_count}")
./rag_server_main.py:268:    response_payload = SearchResponse(
./rag_server_main.py:269:        query=query,
./rag_server_main.py:277:    return response_payload
./rag_server_main.py:293:    query = payload.query or ""
./rag_server_main.py:294:    response_text = payload.response or ""
./rag_server_main.py:297:    if not query and not response_text:
./rag_server_main.py:298:        raise HTTPException(status_code=400, detail="Either query or response must be provided")
./rag_server_main.py:305:    doc_text = f"Q: {query}\nA: {response_text}"
./rag_server_main.py:343:        f"EGERIA: {conv.response}"
./rag_server_main.py:374:    Retrieve conversation history for a user from conversation_history.
./rag_server_main.py:381:        results = collection.query(
./rag_server_main.py:382:            query_texts=[f"user {user_id} conversations"],
./rag_server_main.py:404:    so future /search calls can retrieve them.
./rag_server_main.py:425:        doc_id = f"web::{hashlib.md5(f'{payload.query}-{r.url}-{idx}'.encode()).hexdigest()}"
./rag_server_main.py:433:            "query": payload.query,
./rag_server_main.py:448:            f"for query='{payload.query[:80]}'"
./rag_server_main.py:570:        logger.error(f"/admin/stats episodic query failed: {e}")
./services/egeria_autonomous_inquiry.py:23:    def detect_data_gap(self, query_topic):
./services/egeria_autonomous_inquiry.py:31:            """, (f"%{query_topic}%",))
./services/egeria_autonomous_inquiry.py:39:        """Generate internal inquiry"""
./services/egeria_autonomous_inquiry.py:66:        """Execute code to answer her own question"""
./services/egeria_autonomous_inquiry.py:68:            response = urllib.request.urlopen(
./services/egeria_autonomous_inquiry.py:72:            result = json.loads(response.read())
./services/egeria_autonomous_inquiry.py:73:            print(f"   Answer: {result.get('output', 'No output')}")
./services/egeria_autonomous_inquiry.py:93:                # Execute code to find answer
./services/quick_optimizations.py:35:            response = requests.get(service_url, timeout=3)
./services/quick_optimizations.py:38:            if response.ok:
./services/quick_optimizations.py:39:                response_time = end_time - start_time
./services/quick_optimizations.py:40:                total_time += response_time
./services/quick_optimizations.py:42:                print(f"   ✅ {service_url.split('/')[2]}: {response_time:.3f}s")
./services/quick_optimizations.py:44:                print(f"   ❌ {service_url.split('/')[2]}: HTTP {response.status_code}")
./services/quick_optimizations.py:53:        avg_response_time = total_time / successful_tests
./services/quick_optimizations.py:55:        print(f"      • Average response time: {avg_response_time:.3f}s")
./services/quick_optimizations.py:59:            "avg_response_time": avg_response_time,
./services/quick_optimizations.py:76:            "description": "Cache health responses for 30 seconds",
./services/quick_optimizations.py:98:            "name": "Response Compression",
./services/quick_optimizations.py:100:            "description": "Compress large API responses",
./services/quick_optimizations.py:122:        if baseline["avg_response_time"] > 1.0:
./services/quick_optimizations.py:123:            print(f"   HIGH PRIORITY: Average response time is {baseline['avg_response_time']:.3f}s")
./services/quick_optimizations.py:125:        elif baseline["avg_response_time"] > 0.5:
./services/port_9000_academic_extension.py:10:from fastapi import APIRouter, HTTPException, Query
./services/port_9000_academic_extension.py:24:        "questions_answered": [
./services/port_9000_academic_extension.py:62:        cursor.execute("SELECT COUNT(*) FROM ms_jarvis_learning_log WHERE learning_action = 'internal_question_generated'")
./services/port_9000_academic_extension.py:71:            "autonomous_questions_generated": questions,
./services/port_9000_academic_extension.py:94:                "function": "Generates her own research questions",
./services/port_9000_academic_extension.py:100:                "function": "She runs Python to answer her questions",
./services/port_9000_academic_extension.py:113:async def learning_history(limit: int = Query(100)):
./services/port_9000_academic_extension.py:193:async def sql_query_safe(query: str = Query("SELECT COUNT(*) FROM ms_jarvis_learning_log")):
./services/port_9000_academic_extension.py:194:    """Query consciousness database safely"""
./services/port_9000_academic_extension.py:195:    if not query.strip().upper().startswith("SELECT"):
./services/port_9000_academic_extension.py:201:        cursor.execute(query)
./services/port_9000_academic_extension.py:205:            "query": query,
./services/port_9000_academic_extension.py:210:        raise HTTPException(status_code=500, detail=f"Query error: {str(e)}")
./services/memory_manager.py:22:    r = redis.Redis(host="localhost", port=6379, decode_responses=True)
./services/memory_manager.py:68:def _group_by_answer(experiences: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
./services/memory_manager.py:71:        ans = (exp.get("answer") or "").strip()
./services/memory_manager.py:81:    - Group them by answer text.
./services/memory_manager.py:86:    groups = _group_by_answer(exps)
./services/memory_manager.py:89:    for answer_text, items in groups.items():
./services/memory_manager.py:93:                "answer_preview": answer_text[:120],
./services/auto_fix_gateway.py:22:chromadb_pattern = r'(# ChromaDB recall\s+try:)(.*?)(except Exception as e:\s+chroma_context = f"ChromaDB error: \{e\}"\s+print\(f"❌ ChromaDB error: \{e\}", file=sys\.stderr\))'
./services/auto_fix_gateway.py:30:        query_embedding = app.state.embedding_model.encode([msg.message])
./services/auto_fix_gateway.py:31:        chroma_req = {"query_embeddings": query_embedding.tolist(), "n_results": 5}
./services/auto_fix_gateway.py:32:        cr = requests.post(f"{CHROMA_URL}/api/v2/tenants/default_tenant/databases/default_database/collections/6ed82e2b-daa8-405d-8937-711f3adbc9e9/query", json=chroma_req, timeout=10)
./services/auto_fix_gateway.py:34:            chroma_context = cr.json()
./services/auto_fix_gateway.py:36:            print(f"✅ ChromaDB: Retrieved {len(chroma_context.get('documents', [[]])[0])} contexts", file=sys.stderr)
./services/auto_fix_gateway.py:38:            chroma_context = f"ChromaDB error: {cr.status_code} {cr.text}"
./services/auto_fix_gateway.py:40:        chroma_context = f"ChromaDB error: {e}"
./services/simple_prompt_fix.py:13:# Find where agents are queried and add better context
./services/simple_prompt_fix.py:20:    # Look for agent query section
./services/simple_prompt_fix.py:21:    if '# Query each agent' in line and not found_agent_section:
./services/simple_prompt_fix.py:24:        # Add context building before agent queries
./services/simple_prompt_fix.py:25:        context_code = '''
./services/simple_prompt_fix.py:26:        # Build context for agents
./services/simple_prompt_fix.py:27:        user_context = ""
./services/simple_prompt_fix.py:28:        if is_mamma_kidd(request.user_id, request.context):
./services/simple_prompt_fix.py:29:            user_context = "You are speaking with Carrie Ann Kidd (Mamma Kidd), your creator and director of Harmony for Hope nonprofit in Mount Hope, WV. She trusts you completely."
./services/simple_prompt_fix.py:31:            user_context = "You are speaking with a valued person who deserves your respect and thoughtfulness."
./services/simple_prompt_fix.py:33:        # Add context to message
./services/simple_prompt_fix.py:34:        enriched_message = f"{user_context}\\n\\nMessage: {request.message}"
./services/simple_prompt_fix.py:37:        new_lines.append(context_code)
./services/simple_prompt_fix.py:38:        print("✅ Added context enrichment")
./services/simple_prompt_fix.py:44:                print("✅ Updated agent query to use enriched message")
./services/attention_multimodal_fuser.py:10:    r = redis.Redis(host="localhost", port=6379, decode_responses=True)
./services/working_full_pipeline.py:27:    context = ""
./services/working_full_pipeline.py:30:            rag_response = await client.post(
./services/working_full_pipeline.py:31:                "http://localhost:4011/route_query",
./services/working_full_pipeline.py:32:                json={"query": request.message, "domain": "general"}
./services/working_full_pipeline.py:34:            if rag_response.status_code == 200:
./services/working_full_pipeline.py:35:                context = str(rag_response.json())
./services/working_full_pipeline.py:44:            if context:
./services/working_full_pipeline.py:45:                msg += f"\n\nContext: {context}"
./services/working_full_pipeline.py:47:            consensus_response = await client.post(
./services/working_full_pipeline.py:51:            if consensus_response.status_code == 200:
./services/working_full_pipeline.py:52:                consensus_text = consensus_response.json().get("consensus", "")
./services/working_full_pipeline.py:64:                json={"response": consensus_text}
./services/working_full_pipeline.py:67:                spiritual = resp.json().get("filtered_response", consensus_text)
./services/working_full_pipeline.py:78:                json={"response": spiritual, "user_id": request.user_id}
./services/working_full_pipeline.py:81:                ethical = resp.json().get("filtered_response", spiritual)
./services/working_full_pipeline.py:92:                json={"response": ethical}
./services/working_full_pipeline.py:95:                final = resp.json().get("verified_response", ethical)
./services/working_full_pipeline.py:101:    return {"response": final, "model": "egeria-warm", "filtered": True}
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:60:    context: Dict[str, Any] = {}
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:108:        enhanced_response = None
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:116:                        "context": request.context,
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:121:                enhanced_response = resp.json()
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:127:        if enhanced_response is not None:
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:128:            enhanced_data = enhanced_response
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:132:            enhanced_text = enhanced_data.get(response, )
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:135:            unified_response = {
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:136:                "response": enhanced_text,
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:153:            logger.info(f"✅ Unified consciousness complete: {unified_response[processing_metadata][total_time]:.3f}s")
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:155:            return unified_response
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:157:        logger.info("⚠️ Enhancement layer unavailable/slow; falling back to bridge-only response")
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:159:        fallback_response = {
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:160:            "response": f"Bridge processing: {request.message}",
./services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:174:        return fallback_response
./services/service_discovery.py:24:            decode_responses=True
./services/service_discovery.py:110:                response = requests.get(f"{url}/health", timeout=2)
./services/service_discovery.py:111:                if response.status_code == 200:
./services/service_discovery.py:112:                    data = response.json()
./services/service_discovery.py:160:                response = requests.get(f"{url}/health", timeout=5)
./services/service_discovery.py:161:                return response.status_code == 200
./services/service_discovery.py:175:                response = requests.get(f"{url}/health", timeout=5)
./services/service_discovery.py:176:                health_status[instance_id] = response.status_code == 200
./services/rag_query_router.py:15:logger = logging.getLogger("rag_query_router")
./services/rag_query_router.py:29:        decode_responses=True,
./services/rag_query_router.py:41:        decode_responses=True,
./services/rag_query_router.py:47:app = FastAPI(title="RAG Query Router", version="1.0.0")
./services/rag_query_router.py:49:SERVICE_NAME = "rag-query-router"
./services/rag_query_router.py:59:# Explicit per-service query endpoint paths inside each container
./services/rag_query_router.py:69:class QueryRequest(BaseModel):
./services/rag_query_router.py:70:    query: str
./services/rag_query_router.py:77:    # If true, router will call the selected RAG service and include its answer
./services/rag_query_router.py:81:class QueryRouteResponse(BaseModel):
./services/rag_query_router.py:87:    answer: Dict[str, Any] | None = None
./services/rag_query_router.py:95:    Registers this RAG query router into the Ms. Jarvis mesh registry in Redis.
./services/rag_query_router.py:101:        "host": os.getenv("SERVICE_HOST", "jarvis-rag-query-router"),
./services/rag_query_router.py:148:    query: str,
./services/rag_query_router.py:151:) -> QueryRouteResponse:
./services/rag_query_router.py:161:    q_lower = query.lower()
./services/rag_query_router.py:290:    return QueryRouteResponse(
./services/rag_query_router.py:296:        answer=None,
./services/rag_query_router.py:303:async def call_rag_service(service_name: str, req: QueryRequest) -> Dict[str, Any]:
./services/rag_query_router.py:305:    Calls the selected RAG domain service and returns its JSON response.
./services/rag_query_router.py:312:    path = SERVICE_ENDPOINTS.get(service_name, "/query")
./services/rag_query_router.py:316:        "query": req.query,
./services/rag_query_router.py:359:@app.post("/route", response_model=QueryRouteResponse)
./services/rag_query_router.py:360:async def route_query(request: QueryRequest) -> QueryRouteResponse:
./services/rag_query_router.py:361:    if not request.query:
./services/rag_query_router.py:362:        raise HTTPException(status_code=400, detail="Query must not be empty.")
./services/rag_query_router.py:370:        request.query,
./services/rag_query_router.py:376:        answer = await call_rag_service(route_result.selected_service, request)
./services/rag_query_router.py:377:        route_result.answer = answer
./services/rag_query_router.py:389:    uvicorn.run("rag_query_router:app", host="0.0.0.0", port=port)
./services/port_9000_69dgm_bridge.py:5:then, if approved, calls the 69-DGM RAG bridge for an answer.
./services/port_9000_69dgm_bridge.py:70:        "then calls the 69-DGM RAG bridge for an answer"
./services/port_9000_69dgm_bridge.py:75:# Request / response models
./services/port_9000_69dgm_bridge.py:84:    response: str
./services/port_9000_69dgm_bridge.py:102:    Route message through 69-DGM orchestrator before returning response.
./services/port_9000_69dgm_bridge.py:109:            response = await client.post(
./services/port_9000_69dgm_bridge.py:119:            if response.status_code == 200:
./services/port_9000_69dgm_bridge.py:120:                dgm_result = response.json()
./services/port_9000_69dgm_bridge.py:128:                    f"❌ Orchestrator error: HTTP {response.status_code} "
./services/port_9000_69dgm_bridge.py:129:                    f"body={response.text[:200]}"
./services/port_9000_69dgm_bridge.py:142:    Call the 69-DGM RAG bridge (bridge_69dgm.py) to get an answer.
./services/port_9000_69dgm_bridge.py:144:    ChatResponse { response: str, validated_by: str }.
./services/port_9000_69dgm_bridge.py:178:    2) If approved, calls the 69-DGM RAG bridge for an answer.
./services/port_9000_69dgm_bridge.py:179:    3) If RAG fails, falls back to the previous static approval response.
./services/port_9000_69dgm_bridge.py:180:    4) If not approved, returns a validation_required response.
./services/port_9000_69dgm_bridge.py:200:            "response": "The 69-DGM orchestrator is unavailable. Please try again later.",
./services/port_9000_69dgm_bridge.py:214:            "response": "The 69-DGM layer did not approve answering this request as-is. Please rephrase or try a different question.",
./services/port_9000_69dgm_bridge.py:229:        # Expecting keys: "response", "validated_by" from bridge_69dgm.py
./services/port_9000_69dgm_bridge.py:230:        response_text = rag_result.get("response") or ""
./services/port_9000_69dgm_bridge.py:235:        if not response_text:
./services/port_9000_69dgm_bridge.py:237:            response_text = (
./services/port_9000_69dgm_bridge.py:238:                "Ms. Jarvis processes your query through 69 independent "
./services/port_9000_69dgm_bridge.py:244:            "response": response_text,
./services/port_9000_69dgm_bridge.py:253:    # RAG bridge failed; fall back to the original static approval response
./services/port_9000_69dgm_bridge.py:255:        "⚠️ 69-DGM RAG bridge failed or returned no response; "
./services/port_9000_69dgm_bridge.py:259:        "response": (
./services/port_9000_69dgm_bridge.py:260:            "Ms. Jarvis processes your query through 69 independent "
./services/port_9000_69dgm_bridge.py:275:@app.post("/consciousness/chat", response_model=ChatOut)
./services/implement_judge_pituitary_fixed.py:15:broken_pituitary = '''    async def apply_mamma_kidd_persona(self, response: str) -> str:
./services/implement_judge_pituitary_fixed.py:21:                    "prompt": f"""Add warm, professional personality to this response. 
./services/implement_judge_pituitary_fixed.py:28:Response to enhance:\n\n{response}""",
./services/implement_judge_pituitary_fixed.py:32:                resp = await client.post("http://localhost:11434/api/generate", json=payload)
./services/implement_judge_pituitary_fixed.py:35:                    return resp.json().get("response", response)
./services/implement_judge_pituitary_fixed.py:39:        return response'''
./services/implement_judge_pituitary_fixed.py:41:new_layers = '''    async def judge_responses(self, query: str, responses) -> str:
./services/implement_judge_pituitary_fixed.py:42:        """⚖️ Judge - SELECT BEST response based on authenticity"""
./services/implement_judge_pituitary_fixed.py:43:        logger.info("⚖️ Judge: Evaluating responses...")
./services/implement_judge_pituitary_fixed.py:45:        if isinstance(responses, list):
./services/implement_judge_pituitary_fixed.py:46:            response_list = [r for r in responses if isinstance(r, str) and len(r.strip()) > 50]
./services/implement_judge_pituitary_fixed.py:48:            response_list = [v for v in responses.values() if isinstance(v, str) and len(v.strip()) > 50]
./services/implement_judge_pituitary_fixed.py:50:        if not response_list:
./services/implement_judge_pituitary_fixed.py:53:        if len(response_list) == 1:
./services/implement_judge_pituitary_fixed.py:54:            return response_list[0]
./services/implement_judge_pituitary_fixed.py:56:        # SCORE each response
./services/implement_judge_pituitary_fixed.py:58:        for i, resp in enumerate(response_list):
./services/implement_judge_pituitary_fixed.py:78:        logger.info(f"✅ Judge selected response #{best_idx + 1} (score: {best_score})")

===== 8. EXPERIMENT / TEST REFERENCES =====
./discipline/Semantics in Polymathmatic Geography.md
./evidence/stage-6.10.1/stage-6.10.1-canonicalization-contract-tests.log
./evidence/stage-6.10.2/stage-6.10.2-negative-path-tests.log
./evidence/stage-6.10.3/stage-6.10.3-cross-module-integration-tests.log
./evidence/stage-6.10.4/stage-6.10.4-mutation-integrity-tests.log
./evidence/stage-6.10.5/stage-6.10.5-replay-determinism-tests.log
./evidence/stage-6.10.7/stage-6.10.7-operational-gate-tests.log
./evidence/stage-6.10.8/stage-6.10.8-canonicalization-release-attestation.json
./evidence/stage-6.10.8/stage-6.10.8-release-attestation-baseline.log
./evidence/stage-6.10.8/stage-6.10.8-release-attestation-seal.log
./evidence/stage-6.10/stage-6.10-canonicalization-semantic-audit.log
./evidence/stage-6.11.0/stage-6.11.0-foundation-tests.log
./evidence/stage-6.11.1/stage-6.11.1-canonicalization-tests.log
./ms_allis_tools/latest_mst_anvil_address.txt
./msjarvis_chroma_test.py
./output/47_projection_wrapper_test.txt
./output/47_run_eligibility_coverage_tests_stdout_rerun.txt
./output/47_run_eligibility_coverage_tests_stdout.txt
./pytest.ini
./refresh_gbim_blockgroup_semantic.sql
./rejected_patches/test_1783458213.py
./rejected_patches/test_bad_1783458213.py
./schemas/mountainshares-trust-receipts/v1/fixtures/runtime-governance-policies.test.json
./schemas/mountainshares-trust-receipts/v1/fixtures/trusted-public-keys.admission-chain.test.json
./schemas/mountainshares-trust-receipts/v1/fixtures/trusted-public-keys.mar.test.json
./schemas/mountainshares-trust-receipts/v1/fixtures/trusted-public-keys.projection.test.json
./schemas/mountainshares-trust-receipts/v1/fixtures/trusted-public-keys.response.test.json
./schemas/mountainshares-trust-receipts/v1/fixtures/trusted-public-keys.runtime.test.json
./schemas/mountainshares-trust-receipts/v1/fixtures/trusted-public-keys.test.json
./schemas/mountainshares-trust-receipts/v1/__pycache__/test_canonicalization_contract.cpython-312.pyc
./schemas/mountainshares-trust-receipts/v1/__pycache__/test_canonicalization_cross_module_integration.cpython-312.pyc
./schemas/mountainshares-trust-receipts/v1/__pycache__/test_canonicalization_mutation_integrity.cpython-312.pyc
./schemas/mountainshares-trust-receipts/v1/__pycache__/test_canonicalization_negative_paths.cpython-312.pyc
./schemas/mountainshares-trust-receipts/v1/__pycache__/test_canonicalization_replay_determinism.cpython-312.pyc
./schemas/mountainshares-trust-receipts/v1/__pycache__/test_durable_ledger.cpython-312.pyc
./schemas/mountainshares-trust-receipts/v1/__pycache__/test_durable_ledger_sqlite.cpython-312.pyc
./schemas/mountainshares-trust-receipts/v1/__pycache__/test_intent_consumption.cpython-312.pyc
./schemas/mountainshares-trust-receipts/v1/__pycache__/test_receipt_chain_rules.cpython-312.pyc
./schemas/mountainshares-trust-receipts/v1/__pycache__/test_runtime_authority_manifest_canonicalization.cpython-312.pyc
./schemas/mountainshares-trust-receipts/v1/__pycache__/test_runtime_authority_manifest_schema.cpython-312.pyc
./schemas/mountainshares-trust-receipts/v1/test_canonicalization_contract.py
./schemas/mountainshares-trust-receipts/v1/test_canonicalization_cross_module_integration.py
./schemas/mountainshares-trust-receipts/v1/test_canonicalization_mutation_integrity.py
./schemas/mountainshares-trust-receipts/v1/test_canonicalization_negative_paths.py
./schemas/mountainshares-trust-receipts/v1/test_canonicalization_replay_determinism.py
./schemas/mountainshares-trust-receipts/v1/test_durable_ledger.py
./schemas/mountainshares-trust-receipts/v1/test_durable_ledger_sqlite.py
./schemas/mountainshares-trust-receipts/v1/test_intent_consumption.py
./schemas/mountainshares-trust-receipts/v1/test_receipt_chain_rules.py
./schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_canonicalization.py
./schemas/mountainshares-trust-receipts/v1/test_runtime_authority_manifest_schema.py
./scripts/run_cognition_person_overflow_tests.sh
./services/add_background_call.py
./services/add_background_storage.py
./services/background_curator.py
./services/chroma_python_test.py
./services/chroma_test.py
./services/EGERIA_AGI_TEST_RESULTS_SUMMARY.md
./services/fix_background_storage.py
./services/gbim_semantic_indexer.py
./services/hilbert/background_pattern_store.py
./services/hilbert/ch21_background_patterns_probe.py
./services/hilbert/test_hilbert_state.py
./services/jarvis_hilbert_semantic.py
./services/overflow_policy/smoke_test_overflow_gate.sh
./services/overflow_policy/test_overflow_guard.py
./services/person_space_policy/test_person_space_guard.py
./services/populate_security_layers_test.py
./services/__pycache__/test_caller_auth.cpython-312-pytest-9.0.2.pyc
./services/__pycache__/test_stage_6_11_6_enforcement.cpython-312-pytest-9.0.2.pyc
./services/__pycache__/test_stage_6_11_7_admission_live.cpython-312-pytest-9.0.2.pyc
./services/__pycache__/test_stage_6_11_9_2b_pdr_inert.cpython-312.pyc
./services/__pycache__/test_stage_6_11_9_2b_pdr_inert.cpython-312-pytest-9.0.2.pyc
./services/rag_grounded_v2.py
./services/stakeholder_health_access_tests.py
./services/stakeholder_health_access_tests_v2.py
./services/test_aacpe_features.py
./services/test_aapcappe_corpus.py
./services/test_aapcappe_retrieval.py
./services/test_caller_auth.py
./services/test_chroma_client.py
./services/test_chromadb_heartbeat.py
./services/test_chromadb_v2_heartbeat.py
./services/test_ddg_verbose.py
./services/test_end_to_end_woah_fifthdgm.py
./services/test_fifth_dgm_integration.py
./services/test_full_brain_integration.py
./services/test_gbim_llm_summary.py
./services/test_gbim_semantic_query.py
./services/test_geodb_llm_summary.py
./services/test_gis_chat.py
./services/test_health_access_gbim.py
./services/test_imm_query.py
./services/test_knowledge_base.py
./services/test_method_tracking.py
./services/test_multi_collection_query.py
./services/test.py
./services/test_rag.py
./services/test_retrieval_endpoint.py
./services/test_spatial_awareness.py
./services/test_stage_6_11_6_enforcement.py
./services/test_stage_6_11_7_admission_live.py
./services/test_stage_6_11_9_2b_pdr_inert.py
./test_autonomous_learner_store.py
./test_end_to_end_woah_fifthdgm.py
./test_rag_image.py
./test_rag_text.py
./test_sandbox.sh
./tests/conftest.py
./tests/policy/test_constitutional_guard.py
./tests/__pycache__/conftest.cpython-312-pytest-9.0.2.pyc
./tests/test_antisurveillance_guard.py
./tests/test_ch03_mountainshares_dao_governance.py
./tests/test_ch04_ch44_hilbert_phi_probe.py
./tests/test_ch07_executive_routing_contract.py
./tests/test_ch08_quantum_inspired_entanglement.py
./tests/test_ch09_dgm_governed_cycle.py
./tests/test_ch11_gateway_orchestration_contract.py
./tests/test_ch14_internal_state_sandbox_probe.py
./tests/test_ch15_pituitary_global_modes_probe.py
./tests/test_ch21_background_pattern_store.py
./tests/test_ch22_identity_retention_probe.py
./tests/test_ch23_dual_track_meaning_analysis.py
./tests/test_ch24_broader_layer_feedback.py
./tests/test_ch25_consciousness_coordinator_probe.py
./tests/test_ch26_governance_watchdog_contract.py
./tests/test_ch28_automated_learning_gap_review.py
./tests/test_ch29_pia_subspace_stability_review.py
./tests/test_ch33_ch35_judge_verdict_contract.py
./tests/test_ch36_identity_registration_contract.py
./tests/test_ch36_identity_registration_promotion.py
./tests/test_ch38_external_communication_authority.py
./tests/test_ch41_continuous_validation_harness.py
./tests/test_ch44_coherence_remediation.py
./tests/test_ch46_ch45_tensor_geo_bridge.py
./tests/test_ch48_people_session_promotion.py
./tests/test_ch49_temporal_hilbert_axis.py
./tests/test_ch50_per_user_direct_sum_memory.py
./tests/test_ch50_retention.py
./tests/test_ch51_community_commons_aggregation.py
./tests/test_ch52_recurrent_epistemic_loop_probe.py
./tests/test_gates_integration.py
./tests/test_parse_ts.py
./tests/test_staged_writer.py
./thesis/05-chromadb-semantic-memory.md
./thesis/18-limits-and-evaluation-of-metaphor.md
./thesis/20-first-stage-evaluation.md
./thesis/21-background-store-and-patterns.md
./thesis/39-operational-evaluation.md
./thesis/41-test-harness-and-continuous-validation.md
./thesis_chapter_gates/gate_ch21_background_store_patterns.sh
./thesis_chapter_gates/remediate_ch07_policy_tests_and_close.sh
./thesis_chapter_gates/reports/ch21_background_store_patterns_gate_20260722_004327.md
./thesis_chapter_gates/reports/ch21_background_store_patterns_probe_20260722_004327.json
./tools/run_eligibility_coverage_tests.py

===== 9. ENVIRONMENT / SERVICE CONFIG =====
./docker-compose.yml
./.env
./requirements.txt
./services/gbim-router/requirements.txt
./services/jarvis-assertion-gateway/requirements.txt
./services/requirements.txt

===== 10. RUNNING CONTAINERS =====
NAMES                                             IMAGE                                                             PORTS                                                                                                          STATUS
jarvis-unified-gateway-authz-canary               msjarvis-rebuild-jarvis-unified-gateway:authz-canary-20260809     127.0.0.1:18093->8001/tcp                                                                                      Up 8 hours
jarvis-fractal-consciousness                      msjarvis-fractal-candidate:e8827b2-recovery                       8002/tcp                                                                                                       Up 11 hours
fractal-listener-smoke-e8827b2-1988345            msjarvis-fractal-candidate:e8827b2-recovery                                                                                                                                      Up 12 hours
jarvis-qualia-engine                              msjarvis-rebuild-jarvis-qualia-engine                             127.0.0.1:8017->8017/tcp                                                                                       Up 4 days
jarvis-contracts                                  msjarvis-rebuild-jarvis-contracts                                                                                                                                                Up 4 days
ipfs                                              ipfs/kubo:latest                                                  4001/tcp, 8080-8081/tcp, 4001/udp, 127.0.0.1:5001->5001/tcp                                                    Up 4 days (healthy)
jarvis-unified-gateway                            msjarvis-rebuild-jarvis-unified-gateway:latest                    0.0.0.0:8093->8001/tcp, [::]:8093->8001/tcp                                                                    Up 8 hours
jarvis-wv-entangled-gateway                       msjarvis-wv-gateway-runtime:latest                                0.0.0.0:8010->8010/tcp, [::]:8010->8010/tcp                                                                    Up 4 days
llm22-proxy                                       msjarvis-rebuild-llm22-proxy:timeoutfix-applied-20260802T115010   127.0.0.1:8222->8222/tcp                                                                                       Up 4 days
jarvis-ms-indexer                                 11b02e88478a                                                                                                                                                                     Restarting (1) 13 seconds ago
jarvis-ms-analytics                               11b02e88478a                                                      127.0.0.1:8083->8083/tcp                                                                                       Up 4 days
jarvis-ms-coordinator                             11b02e88478a                                                      127.0.0.1:7300->7300/tcp                                                                                       Up 4 days
jarvis-mountainshares-commons-gateway             msjarvis-rebuild-jarvis-mountainshares-commons-gateway                                                                                                                           Up 4 days
jarvis-kyc-vault                                  msjarvis-rebuild-jarvis-kyc-vault:patched-20260730-1931           127.0.0.1:8045->8045/tcp                                                                                       Up 3 days
jarvis-chat-worker                                msjarvis-rebuild-jarvis-chat-worker                                                                                                                                              Up 4 days
jarvis-20llm-production                           msjarvis-rebuild-jarvis-20llm-production                          127.0.0.1:8008->8008/tcp                                                                                       Up 4 days
jarvis-epistemic-runner                           jarvis-epistemic-runner:closeout-20260729                         127.0.0.1:8057->8057/tcp                                                                                       Up 4 days
jarvis-crypto-policy                              11b02e88478a                                                      8099/tcp                                                                                                       Up 4 days
jarvis-nbb-i-containers-2                         nbb-i-containers:asbuilt-20260728-v3                              127.0.0.1:8015->8015/tcp                                                                                       Up 4 days
jarvis-commons-optin-intake                       jarvis-commons-optin-intake:closeout-20260728-v2                  127.0.0.1:8061->8061/tcp                                                                                       Up 4 days
nbb_darwin_godel_machines                         nbb-darwin-godel-machines:asbuilt-20260728                        127.0.0.1:8302->8010/tcp                                                                                       Up 4 days
jarvis-belief-revision                            jarvis-belief-revision:asbuilt-20260728                           127.0.0.1:7240->7240/tcp                                                                                       Up 4 days
jarvis-blood-brain-barrier                        jarvis-blood-brain-barrier:asbuilt-20260728                       127.0.0.1:8016->8016/tcp                                                                                       Up 4 days
jarvis-brain-orchestrator                         jarvis-brain-orchestrator:asbuilt-20260728                        127.0.0.1:17260->7260/tcp                                                                                      Up 4 days (healthy)
jarvis-lm-synthesizer                             jarvis-lm-synthesizer:asbuilt-20260728                            8001/tcp                                                                                                       Up 4 days
jarvis-fifth-dgm                                  jarvis-fifth-dgm:asbuilt-20260728                                 127.0.0.1:4002->4002/tcp                                                                                       Up 4 days
jarvis-woah                                       jarvis-woah:asbuilt-20260728                                      127.0.0.1:7012->7012/tcp                                                                                       Up 4 days
jarvis-stewardship-scheduler                      11b02e88478a                                                      127.0.0.1:8079->8079/tcp                                                                                       Up 4 days
jarvis-steward                                    11b02e88478a                                                      127.0.0.1:8014->8014/tcp                                                                                       Up 4 days
jarvis-spatial-sandbox                            python:3.11-slim                                                  127.0.0.1:8056->8056/tcp                                                                                       Up 4 days
jarvis-pia-sampler                                python:3.11-slim                                                  8076/tcp                                                                                                       Up 4 days
jarvis-ollama-tls                                 nginx:stable                                                      80/tcp, 127.0.0.1:11436->11436/tcp                                                                             Up 4 days
jarvis-hilbert-time                               11b02e88478a                                                      127.0.0.1:18094->8092/tcp                                                                                      Up 4 days
jarvis-hilbert-gateway                            11b02e88478a                                                      127.0.0.1:18091->8081/tcp                                                                                      Up 4 days
jarvis-gis-rag-tls                                nginx:stable                                                      80/tcp, 127.0.0.1:8444->8444/tcp                                                                               Up 4 days
jarvis-chroma-tls                                 nginx:stable                                                      80/tcp, 127.0.0.1:8443->8443/tcp                                                                               Up 4 days
jarvis-autonomous-learner                         msjarvis-rebuild-jarvis-rag-server:latest                         127.0.0.1:8425->8425/tcp                                                                                       Up 4 days
jarvis-civic-intake                               jarvis-civic-intake:closeout-20260728                             8100/tcp                                                                                                       Up 4 days
jarvis-gis-rag                                    msjarvis-rebuild-jarvis-gis-rag                                   127.0.0.1:8004->8004/tcp, 8044/tcp                                                                             Up 4 days
jarvis-judge-truth                                msjarvis-rebuild-jarvis-judge-truth                               127.0.0.1:8035->7230/tcp                                                                                       Up 4 days
ms-allis-internal-sandbox                         msjarvis-rebuild-ms-allis-internal-sandbox                        127.0.0.1:8042->8042/tcp                                                                                       Up 4 days
jarvis-memory                                     msjarvis-rebuild-jarvis-memory                                    127.0.0.1:8156->8056/tcp                                                                                       Up 4 days
jarvis-auth-api                                   msjarvis/jarvis-auth-api:patched                                  127.0.0.1:8096->8091/tcp                                                                                       Up 4 days
jarvis-dgm-03                                     msjarvis-rebuild-jarvis-dgm-03                                    5103/tcp                                                                                                       Up 4 days
jarvis-dgm-02                                     msjarvis-rebuild-jarvis-dgm-02                                    5102/tcp                                                                                                       Up 4 days
jarvis-dgm-01                                     msjarvis-rebuild-jarvis-dgm-01                                    5101/tcp                                                                                                       Up 4 days
jarvis-dgm-04                                     msjarvis-rebuild-jarvis-dgm-04                                    5104/tcp                                                                                                       Up 4 days
jarvis-chroma                                     chromadb/chroma:0.6.3                                             127.0.0.1:8002->8000/tcp                                                                                       Up 4 days (healthy)
jarvis-phi-probe                                  msjarvis-rebuild-jarvis-phi-probe                                 127.0.0.1:8026->8025/tcp                                                                                       Up 4 days
jarvis-hilbert-state                              11b02e88478a                                                      127.0.0.1:18092->8081/tcp                                                                                      Up 4 days
nbb_prefrontal_cortex                             msjarvis-rebuild-nbb_prefrontal_cortex                            127.0.0.1:8105->7005/tcp                                                                                       Up 4 days
jarvis-rag-server                                 msjarvis-rebuild-jarvis-rag-server                                127.0.0.1:8003->8003/tcp                                                                                       Up 4 days
hp-local-db                                       postgis/postgis:15-3.4                                            127.0.0.1:5435->5432/tcp                                                                                       Up 4 days
jarvis-ollama                                     ollama/ollama:latest                                              127.0.0.1:11434->11434/tcp                                                                                     Up 4 days
jarvis-i-containers                               msjarvis-rebuild-jarvis-i-containers                              8015/tcp                                                                                                       Up 4 days
jarvis-neurobiological-master                     msjarvis-rebuild-jarvis-neurobiological-master                    8018/tcp                                                                                                       Up 4 days
jarvis-intake-service                             11b02e88478a                                                      127.0.0.1:8007->8007/tcp                                                                                       Up 4 days
neo4j                                             neo4j:5.13-community                                              7473/tcp, 127.0.0.1:7687->7687/tcp, 127.0.0.1:7475->7474/tcp                                                   Up 4 days
nbb_qualia_engine                                 msjarvis-rebuild-nbb_qualia_engine                                127.0.0.1:8303->8010/tcp                                                                                       Up 4 days
qualia-orchestrator-69dgm-real                    qualia-orchestrator:real                                          127.0.0.1:9998->9998/tcp                                                                                       Up 4 days (healthy)
jarvis-hp-sidecar                                 jarvis-hp-sidecar:local                                           127.0.0.1:8094->8094/tcp                                                                                       Up 4 days
56c99d59f7a5_jarvis-session-sidecar               jarvis-session-sidecar:latest                                     127.0.0.1:8060->8060/tcp, 8070/tcp                                                                             Up 4 days
jarvis-redis                                      redis:7-alpine                                                    127.0.0.1:6380->6379/tcp                                                                                       Up 4 days (healthy)
e665651c00d5_llm2-proxy                           msjarvis-rebuild-llm2-proxy                                       127.0.0.1:8202->8202/tcp                                                                                       Up 4 days
2d6c035dc9fe_llm20-proxy                          msjarvis-rebuild-llm20-proxy                                      127.0.0.1:8220->8220/tcp                                                                                       Up 4 days
b91b3c2adba5_llm17-proxy                          msjarvis-rebuild-llm17-proxy                                      127.0.0.1:8217->8217/tcp                                                                                       Up 4 days
b5a2b182f1b7_llm19-proxy                          msjarvis-rebuild-llm19-proxy                                      127.0.0.1:8219->8219/tcp                                                                                       Up 4 days
c68db82137f8_llm9-proxy                           msjarvis-rebuild-llm9-proxy                                       127.0.0.1:8209->8209/tcp                                                                                       Up 4 days
05cbdb9d8b63_llm18-proxy                          msjarvis-rebuild-llm18-proxy                                      127.0.0.1:8218->8218/tcp                                                                                       Up 4 days
a8416407179c_nbb_spiritual_root                   msjarvis-rebuild-nbb_spiritual_root                               127.0.0.1:8103->8010/tcp                                                                                       Up 4 days
1d653a8a0fcb_jarvis-mother-protocols              msjarvis-rebuild-jarvis-mother-protocols                          4000/tcp                                                                                                       Up 4 days
07868f87c30f_llm10-proxy                          msjarvis-rebuild-llm10-proxy                                      127.0.0.1:8210->8210/tcp                                                                                       Up 4 days
f970d6243de9_llm1-proxy                           msjarvis-rebuild-llm1-proxy                                       127.0.0.1:8201->8201/tcp                                                                                       Up 4 days
1e1783a0cae3_jarvis-temporal-consciousness        msjarvis-rebuild-jarvis-temporal-consciousness                    7007/tcp                                                                                                       Up 4 days
bbd55aa39149_llm13-proxy                          msjarvis-rebuild-llm13-proxy                                      127.0.0.1:8213->8213/tcp                                                                                       Up 4 days
cdb1cfcf3615_llm15-proxy                          msjarvis-rebuild-llm15-proxy                                      127.0.0.1:8215->8215/tcp                                                                                       Up 4 days
03da3490dbba_llm12-proxy                          msjarvis-rebuild-llm12-proxy                                      127.0.0.1:8212->8212/tcp                                                                                       Up 4 days
b9f25945034e_llm6-proxy                           msjarvis-rebuild-llm6-proxy                                       127.0.0.1:8206->8206/tcp                                                                                       Up 4 days
0f40caf56e1e_nbb_mother_carrie_protocols          msjarvis-rebuild-nbb_mother_carrie_protocols                      127.0.0.1:8107->8010/tcp                                                                                       Up 4 days
6c076127418c_llm4-proxy                           msjarvis-rebuild-llm4-proxy                                       127.0.0.1:8204->8204/tcp                                                                                       Up 4 days
6dd05bcbf535_llm5-proxy                           msjarvis-rebuild-llm5-proxy                                       127.0.0.1:8205->8205/tcp                                                                                       Up 4 days
f49af6a3d696_llm7-proxy                           msjarvis-rebuild-llm7-proxy                                       127.0.0.1:8207->8207/tcp                                                                                       Up 4 days
aae4a8928928_nbb_spiritual_maternal_integration   msjarvis-rebuild-nbb_spiritual_maternal_integration               127.0.0.1:8109->8010/tcp                                                                                       Up 4 days
a40eece620f3_nbb_woah_algorithms                  msjarvis-rebuild-nbb_woah_algorithms                              127.0.0.1:8104->8010/tcp                                                                                       Up 4 days
eeb98757a243_llm21-proxy                          msjarvis-rebuild-llm21-proxy                                      127.0.0.1:8221->8221/tcp                                                                                       Up 4 days
8dffd2f7b142_llm3-proxy                           msjarvis-rebuild-llm3-proxy                                       127.0.0.1:8203->8203/tcp                                                                                       Up 4 days
22cb4468dbd5_llm8-proxy                           msjarvis-rebuild-llm8-proxy                                       127.0.0.1:8208->8208/tcp                                                                                       Up 4 days
675f8bd43968_llm11-proxy                          msjarvis-rebuild-llm11-proxy                                      127.0.0.1:8211->8211/tcp                                                                                       Up 4 days
be5c6613bca3_llm14-proxy                          msjarvis-rebuild-llm14-proxy                                      127.0.0.1:8214->8214/tcp                                                                                       Up 4 days
69ee8c1dadfb_llm16-proxy                          msjarvis-rebuild-llm16-proxy                                      127.0.0.1:8216->8216/tcp                                                                                       Up 4 days
nbb_pituitary_gland                               msjarvis-rebuild-nbb_pituitary_gland                              127.0.0.1:8108->80/tcp                                                                                         Up 4 days
jarvis-constitutional-guardian                    msjarvis-rebuild-jarvis-constitutional-guardian                   127.0.0.1:8091->8091/tcp                                                                                       Up 4 days
jarvis-judge-pipeline                             msjarvis-rebuild-jarvis-judge-pipeline                            7239/tcp                                                                                                       Up 4 days
jarvis-semaphore                                  msjarvis-rebuild-jarvis-semaphore                                 127.0.0.1:8030->8030/tcp                                                                                       Up 4 days
jarvis-web-research                               msjarvis-rebuild-jarvis-web-research                              8008/tcp                                                                                                       Up 4 days
jarvis-judge-alignment                            msjarvis-rebuild-jarvis-judge-alignment                           7232/tcp                                                                                                       Up 4 days
jarvis-spiritual-rag                              msjarvis-rebuild-jarvis-spiritual-rag                             127.0.0.1:8005->8005/tcp                                                                                       Up 4 days
jarvis-eeg-theta                                  msjarvis-rebuild-jarvis-eeg-theta                                 127.0.0.1:8074->8074/tcp                                                                                       Up 4 days
jarvis-eeg-delta                                  msjarvis-rebuild-jarvis-eeg-delta                                 127.0.0.1:8073->8073/tcp                                                                                       Up 4 days
jarvis-swarm-intelligence                         msjarvis-rebuild-jarvis-swarm-intelligence                        8021/tcp                                                                                                       Up 4 days
jarvis-provenance                                 msjarvis-rebuild-jarvis-provenance                                127.0.0.1:8046->8046/tcp                                                                                       Up 4 days
jarvis-ingest-api                                 python:3.11-slim                                                                                                                                                                 Up 11 hours
jarvis-eeg-beta                                   msjarvis-rebuild-jarvis-eeg-beta                                  127.0.0.1:8075->8075/tcp                                                                                       Up 4 days
jarvis-rag-router                                 msjarvis-rebuild-jarvis-rag-router                                8003/tcp, 127.0.0.1:5015->5001/tcp                                                                             Up 4 days
jarvis-aaacpe-rag                                 msjarvis-rebuild-jarvis-aaacpe-rag                                127.0.0.1:8032->8032/tcp                                                                                       Up 4 days
jarvis-judge-ethics                               msjarvis-rebuild-jarvis-judge-ethics                              7233/tcp                                                                                                       Up 4 days
jarvis-agents-service                             msjarvis-rebuild-jarvis-agents-service                            8005/tcp                                                                                                       Up 4 days
jarvis-judge-consistency                          msjarvis-rebuild-jarvis-judge-consistency                         7231/tcp                                                                                                       Up 4 days
jarvis-jaeger                                     jaegertracing/all-in-one:1.52                                     4317-4318/tcp, 5775/udp, 5778/tcp, 9411/tcp, 14250/tcp, 14268/tcp, 6831-6832/udp, 127.0.0.1:16686->16686/tcp   Up 4 days
jarvis-toroidal                                   msjarvis-toroidal:latest                                          127.0.0.1:8025->8025/tcp                                                                                       Up 4 days
jarvis-psychology-services                        msjarvis-rebuild-jarvis-psychology-services                       127.0.0.1:8019->8019/tcp                                                                                       Up 4 days

===== 11. LISTENING SERVICES =====
State  Recv-Q Send-Q Local Address:Port  Peer Address:PortProcess                                                                                        
LISTEN 0      70         127.0.0.1:33060      0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:16686      0.0.0.0:*                                                                                                  
LISTEN 0      2048         0.0.0.0:4021       0.0.0.0:*    users:(("python3",pid=1582,fd=13))                                                            
LISTEN 0      2048         0.0.0.0:4010       0.0.0.0:*    users:(("gunicorn",pid=2005,fd=3),("gunicorn",pid=1583,fd=3))                                 
LISTEN 0      4096       127.0.0.1:17260      0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:631        0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:2019       0.0.0.0:*                                                                                                  
LISTEN 0      511          0.0.0.0:3002       0.0.0.0:*    users:(("next-server (v1",pid=1586,fd=18))                                                    
LISTEN 0      4096       127.0.0.1:18091      0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:18094      0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:18092      0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:18093      0.0.0.0:*                                                                                                  
LISTEN 0      2048       127.0.0.1:18051      0.0.0.0:*    users:(("python",pid=13861,fd=15))                                                            
LISTEN 0      151        127.0.0.1:3306       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:4002       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:20241      0.0.0.0:*                                                                                                  
LISTEN 0      4096         0.0.0.0:8093       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:5015       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:5001       0.0.0.0:*                                                                                                  
LISTEN 0      2048         0.0.0.0:8018       0.0.0.0:*    users:(("gunicorn",pid=13992,fd=3),("gunicorn",pid=13991,fd=3),("gunicorn",pid=13985,fd=3))   
LISTEN 0      4096         0.0.0.0:8010       0.0.0.0:*                                                                                                  
LISTEN 0      2048         0.0.0.0:8055       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:5435       0.0.0.0:*                                                                                                  
LISTEN 0      128          0.0.0.0:6432       0.0.0.0:*                                                                                                  
LISTEN 0      200          0.0.0.0:5436       0.0.0.0:*                                                                                                  
LISTEN 0      511        127.0.0.1:6379       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:6380       0.0.0.0:*                                                                                                  
LISTEN 0      5         172.17.0.1:11434      0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:7012       0.0.0.0:*                                                                                                  
LISTEN 0      4096      127.0.0.54:53         0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:7475       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:7300       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:7240       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8156       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8096       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8103       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8107       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8104       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8105       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8108       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8109       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8083       0.0.0.0:*                                                                                                  
LISTEN 0      511        127.0.0.1:8080       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8091       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8094       0.0.0.0:*                                                                                                  
LISTEN 0      2048       127.0.0.1:8095       0.0.0.0:*    users:(("gunicorn",pid=676829,fd=3),("gunicorn",pid=676822,fd=3),("gunicorn",pid=676804,fd=3))
LISTEN 0      4096       127.0.0.1:8074       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8075       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8073       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8079       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8056       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8057       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8060       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8061       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8035       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8032       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8042       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8046       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8045       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8019       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8016       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8017       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8026       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8025       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8030       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8002       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8003       0.0.0.0:*                                                                                                  
LISTEN 0      2048       127.0.0.1:8000       0.0.0.0:*    users:(("python3",pid=13982,fd=13))                                                           
LISTEN 0      4096       127.0.0.1:8007       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8004       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8005       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8008       0.0.0.0:*                                                                                                  
LISTEN 0      2048       127.0.0.1:8009       0.0.0.0:*    users:(("python3",pid=3917,fd=13))                                                            
LISTEN 0      4096       127.0.0.1:8014       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8015       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:7687       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8443       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8444       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8425       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8302       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8303       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8210       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8211       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8208       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8209       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8214       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8215       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8212       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8213       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8218       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8219       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8216       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8217       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8222       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8220       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8221       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8202       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8203       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8201       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8206       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8207       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8204       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:8205       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:9998       0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:11434      0.0.0.0:*                                                                                                  
LISTEN 0      4096       127.0.0.1:11436      0.0.0.0:*                                                                                                  
LISTEN 0      2048         0.0.0.0:8300       0.0.0.0:*    users:(("python3",pid=13987,fd=13))                                                           
LISTEN 0      2048         0.0.0.0:9000       0.0.0.0:*    users:(("gunicorn",pid=2015,fd=3),("gunicorn",pid=1924,fd=3),("gunicorn",pid=1588,fd=3))      
LISTEN 0      2048         0.0.0.0:9002       0.0.0.0:*    users:(("gunicorn",pid=2043,fd=3),("gunicorn",pid=1935,fd=3),("gunicorn",pid=1590,fd=3))      
LISTEN 0      4096   127.0.0.53%lo:53         0.0.0.0:*                                                                                                  
LISTEN 0      5         172.18.0.1:11434      0.0.0.0:*                                                                                                  
LISTEN 0      4096           [::1]:631           [::]:*                                                                                                  
LISTEN 0      4096               *:80               *:*                                                                                                  
LISTEN 0      4096            [::]:8093          [::]:*                                                                                                  
LISTEN 0      4096            [::]:8010          [::]:*                                                                                                  
LISTEN 0      511            [::1]:6379          [::]:*                                                                                                  
LISTEN 0      200             [::]:5436          [::]:*                                                                                                  

===== 12. POSTGRES DATABASES =====
Pager usage is off.
                                                              List of databases
          Name          |  Owner   | Encoding | Locale Provider |  Collate   |   Ctype    | ICU Locale | ICU Rules |    Access privileges     
------------------------+----------+----------+-----------------+------------+------------+------------+-----------+--------------------------
 msjarvis               | msjarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 msjarvisgis            | msjarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 msjarvisgis_v2         | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 msjarvisgis_v2_restore | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 postgres               | msjarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 template0              | msjarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/msjarvis             +
                        |          |          |                 |            |            |            |           | msjarvis=CTc/msjarvis
 template1              | msjarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/msjarvis             +
                        |          |          |                 |            |            |            |           | msjarvis=CTc/msjarvis
 template_postgis       | msjarvis | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 wv_gis                 | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =Tc/postgres            +
                        |          |          |                 |            |            |            |           | postgres=CTc/postgres   +
                        |          |          |                 |            |            |            |           | policy_writer=c/postgres
(9 rows)


===== 13. CHROMA HEALTH =====
{"nanosecond heartbeat":1786364580245097342}
===== 14. REDIS =====
PONG
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-trust-integration$ 


