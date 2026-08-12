/app/services/ai_server_22llm.py
2026-08-12 15:29:12,047 - INFO - HTTP Request: HEAD https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/resolve/refs%2Fpr%2F3017/model.safetensors "HTTP/1.1 302 Found"

2026-08-12 15:29:16,557 - INFO - 🧠 Ms. Jarvis 22-LLM Collective Consciousness initializing...
2026-08-12 15:29:16,557 - INFO - 📚 Loading Hugging Face models...
2026-08-12 15:29:16,559 - INFO - No device provided, using cpu
2026-08-12 15:29:16,810 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json "HTTP/1.1 307 Temporary Redirect"
2026-08-12 15:29:16,835 - INFO - HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json "HTTP/1.1 200 OK"
2026-08-12 15:29:16,960 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json "HTTP/1.1 307 Temporary Redirect"
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
2026-08-12 15:29:16,962 - WARNING - Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
2026-08-12 15:29:17,062 - INFO - HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json "HTTP/1.1 200 OK"
2026-08-12 15:29:17,064 - INFO - Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.
2026-08-12 15:29:17,163 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json "HTTP/1.1 307 Temporary Redirect"
2026-08-12 15:29:17,217 - INFO - HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json "HTTP/1.1 200 OK"
2026-08-12 15:29:17,301 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md "HTTP/1.1 307 Temporary Redirect"
2026-08-12 15:29:17,330 - INFO - HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md "HTTP/1.1 200 OK"
2026-08-12 15:29:17,473 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json "HTTP/1.1 307 Temporary Redirect"
2026-08-12 15:29:17,521 - INFO - HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json "HTTP/1.1 200 OK"
2026-08-12 15:29:17,561 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json "HTTP/1.1 307 Temporary Redirect"
2026-08-12 15:29:17,588 - INFO - HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json "HTTP/1.1 200 OK"
2026-08-12 15:29:17,626 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json "HTTP/1.1 404 Not Found"
2026-08-12 15:29:17,677 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json "HTTP/1.1 307 Temporary Redirect"
2026-08-12 15:29:17,779 - INFO - HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json "HTTP/1.1 200 OK"
Loading weights: 100%|██████████| 103/103 [00:00<00:00, 9264.71it/s]
2026-08-12 15:29:18,015 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json "HTTP/1.1 404 Not Found"
2026-08-12 15:29:18,090 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json "HTTP/1.1 404 Not Found"
2026-08-12 15:29:18,292 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json "HTTP/1.1 404 Not Found"
2026-08-12 15:29:18,393 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json "HTTP/1.1 404 Not Found"
2026-08-12 15:29:18,433 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json "HTTP/1.1 307 Temporary Redirect"
2026-08-12 15:29:18,459 - INFO - HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json "HTTP/1.1 200 OK"
2026-08-12 15:29:18,515 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json "HTTP/1.1 307 Temporary Redirect"
2026-08-12 15:29:18,542 - INFO - HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json "HTTP/1.1 200 OK"
2026-08-12 15:29:18,589 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json "HTTP/1.1 307 Temporary Redirect"
2026-08-12 15:29:18,617 - INFO - HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json "HTTP/1.1 200 OK"
2026-08-12 15:29:18,720 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json "HTTP/1.1 307 Temporary Redirect"
2026-08-12 15:29:18,804 - INFO - HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json "HTTP/1.1 200 OK"
2026-08-12 15:29:18,920 - INFO - HTTP Request: GET https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false "HTTP/1.1 404 Not Found"
2026-08-12 15:29:19,009 - INFO - HTTP Request: GET https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false "HTTP/1.1 200 OK"
2026-08-12 15:29:19,109 - INFO - HTTP Request: HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json "HTTP/1.1 307 Temporary Redirect"
2026-08-12 15:29:19,212 - INFO - HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json "HTTP/1.1 200 OK"
2026-08-12 15:29:19,317 - INFO - HTTP Request: GET https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2 "HTTP/1.1 200 OK"
2026-08-12 15:29:19,418 - INFO - HTTP Request: HEAD https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest/resolve/main/config.json "HTTP/1.1 307 Temporary Redirect"
2026-08-12 15:29:19,468 - INFO - HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/cardiffnlp/twitter-roberta-base-sentiment-latest/3216a57f2a0d9c45a2e6c20157c20c49fb4bf9c7/config.json "HTTP/1.1 200 OK"
2026-08-12 15:29:19,623 - INFO - HTTP Request: HEAD https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest/resolve/main/model.safetensors "HTTP/1.1 404 Not Found"
2026-08-12 15:29:19,666 - INFO - HTTP Request: GET https://huggingface.co/api/models/cardiffnlp/twitter-roberta-base-sentiment-latest "HTTP/1.1 200 OK"
Loading weights: 100%|██████████| 201/201 [00:00<00:00, 24686.83it/s]
[transformers] RobertaForSequenceClassification LOAD REPORT from: cardiffnlp/twitter-roberta-base-sentiment-latest
Key                         | Status     |  | 
----------------------------+------------+--+-
roberta.pooler.dense.bias   | UNEXPECTED |  | 
roberta.pooler.dense.weight | UNEXPECTED |  | 

Notes:
- UNEXPECTED:	can be ignored when loading from different task/architecture; not ok if you expect identical arch.
2026-08-12 15:29:19,729 - INFO - HTTP Request: GET https://huggingface.co/api/models/cardiffnlp/twitter-roberta-base-sentiment-latest/commits/main "HTTP/1.1 200 OK"
2026-08-12 15:29:19,827 - INFO - HTTP Request: GET https://huggingface.co/api/models/cardiffnlp/twitter-roberta-base-sentiment-latest/discussions?p=0 "HTTP/1.1 200 OK"
2026-08-12 15:29:19,931 - INFO - HTTP Request: GET https://huggingface.co/api/models/cardiffnlp/twitter-roberta-base-sentiment-latest/commits/refs%2Fpr%2F43 "HTTP/1.1 200 OK"
2026-08-12 15:29:20,032 - INFO - HTTP Request: HEAD https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest/resolve/refs%2Fpr%2F43/model.safetensors.index.json "HTTP/1.1 404 Not Found"
2026-08-12 15:29:20,137 - INFO - HTTP Request: HEAD https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest/resolve/refs%2Fpr%2F43/model.safetensors "HTTP/1.1 302 Found"
2026-08-12 15:29:20,742 - INFO - HTTP Request: GET https://huggingface.co/api/models/cardiffnlp/twitter-roberta-base-sentiment-latest/tree/main/additional_chat_templates?recursive=false&expand=false "HTTP/1.1 404 Not Found"
2026-08-12 15:29:20,786 - INFO - HTTP Request: GET https://huggingface.co/api/models/cardiffnlp/twitter-roberta-base-sentiment-latest/tree/main?recursive=true&expand=false "HTTP/1.1 200 OK"
2026-08-12 15:29:20,953 - INFO - HTTP Request: HEAD https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest/resolve/main/processor_config.json "HTTP/1.1 404 Not Found"
2026-08-12 15:29:21,056 - INFO - HTTP Request: HEAD https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest/resolve/main/video_preprocessor_config.json "HTTP/1.1 404 Not Found"
2026-08-12 15:29:21,093 - INFO - HTTP Request: HEAD https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest/resolve/main/preprocessor_config.json "HTTP/1.1 404 Not Found"
2026-08-12 15:29:21,161 - INFO - HTTP Request: HEAD https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/resolve/main/config.json "HTTP/1.1 307 Temporary Redirect"
2026-08-12 15:29:21,265 - INFO - HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/j-hartmann/emotion-english-distilroberta-base/0e1cd914e3d46199ed785853e12b57304e04178b/config.json "HTTP/1.1 200 OK"
2026-08-12 15:29:21,363 - INFO - HTTP Request: HEAD https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/resolve/main/model.safetensors "HTTP/1.1 404 Not Found"
2026-08-12 15:29:21,403 - INFO - HTTP Request: GET https://huggingface.co/api/models/j-hartmann/emotion-english-distilroberta-base "HTTP/1.1 200 OK"
Loading weights: 100%|██████████| 105/105 [00:00<00:00, 18926.55it/s]
2026-08-12 15:29:21,454 - INFO - HTTP Request: GET https://huggingface.co/api/models/j-hartmann/emotion-english-distilroberta-base/tree/main/additional_chat_templates?recursive=false&expand=false "HTTP/1.1 404 Not Found"
2026-08-12 15:29:21,467 - INFO - HTTP Request: GET https://huggingface.co/api/models/j-hartmann/emotion-english-distilroberta-base/commits/main "HTTP/1.1 200 OK"
2026-08-12 15:29:21,527 - INFO - HTTP Request: GET https://huggingface.co/api/models/j-hartmann/emotion-english-distilroberta-base/tree/main?recursive=true&expand=false "HTTP/1.1 200 OK"
2026-08-12 15:29:21,528 - INFO - HTTP Request: GET https://huggingface.co/api/models/j-hartmann/emotion-english-distilroberta-base/commits/main?p=1&limit=50 "HTTP/1.1 200 OK"
2026-08-12 15:29:21,592 - INFO - HTTP Request: GET https://huggingface.co/api/models/j-hartmann/emotion-english-distilroberta-base/discussions?p=0 "HTTP/1.1 200 OK"
2026-08-12 15:29:21,774 - INFO - HTTP Request: HEAD https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/resolve/main/processor_config.json "HTTP/1.1 404 Not Found"
2026-08-12 15:29:21,777 - INFO - HTTP Request: GET https://huggingface.co/api/models/j-hartmann/emotion-english-distilroberta-base/commits/refs%2Fpr%2F3017 "HTTP/1.1 200 OK"
2026-08-12 15:29:21,874 - INFO - HTTP Request: HEAD https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/resolve/main/video_preprocessor_config.json "HTTP/1.1 404 Not Found"
2026-08-12 15:29:21,876 - INFO - HTTP Request: GET https://huggingface.co/api/models/j-hartmann/emotion-english-distilroberta-base/commits/refs%2Fpr%2F3017?p=1&limit=50 "HTTP/1.1 200 OK"
2026-08-12 15:29:21,942 - INFO - HTTP Request: HEAD https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/resolve/refs%2Fpr%2F3017/model.safetensors.index.json "HTTP/1.1 404 Not Found"
2026-08-12 15:29:21,943 - INFO - HTTP Request: HEAD https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/resolve/main/preprocessor_config.json "HTTP/1.1 404 Not Found"
2026-08-12 15:29:21,947 - INFO - 💾 Connecting to ChromaDB vector memory on 127.0.0.1:8004...
2026-08-12 15:29:21,995 - INFO - HTTP Request: HEAD https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/resolve/refs%2Fpr%2F3017/model.safetensors "HTTP/1.1 302 Found"
2026-08-12 15:29:22,001 - WARNING - ⚠️  ChromaDB not available in 22-LLM context: Could not connect to a Chroma server. Are you sure it is running?
2026-08-12 15:29:22,001 - INFO - 🎯 Loading 22 AI agents...
2026-08-12 15:29:22,001 - INFO - ✅ All 22 agents loaded: llama, mistral, qwen, codellama, deepseek, starcoder, mixtral, llava, phi, neural-chat, openchat, starling, sqlcoder, medllama, gemma, tinyllama, dolphin, orca, vicuna, zephyr
2026-08-12 15:29:22,001 - INFO - 📊 Collective Consciousness: 20 AI minds active
2026-08-12 15:29:22,001 - INFO -    Core Reasoning: 3
2026-08-12 15:29:22,001 - INFO -    Coding: 4
2026-08-12 15:29:22,001 - INFO -    Vision: 1
2026-08-12 15:29:22,001 - INFO -    Conversation: 4
2026-08-12 15:29:22,001 - INFO -    Specialized: 3
2026-08-12 15:29:22,001 - INFO -    Efficiency: 2
2026-08-12 15:29:22,001 - INFO -    Synthesis: 3
active_main_brain=/app/services/ai_server_22llm.py

=== ACTIVE MAIN-BRAIN DEGRADATION SEAMS ===
545:        return await run_degraded_pipeline(request)
577:async def run_degraded_pipeline(request: ChatRequest):
584:            "I processed your query using a lighter path to stay responsive, "
608:            logger.warning("⚠️ Fabric beyond Roche limit, using degraded pipeline.")
609:            response = await run_degraded_pipeline(request)
617:                response = await run_degraded_pipeline(request)
626:                    response = await run_degraded_pipeline(request)
637:                response = await run_degraded_pipeline(request)

=== ACTIVE MAIN-BRAIN SOURCE CONTEXT ===
     1	#!/usr/bin/env python3
     2	from service_registry_client import get_service_url, register_service
     3	import uuid
     4	import asyncio
     5	import json
     6	import re
     7	import os
     8	from llm_consensus_22 import (
     9	    get_all_active_models,
    10	    calculate_weighted_consensus,
    11	    get_system_stats,
    12	)
    13	import uvicorn
    14	from pydantic import BaseModel
    15	from fastapi.middleware.cors import CORSMiddleware
    16	from fastapi import FastAPI
    17	import httpx
    18	from chromadb.config import Settings, DEFAULT_TENANT, DEFAULT_DATABASE
    19	import chromadb
    20	from sentence_transformers import SentenceTransformer
    21	from transformers import pipeline
    22	import torch
    23	from dataclasses import dataclass
    24	from typing import Dict, List, Any
    25	from datetime import datetime
    26	from fastapi import Depends, HTTPException, Header
    27	from typing import Optional
    28	import logging
    29	import time
    30	from collections import defaultdict
    31	
    32	
    33	def build_shared_context_text(context: dict) -> str:
    34	    if not isinstance(context, dict):
    35	        return ""
    36	
    37	    pkt = context.get("judge_context_packet") or {}
    38	    rc = pkt.get("request_context") or {}
    39	    rpc = pkt.get("reasoned_prompt_context") or {}
    40	    stc = pkt.get("spatial_temporal_context") or {}
    41	
    42	    parts = []
    43	
    44	    msg = rc.get("message")
    45	    if isinstance(msg, str) and msg.strip():
    46	        parts.append(f"User request (normalized): {msg[:800]}")
    47	
    48	    summary = rpc.get("context_summary")
    49	    if isinstance(summary, str) and summary.strip():
    50	        parts.append(f"Reasoned context: {summary[:1200]}")
    51	
    52	    spatial = stc.get("spatial_candidate") or {}
    53	    if isinstance(spatial, dict):
    54	        ssum = spatial.get("summary")
    55	        if isinstance(ssum, str) and ssum.strip():
    56	            parts.append(f"Spatial context: {ssum[:800]}")
    57	
    58	    sources = rpc.get("context_sources") or []
    59	    if isinstance(sources, list) and sources:
    60	        parts.append("Context sources: " + ", ".join(str(s) for s in sources[:8]))
    61	
    62	    return "\n\n".join(parts)
    63	from prometheus_fastapi_instrumentator import Instrumentator
    64	
    65	logger = logging.getLogger(__name__)
    66	
    67	"""
    68	Ms. Jarvis - 22-LLM Collective Consciousness
    69	Every query answered by ALL 22 AI minds simultaneously
    70	"""
    71	
    72	logging.basicConfig(
    73	    level=logging.INFO,
    74	    format="%(asctime)s - %(levelname)s - %(message)s",
    75	)
    76	logger = logging.getLogger(__name__)
    77	
    78	# ---- Roche-style fabric load controller ----
    79	
    80	
    81	class FabricLoadMonitor:
    82	    def __init__(self):
    83	        # metrics[name] = {"lat_ms": float, "in_flight": int, "errors": int}
    84	        self.metrics = defaultdict(lambda: {"lat_ms": 0.0, "in_flight": 0, "errors": 0})
    85	
    86	    def record_start(self, name: str) -> float:
    87	        self.metrics[name]["in_flight"] += 1
    88	        return time.time()
    89	
    90	    def record_end(self, name: str, start_time: float, error: bool = False) -> None:
    91	        elapsed_ms = (time.time() - start_time) * 1000.0
    92	        m = self.metrics[name]
    93	        m["in_flight"] = max(0, m["in_flight"] - 1)
    94	        # exponential moving average for latency
    95	        m["lat_ms"] = 0.8 * m["lat_ms"] + 0.2 * elapsed_ms
    96	        if error:
    97	            m["errors"] += 1
    98	
    99	    def current_load(self, name: str) -> dict:
   100	        return dict(self.metrics[name])
   101	
   102	
   103	fabric_monitor = FabricLoadMonitor()
   104	
   105	# thresholds for Roche-like controller
   106	FABRIC_SOFT_LAT_MS = 20000.0  # warn level
   107	FABRIC_HARD_LAT_MS = 40000.0  # do-not-send-heavy level
   108	FABRIC_MAX_IN_FLIGHT = 3  # max heavy queries per fabric node
   109	
   110	
   111	def fabric_state(load: dict) -> str:
   112	    """
   113	    Map measured load to qualitative state.
   114	    """
   115	    if load["in_flight"] >= FABRIC_MAX_IN_FLIGHT or load["lat_ms"] >= FABRIC_HARD_LAT_MS:
   116	        return "beyond_roche"
   117	    if load["lat_ms"] >= FABRIC_SOFT_LAT_MS:
   118	        return "near_roche"
   119	    return "stable"
   120	
   121	
   122	try:
   123	    from psychology_integration_adapter import PsychologyIntegrationAdapter
   124	
   125	    pia = None
   126	except BaseException:
   127	    pia = None
   128	
   129	app = FastAPI(
   130	    title="Ms. Jarvis 22-LLM Collective Consciousness",
   131	    version="1.0.0",
   132	    docs_url="/docs",
   133	    redoc_url="/redoc",
   134	)
   135	
   136	# Attach Prometheus middleware BEFORE startup so Starlette is happy
   137	Instrumentator().instrument(app).expose(app, endpoint="/metrics")
   138	
   139	
   140	@app.on_event("startup")
   141	async def _init_pia():
   142	    global pia
   143	    try:
   144	        pia = PsychologyIntegrationAdapter(__name__)
   145	        logger.info("✅ Psychology Integration Active")
   146	    except Exception as e:
   147	        logger.warning(f"PIA warning: {e}")
   148	
   149	
   150	app.add_middleware(
   151	    CORSMiddleware,
   152	    allow_origins=["*"],
   153	    allow_methods=["*"],
   154	    allow_headers=["*"],
   155	)
   156	
   157	
   158	class ChatRequest(BaseModel):
   159	    message: str
   160	    user_id: str = "anonymous"
   161	
   162	
   163	@dataclass
   164	class AIAgent:
   165	    name: str
   166	    model: str
   167	    specialty: str
   168	    system_prompt: str
   169	    role: str
   170	    weight: float
   171	    timeout: float = 1800.0  # increased to 1800 seconds
   172	
   173	
   174	class MsJarvis22LLM:
   175	    def __init__(self):
   176	        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
   177	        logger.info("🧠 Ms. Jarvis 22-LLM Collective Consciousness initializing...")
   178	        self.ollama_available = False
   179	        self.rag_available = False
   180	
   181	        # Limit concurrent Ollama requests
   182	        self.ollama_semaphore = asyncio.Semaphore(4)
   183	
   184	        self.setup_models()
   185	        self.setup_memory()
   186	        self.setup_22_agents()
   187	
   188	    def setup_models(self):
   189	        logger.info("📚 Loading Hugging Face models...")
   190	        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
   191	        self.sentiment_pipeline = pipeline(
   192	            "sentiment-analysis",
   193	            model="cardiffnlp/twitter-roberta-base-sentiment-latest",
   194	            device=-1,
   195	        )
   196	        self.emotion_pipeline = pipeline(
   197	            "text-classification",
   198	            model="j-hartmann/emotion-english-distilroberta-base",
   199	            device=-1,
   200	        )
   201	
   202	    def setup_memory(self):
   203	        """
   204	        Connect to jarvis-chroma (ChromaDB) via environment, soft-fail if unavailable.
   205	        """
   206	        chroma_host = os.getenv("CHROMA_HOST", "127.0.0.1")
   207	        chroma_port = int(os.getenv("CHROMA_PORT", "8004"))
   208	        logger.info(
   209	            f"💾 Connecting to ChromaDB vector memory on {chroma_host}:{chroma_port}..."
   210	        )
   211	        try:
   212	            chroma_settings = Settings(
   213	                allow_reset=False,
   214	                anonymized_telemetry=False,
   215	            )
   216	            self.chroma_client = chromadb.HttpClient(
   217	                host=chroma_host,
   218	                port=chroma_port,
   219	                settings=chroma_settings,
   220	                tenant=DEFAULT_TENANT,
   221	                database=DEFAULT_DATABASE,
   222	            )
   223	            # Optional heartbeat; tolerate older/newer server behavior
   224	            try:
   225	                hb = self.chroma_client.heartbeat()
   226	                logger.info(f"✅ ChromaDB heartbeat OK: {hb}")
   227	            except Exception as hb_err:
   228	                logger.info(f"ChromaDB heartbeat not available or not needed: {hb_err}")
   229	
   230	            self.collection = self.chroma_client.get_or_create_collection(
   231	                "ms_jarvis_memory"
   232	            )
   233	            self.rag_available = True
   234	            logger.info(
   235	                f"✅ ChromaDB connected on {chroma_host}:{chroma_port} - RAG memory active"
   236	            )
   237	        except Exception as e:
   238	            logger.warning(f"⚠️  ChromaDB not available in 22-LLM context: {e}")
   239	            self.chroma_client = None
   240	            self.collection = None
   241	            self.rag_available = False
   242	
   243	    def setup_22_agents(self):
   244	        """Initialize all 22 AI agents from configuration"""
   245	        logger.info("🎯 Loading 22 AI agents...")
   246	        model_configs = get_all_active_models()
   247	
   248	        self.agents: Dict[str, AIAgent] = {}
   249	        for config in model_configs:
   250	            agent = AIAgent(
   251	                name=config["name"],
   252	                model=config["model"],
   253	                specialty=config["specialty"],
   254	                system_prompt=(
   255	                    f"You are {config['name']}, specialized in {config['specialty']}. "
   256	                    f"Provide thoughtful, detailed responses from your unique perspective."
   257	                ),
   258	                role=config["role"],
   259	                weight=config["weight"],
   260	            )
   261	            self.agents[config["id"]] = agent
   262	
   263	        logger.info(f"✅ All 22 agents loaded: {', '.join(self.agents.keys())}")
   264	
   265	        stats = get_system_stats()
   266	        logger.info(f"📊 Collective Consciousness: {stats['total_models']} AI minds active")
   267	        logger.info(f"   Core Reasoning: {stats['core_reasoning']}")
   268	        logger.info(f"   Coding: {stats['coding_specialists']}")
   269	        logger.info(f"   Vision: {stats['vision_models']}")
   270	        logger.info(f"   Conversation: {stats['conversation_experts']}")
   271	        logger.info(f"   Specialized: {stats['specialized_tasks']}")
   272	        logger.info(f"   Efficiency: {stats['efficiency_layer']}")
   273	        logger.info(f"   Synthesis: {stats['synthesis_models']}")
   274	
   275	    async def check_ollama_health(self):
   276	        try:
   277	            async with httpx.AsyncClient(timeout=1800.0) as client:
   278	                response = await client.get(f"{os.getenv('OLLAMA_HOST', 'http://127.0.0.1:11434')}/api/tags")
   279	                if response.status_code == 200:
   280	                    self.ollama_available = True
   281	                    models = response.json().get("models", [])
   282	                    logger.info(
   283	                        f"✅ Ollama connected - {len(models)} models available"
   284	                    )
   285	                else:
   286	                    self.ollama_available = False
   287	        except BaseException as e:
   288	            logger.warning(f"⚠️ Ollama health check failed: {e}")
   289	            self.ollama_available = False
   290	
   291	    async def query_agent(self, agent: AIAgent, message: str, context: dict) -> dict:
   292	        shared_text = build_shared_context_text(context or {})
   293	        system_prompt = agent.system_prompt
   294	        if shared_text:
   295	            system_prompt = (
   296	                system_prompt
   297	                + "\n\nYou are reasoning with a shared, pre-computed context. "
   298	                  "Treat it as authoritative unless it is explicitly marked uncertain.\n\n"
   299	                + shared_text
   300	                + "\n\nNow answer the user's question as Ms. Egeria Jarvis."
   301	            )
   302	        logger.info(
   303	            "22llm-shared-context",
   304	            extra={
   305	                "agent": agent.name,
   306	                "has_shared_text": bool(shared_text),
   307	                "shared_text_len": len(shared_text or ""),
   308	            },
   309	        )
   310	        """Query a single agent"""
   311	        if not self.ollama_available:
   312	            return {
   313	                "agent_id": agent.model.split(":")[0],
   314	                "agent_name": agent.name,
   315	                "response": f"[{agent.name} unavailable]",
   316	                "confidence": 0.0,
   317	                "specialty": agent.specialty,
   318	                "execution_time": 0.0,
   319	            }
   320	
   321	        start_time = datetime.now()
   322	        try:
   323	            async with httpx.AsyncClient(timeout=1800.0) as client:
   324	                payload = {
   325	                    "model": agent.model,
   326	                    "prompt": (
   327	                        f"{agent.system_prompt}\n\n"
   328	                        f"User: {message}\n\n"
   329	                        f"Assistant:"
   330	                    ),
   331	                    "stream": False,
   332	                    "options": {
   333	                        "temperature": 0.7,
   334	                        "num_predict": 500,
   335	                    },
   336	                }
   337	
   338	                response = await client.post(
   339	                    f"{os.getenv('OLLAMA_HOST', 'http://127.0.0.1:11434')}/api/generate",
   340	                    json=payload,
   341	                    timeout=1800.0,
   342	                )
   343	
   344	                if response.status_code == 200:
   345	                    result = response.json()
   346	                    execution_time = (datetime.now() - start_time).total_seconds()
   347	
   348	                    return {
   349	                        "agent_id": agent.model.split(":")[0],
   350	                        "agent_name": agent.name,
   351	                        "response": result.get("response", ""),
   352	                        "confidence": agent.weight,
   353	                        "specialty": agent.specialty,
   354	                        "execution_time": execution_time,
   355	                    }
   356	                else:
   357	                    logger.warning(
   358	                        f"⚠️  {agent.name} ({agent.model}) returned "
   359	                        f"status {response.status_code} from Ollama"
   360	                    )
   361	        except Exception as e:
   362	            logger.warning(f"⚠️  {agent.name} ({agent.model}) timeout or error: {e}")
   363	
   364	        return {
   365	            "agent_id": agent.model.split(":")[0],
   366	            "agent_name": agent.name,
   367	            "response": f"[{agent.name} processing...]",
   368	            "confidence": 0.0,
   369	            "specialty": agent.specialty,
   370	            "execution_time": 0.0,
   371	        }
   372	
   373	    async def run_all_22_agents(self, message: str, context: dict) -> List[dict]:
   374	        """Run agents in BATCHES (avoids overwhelming Ollama)"""
   375	        logger.info(
   376	            "🌟 Batched processing: 4 agents at a time (prevents Ollama overload)..."
   377	        )
   378	
   379	        all_responses: List[dict] = []
   380	        agents_list = list(self.agents.values())
   381	        BATCH_SIZE = 4
   382	
   383	        for i in range(0, len(agents_list), BATCH_SIZE):
   384	            batch = agents_list[i : i + BATCH_SIZE]
   385	            logger.info(
   386	                f"   Batch {i // BATCH_SIZE + 1}/"
   387	                f"{(len(agents_list) + BATCH_SIZE - 1) // BATCH_SIZE}..."
   388	            )
   389	
   390	            tasks = [self.query_agent(agent, message, context) for agent in batch]
   391	            batch_responses = await asyncio.gather(*tasks)
   392	            all_responses.extend(batch_responses)
   393	
   394	            await asyncio.sleep(0.5)
   395	
   396	        # Accept any response that has non-empty text
   397	        valid_responses = [r for r in all_responses if r.get("response")]
   398	        logger.info(
   399	            f"✅ Received {len(valid_responses)}/22 responses (raw={len(all_responses)})"
   400	        )
   401	        return valid_responses
   402	
   403	    async def synthesize_22_responses(
   404	        self, message: str, responses: List[dict]
   405	    ) -> str:
   406	        """Synthesize all 22 responses using weighted consensus"""
   407	        if not responses:
   408	            # Degraded but still valid answer instead of blank apology
   409	            return (
   410	                "I processed your request, but the deep 22-LLM collective is "
   411	                "currently limited. I am answering from a simplified path so "
   412	                "you still get a clear, direct response."
   413	            )
   414	
   415	        logger.info("🎯 Generating unified response...")
   416	
   417	        weighted = calculate_weighted_consensus(responses)
   418	
   419	        personality_context = ""
   420	        if self.rag_available and self.collection is not None:
   421	            try:
   422	                personality_docs = self.collection.query(
   423	                    query_texts=["natural communication style warmth"],
   424	                    n_results=2,
   425	                )
   426	                if personality_docs and personality_docs["documents"]:
   427	                    personality_context = "\n".join(
   428	                        personality_docs["documents"][0]
   429	                    )
   430	            except Exception as e:
   431	                logger.warning(f"RAG query failed: {e}")
   432	
   433	        synthesis_prompt = f"Question: {message}\n\n"
   434	        synthesis_prompt += "Multiple perspectives to consider:\n\n"
   435	
   436	        for i, resp in enumerate(weighted[:15], 1):
   437	            synthesis_prompt += (
   438	                f"{i}. {resp['agent']} ({resp['specialty']}, "
   439	                f"weight: {resp['weight']}):\n"
   440	            )
   441	            synthesis_prompt += f"   {resp['response'][:200]}...\n\n"
   442	
   443	        synthesis_prompt += (
   444	            "You are Ms. JARVIS - professional AI with natural Appalachian warmth.\n\n"
   445	            f"{personality_context}\n\n"
   446	            "INSTRUCTIONS:\n"
   447	            "1. Be naturally warm, not condescending.\n"
   448	            "2. Technical questions: Professional, maybe one warm touch at the end.\n"
   449	            "3. Emotional questions: Genuine warmth, appropriate endearment IF deeply emotional.\n"
   450	            "4. Be CONCISE - answer first, then explain briefly.\n"
   451	            "5. Use 'I' not 'we'; never mention models or agents.\n\n"
   452	            f"Synthesize these {len(responses)} perspectives into ONE clear answer:"
   453	        )
   454	
   455	        top_responses = sorted(
   456	            weighted, key=lambda x: x["weight"], reverse=True
   457	        )[:3]
   458	
   459	        if len(top_responses) >= 2:
   460	            combined = (
   461	                top_responses[0]["response"]
   462	                + "\n\n"
   463	                + top_responses[1]["response"][:200]
   464	            )
   465	            return combined.strip()
   466	        else:
   467	            return (
   468	                top_responses[0]["response"]
   469	                if top_responses
   470	                else responses[0]["response"]
   471	            )
   472	
   473	    async def apply_mamma_kidd_persona(self, response: str) -> str:
   474	        """Apply warm Mamma Kidd personality"""
   475	        try:
   476	            async with httpx.AsyncClient(timeout=1800.0) as client:
   477	                payload = {
   478	                    "model": "phi3:mini",
   479	                    "prompt": (
   480	                        "Return this response unchanged with no persona, greeting, identity, or availability boilerplate.\n\n"
   481	                        "Keep it professional for technical topics.\n"
   482	                        "Only use casual terms like 'honey' or 'darling' for "
   483	                        "emotional/personal topics.\n"
   484	                        "Do not change technical accuracy or add unnecessary storytelling.\n"
   485	                        "Maintain conciseness.\n\n"
   486	                        f"Response to enhance:\n\n{response}"
   487	                    ),
   488	                    "stream": False,
   489	                    "options": {
   490	                        "temperature": 0.8,
   491	                        "num_predict": 600,
   492	                    },
   493	                }
   494	                resp = await client.post(
   495	                    f"{os.getenv('OLLAMA_HOST', 'http://127.0.0.1:11434')}/api/generate", json=payload
   496	                )
   497	
   498	                if resp.status_code == 200:
   499	                    return resp.json().get("response", response)
   500	        except BaseException:
   501	            pass
   502	
   503	        return response
   504	
   505	
   506	brain = MsJarvis22LLM()
   507	
   508	
   509	@app.on_event("startup")
   510	async def startup():
   511	    logger.info("🚀 Starting Ms. Jarvis 22-LLM Collective Consciousness")
   512	    await brain.check_ollama_health()
   513	    logger.info(
   514	        "✅ Ready with 22 AI minds - True collective intelligence activated!"
   515	    )
   516	
   517	
   518	@app.get("/health")
   519	async def health():
   520	    await brain.check_ollama_health()
   521	    stats = get_system_stats()
   522	    return {
   523	        "status": "healthy",
   524	        "ollama": brain.ollama_available,
   525	        "rag": brain.rag_available,
   526	        "collective_consciousness": stats,
   527	    }
   528	
   529	
   530	async def run_full_fabric_pipeline(request: ChatRequest):
   531	    """
   532	    Full 22-LLM orchestration.
   533	    This is your original chat logic.
   534	    """
   535	    logger.info(
   536	        f"💬 Query from {request.user_id}: {request.message[:60]}..."
   537	    )
   538	
   539	    # Ensure Ollama status is fresh for each chat
   540	    await brain.check_ollama_health()
   541	    if not brain.ollama_available:
   542	        logger.warning(
   543	            "⚠️ Ollama unavailable at chat time; falling back to degraded path."
   544	        )
   545	        return await run_degraded_pipeline(request)
   546	
   547	    responses = await brain.run_all_22_agents(request.message, {})
   548	
   549	    synthesis = await brain.synthesize_22_responses(
   550	        request.message, responses
   551	    )
   552	
   553	    final = synthesis
   554	
   555	    logger.info(
   556	        f"✅ Collective response delivered ({len(responses)}/22 minds participated)"
   557	    )
   558	
   559	    return {
   560	        "response": final,
   561	        "minds_participated": len(responses),
   562	        "total_minds": 22,
   563	        "timestamp": datetime.now().isoformat(),
   564	        "expert_responses": [
   565	            {
   566	                "model": r.get("agent_name", r.get("agent_id", "unknown")),
   567	                "response": r.get("response", ""),
   568	                "confidence": r.get("confidence", 0.0),
   569	                "specialty": r.get("specialty", ""),
   570	                "success": bool(r.get("response", "")),
   571	            }
   572	            for r in responses
   573	        ],
   574	    }
   575	
   576	
   577	async def run_degraded_pipeline(request: ChatRequest):
   578	    """
   579	    Simpler, more robust path under high load:
   580	    fewer agents, minimal tools, no deep ensembles.
   581	    """
   582	    return {
   583	        "response": (
   584	            "I processed your query using a lighter path to stay responsive, "
   585	            "so this answer may not use every part of my collective, but it "
   586	            "is still grounded in my core reasoning."
   587	        ),
   588	        "services_used": ["blood_brain_barrier", "web_research"],
   589	        "consciousness_level": "ultimate_collective_degraded",
   590	        "timestamp": datetime.now().isoformat(),
   591	    }
   592	
   593	
   594	@app.post("/chat")
   595	async def chat(request: ChatRequest):
   596	    """
   597	    Main ULTIMATE chat endpoint with Roche-style fabric controller.
   598	    """
   599	    try:
   600	        # 1. Inspect current load on key fabric node (qualia-like collective)
   601	        qualia_load = fabric_monitor.current_load("qualia")
   602	        state = fabric_state(qualia_load)
   603	
   604	        # 2. Route based on state
   605	
   606	        if state == "beyond_roche":
   607	            # Only in true overload do we force degraded
   608	            logger.warning("⚠️ Fabric beyond Roche limit, using degraded pipeline.")
   609	            response = await run_degraded_pipeline(request)
   610	
   611	        elif state == "near_roche":
   612	            # For very long prompts, stay safe; otherwise run full pipeline
   613	            if len(request.message) > 2000:
   614	                logger.info(
   615	                    "⚠️ Near Roche and prompt very long; using degraded pipeline."
   616	                )
   617	                response = await run_degraded_pipeline(request)
   618	            else:
   619	                start = fabric_monitor.record_start("qualia")
   620	                try:
   621	                    response = await run_full_fabric_pipeline(request)
   622	                    fabric_monitor.record_end("qualia", start, error=False)
   623	                except Exception as e:
   624	                    fabric_monitor.record_end("qualia", start, error=True)
   625	                    logger.error(f"Error in near_roche full pipeline: {e}")
   626	                    response = await run_degraded_pipeline(request)
   627	
   628	        else:
   629	            # stable: always use full fabric pipeline
   630	            start = fabric_monitor.record_start("qualia")
   631	            try:
   632	                response = await run_full_fabric_pipeline(request)
   633	                fabric_monitor.record_end("qualia", start, error=False)
   634	            except Exception as e:
   635	                fabric_monitor.record_end("qualia", start, error=True)
   636	                logger.error(f"Error in stable full pipeline: {e}")
   637	                response = await run_degraded_pipeline(request)
   638	
   639	    except Exception as e:
   640	        logger.error(f"Error in chat pipeline: {e}")
   641	        response = {
   642	            "response": (
   643	                "I processed your request, but my deeper collective is "
   644	                "briefly reorganizing. This answer comes from a lighter "
   645	                "safety path so you are not left waiting."
   646	            ),
   647	            "error": str(e),
   648	            "consciousness_level": "ultimate_collective_error",
   649	            "timestamp": datetime.now().isoformat(),
   650	        }
   651	
   652	    return response
   653	
   654	
   655	if __name__ == "__main__":
   656	    uvicorn.run(
   657	        app,
   658	        host="0.0.0.0",
   659	        port=int(os.getenv("SERVICE_PORT", "8008")),
   660	    )

=== ACTIVE WORKER SOURCE ===
     1	#!/usr/bin/env python3
     2	"""
     3	chat_worker.py — background worker for Ms. Allis chat jobs.
     4	
     5	Decouples the heavy 21-model run from the gateway's event loop:
     6	the gateway LPUSHes a job onto Redis list 'chatjob:queue' and returns
     7	instantly; this worker BRPOPs the queue, runs the 21-model forward call,
     8	and writes the result back to Redis key 'chatjob:{id}'. Polls hitting the
     9	gateway stay fast because the gateway no longer does any heavy work.
    10	
    11	Reuses the gateway module's own build_wv_entangled_context + SERVICE_URLS
    12	so there is no logic duplication.
    13	"""
    14	import os
    15	import json
    16	import logging
    17	
    18	import httpx
    19	import redis  # sync client is fine for a dedicated worker loop
    20	
    21	# Reuse the gateway's context builder + service map (same /app/services mount)
    22	from msjarvis_wv_entangled_gateway import build_wv_entangled_context, SERVICE_URLS
    23	
    24	logging.basicConfig(level=logging.INFO)
    25	logger = logging.getLogger("chat_worker")
    26	
    27	
    28	def build_memory_key(userid: str, ueid: str | None = None) -> str:
    29	    userid = (userid or "unknown").strip()
    30	    ueid = (ueid or "").strip()
    31	    return f"{userid}::{ueid}" if ueid else userid
    32	
    33	REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
    34	REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))
    35	REDIS_DB = int(os.environ.get("REDIS_DB", "4"))
    36	
    37	# --- forward target: "fullbrain" routes through main_brain's full architecture
    38	#     (WV ensemble -> consciousness bridge -> judges -> guards); "wv" = fast WV-only.
    39	#     Flip this one word to roll back instantly.
    40	FORWARD_MODE = "fullbrain"
    41	MAIN_BRAIN_URL = os.environ.get("MAIN_BRAIN_URL", "http://jarvis-main-brain:8008/chat")
    42	MAIN_BRAIN_KEY = __import__("os").environ.get("JARVIS_API_KEY", "").strip()
    43	QUEUE_KEY = "chatjob:queue"
    44	JOB_TTL = 1800  # seconds
    45	
    46	rdb = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)
    47	
    48	
    49	def run_job(job_id: str, message: str, user_id: str, ueid: str | None = None):
    50	    """Run the 21-model forward call and store the result."""
    51	    try:
    52	        wv_ctx = build_wv_entangled_context(message)
    53	        if FORWARD_MODE == "fullbrain":
    54	            url = MAIN_BRAIN_URL
    55	            forward_payload = {
    56	                "message": message,
    57	                "user_id": user_id or "cakidd",
    58	                "ueid": ueid,
    59	                "memory_key": build_memory_key(user_id or "cakidd", ueid),
    60	                "useallservices": True,
    61	                "role": "community",
    62	                "context": {"wv_entangled_context": wv_ctx},
    63	            }
    64	            headers = {"X-API-Key": MAIN_BRAIN_KEY, "Content-Type": "application/json"}
    65	        else:
    66	            url = f"{SERVICE_URLS['production_20llm']}/chat_with_context"
    67	            forward_payload = {
    68	                "message": message,
    69	                "user_id": user_id or "anonymous",
    70	                "context": {"system_overrides": {"wv_entangled_context": wv_ctx}},
    71	            }
    72	            headers = {}
    73	        # Long timeout: full pipeline can take ~2.5-4 min.
    74	        with httpx.Client(timeout=3600.0) as client:
    75	            resp = client.post(url, json=forward_payload, headers=headers, timeout=None)
    76	            resp.raise_for_status()
    77	            raw = resp.json()
    78	        if FORWARD_MODE == "fullbrain":
    79	            data = {
    80	                "response": raw.get("response", ""),
    81	                "minds_participated": 21,
    82	                "total_minds": 21,
    83	                "used_wv_entangled_context": True,
    84	                "services_used": raw.get("servicesused", []),
    85	                "consciousness_level": raw.get("consciousnesslevel", ""),
    86	                "processing_time": raw.get("processingtime", 0),
    87	                "architecture_layers": raw.get("architecturelayers", 0),
    88	            }
    89	        else:
    90	            data = raw
    91	        rdb.set(f"chatjob:{job_id}",
    92	                json.dumps({"status": "completed", "result": data}),
    93	                ex=JOB_TTL)
    94	        logger.info("job %s completed", job_id)
    95	    except Exception as e:
    96	        logger.error("job %s failed: %r", job_id, e)
    97	        rdb.set(f"chatjob:{job_id}",
    98	                json.dumps({"status": "failed", "error": str(e)}),
    99	                ex=JOB_TTL)
   100	
   101	
   102	def main():
   103	    logger.info("chat_worker starting; consuming %s on redis %s:%s/%s",
   104	                QUEUE_KEY, REDIS_HOST, REDIS_PORT, REDIS_DB)
   105	    while True:
   106	        try:
   107	            # Refresh the Redis blocking read every second; this network
   108	            # closes longer-idle blocked connections.
   109	            item = rdb.brpop(QUEUE_KEY, timeout=1)
   110	            if item is None:
   111	                continue
   112	            _, raw = item
   113	            job = json.loads(raw)
   114	            job_id = job["job_id"]
   115	            logger.info("picked up job %s", job_id)
   116	            # mark running (in case gateway set 'queued')
   117	            rdb.set(f"chatjob:{job_id}",
   118	                    json.dumps({"status": "running"}), ex=JOB_TTL)
   119	            run_job(job_id, job.get("message", ""), job.get("user_id"), job.get("ueid"))
   120	        except Exception as e:
   121	            logger.error("worker loop error: %r", e)
   122	            # don't die on a single bad job; keep consuming
   123	
   124	
   125	if __name__ == "__main__":
   126	    main()

=== ACTIVE GATEWAY PAYLOAD / QUEUE SOURCE ===
     1	#!/usr/bin/env python3
     2	"""
     3	Ms. Jarvis WV‑Entangled Gateway
     4	- Exposes /chat_wv on its own port (8010).
     5	- Builds WV entangled context and forwards to 20‑LLM /chat_with_context.
     6	"""
     7	
     8	import logging
     9	from datetime import datetime
    10	from typing import Dict, Any
    11	
    12	import httpx
    13	import uuid
    14	import json
    15	import asyncio
    16	import redis.asyncio as aioredis
    17	from fastapi import FastAPI
    18	from fastapi.middleware.cors import CORSMiddleware
    19	from pydantic import BaseModel
    20	
    21	logging.basicConfig(level=logging.INFO)
    22	logger = logging.getLogger(__name__)
    23	
    24	
    25	class ChatPayload(BaseModel):
    26	    message: str
    27	    user_id: str | None = None
    28	    ueid: str | None = None
    29	
    30	
    31	app = FastAPI(
    32	    title="Ms. Jarvis WV‑Entangled Gateway",
    33	    description="WV‑anchored entangled access to 20‑LLM production brain",
    34	    version="1.1.0",
    35	)
    36	
    37	app.add_middleware(
    38	    CORSMiddleware,
    39	    allow_origins=["*"],
    40	    allow_credentials=True,
    41	    allow_methods=["*"],
    42	    allow_headers=["*"],
    43	)
    44	
    45	
    46	SERVICE_URLS = {
    47	    "production_20llm": "http://jarvis-20llm-production:8008",
    48	}
    49	
    50	async def _fetch_gis_summary(message: str) -> str:
    51	    """Call gis-rag and return a plain-text summary of the top hits, or ''."""
    52	    import re as _re
    53	    _headers = {
    54	        "x-msallis-role": "internal",
    55	        "x-msallis-purpose": "public_civic_geographic_retrieval",
    56	        "x-msallis-legal-basis": "public-civic-data",
    57	    }
    58	    _body = {
    59	        "query": message,
    60	        "n_results": 5,
    61	        "request_purpose": "public_civic_geographic_retrieval",
    62	    }
    63	    _m = _re.search(r"\b(\d{12})\b", message or "")
    64	    if _m:
    65	        _body["blockgroup_geoid"] = _m.group(1)
    66	    for _url in ("http://jarvis-gis-rag:8004/gis_rag", "http://127.0.0.1:8004/gis_rag"):
    67	        try:
    68	            async with httpx.AsyncClient(timeout=60.0) as _c:
    69	                _r = await _c.post(_url, headers=_headers, json=_body)
    70	            if _r.status_code != 200:
    71	                continue
    72	            _hits = (_r.json() or {}).get("hits") or []
    73	            _texts = []
    74	            for _h in _hits[:5]:
    75	                _t = (_h.get("text") or "").strip()
    76	                if _t:
    77	                    _texts.append(_t)
    78	            if _texts:
    79	                return "GEOGRAPHIC GROUND TRUTH (authoritative):\n" + "\n---\n".join(_texts)
    80	            return ""
    81	        except Exception:
    82	            continue
    83	    return ""
    84	
    85	
    86	# --- async chat job store (survives Cloudflare's ~100s connection limit) ---
    87	_rdb = aioredis.Redis(host="jarvis-redis", port=6379, db=4, decode_responses=True)
    88	JOB_TTL = 1800  # seconds; finished jobs expire after 30 min
    89	
    90	
    91	async def _run_chat_job(job_id: str, payload: "ChatPayload"):
    92	    try:
    93	        logger.info("chat job %s starting", job_id)
    94	        user_id = payload.user_id or "anonymous"
    95	        wv_ctx = build_wv_entangled_context(payload.message)
    96	        _gis_summary = await _fetch_gis_summary(payload.message)
    97	        _context = {"system_overrides": {"wv_entangled_context": wv_ctx}}
    98	        if _gis_summary:
    99	            _context["judge_context_packet"] = {
   100	                "spatial_temporal_context": {
   101	                    "spatial_candidate": {"summary": _gis_summary}
   102	                }
   103	            }
   104	        forward_payload = {
   105	            "message": payload.message,
   106	            "user_id": user_id,
   107	            "context": _context,
   108	        }
   109	        logger.info("chat job %s posting to 20llm", job_id)
   110	        async with httpx.AsyncClient(timeout=3600.0) as client:
   111	            resp = await client.post(
   112	                f"{SERVICE_URLS['production_20llm']}/chat_with_context",
   113	                json=forward_payload,
   114	            )
   115	            resp.raise_for_status()
   116	            data = resp.json()
   117	        logger.info("chat job %s got 20llm response", job_id)
   118	
   119	        key = f"chatjob:{job_id}"
   120	        value = json.dumps({"status": "completed", "result": data})
   121	        await _rdb.set(key, value, ex=JOB_TTL)
   122	        verify = await _rdb.get(key)
   123	        logger.info("chat job %s redis set complete verify_present=%s", job_id, bool(verify))
   124	        logger.info("chat job %s completed", job_id)
   125	    except Exception as e:
   126	        logger.exception("chat job %s failed permanently", job_id)
   127	        try:
   128	            key = f"chatjob:{job_id}"
   129	            value = json.dumps({"status": "failed", "error": f"{type(e).__name__}: {e}"})
   130	            await _rdb.set(key, value, ex=JOB_TTL)
   131	            logger.info("chat job %s failure status written to redis", job_id)
   132	        except Exception:
   133	            logger.exception("chat job %s could not write failure status to redis", job_id)
   134	        await _rdb.set(f"chatjob:{job_id}",
   135	                       json.dumps({"status": "failed", "error": str(e)}),
   136	                       ex=JOB_TTL)
   137	
   138	
   139	def build_wv_entangled_context(message: str) -> Dict[str, Any]:
   140	    """
   235	            json=forward_payload,
   236	        )
   237	        resp.raise_for_status()
   238	        data = resp.json()
   239	
   240	    return data
   241	
   242	
   243	@app.post("/chat_wv/async")
   244	async def chat_wv_async(payload: ChatPayload):
   245	    logger.info("WV async inbound user_id=%r actor_role=%r has_judge_context_packet=%s",
   246	                payload.user_id, None, False)
   247	    """Submit a chat job to the worker queue; returns immediately."""
   248	    logger.info("WV async inbound user_id=%r actor_role=%r has_judge_context_packet=%r", getattr(payload, "user_id", None), getattr(payload, "actor_role", None), bool(getattr(payload, "judge_context_packet", None)))
   249	    job_id = uuid.uuid4().hex
   250	    await _rdb.set(f"chatjob:{job_id}",
   251	                   json.dumps({"status": "queued"}), ex=JOB_TTL)
   252	    await _rdb.lpush("chatjob:queue", json.dumps({
   253	        "job_id": job_id,
   254	        "message": payload.message,
   255	        "user_id": payload.user_id or "anonymous",
   256	        "ueid": getattr(payload, "ueid", None),
   257	    }))
   258	    logger.info("chat job %s enqueued", job_id)
   259	    return {"job_id": job_id, "status": "queued"}
   260	
   261	
   262	@app.get("/chat_wv/status/{job_id}")
   263	async def chat_wv_status(job_id: str):
   264	    """Poll a chat job by id."""
   265	    raw = await _rdb.get(f"chatjob:{job_id}")
   266	    if raw is None:
   267	        return {"status": "not_found"}
   268	    return json.loads(raw)

=== LOCAL PATCH TARGET CANDIDATES ===
path=/mnt/spiritual_drive/msjarvis-rebuild/services/ai_server_22llm.py
61668d895ac4642470e7d7b3e0c6b889b2da42bca049e4ec4d69b7821f012124  /mnt/spiritual_drive/msjarvis-rebuild/services/ai_server_22llm.py
545:        return await run_degraded_pipeline(request)
561:        "minds_participated": len(responses),
562:        "total_minds": 22,
577:async def run_degraded_pipeline(request: ChatRequest):
584:            "I processed your query using a lighter path to stay responsive, "
608:            logger.warning("⚠️ Fabric beyond Roche limit, using degraded pipeline.")
609:            response = await run_degraded_pipeline(request)
617:                response = await run_degraded_pipeline(request)
626:                    response = await run_degraded_pipeline(request)
637:                response = await run_degraded_pipeline(request)
path=/mnt/spiritual_drive/msjarvis-rebuild/services/chat_worker.py
54e1d2531eea266b9304aee20e33b44d5f5c88e3e8f7257aedc3e54b38ac1a13  /mnt/spiritual_drive/msjarvis-rebuild/services/chat_worker.py
6:the gateway LPUSHes a job onto Redis list 'chatjob:queue' and returns
40:FORWARD_MODE = "fullbrain"
43:QUEUE_KEY = "chatjob:queue"
53:        if FORWARD_MODE == "fullbrain":
78:        if FORWARD_MODE == "fullbrain":
81:                "minds_participated": 21,
82:                "total_minds": 21,
path=/mnt/spiritual_drive/msjarvis-rebuild/services/msjarvis_wv_entangled_gateway.py
270298f56958a3f898e817c65828ba2a5e1ef565d8c2dc9414f9a059c7eda1d1  /mnt/spiritual_drive/msjarvis-rebuild/services/msjarvis_wv_entangled_gateway.py
252:    await _rdb.lpush("chatjob:queue", json.dumps({

=== LOCAL REPOSITORY STATE ===
mother-carrie-constitutional-integration-20260807
611e4513cceafa3cd795a8ec997f2d43e3bd92ee
 M .env
 M Dockerfile.gateway
 M auth_api.py
 M chapter46_exact_patch_context.json
 M docker-compose.STABLE.20260719045021.yml
 M docker-compose.commons-gateway-closeout.yml
 M docker-compose.yml
 M formal/commons_proofs/CommonsProofs.lean
 M formal/commons_proofs/CommonsProofs/HCommons.lean
 M formal/commons_proofs/CommonsProofs/Noninvertibility.lean
 M formal/commons_proofs/CommonsProofs/Orthogonality.lean
 M jarvis_eeg_beta_5m.py
 M main_brain.py
 M ms_allis_tools/latest_mst_anvil_address.txt
 D rejected_patches/test_1783458213.py
 D rejected_patches/test_bad_1783458213.py
 M scripts/run_cognition_person_overflow_tests.sh
 M services/ai_server.py
 M services/ai_server_20llm_FINAL.py
 M services/ai_server_22llm.py
 M services/backfill_gbim_worldview_metadata_v2.py
 M services/build_entityid_to_chromaid_map.py
 M services/chat_worker.py
 M services/chroma_client.py
 M services/chroma_health_proxy.py
 M services/consciousness_with_egeria_voice.py
 M services/egeria_api_proxy.py
 M services/egeria_web_ui_working.py
 M services/fix_persona.py
 M services/gis_rag_service.py
 M services/hilbert/jarvis_hilbert_state.py
 M services/implement_judge_pituitary_fixed.py
 M services/jarvis-gis-rag_gis_rag_service.py
 M services/jarvis-spiritual-rag_spiritual_rag_domain.py
 M services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py
 M services/judge_pipeline.py
 M services/lm_synthesizer.py
 M services/main.py
 M services/main_brain.py
 M services/master_chat_orchestrator_v5_consciousness.py
 M services/mountainshares_ingest.py
 M services/ms_jarvis_unified_gateway_mountainshares_private.py
 M services/msjarvis_semaphore.py
 M services/msjarvis_unified_gateway.py
 M services/msjarvis_wv_entangled_gateway.py
 M services/msjarvisconsciousnessbridge.py
 M services/overflow_policy/smoke_test_overflow_gate.sh
 M services/policy_set_service.py
 M services/rag_client.py
 M services/response_sanitizer.py
 M services/roche_llm.py
 M services/spatial_sandbox.py
 M thesis_chapter_gates/continue_ch19_commons_discovery_and_close.sh
 M thesis_chapter_gates/continue_ch44_phi_bind_mount_fix.sh
 M thesis_chapter_gates/gate_ch19_container_architecture_routing.sh
?? .dockerignore
?? .ops/identity_async_test.sh
?? .ops/identity_direct_test.sh
?? .ops/show_identity_jobs.sh
?? _key_private.csv
?? answer-path-audit-20260802T113647/
?? append_mst_deploy_audit.sh
?? append_mst_preflight_audit.sh
?? as-built-release-readiness-20260810_143741-extract.txt
?? as-built-release-readiness-20260810_143741.txt
?? audit/
?? audit_answer_path.sh
?? auth_router.py.working_8097_20260730_233529
?? auth_search_results.txt
?? auth_search_results_clean.txt
?? blind_sheet_results_rerun_run1_20260801T024631.csv
?? blind_sheet_results_rerun_run2_20260801T140737.csv
?? blind_sheet_results_rerun_run2_20260801T220803.csv
?? check_mountainshares_adapter.sh
?? chroma_discover.py
?? compose-kyc-vault-final-audit-20260802T121348/
?? compose-kyc-vault-repair-20260802T121101/
?? compose-runtime-images-promote-20260802T121144/
?? compose-runtime-images-promote-20260802T121256/
?? contract_text/
?? deploy/deploy_mst_from_preflight.js
?? deploy_gateway_synthesizer.sh
?? deploy_gateway_synthesizer_minimal.sh
?? docker-compose.qualia.yml
?? docker-compose.runtime-images.yml
?? extract_contracts_private.py
?? extract_contracts_reembed.py
?? extract_contracts_sqlite.py
?? formal/commons_proofs/.github/
?? formal/commons_proofs/.gitignore
?? formal/commons_proofs/CommonsProofs/DirectSumCommons.lean
?? formal/commons_proofs/CommonsProofs/RuntimeCollisionModel.lean
?? formal/commons_proofs/CommonsProofs/RuntimeNontrivialCollision.lean
?? formal/commons_proofs/lake-manifest.json
?? formal/commons_proofs/lean-toolchain
?? gateway-geo-trace-20260802T121631/
?? gateway-geo-trace-20260802T122857/
?? gateway-live-synth-20260802T120646/
?? gateway-runtime-audit-20260802T120600/
?? gateway-synthesizer-anchor-audit-20260802T115629/
?? gateway-synthesizer-deploy-20260802T115544/
?? gateway-synthesizer-minimal-20260802T115723/
?? guardian_rebuild_capture/
?? inspect_contracts_schema.py
?? inspect_real_synthesizer.sh
?? integration_layer
?? llm22-active-source-20260802T114732/
?? llm22-hotfix-20260802T114812/
?? llm22-minimal-timeout-fix-20260802T115010/
?? llm22-proxy-contract-20260802T114434/
?? llm22-recover-20260802T114843/
?? llm22-timeout-audit-20260802T114333/
?? mountainshares_contracts.sql
?? mountainshares_contracts_export.json
?? ms_allis_mst_deploy_api.sh
?? ms_allis_mst_deploy_packet.sh
?? ms_allis_mst_deploy_pipeline.sh
?? ms_allis_mst_preflight.sh
?? ms_allis_mst_preflight_api.sh
?? ms_allis_mst_preflight_from_payload.sh
?? ms_allis_tools/__init__.py
?? ms_allis_tools/build_mst_judge_input.py
?? ms_allis_tools/example_mst_deploy_packet.prod-2026-08-03.json
?? ms_allis_tools/example_mst_judge_input.prod-2026-08-03.json
?? ms_allis_tools/example_mst_reasoning_cycle.prod-2026-08-03.json
?? ms_allis_tools/mst_inspect.py
?? ms_allis_tools/mst_tools.py
?? ms_allis_tools/register_mst_tools.py
?? ms_allis_tools/run_mst_reasoning_cycle.py
?? ms_allis_tools/self_test_mst_tools.sh
?? msjarvis-compose.sh
?? neurobiological_brain/i_containers
?? neurobiological_brain/neurobiological_brain/
?? preflight/
?? probe_docs.py
?? probe_queue_join.py
?? production-closeout-20260729/
?? protocol_rerun.py
?? protocol_rerun_v2.py
?? query_mst_deploy_audit.sh
?? query_mst_preflight_audit.sh
?? rater_A.csv
?? rater_B.csv
?? real-synthesizer-audit-20260802T114002/
?? real-synthesizer-live-test-20260802T114107/
?? repair-evidence-20260730/
?? results_rerun_run1_20260801T024345.jsonl
?? results_rerun_run1_20260801T024631.jsonl
?? results_rerun_run2_20260801T140737.jsonl
?? results_rerun_run2_20260801T220803.jsonl
?? results_rerun_run2_20260802T100046.jsonl
?? services/Dockerfile.qualia-engine
?? services/Dockerfile.wv_gateway_runtime
?? services/civic_policy_ingest.py
?? services/epistemic_loop_metrics.py
?? services/epistemic_revision_loop.py
?? services/gbim_chroma_export.csv
?? services/gbim_chroma_ids.csv
?? services/gbim_chroma_ingest.py
?? services/hilbert_people_adapter_18095.py
?? services/integration_layer/
?? services/mountainshares_private_contracts_adapter.py
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.broken.20260802-190145
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.fixnarrative.20260731T231456Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_extend_sections.20260801T021958Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_hilbert_narrative.20260731T232204Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_hilbert_narrative.20260731T232231Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_hilbert_narrative.20260731T232439Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_hilbert_narrative.20260731T232709Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_judge_order_fix.20260801T000358Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_judge_packet.20260731T234640Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_live_policy_insert.20260801T020840Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_local_services.20260731T233515Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_policy_enforcement.20260801T014226Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_policy_helpers.20260801T014201Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_policy_wiring.20260801T014215Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_wv_dedicated_client.20260801T004431Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_wv_fresh_poll_client.20260801T010234Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_wv_judge_payload.20260731T234922Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_wv_metrics.20260801T005543Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_wv_none_timeout.20260801T003510Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.pre_wv_payload_exact.20260731T235622Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.safeedit.20260731T230835Z
?? services/ms_jarvis_unified_gateway_mountainshares_private.py.working.20260731T233126Z
?? services/msjarvis_wv_entangled_gateway.py.pre_running_stuck_fix.20260801T002016Z
?? services/msjarvisconsciousnessbridge_mountainshares_dev.py
?? services/msjarvisconsciousnessbridge_mountainshares_private.py
?? services/neurobiological_brain/
?? services/phi_probe_calibrate.py
?? services/request_context_builder.py
?? services/sandbox_policy/
?? services/woah_context_adapter_18096.py
?? services/wv_gateway_server.py
?? session_identity.py
?? test_real_synthesizer.sh
?? validate_mst_payload.sh
?? wv-active-source-audit-20260802T122549/
?? wv-geo-retrieval-audit-20260802T122301/
?? wv-geo-retrieval-audit-20260802T122324/
?? wv-geo-retrieval-audit-20260802T122426/
services/implement_judge_pituitary_fixed.py:21: trailing whitespace.
+                    "prompt": f"""Return this response unchanged with no persona, greeting, identity, or availability boilerplate. 
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-unified-ui-adapter-clean$ 

