(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild && \
echo '=== compose references ===' && \
grep -RIn --include='docker-compose*.yml' --include='compose*.yml' --include='*.yaml' 'mountainshares\|assertion-gateway\|auth_api\|8097\|5435\|5433' . 2>/dev/null | head -n 200 && \
echo '=== running containers ===' && \
docker ps -a --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}' | egrep 'mountain|jarvis|auth|postgres|redis' && \
echo '=== code using underscored names ===' && \
grep -RIn --include='*.py' --include='*.sql' 'mountainshares_ledger\|equity_timesheet\|mountainshares_balances' . 2>/dev/null | head -n 200 && \
echo '=== code using non-underscored names ===' && \
grep -RIn --include='*.py' --include='*.sql' 'mountainsharesledger\|equitytimesheet\|mountainsharesbalances' . 2>/dev/null | head -n 200
=== compose references ===
./docker-compose.yml:4:  mountainshares_sandbox:
./docker-compose.yml:7:      dockerfile: Dockerfile.mountainshares_sandbox
./docker-compose.yml:8:    container_name: mountainshares_sandbox
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.yml:4:  mountainshares_sandbox:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.yml:7:      dockerfile: Dockerfile.mountainshares_sandbox
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.yml:8:    container_name: mountainshares_sandbox
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:33:        published: "5435"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:196:  jarvis-assertion-gateway:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:198:      context: /mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-assertion-gateway
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:200:    container_name: jarvis-assertion-gateway
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:1627:      - POSTGRES_PORT=5433
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:1978:      - LOCAL_RESOURCES_PORT=5435
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:2369:  jarvis-mountainshares-commons-gateway:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:2372:      dockerfile: Dockerfile.mountainshares_commons_gateway
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:2373:    container_name: jarvis-mountainshares-commons-gateway
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:2402:        published: "5433"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:2696:        source: /home/cakidd/msjarvis-rebuild/data/mountainshares
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:2697:        target: /app/mountainshares_docs
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:2702:        source: /mnt/spiritual_drive/msjarvis-rebuild/services/backup_chroma_mountainshares_knowledge.json
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:2703:        target: /app/backup_mountainshares.json
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:3656:  ms-mountainshares-analytics:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:3657:    command: sh -c 'cd /app/services && python3 ms_mountainshares_analytics.py'
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:3660:      ms-mountainshares-coordinator:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:3677:  ms-mountainshares-coordinator:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:3678:    command: sh -c 'cd /app/services && python3 ms_mountainshares_coordinator.py'
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:3704:  ms-mountainshares-indexer:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:3705:    command: sh -c 'cd /app/services && python3 ms_mountainshares_indexer.py'
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.STABLE.20260719045021.yml:3708:      ms-mountainshares-coordinator:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.commons-gateway-closeout.yml:2:  jarvis-mountainshares-commons-gateway:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.commons-gateway-closeout.yml:3:    container_name: jarvis-mountainshares-commons-gateway
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/docker-compose.commons-gateway-closeout.yml:11:      - mountainshares_commons_gateway:app
./production_closeout_20260728/snapshot_deploy/docker-compose.direct-snapshot-mounts.yml:2:  jarvis-assertion-gateway:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.yml:4:  mountainshares_sandbox:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.yml:7:      dockerfile: Dockerfile.mountainshares_sandbox
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.yml:8:    container_name: mountainshares_sandbox
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:33:        published: "5435"
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:196:  jarvis-assertion-gateway:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:198:      context: /mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-assertion-gateway
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:200:    container_name: jarvis-assertion-gateway
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:1627:      - POSTGRES_PORT=5433
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:1978:      - LOCAL_RESOURCES_PORT=5435
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:2369:  jarvis-mountainshares-commons-gateway:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:2372:      dockerfile: Dockerfile.mountainshares_commons_gateway
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:2373:    container_name: jarvis-mountainshares-commons-gateway
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:2402:        published: "5433"
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:2696:        source: /home/cakidd/msjarvis-rebuild/data/mountainshares
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:2697:        target: /app/mountainshares_docs
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:2702:        source: /mnt/spiritual_drive/msjarvis-rebuild/services/backup_chroma_mountainshares_knowledge.json
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:2703:        target: /app/backup_mountainshares.json
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:3656:  ms-mountainshares-analytics:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:3657:    command: sh -c 'cd /app/services && python3 ms_mountainshares_analytics.py'
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:3660:      ms-mountainshares-coordinator:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:3677:  ms-mountainshares-coordinator:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:3678:    command: sh -c 'cd /app/services && python3 ms_mountainshares_coordinator.py'
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:3704:  ms-mountainshares-indexer:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:3705:    command: sh -c 'cd /app/services && python3 ms_mountainshares_indexer.py'
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.STABLE.20260719045021.yml:3708:      ms-mountainshares-coordinator:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.commons-gateway-closeout.yml:2:  jarvis-mountainshares-commons-gateway:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.commons-gateway-closeout.yml:3:    container_name: jarvis-mountainshares-commons-gateway
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/docker-compose.commons-gateway-closeout.yml:11:      - mountainshares_commons_gateway:app
./docker-compose.STABLE.20260719045021.yml:33:        published: "5435"
./docker-compose.STABLE.20260719045021.yml:196:  jarvis-assertion-gateway:
./docker-compose.STABLE.20260719045021.yml:198:      context: /mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-assertion-gateway
./docker-compose.STABLE.20260719045021.yml:200:    container_name: jarvis-assertion-gateway
./docker-compose.STABLE.20260719045021.yml:1628:      - POSTGRES_PORT=5433
./docker-compose.STABLE.20260719045021.yml:1979:      - LOCAL_RESOURCES_PORT=5435
./docker-compose.STABLE.20260719045021.yml:2370:  jarvis-mountainshares-commons-gateway:
./docker-compose.STABLE.20260719045021.yml:2373:      dockerfile: Dockerfile.mountainshares_commons_gateway
./docker-compose.STABLE.20260719045021.yml:2374:    container_name: jarvis-mountainshares-commons-gateway
./docker-compose.STABLE.20260719045021.yml:2403:        published: "5433"
./docker-compose.STABLE.20260719045021.yml:2697:        source: /home/cakidd/msjarvis-rebuild/data/mountainshares
./docker-compose.STABLE.20260719045021.yml:2698:        target: /app/mountainshares_docs
./docker-compose.STABLE.20260719045021.yml:2703:        source: /mnt/spiritual_drive/msjarvis-rebuild/services/backup_chroma_mountainshares_knowledge.json
./docker-compose.STABLE.20260719045021.yml:2704:        target: /app/backup_mountainshares.json
./docker-compose.STABLE.20260719045021.yml:3657:  ms-mountainshares-analytics:
./docker-compose.STABLE.20260719045021.yml:3658:    command: sh -c 'cd /app/services && python3 ms_mountainshares_analytics.py'
./docker-compose.STABLE.20260719045021.yml:3661:      ms-mountainshares-coordinator:
./docker-compose.STABLE.20260719045021.yml:3678:  ms-mountainshares-coordinator:
./docker-compose.STABLE.20260719045021.yml:3679:    command: sh -c 'cd /app/services && python3 ms_mountainshares_coordinator.py'
./docker-compose.STABLE.20260719045021.yml:3705:  ms-mountainshares-indexer:
./docker-compose.STABLE.20260719045021.yml:3706:    command: sh -c 'cd /app/services && python3 ms_mountainshares_indexer.py'
./docker-compose.STABLE.20260719045021.yml:3709:      ms-mountainshares-coordinator:
./docker-compose.commons-gateway-closeout.yml:2:  jarvis-mountainshares-commons-gateway:
./docker-compose.commons-gateway-closeout.yml:3:    container_name: jarvis-mountainshares-commons-gateway
./docker-compose.commons-gateway-closeout.yml:10:      - mountainshares_commons_gateway:app
=== running containers ===
jarvis-assertion-gateway                          msjarvis-rebuild-jarvis-assertion-gateway                 Exited (1) 2 minutes ago   
msjarvis-db-5433-proxy                            alpine/socat                                              Up 21 minutes              
jarvis-kyc-vault                                  msjarvis-rebuild-jarvis-kyc-vault:patched-20260730-1931   Up 3 hours                 127.0.0.1:8045->8045/tcp
jarvis-chat-worker                                msjarvis-rebuild-jarvis-chat-worker                       Up 20 hours                
jarvis-20llm-production                           msjarvis-rebuild-jarvis-20llm-production                  Up 5 hours                 127.0.0.1:8008->8008/tcp
jarvis-epistemic-runner                           jarvis-epistemic-runner:closeout-20260729                 Up 32 hours                127.0.0.1:8057->8057/tcp
jarvis-crypto-policy                              jarvis-main-brain:latest                                  Up 33 hours                8099/tcp
jarvis-mountainshares-commons-gateway             jarvis-commons-gateway:closeout-20260729                  Up 33 hours                127.0.0.1:8055->8055/tcp
jarvis-policy-set                                 jarvis-civic-intake:closeout-20260728-policy-openapi      Exited (0) 39 hours ago    
jarvis-dgm-23                                     msjarvis-rebuild-jarvis-dgm-23                            Up 2 days                  127.0.0.1:5123->5123/tcp
jarvis-dgm-22                                     msjarvis-rebuild-jarvis-dgm-22                            Up 2 days                  127.0.0.1:5122->5122/tcp
jarvis-dgm-21                                     msjarvis-rebuild-jarvis-dgm-21                            Up 2 days                  127.0.0.1:5121->5121/tcp
jarvis-dgm-20                                     msjarvis-rebuild-jarvis-dgm-20                            Up 2 days                  127.0.0.1:5120->5120/tcp
jarvis-dgm-19                                     msjarvis-rebuild-jarvis-dgm-19                            Up 2 days                  127.0.0.1:5119->5119/tcp
jarvis-dgm-18                                     msjarvis-rebuild-jarvis-dgm-18                            Up 2 days                  127.0.0.1:5118->5118/tcp
jarvis-dgm-17                                     msjarvis-rebuild-jarvis-dgm-17                            Up 2 days                  127.0.0.1:5117->5117/tcp
jarvis-dgm-16                                     msjarvis-rebuild-jarvis-dgm-16                            Up 2 days                  127.0.0.1:5116->5116/tcp
jarvis-dgm-15                                     msjarvis-rebuild-jarvis-dgm-15                            Up 2 days                  127.0.0.1:5115->5115/tcp
jarvis-dgm-14                                     msjarvis-rebuild-jarvis-dgm-14                            Up 2 days                  127.0.0.1:5114->5114/tcp
jarvis-dgm-13                                     msjarvis-rebuild-jarvis-dgm-13                            Up 2 days                  127.0.0.1:5113->5113/tcp
jarvis-dgm-12                                     msjarvis-rebuild-jarvis-dgm-12                            Up 2 days                  127.0.0.1:5112->5112/tcp
jarvis-dgm-11                                     msjarvis-rebuild-jarvis-dgm-11                            Up 2 days                  127.0.0.1:5111->5111/tcp
jarvis-dgm-10                                     msjarvis-rebuild-jarvis-dgm-10                            Up 2 days                  127.0.0.1:5110->5110/tcp
jarvis-dgm-09                                     msjarvis-rebuild-jarvis-dgm-09                            Up 2 days                  127.0.0.1:5109->5109/tcp
jarvis-dgm-08                                     msjarvis-rebuild-jarvis-dgm-08                            Up 2 days                  127.0.0.1:5108->5108/tcp
jarvis-dgm-07                                     msjarvis-rebuild-jarvis-dgm-07                            Up 2 days                  127.0.0.1:5107->5107/tcp
jarvis-dgm-06                                     msjarvis-rebuild-jarvis-dgm-06                            Up 2 days                  127.0.0.1:5106->5106/tcp
jarvis-dgm-05                                     msjarvis-rebuild-jarvis-dgm-05                            Up 2 days                  127.0.0.1:5105->5105/tcp
jarvis-contracts                                  jarvis-contracts:asbuilt-20260728-solc-0.8.24-tested-v3   Up 2 days                  
jarvis-nbb-i-containers-2                         nbb-i-containers:asbuilt-20260728-v3                      Up 2 days                  127.0.0.1:8015->8015/tcp
jarvis-commons-optin-intake                       jarvis-commons-optin-intake:closeout-20260728-v2          Up 2 days                  127.0.0.1:8061->8061/tcp
jarvis-belief-revision                            jarvis-belief-revision:asbuilt-20260728                   Up 2 days                  127.0.0.1:7240->7240/tcp
jarvis-blood-brain-barrier                        jarvis-blood-brain-barrier:asbuilt-20260728               Up 2 days                  127.0.0.1:8016->8016/tcp
jarvis-wv-entangled-gateway                       jarvis-wv-entangled-gateway:asbuilt-20260728              Up 5 hours                 127.0.0.1:8010->8010/tcp
jarvis-brain-orchestrator                         jarvis-brain-orchestrator:asbuilt-20260728                Up 2 days (healthy)        127.0.0.1:17260->7260/tcp
jarvis-main-brain                                 jarvis-main-brain:asbuilt-20260728                        Up 2 days                  127.0.0.1:8050->8050/tcp
jarvis-lm-synthesizer                             jarvis-lm-synthesizer:asbuilt-20260728                    Up 2 days                  8001/tcp
jarvis-fifth-dgm                                  jarvis-fifth-dgm:asbuilt-20260728                         Up 2 days                  127.0.0.1:4002->4002/tcp
jarvis-woah                                       jarvis-woah:asbuilt-20260728                              Up 2 days                  127.0.0.1:7012->7012/tcp
jarvis-stewardship-scheduler                      jarvis-main-brain:latest                                  Up 2 days                  127.0.0.1:8079->8079/tcp
jarvis-steward                                    jarvis-main-brain:latest                                  Up 2 days                  127.0.0.1:8014->8014/tcp
jarvis-spatial-sandbox                            python:3.11-slim                                          Up 2 days                  127.0.0.1:8056->8056/tcp
jarvis-pia-sampler                                python:3.11-slim                                          Up 2 days                  8076/tcp
jarvis-ollama-tls                                 nginx:stable                                              Up 2 days                  80/tcp, 127.0.0.1:11436->11436/tcp
jarvis-hilbert-time                               jarvis-main-brain:latest                                  Up 2 days                  127.0.0.1:18094->8092/tcp
jarvis-hilbert-gateway                            jarvis-main-brain:latest                                  Up 2 days                  127.0.0.1:18091->8081/tcp
jarvis-gis-rag-tls                                nginx:stable                                              Up 2 days                  80/tcp, 127.0.0.1:8444->8444/tcp
jarvis-chroma-tls                                 nginx:stable                                              Up 2 days                  80/tcp, 127.0.0.1:8443->8443/tcp
jarvis-autonomous-learner                         msjarvis-rebuild-jarvis-rag-server:latest                 Up 2 days                  127.0.0.1:8425->8425/tcp
jarvis-fractal-consciousness                      msjarvis-rebuild-jarvis-fractal-consciousness             Up 2 days                  8027/tcp
jarvis-policy-set-preopenapi-20260728             jarvis-civic-intake:closeout-20260728                     Exited (0) 2 days ago      
jarvis-civic-intake                               jarvis-civic-intake:closeout-20260728                     Up 2 days                  8100/tcp
jarvis-gis-rag                                    msjarvis-rebuild-jarvis-gis-rag                           Up 6 days                  127.0.0.1:8004->8004/tcp, 8044/tcp
jarvis-judge-truth                                msjarvis-rebuild-jarvis-judge-truth                       Up 6 days                  127.0.0.1:8035->7230/tcp
ms-allis-internal-sandbox                         msjarvis-rebuild-ms-allis-internal-sandbox                Up 7 days                  127.0.0.1:8042->8042/tcp
jarvis-memory                                     msjarvis-rebuild-jarvis-memory                            Up 7 days                  127.0.0.1:8156->8056/tcp
jarvis-unified-gateway                            msjarvis-rebuild-jarvis-unified-gateway                   Up 26 hours (healthy)      127.0.0.1:8093->8001/tcp
jarvis-auth-api                                   msjarvis/jarvis-auth-api:patched                          Up 7 days                  127.0.0.1:8096->8091/tcp
jarvis-dgm-03                                     msjarvis-rebuild-jarvis-dgm-03                            Up 7 days                  5103/tcp
jarvis-dgm-02                                     msjarvis-rebuild-jarvis-dgm-02                            Up 7 days                  5102/tcp
jarvis-dgm-01                                     msjarvis-rebuild-jarvis-dgm-01                            Up 7 days                  5101/tcp
jarvis-dgm-04                                     msjarvis-rebuild-jarvis-dgm-04                            Up 7 days                  5104/tcp
jarvis-chroma                                     chromadb/chroma:0.6.3                                     Up 7 days (healthy)        127.0.0.1:8002->8000/tcp
jarvis-phi-probe                                  msjarvis-rebuild-jarvis-phi-probe                         Up 7 days                  127.0.0.1:8026->8025/tcp
jarvis-hilbert-state                              jarvis-main-brain:latest                                  Up 7 days                  127.0.0.1:18092->8081/tcp
jarvis-msjarvis-db                                postgis/postgis:16-3.4                                    Up 39 hours                5432/tcp
jarvis-consciousness-bridge-temp                  python:3.11-slim                                          Exited (137) 8 days ago    
55e2824e1e9b_jarvis-neurobiological-master        msjarvis-rebuild-jarvis-neurobiological-master            Created                    
nbb_prefrontal_cortex                             msjarvis-rebuild-nbb_prefrontal_cortex                    Up 7 days                  127.0.0.1:8105->7005/tcp
jarvis-rag-server                                 msjarvis-rebuild-jarvis-rag-server                        Up 7 days                  127.0.0.1:8003->8003/tcp
jarvis-gbim-query-router                          jarvis-main-brain:latest                                  Exited (0) 10 days ago     
jarvis-ollama                                     ollama/ollama:latest                                      Up 6 days                  127.0.0.1:11434->11434/tcp
jarvis-i-containers                               msjarvis-rebuild-jarvis-i-containers                      Up 7 days                  8015/tcp
jarvis-dgm-23-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-23                            Exited (137) 2 days ago    
jarvis-dgm-22-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-22                            Exited (137) 2 days ago    
jarvis-dgm-21-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-21                            Exited (137) 2 days ago    
jarvis-dgm-20-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-20                            Exited (137) 2 days ago    
jarvis-dgm-19-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-19                            Exited (137) 2 days ago    
jarvis-dgm-18-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-18                            Exited (137) 2 days ago    
jarvis-dgm-17-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-17                            Exited (137) 2 days ago    
jarvis-dgm-16-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-16                            Exited (137) 2 days ago    
jarvis-dgm-15-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-15                            Exited (137) 2 days ago    
jarvis-dgm-14-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-14                            Exited (137) 2 days ago    
jarvis-dgm-13-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-13                            Exited (137) 2 days ago    
jarvis-dgm-12-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-12                            Exited (137) 2 days ago    
jarvis-dgm-11-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-11                            Exited (137) 2 days ago    
jarvis-dgm-10-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-10                            Exited (137) 2 days ago    
jarvis-dgm-09-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-09                            Exited (137) 2 days ago    
jarvis-dgm-08-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-08                            Exited (137) 2 days ago    
jarvis-dgm-07-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-07                            Exited (137) 2 days ago    
jarvis-dgm-06-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-06                            Exited (137) 2 days ago    
jarvis-dgm-05-preloopback-20260728                msjarvis-rebuild-jarvis-dgm-05                            Exited (137) 2 days ago    
jarvis-neurobiological-master                     msjarvis-rebuild-jarvis-neurobiological-master            Up 7 days                  8018/tcp
jarvis-intake-service                             jarvis-main-brain:latest                                  Up 7 days                  127.0.0.1:8007->8007/tcp
d6cfb685887e_jarvis-qualia-engine                 msjarvis-rebuild-jarvis-qualia-engine                     Created                    
nbb_qualia_engine                                 msjarvis-rebuild-nbb_qualia_engine                        Up 7 days                  127.0.0.1:8303->8010/tcp
83b469105701_jarvis-ingest-watcher                jarvis-main-brain:latest                                  Created                    
7695786a2c17_jarvis-hilbert-commons               msjarvis-rebuild-jarvis-hilbert-commons                   Created                    
jarvis-hp-sidecar                                 jarvis-hp-sidecar:local                                   Up 7 days                  127.0.0.1:8094->8094/tcp
588b015a5d92_jarvis-gbim-benefit-indexer          jarvis-main-brain:latest                                  Created                    
fea7131a2e55_jarvis-commons-gamification          jarvis-main-brain:latest                                  Created                    
c1fb4544a3bd_jarvis-dao-governance                jarvis-main-brain:latest                                  Created                    
442313afede2_jarvis-community-stake-registry      jarvis-main-brain:latest                                  Created                    
476a8a928cd7_jarvis-ms-analytics                  877712e4f657                                              Created                    
87731cb669d0_jarvis-ms-indexer                    877712e4f657                                              Created                    
d13f0d5cb66f_jarvis-ms-coordinator                877712e4f657                                              Created                    
374ec8ab07e5_jarvis-local-resources               msjarvis-rebuild-jarvis-local-resources                   Created                    
56c99d59f7a5_jarvis-session-sidecar               jarvis-session-sidecar:latest                             Up 7 days                  127.0.0.1:8060->8060/tcp, 8070/tcp
8be7c5cb1820_jarvis-hippocampus                   msjarvis-rebuild-jarvis-hippocampus                       Created                    
jarvis-redis                                      redis:7-alpine                                            Up 7 days (healthy)        127.0.0.1:6380->6379/tcp
e665651c00d5_llm2-proxy                           msjarvis-rebuild-llm2-proxy                               Up 6 days                  127.0.0.1:8202->8202/tcp
2d6c035dc9fe_llm20-proxy                          msjarvis-rebuild-llm20-proxy                              Up 6 days                  127.0.0.1:8220->8220/tcp
b91b3c2adba5_llm17-proxy                          msjarvis-rebuild-llm17-proxy                              Up 6 days                  127.0.0.1:8217->8217/tcp
b5a2b182f1b7_llm19-proxy                          msjarvis-rebuild-llm19-proxy                              Up 6 days                  127.0.0.1:8219->8219/tcp
2deb1f7c2c97_jarvis-dgm-bridge-09                 msjarvis-rebuild-jarvis-dgm-bridge-09:latest              Created                    
c68db82137f8_llm9-proxy                           msjarvis-rebuild-llm9-proxy                               Up 6 days                  127.0.0.1:8209->8209/tcp
88d6e6d22fc5_jarvis-dgm-bridge-14                 msjarvis-rebuild-jarvis-dgm-bridge-14:latest              Created                    
05cbdb9d8b63_llm18-proxy                          msjarvis-rebuild-llm18-proxy                              Up 6 days                  127.0.0.1:8218->8218/tcp
a8416407179c_nbb_spiritual_root                   msjarvis-rebuild-nbb_spiritual_root                       Up 7 days                  127.0.0.1:8103->8010/tcp
83107192806b_jarvis-dgm-bridge-23                 msjarvis-rebuild-jarvis-dgm-bridge-23:latest              Created                    
1d653a8a0fcb_jarvis-mother-protocols              msjarvis-rebuild-jarvis-mother-protocols                  Up 7 days                  4000/tcp
07868f87c30f_llm10-proxy                          msjarvis-rebuild-llm10-proxy                              Up 6 days                  127.0.0.1:8210->8210/tcp
f970d6243de9_llm1-proxy                           msjarvis-rebuild-llm1-proxy                               Up 6 days                  127.0.0.1:8201->8201/tcp
1e1783a0cae3_jarvis-temporal-consciousness        msjarvis-rebuild-jarvis-temporal-consciousness            Up 7 days                  7007/tcp
bbd55aa39149_llm13-proxy                          msjarvis-rebuild-llm13-proxy                              Up 6 days                  127.0.0.1:8213->8213/tcp
cdb1cfcf3615_llm15-proxy                          msjarvis-rebuild-llm15-proxy                              Up 6 days                  127.0.0.1:8215->8215/tcp
03da3490dbba_llm12-proxy                          msjarvis-rebuild-llm12-proxy                              Up 6 days                  127.0.0.1:8212->8212/tcp
cd7a66d93ac6_jarvis-dgm-bridge-16                 msjarvis-rebuild-jarvis-dgm-bridge-16:latest              Created                    
2c6d4b7ee36f_nbb-i-containers                     msjarvis-rebuild-nbb-i-containers                         Created                    
b9f25945034e_llm6-proxy                           msjarvis-rebuild-llm6-proxy                               Up 6 days                  127.0.0.1:8206->8206/tcp
0f40caf56e1e_nbb_mother_carrie_protocols          msjarvis-rebuild-nbb_mother_carrie_protocols              Up 7 days                  127.0.0.1:8107->8010/tcp
d726744ac7b6_nbb_subconscious                     msjarvis-rebuild-nbb_subconscious                         Created                    
34a411a13e56_jarvis-dgm-bridge-05                 msjarvis-rebuild-jarvis-dgm-bridge-05:latest              Created                    
b64d71635493_jarvis-dgm-bridge-21                 msjarvis-rebuild-jarvis-dgm-bridge-21:latest              Created                    
016624f872e9_nbb_consciousness_containers         msjarvis-rebuild-nbb_consciousness_containers             Created                    
6c076127418c_llm4-proxy                           msjarvis-rebuild-llm4-proxy                               Up 6 days                  127.0.0.1:8204->8204/tcp
6dd05bcbf535_llm5-proxy                           msjarvis-rebuild-llm5-proxy                               Up 6 days                  127.0.0.1:8205->8205/tcp
f85353dc2357_jarvis-dgm-bridge-01                 msjarvis-rebuild-jarvis-dgm-bridge-01:latest              Created                    
7450f93f1840_psychological_rag_domain             msjarvis-rebuild-psychological_rag_domain                 Created                    
32c012be1f39_jarvis-dgm-bridge-22                 msjarvis-rebuild-jarvis-dgm-bridge-22:latest              Created                    
f49af6a3d696_llm7-proxy                           msjarvis-rebuild-llm7-proxy                               Up 6 days                  127.0.0.1:8207->8207/tcp
687596ae0eb1_llm22-proxy                          msjarvis-rebuild-llm22-proxy                              Up 6 days                  127.0.0.1:8222->8222/tcp
aae4a8928928_nbb_spiritual_maternal_integration   msjarvis-rebuild-nbb_spiritual_maternal_integration       Up 7 days                  127.0.0.1:8109->8010/tcp
a40eece620f3_nbb_woah_algorithms                  msjarvis-rebuild-nbb_woah_algorithms                      Up 7 days                  127.0.0.1:8104->8010/tcp
eeb98757a243_llm21-proxy                          msjarvis-rebuild-llm21-proxy                              Up 6 days                  127.0.0.1:8221->8221/tcp
5583028e194d_nbb_heteroglobulin_transport         msjarvis-rebuild-nbb_heteroglobulin_transport             Created                    
8d56fc8a524b_jarvis-dgm-bridge-06                 msjarvis-rebuild-jarvis-dgm-bridge-06:latest              Created                    
317bdadaa740_jarvis-dgm-bridge-15                 msjarvis-rebuild-jarvis-dgm-bridge-15:latest              Created                    
8dffd2f7b142_llm3-proxy                           msjarvis-rebuild-llm3-proxy                               Up 6 days                  127.0.0.1:8203->8203/tcp
ee7caaa7707e_jarvis-dgm-bridge-20                 msjarvis-rebuild-jarvis-dgm-bridge-20:latest              Created                    
cacc76ea4643_nbb_blood_brain_barrier              msjarvis-rebuild-nbb_blood_brain_barrier                  Created                    
6063d2fd2b57_jarvis-dgm-bridge-07                 msjarvis-rebuild-jarvis-dgm-bridge-07:latest              Created                    
22cb4468dbd5_llm8-proxy                           msjarvis-rebuild-llm8-proxy                               Up 6 days                  127.0.0.1:8208->8208/tcp
720606c93fb5_jarvis-dgm-bridge-18                 msjarvis-rebuild-jarvis-dgm-bridge-18:latest              Created                    
675f8bd43968_llm11-proxy                          msjarvis-rebuild-llm11-proxy                              Up 6 days                  127.0.0.1:8211->8211/tcp
d5abcf6816b1_jarvis-dgm-bridge-12                 msjarvis-rebuild-jarvis-dgm-bridge-12:latest              Created                    
0fe048e236a2_jarvis-dgm-bridge-17                 msjarvis-rebuild-jarvis-dgm-bridge-17:latest              Created                    
6e3371d9a45b_jarvis-dgm-bridge-13                 msjarvis-rebuild-jarvis-dgm-bridge-13:latest              Created                    
d143ecf04a83_jarvis-69dgm-bridge                  msjarvis-rebuild-jarvis-69dgm-bridge                      Created                    
09d31d2da8cf_jarvis-dgm-bridge-03                 msjarvis-rebuild-jarvis-dgm-bridge-03:latest              Created                    
ae475806a449_jarvis-dgm-bridge-08                 msjarvis-rebuild-jarvis-dgm-bridge-08:latest              Created                    
9d78df19ad7b_jarvis-dgm-bridge-19                 msjarvis-rebuild-jarvis-dgm-bridge-19:latest              Created                    
0794da8eb926_jarvis-dgm-bridge-11                 msjarvis-rebuild-jarvis-dgm-bridge-11:latest              Created                    
43f524c3852a_jarvis-dgm-bridge-10                 msjarvis-rebuild-jarvis-dgm-bridge-10:latest              Created                    
be5c6613bca3_llm14-proxy                          msjarvis-rebuild-llm14-proxy                              Up 6 days                  127.0.0.1:8214->8214/tcp
69ee8c1dadfb_llm16-proxy                          msjarvis-rebuild-llm16-proxy                              Up 6 days                  127.0.0.1:8216->8216/tcp
0030c0c3bcf5_jarvis-dgm-bridge-02                 msjarvis-rebuild-jarvis-dgm-bridge-02:latest              Created                    
c3bc24fe5365_jarvis-dgm-bridge-04                 msjarvis-rebuild-jarvis-dgm-bridge-04:latest              Created                    
nbb_pituitary_gland                               msjarvis-rebuild-nbb_pituitary_gland                      Up 7 days                  127.0.0.1:8108->80/tcp
jarvis-constitutional-guardian                    msjarvis-rebuild-jarvis-constitutional-guardian           Up 7 days                  127.0.0.1:8091->8091/tcp
jarvis-judge-pipeline                             msjarvis-rebuild-jarvis-judge-pipeline                    Up 6 days                  7239/tcp
jarvis-semaphore                                  msjarvis-rebuild-jarvis-semaphore                         Up 3 days                  127.0.0.1:8030->8030/tcp
jarvis-web-research                               msjarvis-rebuild-jarvis-web-research                      Up 7 days                  8008/tcp
jarvis-judge-alignment                            msjarvis-rebuild-jarvis-judge-alignment                   Up 7 days                  7232/tcp
jarvis-spiritual-rag                              msjarvis-rebuild-jarvis-spiritual-rag                     Up 7 days                  127.0.0.1:8005->8005/tcp
jarvis-eeg-theta                                  msjarvis-rebuild-jarvis-eeg-theta                         Up 7 days                  127.0.0.1:8074->8074/tcp
jarvis-eeg-delta                                  msjarvis-rebuild-jarvis-eeg-delta                         Up 7 days                  127.0.0.1:8073->8073/tcp
jarvis-swarm-intelligence                         msjarvis-rebuild-jarvis-swarm-intelligence                Up 7 days                  8021/tcp
jarvis-provenance                                 msjarvis-rebuild-jarvis-provenance                        Up 7 days                  127.0.0.1:8046->8046/tcp
jarvis-ingest-api                                 python:3.11-slim                                          Up 5 hours                 
jarvis-eeg-beta                                   msjarvis-rebuild-jarvis-eeg-beta                          Up 7 days                  127.0.0.1:8075->8075/tcp
jarvis-rag-router                                 msjarvis-rebuild-jarvis-rag-router                        Up 7 days                  8003/tcp, 127.0.0.1:5015->5001/tcp
jarvis-aaacpe-rag                                 msjarvis-rebuild-jarvis-aaacpe-rag                        Up 7 days                  127.0.0.1:8032->8032/tcp
jarvis-aaacpe-scraper                             msjarvis-rebuild-jarvis-aaacpe-scraper                    Up 6 days                  127.0.0.1:8033->8033/tcp
jarvis-judge-ethics                               msjarvis-rebuild-jarvis-judge-ethics                      Up 7 days                  7233/tcp
jarvis-agents-service                             msjarvis-rebuild-jarvis-agents-service                    Up 7 days                  8005/tcp
jarvis-judge-consistency                          msjarvis-rebuild-jarvis-judge-consistency                 Up 6 days                  7231/tcp
jarvis-jaeger                                     jaegertracing/all-in-one:1.52                             Up 7 days                  4317-4318/tcp, 5775/udp, 5778/tcp, 9411/tcp, 14250/tcp, 14268/tcp, 6831-6832/udp, 127.0.0.1:16686->16686/tcp
jarvis-toroidal                                   msjarvis-toroidal:latest                                  Up 7 days                  127.0.0.1:8025->8025/tcp
jarvis-psychology-services                        msjarvis-rebuild-jarvis-psychology-services               Up 7 days                  127.0.0.1:8019->8019/tcp
=== code using underscored names ===
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:49:                    "SELECT ems_balance FROM mountainshares_balances WHERE ueid = %s",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:58:                    "FROM mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:82:                    "UPDATE mountainshares_balances "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:93:                    "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:190:                    "UPDATE mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:226:                        "UPDATE mountainshares_balances "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:232:                        "UPDATE mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/chain_listener.py:68:                "UPDATE mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:600:            _cur.execute("INSERT INTO mountainshares_balances (ueid) VALUES (%s) ON CONFLICT DO NOTHING", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:619:                    _cur.execute("SELECT COUNT(*) FROM mountainshares_ledger WHERE ueid = %s AND transaction_type = 'founding_grant'", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:622:                            "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:631:                        "UPDATE mountainshares_balances SET ems_balance = ems_balance + 100.0000, "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:871:        cur.execute("SELECT ems_balance, rank, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:875:        cur.execute("SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s AND ueid IN (%s, %s)", (sub, sub, f"UEID-{sub.upper()}-ADMIN"))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:932:            "FROM mountainshares_ledger " + where +
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:938:            "SELECT COUNT(*) FROM mountainshares_ledger " + where,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:1029:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:1038:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/003_ledger_columns.sql:1:ALTER TABLE mountainshares_ledger
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/003_ledger_columns.sql:8:CREATE OR REPLACE VIEW mountainshares_ledger_v AS
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/003_ledger_columns.sql:9:    SELECT *, ems_amount AS amount FROM mountainshares_ledger;
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/004_ledger_event_types.sql:2:ALTER TABLE mountainshares_ledger
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/004_ledger_event_types.sql:3:    DROP CONSTRAINT mountainshares_ledger_event_type_check;
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/004_ledger_event_types.sql:5:ALTER TABLE mountainshares_ledger
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/004_ledger_event_types.sql:6:    ADD CONSTRAINT mountainshares_ledger_event_type_check
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:422:            _cur.execute("INSERT INTO mountainshares_balances (ueid) VALUES (%s) ON CONFLICT DO NOTHING", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:435:                    _cur.execute("SELECT COUNT(*) FROM mountainshares_ledger WHERE ueid = %s AND transaction_type = 'founding_grant'", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:438:                        "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:447:                        "UPDATE mountainshares_balances SET ems_balance = ems_balance + 100.0000, "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:634:        cur.execute("SELECT ems_balance, rank, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:638:        cur.execute("SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s AND ueid IN (%s, %s)", (sub, sub, f"UEID-{sub.upper()}-ADMIN"))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:695:            "FROM mountainshares_ledger " + where +
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:701:            "SELECT COUNT(*) FROM mountainshares_ledger " + where,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:792:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:801:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/scripts/materialize_tensor_bridge.py:17:    'geo_equity_timesheet',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/scripts/materialize_tensor_bridge.py:18:    'geo_equity_timesheet_ctx_backup',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/scripts/materialize_tensor_bridge.py:26:    'equity_timesheet',
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:49:                    "SELECT ems_balance FROM mountainshares_balances WHERE ueid = %s",
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:58:                    "FROM mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:82:                    "UPDATE mountainshares_balances "
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:93:                    "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:190:                    "UPDATE mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:226:                        "UPDATE mountainshares_balances "
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:232:                        "UPDATE mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/chain_listener.py:68:                "UPDATE mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:49:                    "SELECT ems_balance FROM mountainshares_balances WHERE ueid = %s",
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:58:                    "FROM mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:82:                    "UPDATE mountainshares_balances "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:93:                    "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:190:                    "UPDATE mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:226:                        "UPDATE mountainshares_balances "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:232:                        "UPDATE mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/chain_listener.py:68:                "UPDATE mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:49:                    "SELECT ems_balance FROM mountainshares_balances WHERE ueid = %s",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:58:                    "FROM mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:82:                    "UPDATE mountainshares_balances "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:93:                    "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:190:                    "UPDATE mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:226:                        "UPDATE mountainshares_balances "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:232:                        "UPDATE mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/chain_listener.py:68:                "UPDATE mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:600:            _cur.execute("INSERT INTO mountainshares_balances (ueid) VALUES (%s) ON CONFLICT DO NOTHING", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:619:                    _cur.execute("SELECT COUNT(*) FROM mountainshares_ledger WHERE ueid = %s AND transaction_type = 'founding_grant'", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:622:                            "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:631:                        "UPDATE mountainshares_balances SET ems_balance = ems_balance + 100.0000, "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:871:        cur.execute("SELECT ems_balance, rank, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:875:        cur.execute("SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s AND ueid IN (%s, %s)", (sub, sub, f"UEID-{sub.upper()}-ADMIN"))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:932:            "FROM mountainshares_ledger " + where +
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:938:            "SELECT COUNT(*) FROM mountainshares_ledger " + where,
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:1029:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:1038:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/003_ledger_columns.sql:1:ALTER TABLE mountainshares_ledger
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/003_ledger_columns.sql:8:CREATE OR REPLACE VIEW mountainshares_ledger_v AS
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/003_ledger_columns.sql:9:    SELECT *, ems_amount AS amount FROM mountainshares_ledger;
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/004_ledger_event_types.sql:2:ALTER TABLE mountainshares_ledger
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/004_ledger_event_types.sql:3:    DROP CONSTRAINT mountainshares_ledger_event_type_check;
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/004_ledger_event_types.sql:5:ALTER TABLE mountainshares_ledger
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/004_ledger_event_types.sql:6:    ADD CONSTRAINT mountainshares_ledger_event_type_check
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:422:            _cur.execute("INSERT INTO mountainshares_balances (ueid) VALUES (%s) ON CONFLICT DO NOTHING", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:435:                    _cur.execute("SELECT COUNT(*) FROM mountainshares_ledger WHERE ueid = %s AND transaction_type = 'founding_grant'", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:438:                        "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:447:                        "UPDATE mountainshares_balances SET ems_balance = ems_balance + 100.0000, "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:634:        cur.execute("SELECT ems_balance, rank, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:638:        cur.execute("SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s AND ueid IN (%s, %s)", (sub, sub, f"UEID-{sub.upper()}-ADMIN"))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:695:            "FROM mountainshares_ledger " + where +
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:701:            "SELECT COUNT(*) FROM mountainshares_ledger " + where,
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:792:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:801:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/scripts/materialize_tensor_bridge.py:17:    'geo_equity_timesheet',
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/scripts/materialize_tensor_bridge.py:18:    'geo_equity_timesheet_ctx_backup',
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/scripts/materialize_tensor_bridge.py:26:    'equity_timesheet',
./services/conversion_service.py:49:                    "SELECT ems_balance FROM mountainshares_balances WHERE ueid = %s",
./services/conversion_service.py:58:                    "FROM mountainshares_ledger "
./services/conversion_service.py:82:                    "UPDATE mountainshares_balances "
./services/conversion_service.py:93:                    "INSERT INTO mountainshares_ledger "
./services/conversion_service.py:190:                    "UPDATE mountainshares_ledger "
./services/conversion_service.py:226:                        "UPDATE mountainshares_balances "
./services/conversion_service.py:232:                        "UPDATE mountainshares_ledger "
./services/chain_listener.py:68:                "UPDATE mountainshares_ledger "
./auth_router.py:600:            _cur.execute("INSERT INTO mountainshares_balances (ueid) VALUES (%s) ON CONFLICT DO NOTHING", (_ueid,))
./auth_router.py:619:                    _cur.execute("SELECT COUNT(*) FROM mountainshares_ledger WHERE ueid = %s AND transaction_type = 'founding_grant'", (_ueid,))
./auth_router.py:622:                            "INSERT INTO mountainshares_ledger "
./auth_router.py:631:                        "UPDATE mountainshares_balances SET ems_balance = ems_balance + 100.0000, "
./auth_router.py:871:        cur.execute("SELECT ems_balance, rank, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
./auth_router.py:875:        cur.execute("SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s AND ueid IN (%s, %s)", (sub, sub, f"UEID-{sub.upper()}-ADMIN"))
./auth_router.py:932:            "FROM mountainshares_ledger " + where +
./auth_router.py:938:            "SELECT COUNT(*) FROM mountainshares_ledger " + where,
./auth_router.py:1029:            FROM equity_timesheet
./auth_router.py:1038:            FROM equity_timesheet
./migrations/003_ledger_columns.sql:1:ALTER TABLE mountainshares_ledger
./migrations/003_ledger_columns.sql:8:CREATE OR REPLACE VIEW mountainshares_ledger_v AS
./migrations/003_ledger_columns.sql:9:    SELECT *, ems_amount AS amount FROM mountainshares_ledger;
./migrations/004_ledger_event_types.sql:2:ALTER TABLE mountainshares_ledger
./migrations/004_ledger_event_types.sql:3:    DROP CONSTRAINT mountainshares_ledger_event_type_check;
./migrations/004_ledger_event_types.sql:5:ALTER TABLE mountainshares_ledger
./migrations/004_ledger_event_types.sql:6:    ADD CONSTRAINT mountainshares_ledger_event_type_check
./.archive/debug_files_20260630/auth_router.debug.py:422:            _cur.execute("INSERT INTO mountainshares_balances (ueid) VALUES (%s) ON CONFLICT DO NOTHING", (_ueid,))
./.archive/debug_files_20260630/auth_router.debug.py:435:                    _cur.execute("SELECT COUNT(*) FROM mountainshares_ledger WHERE ueid = %s AND transaction_type = 'founding_grant'", (_ueid,))
./.archive/debug_files_20260630/auth_router.debug.py:438:                        "INSERT INTO mountainshares_ledger "
./.archive/debug_files_20260630/auth_router.debug.py:447:                        "UPDATE mountainshares_balances SET ems_balance = ems_balance + 100.0000, "
./.archive/debug_files_20260630/auth_router.debug.py:634:        cur.execute("SELECT ems_balance, rank, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
./.archive/debug_files_20260630/auth_router.debug.py:638:        cur.execute("SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s AND ueid IN (%s, %s)", (sub, sub, f"UEID-{sub.upper()}-ADMIN"))
./.archive/debug_files_20260630/auth_router.debug.py:695:            "FROM mountainshares_ledger " + where +
./.archive/debug_files_20260630/auth_router.debug.py:701:            "SELECT COUNT(*) FROM mountainshares_ledger " + where,
./.archive/debug_files_20260630/auth_router.debug.py:792:            FROM equity_timesheet
./.archive/debug_files_20260630/auth_router.debug.py:801:            FROM equity_timesheet
./scripts/materialize_tensor_bridge.py:17:    'geo_equity_timesheet',
./scripts/materialize_tensor_bridge.py:18:    'geo_equity_timesheet_ctx_backup',
./scripts/materialize_tensor_bridge.py:26:    'equity_timesheet',
=== code using non-underscored names ===
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

