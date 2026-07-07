(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ sudo python3 << 'PYEOF'
import re

# ── Fix 1: dgm_worker.py — score component name too ──
wpath = "/mnt/spiritual_drive/msjarvis-rebuild/services/dgm_worker.py"
with open(wpath) as f:
    w = f.read()

old_score = '''def score_message(text: str):
    text_lower = text.lower()
    matched = [kw for kw in KEYWORDS if kw in text_lower]
    score = min(0.25 + len(matched) * 0.12, 1.0)
    return round(score, 3), matched'''

new_score = '''def score_message(text: str, component: str = ""): 
    # Score both patch content AND component filename for domain routing
    combined = (text + " " + component).lower()
    matched = [kw for kw in KEYWORDS if kw in combined]
    # Bonus if component filename directly contains a specialty keyword
    fname_matched = [kw for kw in KEYWORDS if kw.replace(" ","_")PYEOF("✅ scheduler syntax OK")OK")tent passed through pipeline")
✅ dgm_worker.py: component-aware scoring applied
✅ scheduler: real patch content passed through pipeline
✅ dgm_worker.py syntax OK
✅ scheduler syntax OK
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ # Copy scheduler back into container and rebuild DGM workers
docker cp /mnt/spiritual_drive/msjarvis-rebuild/services/master_unified_consciousness_scheduler_ENRICHED.py \
  jarvis-consciousness-scheduler:/app/master_unified_consciousness_scheduler_ENRICHED.py

docker cp /mnt/spiritual_drive/msjarvis-rebuild/services/dgm_worker.py \
  jarvis-dgm-01:/app/dgm_worker.py

# Restart consciousness scheduler immediately (no rebuild needed — file copied in)
docker restart jarvis-consciousness-scheduler

# Rebuild the DGM image so all 23 workers get the new dgm_worker.py
docker compose -f docker-compose.STABLE_20260703_103332.yml \
  build --no-cache jarvis-dgm-01 && \
docker compose -f docker-compose.STABLE_20260703_103332.yml \
  up -d --no-deps \
  jarvis-dgm-01 jarvis-dgm-02 jarvis-dgm-03 jarvis-dgm-04 jarvis-dgm-05 \
  jarvis-dgm-06 jarvis-dgm-07 jarvis-dgm-08 jarvis-dgm-09 jarvis-  jarvis-dgm-21 jarvis-dgm-22 jarvis-dgm-23 jarvis-dgm-19 jarvis-
Successfully copied 10.8kB (transferred 12.8kB) to jarvis-consciousness-scheduler:/app/master_unified_consciousness_scheduler_ENRICHED.py
Error response from daemon: unlinkat /app/master_unified_consciousness_scheduler_ENRICHED.py: device or resource busy
Successfully copied 6.95kB (transferred 8.7kB) to jarvis-dgm-01:/app/dgm_worker.py
jarvis-consciousness-scheduler
[+] Building 8776.3s (10/11)                                       
 => [internal] load local bake definitions                    0.0s
 => => reading from stdin 625B                                0.0s
 => [internal] load build definition from Dockerfile.dgm_wor  0.0s
 => => transferring dockerfile: 440B                          0.0s
 => [internal] load metadata for docker.io/library/python:3.  0.0s
 => [internal] load .dockerignore                             0.0s
 => => transferring context: 2B                               0.0s
 => [1/6] FROM docker.io/library/python:3.11-slim             0.0s
 => [internal] load build context                             0.0s
 => => transferring context: 7.35kB                           0.0s
 => CACHED [2/6] WORKDIR /app                                 0.0s
 => [3/6] RUN apt-get update && apt-get install -y --no-in  881.5s
 => [4/6] COPY requirements.txt /app/requirements.txt         0.0s
 => ERROR [5/6] RUN pip install --no-cache-dir -r /app/re  7894.6s
------                                                             
 > [5/6] RUN pip install --no-cache-dir -r /app/requirements.txt:  
4.201 Collecting fastapi (from -r /app/requirements.txt (line 1))  
13.86   Downloading fastapi-0.139.0-py3-none-any.whl.metadata (26 kB)                                                                 
20.03 Collecting pydantic (from -r /app/requirements.txt (line 3)) 
20.51   Downloading pydantic-2.13.4-py3-none-any.whl.metadata (109 kB)
23.21      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 109.4/109.4 kB 37.5 kB/s eta 0:00:00
39.68 Collecting numpy (from -r /app/requirements.txt (line 4))
40.01   Downloading numpy-2.4.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
40.94 Collecting httpx (from -r /app/requirements.txt (line 5))
41.12   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
45.63 Collecting chromadb==0.6.3 (from -r /app/requirements.txt (line 6))
45.92   Downloading chromadb-0.6.3-py3-none-any.whl.metadata (6.8 kB)
47.41 Collecting redis (from -r /app/requirements.txt (line 7))
47.55   Downloading redis-8.0.1-py3-none-any.whl.metadata (13 kB)
49.08 Collecting python-multipart (from -r /app/requirements.txt (line 8))
50.03   Downloading python_multipart-0.0.32-py3-none-any.whl.metadata (2.1 kB)
51.57 Collecting requests (from -r /app/requirements.txt (line 9))
52.16   Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
52.44 Collecting ollama (from -r /app/requirements.txt (line 10))
53.40   Downloading ollama-0.6.2-py3-none-any.whl.metadata (5.8 kB)
84.87 Collecting aiohttp (from -r /app/requirements.txt (line 11))
84.92   Downloading aiohttp-3.14.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (8.3 kB)
85.53 Collecting asyncio (from -r /app/requirements.txt (line 12))
86.77   Downloading asyncio-4.0.0-py3-none-any.whl.metadata (994 bytes)
87.34 Collecting python-dateutil (from -r /app/requirements.txt (line 13))
87.67   Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
91.42 Collecting transformers (from -r /app/requirements.txt (line 15))
91.75   Downloading transformers-5.13.0-py3-none-any.whl.metadata (32 kB)
93.46 Collecting sentence_transformers (from -r /app/requirements.txt (line 16))
93.75   Downloading sentence_transformers-5.6.0-py3-none-any.whl.metadata (18 kB)
96.72 Collecting pytz (from -r /app/requirements.txt (line 17))
97.26   Downloading pytz-2026.2-py2.py3-none-any.whl.metadata (22 kB)
106.0 Collecting scikit-learn (from -r /app/requirements.txt (line 18))
106.8   Downloading scikit_learn-1.9.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (11 kB)
115.6 Collecting scipy (from -r /app/requirements.txt (line 19))
116.5   Downloading scipy-1.17.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
116.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.1/62.1 kB 120.9 kB/s eta 0:00:00
117.4 Collecting textblob (from -r /app/requirements.txt (line 20))
117.8   Downloading textblob-0.20.0-py3-none-any.whl.metadata (4.0 kB)
119.7 Collecting duckduckgo-search (from -r /app/requirements.txt (line 21))
120.1   Downloading duckduckgo_search-8.1.1-py3-none-any.whl.metadata (16 kB)
120.4 Collecting rake-nltk (from -r /app/requirements.txt (line 22))
121.1   Downloading rake_nltk-1.0.6-py3-none-any.whl.metadata (6.4 kB)
121.9 Collecting nltk (from -r /app/requirements.txt (line 23))
122.2   Downloading nltk-3.9.4-py3-none-any.whl.metadata (3.2 kB)
122.8 Collecting PyPDF2 (from -r /app/requirements.txt (line 24))
123.2   Downloading pypdf2-3.0.1-py3-none-any.whl.metadata (6.8 kB)
123.5 Collecting Flask (from -r /app/requirements.txt (line 25))
123.8   Downloading flask-3.1.3-py3-none-any.whl.metadata (3.2 kB)
124.3 Collecting Flask-CORS (from -r /app/requirements.txt (line 26))
124.5   Downloading flask_cors-6.0.5-py3-none-any.whl.metadata (5.4 kB)
124.7 Collecting asgiref (from -r /app/requirements.txt (line 27))
125.0   Downloading asgiref-3.11.1-py3-none-any.whl.metadata (9.3 kB)
127.8 Collecting psycopg2-binary>=2.9.0 (from -r /app/requirements.txt (line 28))
128.1   Downloading psycopg2_binary-2.9.12-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
129.6 Collecting asyncpg>=0.29.0 (from -r /app/requirements.txt (line 29))
129.9   Downloading asyncpg-0.31.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.4 kB)
130.6 Collecting uvicorn[standard] (from -r /app/requirements.txt (line 2))
130.9   Downloading uvicorn-0.50.2-py3-none-any.whl.metadata (6.7 kB)
131.2 Collecting build>=1.0.3 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
131.4   Downloading build-1.5.0-py3-none-any.whl.metadata (5.7 kB)
131.8 Collecting chroma-hnswlib==0.7.6 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
132.0   Downloading chroma_hnswlib-0.7.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (252 bytes)
133.6 Collecting posthog>=2.4.0 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
133.9   Downloading posthog-7.22.0-py3-none-any.whl.metadata (5.4 kB)
134.5 Collecting typing_extensions>=4.5.0 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
134.7   Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
137.8 Collecting onnxruntime>=1.14.1 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
137.9   Downloading onnxruntime-1.27.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (5.4 kB)
138.3 Collecting opentelemetry-api>=1.2.0 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
138.4   Downloading opentelemetry_api-1.43.0-py3-none-any.whl.metadata (1.4 kB)
138.8 Collecting opentelemetry-exporter-otlp-proto-grpc>=1.2.0 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
139.0   Downloading opentelemetry_exporter_otlp_proto_grpc-1.43.0-py3-none-any.whl.metadata (2.6 kB)
139.3 Collecting opentelemetry-instrumentation-fastapi>=0.41b0 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
139.4   Downloading opentelemetry_instrumentation_fastapi-0.64b0-py3-none-any.whl.metadata (2.2 kB)
139.8 Collecting opentelemetry-sdk>=1.2.0 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
139.9   Downloading opentelemetry_sdk-1.43.0-py3-none-any.whl.metadata (1.7 kB)
143.4 Collecting tokenizers>=0.13.2 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
143.6   Downloading tokenizers-0.23.1-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.8 kB)
144.1 Collecting pypika>=0.48.9 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
144.1   Downloading pypika-0.51.1-py2.py3-none-any.whl.metadata (51 kB)
144.8      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 52.0/52.0 kB 121.4 kB/s eta 0:00:00
146.0 Collecting tqdm>=4.65.0 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
146.1   Downloading tqdm-4.68.3-py3-none-any.whl.metadata (57 kB)
146.5      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.4/57.4 kB 132.8 kB/s eta 0:00:00
146.8 Collecting overrides>=7.3.1 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
147.0   Downloading overrides-7.7.0-py3-none-any.whl.metadata (5.8 kB)
147.6 Collecting importlib-resources (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
148.1   Downloading importlib_resources-7.1.0-py3-none-any.whl.metadata (4.0 kB)
160.5 Collecting grpcio>=1.58.0 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
160.6   Downloading grpcio-1.82.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (3.7 kB)
161.1 Collecting bcrypt>=4.0.1 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
161.4   Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl.metadata (10 kB)
161.8 Collecting typer>=0.9.0 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
162.1   Downloading typer-0.26.8-py3-none-any.whl.metadata (15 kB)
162.5 Collecting kubernetes>=28.1.0 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
162.5   Downloading kubernetes-36.0.2-py2.py3-none-any.whl.metadata (1.8 kB)
163.1 Collecting tenacity>=8.2.3 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
163.3   Downloading tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)
164.0 Collecting PyYAML>=6.0.0 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
164.1   Downloading pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
165.1 Collecting mmh3>=4.0.1 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
165.3   Downloading mmh3-5.2.1-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (14 kB)
168.9 Collecting orjson>=3.9.12 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
169.2   Downloading orjson-3.11.9-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (41 kB)
169.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.0/42.0 kB 1.3 MB/s eta 0:00:00
169.8 Collecting rich>=10.11.0 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
170.2   Downloading rich-15.0.0-py3-none-any.whl.metadata (18 kB)
170.6 Collecting starlette>=0.46.0 (from fastapi->-r /app/requirements.txt (line 1))
170.9   Downloading starlette-1.3.1-py3-none-any.whl.metadata (6.4 kB)
171.2 Collecting typing-inspection>=0.4.2 (from fastapi->-r /app/requirements.txt (line 1))
171.6   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
171.9 Collecting annotated-doc>=0.0.2 (from fastapi->-r /app/requirements.txt (line 1))
172.2   Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
172.3 Collecting click>=7.0 (from uvicorn[standard]->-r /app/requirements.txt (line 2))
172.5   Downloading click-8.4.2-py3-none-any.whl.metadata (2.6 kB)
172.6 Collecting h11>=0.8 (from uvicorn[standard]->-r /app/requirements.txt (line 2))
172.7   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
173.3 Collecting httptools>=0.8.0 (from uvicorn[standard]->-r /app/requirements.txt (line 2))
173.4   Downloading httptools-0.8.0-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)
173.6 Collecting python-dotenv>=0.13 (from uvicorn[standard]->-r /app/requirements.txt (line 2))
174.0   Downloading python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
174.5 Collecting uvloop>=0.15.1 (from uvicorn[standard]->-r /app/requirements.txt (line 2))
174.6   Downloading uvloop-0.22.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
175.5 Collecting watchfiles>=0.20 (from uvicorn[standard]->-r /app/requirements.txt (line 2))
175.7   Downloading watchfiles-1.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
176.5 Collecting websockets>=13.0 (from uvicorn[standard]->-r /app/requirements.txt (line 2))
176.6   Downloading websockets-16.0-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (6.8 kB)
176.8 Collecting annotated-types>=0.6.0 (from pydantic->-r /app/requirements.txt (line 3))
176.9   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
188.8 Collecting pydantic-core==2.46.4 (from pydantic->-r /app/requirements.txt (line 3))
188.9   Downloading pydantic_core-2.46.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
189.6 Collecting anyio (from httpx->-r /app/requirements.txt (line 5))
189.9   Downloading anyio-4.14.1-py3-none-any.whl.metadata (4.6 kB)
190.5 Collecting certifi (from httpx->-r /app/requirements.txt (line 5))
190.6   Downloading certifi-2026.6.17-py3-none-any.whl.metadata (2.5 kB)
191.1 Collecting httpcore==1.* (from httpx->-r /app/requirements.txt (line 5))
191.2   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
191.7 Collecting idna (from httpx->-r /app/requirements.txt (line 5))
192.1   Downloading idna-3.18-py3-none-any.whl.metadata (6.1 kB)
193.4 Collecting charset_normalizer<4,>=2 (from requests->-r /app/requirements.txt (line 9))
193.5   Downloading charset_normalizer-3.4.8-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (41 kB)
194.1      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.5/41.5 kB 150.0 kB/s eta 0:00:00
194.5 Collecting urllib3<3,>=1.26 (from requests->-r /app/requirements.txt (line 9))
194.8   Downloading urllib3-2.7.0-py3-none-any.whl.metadata (6.9 kB)
195.0 Collecting aiohappyeyeballs>=2.5.0 (from aiohttp->-r /app/requirements.txt (line 11))
195.3   Downloading aiohappyeyeballs-2.7.1-py3-none-any.whl.metadata (5.9 kB)
195.3 Collecting aiosignal>=1.4.0 (from aiohttp->-r /app/requirements.txt (line 11))
195.7   Downloading aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
195.9 Collecting attrs>=17.3.0 (from aiohttp->-r /app/requirements.txt (line 11))
196.0   Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
199.1 Collecting frozenlist>=1.1.1 (from aiohttp->-r /app/requirements.txt (line 11))
199.4   Downloading frozenlist-1.8.0-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (20 kB)
204.2 Collecting multidict<7.0,>=4.5 (from aiohttp->-r /app/requirements.txt (line 11))
204.5   Downloading multidict-6.7.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (5.3 kB)
205.1 Collecting propcache>=0.2.0 (from aiohttp->-r /app/requirements.txt (line 11))
205.4   Downloading propcache-0.5.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (16 kB)
210.3 Collecting yarl<2.0,>=1.17.0 (from aiohttp->-r /app/requirements.txt (line 11))
210.4   Downloading yarl-1.24.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (94 kB)
210.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 94.2/94.2 kB 176.4 kB/s eta 0:00:00
211.6 Collecting six>=1.5 (from python-dateutil->-r /app/requirements.txt (line 13))
211.6   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
213.1 Collecting huggingface-hub<2.0,>=1.5.0 (from transformers->-r /app/requirements.txt (line 15))
213.4   Downloading huggingface_hub-1.22.0-py3-none-any.whl.metadata (14 kB)
213.6 Collecting packaging>=20.0 (from transformers->-r /app/requirements.txt (line 15))
213.8   Downloading packaging-26.2-py3-none-any.whl.metadata (3.5 kB)
223.4 Collecting regex>=2025.10.22 (from transformers->-r /app/requirements.txt (line 15))
223.6   Downloading regex-2026.6.28-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (40 kB)
223.7      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.5/40.5 kB 270.7 kB/s eta 0:00:00
223.7 Collecting tokenizers>=0.13.2 (from chromadb==0.6.3->-r /app/requirements.txt (line 6))
224.1   Downloading tokenizers-0.22.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
226.6 Collecting safetensors>=0.8.0 (from transformers->-r /app/requirements.txt (line 15))
227.0   Downloading safetensors-0.8.0-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.2 kB)
228.9 Collecting torch>=1.11.0 (from sentence_transformers->-r /app/requirements.txt (line 16))
229.0   Downloading torch-2.12.1-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (31 kB)
229.7 Collecting joblib>=1.4.0 (from scikit-learn->-r /app/requirements.txt (line 18))
230.0   Downloading joblib-1.5.3-py3-none-any.whl.metadata (5.5 kB)
230.6 Collecting narwhals>=2.0.1 (from scikit-learn->-r /app/requirements.txt (line 18))
230.8   Downloading narwhals-2.23.0-py3-none-any.whl.metadata (15 kB)
231.1 Collecting threadpoolctl>=3.5.0 (from scikit-learn->-r /app/requirements.txt (line 18))
231.1   Downloading threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
231.9 Collecting primp>=0.15.0 (from duckduckgo-search->-r /app/requirements.txt (line 21))
232.0   Downloading primp-1.3.1-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.7 kB)
236.2 Collecting lxml>=5.3.0 (from duckduckgo-search->-r /app/requirements.txt (line 21))
236.3   Downloading lxml-6.1.1-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (3.5 kB)
236.4 Collecting blinker>=1.9.0 (from Flask->-r /app/requirements.txt (line 25))
236.6   Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
236.7 Collecting itsdangerous>=2.2.0 (from Flask->-r /app/requirements.txt (line 25))
236.7   Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
237.1 Collecting jinja2>=3.1.2 (from Flask->-r /app/requirements.txt (line 25))
237.4   Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
238.9 Collecting markupsafe>=2.1.1 (from Flask->-r /app/requirements.txt (line 25))
239.1   Downloading markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
239.5 Collecting werkzeug>=3.1.0 (from Flask->-r /app/requirements.txt (line 25))
239.6   Downloading werkzeug-3.1.8-py3-none-any.whl.metadata (4.0 kB)
239.8 Collecting pyproject_hooks (from build>=1.0.3->chromadb==0.6.3->-r /app/requirements.txt (line 6))
240.1   Downloading pyproject_hooks-1.2.0-py3-none-any.whl.metadata (1.3 kB)
241.0 Collecting filelock>=3.10.0 (from huggingface-hub<2.0,>=1.5.0->transformers->-r /app/requirements.txt (line 15))
241.3   Downloading filelock-3.29.6-py3-none-any.whl.metadata (2.0 kB)
241.6 Collecting fsspec>=2023.5.0 (from huggingface-hub<2.0,>=1.5.0->transformers->-r /app/requirements.txt (line 15))
241.7   Downloading fsspec-2026.6.0-py3-none-any.whl.metadata (10 kB)
242.4 Collecting hf-xet<2.0.0,>=1.5.1 (from huggingface-hub<2.0,>=1.5.0->transformers->-r /app/requirements.txt (line 15))
242.6   Downloading hf_xet-1.5.1-cp37-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
243.0 Collecting websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0 (from kubernetes>=28.1.0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
243.3   Downloading websocket_client-1.9.0-py3-none-any.whl.metadata (8.3 kB)
243.5 Collecting requests-oauthlib (from kubernetes>=28.1.0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
243.7   Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)
244.1 Collecting durationpy>=0.7 (from kubernetes>=28.1.0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
244.2   Downloading durationpy-0.10-py3-none-any.whl.metadata (340 bytes)
244.4 Collecting flatbuffers (from onnxruntime>=1.14.1->chromadb==0.6.3->-r /app/requirements.txt (line 6))
244.5   Downloading flatbuffers-25.12.19-py2.py3-none-any.whl.metadata (1.0 kB)
247.5 Collecting protobuf>=4.25.8 (from onnxruntime>=1.14.1->chromadb==0.6.3->-r /app/requirements.txt (line 6))
247.5   Downloading protobuf-7.35.1-cp310-abi3-manylinux2014_x86_64.whl.metadata (595 bytes)
247.9 Collecting googleapis-common-protos~=1.57 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
248.2   Downloading googleapis_common_protos-1.75.0-py3-none-any.whl.metadata (8.6 kB)
248.5 Collecting opentelemetry-exporter-otlp-proto-common==1.43.0 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
248.8   Downloading opentelemetry_exporter_otlp_proto_common-1.43.0-py3-none-any.whl.metadata (1.8 kB)
249.2 Collecting opentelemetry-proto==1.43.0 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
249.5   Downloading opentelemetry_proto-1.43.0-py3-none-any.whl.metadata (2.3 kB)
249.8 Collecting opentelemetry-instrumentation-asgi==0.64b0 (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
250.0   Downloading opentelemetry_instrumentation_asgi-0.64b0-py3-none-any.whl.metadata (2.0 kB)
250.7 Collecting opentelemetry-instrumentation==0.64b0 (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
251.0   Downloading opentelemetry_instrumentation-0.64b0-py3-none-any.whl.metadata (7.2 kB)
251.4 Collecting opentelemetry-semantic-conventions==0.64b0 (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
251.7   Downloading opentelemetry_semantic_conventions-0.64b0-py3-none-any.whl.metadata (2.4 kB)
252.1 Collecting opentelemetry-util-http==0.64b0 (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
252.1   Downloading opentelemetry_util_http-0.64b0-py3-none-any.whl.metadata (2.6 kB)
256.5 Collecting wrapt<3.0.0,>=1.0.0 (from opentelemetry-instrumentation==0.64b0->opentelemetry-instrumentation-fastapi>=0.41b0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
256.7   Downloading wrapt-2.2.2-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (7.4 kB)
257.0 Collecting backoff>=1.10.0 (from posthog>=2.4.0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
257.3   Downloading backoff-2.2.1-py3-none-any.whl.metadata (14 kB)
257.6 Collecting distro>=1.5.0 (from posthog>=2.4.0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
257.8   Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
258.1 Collecting markdown-it-py>=2.2.0 (from rich>=10.11.0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
258.2   Downloading markdown_it_py-4.2.0-py3-none-any.whl.metadata (7.4 kB)
259.8 Collecting pygments<3.0.0,>=2.13.0 (from rich>=10.11.0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
259.9   Downloading pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
260.1 Requirement already satisfied: setuptools<82 in /usr/local/lib/python3.11/site-packages (from torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16)) (79.0.1)
260.5 Collecting sympy>=1.13.3 (from torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
260.8   Downloading sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
261.2 Collecting networkx>=2.5.1 (from torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
261.5   Downloading networkx-3.6.1-py3-none-any.whl.metadata (6.8 kB)
262.2 Collecting cuda-toolkit==13.0.2 (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
262.4   Downloading cuda_toolkit-13.0.2-py2.py3-none-any.whl.metadata (9.4 kB)
262.8 Collecting nvidia-cublas<=13.1.1.3,>=13.1.0.3 (from torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
263.1   Downloading nvidia_cublas-13.1.1.3-py3-none-manylinux_2_27_x86_64.whl.metadata (1.8 kB)
263.5 Collecting cuda-bindings<14,>=13.0.3 (from torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
263.7   Downloading cuda_bindings-13.3.1-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (2.5 kB)
263.8 Collecting nvidia-cudnn-cu13==9.20.0.48 (from torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
263.9   Downloading nvidia_cudnn_cu13-9.20.0.48-py3-none-manylinux_2_27_x86_64.whl.metadata (1.9 kB)
264.0 Collecting nvidia-cusparselt-cu13==0.8.1 (from torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
264.0   Downloading nvidia_cusparselt_cu13-0.8.1-py3-none-manylinux2014_x86_64.whl.metadata (12 kB)
264.3 Collecting nvidia-nccl-cu13==2.29.7 (from torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
264.7   Downloading nvidia_nccl_cu13-2.29.7-py3-none-manylinux_2_18_x86_64.whl.metadata (2.1 kB)
264.9 Collecting nvidia-nvshmem-cu13==3.4.5 (from torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
265.2   Downloading nvidia_nvshmem_cu13-3.4.5-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.1 kB)
265.5 Collecting triton==3.7.1 (from torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
265.8   Downloading triton-3.7.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (1.7 kB)
266.0 Collecting nvidia-cuda-runtime==13.0.96.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
266.5   Downloading nvidia_cuda_runtime-13.0.96-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.7 kB)
266.8 Collecting nvidia-cufft==12.0.0.61.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
267.0   Downloading nvidia_cufft-12.0.0.61-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.8 kB)
267.3 Collecting nvidia-cufile==1.15.1.6.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
267.6   Downloading nvidia_cufile-1.15.1.6-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.7 kB)
267.7 Collecting nvidia-cuda-cupti==13.0.85.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
268.0   Downloading nvidia_cuda_cupti-13.0.85-py3-none-manylinux_2_25_x86_64.whl.metadata (1.7 kB)
268.3 Collecting nvidia-curand==10.4.0.35.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
268.6   Downloading nvidia_curand-10.4.0.35-py3-none-manylinux_2_27_x86_64.whl.metadata (1.7 kB)
268.8 Collecting nvidia-cusolver==12.0.4.66.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
269.1   Downloading nvidia_cusolver-12.0.4.66-py3-none-manylinux_2_27_x86_64.whl.metadata (1.8 kB)
269.3 Collecting nvidia-cusparse==12.6.3.3.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
269.5   Downloading nvidia_cusparse-12.6.3.3-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.8 kB)
269.9 Collecting nvidia-nvjitlink==13.0.88.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
270.1   Downloading nvidia_nvjitlink-13.0.88-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl.metadata (1.7 kB)
270.3 Collecting nvidia-cuda-nvrtc==13.0.88.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
270.6   Downloading nvidia_cuda_nvrtc-13.0.88-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl.metadata (1.7 kB)
271.0 Collecting nvidia-nvtx==13.0.85.* (from cuda-toolkit[cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
271.2   Downloading nvidia_nvtx-13.0.85-py3-none-manylinux1_x86_64.manylinux_2_5_x86_64.whl.metadata (1.8 kB)
271.4 Collecting shellingham>=1.3.0 (from typer>=0.9.0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
271.6   Downloading shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
271.9 Collecting cuda-pathfinder>=1.4.2 (from cuda-bindings<14,>=13.0.3->torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
271.9   Downloading cuda_pathfinder-1.5.6-py3-none-any.whl.metadata (1.9 kB)
272.2 Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=10.11.0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
272.2   Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
272.5 Collecting mpmath<1.4,>=1.1.0 (from sympy>=1.13.3->torch>=1.11.0->sentence_transformers->-r /app/requirements.txt (line 16))
272.7   Downloading mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
272.9 Collecting oauthlib>=3.0.0 (from requests-oauthlib->kubernetes>=28.1.0->chromadb==0.6.3->-r /app/requirements.txt (line 6))
273.2   Downloading oauthlib-3.3.1-py3-none-any.whl.metadata (7.9 kB)
273.4 Downloading chromadb-0.6.3-py3-none-any.whl (611 kB)
279.7    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 611.1/611.1 kB 99.1 kB/s eta 0:00:00
280.0 Downloading chroma_hnswlib-0.7.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.4 MB)
295.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 156.8 kB/s eta 0:00:00
295.6 Downloading fastapi-0.139.0-py3-none-any.whl (130 kB)
297.1    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 130.3/130.3 kB 83.2 kB/s eta 0:00:00
297.3 Downloading pydantic-2.13.4-py3-none-any.whl (472 kB)
299.6    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 472.3/472.3 kB 200.4 kB/s eta 0:00:00
299.9 Downloading pydantic_core-2.46.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
307.6    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 269.8 kB/s eta 0:00:00
307.8 Downloading numpy-2.4.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.9 MB)
450.6    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.9/16.9 MB 135.6 kB/s eta 0:00:00
450.8 Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
451.5    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.5/73.5 kB 96.1 kB/s eta 0:00:00
451.8 Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
452.1    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.8/78.8 kB 192.6 kB/s eta 0:00:00
452.2 Downloading redis-8.0.1-py3-none-any.whl (502 kB)
455.4    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 502.4/502.4 kB 157.1 kB/s eta 0:00:00
455.4 Downloading python_multipart-0.0.32-py3-none-any.whl (30 kB)
456.1 Downloading requests-2.34.2-py3-none-any.whl (73 kB)
456.5    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.1/73.1 kB 143.5 kB/s eta 0:00:00
456.9 Downloading ollama-0.6.2-py3-none-any.whl (15 kB)
457.2 Downloading aiohttp-3.14.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.8 MB)
467.4    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 175.0 kB/s eta 0:00:00
467.4 Downloading asyncio-4.0.0-py3-none-any.whl (5.6 kB)
467.7 Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
470.4    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 80.7 kB/s eta 0:00:00
470.7 Downloading transformers-5.13.0-py3-none-any.whl (11.5 MB)
573.1    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.5/11.5 MB 115.4 kB/s eta 0:00:00
573.5 Downloading sentence_transformers-5.6.0-py3-none-any.whl (596 kB)
577.7    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 596.4/596.4 kB 138.8 kB/s eta 0:00:00
577.9 Downloading pytz-2026.2-py2.py3-none-any.whl (510 kB)
583.8    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 510.1/510.1 kB 83.9 kB/s eta 0:00:00
584.1 Downloading scikit_learn-1.9.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (9.3 MB)
706.0    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.3/9.3 MB 77.9 kB/s eta 0:00:00
706.2 Downloading scipy-1.17.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (35.3 MB)
1104.1    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.3/35.3 MB 131.5 kB/s eta 0:00:00
1104.5 Downloading textblob-0.20.0-py3-none-any.whl (624 kB)
1109.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 625.0/625.0 kB 130.6 kB/s eta 0:00:00
1109.5 Downloading duckduckgo_search-8.1.1-py3-none-any.whl (18 kB)
1109.9 Downloading rake_nltk-1.0.6-py3-none-any.whl (9.1 kB)
1109.9 Downloading nltk-3.9.4-py3-none-any.whl (1.6 MB)
1119.0    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 169.5 kB/s eta 0:00:00
1119.1 Downloading pypdf2-3.0.1-py3-none-any.whl (232 kB)
1121.0    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 232.6/232.6 kB 131.6 kB/s eta 0:00:00
1121.3 Downloading flask-3.1.3-py3-none-any.whl (103 kB)
1122.5    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.4/103.4 kB 82.6 kB/s eta 0:00:00
1122.8 Downloading flask_cors-6.0.5-py3-none-any.whl (16 kB)
1123.1 Downloading asgiref-3.11.1-py3-none-any.whl (24 kB)
1123.6 Downloading psycopg2_binary-2.9.12-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.3 MB)
1144.6    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.3/4.3 MB 202.7 kB/s eta 0:00:00
1144.9 Downloading asyncpg-0.31.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.0 MB)
1166.5    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 136.9 kB/s eta 0:00:00
1166.9 Downloading aiohappyeyeballs-2.7.1-py3-none-any.whl (15 kB)
1167.3 Downloading aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
1167.6 Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
1167.9 Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
1168.1 Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
1168.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 67.5/67.5 kB 266.5 kB/s eta 0:00:00
1168.6 Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl (278 kB)
1170.1    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 278.2/278.2 kB 181.9 kB/s eta 0:00:00
1170.2 Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
1170.4 Downloading build-1.5.0-py3-none-any.whl (26 kB)
1170.7 Downloading certifi-2026.6.17-py3-none-any.whl (133 kB)
1170.9    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.3/133.3 kB 544.5 kB/s eta 0:00:00
1171.0 Downloading charset_normalizer-3.4.8-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (221 kB)
1172.0    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 221.0/221.0 kB 219.7 kB/s eta 0:00:00
1172.2 Downloading click-8.4.2-py3-none-any.whl (119 kB)
1172.7    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 119.2/119.2 kB 322.6 kB/s eta 0:00:00
1172.9 Downloading frozenlist-1.8.0-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (231 kB)
1174.5    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 231.1/231.1 kB 140.5 kB/s eta 0:00:00
1174.5 Downloading grpcio-1.82.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (6.9 MB)
1206.5    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.9/6.9 MB 218.5 kB/s eta 0:00:00
1206.9 Downloading h11-0.16.0-py3-none-any.whl (37 kB)
1207.5 Downloading httptools-0.8.0-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (464 kB)
1210.1    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 464.7/464.7 kB 176.1 kB/s eta 0:00:00
1210.3 Downloading huggingface_hub-1.22.0-py3-none-any.whl (765 kB)
1216.6    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 765.1/765.1 kB 119.5 kB/s eta 0:00:00
1217.0 Downloading idna-3.18-py3-none-any.whl (65 kB)
1217.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 65.5/65.5 kB 237.5 kB/s eta 0:00:00
1217.4 Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
1217.7 Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
1218.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 134.9/134.9 kB 267.3 kB/s eta 0:00:00
1218.5 Downloading joblib-1.5.3-py3-none-any.whl (309 kB)
1219.1    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 309.1/309.1 kB 543.9 kB/s eta 0:00:00
1219.3 Downloading kubernetes-36.0.2-py2.py3-none-any.whl (4.6 MB)
1243.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 193.2 kB/s eta 0:00:00
1243.2 Downloading lxml-6.1.1-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (5.2 MB)
1276.4    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.2/5.2 MB 168.7 kB/s eta 0:00:00
1276.9 Downloading markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
1276.9 Downloading mmh3-5.2.1-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (103 kB)
1277.4    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.1/103.1 kB 199.9 kB/s eta 0:00:00
1278.4 Downloading multidict-6.7.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (246 kB)
1281.7    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 246.3/246.3 kB 72.3 kB/s eta 0:00:00
1282.0 Downloading narwhals-2.23.0-py3-none-any.whl (458 kB)
1288.5    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 458.9/458.9 kB 69.9 kB/s eta 0:00:00
1288.8 Downloading onnxruntime-1.27.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (18.6 MB)
1400.9    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.6/18.6 MB 144.5 kB/s eta 0:00:00
1401.2 Downloading opentelemetry_api-1.43.0-py3-none-any.whl (61 kB)
1401.4    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.9/61.9 kB 230.2 kB/s eta 0:00:00
1401.8 Downloading opentelemetry_exporter_otlp_proto_grpc-1.43.0-py3-none-any.whl (19 kB)
1402.0 Downloading opentelemetry_exporter_otlp_proto_common-1.43.0-py3-none-any.whl (17 kB)
1402.8 Downloading opentelemetry_proto-1.43.0-py3-none-any.whl (72 kB)
1403.0    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 72.5/72.5 kB 275.2 kB/s eta 0:00:00
1403.2 Downloading opentelemetry_instrumentation_fastapi-0.64b0-py3-none-any.whl (13 kB)
1403.6 Downloading opentelemetry_instrumentation-0.64b0-py3-none-any.whl (35 kB)
1404.4 Downloading opentelemetry_instrumentation_asgi-0.64b0-py3-none-any.whl (15 kB)
1404.7 Downloading opentelemetry_semantic_conventions-0.64b0-py3-none-any.whl (203 kB)
1407.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 203.7/203.7 kB 79.0 kB/s eta 0:00:00
1407.3 Downloading opentelemetry_util_http-0.64b0-py3-none-any.whl (8.2 kB)
1407.4 Downloading opentelemetry_sdk-1.43.0-py3-none-any.whl (178 kB)
1409.7    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 178.9/178.9 kB 84.6 kB/s eta 0:00:00
1409.9 Downloading orjson-3.11.9-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (133 kB)
1411.1    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 134.0/134.0 kB 109.3 kB/s eta 0:00:00
1411.2 Downloading overrides-7.7.0-py3-none-any.whl (17 kB)
1411.8 Downloading packaging-26.2-py3-none-any.whl (100 kB)
1412.5    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.2/100.2 kB 133.1 kB/s eta 0:00:00
1412.7 Downloading posthog-7.22.0-py3-none-any.whl (394 kB)
1415.7    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 394.6/394.6 kB 127.8 kB/s eta 0:00:00
1416.0 Downloading primp-1.3.1-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.3 MB)
1451.8    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.3/5.3 MB 159.1 kB/s eta 0:00:00
1452.1 Downloading propcache-0.5.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (58 kB)
1452.6    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.9/58.9 kB 108.8 kB/s eta 0:00:00
1452.8 Downloading pypika-0.51.1-py2.py3-none-any.whl (60 kB)
1452.9    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.6/60.6 kB 453.4 kB/s eta 0:00:00
1453.2 Downloading python_dotenv-1.2.2-py3-none-any.whl (22 kB)
1453.8 Downloading pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (806 kB)
1460.8    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 806.6/806.6 kB 113.8 kB/s eta 0:00:00
1460.9 Downloading regex-2026.6.28-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (799 kB)
1464.6    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 799.9/799.9 kB 212.9 kB/s eta 0:00:00
1464.8 Downloading rich-15.0.0-py3-none-any.whl (310 kB)
1467.0    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 310.7/310.7 kB 141.9 kB/s eta 0:00:00
1467.2 Downloading safetensors-0.8.0-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (516 kB)
1471.1    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 516.0/516.0 kB 128.3 kB/s eta 0:00:00
1471.5 Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
1471.5 Downloading starlette-1.3.1-py3-none-any.whl (73 kB)
1472.1    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.6/73.6 kB 181.0 kB/s eta 0:00:00
1472.1 Downloading anyio-4.14.1-py3-none-any.whl (124 kB)
1472.7    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 124.9/124.9 kB 342.8 kB/s eta 0:00:00
1473.0 Downloading tenacity-9.1.4-py3-none-any.whl (28 kB)
1473.3 Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
1473.5 Downloading tokenizers-0.22.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.3 MB)
1496.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 143.7 kB/s eta 0:00:00
1496.5 Downloading torch-2.12.1-cp311-cp311-manylinux_2_28_x86_64.whl (532.2 MB)
4796.7    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 532.2/532.2 MB 196.9 kB/s eta 0:00:00
4796.9 Downloading cuda_toolkit-13.0.2-py2.py3-none-any.whl (2.4 kB)
4797.3 Downloading nvidia_cudnn_cu13-9.20.0.48-py3-none-manylinux_2_27_x86_64.whl (366.2 MB)
7101.9    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 366.2/366.2 MB 227.4 kB/s eta 0:00:00
7102.2 Downloading nvidia_cusparselt_cu13-0.8.1-py3-none-manylinux2014_x86_64.whl (170.1 MB)
7890.0    ━━━━━━━━━━━━━━━━━━━━━━━━━━━╸             118.8/170.1 MB 21.6 kB/s eta 0:39:36
7890.0 ERROR: Exception:
7890.0 Traceback (most recent call last):
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_vendor/urllib3/response.py", line 438, in _error_catcher
7890.0     yield
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_vendor/urllib3/response.py", line 561, in read
7890.0     data = self._fp_read(amt) if not fp_closed else b""
7890.0            ^^^^^^^^^^^^^^^^^^
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_vendor/urllib3/response.py", line 527, in _fp_read
7890.0     return self._fp.read(amt) if amt is not None else self._fp.read()
7890.0            ^^^^^^^^^^^^^^^^^^
7890.0   File "/usr/local/lib/python3.11/http/client.py", line 478, in read
7890.0     s = self.fp.read(amt)
7890.0         ^^^^^^^^^^^^^^^^^
7890.0   File "/usr/local/lib/python3.11/socket.py", line 718, in readinto
7890.0     return self._sock.recv_into(b)
7890.0            ^^^^^^^^^^^^^^^^^^^^^^^
7890.0   File "/usr/local/lib/python3.11/ssl.py", line 1314, in recv_into
7890.0     return self.read(nbytes, buffer)
7890.0            ^^^^^^^^^^^^^^^^^^^^^^^^^
7890.0   File "/usr/local/lib/python3.11/ssl.py", line 1166, in read
7890.0     return self._sslobj.read(len, buffer)
7890.0            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
7890.0 TimeoutError: The read operation timed out
7890.0 
7890.0 During handling of the above exception, another exception occurred:
7890.0 
7890.0 Traceback (most recent call last):
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_internal/cli/base_command.py", line 180, in exc_logging_wrapper
7890.0     status = run_func(*args)
7890.0              ^^^^^^^^^^^^^^^
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_internal/cli/req_command.py", line 245, in wrapper
7890.0     return func(self, options, args)
7890.0            ^^^^^^^^^^^^^^^^^^^^^^^^^
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_internal/commands/install.py", line 377, in run
7890.0     requirement_set = resolver.resolve(
7890.0                       ^^^^^^^^^^^^^^^^^
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/resolver.py", line 179, in resolve
7890.0     self.factory.preparer.prepare_linked_requirements_more(reqs)
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_internal/operations/prepare.py", line 552, in prepare_linked_requirements_more
7890.0     self._complete_partial_requirements(
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_internal/operations/prepare.py", line 467, in _complete_partial_requirements
7890.0     for link, (filepath, _) in batch_download:
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_internal/network/download.py", line 183, in __call__
7890.0     for chunk in chunks:
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_internal/cli/progress_bars.py", line 53, in _rich_progress_bar
7890.0     for chunk in iterable:
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_internal/network/utils.py", line 63, in response_chunks
7890.0     for chunk in response.raw.stream(
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_vendor/urllib3/response.py", line 622, in stream
7890.0     data = self.read(amt=amt, decode_content=decode_content)
7890.0            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_vendor/urllib3/response.py", line 560, in read
7890.0     with self._error_catcher():
7890.0   File "/usr/local/lib/python3.11/contextlib.py", line 158, in __exit__
7890.0     self.gen.throw(typ, value, traceback)
7890.0   File "/usr/local/lib/python3.11/site-packages/pip/_vendor/urllib3/response.py", line 443, in _error_catcher
7890.0     raise ReadTimeoutError(self._pool, None, "Read timed out.")
7890.0 pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.
7891.3 
7891.3 [notice] A new release of pip is available: 24.0 -> 26.1.2
7891.3 [notice] To update, run: pip install --upgrade pip
------
[+] build 0/1
 ⠙ Image msjarvis-rebuild-jarvis-dgm-01 Building            8776.4s
Dockerfile.dgm_worker:6

--------------------

   4 |         ca-certificates curl && rm -rf /var/lib/apt/lists/*

   5 |     COPY requirements.txt /app/requirements.txt

   6 | >>> RUN pip install --no-cache-dir -r /app/requirements.txt

   7 |     COPY dgm_worker.py /app/dgm_worker.py

   8 |     CMD ["sh", "-c", "python3 -m uvicorn dgm_worker:app --host 0.0.0.0 --port ${DGM_PORT:-5100}"]

--------------------

failed to solve: process "/bin/sh -c pip install --no-cache-dir -r /app/requirements.txt" did not complete successfully: exit code: 2

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

