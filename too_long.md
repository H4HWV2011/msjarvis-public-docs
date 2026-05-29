(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ cd /opt/msjarvis-rebuild
docker compose build --no-cache
docker compose up -d --force-recreate
[+] Building 1536.9s (474/510)                                                
 => [internal] load local bake definitions                               0.0s
 => => reading from stdin 52.33kB                                        0.0s
 => [llm3-proxy internal] load build definition from Dockerfile-llm3-pr  0.1s
 => => transferring dockerfile: 259B                                     0.0s
 => [nbb_qualia_engine internal] load build definition from Dockerfile   0.1s
 => => transferring dockerfile: 233B                                     0.0s
 => [jarvis-dgm-bridge-22 internal] load build definition from Dockerfi  0.2s
 => => transferring dockerfile: 232B                                     0.0s
 => [jarvis-eeg-beta internal] load build definition from Dockerfile.ee  0.3s
 => => transferring dockerfile: 530B                                     0.0s
 => [jarvis-gis-rag internal] load build definition from Dockerfile.gis  0.0s
 => => transferring dockerfile: 341B                                     0.0s
 => [nbb-i-containers internal] load build definition from Dockerfile.n  0.1s
 => => transferring dockerfile: 672B                                     0.0s
 => [jarvis-consciousness-bridge internal] load build definition from D  0.3s
 => => transferring dockerfile: 284B                                     0.0s
 => [jarvis-fifth-dgm internal] load build definition from Dockerfile.f  0.2s
 => => transferring dockerfile: 717B                                     0.0s
 => [jarvis-qualia-engine internal] load build definition from Dockerfi  0.2s
 => => transferring dockerfile: 1.25kB                                   0.0s
 => [jarvis-temporal-consciousness internal] load build definition from  0.3s
 => => transferring dockerfile: 387B                                     0.0s
 => [nbb_darwin_godel_machines internal] load build definition from Doc  0.1s
 => => transferring dockerfile: 245B                                     0.0s
 => [jarvis-aaacpe-rag internal] load build definition from Dockerfile.  0.1s
 => => transferring dockerfile: 409B                                     0.0s
 => [llm19-proxy internal] load build definition from Dockerfile-llm19-  0.3s
 => => transferring dockerfile: 262B                                     0.0s
 => [jarvis-auth-api internal] load build definition from Dockerfile.au  0.1s
 => => transferring dockerfile: 466B                                     0.0s
 => [jarvis-judge-consistency internal] load build definition from Dock  0.2s
 => => transferring dockerfile: 407B                                     0.0s
 => [jarvis-swarm-intelligence internal] load build definition from Doc  0.2s
 => => transferring dockerfile: 292B                                     0.0s
 => [llm11-proxy internal] load build definition from Dockerfile-llm11-  0.3s
 => => transferring dockerfile: 262B                                     0.0s
 => [jarvis-web-research internal] load build definition from Dockerfil  0.2s
 => => transferring dockerfile: 281B                                     0.0s
 => [jarvis-fractal-consciousness internal] load build definition from   0.3s
 => => transferring dockerfile: 549B                                     0.0s
 => [jarvis-agents-service internal] load build definition from Dockerf  0.1s
 => => transferring dockerfile: 289B                                     0.0s
 => [jarvis-spiritual-rag internal] load build definition from Dockerfi  0.1s
 => => transferring dockerfile: 248B                                     0.0s
 => [llm7-proxy internal] load build definition from Dockerfile-llm7-pr  0.1s
 => => transferring dockerfile: 259B                                     0.0s
 => [jarvis-rag-server internal] load build definition from Dockerfile.  0.3s
 => => transferring dockerfile: 335B                                     0.0s
 => [jarvis-69dgm-bridge internal] load build definition from Dockerfil  0.3s
 => => transferring dockerfile: 367B                                     0.0s
 => [nbb_heteroglobulin_transport internal] load build definition from   0.2s
 => => transferring dockerfile: 747B                                     0.0s
 => [nbb_spiritual_maternal_integration internal] load build definition  0.1s
 => => transferring dockerfile: 747B                                     0.0s
 => [jarvis-hippocampus internal] load build definition from Dockerfile  0.2s
 => => transferring dockerfile: 540B                                     0.0s
 => [llm10-proxy internal] load build definition from Dockerfile-llm10-  0.1s
 => => transferring dockerfile: 262B                                     0.0s
 => [nbb_pituitary_gland internal] load build definition from Dockerfil  0.2s
 => => transferring dockerfile: 701B                                     0.0s
 => [llm5-proxy internal] load build definition from Dockerfile-llm5-pr  0.3s
 => => transferring dockerfile: 259B                                     0.0s
 => [jarvis-i-containers internal] load build definition from Dockerfil  0.2s
 => => transferring dockerfile: 663B                                     0.0s
 => [jarvis-constitutional-guardian internal] load build definition fro  0.1s
 => => transferring dockerfile: 504B                                     0.0s
 => [jarvis-lm-synthesizer internal] load build definition from Dockerf  0.3s
 => => transferring dockerfile: 433B                                     0.0s
 => [jarvis-semaphore internal] load build definition from Dockerfile.s  0.2s
 => => transferring dockerfile: 484B                                     0.0s
 => [llm2-proxy internal] load build definition from Dockerfile-llm2-pr  0.1s
 => => transferring dockerfile: 259B                                     0.0s
 => [llm13-proxy internal] load build definition from Dockerfile-llm13-  0.3s
 => => transferring dockerfile: 262B                                     0.0s
 => [jarvis-toroidal internal] load build definition from Dockerfile.to  0.3s
 => => transferring dockerfile: 659B                                     0.0s
 => [llm4-proxy internal] load build definition from Dockerfile-llm4-pr  0.1s
 => => transferring dockerfile: 259B                                     0.0s
 => [nbb_spiritual_root internal] load build definition from Dockerfile  0.0s
 => => transferring dockerfile: 617B                                     0.0s
 => [jarvis-brain-orchestrator internal] load build definition from Doc  0.2s
 => => transferring dockerfile: 639B                                     0.0s
 => [llm16-proxy internal] load build definition from Dockerfile-llm16-  0.2s
 => => transferring dockerfile: 262B                                     0.0s
 => [llm14-proxy internal] load build definition from Dockerfile-llm14-  0.2s
 => => transferring dockerfile: 262B                                     0.0s
 => [jarvis-unified-gateway internal] load build definition from Docker  0.2s
 => => transferring dockerfile: 319B                                     0.0s
 => [jarvis-eeg-beta internal] load metadata for docker.io/library/pyth  0.9s
 => [nbb_prefrontal_cortex internal] load metadata for docker.io/tiango  1.0s
 => [jarvis-mother-protocols internal] load metadata for docker.io/libr  1.1s
 => [jarvis-main-brain internal] load metadata for docker.io/library/py  0.6s
 => [jarvis-unified-gateway internal] load metadata for docker.io/libra  0.4s
 => [jarvis-neurobiological-master internal] load .dockerignore          0.1s
 => => transferring context: 871B                                        0.0s
 => [jarvis-mother-protocols internal] load .dockerignore                0.2s
 => => transferring context: 69B                                         0.0s
 => [nbb_darwin_godel_machines internal] load .dockerignore              0.0s
 => => transferring context: 2B                                          0.0s
 => [nbb_qualia_engine internal] load .dockerignore                      0.0s
 => => transferring context: 2B                                          0.0s
 => [nbb_spiritual_root internal] load .dockerignore                     0.0s
 => => transferring context: 2B                                          0.0s
 => [nbb_pituitary_gland internal] load .dockerignore                    0.0s
 => => transferring context: 2B                                          0.0s
 => [nbb_heteroglobulin_transport internal] load .dockerignore           0.1s
 => => transferring context: 2B                                          0.0s
 => [nbb_spiritual_maternal_integration internal] load .dockerignore     0.1s
 => => transferring context: 2B                                          0.0s
 => [llm21-proxy internal] load build definition from Dockerfile-llm21-  0.1s
 => => transferring dockerfile: 262B                                     0.0s
 => [psychological_rag_domain internal] load build definition from Dock  0.1s
 => => transferring dockerfile: 267B                                     0.0s
 => [jarvis-blood-brain-barrier internal] load build definition from Do  0.1s
 => => transferring dockerfile: 407B                                     0.0s
 => [jarvis-woah internal] load build definition from Dockerfile.woah    0.0s
 => => transferring dockerfile: 386B                                     0.0s
 => [nbb_woah_algorithms internal] load build definition from Dockerfil  0.1s
 => => transferring dockerfile: 473B                                     0.0s
 => [llm8-proxy internal] load build definition from Dockerfile-llm8-pr  0.2s
 => => transferring dockerfile: 259B                                     0.0s
 => [jarvis-psychology-services internal] load build definition from Do  0.2s
 => => transferring dockerfile: 320B                                     0.0s
 => [nbb_blood_brain_barrier internal] load build definition from Docke  0.1s
 => => transferring dockerfile: 588B                                     0.0s
 => [llm17-proxy internal] load build definition from Dockerfile-llm17-  0.4s
 => => transferring dockerfile: 262B                                     0.0s
 => [llm6-proxy internal] load build definition from Dockerfile-llm6-pr  0.2s
 => => transferring dockerfile: 259B                                     0.0s
 => [llm9-proxy internal] load build definition from Dockerfile-llm9-pr  0.6s
 => => transferring dockerfile: 259B                                     0.0s
 => [llm15-proxy internal] load build definition from Dockerfile-llm15-  0.2s
 => => transferring dockerfile: 262B                                     0.0s
 => [nbb_subconscious internal] load build definition from Dockerfile    0.0s
 => => transferring dockerfile: 617B                                     0.0s
 => [jarvis-local-resources internal] load build definition from Docker  0.1s
 => => transferring dockerfile: 336B                                     0.0s
 => [jarvis-main-brain internal] load build definition from Dockerfile   0.1s
 => => transferring dockerfile: 590B                                     0.0s
 => [jarvis-semaphore internal] load build context                       5.1s
 => => transferring context: 88B                                         4.8s
 => [jarvis-toroidal internal] load build context                        0.1s
 => => transferring context: 3.83kB                                      0.0s
 => [jarvis-lm-synthesizer internal] load build context                  0.1s
 => => transferring context: 4.56kB                                      0.0s
 => [jarvis-eeg-beta internal] load build context                        0.5s
 => => transferring context: 22.44kB                                     0.0s
 => [jarvis-mother-protocols stage-0 1/5] FROM docker.io/library/python  0.0s
 => [jarvis-neurobiological-master 1/6] FROM docker.io/library/python:3  0.0s
 => [llm20-proxy internal] load build definition from Dockerfile-llm20-  1.4s
 => => transferring dockerfile: 262B                                     0.0s
 => [nbb_mother_carrie_protocols internal] load build definition from D  0.1s
 => => transferring dockerfile: 747B                                     0.0s
 => [llm12-proxy internal] load build definition from Dockerfile-llm12-  0.5s
 => => transferring dockerfile: 262B                                     0.0s
 => [llm18-proxy internal] load build definition from Dockerfile-llm18-  0.2s
 => => transferring dockerfile: 262B                                     0.0s
 => [jarvis-neurobiological-master internal] load build definition from  0.1s
 => => transferring dockerfile: 539B                                     0.0s
 => [llm1-proxy internal] load build definition from Dockerfile-llm1-pr  0.5s
 => => transferring dockerfile: 259B                                     0.0s
 => [nbb_consciousness_containers internal] load build definition from   0.3s
 => => transferring dockerfile: 617B                                     0.0s
 => [llm22-proxy internal] load build definition from Dockerfile-llm22-  0.1s
 => => transferring dockerfile: 262B                                     0.0s
 => [jarvis-dgm-bridge-10 internal] load build context                 683.5s
 => => transferring context: 30.57GB                                   682.3s
 => [jarvis-temporal-consciousness internal] load build context          0.2s
 => => transferring context: 712B                                        0.0s
 => [jarvis-judge-ethics internal] load build context                    1.2s
 => => transferring context: 122.26kB                                    0.4s
 => [jarvis-swarm-intelligence internal] load build context            308.1s
 => => transferring context: 5.67GB                                    307.6s
 => [jarvis-69dgm-bridge internal] load build context                    0.2s
 => => transferring context: 4.45kB                                      0.0s
 => [jarvis-auth-api internal] load build context                        8.6s
 => => transferring context: 619.53MB                                    8.5s
 => [jarvis-hippocampus internal] load build context                     0.2s
 => => transferring context: 7.44kB                                      0.0s
 => [jarvis-rag-server internal] load build context                      0.3s
 => => transferring context: 6.22kB                                      0.0s
 => [jarvis-wv-entangled-gateway internal] load build context          298.7s
 => => transferring context: 5.67GB                                    296.9s
 => [llm16-proxy internal] load build context                            0.3s
 => => transferring context: 1.65kB                                      0.0s
 => [llm14-proxy internal] load build context                            0.3s
 => => transferring context: 1.80kB                                      0.0s
 => [llm5-proxy internal] load build context                             0.2s
 => => transferring context: 1.80kB                                      0.0s
 => [jarvis-unified-gateway internal] load build context               312.3s
 => => transferring context: 5.67GB                                    311.6s
 => [llm13-proxy internal] load build context                            0.2s
 => => transferring context: 1.82kB                                      0.0s
 => [llm11-proxy internal] load build context                            0.3s
 => => transferring context: 1.61kB                                      0.0s
 => [jarvis-gis-rag internal] load build context                         0.3s
 => => transferring context: 14.52kB                                     0.1s
 => [llm10-proxy internal] load build context                            0.3s
 => => transferring context: 1.80kB                                      0.0s
 => CACHED [jarvis-mother-protocols stage-0 2/5] WORKDIR /app            0.1s
 => [jarvis-unified-gateway 1/5] FROM docker.io/library/python:3.10@sha  0.0s
 => CACHED [jarvis-blood-brain-barrier 2/4] WORKDIR /app/services        0.0s
 => CACHED [jarvis-neurobiological-master 2/6] WORKDIR /app              0.1s
 => CACHED [jarvis-dgm-bridge-12 2/5] WORKDIR /app/services              0.0s
 => CACHED [jarvis-unified-gateway 2/5] WORKDIR /app/services            0.0s
 => [jarvis-auth-api 3/5] RUN pip install --no-cache-dir     fastapi   708.6s
 => [jarvis-consciousness-bridge stage-0 3/5] COPY requirements.txt /ap  0.4s
 => [llm7-proxy internal] load build context                             0.6s
 => => transferring context: 1.64kB                                      0.0s
 => [jarvis-web-research internal] load build context                    0.8s
 => => transferring context: 30B                                         0.0s
 => [nbb_spiritual_maternal_integration internal] load build context     0.6s
 => => transferring context: 43.22kB                                     0.0s
 => [nbb_subconscious internal] load .dockerignore                       0.2s
 => => transferring context: 2B                                          0.0s
 => [jarvis-i-containers internal] load build context                    1.4s
 => => transferring context: 138.45kB                                    0.0s
 => [nbb_woah_algorithms internal] load .dockerignore                    1.0s
 => => transferring context: 2B                                          0.0s
 => [nbb_prefrontal_cortex 1/8] FROM docker.io/tiangolo/uvicorn-gunicor  0.0s
 => [nbb_heteroglobulin_transport internal] load build context           0.7s
 => => transferring context: 33.74kB                                     0.0s
 => [llm19-proxy internal] load build context                            1.0s
 => => transferring context: 1.80kB                                      0.0s
 => [jarvis-mother-protocols internal] load build definition from Docke  1.9s
 => => transferring dockerfile: 339B                                     0.0s
 => [nbb_blood_brain_barrier internal] load .dockerignore                1.2s
 => => transferring context: 2B                                          0.0s
 => [nbb_prefrontal_cortex internal] load build definition from Dockerf  0.5s
 => => transferring dockerfile: 860B                                     0.0s
 => [jarvis-fractal-consciousness internal] load build context           1.0s
 => => transferring context: 127.15kB                                    0.0s
 => [llm4-proxy internal] load build context                             1.8s
 => => transferring context: 1.64kB                                      0.0s
 => [nbb_pituitary_gland internal] load build context                    0.9s
 => => transferring context: 45.38kB                                     0.0s
 => [nbb_spiritual_root internal] load build context                     0.9s
 => => transferring context: 37.47kB                                     0.0s
 => [nbb_qualia_engine internal] load build context                      0.7s
 => => transferring context: 8.77kB                                      0.0s
 => [nbb_darwin_godel_machines internal] load build context              0.3s
 => => transferring context: 26.30kB                                     0.0s
 => [llm3-proxy internal] load build context                             1.0s
 => => transferring context: 1.82kB                                      0.0s
 => [llm2-proxy internal] load build context                             0.3s
 => => transferring context: 1.62kB                                      0.0s
 => [jarvis-fifth-dgm internal] load build context                       1.7s
 => => transferring context: 39.51kB                                     0.0s
 => [jarvis-fifth-dgm 3/9] RUN apt-get update && apt-get install -y -  708.7s
 => [jarvis-web-research 3/4] RUN pip install --no-cache-dir --root-u  707.3s
 => [jarvis-i-containers 3/6] RUN pip install --no-cache-dir fastapi   706.7s
 => [jarvis-judge-alignment 3/5] RUN pip install --no-cache-dir     f  708.3s
 => [jarvis-toroidal 3/6] RUN apt-get update && apt-get install -y --  706.5s
 => [jarvis-eeg-delta 3/8] RUN pip install --no-cache-dir     fastapi  707.3s
 => [jarvis-hippocampus 3/5] RUN apt-get update && apt-get install -y  708.0s
 => [llm11-proxy 3/4] COPY llm11_health_proxy.py .                       0.9s
 => [llm13-proxy 3/4] COPY llm13_health_proxy.py .                       0.9s
 => [jarvis-temporal-consciousness 3/5] COPY requirements_temporal.txt   0.9s
 => [llm14-proxy 3/4] COPY llm14_health_proxy.py .                       0.9s
 => [llm5-proxy 3/4] COPY llm5_health_proxy.py .                         0.9s
 => [llm10-proxy 3/4] COPY llm10_health_proxy.py .                       0.9s
 => [llm16-proxy 3/4] COPY llm16_health_proxy.py .                       0.9s
 => CACHED [nbb_prefrontal_cortex 2/8] WORKDIR /app                      0.1s
 => [jarvis-lm-synthesizer stage-0 4/5] RUN --mount=type=cache,targe  1533.9s
 => CACHED [jarvis-69dgm-bridge 3/6] COPY ../requirements.txt /app/requ  0.0s
 => CANCELED [jarvis-consciousness-bridge 4/6] RUN pip install --no-  1534.8s
 => => # Downloading tokenizers-0.22.2-cp39-abi3-manylinux_2_17_x86_64.manyli
 => => # nux2014_x86_64.whl (3.3 MB)                                         
 => => #    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 1.7 MB/s eta 
 => => # 0:00:00                                                             
 => => # Downloading torch-2.12.0-cp312-cp312-manylinux_2_28_x86_64.whl (532.
 => => # 3 MB)                                                               
 => [psychological_rag_domain internal] load build context               1.0s
 => => transferring context: 7.06kB                                      0.0s
 => [jarvis-rag-server 3/4] RUN pip install --no-cache-dir fastapi u  1533.9s
 => [jarvis-constitutional-guardian internal] load build context         1.0s
 => => transferring context: 15.11kB                                     0.0s
 => [jarvis-aaacpe-rag internal] load build context                      1.9s
 => => transferring context: 5.40kB                                      0.0s
 => [nbb_mother_carrie_protocols internal] load .dockerignore            1.9s
 => => transferring context: 2B                                          0.0s
 => [jarvis-spiritual-rag internal] load build context                   1.4s
 => => transferring context: 5.81kB                                      0.0s
 => [jarvis-local-resources internal] load build context                 1.0s
 => => transferring context: 3.52kB                                      0.1s
 => [jarvis-brain-orchestrator internal] load build context            319.8s
 => => transferring context: 5.67GB                                    317.8s
 => [jarvis-qualia-engine 1/5] FROM docker.io/library/python:3.10-slim@  0.5s
 => => resolve docker.io/library/python:3.10-slim@sha256:70f65c721aaddf  0.2s
 => [llm21-proxy internal] load build context                            1.0s
 => => transferring context: 1.82kB                                      0.0s
 => [jarvis-psychology-services internal] load build context             1.0s
 => => transferring context: 10.40kB                                     0.0s
 => [llm22-proxy internal] load build context                            1.0s
 => => transferring context: 2.13kB                                      0.0s
 => [llm8-proxy internal] load build context                             1.7s
 => => transferring context: 1.64kB                                      0.0s
 => [llm6-proxy internal] load build context                             1.8s
 => => transferring context: 1.63kB                                      0.0s
 => [llm15-proxy internal] load build context                            1.0s
 => => transferring context: 1.80kB                                      0.0s
 => [jarvis-neurobiological-master internal] load build context        318.6s
 => => transferring context: 5.67GB                                    317.4s
 => [jarvis-gis-rag 3/5] COPY services/gis_rag_service.py /app/gis_rag_  0.9s
 => [nbb_subconscious internal] load build context                       0.9s
 => => transferring context: 25.81kB                                     0.0s
 => [llm2-proxy 3/4] COPY llm2_health_proxy.py .                         0.8s
 => [nbb_darwin_godel_machines 3/4] COPY . /app                          1.1s
 => [nbb_spiritual_root 3/8] COPY . /app                                 1.2s
 => [llm11-proxy 4/4] RUN pip install fastapi uvicorn httpx            708.1s
 => [nbb_spiritual_maternal_integration 3/8] COPY . /app                 1.2s
 => [nbb_heteroglobulin_transport 3/8] COPY . /app                       1.2s
 => [llm7-proxy 3/4] COPY llm7_health_proxy.py .                         1.3s
 => [nbb_pituitary_gland 3/8] COPY . /app                                1.2s
 => [nbb_qualia_engine 3/4] COPY . /app                                  1.2s
 => [llm16-proxy 4/4] RUN pip install fastapi uvicorn httpx            706.9s
 => [jarvis-temporal-consciousness 4/5] RUN pip install --no-cache-di  705.7s
 => [llm10-proxy 4/4] RUN pip install fastapi uvicorn httpx            707.8s
 => [llm5-proxy 4/4] RUN pip install fastapi uvicorn httpx             706.0s
 => [llm14-proxy 4/4] RUN pip install fastapi uvicorn httpx            705.8s
 => [llm13-proxy 4/4] RUN pip install fastapi uvicorn httpx            707.0s
 => [llm3-proxy 3/4] COPY llm3_health_proxy.py .                         1.3s
 => [jarvis-gis-rag 4/5] COPY gis_service /app/gis_service               1.7s
 => CACHED [jarvis-brain-orchestrator 2/5] WORKDIR /app/services         0.2s
 => CACHED [jarvis-spiritual-rag 2/5] WORKDIR /app                       0.2s
 => [psychological_rag_domain 3/4] COPY psychological_rag_domain.py .    1.3s
 => [llm21-proxy 3/4] COPY llm21_health_proxy.py .                       1.3s
 => [jarvis-psychology-services 3/5] COPY psychology_integration_adapte  1.4s
 => [nbb_subconscious 3/8] COPY . /app                                   1.4s
 => [llm2-proxy 4/4] RUN pip install fastapi uvicorn httpx             706.3s
 => [llm19-proxy 3/4] COPY llm19_health_proxy.py .                       1.3s
 => [jarvis-local-resources 3/4] COPY services/local_resources_resolver  1.5s
 => [llm22-proxy 3/4] COPY llm22_health_proxy.py .                       1.3s
 => [llm15-proxy 3/4] COPY llm15_health_proxy.py .                       1.5s
 => [nbb_consciousness_containers internal] load .dockerignore           1.6s
 => => transferring context: 2B                                          0.0s
 => [nbb_woah_algorithms internal] load build context                    1.6s
 => => transferring context: 28.94kB                                     0.0s
 => [nbb_blood_brain_barrier internal] load build context                1.6s
 => => transferring context: 5.23kB                                      0.0s
 => [llm18-proxy internal] load build context                            1.6s
 => => transferring context: 1.82kB                                      0.0s
 => [llm17-proxy internal] load build context                            1.6s
 => => transferring context: 1.65kB                                      0.0s
 => [llm9-proxy internal] load build context                             1.6s
 => => transferring context: 1.66kB                                      0.0s
 => [llm12-proxy internal] load build context                            1.7s
 => => transferring context: 1.65kB                                      0.0s
 => [llm1-proxy internal] load build context                             1.7s
 => => transferring context: 1.64kB                                      0.0s
 => [jarvis-fractal-consciousness 3/7] COPY web_research_requirements.t  1.5s
 => [jarvis-20llm-production 3/5] RUN apt-get update && apt-get insta  706.6s
 => [jarvis-main-brain 3/7] RUN apt-get update && apt-get install -y   707.3s
 => [jarvis-woah 3/5] RUN apt-get update && apt-get install -y --no-i  707.9s
 => [jarvis-qualia-engine  3/12] RUN apt-get update && apt-get instal  707.7s
 => [jarvis-spiritual-rag 3/4] RUN pip install --no-cache-dir fastapi  705.6s
 => [jarvis-aaacpe-rag 3/5] RUN pip install --no-cache-dir     fastap  706.4s
 => [jarvis-constitutional-guardian 3/5] COPY requirements.txt /app/req  1.5s
 => [nbb_prefrontal_cortex internal] load .dockerignore                  1.9s
 => => transferring context: 2B                                          0.0s
 => [llm20-proxy internal] load build context                            1.9s
 => => transferring context: 1.62kB                                      0.0s
 => [llm8-proxy 3/4] COPY llm8_health_proxy.py .                         1.3s
 => [llm6-proxy 3/4] COPY llm6_health_proxy.py .                         1.2s
 => [llm4-proxy 3/4] COPY llm4_health_proxy.py .                         1.3s
 => [nbb_mother_carrie_protocols internal] load build context            1.5s
 => => transferring context: 40.70kB                                     0.0s
 => [jarvis-mother-protocols internal] load build context                2.0s
 => => transferring context: 934B                                        0.0s
 => [nbb_darwin_godel_machines 4/4] RUN pip install --no-cache-dir fa  705.5s
 => [nbb_spiritual_maternal_integration 4/8] RUN pip install --no-cac  707.5s
 => [nbb_pituitary_gland 4/8] COPY requirements.txt /tmp/requirements.t  1.1s
 => [nbb_spiritual_root 4/8] COPY requirements.txt /tmp/requirements.tx  1.2s
 => [nbb_heteroglobulin_transport 4/8] RUN pip install --no-cache-dir  705.6s
 => [nbb_qualia_engine 4/4] RUN pip install --no-cache-dir fastapi uv  707.1s
 => [llm7-proxy 4/4] RUN pip install fastapi uvicorn httpx             706.2s
 => [llm3-proxy 4/4] RUN pip install fastapi uvicorn httpx             706.9s
 => [psychological_rag_domain 4/4] RUN pip install --no-cache-dir fas  706.7s
 => [llm21-proxy 4/4] RUN pip install fastapi uvicorn httpx            705.2s
 => [llm22-proxy 4/4] RUN pip install fastapi uvicorn httpx            706.2s
 => [llm19-proxy 4/4] RUN pip install fastapi uvicorn httpx            707.4s
 => [nbb_subconscious 4/8] COPY requirements.txt /tmp/requirements.txt   1.1s
 => [jarvis-psychology-services 4/5] COPY psychology_server.py .         1.0s
 => [llm15-proxy 4/4] RUN pip install fastapi uvicorn httpx            704.6s
 => [jarvis-fractal-consciousness 4/7] RUN pip install --no-cache-dir  703.8s
 => [jarvis-local-resources 4/4] RUN pip install --no-cache-dir fasta  706.6s
 => [nbb_consciousness_containers internal] load build context           1.4s
 => => transferring context: 30.44kB                                     0.0s
 => [nbb_blood_brain_barrier 3/7] COPY . /app                            0.9s
 => [nbb_woah_algorithms 3/6] COPY . /app                                0.8s
 => CANCELED [jarvis-constitutional-guardian 4/5] RUN pip install --  1530.2s
 => [llm18-proxy 3/4] COPY llm18_health_proxy.py .                       0.9s
 => [llm9-proxy 3/4] COPY llm9_health_proxy.py .                         0.9s
 => [jarvis-gis-rag 5/5] RUN pip install --no-cache-dir fastapi uvico  706.6s
 => [llm17-proxy 3/4] COPY llm17_health_proxy.py .                       1.0s
 => [llm12-proxy 3/4] COPY llm12_health_proxy.py .                       0.9s
 => [llm1-proxy 3/4] COPY llm1_health_proxy.py .                         1.0s
 => [llm8-proxy 4/4] RUN pip install fastapi uvicorn httpx             703.7s
 => [llm6-proxy 4/4] RUN pip install fastapi uvicorn httpx             706.8s
 => [llm4-proxy 4/4] RUN pip install fastapi uvicorn httpx             704.3s
 => [nbb_prefrontal_cortex internal] load build context                  0.8s
 => => transferring context: 32.97kB                                     0.0s
 => [llm20-proxy 3/4] COPY llm20_health_proxy.py .                       0.6s
 => [nbb_mother_carrie_protocols 3/8] COPY . /app                        0.7s
 => [nbb_pituitary_gland 5/8] RUN pip install --no-cache-dir -r /tmp/  704.7s
 => [nbb_spiritual_root 5/8] RUN pip install --no-cache-dir -r /tmp/r  705.3s
 => [nbb_woah_algorithms 4/6] RUN pip install --no-cache-dir -r requi  706.1s
 => [jarvis-psychology-services 5/5] RUN pip install --no-cache-dir f  704.3s
 => [nbb_blood_brain_barrier 4/7] RUN pip install --no-cache-dir fast  705.2s
 => [llm9-proxy 4/4] RUN pip install fastapi uvicorn httpx             704.5s
 => [llm18-proxy 4/4] RUN pip install fastapi uvicorn httpx            703.3s
 => [llm12-proxy 4/4] RUN pip install fastapi uvicorn httpx            703.4s
 => [nbb_subconscious 5/8] RUN pip install --no-cache-dir -r /tmp/req  705.7s
 => [llm17-proxy 4/4] RUN pip install fastapi uvicorn httpx            704.6s
 => [llm1-proxy 4/4] RUN pip install fastapi uvicorn httpx             704.0s
 => [llm20-proxy 4/4] RUN pip install fastapi uvicorn httpx            704.6s
 => [nbb_consciousness_containers 3/8] COPY . /app                       0.4s
 => [nbb_prefrontal_cortex 3/8] COPY . /app                              0.2s
 => [nbb_mother_carrie_protocols 4/8] RUN pip install --no-cache-dir   702.4s
 => [nbb_prefrontal_cortex 4/8] RUN pip install --no-cache-dir flask   703.1s
 => [nbb_consciousness_containers 4/8] COPY requirements.txt /tmp/requi  0.5s
 => [nbb_consciousness_containers 5/8] RUN pip install --no-cache-dir  702.1s
 => [nbb-i-containers 3/6] COPY neurobiological_brain/ /app/neurobiol  411.1s
 => [jarvis-swarm-intelligence 3/5] COPY services/requirements.txt /a  402.2s
 => [jarvis-unified-gateway 3/5] COPY services /app/services           397.4s
 => [jarvis-dgm-bridge-21 3/5] COPY requirements.txt .                  23.7s
 => [jarvis-blood-brain-barrier 3/6] COPY bbb_requirements.txt /app/bb  25.9s
 => ERROR [jarvis-dgm-bridge-21 4/5] RUN pip install --no-cache-dir -  819.7s
 => [jarvis-fractal-consciousness 5/7] COPY neurobiological_brain/ /app  9.0s
 => [jarvis-semaphore 4/6] COPY requirements_semaphore.txt /app/require  8.9s
 => [jarvis-toroidal 4/7] COPY requirements_toroidal.txt /app/requireme  8.8s
 => [nbb_mother_carrie_protocols 5/8] RUN pip install --no-cache-dir   111.1s
 => [jarvis-i-containers 4/6] COPY ms_jarvis_i_containers_service.py /a  9.2s
 => [llm8-proxy] exporting to image                                     14.4s
 => => exporting layers                                                 10.7s
 => => writing image sha256:f30155791a93abf3f6671ca048bf120fd6a38d9f9cb  1.1s
 => => naming to docker.io/library/msjarvis-rebuild-llm8-proxy           0.1s
 => [jarvis-spiritual-rag 4/4] COPY spiritual_rag_domain.py /app/        9.4s
 => [jarvis-temporal-consciousness 5/5] COPY temporal_consciousness.py   9.5s
 => [llm14-proxy] exporting to image                                    16.6s
 => => exporting layers                                                 10.7s
 => => writing image sha256:c35110b85e86eced19b16c96508119b831250bac734  3.5s
 => => naming to docker.io/library/msjarvis-rebuild-llm14-proxy          0.1s
 => [llm18-proxy] exporting to image                                    21.4s
 => => exporting layers                                                 11.0s
 => => writing image sha256:c680955dba9e0cb44f62938d387d5c7c0c31a9b3ddc  8.5s
 => => naming to docker.io/library/msjarvis-rebuild-llm18-proxy          0.1s
 => [nbb_consciousness_containers 6/8] RUN pip install --no-cache-dir   20.8s
 => [llm12-proxy] exporting to image                                    33.7s
 => => exporting layers                                                 12.1s
 => => writing image sha256:026e454a5d0bd5c5ab977a12fa18a0713a699de859  19.2s
 => => naming to docker.io/library/msjarvis-rebuild-llm12-proxy          0.1s
 => [llm5-proxy] exporting to image                                     38.2s
 => => exporting layers                                                 12.4s
 => => writing image sha256:d89811c144a1fe102cf8cb24607a36e17efcca7cc8  19.8s
 => => naming to docker.io/library/msjarvis-rebuild-llm5-proxy           0.4s
 => [jarvis-eeg-beta 4/8] COPY eeg_shared/ /app/eeg_shared/              9.1s
 => [llm15-proxy] exporting to image                                    31.5s
 => => exporting layers                                                 11.7s
 => => writing image sha256:7d79e2070a9afb5ec1fb2f004ea7ad24c8875ae0de  16.9s
 => => naming to docker.io/library/msjarvis-rebuild-llm15-proxy          0.4s
 => [jarvis-web-research 4/4] COPY services/ /app/services/              9.1s
 => [llm2-proxy] exporting to image                                     40.2s
 => => exporting layers                                                 12.5s
 => => writing image sha256:c2e53d25e2c2c7bab972252e20dcf8e94eb5ec77c1  18.1s
 => => naming to docker.io/library/msjarvis-rebuild-llm2-proxy           0.5s
 => [nbb_prefrontal_cortex 5/8] RUN pip install --no-cache-dir redis   110.6s
 => [llm4-proxy] exporting to image                                     44.4s
 => => exporting layers                                                 14.2s
 => => writing image sha256:72aeb39bc439b2e2dd84eda647da3e1e58b6d0e9cd  17.6s
 => => naming to docker.io/library/msjarvis-rebuild-llm4-proxy           0.8s
 => [jarvis-aaacpe-rag 4/5] RUN mkdir -p /data/aaacpe_chroma             8.9s
 => [llm21-proxy] exporting to image                                    43.0s
 => => exporting layers                                                 12.8s
 => => writing image sha256:d5d4c14b25764fa37f3da0ab26491037af285a1047  18.0s
 => => naming to docker.io/library/msjarvis-rebuild-llm21-proxy          0.6s
 => [nbb_darwin_godel_machines] exporting to image                      43.8s
 => => exporting layers                                                 13.7s
 => => writing image sha256:1fe8f54cc241a6469775b3b9bee8ff5826b24064c4  17.6s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_darwin_godel_ma  0.7s
 => [jarvis-brain-orchestrator 4/5] COPY services /app/services        328.8s
 => [llm1-proxy] exporting to image                                     44.6s
 => => exporting layers                                                 14.3s
 => => writing image sha256:e446263e41f2e1795bdbe168bf7a2517766bd4a4fc  17.6s
 => => naming to docker.io/library/msjarvis-rebuild-llm1-proxy           0.9s
 => [jarvis-psychology-services] exporting to image                     48.7s
 => => exporting layers                                                 15.8s
 => => writing image sha256:582118cfc71b605a6fd8481f9a4ea194deac9a387c  13.2s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-psychology-s  1.3s
 => [nbb_heteroglobulin_transport 5/8] RUN pip install --no-cache-dir  110.0s
 => [llm16-proxy] exporting to image                                    44.9s
 => => exporting layers                                                 14.8s
 => => writing image sha256:a1402ab260c41ed9ea6493b3ded9e401c0c2088aec  16.7s
 => => naming to docker.io/library/msjarvis-rebuild-llm16-proxy          0.9s
 => [jarvis-hippocampus 4/5] RUN pip install --no-cache-dir     fasta  730.3s
 => [llm13-proxy] exporting to image                                    46.7s
 => => exporting layers                                                 17.2s
 => => writing image sha256:26072f1e404b30d59a75fd918af7e0999a80d9155f  13.9s
 => => naming to docker.io/library/msjarvis-rebuild-llm13-proxy          1.1s
 => [nbb_pituitary_gland 6/8] RUN pip install --no-cache-dir flask      19.5s
 => [llm9-proxy] exporting to image                                     46.1s
 => => exporting layers                                                 15.2s
 => => writing image sha256:78799f772b062a03a596c4401cd9f1d77b71ab86e7  13.9s
 => => naming to docker.io/library/msjarvis-rebuild-llm9-proxy           1.0s
 => [jarvis-judge-consistency 4/5] COPY judge_*.py /app/                 8.4s
 => [jarvis-auth-api 4/5] COPY services/ /app/services/                328.0s
 => [llm17-proxy] exporting to image                                    48.5s
 => => exporting layers                                                 18.2s
 => => writing image sha256:a782d5833e3495d0ae90ba5730b5f2e75d6bf98209  13.1s
 => => naming to docker.io/library/msjarvis-rebuild-llm17-proxy          1.4s
 => [jarvis-main-brain 4/7] COPY requirements.txt /app/                  8.2s
 => [llm20-proxy] exporting to image                                    42.5s
 => => exporting layers                                                 12.3s
 => => writing image sha256:86cbab0147cce5133422e4aaf4aac188d63a14fe0e  17.9s
 => => naming to docker.io/library/msjarvis-rebuild-llm20-proxy          0.7s
 => [llm7-proxy] exporting to image                                     52.6s
 => => exporting layers                                                 20.4s
 => => writing image sha256:1c1af6f5b551b9975838caf165369afb1fd6713ea55  7.3s
 => => naming to docker.io/library/msjarvis-rebuild-llm7-proxy           1.9s
 => [llm22-proxy] exporting to image                                    49.8s
 => => exporting layers                                                 19.4s
 => => writing image sha256:815e1fecc35f8470310fc5221dcc4a18e22ee2ba83  10.8s
 => => naming to docker.io/library/msjarvis-rebuild-llm22-proxy          1.4s
 => [jarvis-fifth-dgm 4/9] COPY requirements.txt /app/requirements.txt   8.2s
 => [nbb_blood_brain_barrier 5/7] RUN pip install --no-cache-dir flas  109.8s
 => [nbb_spiritual_root 6/8] RUN pip install --no-cache-dir flask       11.0s
 => [jarvis-qualia-engine  4/12] RUN pip install --upgrade pip setupt  327.3s
 => [llm10-proxy] exporting to image                                    81.0s
 => => exporting layers                                                 37.3s
 => => writing image sha256:6cd1a93c859b50add3dc21c9534b26c0e809fbe2058  5.8s
 => => naming to docker.io/library/msjarvis-rebuild-llm10-proxy          0.2s
 => [jarvis-blood-brain-barrier 4/6] COPY neurobiological_brain/blood_b  8.0s
 => [jarvis-woah 4/5] COPY services /app/services                      327.8s
 => [psychological_rag_domain] exporting to image                      170.1s
 => => exporting layers                                                168.5s
 => => writing image sha256:6b26aeba87f038627efb0618a5e859b8b4055772e30  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-psychological_rag_d  0.1s
 => [llm11-proxy] exporting to image                                    52.6s
 => => exporting layers                                                 23.1s
 => => writing image sha256:902b84d3b27a5314cc791ef93df8aae4392f9e65f5e  5.4s
 => => naming to docker.io/library/msjarvis-rebuild-llm11-proxy          1.9s
 => [jarvis-local-resources] exporting to image                         44.5s
 => => exporting layers                                                 13.8s
 => => writing image sha256:f441e205138ef4c9b4a5f03b7d2ea882e076be915f  16.5s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-local-resour  1.0s
 => [llm3-proxy] exporting to image                                     50.0s
 => => exporting layers                                                 19.0s
 => => writing image sha256:2f7d2b3fa38539f3e38ac930e0b0a94fb846b6f05fa  7.3s
 => => naming to docker.io/library/msjarvis-rebuild-llm3-proxy           1.8s
 => [jarvis-gis-rag] exporting to image                                 48.0s
 => => exporting layers                                                 18.4s
 => => writing image sha256:d7224201757ad620dd52e398b9fecd2507998d9f3a  11.9s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-gis-rag       1.4s
 => [nbb_subconscious 6/8] RUN pip install --no-cache-dir flask         10.4s
 => [nbb_qualia_engine] exporting to image                              87.4s
 => => exporting layers                                                 35.8s
 => => writing image sha256:da5ff0e5bff1aaf2d16fcabb4100dc65d70e168d288  5.8s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_qualia_engine    1.7s
 => CANCELED [jarvis-neurobiological-master 4/5] RUN pip install --no  820.5s
 => [nbb-i-containers 4/6] COPY services/ /app/services/               327.3s
 => [nbb_woah_algorithms 5/6] RUN pip install --no-cache-dir redis      18.0s
 => [jarvis-unified-gateway 4/5] COPY gateway-entrypoint.sh /app/gatewa  7.6s
 => [nbb_spiritual_maternal_integration 5/8] RUN pip install --no-cac  108.7s
 => [llm6-proxy] exporting to image                                     50.3s
 => => exporting layers                                                 20.5s
 => => writing image sha256:14c632d957c5dbe006b8f3b6feeb50331bb9940b818  5.4s
 => => naming to docker.io/library/msjarvis-rebuild-llm6-proxy           1.9s
 => [llm19-proxy] exporting to image                                    52.7s
 => => exporting layers                                                 23.8s
 => => writing image sha256:e6a6f65f510beb193be9ebe478bc4dfcc981cb09060  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-llm19-proxy          0.7s
 => [jarvis-toroidal 5/7] RUN pip install --no-cache-dir -r /app/requ  320.8s
 => [jarvis-semaphore 5/6] RUN pip install --no-cache-dir -r /app/req  320.8s
 => [jarvis-fractal-consciousness 6/7] COPY integration_layer/ /app/int  3.6s
 => [jarvis-i-containers 5/6] COPY integration_layer/ /app/integration_  3.4s
 => [jarvis-spiritual-rag] exporting to image                           80.4s
 => => exporting layers                                                 33.6s
 => => writing image sha256:6c02d6c35a5853cb3ff3c0385925d3e99a05681e615  5.8s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-spiritual-ra  1.5s
 => [jarvis-temporal-consciousness] exporting to image                  80.6s
 => => exporting layers                                                 35.6s
 => => writing image sha256:cce7ce4dddf8f3564198f5f3cc8d5902a449dc19a15  5.8s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-temporal-con  1.7s
 => [jarvis-eeg-delta 5/8] COPY jarvis_eeg_delta_30s.py /app/            3.2s
 => [jarvis-web-research] exporting to image                            80.6s
 => => exporting layers                                                 34.9s
 => => writing image sha256:953786fadd8d13d84328a95d16bc35b8d219a7c909e  5.8s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-web-research  1.7s
 => [jarvis-aaacpe-rag 5/5] COPY aaacpe_rag_service.py /app/             3.4s
 => [jarvis-judge-pipeline 5/5] COPY lm_synthesizer.py /app/             3.2s
 => CANCELED [jarvis-wv-entangled-gateway 5/7] RUN pip install --no-c  814.4s
 => CANCELED [jarvis-fifth-dgm 5/9] RUN pip install --no-cache-dir -r  814.9s
 => [jarvis-blood-brain-barrier 5/6] RUN pip install --no-cache-dir -  319.7s
 => [jarvis-unified-gateway 5/5] RUN chmod +x /app/gateway-entrypoint.s  4.8s
 => [jarvis-i-containers 6/6] COPY neurobiological_brain/ /app/neurobio  3.2s
 => [jarvis-fractal-consciousness 7/7] COPY ms_jarvis_web_research_simp  3.1s
 => [jarvis-eeg-beta 6/8] COPY jarvis_eeg_theta_60s.py /app/             3.0s
 => [nbb_subconscious 7/8] RUN pip install --no-cache-dir redis         58.0s
 => [nbb_spiritual_root 7/8] RUN pip install --no-cache-dir redis       97.4s
 => [jarvis-judge-alignment] exporting to image                         76.5s
 => => exporting layers                                                 33.1s
 => => writing image sha256:6019af2cff82e0353cd45d27352d5bfbd8f702aa2b2  5.8s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-judge-alignm  1.3s
 => [jarvis-judge-truth] exporting to image                             76.0s
 => => exporting layers                                                 33.1s
 => => writing image sha256:e435e6611d27eaf90bfd81bd33c8f1e56dc8eed9cff  5.8s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-judge-truth   1.1s
 => [jarvis-judge-consistency] exporting to image                       75.4s
 => => exporting layers                                                 33.1s
 => => writing image sha256:7cee3224a6b1159889167041d164eb48013f4b364ac  5.8s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-judge-consis  0.7s
 => [jarvis-judge-ethics] exporting to image                            75.6s
 => => exporting layers                                                 33.1s
 => => writing image sha256:6d7b80f8d7b4fb2c5851b6f313f23c3569200c81f2c  5.8s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-judge-ethics  0.8s
 => [jarvis-judge-pipeline] exporting to image                          75.6s
 => => exporting layers                                                 33.0s
 => => writing image sha256:4bee721a293d20b5840a0acad44839848ec4aec276a  5.8s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-judge-pipeli  0.8s
 => [jarvis-aaacpe-rag] exporting to image                             276.4s
 => => exporting layers                                                266.7s
 => => writing image sha256:a51f0f152f43cc1886e73e7ff22b44b0c0cad9f5cea  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-aaacpe-rag    0.1s
 => [jarvis-unified-gateway] exporting to image                        281.6s
 => => exporting layers                                                281.3s
 => => writing image sha256:7d72e59f89b7b04b4c10c3d78921cd5b5f61d46dbea  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-unified-gate  0.1s
 => [jarvis-eeg-delta 7/8] COPY jarvis_eeg_beta_5m.py /app/              5.1s
 => [jarvis-i-containers] exporting to image                            73.8s
 => => exporting layers                                                 32.1s
 => => writing image sha256:e095e0bf92ede662a897a30e005035dc5936eac44c7  5.8s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-i-containers  1.5s
 => [jarvis-fractal-consciousness] exporting to image                   74.2s
 => => exporting layers                                                 48.6s
 => => writing image sha256:d2e3719a6f0a9df5a20d2e9835abecf52ff88817048  1.3s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-fractal-cons  0.3s
 => [llm8-proxy] resolving provenance for metadata file                  0.0s
 => [nbb_woah_algorithms 6/6] RUN pip install --no-cache-dir requests   90.8s
 => [nbb_pituitary_gland 7/8] RUN pip install --no-cache-dir redis      90.8s
 => [nbb_consciousness_containers 7/8] RUN pip install --no-cache-dir   90.7s
 => [jarvis-eeg-theta 8/8] RUN touch /app/eeg_shared/__init__.py        90.5s
 => [llm14-proxy] resolving provenance for metadata file                 0.0s
 => [nbb_subconscious 8/8] RUN pip install --no-cache-dir requests     258.6s
 => [nbb_spiritual_root 8/8] RUN pip install --no-cache-dir requests   219.0s
 => [nbb_mother_carrie_protocols 6/8] COPY service_discovery.py /app/  219.3s
 => [nbb_heteroglobulin_transport 6/8] COPY service_discovery.py /app  219.0s
 => [nbb_prefrontal_cortex 6/8] COPY service_discovery.py /app/servic  218.8s
 => [nbb_spiritual_maternal_integration 6/8] COPY service_discovery.p  218.4s
 => [nbb_blood_brain_barrier 6/7] RUN pip install --no-cache-dir redi  217.7s
 => [nbb_consciousness_containers 8/8] RUN pip install --no-cache-dir  218.1s
 => [nbb_pituitary_gland 8/8] RUN pip install --no-cache-dir requests  217.9s
 => [jarvis-eeg-theta] exporting to image                              220.6s
 => => exporting layers                                                219.2s
 => => writing image sha256:4f5cf0805f9ea6c88d08c64f4f54f2f4645c7b595b1  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-eeg-theta     0.1s
 => [jarvis-eeg-beta] exporting to image                               220.5s
 => => exporting layers                                                219.2s
 => => writing image sha256:45c3b5e1eb98342dd22d2b90589d613ea9a53b714ba  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-eeg-beta      0.1s
 => [jarvis-eeg-delta] exporting to image                              220.6s
 => => exporting layers                                                219.2s
 => => writing image sha256:c6ea9ad3ace46dc5a48fd01d802bd9560ed4ce31994  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-eeg-delta     0.1s
 => [nbb_woah_algorithms] exporting to image                            38.3s
 => => exporting layers                                                 36.3s
 => => writing image sha256:dd1f4dfb749fb1b886f2eaaab70a2dfae5a53eeb5d4  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_woah_algorithms  0.2s
 => [llm18-proxy] resolving provenance for metadata file               114.6s
 => [jarvis-local-resources] resolving provenance for metadata file    116.8s
 => [llm17-proxy] resolving provenance for metadata file               114.3s
 => [jarvis-psychology-services] resolving provenance for metadata fi  111.5s
 => [llm6-proxy] resolving provenance for metadata file                110.5s
 => [llm22-proxy] resolving provenance for metadata file               109.5s
 => [llm19-proxy] resolving provenance for metadata file               108.1s
 => [llm11-proxy] resolving provenance for metadata file               105.9s
 => [llm2-proxy] resolving provenance for metadata file                102.9s
 => [llm1-proxy] resolving provenance for metadata file                102.0s
 => [llm4-proxy] resolving provenance for metadata file                101.0s
 => [llm3-proxy] resolving provenance for metadata file                100.0s
 => [llm5-proxy] resolving provenance for metadata file                 99.2s
 => [llm13-proxy] resolving provenance for metadata file                97.2s
 => [llm16-proxy] resolving provenance for metadata file                93.5s
 => [llm15-proxy] resolving provenance for metadata file                91.8s
 => [llm7-proxy] resolving provenance for metadata file                 89.9s
 => [llm20-proxy] resolving provenance for metadata file                88.4s
 => [jarvis-gis-rag] resolving provenance for metadata file             85.5s
 => [llm21-proxy] resolving provenance for metadata file                83.0s
 => [llm12-proxy] resolving provenance for metadata file                80.6s
 => [jarvis-judge-pipeline] resolving provenance for metadata file      76.7s
 => [llm9-proxy] resolving provenance for metadata file                 74.7s
 => [nbb_darwin_godel_machines] resolving provenance for metadata file  73.1s
 => [llm10-proxy] resolving provenance for metadata file                70.8s
 => [jarvis-judge-consistency] resolving provenance for metadata file   68.4s
 => [jarvis-judge-ethics] resolving provenance for metadata file        66.3s
 => [jarvis-spiritual-rag] resolving provenance for metadata file       64.9s
 => [jarvis-judge-truth] resolving provenance for metadata file         62.7s
 => [jarvis-judge-alignment] resolving provenance for metadata file     60.6s
 => [jarvis-i-containers] resolving provenance for metadata file        56.3s
 => [nbb_qualia_engine] resolving provenance for metadata file          54.8s
 => [jarvis-temporal-consciousness] resolving provenance for metadata   51.8s
 => [jarvis-web-research] resolving provenance for metadata file        24.0s
 => [jarvis-fractal-consciousness] resolving provenance for metadata f  23.0s
 => [nbb_woah_algorithms] resolving provenance for metadata file         1.0s
 => [psychological_rag_domain] resolving provenance for metadata file    0.0s
 => [jarvis-aaacpe-rag] resolving provenance for metadata file           0.4s
 => [jarvis-unified-gateway] resolving provenance for metadata file      0.0s
 => CANCELED [jarvis-qualia-engine  5/12] RUN pip install --no-cache-  496.0s
 => [jarvis-toroidal 6/7] RUN python -m pip install --no-cache-dir fas  54.0s
 => [nbb_blood_brain_barrier 7/7] RUN pip install --no-cache-dir reque  54.2s
 => [jarvis-semaphore 6/6] COPY msjarvis_semaphore.py /app/msjarvis_sem  2.9s
 => [jarvis-auth-api 5/5] COPY auth_api.py /app/auth_api.py              2.9s
 => [nbb_spiritual_root] exporting to image                              8.1s
 => => exporting layers                                                  7.8s
 => => writing image sha256:4cf6c1183bc3df930c55b178b2473a275332eaa3bc9  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_spiritual_root   0.0s
 => [nbb_pituitary_gland] exporting to image                             7.8s
 => => exporting layers                                                  6.6s
 => => writing image sha256:b7b2457eb2ceec2cdfad6e468e46b645e0c25bdd89b  0.5s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_pituitary_gland  0.2s
 => [jarvis-20llm-production 5/5] RUN pip install --no-cache-dir fast  134.6s
 => [nbb_subconscious] exporting to image                                7.9s
 => => exporting layers                                                  7.5s
 => => writing image sha256:22ba95b21e8fe53e0b2fd2d69a34040a7bc05a99696  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_subconscious     0.1s
 => [nbb_consciousness_containers] exporting to image                    7.8s
 => => exporting layers                                                  7.0s
 => => writing image sha256:925645fcfd3093087480779bfbe3dc756ef34653b9a  0.5s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_consciousness_c  0.0s
 => [jarvis-blood-brain-barrier 6/6] COPY . /app/services              439.9s
 => [jarvis-woah 5/5] RUN pip install --no-cache-dir fastapi uvicorn[  130.5s
 => [nbb-i-containers 5/6] COPY requirements.txt /app/requirements.txt   2.5s
 => [nbb_spiritual_maternal_integration 7/8] RUN pip install --no-cach  53.6s
 => [nbb_prefrontal_cortex 7/8] RUN pip install --no-cache-dir request  53.6s
 => [nbb_heteroglobulin_transport 7/8] RUN pip install --no-cache-dir   53.2s
 => [nbb_mother_carrie_protocols 7/8] RUN pip install --no-cache-dir r  53.1s
 => [jarvis-semaphore] exporting to image                                9.6s
 => => exporting layers                                                  9.3s
 => => writing image sha256:1ec22503176809d28125cdf3627bf60cc2ad04e0f65  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-semaphore     0.0s
 => [jarvis-auth-api] exporting to image                               132.8s
 => => exporting layers                                                132.8s
 => => writing image sha256:0323cf36a992d9075514bf98afccbc1d488c0722a8a  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-auth-api      0.0s
 => CANCELED [nbb-i-containers 6/6] RUN pip install --no-cache-dir -r  492.2s
 => [jarvis-eeg-theta] resolving provenance for metadata file            0.3s
 => [jarvis-eeg-delta] resolving provenance for metadata file            0.1s
 => [jarvis-eeg-beta] resolving provenance for metadata file             0.0s
 => [nbb_pituitary_gland] resolving provenance for metadata file         0.6s
 => [nbb_consciousness_containers] resolving provenance for metadata fi  0.3s
 => [nbb_subconscious] resolving provenance for metadata file            0.2s
 => [nbb_spiritual_root] resolving provenance for metadata file          0.0s
 => [jarvis-semaphore] resolving provenance for metadata file            0.5s
 => [jarvis-toroidal 7/7] COPY toroidal_service.py /app/toroidal_servic  2.9s
 => [nbb_mother_carrie_protocols 8/8] COPY service_registry_client.py /  2.9s
 => [nbb_heteroglobulin_transport 8/8] COPY service_registry_client.py   2.9s
 => [nbb_blood_brain_barrier] exporting to image                        12.2s
 => => exporting layers                                                 11.7s
 => => writing image sha256:7b7b3cb2dae20aaa3c903481a9186d9ba7d5aeecbb3  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_blood_brain_bar  0.0s
 => [nbb_spiritual_maternal_integration 8/8] COPY service_registry_clie  2.7s
 => [nbb_prefrontal_cortex 8/8] COPY service_registry_client.py /app/se  2.7s
 => [jarvis-toroidal] exporting to image                                 9.5s
 => => exporting layers                                                  9.2s
 => => writing image sha256:d1f44bee7f13d662e67a2898c5bed6cb0bcf3b459a4  0.0s
 => => naming to docker.io/library/msjarvis-toroidal:latest              0.0s
 => [nbb_mother_carrie_protocols] exporting to image                     2.2s
 => => exporting layers                                                  1.6s
 => => writing image sha256:bffa7eb77532b343e737033d427e1bb69f9baad0539  0.3s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_mother_carrie_p  0.0s
 => [nbb_spiritual_maternal_integration] exporting to image              8.0s
 => => exporting layers                                                  2.2s
 => => writing image sha256:13f6959177ee5eecba4b10b55fb2e0fcfd2e17ded16  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_spiritual_mater  0.2s
 => [nbb_heteroglobulin_transport] exporting to image                    3.0s
 => => exporting layers                                                  2.1s
 => => writing image sha256:c5be8041eee45d2c4e89ddf97ca788e0714ddc082c6  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_heteroglobulin_  0.3s
 => [nbb_prefrontal_cortex] exporting to image                           8.0s
 => => exporting layers                                                  3.2s
 => => writing image sha256:5a70be21b5119647bcbb42df1a9afed6a2d5dd3e671  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_prefrontal_cort  0.3s
 => [nbb_heteroglobulin_transport] resolving provenance for metadata fi  0.8s
 => [nbb_mother_carrie_protocols] resolving provenance for metadata fil  0.4s
 => [nbb_spiritual_maternal_integration] resolving provenance for metad  0.3s
 => [nbb_prefrontal_cortex] resolving provenance for metadata file       0.1s
 => [nbb_blood_brain_barrier] resolving provenance for metadata file     0.0s
 => [jarvis-toroidal] resolving provenance for metadata file             0.0s
 => [jarvis-brain-orchestrator] exporting to image                     123.6s
 => => exporting layers                                                123.4s
 => => writing image sha256:bec92fd4832de3e0a489f7ce16b27d42fe55ced5be0  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-brain-orches  0.0s
 => [jarvis-woah] exporting to image                                   123.6s
 => => exporting layers                                                123.4s
 => => writing image sha256:58d7b3ce33d9b9818feec7f5ff38418fbdb4c8d0603  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-woah          0.0s
 => [jarvis-20llm-production] exporting to image                       123.5s
 => => exporting layers                                                123.4s
 => => writing image sha256:59a706e5450750ee8db6acd5b7e818540bebc0e2338  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-20llm-produc  0.0s
 => [jarvis-auth-api] resolving provenance for metadata file             0.1s
 => [jarvis-20llm-production] resolving provenance for metadata file     0.2s
 => [jarvis-woah] resolving provenance for metadata file                 0.1s
 => [jarvis-brain-orchestrator] resolving provenance for metadata file   0.0s
 => [jarvis-hippocampus 5/5] COPY hippocampus_service.py /app/hippocamp  7.8s
 => [jarvis-hippocampus] exporting to image                             31.8s
 => => exporting layers                                                 31.8s
 => => writing image sha256:3cb112e34f1cb67c5310fa411c25e834467891b0a06  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-hippocampus   0.0s
 => [jarvis-blood-brain-barrier] exporting to image                     57.7s
 => => exporting layers                                                 57.7s
 => [jarvis-hippocampus] resolving provenance for metadata file          0.0s
------
 > [jarvis-dgm-bridge-21 4/5] RUN pip install --no-cache-dir -r requirements.txt:
53.01 Collecting fastapi (from -r requirements.txt (line 1))
55.30   Downloading fastapi-0.136.3-py3-none-any.whl.metadata (27 kB)
58.59 Collecting pydantic (from -r requirements.txt (line 3))
59.13   Downloading pydantic-2.13.4-py3-none-any.whl.metadata (109 kB)
63.16 Collecting numpy (from -r requirements.txt (line 4))
63.51   Downloading numpy-2.4.6-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
63.91 Collecting httpx (from -r requirements.txt (line 5))
64.48   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
65.48 Collecting chromadb==1.2.2 (from -r requirements.txt (line 6))
65.99   Downloading chromadb-1.2.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.2 kB)
66.93 Collecting redis (from -r requirements.txt (line 7))
67.56   Downloading redis-8.0.0-py3-none-any.whl.metadata (13 kB)
68.44 Collecting python-multipart (from -r requirements.txt (line 8))
68.89   Downloading python_multipart-0.0.29-py3-none-any.whl.metadata (2.1 kB)
69.34 Collecting requests (from -r requirements.txt (line 9))
69.65   Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
69.82 Collecting ollama (from -r requirements.txt (line 10))
70.31   Downloading ollama-0.6.2-py3-none-any.whl.metadata (5.8 kB)
74.36 Collecting aiohttp (from -r requirements.txt (line 11))
75.07   Downloading aiohttp-3.13.5-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (8.1 kB)
75.89 Collecting asyncio (from -r requirements.txt (line 12))
76.60   Downloading asyncio-4.0.0-py3-none-any.whl.metadata (994 bytes)
78.29 Collecting python-dateutil (from -r requirements.txt (line 13))
79.12   Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
80.10 Collecting transformers (from -r requirements.txt (line 15))
80.15   Downloading transformers-5.9.0-py3-none-any.whl.metadata (33 kB)
81.14 Collecting sentence_transformers (from -r requirements.txt (line 16))
82.84   Downloading sentence_transformers-5.5.1-py3-none-any.whl.metadata (18 kB)
83.56 Collecting pytz (from -r requirements.txt (line 17))
83.90   Downloading pytz-2026.2-py2.py3-none-any.whl.metadata (22 kB)
84.82 Collecting scikit-learn (from -r requirements.txt (line 18))
85.23   Downloading scikit_learn-1.8.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (11 kB)
86.10 Collecting scipy (from -r requirements.txt (line 19))
86.62   Downloading scipy-1.17.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
87.45 Collecting textblob (from -r requirements.txt (line 20))
87.75   Downloading textblob-0.20.0-py3-none-any.whl.metadata (4.0 kB)
88.15 Collecting duckduckgo-search (from -r requirements.txt (line 21))
88.56   Downloading duckduckgo_search-8.1.1-py3-none-any.whl.metadata (16 kB)
88.91 Collecting rake-nltk (from -r requirements.txt (line 22))
89.29   Downloading rake_nltk-1.0.6-py3-none-any.whl.metadata (6.4 kB)
89.54 Collecting nltk (from -r requirements.txt (line 23))
89.71   Downloading nltk-3.9.4-py3-none-any.whl.metadata (3.2 kB)
90.15 Collecting PyPDF2 (from -r requirements.txt (line 24))
90.52   Downloading pypdf2-3.0.1-py3-none-any.whl.metadata (6.8 kB)
90.85 Collecting Flask (from -r requirements.txt (line 25))
92.16   Downloading flask-3.1.3-py3-none-any.whl.metadata (3.2 kB)
92.58 Collecting Flask-CORS (from -r requirements.txt (line 26))
93.04   Downloading flask_cors-6.0.2-py3-none-any.whl.metadata (5.3 kB)
93.60 Collecting asgiref (from -r requirements.txt (line 27))
94.09   Downloading asgiref-3.11.1-py3-none-any.whl.metadata (9.3 kB)
94.87 Collecting psycopg2-binary (from -r requirements.txt (line 28))
95.36   Downloading psycopg2_binary-2.9.12-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
96.19 Collecting uvicorn[standard] (from -r requirements.txt (line 2))
96.52   Downloading uvicorn-0.48.0-py3-none-any.whl.metadata (6.7 kB)
97.09 Collecting build>=1.0.3 (from chromadb==1.2.2->-r requirements.txt (line 6))
97.56   Downloading build-1.5.0-py3-none-any.whl.metadata (5.7 kB)
98.44 Collecting pybase64>=1.4.1 (from chromadb==1.2.2->-r requirements.txt (line 6))
98.91   Downloading pybase64-1.4.3-cp312-cp312-manylinux1_x86_64.manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_5_x86_64.whl.metadata (8.7 kB)
99.48 Collecting posthog<6.0.0,>=2.4.0 (from chromadb==1.2.2->-r requirements.txt (line 6))
99.99   Downloading posthog-5.4.0-py3-none-any.whl.metadata (5.7 kB)
100.3 Collecting typing-extensions>=4.5.0 (from chromadb==1.2.2->-r requirements.txt (line 6))
100.7   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
102.0 Collecting onnxruntime>=1.14.1 (from chromadb==1.2.2->-r requirements.txt (line 6))
102.5   Downloading onnxruntime-1.26.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (5.3 kB)
103.0 Collecting opentelemetry-api>=1.2.0 (from chromadb==1.2.2->-r requirements.txt (line 6))
103.6   Downloading opentelemetry_api-1.42.1-py3-none-any.whl.metadata (1.4 kB)
104.3 Collecting opentelemetry-exporter-otlp-proto-grpc>=1.2.0 (from chromadb==1.2.2->-r requirements.txt (line 6))
104.6   Downloading opentelemetry_exporter_otlp_proto_grpc-1.42.1-py3-none-any.whl.metadata (2.6 kB)
104.9 Collecting opentelemetry-sdk>=1.2.0 (from chromadb==1.2.2->-r requirements.txt (line 6))
105.4   Downloading opentelemetry_sdk-1.42.1-py3-none-any.whl.metadata (1.7 kB)
107.0 Collecting tokenizers>=0.13.2 (from chromadb==1.2.2->-r requirements.txt (line 6))
108.4   Downloading tokenizers-0.23.1-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.8 kB)
109.3 Collecting pypika>=0.48.9 (from chromadb==1.2.2->-r requirements.txt (line 6))
109.8   Downloading pypika-0.51.1-py2.py3-none-any.whl.metadata (51 kB)
110.7 Collecting tqdm>=4.65.0 (from chromadb==1.2.2->-r requirements.txt (line 6))
111.5   Downloading tqdm-4.67.3-py3-none-any.whl.metadata (57 kB)
113.2 Collecting overrides>=7.3.1 (from chromadb==1.2.2->-r requirements.txt (line 6))
115.0   Downloading overrides-7.7.0-py3-none-any.whl.metadata (5.8 kB)
116.0 Collecting importlib-resources (from chromadb==1.2.2->-r requirements.txt (line 6))
116.4   Downloading importlib_resources-7.1.0-py3-none-any.whl.metadata (4.0 kB)
121.6 Collecting grpcio>=1.58.0 (from chromadb==1.2.2->-r requirements.txt (line 6))
122.3   Downloading grpcio-1.80.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (3.8 kB)
123.1 Collecting bcrypt>=4.0.1 (from chromadb==1.2.2->-r requirements.txt (line 6))
123.8   Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl.metadata (10 kB)
125.9 Collecting typer>=0.9.0 (from chromadb==1.2.2->-r requirements.txt (line 6))
126.4   Downloading typer-0.26.3-py3-none-any.whl.metadata (16 kB)
127.7 Collecting kubernetes>=28.1.0 (from chromadb==1.2.2->-r requirements.txt (line 6))
127.9   Downloading kubernetes-36.0.1-py2.py3-none-any.whl.metadata (1.8 kB)
128.4 Collecting tenacity>=8.2.3 (from chromadb==1.2.2->-r requirements.txt (line 6))
128.9   Downloading tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)
130.5 Collecting pyyaml>=6.0.0 (from chromadb==1.2.2->-r requirements.txt (line 6))
131.2   Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
134.8 Collecting mmh3>=4.0.1 (from chromadb==1.2.2->-r requirements.txt (line 6))
135.8   Downloading mmh3-5.2.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (14 kB)
143.0 Collecting orjson>=3.9.12 (from chromadb==1.2.2->-r requirements.txt (line 6))
143.5   Downloading orjson-3.11.9-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (41 kB)
146.0 Collecting rich>=10.11.0 (from chromadb==1.2.2->-r requirements.txt (line 6))
146.1   Downloading rich-15.0.0-py3-none-any.whl.metadata (18 kB)
147.5 Collecting jsonschema>=4.19.0 (from chromadb==1.2.2->-r requirements.txt (line 6))
148.2   Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
150.3 Collecting starlette>=0.46.0 (from fastapi->-r requirements.txt (line 1))
150.5   Downloading starlette-1.2.0-py3-none-any.whl.metadata (6.3 kB)
151.0 Collecting typing-inspection>=0.4.2 (from fastapi->-r requirements.txt (line 1))
152.8   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
153.4 Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 1))
153.8   Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
154.5 Collecting click>=7.0 (from uvicorn[standard]->-r requirements.txt (line 2))
155.4   Downloading click-8.4.1-py3-none-any.whl.metadata (2.6 kB)
156.2 Collecting h11>=0.8 (from uvicorn[standard]->-r requirements.txt (line 2))
156.8   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
158.2 Collecting httptools>=0.6.3 (from uvicorn[standard]->-r requirements.txt (line 2))
159.1   Downloading httptools-0.8.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)
161.9 Collecting python-dotenv>=0.13 (from uvicorn[standard]->-r requirements.txt (line 2))
162.7   Downloading python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
164.2 Collecting uvloop>=0.15.1 (from uvicorn[standard]->-r requirements.txt (line 2))
164.8   Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
167.3 Collecting watchfiles>=0.20 (from uvicorn[standard]->-r requirements.txt (line 2))
167.9   Downloading watchfiles-1.2.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
169.9 Collecting websockets>=10.4 (from uvicorn[standard]->-r requirements.txt (line 2))
170.4   Downloading websockets-16.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (6.8 kB)
170.6 Collecting annotated-types>=0.6.0 (from pydantic->-r requirements.txt (line 3))
171.4   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
188.9 Collecting pydantic-core==2.46.4 (from pydantic->-r requirements.txt (line 3))
189.1   Downloading pydantic_core-2.46.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
190.0 Collecting anyio (from httpx->-r requirements.txt (line 5))
190.6   Downloading anyio-4.13.0-py3-none-any.whl.metadata (4.5 kB)
191.2 Collecting certifi (from httpx->-r requirements.txt (line 5))
192.0   Downloading certifi-2026.5.20-py3-none-any.whl.metadata (2.5 kB)
192.4 Collecting httpcore==1.* (from httpx->-r requirements.txt (line 5))
192.9   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
194.3 Collecting idna (from httpx->-r requirements.txt (line 5))
195.0   Downloading idna-3.17-py3-none-any.whl.metadata (6.4 kB)
196.7 Collecting charset_normalizer<4,>=2 (from requests->-r requirements.txt (line 9))
197.3   Downloading charset_normalizer-3.4.7-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (40 kB)
198.9 Collecting urllib3<3,>=1.26 (from requests->-r requirements.txt (line 9))
199.8   Downloading urllib3-2.7.0-py3-none-any.whl.metadata (6.9 kB)
201.0 Collecting aiohappyeyeballs>=2.5.0 (from aiohttp->-r requirements.txt (line 11))
202.7   Downloading aiohappyeyeballs-2.6.2-py3-none-any.whl.metadata (5.9 kB)
203.5 Collecting aiosignal>=1.4.0 (from aiohttp->-r requirements.txt (line 11))
203.6   Downloading aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
204.2 Collecting attrs>=17.3.0 (from aiohttp->-r requirements.txt (line 11))
204.4   Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
205.6 Collecting frozenlist>=1.1.1 (from aiohttp->-r requirements.txt (line 11))
206.2   Downloading frozenlist-1.8.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (20 kB)
208.8 Collecting multidict<7.0,>=4.5 (from aiohttp->-r requirements.txt (line 11))
209.3   Downloading multidict-6.7.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (5.3 kB)
209.9 Collecting propcache>=0.2.0 (from aiohttp->-r requirements.txt (line 11))
210.6   Downloading propcache-0.5.2-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (16 kB)
212.9 Collecting yarl<2.0,>=1.17.0 (from aiohttp->-r requirements.txt (line 11))
213.6   Downloading yarl-1.24.2-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (94 kB)
216.0 Collecting six>=1.5 (from python-dateutil->-r requirements.txt (line 13))
217.3   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
218.1 Collecting huggingface-hub<2.0,>=1.5.0 (from transformers->-r requirements.txt (line 15))
218.7   Downloading huggingface_hub-1.17.0-py3-none-any.whl.metadata (14 kB)
219.6 Collecting packaging>=20.0 (from transformers->-r requirements.txt (line 15))
220.2   Downloading packaging-26.2-py3-none-any.whl.metadata (3.5 kB)
222.5 Collecting regex>=2025.10.22 (from transformers->-r requirements.txt (line 15))
222.9   Downloading regex-2026.5.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (40 kB)
223.4 Collecting tokenizers>=0.13.2 (from chromadb==1.2.2->-r requirements.txt (line 6))
223.9   Downloading tokenizers-0.22.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
225.4 Collecting safetensors>=0.4.3 (from transformers->-r requirements.txt (line 15))
226.0   Downloading safetensors-0.7.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
227.0 Collecting torch>=1.11.0 (from sentence_transformers->-r requirements.txt (line 16))
228.2   Downloading torch-2.12.0-cp312-cp312-manylinux_2_28_x86_64.whl.metadata (31 kB)
232.0 Collecting joblib>=1.3.0 (from scikit-learn->-r requirements.txt (line 18))
232.2   Downloading joblib-1.5.3-py3-none-any.whl.metadata (5.5 kB)
233.0 Collecting threadpoolctl>=3.2.0 (from scikit-learn->-r requirements.txt (line 18))
233.1   Downloading threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
234.0 Collecting primp>=0.15.0 (from duckduckgo-search->-r requirements.txt (line 21))
234.3   Downloading primp-1.3.1-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.7 kB)
235.5 Collecting lxml>=5.3.0 (from duckduckgo-search->-r requirements.txt (line 21))
235.6   Downloading lxml-6.1.1-cp312-cp312-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (3.5 kB)
235.9 Collecting blinker>=1.9.0 (from Flask->-r requirements.txt (line 25))
236.3   Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
236.6 Collecting itsdangerous>=2.2.0 (from Flask->-r requirements.txt (line 25))
238.0   Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
238.3 Collecting jinja2>=3.1.2 (from Flask->-r requirements.txt (line 25))
238.4   Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
239.1 Collecting markupsafe>=2.1.1 (from Flask->-r requirements.txt (line 25))
239.3   Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
239.7 Collecting werkzeug>=3.1.0 (from Flask->-r requirements.txt (line 25))
240.0   Downloading werkzeug-3.1.8-py3-none-any.whl.metadata (4.0 kB)
240.3 Collecting pyproject_hooks (from build>=1.0.3->chromadb==1.2.2->-r requirements.txt (line 6))
240.6   Downloading pyproject_hooks-1.2.0-py3-none-any.whl.metadata (1.3 kB)
241.2 Collecting filelock>=3.10.0 (from huggingface-hub<2.0,>=1.5.0->transformers->-r requirements.txt (line 15))
241.3   Downloading filelock-3.29.0-py3-none-any.whl.metadata (2.0 kB)
241.9 Collecting fsspec>=2023.5.0 (from huggingface-hub<2.0,>=1.5.0->transformers->-r requirements.txt (line 15))
242.1   Downloading fsspec-2026.4.0-py3-none-any.whl.metadata (10 kB)
242.9 Collecting hf-xet<2.0.0,>=1.4.3 (from huggingface-hub<2.0,>=1.5.0->transformers->-r requirements.txt (line 15))
243.4   Downloading hf_xet-1.5.0-cp37-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
243.5 Collecting typer>=0.9.0 (from chromadb==1.2.2->-r requirements.txt (line 6))
244.0   Downloading typer-0.25.1-py3-none-any.whl.metadata (15 kB)
244.3 Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=4.19.0->chromadb==1.2.2->-r requirements.txt (line 6))
244.4   Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
245.2 Collecting referencing>=0.28.4 (from jsonschema>=4.19.0->chromadb==1.2.2->-r requirements.txt (line 6))
245.9   Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
253.3 Collecting rpds-py>=0.25.0 (from jsonschema>=4.19.0->chromadb==1.2.2->-r requirements.txt (line 6))
254.1   Downloading rpds_py-2026.5.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
255.1 Collecting websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0 (from kubernetes>=28.1.0->chromadb==1.2.2->-r requirements.txt (line 6))
256.1   Downloading websocket_client-1.9.0-py3-none-any.whl.metadata (8.3 kB)
256.9 Collecting requests-oauthlib (from kubernetes>=28.1.0->chromadb==1.2.2->-r requirements.txt (line 6))
257.7   Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)
258.9 Collecting durationpy>=0.7 (from kubernetes>=28.1.0->chromadb==1.2.2->-r requirements.txt (line 6))
259.4   Downloading durationpy-0.10-py3-none-any.whl.metadata (340 bytes)
260.3 Collecting flatbuffers (from onnxruntime>=1.14.1->chromadb==1.2.2->-r requirements.txt (line 6))
260.9   Downloading flatbuffers-25.12.19-py2.py3-none-any.whl.metadata (1.0 kB)
265.3 Collecting protobuf (from onnxruntime>=1.14.1->chromadb==1.2.2->-r requirements.txt (line 6))
265.7   Downloading protobuf-7.35.0-cp310-abi3-manylinux2014_x86_64.whl.metadata (595 bytes)
266.8 Collecting googleapis-common-protos~=1.57 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb==1.2.2->-r requirements.txt (line 6))
267.6   Downloading googleapis_common_protos-1.75.0-py3-none-any.whl.metadata (8.6 kB)
269.0 Collecting opentelemetry-exporter-otlp-proto-common==1.42.1 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb==1.2.2->-r requirements.txt (line 6))
269.7   Downloading opentelemetry_exporter_otlp_proto_common-1.42.1-py3-none-any.whl.metadata (1.8 kB)
270.9 Collecting opentelemetry-proto==1.42.1 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb==1.2.2->-r requirements.txt (line 6))
271.8   Downloading opentelemetry_proto-1.42.1-py3-none-any.whl.metadata (2.3 kB)
271.8 Collecting protobuf (from onnxruntime>=1.14.1->chromadb==1.2.2->-r requirements.txt (line 6))
273.1   Downloading protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl.metadata (593 bytes)
274.1 Collecting opentelemetry-semantic-conventions==0.63b1 (from opentelemetry-sdk>=1.2.0->chromadb==1.2.2->-r requirements.txt (line 6))
274.6   Downloading opentelemetry_semantic_conventions-0.63b1-py3-none-any.whl.metadata (2.4 kB)
275.6 Collecting backoff>=1.10.0 (from posthog<6.0.0,>=2.4.0->chromadb==1.2.2->-r requirements.txt (line 6))
276.1   Downloading backoff-2.2.1-py3-none-any.whl.metadata (14 kB)
277.2 Collecting distro>=1.5.0 (from posthog<6.0.0,>=2.4.0->chromadb==1.2.2->-r requirements.txt (line 6))
277.6   Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
278.6 Collecting markdown-it-py>=2.2.0 (from rich>=10.11.0->chromadb==1.2.2->-r requirements.txt (line 6))
278.7   Downloading markdown_it_py-4.2.0-py3-none-any.whl.metadata (7.4 kB)
280.0 Collecting pygments<3.0.0,>=2.13.0 (from rich>=10.11.0->chromadb==1.2.2->-r requirements.txt (line 6))
280.7   Downloading pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
283.4 Collecting setuptools<82 (from torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
284.7   Downloading setuptools-81.0.0-py3-none-any.whl.metadata (6.6 kB)
285.1 Collecting sympy>=1.13.3 (from torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
286.8   Downloading sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
288.6 Collecting networkx>=2.5.1 (from torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
289.6   Downloading networkx-3.6.1-py3-none-any.whl.metadata (6.8 kB)
291.4 Collecting cuda-toolkit==13.0.2 (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
291.4   Downloading cuda_toolkit-13.0.2-py2.py3-none-any.whl.metadata (9.4 kB)
295.2 Collecting nvidia-cublas<=13.1.1.3,>=13.1.0.3 (from torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
295.8   Downloading nvidia_cublas-13.1.1.3-py3-none-manylinux_2_27_x86_64.whl.metadata (1.8 kB)
297.4 Collecting cuda-bindings<14,>=13.0.3 (from torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
298.1   Downloading cuda_bindings-13.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (2.5 kB)
298.3 Collecting nvidia-cudnn-cu13==9.20.0.48 (from torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
300.2   Downloading nvidia_cudnn_cu13-9.20.0.48-py3-none-manylinux_2_27_x86_64.whl.metadata (1.9 kB)
300.3 Collecting nvidia-cusparselt-cu13==0.8.1 (from torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
300.3   Downloading nvidia_cusparselt_cu13-0.8.1-py3-none-manylinux2014_x86_64.whl.metadata (12 kB)
301.0 Collecting nvidia-nccl-cu13==2.29.7 (from torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
301.0   Downloading nvidia_nccl_cu13-2.29.7-py3-none-manylinux_2_18_x86_64.whl.metadata (2.1 kB)
302.9 Collecting nvidia-nvshmem-cu13==3.4.5 (from torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
303.2   Downloading nvidia_nvshmem_cu13-3.4.5-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.1 kB)
303.4 Collecting triton==3.7.0 (from torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
303.7   Downloading triton-3.7.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (1.7 kB)
304.1 Collecting nvidia-cuda-runtime==13.0.96.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
304.2   Downloading nvidia_cuda_runtime-13.0.96-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.7 kB)
304.6 Collecting nvidia-cufft==12.0.0.61.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
304.8   Downloading nvidia_cufft-12.0.0.61-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.8 kB)
305.2 Collecting nvidia-cufile==1.15.1.6.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
306.4   Downloading nvidia_cufile-1.15.1.6-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.7 kB)
307.8 Collecting nvidia-cuda-cupti==13.0.85.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
307.8   Downloading nvidia_cuda_cupti-13.0.85-py3-none-manylinux_2_25_x86_64.whl.metadata (1.7 kB)
308.3 Collecting nvidia-curand==10.4.0.35.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
308.3   Downloading nvidia_curand-10.4.0.35-py3-none-manylinux_2_27_x86_64.whl.metadata (1.7 kB)
308.7 Collecting nvidia-cusolver==12.0.4.66.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
308.7   Downloading nvidia_cusolver-12.0.4.66-py3-none-manylinux_2_27_x86_64.whl.metadata (1.8 kB)
308.8 Collecting nvidia-cusparse==12.6.3.3.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
308.8   Downloading nvidia_cusparse-12.6.3.3-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.8 kB)
309.0 Collecting nvidia-nvjitlink==13.0.88.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
309.0   Downloading nvidia_nvjitlink-13.0.88-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl.metadata (1.7 kB)
309.1 Collecting nvidia-cuda-nvrtc==13.0.88.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
309.1   Downloading nvidia_cuda_nvrtc-13.0.88-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl.metadata (1.7 kB)
309.1 Collecting nvidia-nvtx==13.0.85.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
309.2   Downloading nvidia_nvtx-13.0.85-py3-none-manylinux1_x86_64.manylinux_2_5_x86_64.whl.metadata (1.8 kB)
309.5 Collecting shellingham>=1.3.0 (from typer>=0.9.0->chromadb==1.2.2->-r requirements.txt (line 6))
310.4   Downloading shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
310.6 Collecting cuda-pathfinder>=1.4.2 (from cuda-bindings<14,>=13.0.3->torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
310.6   Downloading cuda_pathfinder-1.5.5-py3-none-any.whl.metadata (1.9 kB)
310.7 Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=10.11.0->chromadb==1.2.2->-r requirements.txt (line 6))
310.7   Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
310.8 Collecting mpmath<1.4,>=1.1.0 (from sympy>=1.13.3->torch>=1.11.0->sentence_transformers->-r requirements.txt (line 16))
310.8   Downloading mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
311.0 Collecting oauthlib>=3.0.0 (from requests-oauthlib->kubernetes>=28.1.0->chromadb==1.2.2->-r requirements.txt (line 6))
311.0   Downloading oauthlib-3.3.1-py3-none-any.whl.metadata (7.9 kB)
311.6 Downloading chromadb-1.2.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (20.7 MB)
396.8    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 20.7/20.7 MB 266.6 kB/s eta 0:00:00
397.8 Downloading fastapi-0.136.3-py3-none-any.whl (117 kB)
400.3 Downloading pydantic-2.13.4-py3-none-any.whl (472 kB)
402.3 Downloading pydantic_core-2.46.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
407.4    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 414.6 kB/s eta 0:00:00
407.8 Downloading numpy-2.4.6-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.6 MB)
457.6    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.6/16.6 MB 302.4 kB/s eta 0:00:00
458.0 Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
459.6 Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
460.6 Downloading redis-8.0.0-py3-none-any.whl (499 kB)
464.8 Downloading python_multipart-0.0.29-py3-none-any.whl (29 kB)
465.7 Downloading requests-2.34.2-py3-none-any.whl (73 kB)
466.9 Downloading ollama-0.6.2-py3-none-any.whl (15 kB)
467.9 Downloading aiohttp-3.13.5-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.8 MB)
475.5    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 235.7 kB/s eta 0:00:00
475.9 Downloading asyncio-4.0.0-py3-none-any.whl (5.6 kB)
476.0 Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
477.1 Downloading transformers-5.9.0-py3-none-any.whl (10.8 MB)
504.1    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.8/10.8 MB 399.7 kB/s eta 0:00:00
504.4 Downloading sentence_transformers-5.5.1-py3-none-any.whl (588 kB)
505.8    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 588.9/588.9 kB 436.4 kB/s eta 0:00:00
505.9 Downloading pytz-2026.2-py2.py3-none-any.whl (510 kB)
507.8 Downloading scikit_learn-1.8.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (8.9 MB)
538.4    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.9/8.9 MB 291.1 kB/s eta 0:00:00
538.9 Downloading scipy-1.17.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (35.2 MB)
628.5    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.2/35.2 MB 412.0 kB/s eta 0:00:00
629.1 Downloading textblob-0.20.0-py3-none-any.whl (624 kB)
630.1    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 625.0/625.0 kB 453.2 kB/s eta 0:00:00
630.7 Downloading duckduckgo_search-8.1.1-py3-none-any.whl (18 kB)
631.3 Downloading rake_nltk-1.0.6-py3-none-any.whl (9.1 kB)
631.9 Downloading nltk-3.9.4-py3-none-any.whl (1.6 MB)
634.6    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 537.4 kB/s eta 0:00:00
634.9 Downloading pypdf2-3.0.1-py3-none-any.whl (232 kB)
635.4 Downloading flask-3.1.3-py3-none-any.whl (103 kB)
635.6 Downloading flask_cors-6.0.2-py3-none-any.whl (13 kB)
636.1 Downloading asgiref-3.11.1-py3-none-any.whl (24 kB)
636.5 Downloading psycopg2_binary-2.9.12-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.3 MB)
642.5    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.3/4.3 MB 704.5 kB/s eta 0:00:00
642.9 Downloading aiohappyeyeballs-2.6.2-py3-none-any.whl (15 kB)
643.3 Downloading aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
643.7 Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
644.4 Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
644.8 Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
645.4 Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl (278 kB)
646.6 Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
647.2 Downloading build-1.5.0-py3-none-any.whl (26 kB)
647.7 Downloading certifi-2026.5.20-py3-none-any.whl (134 kB)
649.5 Downloading charset_normalizer-3.4.7-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (216 kB)
652.2 Downloading click-8.4.1-py3-none-any.whl (116 kB)
653.3 Downloading frozenlist-1.8.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (242 kB)
655.0 Downloading grpcio-1.80.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (6.8 MB)
680.7    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.8/6.8 MB 259.7 kB/s eta 0:00:00
681.3 Downloading h11-0.16.0-py3-none-any.whl (37 kB)
682.1 Downloading httptools-0.8.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (523 kB)
683.7 Downloading huggingface_hub-1.17.0-py3-none-any.whl (671 kB)
685.7    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 671.5/671.5 kB 364.6 kB/s eta 0:00:00
685.9 Downloading idna-3.17-py3-none-any.whl (65 kB)
686.3 Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
686.8 Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
687.2 Downloading joblib-1.5.3-py3-none-any.whl (309 kB)
688.0 Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)
688.5 Downloading kubernetes-36.0.1-py2.py3-none-any.whl (4.6 MB)
700.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 383.8 kB/s eta 0:00:00
700.9 Downloading lxml-6.1.1-cp312-cp312-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (5.2 MB)
718.0    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.2/5.2 MB 301.3 kB/s eta 0:00:00
718.7 Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
719.1 Downloading mmh3-5.2.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (103 kB)
720.2 Downloading multidict-6.7.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (256 kB)
721.1 Downloading onnxruntime-1.26.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (18.2 MB)
774.4    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.2/18.2 MB 357.8 kB/s eta 0:00:00
777.1 Downloading opentelemetry_api-1.42.1-py3-none-any.whl (61 kB)
795.3 Downloading opentelemetry_exporter_otlp_proto_grpc-1.42.1-py3-none-any.whl (19 kB)
819.2 ERROR: Exception:
819.2 Traceback (most recent call last):
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_vendor/urllib3/response.py", line 438, in _error_catcher
819.2     yield
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_vendor/urllib3/response.py", line 561, in read
819.2     data = self._fp_read(amt) if not fp_closed else b""
819.2            ^^^^^^^^^^^^^^^^^^
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_vendor/urllib3/response.py", line 527, in _fp_read
819.2     return self._fp.read(amt) if amt is not None else self._fp.read()
819.2            ^^^^^^^^^^^^^^^^^^
819.2   File "/usr/local/lib/python3.12/http/client.py", line 484, in read
819.2     s = self.fp.read(amt)
819.2         ^^^^^^^^^^^^^^^^^
819.2   File "/usr/local/lib/python3.12/socket.py", line 720, in readinto
819.2     return self._sock.recv_into(b)
819.2            ^^^^^^^^^^^^^^^^^^^^^^^
819.2   File "/usr/local/lib/python3.12/ssl.py", line 1251, in recv_into
819.2     return self.read(nbytes, buffer)
819.2            ^^^^^^^^^^^^^^^^^^^^^^^^^
819.2   File "/usr/local/lib/python3.12/ssl.py", line 1103, in read
819.2     return self._sslobj.read(len, buffer)
819.2            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
819.2 TimeoutError: The read operation timed out
819.2 
819.2 During handling of the above exception, another exception occurred:
819.2 
819.2 Traceback (most recent call last):
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_internal/cli/base_command.py", line 106, in _run_wrapper
819.2     status = _inner_run()
819.2              ^^^^^^^^^^^^
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_internal/cli/base_command.py", line 97, in _inner_run
819.2     return self.run(options, args)
819.2            ^^^^^^^^^^^^^^^^^^^^^^^
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_internal/cli/req_command.py", line 67, in wrapper
819.2     return func(self, options, args)
819.2            ^^^^^^^^^^^^^^^^^^^^^^^^^
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_internal/commands/install.py", line 386, in run
819.2     requirement_set = resolver.resolve(
819.2                       ^^^^^^^^^^^^^^^^^
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_internal/resolution/resolvelib/resolver.py", line 179, in resolve
819.2     self.factory.preparer.prepare_linked_requirements_more(reqs)
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_internal/operations/prepare.py", line 554, in prepare_linked_requirements_more
819.2     self._complete_partial_requirements(
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_internal/operations/prepare.py", line 469, in _complete_partial_requirements
819.2     for link, (filepath, _) in batch_download:
819.2                                ^^^^^^^^^^^^^^
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_internal/network/download.py", line 184, in __call__
819.2     for chunk in chunks:
819.2                  ^^^^^^
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_internal/network/utils.py", line 65, in response_chunks
819.2     for chunk in response.raw.stream(
819.2                  ^^^^^^^^^^^^^^^^^^^^
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_vendor/urllib3/response.py", line 622, in stream
819.2     data = self.read(amt=amt, decode_content=decode_content)
819.2            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_vendor/urllib3/response.py", line 560, in read
819.2     with self._error_catcher():
819.2          ^^^^^^^^^^^^^^^^^^^^^
819.2   File "/usr/local/lib/python3.12/contextlib.py", line 158, in __exit__
819.2     self.gen.throw(value)
819.2   File "/usr/local/lib/python3.12/site-packages/pip/_vendor/urllib3/response.py", line 443, in _error_catcher
819.2     raise ReadTimeoutError(self._pool, None, "Read timed out.")
819.2 pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.
------
[+] build 0/98
 ⠙ Image msjarvis-rebuild-jarvis-20llm-production            Building  1537.0s
 ⠙ Image msjarvis-rebuild-jarvis-spiritual-rag               Building  1537.0s
 ⠙ Image msjarvis-rebuild-jarvis-dgm-bridge-03               Building  1537.0s
 ⠙ Image msjarvis-rebuild-jarvis-dgm-bridge-17               Building  1537.0s
 ⠙ Image msjarvis-rebuild-nbb_pituitary_gland                Building  1537.0s
 ⠙ Image msjarvis-rebuild-nbb_woah_algorithms                Building  1537.0s
 ⠙ Image msjarvis-rebuild-jarvis-wv-entangled-gateway        Building  1537.0s
 ⠙ Image msjarvis-toroidal:latest                            Building  1537.0s
 ⠙ Image msjarvis-rebuild-jarvis-judge-truth                 Building  1537.0s
 ⠙ Image msjarvis-rebuild-jarvis-brain-orchestrator          Building  1537.0s
 ⠙ Image msjarvis-rebuild-llm6-proxy                         Building  1537.0s
 ⠙ Image msjarvis-rebuild-jarvis-judge-ethics                Building  1537.0s
 ⠙ Image msjarvis-rebuild-jarvis-judge-alignment             Building  1537.0s
 ⠙ Image msjarvis-rebuild-nbb_spiritual_maternal_integration Building  1537.0s
 ⠙ Image msjarvis-rebuild-psychological_rag_domain           Building  1537.0s
 ⠙ Image msjarvis-rebuild-jarvis-gis-rag                     Building  1537.0s
 ⠙ Image msjarvis-rebuild-llm1-proxy                         Building  1537.0s
 ⠙ Image msjarvis-rebuild-llm16-proxy                        Building  1537.0s
 ⠙ Image msjarvis-rebuild-jarvis-rag-server                  Building  1537.0s
 ⠙ Image msjarvis-rebuild-jarvis-semaphore                   Building  1537.0s
 ⠙ Image msjarvis-rebuild-jarvis-dgm-bridge-05               Building  1537.0s
 ... 77 more                                                                  
Dockerfile.bridge:4

--------------------

   2 |     WORKDIR /app/services

   3 |     COPY requirements.txt .

   4 | >>> RUN pip install --no-cache-dir -r requirements.txt

   5 |     COPY . /app/services/

   6 |     CMD ["python3", "bridge_cross_dgm_10001.py"]

--------------------

target jarvis-dgm-bridge-12: failed to solve: process "/bin/sh -c pip install --no-cache-dir -r requirements.txt" did not complete successfully: exit code: 2

[+] up 106/106
 ✔ Container llm2-proxy                                          Started 23.8s
 ✔ Container llm7-proxy                                          Started 28.2s
 ✔ Container jarvis-fifth-dgm                                    Started 28.1s
 ✔ Container msjarvis-rebuild-nbb_consciousness_containers-1     Started 23.4s
 ✔ Container llm11-proxy                                         Started 23.6s
 ✔ Container nbb-i-containers                                    Started 26.0s
 ✔ Container msjarvis-rebuild-nbb_subconscious-1                 Started 24.2s
 ✔ Container psychological_rag_domain                            Started 23.8s
 ✔ Container llm12-proxy                                         Started 24.9s
 ✔ Container llm1-proxy                                          Started 23.9s
 ✔ Container jarvis-ollama                                       Started 33.5s
 ✔ Container msjarvis-rebuild-nbb_woah_algorithms-1              Started 26.0s
 ✔ Container msjarvis-rebuild-nbb_heteroglobulin_transport-1     Started 24.6s
 ✔ Container llm3-proxy                                          Started 23.2s
 ✔ Container llm10-proxy                                         Started 23.7s
 ✔ Container llm15-proxy                                         Started 24.6s
 ✔ Container jarvis-temporal-consciousness                       Started 23.2s
 ✔ Container msjarvis-rebuild-nbb_pituitary_gland-1              Started 26.9s
 ✔ Container msjarvis-rebuild-nbb_spiritual_maternal_integrat... Started 23.5s
 ✔ Container msjarvis-rebuild-nbb_mother_carrie_protocols-1      Started 26.8s
 ✔ Container jarvis-judge-consistency                            Started 24.7s
 ... 85 more                                                                  
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

