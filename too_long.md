crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild

# Full rebuild sequence
docker compose down

docker compose build --parallel 2>&1 | tee /tmp/build.log

docker compose up -d 2>&1 | tee /tmp/up.log

# Watch it come up
watch -n3 'docker ps --format "table {{.Name}}\t{{.Status}}" | grep -v "Up " | head -20'
[+] down 105/105
 ✔ Container llm5-proxy                                   Removed         2.0s
 ✔ Container jarvis-dgm-bridge-13                         Removed         1.4s
 ✔ Container jarvis-hippocampus                           Removed         4.6s
 ✔ Container llm6-proxy                                   Removed         2.5s
 ✔ Container llm10-proxy                                  Removed         2.5s
 ✔ Container jarvis-dgm-bridge-01                         Removed         1.6s
 ✔ Container llm3-proxy                                   Removed         2.7s
 ✔ Container jarvis-local-resources                       Removed         2.2s
 ✔ Container jarvis-dgm-bridge-17                         Removed         1.9s
 ✔ Container llm15-proxy                                  Removed         2.4s
 ✔ Container llm21-proxy                                  Removed         3.8s
 ✔ Container llm7-proxy                                   Removed         2.6s
 ✔ Container llm1-proxy                                   Removed         3.3s
 ✔ Container jarvis-dgm-bridge-15                         Removed         1.9s
 ✔ Container mysql                                        Removed         4.6s
 ✔ Container msjarvis-rebuild-nbb_darwin_godel_machines-1 Removed         2.6s
 ✔ Container jarvis-dgm-bridge-07                         Removed         1.8s
 ✔ Container llm14-proxy                                  Removed         2.3s
 ✔ Container jarvis-69dgm-bridge                          Removed         4.2s
 ✔ Container jarvis-dgm-bridge-19                         Removed         1.4s
 ✔ Container llm22-proxy                                  Removed         3.5s
 ... 84 more                                                                  
 Image msjarvis-rebuild-jarvis-brain-orchestrator Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-14 Building 
 Image msjarvis-rebuild-jarvis-judge-ethics Building 
 Image msjarvis-rebuild-jarvis-gis-rag Building 
 Image msjarvis-rebuild-llm15-proxy Building 
 Image msjarvis-rebuild-jarvis-judge-truth Building 
 Image msjarvis-rebuild-nbb_subconscious Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-20 Building 
 Image msjarvis-rebuild-nbb_spiritual_root Building 
 Image msjarvis-rebuild-nbb_pituitary_gland Building 
 Image jarvis-main-brain:latest Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-18 Building 
 Image msjarvis-rebuild-jarvis-spiritual-rag Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-05 Building 
 Image msjarvis-rebuild-llm22-proxy Building 
 Image msjarvis-rebuild-llm6-proxy Building 
 Image msjarvis-rebuild-jarvis-local-resources Building 
 Image msjarvis-rebuild-jarvis-judge-alignment Building 
 Image msjarvis-rebuild-llm20-proxy Building 
 Image msjarvis-rebuild-nbb_woah_algorithms Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-22 Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-08 Building 
 Image msjarvis-rebuild-jarvis-wv-entangled-gateway Building 
 Image msjarvis-rebuild-nbb_darwin_godel_machines Building 
 Image msjarvis-rebuild-jarvis-consciousness-bridge Building 
 Image msjarvis-rebuild-psychological_rag_domain Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-07 Building 
 Image msjarvis-rebuild-jarvis-agents-service Building 
 Image msjarvis-rebuild-llm18-proxy Building 
 Image msjarvis-rebuild-llm8-proxy Building 
 Image msjarvis-rebuild-llm10-proxy Building 
 Image msjarvis-rebuild-jarvis-lm-synthesizer Building 
 Image msjarvis-rebuild-jarvis-judge-consistency Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-23 Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-12 Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-02 Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-04 Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-01 Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-21 Building 
 Image msjarvis-rebuild-jarvis-judge-pipeline Building 
 Image msjarvis-rebuild-jarvis-unified-gateway Building 
 Image msjarvis-rebuild-jarvis-aaacpe-rag Building 
 Image msjarvis-rebuild-jarvis-temporal-consciousness Building 
 Image msjarvis-rebuild-jarvis-constitutional-guardian Building 
 Image msjarvis-rebuild-jarvis-rag-server Building 
 Image msjarvis-rebuild-nbb_mother_carrie_protocols Building 
 Image msjarvis-rebuild-jarvis-20llm-production Building 
 Image msjarvis-rebuild-llm19-proxy Building 
 Image msjarvis-rebuild-llm12-proxy Building 
 Image msjarvis-rebuild-nbb_qualia_engine Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-19 Building 
 Image msjarvis-rebuild-nbb_consciousness_containers Building 
 Image msjarvis-rebuild-jarvis-woah Building 
 Image msjarvis-rebuild-llm4-proxy Building 
 Image msjarvis-rebuild-jarvis-mother-protocols Building 
 Image msjarvis-rebuild-nbb-i-containers Building 
 Image msjarvis-rebuild-jarvis-fractal-consciousness Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-16 Building 
 Image msjarvis-rebuild-jarvis-eeg-beta Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-15 Building 
 Image msjarvis-rebuild-jarvis-69dgm-bridge Building 
 Image msjarvis-rebuild-nbb_spiritual_maternal_integration Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-17 Building 
 Image msjarvis-rebuild-llm21-proxy Building 
 Image msjarvis-rebuild-jarvis-semaphore Building 
 Image msjarvis-rebuild-llm13-proxy Building 
 Image msjarvis-rebuild-llm2-proxy Building 
 Image msjarvis-rebuild-llm9-proxy Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-09 Building 
 Image msjarvis-rebuild-jarvis-web-research Building 
 Image msjarvis-rebuild-llm11-proxy Building 
 Image msjarvis-rebuild-llm14-proxy Building 
 Image msjarvis-rebuild-nbb_heteroglobulin_transport Building 
 Image msjarvis-rebuild-nbb_prefrontal_cortex Building 
 Image msjarvis-rebuild-llm5-proxy Building 
 Image msjarvis-rebuild-jarvis-eeg-delta Building 
 Image msjarvis-rebuild-nbb_blood_brain_barrier Building 
 Image msjarvis-rebuild-jarvis-psychology-services Building 
 Image msjarvis-rebuild-jarvis-eeg-theta Building 
 Image msjarvis-rebuild-jarvis-blood-brain-barrier Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-03 Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-11 Building 
 Image msjarvis-rebuild-jarvis-swarm-intelligence Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-10 Building 
 Image msjarvis-rebuild-jarvis-neurobiological-master Building 
 Image msjarvis-rebuild-llm16-proxy Building 
 Image msjarvis-rebuild-jarvis-fifth-dgm Building 
 Image msjarvis-rebuild-llm3-proxy Building 
 Image msjarvis-toroidal:latest Building 
 Image msjarvis-rebuild-llm7-proxy Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-06 Building 
 Image msjarvis-rebuild-jarvis-i-containers Building 
 Image msjarvis-rebuild-llm17-proxy Building 
 Image msjarvis-rebuild-jarvis-qualia-engine Building 
 Image msjarvis-rebuild-jarvis-hippocampus Building 
 Image msjarvis-rebuild-jarvis-dgm-bridge-13 Building 
 Image msjarvis-rebuild-llm1-proxy Building 
#1 [internal] load local bake definitions
#1 reading from stdin 49.51kB done
#1 DONE 0.0s

#2 [llm19-proxy internal] load build definition from Dockerfile-llm19-proxy
#2 transferring dockerfile: 262B 0.0s done
#2 DONE 0.1s

#3 [llm7-proxy internal] load build definition from Dockerfile-llm7-proxy
#3 transferring dockerfile: 259B 0.0s done
#3 DONE 0.1s

#4 [jarvis-dgm-bridge-14 internal] load build definition from Dockerfile.bridge
#4 transferring dockerfile: 232B 0.0s done
#4 DONE 0.6s

#5 [jarvis-local-resources internal] load build definition from Dockerfile.local_resources
#5 transferring dockerfile: 336B done
#5 DONE 0.7s

#6 [jarvis-local-resources internal] load metadata for docker.io/library/python:3.11-slim
#6 ...

#7 [llm12-proxy internal] load build definition from Dockerfile-llm12-proxy
#7 transferring dockerfile: 262B 0.0s done
#7 DONE 0.9s

#8 [llm15-proxy internal] load build definition from Dockerfile-llm15-proxy
#8 transferring dockerfile: 262B 0.0s done
#8 DONE 1.0s

#9 [llm15-proxy internal] load metadata for docker.io/library/python:3.12-slim
#9 ...

#10 [llm10-proxy internal] load build definition from Dockerfile-llm10-proxy
#10 transferring dockerfile: 262B 0.0s done
#10 DONE 1.1s

#9 [llm10-proxy internal] load metadata for docker.io/library/python:3.12-slim
#9 ...

#11 [jarvis-semaphore internal] load build definition from Dockerfile.semaphore
#11 transferring dockerfile: 484B 0.0s done
#11 DONE 1.3s

#12 [llm17-proxy internal] load build definition from Dockerfile-llm17-proxy
#12 transferring dockerfile: 262B 0.0s done
#12 DONE 1.4s

#9 [llm17-proxy internal] load metadata for docker.io/library/python:3.12-slim
#9 ...

#13 [jarvis-qualia-engine internal] load build definition from Dockerfile.qualia
#13 transferring dockerfile: 1.25kB 0.0s done
#13 DONE 1.5s

#14 [psychological_rag_domain internal] load build definition from Dockerfile.psychological_rag
#14 transferring dockerfile: 267B 0.0s done
#14 DONE 1.5s

#15 [llm8-proxy internal] load build definition from Dockerfile-llm8-proxy
#15 transferring dockerfile: 259B 0.0s done
#15 DONE 1.5s

#16 [llm21-proxy internal] load build definition from Dockerfile-llm21-proxy
#16 transferring dockerfile: 262B 0.0s done
#16 DONE 1.5s

#17 [jarvis-blood-brain-barrier internal] load build definition from Dockerfile.bbb
#17 transferring dockerfile: 407B 0.0s done
#17 DONE 1.5s

#18 [jarvis-i-containers internal] load build definition from Dockerfile.icontainers_fastapi
#18 transferring dockerfile: 663B 0.0s done
#18 DONE 1.6s

#19 [nbb-i-containers internal] load build definition from Dockerfile.nbb_icontainers_fastapi
#19 transferring dockerfile: 672B done
#19 DONE 1.6s

#9 [llm21-proxy internal] load metadata for docker.io/library/python:3.12-slim
#9 ...

#20 [llm9-proxy internal] load build definition from Dockerfile-llm9-proxy
#20 transferring dockerfile: 259B 0.0s done
#20 DONE 1.6s

#21 [llm2-proxy internal] load build definition from Dockerfile-llm2-proxy
#21 transferring dockerfile: 259B 0.0s done
#21 DONE 1.6s

#22 [jarvis-spiritual-rag internal] load build definition from Dockerfile.spiritual_rag
#22 transferring dockerfile: 248B 0.0s done
#22 DONE 1.6s

#23 [llm22-proxy internal] load build definition from Dockerfile-llm22-proxy
#23 transferring dockerfile: 262B 0.0s done
#23 DONE 1.6s

#24 [nbb_spiritual_root internal] load build definition from Dockerfile
#24 transferring dockerfile: 617B done
#24 DONE 1.6s

#25 [jarvis-rag-server internal] load build definition from Dockerfile.rag_server
#25 transferring dockerfile: 335B 0.0s done
#25 DONE 1.7s

#26 [jarvis-mother-protocols internal] load build definition from Dockerfile.mother_protocols
#26 transferring dockerfile: 339B 0.0s done
#26 DONE 1.7s

#27 [nbb_qualia_engine internal] load build definition from Dockerfile
#27 transferring dockerfile: 233B done
#27 DONE 1.7s

#9 [llm22-proxy internal] load metadata for docker.io/library/python:3.12-slim
#9 ...

#28 [jarvis-consciousness-bridge internal] load build definition from Dockerfile.consciousness_bridge
#28 transferring dockerfile: 284B 0.0s done
#28 DONE 1.7s

#29 [jarvis-fifth-dgm internal] load build definition from Dockerfile.fifth_dgm_real
#29 transferring dockerfile: 717B 0.0s done
#29 DONE 1.7s

#30 [jarvis-eeg-beta internal] load build definition from Dockerfile.eeg
#30 transferring dockerfile: 530B 0.0s done
#30 DONE 1.7s

#31 [llm6-proxy internal] load build definition from Dockerfile-llm6-proxy
#31 transferring dockerfile: 259B 0.0s done
#31 DONE 1.7s

#32 [jarvis-judge-truth internal] load build definition from Dockerfile.judge
#32 transferring dockerfile: 407B 0.0s done
#32 DONE 1.8s

#33 [jarvis-web-research internal] load build definition from Dockerfile.web_research
#33 transferring dockerfile: 474B 0.0s done
#33 DONE 1.8s

#34 [llm18-proxy internal] load build definition from Dockerfile-llm18-proxy
#34 transferring dockerfile: 262B 0.0s done
#34 DONE 1.8s

#35 [llm11-proxy internal] load build definition from Dockerfile-llm11-proxy
#35 transferring dockerfile: 262B 0.0s done
#35 DONE 1.8s

#9 [llm6-proxy internal] load metadata for docker.io/library/python:3.12-slim
#9 ...

#36 [jarvis-brain-orchestrator internal] load build definition from Dockerfile.brain
#36 transferring dockerfile: 614B done
#36 DONE 1.8s

#37 [jarvis-swarm-intelligence internal] load build definition from Dockerfile.swarm
#37 transferring dockerfile: 292B done
#37 DONE 1.8s

#38 [jarvis-wv-entangled-gateway internal] load build definition from Dockerfile
#38 transferring dockerfile: 590B done
#38 DONE 1.8s

#39 [llm16-proxy internal] load build definition from Dockerfile-llm16-proxy
#39 transferring dockerfile: 262B 0.0s done
#39 DONE 1.8s

#40 [jarvis-fractal-consciousness internal] load build definition from Dockerfile
#40 transferring dockerfile: 549B 0.0s done
#40 DONE 1.9s

#41 [llm13-proxy internal] load build definition from Dockerfile-llm13-proxy
#41 transferring dockerfile: 262B 0.0s done
#41 DONE 1.9s

#42 [llm20-proxy internal] load build definition from Dockerfile-llm20-proxy
#42 transferring dockerfile: 262B 0.0s done
#42 DONE 1.9s

#43 [nbb_mother_carrie_protocols internal] load build definition from Dockerfile
#43 transferring dockerfile: 747B done
#43 DONE 1.9s

#9 [llm13-proxy internal] load metadata for docker.io/library/python:3.12-slim
#9 ...

#44 [llm5-proxy internal] load build definition from Dockerfile-llm5-proxy
#44 transferring dockerfile: 259B 0.0s done
#44 DONE 1.9s

#45 [jarvis-unified-gateway internal] load build definition from Dockerfile.gateway
#45 transferring dockerfile: 319B done
#45 DONE 1.9s

#46 [llm14-proxy internal] load build definition from Dockerfile-llm14-proxy
#46 transferring dockerfile: 262B 0.0s done
#46 DONE 1.9s

#47 [jarvis-hippocampus internal] load build definition from Dockerfile.hippocampus
#47 transferring dockerfile: 540B 0.0s done
#47 DONE 2.0s

#48 [jarvis-aaacpe-rag internal] load build definition from Dockerfile.aaacpe_rag
#48 transferring dockerfile: 409B 0.0s done
#48 DONE 2.0s

#9 [llm14-proxy internal] load metadata for docker.io/library/python:3.12-slim
#9 ...

#4 [jarvis-dgm-bridge-20 internal] load build definition from Dockerfile.bridge
#4 transferring dockerfile: 232B 0.0s done
#4 DONE 0.6s

#30 [jarvis-eeg-delta internal] load build definition from Dockerfile.eeg
#30 transferring dockerfile: 530B 0.0s done
#30 DONE 1.7s

#36 [jarvis-20llm-production internal] load build definition from Dockerfile.brain
#36 transferring dockerfile: 614B done
#36 DONE 1.8s

#49 [jarvis-blood-brain-barrier internal] load .dockerignore
#49 transferring context: 352B 0.0s done
#49 DONE 0.0s

#50 [jarvis-rag-server 1/5] FROM docker.io/library/python:3.11-slim@sha256:a3ab0b966bc4e91546a033e22093cb840908979487a9fc0e6e38295747e49ac0
#50 DONE 0.0s

#51 [jarvis-swarm-intelligence internal] load .dockerignore
#51 transferring context: 848B done
#51 DONE 0.1s

#52 [jarvis-rag-server internal] load build context
#52 DONE 0.0s

#9 [jarvis-dgm-bridge-07 internal] load metadata for docker.io/library/python:3.12-slim
#9 ...

#53 [nbb_darwin_godel_machines internal] load build definition from Dockerfile
#53 transferring dockerfile: 245B done
#53 DONE 0.1s

#9 [nbb_darwin_godel_machines internal] load metadata for docker.io/library/python:3.12-slim
#9 ...

#54 [nbb_consciousness_containers internal] load build definition from Dockerfile
#54 transferring dockerfile: 617B done
#54 DONE 0.3s

#55 [nbb_spiritual_maternal_integration internal] load build definition from Dockerfile
#55 transferring dockerfile: 747B done
#55 DONE 0.3s

#56 [nbb_woah_algorithms internal] load build definition from Dockerfile
#56 transferring dockerfile: 473B done
#56 DONE 0.3s

#57 [jarvis-gis-rag internal] load build definition from Dockerfile.gis_rag
#57 transferring dockerfile: 341B done
#57 DONE 0.4s

#58 [jarvis-constitutional-guardian internal] load build definition from Dockerfile.constitutional_guardian
#58 transferring dockerfile: 504B 0.0s done
#58 DONE 0.4s

#51 [jarvis-unified-gateway internal] load .dockerignore
#51 transferring context: 848B done
#51 DONE 0.1s

#59 [jarvis-unified-gateway internal] load metadata for docker.io/library/python:3.10
#59 DONE 0.5s

#9 [nbb_woah_algorithms internal] load metadata for docker.io/library/python:3.12-slim
#9 ...

#60 [llm1-proxy internal] load build definition from Dockerfile-llm1-proxy
#60 transferring dockerfile: 259B 0.0s done
#60 DONE 0.4s

#61 [nbb_subconscious internal] load build definition from Dockerfile
#61 transferring dockerfile: 617B done
#61 DONE 0.4s

#4 [jarvis-dgm-bridge-11 internal] load build definition from Dockerfile.bridge
#4 transferring dockerfile: 232B 0.0s done
#4 DONE 0.6s

#30 [jarvis-eeg-theta internal] load build definition from Dockerfile.eeg
#30 transferring dockerfile: 530B 0.0s done
#30 DONE 1.7s

#32 [jarvis-judge-consistency internal] load build definition from Dockerfile.judge
#32 transferring dockerfile: 407B 0.0s done
#32 DONE 1.8s

#49 [jarvis-dgm-bridge-20 internal] load .dockerignore
#49 transferring context: 352B 0.0s done
#49 DONE 0.1s

#50 [jarvis-judge-pipeline 1/5] FROM docker.io/library/python:3.11-slim@sha256:a3ab0b966bc4e91546a033e22093cb840908979487a9fc0e6e38295747e49ac0
#50 DONE 0.0s

#51 [nbb-i-containers internal] load .dockerignore
#51 transferring context: 848B done
#51 DONE 0.1s

#62 [jarvis-judge-pipeline internal] load build context
#62 transferring context: 2B 0.3s done
#62 DONE 0.4s

#52 [jarvis-rag-server internal] load build context
#52 transferring context: 2B 0.0s done
#52 DONE 0.4s

#63 [llm12-proxy internal] load build context
#63 DONE 0.0s

#64 [psychological_rag_domain internal] load build context
#64 DONE 0.0s

#65 [jarvis-judge-pipeline 4/5] COPY judge_*.py /app/
#65 CACHED

#66 [jarvis-judge-pipeline 3/5] RUN pip install --no-cache-dir     fastapi==0.115.0     uvicorn==0.30.0     httpx==0.27.0     redis==5.0.0     pydantic==2.8.0
#66 CACHED

#67 [jarvis-judge-pipeline 2/5] WORKDIR /app
#67 CACHED

#68 [jarvis-judge-pipeline 5/5] COPY lm_synthesizer.py /app/
#68 ERROR: failed to calculate checksum of ref 7b72fadc-02f8-4f9c-a29d-13a27a5c530e::k0s2i8j0wa9ts1wmfqqc2jo63: "/lm_synthesizer.py": not found

#9 [jarvis-dgm-bridge-13 internal] load metadata for docker.io/library/python:3.12-slim
#9 ...

#69 [jarvis-lm-synthesizer internal] load build definition from Dockerfile.lm_synthesizer
#69 transferring dockerfile: 433B 0.0s done
#69 DONE 0.3s

#70 [llm1-proxy internal] load build context
#70 DONE 0.0s

#71 [jarvis-rag-server 2/4] WORKDIR /app/services
#71 CACHED

#72 [jarvis-rag-server 3/4] RUN pip install --no-cache-dir fastapi uvicorn httpx pydantic chromadb sentence-transformers
#72 CACHED

#73 [jarvis-rag-server 4/4] COPY ms_jarvis_rag_server.py ms_jarvis_rag_server.py
#73 ERROR: failed to calculate checksum of ref 7b72fadc-02f8-4f9c-a29d-13a27a5c530e::d33j0ph1yyfd78es7x754uhpq: "/ms_jarvis_rag_server.py": not found

#66 [jarvis-judge-alignment 3/5] RUN pip install --no-cache-dir     fastapi==0.115.0     uvicorn==0.30.0     httpx==0.27.0     redis==5.0.0     pydantic==2.8.0
#66 CACHED

#65 [jarvis-judge-alignment 4/5] COPY judge_*.py /app/
#65 CACHED

#67 [jarvis-judge-alignment 2/5] WORKDIR /app
#67 CACHED

#68 [jarvis-judge-alignment 5/5] COPY lm_synthesizer.py /app/
#68 ERROR: failed to calculate checksum of ref 7b72fadc-02f8-4f9c-a29d-13a27a5c530e::k0s2i8j0wa9ts1wmfqqc2jo63: "/lm_synthesizer.py": not found

#74 [jarvis-hippocampus internal] load build context
#74 DONE 0.0s

#75 [jarvis-web-research internal] load build context
#75 DONE 0.0s

#76 [jarvis-swarm-intelligence internal] load build context
#76 DONE 0.0s

#77 [jarvis-i-containers internal] load build context
#77 DONE 0.0s

#78 [jarvis-semaphore internal] load build context
#78 DONE 0.0s

#79 [jarvis-fifth-dgm internal] load build context
#79 DONE 0.0s

#80 [jarvis-mother-protocols internal] load build context
#80 DONE 0.0s

#81 [llm16-proxy internal] load build context
#81 DONE 0.0s

#82 [llm6-proxy internal] load build context
#82 DONE 0.0s

#83 [jarvis-local-resources internal] load build context
#83 DONE 0.0s

#84 [jarvis-eeg-beta internal] load build context
#84 DONE 0.0s

#85 [llm14-proxy internal] load build context
#85 DONE 0.0s

#86 [llm17-proxy internal] load build context
#86 DONE 0.0s

#87 [llm21-proxy internal] load build context
#87 DONE 0.0s

#88 [llm10-proxy internal] load build context
#88 DONE 0.0s

#89 [llm2-proxy internal] load build context
#89 DONE 0.0s

#90 [llm8-proxy internal] load build context
#90 DONE 0.0s

#91 [llm18-proxy internal] load build context
#91 DONE 0.0s

#92 [llm11-proxy internal] load build context
#92 DONE 0.0s

#93 [llm15-proxy internal] load build context
#93 DONE 0.0s

#94 [jarvis-dgm-bridge-01 1/4] FROM docker.io/library/python:3.12-slim@sha256:090ba77e2958f6af52a5341f788b50b032dd4ca28377d2893dcf1ecbdfdfe203
#94 DONE 0.0s

#95 [llm5-proxy internal] load build context
#95 DONE 0.0s

#96 [llm20-proxy internal] load build context
#96 DONE 0.0s

#97 [nbb-i-containers internal] load build context
#97 DONE 0.0s

#98 [llm22-proxy internal] load build context
#98 DONE 0.0s

#99 [jarvis-unified-gateway internal] load build context
#99 DONE 0.0s

#100 [llm13-proxy internal] load build context
#100 DONE 0.0s

#101 [llm9-proxy internal] load build context
#101 DONE 0.0s

#102 [llm7-proxy internal] load build context
#102 DONE 0.0s

#103 [llm19-proxy internal] load build context
#103 DONE 0.0s

#9 [jarvis-dgm-bridge-11 internal] load metadata for docker.io/library/python:3.12-slim
#9 ...

#104 [nbb_darwin_godel_machines internal] load .dockerignore
#104 transferring context: 2B done
#104 DONE 0.2s

#105 [nbb_woah_algorithms internal] load .dockerignore
#105 transferring context: 2B done
#105 DONE 0.2s

#106 [nbb_blood_brain_barrier internal] load build definition from Dockerfile
#106 transferring dockerfile: 588B done
#106 DONE 0.3s

#107 [jarvis-dgm-bridge-01 internal] load build context
#107 ...

#108 [nbb_prefrontal_cortex internal] load build definition from Dockerfile
#108 transferring dockerfile: 860B done
#108 DONE 0.4s

#109 [jarvis-69dgm-bridge internal] load build definition from Dockerfile.69dgm_bridge
#109 transferring dockerfile: 367B 0.0s done
#109 DONE 0.5s

#110 [jarvis-neurobiological-master internal] load build definition from Dockerfile.neuro
#110 transferring dockerfile: 539B done
#110 DONE 0.5s

#111 [nbb_qualia_engine internal] load .dockerignore
#111 transferring context: 2B done
#111 DONE 0.6s

#6 [jarvis-judge-consistency internal] load metadata for docker.io/library/python:3.11-slim
#6 DONE 3.0s

#112 [jarvis-woah internal] load build definition from Dockerfile.woah
#112 transferring dockerfile: 386B done
#112 CANCELED

#113 [nbb_heteroglobulin_transport internal] load build definition from Dockerfile
#113 transferring dockerfile: 747B done
#113 CANCELED

#114 [llm3-proxy internal] load build definition from Dockerfile-llm3-proxy
#114 CANCELED

#115 [jarvis-agents-service internal] load build definition from Dockerfile.agents
#115 transferring dockerfile: 289B done
#115 CANCELED

#116 [llm4-proxy internal] load build definition from Dockerfile-llm4-proxy
#116 transferring dockerfile: 259B 0.0s done
#116 DONE 0.8s

#117 [jarvis-toroidal internal] load build definition from Dockerfile.toroidal
#117 transferring dockerfile: 659B 0.0s done
#117 CANCELED

#118 [jarvis-temporal-consciousness internal] load build definition from Dockerfile.temporal_consciousness
#118 CANCELED

#119 [nbb_pituitary_gland internal] load build definition from Dockerfile
#119 transferring dockerfile: 701B done
#119 CANCELED

#120 [jarvis-psychology-services internal] load build definition from Dockerfile.psychology_services
#120 transferring dockerfile: 320B 0.0s done
#120 DONE 0.8s

#121 [nbb_spiritual_maternal_integration internal] load .dockerignore
#121 transferring context: 2B done
#121 CANCELED

#122 [nbb_consciousness_containers internal] load .dockerignore
#122 transferring context: 2B done
#122 CANCELED

#49 [jarvis-judge-ethics internal] load .dockerignore
#49 transferring context: 352B 0.0s done
#49 DONE 0.1s

#51 [jarvis-gis-rag internal] load .dockerignore
#51 transferring context: 848B done
#51 DONE 0.2s

#123 [nbb_subconscious internal] load metadata for docker.io/tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
#123 DONE 1.8s

#124 [jarvis-brain-orchestrator internal] load metadata for docker.io/library/python:3.10-slim
#124 DONE 2.7s

#9 [jarvis-dgm-bridge-02 internal] load metadata for docker.io/library/python:3.12-slim
#9 DONE 3.3s

#125 [nbb_mother_carrie_protocols internal] load .dockerignore
#125 transferring context: 2B done
#125 CANCELED

#126 [nbb_spiritual_root internal] load .dockerignore
#126 transferring context: 2B done
#126 CANCELED

#107 [jarvis-dgm-bridge-12 internal] load build context
#107 ERROR: rpc error: code = Canceled desc = rpc error: code = Canceled desc = grpc: the client connection is closing

#78 [jarvis-semaphore internal] load build context
#78 ERROR: rpc error: code = Canceled desc = rpc error: code = Canceled desc = grpc: the client connection is closing

#74 [jarvis-hippocampus internal] load build context
#74 CANCELED

#127 [jarvis-unified-gateway 1/5] FROM docker.io/library/python:3.10@sha256:b6c2f85994c8d67e2d459a804ab80584471a23a438f9148763b92adecaaf687a
#127 DONE 0.0s

#76 [jarvis-swarm-intelligence internal] load build context
#76 CANCELED

#75 [jarvis-fractal-consciousness internal] load build context
#75 CANCELED

#77 [jarvis-i-containers internal] load build context
#77 CANCELED

#63 [llm12-proxy internal] load build context
#63 CANCELED

#80 [jarvis-mother-protocols internal] load build context
#80 CANCELED

#79 [jarvis-fifth-dgm internal] load build context
#79 CANCELED

#64 [psychological_rag_domain internal] load build context
#64 CANCELED
------
 > [jarvis-judge-alignment 5/5] COPY lm_synthesizer.py /app/:
------
------
 > [jarvis-rag-server 4/4] COPY ms_jarvis_rag_server.py ms_jarvis_rag_server.py:
------
------
 > [jarvis-dgm-bridge-10 internal] load build context:
------
------
 > [jarvis-semaphore internal] load build context:
------
Dockerfile.judge:15

--------------------

  13 |     # Copy judge files

  14 |     COPY judge_*.py /app/

  15 | >>> COPY lm_synthesizer.py /app/

  16 |     

  17 |     # Default command (will be overridden in docker-compose)

--------------------

target jarvis-judge-pipeline: failed to solve: failed to compute cache key: failed to calculate checksum of ref 7b72fadc-02f8-4f9c-a29d-13a27a5c530e::k0s2i8j0wa9ts1wmfqqc2jo63: "/lm_synthesizer.py": not found

 Container llm2-proxy Creating 
 Container jarvis-judge-truth Creating 
 Container llm5-proxy Creating 
 Container msjarvis-rebuild-nbb_heteroglobulin_transport-1 Creating 
 Container jarvis-69dgm-bridge Creating 
 Container msjarvis-rebuild-nbb_qualia_engine-1 Creating 
 Container llm20-proxy Creating 
 Container jarvis-chroma Creating 
 Container jarvis-web-research Creating 
 Container jarvis-redis Creating 
 Container jarvis-judge-ethics Creating 
 Container llm4-proxy Creating 
 Container llm8-proxy Creating 
 Container llm11-proxy Creating 
 Container msjarvis-rebuild-nbb_spiritual_root-1 Creating 
 Container llm17-proxy Creating 
 Container jarvis-judge-alignment Creating 
 Container llm10-proxy Creating 
 Container llm13-proxy Creating 
 Container llm18-proxy Creating 
 Container llm19-proxy Creating 
 Container llm3-proxy Creating 
 Container msjarvis-rebuild-nbb_prefrontal_cortex-1 Creating 
 Container llm15-proxy Creating 
 Container llm21-proxy Creating 
 Container jarvis-i-containers Creating 
 Container msjarvis-rebuild-nbb_darwin_godel_machines-1 Creating 
 Container llm9-proxy Creating 
 Container llm22-proxy Creating 
 Container msjarvis-rebuild-nbb_consciousness_containers-1 Creating 
 Container psychological_rag_domain Creating 
 Container jarvis-temporal-consciousness Creating 
 Container msjarvis-rebuild-nbb_woah_algorithms-1 Creating 
 Container jarvis-judge-consistency Creating 
 Container msjarvis-rebuild-nbb_mother_carrie_protocols-1 Creating 
 Container llm14-proxy Creating 
 Container jarvis-local-resources-db Creating 
 Container msjarvis-rebuild-nbb_blood_brain_barrier-1 Creating 
 Container jarvis-fifth-dgm Creating 
 Container jarvis-swarm-intelligence Creating 
 Container llm7-proxy Creating 
 Container msjarvis-rebuild-nbb_pituitary_gland-1 Creating 
 Container jarvis-ollama Creating 
 Container llm12-proxy Creating 
 Container llm6-proxy Creating 
 Container msjarvis-rebuild-nbb_subconscious-1 Creating 
 Container jarvis-agents-service Creating 
 Container mysql Creating 
 Container jarvis-semaphore Creating 
 Container jarvis-lm-synthesizer Creating 
 Container llm16-proxy Creating 
 Container nbb-i-containers Creating 
 Container llm1-proxy Creating 
 Container neo4j Creating 
 Container ipfs Creating 
 Container msjarvis-rebuild-nbb_spiritual_maternal_integration-1 Creating 
 Container jarvis-mother-protocols Creating 
 Container jarvis-judge-truth Created 
 Container jarvis-judge-consistency Created 
 Container msjarvis-rebuild-nbb_consciousness_containers-1 Created 
 Container llm22-proxy Created 
 Container llm2-proxy Created 
 Container msjarvis-rebuild-nbb_qualia_engine-1 Created 
 Container jarvis-temporal-consciousness Created 
 Container ipfs Created 
 Container llm21-proxy Created 
 Container jarvis-lm-synthesizer Created 
 Container mysql Created 
 Container jarvis-i-containers Created 
 Container llm8-proxy Created 
 Container jarvis-swarm-intelligence Created 
 Container jarvis-semaphore Created 
 Container llm7-proxy Created 
 Container llm14-proxy Created 
 Container llm10-proxy Created 
 Container llm20-proxy Created 
 Container jarvis-judge-ethics Created 
 Container llm11-proxy Created 
 Container llm17-proxy Created 
 Container llm3-proxy Created 
 Container llm16-proxy Created 
 Container jarvis-judge-alignment Created 
 Container jarvis-local-resources-db Created 
 Container jarvis-judge-pipeline Creating 
 Container jarvis-local-resources Creating 
 Container jarvis-chroma Created 
 Container msjarvis-rebuild-nbb_spiritual_maternal_integration-1 Created 
 Container jarvis-autonomous-learner Creating 
 Container jarvis-spiritual-rag Creating 
 Container jarvis-hippocampus Creating 
 Container jarvis-rag-server Creating 
 Container llm19-proxy Created 
 Container jarvis-aaacpe-rag Creating 
 Container jarvis-gis-rag Creating 
 Container llm4-proxy Created 
 Container msjarvis-rebuild-nbb_darwin_godel_machines-1 Created 
 Container llm1-proxy Created 
 Container jarvis-mother-protocols Created 
 Container jarvis-agents-service Created 
 Container llm9-proxy Created 
 Container llm13-proxy Created 
 Container msjarvis-rebuild-nbb_blood_brain_barrier-1 Created 
 Container msjarvis-rebuild-nbb_heteroglobulin_transport-1 Created 
 Container nbb-i-containers Created 
 Container psychological_rag_domain Created 
 Container msjarvis-rebuild-nbb_subconscious-1 Created 
 Container jarvis-psychology-services Creating 
 Container msjarvis-rebuild-nbb_spiritual_root-1 Created 
 Container jarvis-69dgm-bridge Created 
 Container msjarvis-rebuild-nbb_prefrontal_cortex-1 Created 
 Container llm12-proxy Created 
 Container msjarvis-rebuild-nbb_mother_carrie_protocols-1 Created 
 Container jarvis-redis Created 
 Container llm18-proxy Created 
 Container llm6-proxy Created 
 Container jarvis-eeg-beta Creating 
 Container jarvis-eeg-delta Creating 
 Container msjarvis-rebuild-nbb_woah_algorithms-1 Created 
 Container jarvis-eeg-theta Creating 
 Container llm15-proxy Created 
 Container jarvis-ollama Created 
 Container jarvis-main-brain Creating 
 Container jarvis-fractal-consciousness Creating 
 Container jarvis-woah Creating 
 Container jarvis-20llm-production Creating 
 Container jarvis-qualia-engine Creating 
 Container jarvis-blood-brain-barrier Creating 
 Container llm5-proxy Created 
 Container jarvis-fifth-dgm Created 
 Container jarvis-web-research Created 
 Container msjarvis-rebuild-nbb_pituitary_gland-1 Created 
 Container neo4j Created 
 Container jarvis-local-resources Created 
 Container jarvis-judge-pipeline Created 
 Container jarvis-psychology-services Created 
 Container jarvis-20llm-production Created 
 Container jarvis-wv-entangled-gateway Creating 
 Container jarvis-aaacpe-rag Created 
 Container jarvis-autonomous-learner Created 
 Container jarvis-spiritual-rag Created 
 Container jarvis-gis-rag Created 
 Container jarvis-rag-server Created 
 Container jarvis-woah Created 
 Container jarvis-consciousness-bridge Creating 
 Container jarvis-main-brain Created 
 Container jarvis-brain-orchestrator Creating 
 Container jarvis-fractal-consciousness Created 
 Container jarvis-dgm-bridge-20 Creating 
 Container jarvis-dgm-bridge-21 Creating 
 Container jarvis-dgm-bridge-11 Creating 
 Container jarvis-dgm-bridge-18 Creating 
 Container jarvis-dgm-bridge-16 Creating 
 Container jarvis-dgm-bridge-08 Creating 
 Container jarvis-dgm-bridge-10 Creating 
 Container jarvis-dgm-bridge-07 Creating 
 Container jarvis-dgm-bridge-19 Creating 
 Container jarvis-dgm-bridge-13 Creating 
 Container jarvis-dgm-bridge-09 Creating 
 Container jarvis-dgm-bridge-05 Creating 
 Container jarvis-dgm-bridge-22 Creating 
 Container jarvis-dgm-bridge-03 Creating 
 Container jarvis-dgm-bridge-14 Creating 
 Container jarvis-dgm-bridge-17 Creating 
 Container jarvis-dgm-bridge-02 Creating 
 Container jarvis-dgm-bridge-23 Creating 
 Container jarvis-dgm-bridge-12 Creating 
 Container jarvis-dgm-bridge-06 Creating 
 Container jarvis-dgm-bridge-01 Creating 
 Container jarvis-dgm-bridge-04 Creating 
 Container jarvis-dgm-bridge-15 Creating 
 Container jarvis-eeg-beta Created 
 Container jarvis-eeg-theta Created 
 Container jarvis-blood-brain-barrier Created 
 Container jarvis-hippocampus Created 
 Container jarvis-constitutional-guardian Creating 
 Container jarvis-eeg-delta Created 
 Container jarvis-qualia-engine Created 
 Container jarvis-neurobiological-master Creating 
 Container jarvis-consciousness-bridge Created 
 Container jarvis-toroidal Creating 
 Container jarvis-dgm-bridge-13 Created 
 Container jarvis-dgm-bridge-14 Created 
 Container jarvis-dgm-bridge-20 Created 
 Container jarvis-neurobiological-master Created 
 Container jarvis-brain-orchestrator Created 
 Container jarvis-dgm-bridge-11 Created 
 Container jarvis-dgm-bridge-18 Created 
 Container jarvis-wv-entangled-gateway Created 
 Container jarvis-dgm-bridge-07 Created 
 Container jarvis-dgm-bridge-02 Created 
 Container jarvis-dgm-bridge-06 Created 
 Container jarvis-dgm-bridge-15 Created 
 Container jarvis-dgm-bridge-12 Created 
 Container jarvis-dgm-bridge-10 Created 
 Container jarvis-dgm-bridge-03 Created 
 Container jarvis-dgm-bridge-23 Created 
 Container jarvis-dgm-bridge-16 Created 
 Container jarvis-dgm-bridge-17 Created 
 Container jarvis-dgm-bridge-09 Created 
 Container jarvis-dgm-bridge-05 Created 
 Container jarvis-dgm-bridge-08 Created 
 Container jarvis-dgm-bridge-19 Created 
 Container jarvis-constitutional-guardian Created 
 Container jarvis-dgm-bridge-01 Created 
 Container jarvis-dgm-bridge-04 Created 
 Container jarvis-dgm-bridge-22 Created 
 Container jarvis-dgm-bridge-21 Created 
 Container jarvis-toroidal Created 
 Container jarvis-unified-gateway Creating 
 Container jarvis-unified-gateway Created 
 Container llm8-proxy Starting 
 Container jarvis-judge-truth Starting 
 Container mysql Starting 
 Container neo4j Starting 
 Container msjarvis-rebuild-nbb_spiritual_root-1 Starting 
 Container nbb-i-containers Starting 
 Container jarvis-69dgm-bridge Starting 
 Container jarvis-web-research Starting 
 Container llm15-proxy Starting 
 Container llm7-proxy Starting 
 Container jarvis-i-containers Starting 
 Container msjarvis-rebuild-nbb_pituitary_gland-1 Starting 
 Container llm10-proxy Starting 
 Container msjarvis-rebuild-nbb_subconscious-1 Starting 
 Container msjarvis-rebuild-nbb_woah_algorithms-1 Starting 
 Container jarvis-redis Starting 
 Container llm21-proxy Starting 
 Container jarvis-judge-ethics Starting 
 Container jarvis-swarm-intelligence Starting 
 Container jarvis-judge-consistency Starting 
 Container llm2-proxy Starting 
 Container jarvis-local-resources-db Starting 
 Container msjarvis-rebuild-nbb_heteroglobulin_transport-1 Starting 
 Container llm1-proxy Starting 
 Container llm3-proxy Starting 
 Container llm13-proxy Starting 
 Container llm18-proxy Starting 
 Container llm4-proxy Starting 
 Container llm9-proxy Starting 
 Container llm12-proxy Starting 
 Container msjarvis-rebuild-nbb_qualia_engine-1 Starting 
 Container jarvis-fifth-dgm Starting 
 Container llm19-proxy Starting 
 Container llm6-proxy Starting 
 Container ipfs Starting 
 Container jarvis-temporal-consciousness Starting 
 Container msjarvis-rebuild-nbb_consciousness_containers-1 Starting 
 Container jarvis-mother-protocols Starting 
 Container llm22-proxy Starting 
 Container jarvis-ollama Starting 
 Container llm14-proxy Starting 
 Container msjarvis-rebuild-nbb_spiritual_maternal_integration-1 Starting 
 Container llm17-proxy Starting 
 Container jarvis-chroma Starting 
 Container msjarvis-rebuild-nbb_darwin_godel_machines-1 Starting 
 Container msjarvis-rebuild-nbb_prefrontal_cortex-1 Starting 
 Container llm11-proxy Starting 
 Container psychological_rag_domain Starting 
 Container jarvis-judge-alignment Starting 
 Container jarvis-lm-synthesizer Starting 
 Container llm20-proxy Starting 
 Container llm16-proxy Starting 
 Container jarvis-agents-service Starting 
 Container msjarvis-rebuild-nbb_blood_brain_barrier-1 Starting 
 Container msjarvis-rebuild-nbb_mother_carrie_protocols-1 Starting 
 Container jarvis-semaphore Starting 
 Container llm5-proxy Starting 
 Container msjarvis-rebuild-nbb_spiritual_root-1 Started 
 Container msjarvis-rebuild-nbb_spiritual_maternal_integration-1 Started 
 Container mysql Started 
 Container jarvis-lm-synthesizer Started 
 Container llm21-proxy Started 
 Container neo4j Started 
 Container ipfs Started 
 Container jarvis-redis Started 
 Container jarvis-eeg-delta Starting 
 Container jarvis-eeg-theta Starting 
 Container jarvis-eeg-beta Starting 
 Container llm15-proxy Started 
 Container nbb-i-containers Started 
 Container llm7-proxy Started 
 Container llm17-proxy Started 
 Container llm13-proxy Started 
 Container jarvis-judge-ethics Started 
 Container msjarvis-rebuild-nbb_darwin_godel_machines-1 Started 
 Container msjarvis-rebuild-nbb_prefrontal_cortex-1 Started 
 Container llm22-proxy Started 
 Container llm8-proxy Started 
 Container msjarvis-rebuild-nbb_heteroglobulin_transport-1 Started 
 Container jarvis-temporal-consciousness Started 
 Container jarvis-judge-alignment Started 
 Container psychological_rag_domain Started 
 Container jarvis-psychology-services Starting 
 Container jarvis-judge-truth Started 
 Container jarvis-judge-consistency Started 
 Container jarvis-swarm-intelligence Started 
 Container jarvis-judge-pipeline Starting 
 Container llm1-proxy Started 
 Container msjarvis-rebuild-nbb_pituitary_gland-1 Started 
 Container llm14-proxy Started 
 Container jarvis-agents-service Started 
 Container msjarvis-rebuild-nbb_woah_algorithms-1 Started 
 Container llm11-proxy Started 
 Container llm6-proxy Started 
 Container llm18-proxy Started 
 Container llm5-proxy Started 
 Container jarvis-web-research Started 
 Container llm10-proxy Started 
 Container msjarvis-rebuild-nbb_mother_carrie_protocols-1 Started 
 Container llm2-proxy Started 
 Container jarvis-mother-protocols Started 
 Container llm3-proxy Started 
 Container jarvis-semaphore Started 
 Container msjarvis-rebuild-nbb_consciousness_containers-1 Started 
 Container jarvis-69dgm-bridge Started 
 Container jarvis-local-resources-db Started 
 Container jarvis-local-resources Starting 
 Container jarvis-chroma Started 
 Container jarvis-spiritual-rag Starting 
 Container jarvis-rag-server Starting 
 Container jarvis-aaacpe-rag Starting 
 Container jarvis-hippocampus Starting 
 Container jarvis-gis-rag Starting 
 Container jarvis-autonomous-learner Starting 
 Container jarvis-i-containers Started 
 Container msjarvis-rebuild-nbb_qualia_engine-1 Started 
 Container llm19-proxy Started 
 Container jarvis-fifth-dgm Started 
 Container msjarvis-rebuild-nbb_blood_brain_barrier-1 Started 
 Container msjarvis-rebuild-nbb_subconscious-1 Started 
 Container llm16-proxy Started 
 Container llm12-proxy Started 
 Container llm20-proxy Started 
 Container llm9-proxy Started 
 Container llm4-proxy Started 
 Container jarvis-eeg-delta Started 
 Container jarvis-eeg-theta Started 
 Container jarvis-eeg-beta Started 
 Container jarvis-gis-rag Started 
 Container jarvis-psychology-services Started 
 Container jarvis-judge-pipeline Started 
 Container jarvis-local-resources Started 
 Container jarvis-hippocampus Started 
 Container jarvis-autonomous-learner Started 
 Container jarvis-aaacpe-rag Started 
 Container jarvis-spiritual-rag Started 
 Container jarvis-rag-server Started 
 Container jarvis-ollama Started 
 Container jarvis-woah Starting 
 Container jarvis-fractal-consciousness Starting 
 Container jarvis-main-brain Starting 
 Container jarvis-qualia-engine Starting 
 Container jarvis-blood-brain-barrier Starting 
 Container jarvis-20llm-production Starting 
 Container jarvis-20llm-production Started 
 Container jarvis-wv-entangled-gateway Starting 
 Container jarvis-woah Started 
 Container jarvis-consciousness-bridge Starting 
 Container jarvis-blood-brain-barrier Started 
 Container jarvis-fractal-consciousness Started 
 Container jarvis-dgm-bridge-17 Starting 
 Container jarvis-dgm-bridge-11 Starting 
 Container jarvis-dgm-bridge-19 Starting 
 Container jarvis-dgm-bridge-21 Starting 
 Container jarvis-dgm-bridge-09 Starting 
 Container jarvis-dgm-bridge-01 Starting 
 Container jarvis-dgm-bridge-06 Starting 
 Container jarvis-dgm-bridge-04 Starting 
 Container jarvis-dgm-bridge-12 Starting 
 Container jarvis-dgm-bridge-23 Starting 
 Container jarvis-dgm-bridge-14 Starting 
 Container jarvis-dgm-bridge-13 Starting 
 Container jarvis-dgm-bridge-16 Starting 
 Container jarvis-dgm-bridge-10 Starting 
 Container jarvis-dgm-bridge-22 Starting 
 Container jarvis-dgm-bridge-08 Starting 
 Container jarvis-dgm-bridge-20 Starting 
 Container jarvis-dgm-bridge-02 Starting 
 Container jarvis-dgm-bridge-03 Starting 
 Container jarvis-dgm-bridge-05 Starting 
 Container jarvis-dgm-bridge-15 Starting 
 Container jarvis-dgm-bridge-18 Starting 
 Container jarvis-dgm-bridge-07 Starting 
 Container jarvis-main-brain Started 
 Container jarvis-constitutional-guardian Starting 
 Container jarvis-brain-orchestrator Starting 
 Container jarvis-qualia-engine Started 
 Container jarvis-neurobiological-master Starting 
 Container jarvis-consciousness-bridge Started 
 Container jarvis-toroidal Starting 
 Container jarvis-dgm-bridge-21 Started 
 Container jarvis-dgm-bridge-14 Started 
 Container jarvis-dgm-bridge-19 Started 
 Container jarvis-wv-entangled-gateway Started 
 Container jarvis-dgm-bridge-05 Started 
 Container jarvis-dgm-bridge-11 Started 
 Container jarvis-dgm-bridge-10 Started 
 Container jarvis-dgm-bridge-15 Started 
 Container jarvis-toroidal Started 
 Container jarvis-dgm-bridge-23 Started 
 Container jarvis-dgm-bridge-12 Started 
 Container jarvis-dgm-bridge-07 Started 
 Container jarvis-dgm-bridge-02 Started 
 Container jarvis-dgm-bridge-01 Started 
 Container jarvis-dgm-bridge-09 Started 
 Container jarvis-dgm-bridge-22 Started 
 Container jarvis-dgm-bridge-03 Started 
 Container jarvis-dgm-bridge-16 Started 
 Container jarvis-dgm-bridge-06 Started 
 Container jarvis-dgm-bridge-13 Started 
 Container jarvis-dgm-bridge-18 Started 
 Container jarvis-dgm-bridge-20 Started 
 Container jarvis-dgm-bridge-08 Started 
 Container jarvis-dgm-bridge-04 Started 
 Container jarvis-brain-orchestrator Started 
 Container jarvis-dgm-bridge-17 Started 
 Container jarvis-constitutional-guardian Started 
 Container jarvis-neurobiological-master Started 
 Container jarvis-unified-gateway Starting 
 Container jarvis-unified-gateway Started 
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

