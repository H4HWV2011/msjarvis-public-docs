(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ tail -30 /opt/msjarvis-rebuild/neurobiological_brain/darwin_godel_machines/service/dgm_service.py
            )
            os.unlink(patch_file)
            if result.returncode != 0:
                return JSONResponse(status_code=422, content={
                    "status": "patch_failed",
                    "stderr": result.stderr,
                    "stdout": result.stdout
                })
            with open(host_path, "rb") as f:
                new_hash = hashlib.sha256(f.read()).hexdigest()[:12]
        else:
            return JSONResponse(status_code=400, content={
                "status": "rejected", "reason": "unknown_patch_type"
            })
    except Exception as e:
        return JSONResponse(status_code=500, content={
            "status": "error", "detail": str(e)
        })

    return {
        "status": "applied",
        "container": req.target_container,
        "file_path": req.file_path,
        "host_path": host_path,
        "agent": req.dgm_agent,
        "orig_hash": orig_hash,
        "new_hash": new_hash,
        "backup": backup_path,
        "note": "file written to bind-mounted path — live in container immediately"
    }
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild/neurobiological_brain/darwin_godel_machines
docker compose up -d --build
[+] Building 3654.9s (523/523) FINISHED                                       
 => [internal] load local bake definitions                               0.0s
 => => reading from stdin 37.87kB                                        0.0s
 => [jarvis-judge-ethics internal] load build definition from Dockerfil  0.1s
 => => transferring dockerfile: 407B                                     0.0s
 => [llm8-proxy internal] load build definition from Dockerfile-llm8-pr  0.1s
 => => transferring dockerfile: 259B                                     0.0s
 => [nbb_heteroglobulin_transport internal] load build definition from   0.7s
 => => transferring dockerfile: 747B                                     0.0s
 => [llm6-proxy internal] load build definition from Dockerfile-llm6-pr  1.9s
 => => transferring dockerfile: 259B                                     0.0s
 => [jarvis-eeg-beta internal] load build definition from Dockerfile.ee  2.0s
 => => transferring dockerfile: 530B                                     0.0s
 => [nbb_blood_brain_barrier internal] load build definition from Docke  0.8s
 => => transferring dockerfile: 588B                                     0.0s
 => [jarvis-unified-gateway internal] load build definition from Docker  1.9s
 => => transferring dockerfile: 319B                                     0.0s
 => [nbb_qualia_engine internal] load build definition from Dockerfile   0.1s 
 => => transferring dockerfile: 233B                                     0.0s 
 => [llm16-proxy internal] load build definition from Dockerfile-llm16-  2.0s 
 => => transferring dockerfile: 262B                                     0.0s 
 => [llm11-proxy internal] load build definition from Dockerfile-llm11-  0.1s 
 => => transferring dockerfile: 262B                                     0.0s 
 => [jarvis-constitutional-guardian internal] load build definition fro  2.0s
 => => transferring dockerfile: 504B                                     0.0s
 => [jarvis-woah internal] load build definition from Dockerfile.woah    1.9s
 => => transferring dockerfile: 386B                                     0.0s
 => [jarvis-toroidal internal] load build definition from Dockerfile.to  0.2s
 => => transferring dockerfile: 659B                                     0.0s
 => [llm14-proxy internal] load build definition from Dockerfile-llm14-  2.0s
 => => transferring dockerfile: 262B                                     0.0s
 => [nbb_spiritual_root internal] load build definition from Dockerfile  0.2s
 => => transferring dockerfile: 617B                                     0.0s
 => [jarvis-agents-service internal] load build definition from Dockerf  1.7s
 => => transferring dockerfile: 289B                                     0.0s
 => [jarvis-brain-orchestrator internal] load build definition from Doc  2.0s
 => => transferring dockerfile: 614B                                     0.0s
 => [llm9-proxy internal] load build definition from Dockerfile-llm9-pr  2.3s
 => => transferring dockerfile: 259B                                     0.0s
 => [llm21-proxy internal] load build definition from Dockerfile-llm21-  2.2s
 => => transferring dockerfile: 262B                                     0.0s
 => [jarvis-psychology-services internal] load build definition from Do  2.0s
 => => transferring dockerfile: 320B                                     0.0s
 => [jarvis-fifth-dgm internal] load build definition from Dockerfile.f  2.3s
 => => transferring dockerfile: 717B                                     0.0s
 => [psychological_rag_domain internal] load build definition from Dock  2.2s
 => => transferring dockerfile: 267B                                     0.0s
 => [jarvis-aaacpe-rag internal] load build definition from Dockerfile.  2.0s
 => => transferring dockerfile: 409B                                     0.0s
 => [jarvis-swarm-intelligence internal] load build definition from Doc  2.1s
 => => transferring dockerfile: 292B                                     0.0s
 => [jarvis-main-brain internal] load build definition from Dockerfile   0.2s
 => => transferring dockerfile: 590B                                     0.0s
 => [llm15-proxy internal] load build definition from Dockerfile-llm15-  2.1s
 => => transferring dockerfile: 262B                                     0.0s
 => [jarvis-69dgm-bridge internal] load build definition from Dockerfil  2.2s
 => => transferring dockerfile: 367B                                     0.0s
 => [jarvis-semaphore internal] load build definition from Dockerfile.s  2.3s
 => => transferring dockerfile: 484B                                     0.0s
 => [nbb_prefrontal_cortex internal] load build definition from Dockerf  1.4s
 => => transferring dockerfile: 860B                                     0.0s
 => [jarvis-web-research internal] load build definition from Dockerfil  2.2s
 => => transferring dockerfile: 474B                                     0.0s
 => [nbb_darwin_godel_machines internal] load build definition from Doc  1.4s
 => => transferring dockerfile: 245B                                     0.0s
 => [nbb_mother_carrie_protocols internal] load build definition from D  1.3s
 => => transferring dockerfile: 747B                                     0.0s
 => [nbb_spiritual_maternal_integration internal] load build definition  1.1s
 => => transferring dockerfile: 747B                                     0.0s
 => [nbb-i-containers internal] load build definition from Dockerfile.n  1.7s
 => => transferring dockerfile: 672B                                     0.0s
 => [nbb_subconscious internal] load build definition from Dockerfile    0.9s
 => => transferring dockerfile: 617B                                     0.0s
 => [jarvis-temporal-consciousness internal] load build definition from  1.8s
 => => transferring dockerfile: 387B                                     0.0s
 => [llm4-proxy internal] load build definition from Dockerfile-llm4-pr  2.2s
 => => transferring dockerfile: 259B                                     0.0s
 => [llm13-proxy internal] load build definition from Dockerfile-llm13-  2.2s
 => => transferring dockerfile: 262B                                     0.0s
 => [jarvis-i-containers internal] load build definition from Dockerfil  2.0s
 => => transferring dockerfile: 663B                                     0.0s
 => [llm18-proxy internal] load build definition from Dockerfile-llm18-  2.3s
 => => transferring dockerfile: 262B                                     0.0s
 => [jarvis-rag-server internal] load build definition from Dockerfile.  2.1s
 => => transferring dockerfile: 335B                                     0.0s
 => [llm1-proxy internal] load build definition from Dockerfile-llm1-pr  2.1s
 => => transferring dockerfile: 259B                                     0.0s
 => [llm5-proxy internal] load build definition from Dockerfile-llm5-pr  2.1s
 => => transferring dockerfile: 259B                                     0.0s
 => [jarvis-spiritual-rag internal] load build definition from Dockerfi  2.2s
 => => transferring dockerfile: 248B                                     0.0s
 => [llm17-proxy internal] load build definition from Dockerfile-llm17-  2.1s
 => => transferring dockerfile: 262B                                     0.0s
 => [llm12-proxy internal] load build definition from Dockerfile-llm12-  1.5s
 => => transferring dockerfile: 262B                                     0.0s
 => [jarvis-hippocampus internal] load build definition from Dockerfile  2.2s
 => => transferring dockerfile: 540B                                     0.0s
 => [jarvis-blood-brain-barrier internal] load build definition from Do  1.8s
 => => transferring dockerfile: 277B                                     0.0s
 => [nbb_pituitary_gland internal] load build definition from Dockerfil  1.8s
 => => transferring dockerfile: 701B                                     0.0s
 => [jarvis-local-resources internal] load build definition from Docker  1.7s
 => => transferring dockerfile: 336B                                     0.0s
 => [llm2-proxy internal] load build definition from Dockerfile-llm2-pr  2.2s
 => => transferring dockerfile: 259B                                     0.0s
 => [nbb_woah_algorithms internal] load build definition from Dockerfil  1.0s
 => => transferring dockerfile: 473B                                     0.0s
 => [jarvis-consciousness-bridge internal] load build definition from D  1.9s
 => => transferring dockerfile: 284B                                     0.0s
 => [jarvis-fractal-consciousness internal] load build definition from   1.8s
 => => transferring dockerfile: 549B                                     0.0s
 => [llm19-proxy internal] load build definition from Dockerfile-llm19-  1.8s
 => => transferring dockerfile: 262B                                     0.0s
 => [llm22-proxy internal] load build definition from Dockerfile-llm22-  1.8s
 => => transferring dockerfile: 262B                                     0.0s
 => [llm20-proxy internal] load build definition from Dockerfile-llm20-  2.3s
 => => transferring dockerfile: 262B                                     0.0s
 => [jarvis-lm-synthesizer internal] load build definition from Dockerf  1.8s
 => => transferring dockerfile: 433B                                     0.0s
 => [jarvis-qualia-engine internal] load build definition from Dockerfi  2.1s
 => => transferring dockerfile: 1.25kB                                   0.0s
 => [llm3-proxy internal] load build definition from Dockerfile-llm3-pr  1.8s
 => => transferring dockerfile: 259B                                     0.0s
 => [jarvis-neurobiological-master internal] load build definition from  2.2s
 => => transferring dockerfile: 539B                                     0.0s
 => [jarvis-mother-protocols internal] load build definition from Docke  2.1s
 => => transferring dockerfile: 339B                                     0.0s
 => [nbb_consciousness_containers internal] load build definition from   1.9s
 => => transferring dockerfile: 617B                                     0.0s
 => [llm10-proxy internal] load build definition from Dockerfile-llm10-  1.9s
 => => transferring dockerfile: 262B                                     0.0s
 => [llm7-proxy internal] load build definition from Dockerfile-llm7-pr  1.2s
 => => transferring dockerfile: 259B                                     0.0s
 => [jarvis-gis-rag internal] load build definition from Dockerfile.gis  1.9s
 => => transferring dockerfile: 341B                                     0.0s
 => [llm9-proxy internal] load metadata for docker.io/library/python:3.  2.2s
 => [jarvis-fifth-dgm internal] load metadata for docker.io/library/pyt  1.7s
 => [jarvis-brain-orchestrator internal] load metadata for docker.io/li  1.2s
 => [nbb_pituitary_gland internal] load metadata for docker.io/tiangolo  1.7s
 => [jarvis-semaphore internal] load .dockerignore                       1.4s
 => => transferring context: 146B                                        0.0s
 => [nbb_qualia_engine internal] load .dockerignore                      1.3s
 => => transferring context: 2B                                          0.0s
 => [nbb_blood_brain_barrier internal] load .dockerignore                1.5s
 => => transferring context: 2B                                          0.0s
 => [jarvis-unified-gateway internal] load .dockerignore                 1.6s
 => => transferring context: 848B                                        0.0s
 => [nbb_woah_algorithms internal] load .dockerignore                    1.5s
 => => transferring context: 2B                                          0.0s
 => [nbb_darwin_godel_machines internal] load .dockerignore              1.2s
 => => transferring context: 2B                                          0.0s
 => [nbb_spiritual_root internal] load .dockerignore                     1.1s
 => => transferring context: 2B                                          0.0s
 => [nbb_subconscious internal] load .dockerignore                       1.0s
 => => transferring context: 2B                                          0.0s
 => [nbb_spiritual_maternal_integration internal] load .dockerignore     1.0s
 => => transferring context: 2B                                          0.0s
 => [nbb_prefrontal_cortex internal] load .dockerignore                  1.0s
 => => transferring context: 2B                                          0.0s
 => [nbb_heteroglobulin_transport internal] load .dockerignore           1.0s
 => => transferring context: 2B                                          0.0s
 => [nbb_mother_carrie_protocols internal] load .dockerignore            1.0s
 => => transferring context: 2B                                          0.0s
 => [jarvis-unified-gateway internal] load metadata for docker.io/libra  1.7s
 => [nbb_pituitary_gland internal] load .dockerignore                    0.8s
 => => transferring context: 2B                                          0.0s
 => [nbb_consciousness_containers internal] load .dockerignore           0.7s
 => => transferring context: 2B                                          0.0s
 => [llm21-proxy 1/4] FROM docker.io/library/python:3.12-slim@sha256:09  0.0s
 => [nbb_qualia_engine internal] load build context                      0.3s
 => => transferring context: 8.77kB                                      0.0s
 => [llm12-proxy internal] load build context                            0.4s
 => => transferring context: 1.65kB                                      0.0s
 => CACHED [llm21-proxy 2/4] WORKDIR /app                                0.1s
 => CACHED [jarvis-fifth-dgm 1/5] FROM docker.io/library/python:3.11-sl  0.0s
 => [jarvis-judge-ethics internal] load build context                    2.5s
 => => transferring context: 122.26kB                                    1.1s
 => CACHED [jarvis-fifth-dgm 2/5] WORKDIR /app                           0.0s
 => [llm19-proxy internal] load build context                            1.9s
 => => transferring context: 1.80kB                                      0.8s
 => [jarvis-swarm-intelligence internal] load build context             77.5s
 => => transferring context: 5.06GB                                     76.1s
 => [jarvis-spiritual-rag internal] load build context                   1.5s
 => => transferring context: 5.81kB                                      0.0s
 => [nbb_qualia_engine 3/4] COPY . /app                                  0.1s
 => [jarvis-i-containers internal] load build context                    1.9s
 => => transferring context: 124.74kB                                    0.0s
 => [jarvis-temporal-consciousness internal] load build context          1.8s
 => => transferring context: 712B                                        0.0s
 => [jarvis-lm-synthesizer internal] load build context                  1.8s
 => => transferring context: 4.56kB                                      0.0s
 => [jarvis-toroidal internal] load build context                        1.4s
 => => transferring context: 3.83kB                                      0.0s
 => [llm6-proxy internal] load build context                             1.9s
 => => transferring context: 1.63kB                                      0.0s
 => [jarvis-gis-rag internal] load build context                         2.2s
 => => transferring context: 14.52kB                                     0.1s
 => [jarvis-constitutional-guardian internal] load build context         2.2s
 => => transferring context: 15.11kB                                     0.0s
 => [jarvis-web-research internal] load build context                    1.4s
 => => transferring context: 113.44kB                                    0.0s
 => [llm8-proxy internal] load build context                             1.9s
 => => transferring context: 1.64kB                                      0.0s
 => [nbb_heteroglobulin_transport internal] load build context           2.1s
 => => transferring context: 33.74kB                                     0.0s
 => [jarvis-qualia-engine internal] load build context                 185.4s
 => => transferring context: 29.93GB                                   183.7s
 => [jarvis-aaacpe-rag internal] load build context                      2.1s
 => => transferring context: 5.40kB                                      0.0s
 => [llm22-proxy internal] load build context                            2.0s
 => => transferring context: 2.13kB                                      0.0s
 => [llm12-proxy 3/4] COPY llm12_health_proxy.py .                       0.5s
 => [jarvis-brain-orchestrator internal] load build context             79.8s
 => => transferring context: 5.06GB                                     79.6s
 => [llm14-proxy internal] load build context                            2.1s
 => => transferring context: 1.80kB                                      0.0s
 => [jarvis-local-resources internal] load build context                 2.1s
 => => transferring context: 3.52kB                                      0.1s
 => [llm11-proxy internal] load build context                            2.0s
 => => transferring context: 1.61kB                                      0.0s
 => [jarvis-main-brain internal] load build context                     76.0s
 => => transferring context: 5.06GB                                     74.9s
 => [nbb_spiritual_maternal_integration internal] load build context     2.2s
 => => transferring context: 43.22kB                                     0.0s
 => [llm16-proxy internal] load build context                            2.0s
 => => transferring context: 1.65kB                                      0.0s
 => CACHED [jarvis-main-brain 1/4] FROM docker.io/library/python:3.10-s  0.9s
 => => resolve docker.io/library/python:3.10-slim@sha256:70f65c721aaddf  0.9s
 => [jarvis-psychology-services internal] load build context             2.2s
 => => transferring context: 10.40kB                                     0.1s
 => [llm10-proxy internal] load build context                            2.1s
 => => transferring context: 1.80kB                                      0.0s
 => [nbb_mother_carrie_protocols internal] load build context            2.2s
 => => transferring context: 40.70kB                                     0.0s
 => [nbb_prefrontal_cortex internal] load build context                  2.1s
 => => transferring context: 32.97kB                                     0.0s
 => [llm7-proxy internal] load build context                             2.0s
 => => transferring context: 1.64kB                                      0.0s
 => [llm3-proxy internal] load build context                             1.7s
 => => transferring context: 1.82kB                                      0.0s
 => [llm1-proxy internal] load build context                             1.9s
 => => transferring context: 1.64kB                                      0.0s
 => [jarvis-eeg-beta internal] load build context                        2.2s
 => => transferring context: 22.44kB                                     0.0s
 => [jarvis-judge-ethics 3/5] RUN pip install --no-cache-dir     fast  195.3s
 => [nbb_woah_algorithms internal] load build context                    2.2s
 => => transferring context: 28.94kB                                     0.0s
 => [nbb_blood_brain_barrier internal] load build context                2.2s
 => => transferring context: 5.23kB                                      0.0s
 => [nbb_pituitary_gland internal] load build context                    1.3s
 => => transferring context: 45.38kB                                     0.0s
 => [nbb_spiritual_root internal] load build context                     1.3s
 => => transferring context: 37.47kB                                     0.0s
 => [nbb_consciousness_containers internal] load build context           1.4s
 => => transferring context: 30.44kB                                     0.0s
 => [nbb_subconscious internal] load build context                       1.3s
 => => transferring context: 25.81kB                                     0.0s
 => [nbb_subconscious 1/8] FROM docker.io/tiangolo/uvicorn-gunicorn-fas  3.0s
 => => resolve docker.io/tiangolo/uvicorn-gunicorn-fastapi:python3.10-s  0.9s
 => => sha256:244b6c0a6b5003d7e4e07c0ee5ae9a49aa44686b6 1.61kB / 1.61kB  0.0s
 => => sha256:e5381bb9a177b6e4cede28d6d463d32ad67bcb7be 3.32kB / 3.32kB  0.0s
 => => sha256:297998286420f19c8bbdcba1c60e204c891be25a9 9.17kB / 9.17kB  0.0s
 => [jarvis-toroidal 3/7] RUN apt-get update && apt-get install -y --  260.8s
 => [jarvis-i-containers 3/6] RUN pip install --no-cache-dir fastapi   195.4s
 => [jarvis-rag-server internal] load build context                      2.2s
 => => transferring context: 6.22kB                                      0.0s
 => [llm20-proxy internal] load build context                            2.2s
 => => transferring context: 1.62kB                                      0.0s
 => [nbb_darwin_godel_machines internal] load build context              1.7s
 => => transferring context: 26.30kB                                     0.0s
 => [llm9-proxy internal] load build context                             2.2s
 => => transferring context: 1.66kB                                      0.0s
 => [jarvis-eeg-theta 3/8] RUN pip install --no-cache-dir     fastapi  516.1s
 => [llm2-proxy internal] load build context                             2.2s
 => => transferring context: 1.62kB                                      0.0s
 => [llm4-proxy internal] load build context                             2.2s
 => => transferring context: 1.64kB                                      0.0s
 => [jarvis-mother-protocols internal] load build context                2.2s
 => => transferring context: 934B                                        0.0s
 => [llm13-proxy internal] load build context                            2.2s
 => => transferring context: 1.82kB                                      0.0s
 => [llm15-proxy internal] load build context                            1.0s
 => => transferring context: 1.80kB                                      0.0s
 => [jarvis-semaphore internal] load build context                       0.8s
 => => transferring context: 2.64kB                                      0.0s
 => [llm5-proxy internal] load build context                             1.8s
 => => transferring context: 1.80kB                                      0.0s
 => [jarvis-69dgm-bridge internal] load build context                    2.1s
 => => transferring context: 4.45kB                                      0.0s
 => [psychological_rag_domain internal] load build context               2.1s
 => => transferring context: 7.06kB                                      0.0s
 => [jarvis-rag-server 2/5] WORKDIR /app/services                        2.0s
 => [llm17-proxy internal] load build context                            2.2s
 => => transferring context: 1.65kB                                      0.0s
 => [jarvis-neurobiological-master internal] load build context         79.9s
 => => transferring context: 5.06GB                                     78.2s
 => [jarvis-hippocampus internal] load build context                     2.3s
 => => transferring context: 7.44kB                                      0.0s
 => [llm18-proxy internal] load build context                            2.3s
 => => transferring context: 1.82kB                                      0.0s
 => [llm21-proxy internal] load build context                            2.2s
 => => transferring context: 1.82kB                                      0.0s
 => [jarvis-fifth-dgm internal] load build context                       2.3s
 => => transferring context: 39.51kB                                     0.0s
 => [jarvis-hippocampus 3/5] RUN apt-get update && apt-get install -y  260.7s
 => [nbb_qualia_engine 4/4] RUN pip install --no-cache-dir fastapi uv  196.6s
 => [llm12-proxy 4/4] RUN pip install fastapi uvicorn httpx            195.4s
 => [jarvis-unified-gateway 1/5] FROM docker.io/library/python:3.10@sha  1.8s
 => => resolve docker.io/library/python:3.10@sha256:b6c2f85994c8d67e2d4  0.1s
 => => sha256:b6c2f85994c8d67e2d459a804ab80584471a23a 10.32kB / 10.32kB  0.0s
 => => sha256:54d6eadc673239926a3b41c2d36aeed40dc067aea 2.32kB / 2.32kB  0.0s
 => => sha256:f3a3230a07824d169b7426a01a2a759c0016e9733 6.35kB / 6.35kB  0.0s
 => [jarvis-unified-gateway internal] load build context                79.5s
 => => transferring context: 5.06GB                                     79.3s
 => [llm11-proxy 3/4] COPY llm11_health_proxy.py .                       1.0s
 => [llm22-proxy 3/4] COPY llm22_health_proxy.py .                       0.9s
 => [llm15-proxy 3/4] COPY llm15_health_proxy.py .                       0.9s
 => [llm16-proxy 3/4] COPY llm16_health_proxy.py .                       0.9s
 => [llm14-proxy 3/4] COPY llm14_health_proxy.py .                       0.9s
 => [llm10-proxy 3/4] COPY llm10_health_proxy.py .                       1.0s
 => [jarvis-temporal-consciousness 3/5] COPY requirements_temporal.txt   0.9s
 => [llm1-proxy 3/4] COPY llm1_health_proxy.py .                         1.0s
 => [jarvis-rag-server 3/4] RUN pip install --no-cache-dir fastapi u  3254.6s
 => [llm8-proxy 3/4] COPY llm8_health_proxy.py .                         1.0s
 => [llm6-proxy 3/4] COPY llm6_health_proxy.py .                         1.0s
 => [psychological_rag_domain 3/4] COPY psychological_rag_domain.py .    1.0s
 => CACHED [jarvis-wv-entangled-gateway 2/4] WORKDIR /app                0.0s
 => CACHED [jarvis-spiritual-rag 3/4] RUN pip install --no-cache-dir fa  0.0s
 => CACHED [jarvis-spiritual-rag 4/4] COPY spiritual_rag_domain.py /app  0.0s
 => [llm3-proxy 3/4] COPY llm3_health_proxy.py .                         0.9s
 => [llm5-proxy 3/4] COPY llm5_health_proxy.py .                         1.0s
 => [llm19-proxy 3/4] COPY llm19_health_proxy.py .                       0.9s
 => [llm20-proxy 3/4] COPY llm20_health_proxy.py .                       1.0s
 => [llm2-proxy 3/4] COPY llm2_health_proxy.py .                         1.0s
 => [llm9-proxy 3/4] COPY llm9_health_proxy.py .                         1.0s
 => [llm17-proxy 3/4] COPY llm17_health_proxy.py .                       1.0s
 => [jarvis-psychology-services 3/5] COPY psychology_integration_adapte  1.0s
 => CACHED [jarvis-consciousness-bridge stage-0 3/5] COPY requirements.  0.0s
 => [llm13-proxy 3/4] COPY llm13_health_proxy.py .                       1.0s
 => [llm7-proxy 3/4] COPY llm7_health_proxy.py .                         1.0s
 => [jarvis-local-resources 3/4] COPY services/local_resources_resolver  1.0s
 => [llm4-proxy 3/4] COPY llm4_health_proxy.py .                         1.0s
 => [llm21-proxy 3/4] COPY llm21_health_proxy.py .                       1.0s
 => [llm18-proxy 3/4] COPY llm18_health_proxy.py .                       1.0s
 => [nbb_darwin_godel_machines 3/4] COPY . /app                          1.0s
 => [jarvis-spiritual-rag] exporting to image                            0.2s
 => => exporting layers                                                  0.0s
 => => writing image sha256:ee9eec3dc3b52a00f25cd47b9d9a2cf7fb7f14d47aa  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-spiritual-ra  0.0s
 => CACHED [jarvis-mother-protocols 3/5] COPY ../requirements.txt /app/  0.0s
 => CACHED [jarvis-mother-protocols 4/5] RUN pip install --no-cache-dir  0.0s
 => CACHED [jarvis-mother-protocols 5/5] COPY mother_protocols.py /app/  0.0s
 => CACHED [jarvis-69dgm-bridge 3/6] COPY ../requirements.txt /app/requ  0.0s
 => CACHED [jarvis-69dgm-bridge 4/6] RUN pip install --no-cache-dir -r   0.0s
 => CACHED [jarvis-69dgm-bridge 5/6] COPY bridge_69dgm.py /app/bridge_6  0.0s
 => CACHED [jarvis-69dgm-bridge 6/6] COPY chroma_client.py /app/chroma_  0.0s
 => [jarvis-fractal-consciousness 3/7] COPY web_research_requirements.t  0.2s
 => [jarvis-mother-protocols] exporting to image                         0.0s
 => => exporting layers                                                  0.0s
 => => writing image sha256:4f7d6fbee017861a514e06f464bd568d244c3960d62  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-mother-proto  0.0s
 => [jarvis-lm-synthesizer stage-0 4/5] RUN --mount=type=cache,targe  1096.3s
 => [jarvis-69dgm-bridge] exporting to image                             0.3s
 => => exporting layers                                                  0.0s
 => => writing image sha256:68876f6a0dbcadfc4faa3195a2e9a85557a85e2bf38  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-69dgm-bridge  0.0s
 => [nbb_woah_algorithms 3/6] COPY . /app                                1.3s
 => CACHED [jarvis-gis-rag 3/5] COPY services/gis_rag_service.py /app/g  0.0s
 => CACHED [jarvis-gis-rag 4/5] COPY gis_service /app/gis_service        0.0s
 => CACHED [jarvis-gis-rag 5/5] RUN pip install --no-cache-dir fastapi   0.0s
 => [jarvis-aaacpe-rag 3/5] RUN pip install --no-cache-dir     fastap  513.9s
 => [llm14-proxy 4/4] RUN pip install fastapi uvicorn httpx            194.1s
 => [llm22-proxy 4/4] RUN pip install fastapi uvicorn httpx            193.6s
 => [llm19-proxy 4/4] RUN pip install fastapi uvicorn httpx            192.3s
 => [llm3-proxy 4/4] RUN pip install fastapi uvicorn httpx             192.2s
 => [llm15-proxy 4/4] RUN pip install fastapi uvicorn httpx            193.4s
 => CACHED [jarvis-fifth-dgm 3/9] RUN apt-get update && apt-get install  0.0s
 => CACHED [jarvis-fifth-dgm 4/9] COPY requirements.txt /app/requiremen  0.0s
 => CACHED [jarvis-fifth-dgm 5/9] RUN pip install --no-cache-dir -r /ap  0.0s
 => CACHED [jarvis-fifth-dgm 6/9] COPY ms_jarvis_fifth_dgm_orchestrator  0.0s
 => CACHED [jarvis-fifth-dgm 7/9] COPY dynamic_port_service.py /app/dyn  0.0s
 => CACHED [jarvis-fifth-dgm 8/9] COPY fifth_dgm_integration.py /app/fi  0.0s
 => CACHED [jarvis-fifth-dgm 9/9] COPY service_discovery.py /app/servic  0.0s
 => [llm16-proxy 4/4] RUN pip install fastapi uvicorn httpx            192.3s
 => [jarvis-temporal-consciousness 4/5] RUN pip install --no-cache-di  193.3s
 => [llm11-proxy 4/4] RUN pip install fastapi uvicorn httpx            193.2s
 => [llm6-proxy 4/4] RUN pip install fastapi uvicorn httpx             192.4s
 => [psychological_rag_domain 4/4] RUN pip install --no-cache-dir fas  513.8s
 => [llm5-proxy 4/4] RUN pip install fastapi uvicorn httpx             192.2s
 => [llm7-proxy 4/4] RUN pip install fastapi uvicorn httpx             193.0s
 => [llm1-proxy 4/4] RUN pip install fastapi uvicorn httpx             194.3s
 => [llm10-proxy 4/4] RUN pip install fastapi uvicorn httpx            192.4s
 => [llm8-proxy 4/4] RUN pip install fastapi uvicorn httpx             193.0s
 => [jarvis-psychology-services 4/5] COPY psychology_server.py .         1.4s
 => [llm20-proxy 4/4] RUN pip install fastapi uvicorn httpx            194.2s
 => [nbb_blood_brain_barrier 3/7] COPY . /app                            1.3s
 => [llm9-proxy 4/4] RUN pip install fastapi uvicorn httpx             192.9s
 => [jarvis-constitutional-guardian 3/5] COPY requirements.txt /app/req  1.3s
 => [llm4-proxy 4/4] RUN pip install fastapi uvicorn httpx             192.1s
 => [llm13-proxy 4/4] RUN pip install fastapi uvicorn httpx            192.9s
 => [jarvis-local-resources 4/4] RUN pip install --no-cache-dir fasta  192.8s
 => [llm2-proxy 4/4] RUN pip install fastapi uvicorn httpx             193.5s
 => [llm18-proxy 4/4] RUN pip install fastapi uvicorn httpx            193.7s
 => [nbb_darwin_godel_machines 4/4] RUN pip install --no-cache-dir fa  193.2s
 => [jarvis-woah 2/5] WORKDIR /app/services                              1.3s
 => [llm17-proxy 4/4] RUN pip install fastapi uvicorn httpx            192.7s
 => [jarvis-wv-entangled-gateway 3/7] RUN apt-get update && apt-get i  193.9s
 => [llm21-proxy 4/4] RUN pip install fastapi uvicorn httpx            192.2s
 => [jarvis-web-research 4/7] RUN pip install --no-cache-dir -r /app/  257.4s
 => [jarvis-gis-rag] exporting to image                                  0.4s
 => => exporting layers                                                  0.0s
 => => writing image sha256:6bab4451da5ac804d45d6455ed0b04ec78c7a6386d9  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-gis-rag       0.0s
 => [jarvis-fifth-dgm] exporting to image                                0.4s
 => => exporting layers                                                  0.0s
 => => writing image sha256:fa9cc3db97b68125420c8eeb009e4c567f9c7e3cc3d  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-fifth-dgm     0.0s
 => [jarvis-spiritual-rag] resolving provenance for metadata file        0.0s
 => [jarvis-mother-protocols] resolving provenance for metadata file     0.0s
 => [jarvis-69dgm-bridge] resolving provenance for metadata file         0.0s
 => [nbb_woah_algorithms 4/6] RUN pip install --no-cache-dir -r requi  255.8s
 => [nbb_blood_brain_barrier 4/7] RUN pip install --no-cache-dir fast  191.4s
 => [jarvis-20llm-production 3/5] RUN apt-get update && apt-get insta  512.7s
 => [jarvis-woah 3/5] RUN apt-get update && apt-get install -y --no-i  192.7s
 => [jarvis-constitutional-guardian 4/5] RUN pip install --no-cache-  3445.1s
 => [jarvis-psychology-services 5/5] RUN pip install --no-cache-dir f  191.3s
 => [jarvis-unified-gateway 2/5] WORKDIR /app/services                   0.3s
 => [jarvis-gis-rag] resolving provenance for metadata file              0.0s
 => [jarvis-fifth-dgm] resolving provenance for metadata file            0.0s
 => [nbb_subconscious 2/8] WORKDIR /app                                  0.2s
 => [nbb_consciousness_containers 3/8] COPY . /app                       0.4s
 => [nbb_heteroglobulin_transport 3/8] COPY . /app                       0.2s
 => [nbb_subconscious 3/8] COPY . /app                                   0.3s
 => [nbb_spiritual_root 3/8] COPY . /app                                 0.4s
 => [nbb_mother_carrie_protocols 3/8] COPY . /app                        0.5s
 => [nbb_prefrontal_cortex 3/8] COPY . /app                              0.3s
 => [nbb_pituitary_gland 3/8] COPY . /app                                0.4s
 => [nbb_spiritual_maternal_integration 3/8] COPY . /app                 0.3s
 => [nbb_heteroglobulin_transport 4/8] RUN pip install --no-cache-dir  190.4s
 => [nbb_prefrontal_cortex 4/8] RUN pip install --no-cache-dir flask   189.3s
 => [nbb_subconscious 4/8] COPY requirements.txt /tmp/requirements.txt   0.4s
 => [nbb_spiritual_maternal_integration 4/8] RUN pip install --no-cac  189.8s
 => [nbb_consciousness_containers 4/8] COPY requirements.txt /tmp/requi  0.5s
 => [nbb_spiritual_root 4/8] COPY requirements.txt /tmp/requirements.tx  0.5s
 => [nbb_pituitary_gland 4/8] COPY requirements.txt /tmp/requirements.t  0.5s
 => [nbb_mother_carrie_protocols 4/8] RUN pip install --no-cache-dir   190.2s
 => [nbb_subconscious 5/8] RUN pip install --no-cache-dir -r /tmp/req  189.0s
 => [nbb_spiritual_root 5/8] RUN pip install --no-cache-dir -r /tmp/r  189.3s
 => [nbb_consciousness_containers 5/8] RUN pip install --no-cache-dir  190.6s
 => [nbb_pituitary_gland 5/8] RUN pip install --no-cache-dir -r /tmp/  190.4s
 => [nbb-i-containers 3/6] COPY neurobiological_brain/ /app/neurobiol  120.6s
 => CACHED [jarvis-swarm-intelligence 3/5] COPY services/requirements.t  0.0s
 => CACHED [jarvis-neurobiological-master 4/5] RUN pip install --no-cac  0.0s
 => [jarvis-agents-service 5/5] COPY services /app/services            119.5s
 => CACHED [jarvis-neurobiological-master 3/8] COPY services/requiremen  0.0s
 => CACHED [jarvis-neurobiological-master 4/8] RUN pip install --no-cac  0.0s
 => [jarvis-neurobiological-master 5/8] COPY neurobiological_brain /a  117.2s
 => [jarvis-unified-gateway 3/5] COPY services /app/services           114.1s
 => [jarvis-blood-brain-barrier 3/5] COPY bbb_requirements.txt /app/bbb  9.7s
 => CACHED [jarvis-consciousness-bridge 3/5] COPY requirements.txt /app  0.0s
 => CACHED [jarvis-consciousness-bridge 4/5] RUN pip install --no-cache  0.0s
 => CACHED [jarvis-qualia-engine  3/12] RUN apt-get update && apt-get i  0.0s
 => CACHED [jarvis-qualia-engine  4/12] RUN pip install --upgrade pip s  0.0s
 => CACHED [jarvis-qualia-engine  5/12] RUN pip install --no-cache-dir   0.0s
 => CACHED [jarvis-qualia-engine  6/12] RUN pip install --no-cache-dir   0.0s
 => CACHED [jarvis-qualia-engine  7/12] RUN pip install --no-cache-dir   0.0s
 => CACHED [jarvis-qualia-engine  8/12] COPY requirements.txt .          0.0s
 => CACHED [jarvis-qualia-engine  9/12] RUN pip install --no-cache-dir   0.0s
 => CACHED [jarvis-qualia-engine 10/12] RUN python3 << 'PYNLTK'          0.0s
 => [jarvis-consciousness-bridge 5/5] COPY . /app/services/            934.4s
 => [jarvis-qualia-engine 11/12] COPY . .                              934.3s
 => [nbb_prefrontal_cortex 5/8] RUN pip install --no-cache-dir redis    65.5s
 => [jarvis-judge-ethics 4/5] COPY judge_*.py /app/                     62.8s
 => [nbb_subconscious 6/8] RUN pip install --no-cache-dir flask         65.1s
 => [jarvis-blood-brain-barrier 4/5] RUN pip install --no-cache-dir -  320.9s
 => [jarvis-i-containers 4/6] COPY ms_jarvis_i_containers_service.py /  40.0s
 => [llm4-proxy] exporting to image                                     16.0s
 => => exporting layers                                                 14.8s
 => => writing image sha256:1e0e8d17923602f853ae5290931892972a8706c37bb  0.2s
 => => naming to docker.io/library/msjarvis-rebuild-llm4-proxy           0.1s
 => [llm21-proxy] exporting to image                                    20.5s
 => => exporting layers                                                 15.8s
 => => writing image sha256:96e4738b66e5381550df611c241c886a44bf2159d3b  1.4s
 => => naming to docker.io/library/msjarvis-rebuild-llm21-proxy          0.1s
 => [llm5-proxy] exporting to image                                     15.8s
 => => exporting layers                                                 14.3s
 => => writing image sha256:f09ebda447d6bbe0a7d52bc9c45826d851a5fc503cd  0.4s
 => => naming to docker.io/library/msjarvis-rebuild-llm5-proxy           0.1s
 => [llm3-proxy] exporting to image                                     22.6s
 => => exporting layers                                                 16.9s
 => => writing image sha256:c057b2933a2a1567b473d71fe816d961ce6a7802356  1.6s
 => => naming to docker.io/library/msjarvis-rebuild-llm3-proxy           0.2s
 => [llm19-proxy] exporting to image                                    21.5s
 => => exporting layers                                                 16.0s
 => => writing image sha256:dd767e49dbd32359e39138d8db9bcbb89f277700f5d  1.4s
 => => naming to docker.io/library/msjarvis-rebuild-llm19-proxy          0.5s
 => [llm16-proxy] exporting to image                                    22.0s
 => => exporting layers                                                 16.4s
 => => writing image sha256:c2f62d94eb8ce4fa6a8dcede0cde48948e38b719c3c  1.5s
 => => naming to docker.io/library/msjarvis-rebuild-llm16-proxy          0.2s
 => [llm6-proxy] exporting to image                                     19.7s
 => => exporting layers                                                 15.3s
 => => writing image sha256:0538ffaae74239a4c9ba3dfcbed3540b50cce9c28e6  1.4s
 => => naming to docker.io/library/msjarvis-rebuild-llm6-proxy           0.1s
 => [llm10-proxy] exporting to image                                    17.1s
 => => exporting layers                                                 14.7s
 => => writing image sha256:4d6baa2e1891460e7d494093c85b98429da9f99c504  0.7s
 => => naming to docker.io/library/msjarvis-rebuild-llm10-proxy          0.2s
 => [nbb_spiritual_maternal_integration 5/8] RUN pip install --no-cach  64.6s
 => [nbb_spiritual_root 6/8] RUN pip install --no-cache-dir flask       64.5s
 => [nbb_blood_brain_barrier 5/7] RUN pip install --no-cache-dir flask  64.8s
 => [llm12-proxy] exporting to image                                    28.8s
 => => exporting layers                                                 18.9s
 => => writing image sha256:bb5073e8e80ff62e9d4646a83c1550b3117171b48b9  1.5s
 => => naming to docker.io/library/msjarvis-rebuild-llm12-proxy          0.2s
 => [llm17-proxy] exporting to image                                    24.8s
 => => exporting layers                                                 17.6s
 => => writing image sha256:58ca30306a384cac79a5ca1c42f3a62929a20ad4f5e  1.2s
 => => naming to docker.io/library/msjarvis-rebuild-llm17-proxy          0.2s
 => [jarvis-psychology-services] exporting to image                     36.2s
 => => exporting layers                                                 21.1s
 => => writing image sha256:0603edd6baa33e5224442244842348389c66b465aa0  1.3s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-psychology-s  0.3s
 => [jarvis-local-resources] exporting to image                         13.6s
 => => exporting layers                                                 13.0s
 => => writing image sha256:8e3539eca8f668826e0f9b6bf19dd6c81700797414d  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-local-resour  0.1s
 => [llm9-proxy] exporting to image                                     25.2s
 => => exporting layers                                                 18.0s
 => => writing image sha256:321c4d64ba0f293c61e8795d40808b965b4a6e6c2ef  1.1s
 => => naming to docker.io/library/msjarvis-rebuild-llm9-proxy           0.2s
 => [llm13-proxy] exporting to image                                    24.0s
 => => exporting layers                                                 16.8s
 => => writing image sha256:a19eb2083254362e78c2de8673571ae9c65a7df00a8  1.5s
 => => naming to docker.io/library/msjarvis-rebuild-llm13-proxy          0.1s
 => [llm8-proxy] exporting to image                                     22.8s
 => => exporting layers                                                 16.5s
 => => writing image sha256:3cab47d847cad9f63485b4dea85a994b98f59a30c56  1.5s
 => => naming to docker.io/library/msjarvis-rebuild-llm8-proxy           0.1s
 => [nbb_heteroglobulin_transport 5/8] RUN pip install --no-cache-dir   64.2s
 => [llm7-proxy] exporting to image                                     26.8s
 => => exporting layers                                                 18.3s
 => => writing image sha256:b57613bf3369fde88825984aa9c91de79e358a3a1a7  1.3s
 => => naming to docker.io/library/msjarvis-rebuild-llm7-proxy           0.2s
 => [nbb_mother_carrie_protocols 5/8] RUN pip install --no-cache-dir r  63.9s
 => [nbb_darwin_godel_machines] exporting to image                      25.9s
 => => exporting layers                                                 17.9s
 => => writing image sha256:2a1b26a201dca3296809f5cb838d39e3116f37ea5cf  1.2s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_darwin_godel_ma  0.2s
 => [llm11-proxy] exporting to image                                    36.5s
 => => exporting layers                                                 21.4s
 => => writing image sha256:5e8be22019f02ed6cb74d7f57e8dfbe35f82a169d9e  0.6s
 => => naming to docker.io/library/msjarvis-rebuild-llm11-proxy          0.4s
 => [jarvis-temporal-consciousness 5/5] COPY temporal_consciousness.py  64.0s
 => [nbb-i-containers 4/6] COPY services/ /app/services/               320.1s
 => [nbb_qualia_engine] exporting to image                              37.7s
 => => exporting layers                                                 21.9s
 => => writing image sha256:12e759b91904ee3cc3247b9cdd92c3bf7cd01aecff3  0.2s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_qualia_engine    0.2s
 => [llm15-proxy] exporting to image                                    28.2s
 => => exporting layers                                                 18.5s
 => => writing image sha256:2c7550f7d1992d0bc6af38517bdf5f22b2f32a01da4  1.4s
 => => naming to docker.io/library/msjarvis-rebuild-llm15-proxy          0.1s
 => [llm2-proxy] exporting to image                                     29.4s
 => => exporting layers                                                 18.8s
 => => writing image sha256:096b882a5bbb4807dea01f4b734158a7ef13c3f25fe  1.6s
 => => naming to docker.io/library/msjarvis-rebuild-llm2-proxy           0.1s
 => [jarvis-unified-gateway 4/5] COPY gateway-entrypoint.sh /app/gatew  63.8s
 => [llm22-proxy] exporting to image                                    30.7s
 => => exporting layers                                                 19.1s
 => => writing image sha256:4d7838756413e66dab44bcddeb23a0ee234f6a8def9  1.6s
 => => naming to docker.io/library/msjarvis-rebuild-llm22-proxy          0.2s
 => [nbb_pituitary_gland 6/8] RUN pip install --no-cache-dir flask      63.6s
 => [llm18-proxy] exporting to image                                    32.8s
 => => exporting layers                                                 19.4s
 => => writing image sha256:f95072667af105a571e592ef662030ad5835455d24d  1.5s
 => => naming to docker.io/library/msjarvis-rebuild-llm18-proxy          0.2s
 => [jarvis-swarm-intelligence] exporting to image                     183.7s
 => => exporting layers                                                182.2s
 => => writing image sha256:022b51a874794685a0bebc67efa9e22bdccf42ffd02  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-swarm-intell  0.1s
 => [jarvis-agents-service] exporting to image                         183.4s
 => => exporting layers                                                182.2s
 => => writing image sha256:14865a44e262520c68218c77898d7f31baf12d3b075  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-agents-servi  0.1s
 => [nbb_consciousness_containers 6/8] RUN pip install --no-cache-dir   63.5s
 => [jarvis-neurobiological-master 6/8] COPY services /app/services    319.8s
 => [jarvis-main-brain 4/7] COPY requirements.txt /app/                 63.3s
 => [jarvis-woah 4/5] COPY services /app/services                      319.6s
 => [llm14-proxy] exporting to image                                    36.7s
 => => exporting layers                                                 20.8s
 => => writing image sha256:a4849224d745ac2f66c663c4994f3c06239c2712e52  0.2s
 => => naming to docker.io/library/msjarvis-rebuild-llm14-proxy          0.5s
 => [llm20-proxy] exporting to image                                    35.3s
 => => exporting layers                                                 20.1s
 => => writing image sha256:bcd8a277bc517f1e0f103d40ef46e7f041bd664a960  0.8s
 => => naming to docker.io/library/msjarvis-rebuild-llm20-proxy          0.4s
 => [llm1-proxy] exporting to image                                     33.5s
 => => exporting layers                                                 19.1s
 => => writing image sha256:5ca7e0ab1b76d5abdf58724728b182e6c1c1536b124  1.4s
 => => naming to docker.io/library/msjarvis-rebuild-llm1-proxy           0.2s
 => [jarvis-i-containers 5/6] COPY integration_layer/ /app/integration  25.2s
 => [jarvis-local-resources] resolving provenance for metadata file     36.8s
 => [llm5-proxy] resolving provenance for metadata file                 35.5s
 => [llm21-proxy] resolving provenance for metadata file                34.6s
 => [llm17-proxy] resolving provenance for metadata file                34.0s
 => [llm10-proxy] resolving provenance for metadata file                35.0s
 => [llm6-proxy] resolving provenance for metadata file                 33.9s
 => [jarvis-judge-ethics 5/5] COPY lm_synthesizer.py /app/             257.5s
 => [nbb_woah_algorithms 5/6] RUN pip install --no-cache-dir redis     256.0s
 => [nbb_mother_carrie_protocols 6/8] COPY service_discovery.py /app/  163.1s
 => [nbb_subconscious 7/8] RUN pip install --no-cache-dir redis        255.6s
 => [nbb_spiritual_root 7/8] RUN pip install --no-cache-dir redis      255.6s
 => [nbb_spiritual_maternal_integration 6/8] COPY service_discovery.p  254.3s
 => [nbb_heteroglobulin_transport 6/8] COPY service_discovery.py /app  254.8s
 => [jarvis-main-brain 5/7] RUN pip install --no-cache-dir -r requir  3324.7s
 => [nbb_pituitary_gland 7/8] RUN pip install --no-cache-dir redis     255.5s
 => [jarvis-temporal-consciousness] exporting to image                  11.4s
 => => exporting layers                                                 10.6s
 => => writing image sha256:04f9a5cdd2179f36a6248dd622a1c372363913331cb  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-temporal-con  0.1s
 => [jarvis-hippocampus 4/5] RUN pip install --no-cache-dir     fasta  689.4s
 => [jarvis-unified-gateway 5/5] RUN chmod +x /app/gateway-entrypoint  255.6s
 => [nbb_consciousness_containers 7/8] RUN pip install --no-cache-dir  255.8s
 => [jarvis-toroidal 4/7] COPY requirements_toroidal.txt /app/require  255.1s
 => [jarvis-semaphore 4/6] COPY requirements_semaphore.txt /app/requi  254.9s
 => [nbb_prefrontal_cortex 6/8] COPY service_discovery.py /app/servic  256.0s
 => [nbb_blood_brain_barrier 6/7] RUN pip install --no-cache-dir redi  255.2s
 => [jarvis-i-containers 6/6] COPY neurobiological_brain/ /app/neurob  256.1s
 => [jarvis-fractal-consciousness 5/7] COPY neurobiological_brain/ /a  255.7s
 => [llm8-proxy] resolving provenance for metadata file                 27.7s
 => [llm19-proxy] resolving provenance for metadata file                26.8s
 => [llm16-proxy] resolving provenance for metadata file                26.7s
 => [llm3-proxy] resolving provenance for metadata file                 26.5s
 => [llm4-proxy] resolving provenance for metadata file                 26.3s
 => [llm9-proxy] resolving provenance for metadata file                 26.2s
 => [llm12-proxy] resolving provenance for metadata file                26.0s
 => [llm7-proxy] resolving provenance for metadata file                 25.0s
 => [nbb_darwin_godel_machines] resolving provenance for metadata file  24.6s
 => [llm15-proxy] resolving provenance for metadata file                24.0s
 => [jarvis-psychology-services] resolving provenance for metadata fil  22.8s
 => [llm2-proxy] resolving provenance for metadata file                 21.6s
 => [llm22-proxy] resolving provenance for metadata file                20.4s
 => [llm18-proxy] resolving provenance for metadata file                19.8s
 => [llm1-proxy] resolving provenance for metadata file                 19.1s
 => [llm11-proxy] resolving provenance for metadata file                18.3s
 => [llm20-proxy] resolving provenance for metadata file                17.9s
 => [llm14-proxy] resolving provenance for metadata file                16.6s
 => [nbb_qualia_engine] resolving provenance for metadata file          15.1s
 => [llm13-proxy] resolving provenance for metadata file                13.7s
 => [jarvis-temporal-consciousness] resolving provenance for metadata f  0.0s
 => [jarvis-swarm-intelligence] resolving provenance for metadata file   0.3s
 => [jarvis-agents-service] resolving provenance for metadata file       0.0s
 => [nbb_mother_carrie_protocols 7/8] RUN pip install --no-cache-dir r  93.1s
 => [nbb_spiritual_maternal_integration 7/8] RUN pip install --no-cac  131.2s
 => [nbb_heteroglobulin_transport 7/8] RUN pip install --no-cache-dir  158.0s
 => [jarvis-judge-truth] exporting to image                             18.8s
 => => exporting layers                                                 18.0s
 => => writing image sha256:8a7e36d5ddf3ea39cdd93eecdbc14231c7ce69467a7  0.2s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-judge-truth   0.3s
 => [jarvis-judge-pipeline] exporting to image                          19.2s
 => => exporting layers                                                 18.0s
 => => writing image sha256:475c305efbe0501d229e61f3ca2918ac76a83d7b646  0.2s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-judge-pipeli  0.3s
 => [jarvis-judge-alignment] exporting to image                         19.3s
 => => exporting layers                                                 18.0s
 => => writing image sha256:66700240f4b7f6d447214af2ba446013d16eaf1e7f1  0.2s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-judge-alignm  0.3s
 => [jarvis-judge-consistency] exporting to image                       19.7s
 => => exporting layers                                                 18.0s
 => => writing image sha256:b5ebe45f73d86c7838f6e1009100e15a668c0dc93d5  0.2s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-judge-consis  0.4s
 => [jarvis-semaphore 5/6] RUN pip install --no-cache-dir -r /app/req  225.7s
 => [jarvis-judge-ethics] exporting to image                            19.3s
 => => exporting layers                                                 18.0s
 => => writing image sha256:d358047a5967f3f937c84ea9a33783b446720e67a6d  0.2s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-judge-ethics  0.4s
 => [jarvis-toroidal 5/7] RUN pip install --no-cache-dir -r /app/requ  225.4s
 => [nbb_blood_brain_barrier 7/7] RUN pip install --no-cache-dir requ  199.6s
 => [nbb_subconscious 8/8] RUN pip install --no-cache-dir requests      47.5s
 => [jarvis-eeg-beta 4/8] COPY eeg_shared/ /app/eeg_shared/             11.1s
 => [nbb_spiritual_root 8/8] RUN pip install --no-cache-dir requests    48.6s
 => [nbb_pituitary_gland 8/8] RUN pip install --no-cache-dir requests   43.5s
 => [jarvis-blood-brain-barrier 5/5] COPY . /app/services              603.7s
 => [jarvis-unified-gateway] exporting to image                        211.0s
 => => exporting layers                                                202.1s
 => => writing image sha256:344791ffd4f64da45bbb6b337821e5be8ef68e94f43  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-unified-gate  0.0s
 => [nbb_woah_algorithms 6/6] RUN pip install --no-cache-dir requests   33.7s
 => [nbb_consciousness_containers 8/8] RUN pip install --no-cache-dir   40.3s
 => [jarvis-web-research 6/7] COPY integration_layer/ /app/integration  11.6s
 => [nbb-i-containers 5/6] COPY requirements.txt /app/requirements.txt  11.1s
 => [nbb_prefrontal_cortex 7/8] RUN pip install --no-cache-dir request  88.9s
 => [jarvis-i-containers] exporting to image                            21.8s
 => => exporting layers                                                 17.8s
 => => writing image sha256:339f9c5a828c9d1b042f701470a625076854d837e40  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-i-containers  0.0s
 => [jarvis-woah 5/5] RUN pip install --no-cache-dir fastapi uvicorn[  276.2s
 => [jarvis-neurobiological-master 7/8] RUN pip install --no-cache-dir  47.7s
 => [psychological_rag_domain] exporting to image                      159.8s
 => => exporting layers                                                159.5s
 => => writing image sha256:5ffe32f3662fd5dae72147bc1229190c2a34ec20108  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-psychological_rag_d  0.1s
 => [nbb_mother_carrie_protocols 8/8] COPY service_registry_client.py   11.5s
 => [jarvis-aaacpe-rag 4/5] RUN mkdir -p /data/aaacpe_chroma            10.6s
 => [jarvis-brain-orchestrator 4/5] COPY services /app/services        224.0s
 => [jarvis-eeg-delta 5/8] COPY jarvis_eeg_delta_30s.py /app/            1.8s
 => [jarvis-aaacpe-rag 5/5] COPY aaacpe_rag_service.py /app/             4.1s
 => [nbb-i-containers 6/6] RUN pip install --no-cache-dir -r /app/re  3102.2s
 => [jarvis-fractal-consciousness 7/7] COPY ms_jarvis_web_research_simp  3.6s
 => [nbb_mother_carrie_protocols] exporting to image                     4.5s
 => => exporting layers                                                  4.3s
 => => writing image sha256:77cf160ac666607d8f28e92fba872ea1005c6de1a10  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_mother_carrie_p  0.0s
 => [jarvis-eeg-beta 6/8] COPY jarvis_eeg_theta_60s.py /app/             3.0s
 => [jarvis-aaacpe-rag] exporting to image                             195.1s
 => => exporting layers                                                181.0s
 => => writing image sha256:faca881688b69ced566bccf57afcb02dbb10b388fe8  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-aaacpe-rag    0.2s
 => [jarvis-eeg-delta 7/8] COPY jarvis_eeg_beta_5m.py /app/              1.0s
 => [jarvis-web-research] exporting to image                            32.3s
 => => exporting layers                                                 24.0s
 => => writing image sha256:529f881d48dfe58eeeea4a2eb78b7902cb735372b52  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-web-research  0.1s
 => [jarvis-fractal-consciousness] exporting to image                   29.7s
 => => exporting layers                                                 24.0s
 => => writing image sha256:ce9aef5ebaaace13ce60477170dd22d0f6fecd103a6  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-fractal-cons  0.1s
 => [jarvis-eeg-beta 8/8] RUN touch /app/eeg_shared/__init__.py          5.6s
 => [nbb_mother_carrie_protocols] resolving provenance for metadata fil  0.0s
 => [jarvis-eeg-theta] exporting to image                              186.0s
 => => exporting layers                                                181.2s
 => => writing image sha256:2eb13fe6d500efb25dc004ca344e8d679947b697af4  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-eeg-theta     0.3s
 => [jarvis-eeg-delta] exporting to image                              186.3s
 => => exporting layers                                                181.1s
 => => writing image sha256:973d0b55dbd4454b8d32ccee816cd69227cd38b7758  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-eeg-delta     0.2s
 => [jarvis-eeg-beta] exporting to image                               186.0s
 => => exporting layers                                                181.0s
 => => writing image sha256:48735f9a9a6b308584580a8764856789b6436671174  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-eeg-beta      0.3s
 => [jarvis-judge-truth] resolving provenance for metadata file          8.1s
 => [jarvis-judge-pipeline] resolving provenance for metadata file       7.3s
 => [jarvis-judge-alignment] resolving provenance for metadata file      8.6s
 => [jarvis-judge-consistency] resolving provenance for metadata file    8.4s
 => [jarvis-judge-ethics] resolving provenance for metadata file         7.6s
 => [nbb_woah_algorithms] exporting to image                            25.3s
 => => exporting layers                                                 20.6s
 => => writing image sha256:74f0bcb60499c6520bf3f7c2da6f3d5d7234eb7a425  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_woah_algorithms  0.0s
 => [jarvis-i-containers] resolving provenance for metadata file         5.5s
 => [nbb_consciousness_containers] exporting to image                   18.0s
 => => exporting layers                                                 12.5s
 => => writing image sha256:a2d2cf369e0d38f64b7c586bf596e3b08941dc0a187  0.3s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_consciousness_c  0.0s
 => [nbb_pituitary_gland] exporting to image                            15.5s
 => => exporting layers                                                  8.7s
 => => writing image sha256:84ef0eb2ccd1a110599961deeb43e4207373449cb0d  0.9s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_pituitary_gland  0.4s
 => [nbb_subconscious] exporting to image                               11.8s
 => => exporting layers                                                  3.7s
 => => writing image sha256:78541b556adb5558c4eda3d04f9100ae5f9313d0db1  1.1s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_subconscious     0.4s
 => [nbb_spiritual_root] exporting to image                             10.7s
 => => exporting layers                                                  4.4s
 => => writing image sha256:4f913e74ca8760989f657c625d5f5344f012f25905d  1.0s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_spiritual_root   0.0s
 => [jarvis-neurobiological-master 8/8] RUN pip install --no-cache-di  130.3s
 => [jarvis-fractal-consciousness] resolving provenance for metadata fi  0.0s
 => [jarvis-web-research] resolving provenance for metadata file         0.0s
 => [nbb_spiritual_root] resolving provenance for metadata file          8.0s
 => [nbb_pituitary_gland] resolving provenance for metadata file         7.3s
 => [nbb_consciousness_containers] resolving provenance for metadata fi  5.9s
 => [nbb_woah_algorithms] resolving provenance for metadata file         4.9s
 => [nbb_subconscious] resolving provenance for metadata file            3.7s
 => [nbb_prefrontal_cortex 8/8] COPY service_registry_client.py /app/  121.3s
 => [nbb_spiritual_maternal_integration 8/8] COPY service_registry_cli  91.5s
 => [nbb_heteroglobulin_transport 8/8] COPY service_registry_client.py  67.3s
 => [psychological_rag_domain] resolving provenance for metadata file    1.0s
 => [jarvis-neurobiological-master] exporting to image                 137.4s
 => => exporting layers                                                137.3s
 => => writing image sha256:4ff3c79c458d4aed1b65ef0bc6e445e9e5ac91dd6fa  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-neurobiologi  0.0s
 => [nbb_blood_brain_barrier] exporting to image                        17.2s
 => => exporting layers                                                 17.0s
 => => writing image sha256:a6d09657512e25928d4ba18f6a0212b20b2ed23e9b0  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_blood_brain_bar  0.0s
 => [nbb_prefrontal_cortex] exporting to image                           9.6s
 => => exporting layers                                                  8.9s
 => => writing image sha256:49ebe86e605aaeefa348ce7a978cff1ec6c875de30c  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_prefrontal_cort  0.1s
 => [jarvis-unified-gateway] resolving provenance for metadata file      6.0s
 => [jarvis-aaacpe-rag] resolving provenance for metadata file           5.1s
 => [nbb_spiritual_maternal_integration] exporting to image              4.5s
 => => exporting layers                                                  4.4s
 => => writing image sha256:fb4a519485297c82f6999da1884b28a5b8253880f25  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_spiritual_mater  0.0s
 => [jarvis-eeg-beta] resolving provenance for metadata file             1.7s
 => [nbb_heteroglobulin_transport] exporting to image                    2.0s
 => => exporting layers                                                  1.9s
 => => writing image sha256:e55772c63dd38f2d14782374ba1afdd7200d1c8f746  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-nbb_heteroglobulin_  0.0s
 => [jarvis-toroidal 6/7] RUN python -m pip install --no-cache-dir fas  33.9s
 => [jarvis-20llm-production 5/5] RUN pip install --no-cache-dir fast  208.8s
 => [jarvis-semaphore 6/6] COPY msjarvis_semaphore.py /app/msjarvis_sem  1.4s
 => [jarvis-eeg-theta] resolving provenance for metadata file            1.2s
 => [jarvis-eeg-delta] resolving provenance for metadata file            0.8s
 => [nbb_prefrontal_cortex] resolving provenance for metadata file       0.2s
 => [jarvis-semaphore] exporting to image                               10.8s
 => => exporting layers                                                 10.5s
 => => writing image sha256:c98c24871c50ab92d28d35af4d69067e7dc8a9f865a  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-semaphore     0.0s
 => [nbb_spiritual_maternal_integration] resolving provenance for metad  0.2s
 => [nbb_heteroglobulin_transport] resolving provenance for metadata fi  0.1s
 => [nbb_blood_brain_barrier] resolving provenance for metadata file     0.0s
 => [jarvis-semaphore] resolving provenance for metadata file            0.2s
 => [jarvis-toroidal 7/7] COPY toroidal_service.py /app/toroidal_servic  7.7s
 => [jarvis-toroidal] exporting to image                                10.6s
 => => exporting layers                                                  9.0s
 => => writing image sha256:c4568de49051b88cd9ab4ad0291fd11feece1918f5b  0.0s
 => => naming to docker.io/library/msjarvis-toroidal:latest              0.3s
 => [jarvis-woah] exporting to image                                   137.1s
 => => exporting layers                                                136.1s
 => => writing image sha256:2ca9945317632ca0541a047fc10ec35a6d3539ef030  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-woah          0.2s
 => [jarvis-toroidal] resolving provenance for metadata file             0.2s
 => [jarvis-neurobiological-master] resolving provenance for metadata f  0.2s
 => [jarvis-woah] resolving provenance for metadata file                 3.3s
 => [jarvis-hippocampus 5/5] COPY hippocampus_service.py /app/hippocamp  0.3s
 => [jarvis-brain-orchestrator] exporting to image                     117.7s
 => => exporting layers                                                117.4s
 => => writing image sha256:4a01c40ebe6942019db2b4f00ffb9938ebb5321eafc  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-brain-orches  0.0s
 => [jarvis-20llm-production] exporting to image                       117.6s
 => => exporting layers                                                117.4s
 => => writing image sha256:deecda254a5e0a6306a2e5e3a201f31d1aa2ef3ef90  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-20llm-produc  0.0s
 => [jarvis-hippocampus] exporting to image                             28.5s
 => => exporting layers                                                 27.9s
 => => writing image sha256:edcfa8d0b49397c68ab7cf1aa367061ebc190d54d4d  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-hippocampus   0.1s
 => [jarvis-hippocampus] resolving provenance for metadata file          3.2s
 => [jarvis-brain-orchestrator] resolving provenance for metadata file   3.5s
 => [jarvis-20llm-production] resolving provenance for metadata file     2.6s
 => [jarvis-lm-synthesizer stage-0 5/5] COPY lm_synthesizer.py /app/lm_  2.1s
 => [jarvis-lm-synthesizer] exporting to image                          36.0s
 => => exporting layers                                                 36.0s
 => => writing image sha256:394d75cc4c4f030e3ef6926e75667d3a120bfa886f9  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-lm-synthesiz  0.0s
 => [jarvis-qualia-engine 12/12] WORKDIR /app/services                   0.4s
 => [jarvis-blood-brain-barrier] exporting to image                     54.3s
 => => exporting layers                                                 54.3s
 => => writing image sha256:6d14bbec73e1b7e6c6d0ebc09e679409a3f2a42b33c  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-blood-brain-  0.0s
 => [jarvis-consciousness-bridge] exporting to image                    54.9s
 => => exporting layers                                                 54.7s
 => => writing image sha256:fb112b1dc8e60a85a2439f051ddb810f5111a6997a2  0.1s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-consciousnes  0.0s
 => [jarvis-qualia-engine] exporting to image                           55.0s
 => => exporting layers                                                 54.8s
 => => writing image sha256:922a7f953f4ba7bd21ee3af7d113c7b400c4663d220  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-qualia-engin  0.0s
 => [jarvis-lm-synthesizer] resolving provenance for metadata file       0.1s
 => [jarvis-blood-brain-barrier] resolving provenance for metadata file  0.1s
 => [jarvis-consciousness-bridge] resolving provenance for metadata fil  0.1s
 => [jarvis-qualia-engine] resolving provenance for metadata file        0.0s
 => [jarvis-rag-server 4/4] COPY ms_jarvis_rag_server.py ms_jarvis_rag_  0.0s
 => [jarvis-rag-server] exporting to image                              11.6s
 => => exporting layers                                                 11.5s
 => => writing image sha256:d41640e5e73cf44796116a590ec871b9984a017a82a  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-rag-server    0.0s
 => [jarvis-rag-server] resolving provenance for metadata file           0.0s
 => [jarvis-constitutional-guardian 5/5] COPY constitutional_api.py /ap  0.0s
 => [jarvis-constitutional-guardian] exporting to image                 13.4s
 => => exporting layers                                                 13.4s
 => => writing image sha256:becc55f9cf218987646a824a0809dc49be30b04c8cc  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-constitution  0.0s
 => [jarvis-constitutional-guardian] resolving provenance for metadata   0.0s
 => [jarvis-main-brain 6/7] COPY services/ /app/services/               21.0s
 => [jarvis-wv-entangled-gateway 7/7] COPY neurobiological_brain/ /app/  0.5s
 => [jarvis-wv-entangled-gateway] exporting to image                    15.7s
 => => exporting layers                                                 15.6s
 => => writing image sha256:4949a5af683652bc6edee2460ff69ad2b5945a2f324  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-jarvis-wv-entangled  0.0s
 => [jarvis-main-brain] exporting to image                              15.7s
 => => exporting layers                                                 15.6s
 => => writing image sha256:b845dd8fda12beb44665cd94ff57cf8a91755015702  0.0s
 => => naming to docker.io/library/jarvis-main-brain:latest              0.0s
 => [jarvis-wv-entangled-gateway] resolving provenance for metadata fil  0.1s
 => [jarvis-main-brain] resolving provenance for metadata file           0.1s
 => [nbb-i-containers] exporting to image                               19.7s
 => => exporting layers                                                 19.7s
 => => writing image sha256:e04405cc7daadba6c86e828e31caf463a72763cde1a  0.0s
 => => naming to docker.io/library/msjarvis-rebuild-nbb-i-containers     0.0s
 => [nbb-i-containers] resolving provenance for metadata file            0.1s
[+] up 156/156
 ✔ Image msjarvis-rebuild-nbb_woah_algorithms                Built     3654.9s
 ✔ Image jarvis-main-brain:latest                            Built     3654.9s
 ✔ Image msjarvis-rebuild-nbb_spiritual_maternal_integration Built     3654.9s
 ✔ Image msjarvis-rebuild-jarvis-lm-synthesizer              Built     3654.9s
 ✔ Image msjarvis-rebuild-jarvis-temporal-consciousness      Built     3654.9s
 ✔ Image msjarvis-rebuild-llm19-proxy                        Built     3654.9s
 ✔ Image msjarvis-rebuild-llm9-proxy                         Built     3654.9s
 ✔ Image msjarvis-rebuild-jarvis-rag-server                  Built     3654.9s
 ✔ Image msjarvis-rebuild-jarvis-psychology-services         Built     3654.9s
 ✔ Image msjarvis-rebuild-jarvis-local-resources             Built     3654.9s
 ✔ Image msjarvis-rebuild-jarvis-aaacpe-rag                  Built     3654.9s
 ✔ Image msjarvis-rebuild-nbb_darwin_godel_machines          Built     3654.9s
 ✔ Image msjarvis-rebuild-jarvis-judge-truth                 Built     3654.9s
 ✔ Image msjarvis-rebuild-llm4-proxy                         Built     3654.9s
 ✔ Image msjarvis-rebuild-jarvis-mother-protocols            Built     3654.9s
 ✔ Image msjarvis-rebuild-jarvis-hippocampus                 Built     3654.9s
 ✔ Image msjarvis-rebuild-jarvis-20llm-production            Built     3654.9s
 ✔ Image msjarvis-rebuild-jarvis-agents-service              Built     3654.9s
 ✔ Image msjarvis-rebuild-llm15-proxy                        Built     3654.9s
 ✔ Image msjarvis-rebuild-jarvis-judge-consistency           Built     3654.9s
 ✔ Image msjarvis-rebuild-jarvis-judge-pipeline              Built     3654.9s
 ... 135 more                                                                 
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/neurobiological_brain/darwin_godel_machines$ 

