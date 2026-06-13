crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild

sed -n '1,220p' spiritual_rag_domain.py.tmp

grep -n -A20 -B5 "spiritual-rag\|spiritual_rag" docker-compose.yml
#!/usr/bin/env python3
"""
SPIRITUAL RAG DOMAIN SERVICE v2.0
19,338 chunks across 54 texts, 15 cultural families
ChromaDB semantic search + PostGIS geographic filtering
"""
import os, json, logging
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List
import chromadb
import psycopg2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CHROMA_HOST = os.getenv("CHROMA_HOST", "localhost")
CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8002"))
DB_CONN     = os.getenv("DB_CONN", "dbname=msjarvis user=postgres")
GEOJSON_PATH = os.getenv(
    "GEOJSON_PATH",
    "/app/spiritual_origins.geojson"
)

app = FastAPI(
    title="Spiritual RAG Domain v2",
    version="2.0.0",
    description="19,338 chunks · 54 texts · 15 cultural families · PostGIS geo-aware"
)

# ── Clients ──────────────────────────────────────────────────────────
def get_collection():
    client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
    return client.get_collection("spiritual_texts")

def get_db():
    return psycopg2.connect(DB_CONN)

# ── Models ───────────────────────────────────────────────────────────
class SearchRequest(BaseModel):
    query: str
    top_k: int = 5
    tradition: Optional[str] = None
    cultural_family: Optional[str] = None

class GeoSearchRequest(BaseModel):
    query: str
    lat: float = 37.9718   # Oak Hill, WV default
    lon: float = -81.1498
    radius_km: int = 8000
    top_k: int = 5

# ── Routes ───────────────────────────────────────────────────────────
@app.get("/")
def root():
    try:
        col = get_collection()
        count = col.count()
    except:
        count = "unavailable"
    return {
        "service": "Spiritual RAG Domain v2 — FOUNDATIONAL LAYER",
        "version": "2.0.0",
        "status": "healthy",
        "chunks_in_chromadb": count,
        "texts": 54,
        "cultural_families": 15,
        "geo_enabled": True,
        "reference_point": "Oak Hill, WV"
    }

@app.get("/health")
def health():
    try:
        col = get_collection()
        chroma_ok = col.count() > 0
    except:
        chroma_ok = False
    try:
        conn = get_db(); conn.close()
        postgis_ok = True
    except:
        postgis_ok = False
    return {
        "status": "healthy" if chroma_ok else "degraded",
        "chromadb": chroma_ok,
        "postgis": postgis_ok,
        "service": "spiritual_rag_domain_v2",
        "port": int(os.getenv("SERVICE_PORT", "8005"))
    }

@app.post("/search")
def search(req: SearchRequest):
    """Semantic search across all 54 spiritual texts"""
    col = get_collection()
    where = {}
    if req.tradition:
        where["tradition"] = req.tradition
    if req.cultural_family:
        where["cultural_family"] = req.cultural_family

    kwargs = dict(
        query_texts=[req.query],
        n_results=req.top_k,
        include=["documents", "metadatas", "distances"]
    )
    if where:
        kwargs["where"] = where

    results = col.query(**kwargs)
    return {
        "query": req.query,
        "filters": where or "none",
        "results": [
            {
                "text": d[:500],
                "title": m["title"],
                "tradition": m["tradition"],
                "cultural_family": m.get("cultural_family", ""),
                "region": m.get("region", ""),
                "origin_notes": m.get("origin_notes", ""),
                "relevance": round(1 - dist, 4)
            }
            for d, m, dist in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0]
            )
        ]
    }

@app.post("/search/geo")
def search_geo(req: GeoSearchRequest):
    """Semantic search filtered to traditions within geographic radius"""
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT DISTINCT title FROM spiritual_text_origins
        WHERE ST_DWithin(geom::geography,
          ST_SetSRID(ST_MakePoint(%s, %s), 4326)::geography, %s)
    """, (req.lon, req.lat, req.radius_km * 1000))
    nearby = [r[0] for r in cur.fetchall()]
    conn.close()

    if not nearby:
        return {"query": req.query, "results": [], "nearby_traditions": []}

    col = get_collection()
    results = col.query(
        query_texts=[req.query],
        n_results=req.top_k,
        where={"title": {"$in": nearby}},
        include=["documents", "metadatas", "distances"]
    )
    return {
        "query": req.query,
        "geo_filter": f"{req.radius_km}km from ({req.lat},{req.lon})",
        "nearby_traditions": nearby,
        "results": [
            {
                "text": d[:500],
                "title": m["title"],
                "tradition": m["tradition"],
                "region": m.get("region", ""),
                "relevance": round(1 - dist, 4)
            }
            for d, m, dist in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0]
            )
        ]
    }

@app.get("/geo/map")
def geo_map():
    """Full GeoJSON FeatureCollection for GBIM map layer"""
    with open(GEOJSON_PATH) as f:
        return JSONResponse(json.load(f))

@app.get("/geo/proximity")
def geo_proximity(
    lat: float = Query(37.9718),
    lon: float = Query(-81.1498),
    radius_km: int = Query(8000)
):
    """All traditions within radius, sorted by distance"""
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT title, cultural_family, region, origin_notes,
               ROUND(ST_Distance(geom::geography,
                 ST_SetSRID(ST_MakePoint(%s,%s),4326)::geography)/1000) AS km,
               proximity_band
        FROM v_spiritual_texts_gbim
        WHERE ST_DWithin(geom::geography,
          ST_SetSRID(ST_MakePoint(%s,%s),4326)::geography, %s)
        ORDER BY km
    """, (lon, lat, lon, lat, radius_km * 1000))
    rows = cur.fetchall()
    conn.close()
    return {
        "reference": {"lat": lat, "lon": lon},
        "radius_km": radius_km,
        "count": len(rows),
        "traditions": [
            {"title": r[0], "cultural_family": r[1], "region": r[2],
             "notes": r[3], "km": r[4], "band": r[5]}
            for r in rows
        ]
    }

@app.get("/geo/corridor/{corridor}")
def geo_corridor(corridor: str):
    """Named cultural corridors: silk_road, americas, pacific_rim, europe, africa, appalachia"""
    corridors = {
        "silk_road":   (-15.0, 20.0, 125.0, 55.0),
        "americas":    (-170.0, -60.0, -30.0, 75.0),
        "europe":      (-15.0, 35.0, 45.0, 72.0),
1642-      - /home/cakidd/msjarvis-rebuild/services/backup_chroma_mountainshares_knowledge.json:/app/backup_mountainshares.json:ro
1643-      - /opt/msjarvis-rebuild/services:/app/services
1644-    networks:
1645-      - qualia-net
1646-    restart: unless-stopped
1647:  jarvis-spiritual-rag:
1648-    build:
1649-      context: ./services
1650:      dockerfile: Dockerfile.spiritual_rag
1651:    container_name: jarvis-spiritual-rag
1652-    expose:
1653-      - "8005"
1654-    ports:
1655-      - 127.0.0.1:8005:8005
1656-    environment:
1657-      - SERVICE_PORT=8005
1658-      - CHROMA_HOST=jarvis-chroma
1659-      - CHROMA_PORT=8000
1660-      - CLOCK_TS=1767812077
1661-      - HF_HUB_OFFLINE=1
1662-    depends_on:
1663-      - jarvis-chroma
1664-    volumes:
1665-      - ./services:/app/services
1666-      - /home/cakidd/.cache/huggingface:/root/.cache/huggingface
1667-    networks:
1668-      - qualia-net
1669-    restart: unless-stopped
1670-    logging:
1671-      driver: json-file
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild

grep -RIn --exclude-dir=.git --exclude-dir=crypto-venv \
  -E 'collection *=|collection_name *=|get_or_create_collection\(|create_collection\(' \
  . | grep -Ei 'spiritual|wisdom|mountainshares|knowledge|commons|egeria|allis' | sed -n '1,220p'
./_archive/generated_20260430/enhance_rag_knowledge.py:26:collection = client.get_or_create_collection(name="mountainshares_knowledge")
./_archive/generated_20260430/bulk_load_knowledge.py:27:collection = client.get_or_create_collection(name="mountainshares_knowledge")
./_archive/generated_20260430/ms_jarvis_facebook_dgm_woah.psychology_patched.py:181:            self.community_wisdom = self.chroma_client.create_collection("community_wisdom")
./_archive/generated_20260430/load_pdfs_spiritual.py:17:collection = client.get_or_create_collection(name="mountainshares_knowledge")
./_archive/generated_20260430/bulk_load_MAXIMUM.py:19:collection = client.get_or_create_collection(name="mountainshares_knowledge")
./_archive/generated_20260430/load_spiritual_library.py:17:collection = client.get_or_create_collection(name="spiritual_wisdom")
./_archive/generated_20260430/audit_attrs.py:18:collection = client.get_collection('knowledge_docs')
./_archive/generated_20260430/rag_server.psychology_patched.py:95:        self.knowledge_collection = self.chroma_client.get_or_create_collection(name="mountainshares_knowledge")
./_archive/generated_20260430/ai_server_restored.py:107:            self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/generated_20260430/ai_server_restored.py:116:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/generated_20260430/test_knowledge_base.py:9:collection = client.get_collection("egeria_docs")
./_archive/generated_20260430/load_rag_knowledge.py:16:collection = chroma.get_or_create_collection(name="mountainshares_knowledge")
./_archive/generated_20260430/ingest_knowledge_simple.py:19:    collection = client.get_collection("egeria_docs")
./_archive/generated_20260430/ingest_knowledge_simple.py:22:    collection = client.create_collection("egeria_docs")
./_archive/generated_20260430/export_attributes_to_gis.py:7:collection = client.get_collection('knowledge_docs')
./_archive/generated_20260430/export_metadata_csv.py:3:collection = client.get_collection('knowledge_docs')
./_archive/generated_20260430/load_complete_knowledge_base.py:36:    spiritual_col = client.create_collection(
./_archive/generated_20260430/load_complete_knowledge_base.py:46:    ms_col = client.create_collection(
./_archive/generated_20260430/load_complete_knowledge_base.py:56:    gis_col = client.create_collection(
./_archive/service_baks_20260430/ms_jarvis_autonomous_learner_optimized.py.bak_1765235983:141:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/main_brain.py.bak_ch29:1391:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/main_brain.py.bak3:994:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.before_mamma_protocol:222:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.before_mamma_protocol:233:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/main_brain.py.bak_egeria_patch_1777059405:1368:                    collection_name = item.get("collection", "unknown")
./_archive/service_baks_20260430/main_brain.py.bak_egeria_patch_1777059405:1391:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.backup_before_hierarchy:224:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.backup_before_hierarchy:235:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/audit_attrs.py.backup_20251205234718:6:collection = client.get_collection('knowledge_docs')
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.backup_vocabulary_cleanup:221:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.backup_vocabulary_cleanup:232:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/reload_all_knowledge.py.backup_vocabulary_cleanup:15:collection = client.get_or_create_collection(name="ms_jarvis_knowledge")
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.backup_pre_location_integration:107:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.backup_pre_location_integration:118:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/ms_jarvis_autonomous_learner_optimized.py.bak:88:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/rag_server.py.before_delete:55:        self.knowledge_collection = self.chroma_client.get_or_create_collection(name="mountainshares_knowledge")
./_archive/service_baks_20260430/main_brain.py.bak.1775579935:994:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/main_brain.py.bak.20260416-212709:1129:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/msjarvisautonomouslearner.py.bak-20260114054922:87:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/main_brain.py.bak.ch22fix:1049:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/audit_attrs.py.backup_20251205234841:18:collection = client.get_collection('knowledge_docs')
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.before_persona_fix:222:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.before_persona_fix:233:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/main_brain.py.bak_auth:995:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.backup_1759895250:220:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.backup_1759895250:231:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/load_rag_knowledge.py.backup_vocabulary_cleanup:12:collection = chroma.get_or_create_collection(name="mountainshares_knowledge")
./_archive/service_baks_20260430/ai_server_restored.py.backup_before_portmanager:106:            self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ai_server_restored.py.backup_before_portmanager:115:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/main_brain.py.bak.20260425_210943:1391:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/rag_server.py.backup_20251031:91:        self.knowledge_collection = self.chroma_client.get_or_create_collection(name="mountainshares_knowledge")
./_archive/service_baks_20260430/main.py.bak_enable_llmbridge_20251212_233317:595:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/conversation_memory_endpoints.py.backup_before_portmanager:24:collection = client.get_or_create_collection(name="mountainshares_knowledge")
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.before_prompt_fix:222:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.before_prompt_fix:233:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/main_brain.py.bak.1774448411:1077:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/main_brain.py.bak_1777342937:1403:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/main_brain.py.bak_clean:994:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/ai_server.py.backup.20251006_101858:96:        self.knowledge_memory = self.chroma_client.get_or_create_collection(name="mountainshares_knowledge")
./_archive/service_baks_20260430/main_brain.py.bak.20260416-141747:1128:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/main.py.bak_before_bridge_20251212_232206:595:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.backup_1760220435:220:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.backup_1760220435:231:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/main_brain.py.bak3.20260428_160451:1615:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/main_brain.py.bak.20260407_205446:1032:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/main_brain.py.bak.20260428_154533:1610:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/main.py.bak_enable_llmbridge_20251212_233118:595:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/main.py.bak_before_bridge_20251212_232349:595:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.before_small_models:222:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.before_small_models:233:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/main_brain.py.bak:994:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/rag_server.py.bak:131:            self.knowledge_collection_name = "mountainshares_knowledge"
./_archive/service_baks_20260430/rag_server.py.bak:135:            self.knowledge_collection = self.chroma_client.get_collection(
./_archive/service_baks_20260430/rag_server.py.bak:145:            self.knowledge_collection = self.chroma_client.create_collection(
./_archive/service_baks_20260430/main.py.pre_enhancement.bak:626:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/ms_jarvis_autonomous_learner.py.backup_before_portmanager:63:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.backup_pre_fixes:222:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.backup_pre_fixes:233:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/ms_jarvis_facebook_dgm_woah.py.backup_vocabulary_cleanup:177:            self.community_wisdom = self.chroma_client.create_collection("community_wisdom")
grep: ./chroma_data/chroma_data: No such file or directory
grep: ./output/pia/latest: No such file or directory
grep: ./services/alert_venv/lib64: No such file or directory
./_archive/service_baks_20260430/main_brain.py.bak2.20260428_155604:1610:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/ms_jarvis_facebook_dgm_woah.py.backup_20251031:177:            self.community_wisdom = self.chroma_client.create_collection("community_wisdom")
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.backup_before_22llm:222:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.backup_before_22llm:233:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/ms_jarvis_autonomous_learner_optimized.py.backup_before_auto_research:141:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_autonomous_learner.py.backup_day2:55:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/main.py.bak.before_consciousness_fix:596:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.backup_1759895606:220:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.backup_1759895606:231:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/msjarvisautonomouslearner.py.bak-20260114060021:87:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/gpu_accelerated_rag_fixed.py.backup_before_portmanager:98:            collection_name = "ms_jarvis_knowledge"
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.before_theology:117:            self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.before_theology:129:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.before_rag_web:230:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/ms_jarvis_consciousness_bridge.py.before_rag_web:241:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./_archive/service_baks_20260430/ms_jarvis_autonomous_learner_optimized.py.backup_before_portmanager:90:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./_archive/service_baks_20260430/main_brain.py.bak.1777320408:1408:                        collection_name == "spiritual_texts"
./_archive/service_baks_20260430/rag_server.py.before_store:48:        self.knowledge_collection = self.chroma_client.get_or_create_collection(name="mountainshares_knowledge")
./_archive/service_baks_20260430/rag_server.py.before_filtering:39:        self.knowledge_collection = self.chroma_client.get_or_create_collection(name="mountainshares_knowledge")
./_archive/service_baks_20260430/ms_jarvis_autonomous_learner_WITH_FIFTH_DGM.py.backup_before_portmanager:64:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./msjarvis-rebuild/backups/fix-20260411-080355/main_brain.py.bak:1049:                        collection_name == "spiritual_texts"
./services/enhance_rag_knowledge.py:26:collection = client.get_or_create_collection(name="mountainshares_knowledge")
./services/bulk_load_knowledge.py:27:collection = client.get_or_create_collection(name="mountainshares_knowledge")
./services/ms_jarvis_autonomous_learner_optimized.py:97:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./services/ms_jarvis_facebook_dgm_woah.psychology_patched.py:181:            self.community_wisdom = self.chroma_client.create_collection("community_wisdom")
./services/_archive/restored_documents.json.bak-msallis:10150:      "content": "bled ([--ipv6 mongod option documentation](https://www.mongodb.com/docs/manual/reference/program/mongod/#std-option-mongod.--ipv6))\n> - using a host of `127.0.0.1` in place of localhost\n> - specifying the DNS resolution ordering with the `--dns-resolution-order` Node.js command line argument (e.g. `node --dns-resolution-order=ipv4first`)\n\n```js\nconst { MongoClient } = require('mongodb');\n// or as an es module:\n// import { MongoClient } from 'mongodb'\n\n// Connection URL\nconst url = 'mongodb://localhost:27017';\nconst client = new MongoClient(url);\n\n// Database Name\nconst dbName = 'myProject';\n\nasync function main() {\n  // Use connect method to connect to the server\n  await client.connect();\n  console.log('Connected successfully to server');\n  const db = client.db(dbName);\n  const collection = db.collection('documents');\n\n  // the following code examples can be pasted here...\n\n  return 'done.';\n}\n\nmain()\n  .then(console.log)\n  .catch(console.error)\n  .finally(() => client.close());\n```\n\nRun your app from the command line with:\n\n```bash\nnode app.js\n```\n\nThe application should print **Connected successfully to server** to the console.\n\n### Insert a Document\n\nAdd to **app.js** the following function which uses the **insertMany**\nmethod to add three documents to the **documents** collection.\n\n```js\nconst insertResult = await collection.insertMany([{ a: 1 }, { a: 2 }, { a: 3 }]);\nconsole.log('Inserted documents =>', insertResult);\n```\n\nThe **insertMany** command returns an object wit",
./services/_archive/restored_documents.json.bak-msallis:10518:      "content": "# mquery\n\n`mquery` is a fluent mongodb query builder designed to run in multiple environments.\n\n[![Build Status](https://travis-ci.org/aheckmann/mquery.svg?branch=master)](https://travis-ci.org/aheckmann/mquery)\n[![NPM version](https://badge.fury.io/js/mquery.svg)](http://badge.fury.io/js/mquery)\n\n[![npm](https://nodei.co/npm/mquery.png)](https://www.npmjs.com/package/mquery)\n\n## Features\n\n- fluent query builder api\n- custom base query support\n- MongoDB 2.4 geoJSON support\n- method + option combinations validation\n- node.js driver compatibility\n- environment detection\n- [debug](https://github.com/visionmedia/debug) support\n- separated collection implementations for maximum flexibility\n\n## Use\n\n```js\nconst mongo = require('mongodb');\n\nconst client = new mongo.MongoClient(uri);\nawait client.connect();\n// get a collection\nconst collection = client.collection('artists');\n\n// pass it to the constructor\nawait mquery(collection).find({...});\n\n// or pass it to the collection method\nconst docs = await mquery().find({...}).collection(collection);\n\n// or better yet, create a custom query constructor that has it always set\nconst Artist = mquery(collection).toConstructor();\nconst docs = await Artist().find(...).where(...);\n```\n\n`mquery` requires a collection object to work with. In the example above we just pass the collection object created using the official [MongoDB driver](https://github.com/mongodb/node-mongodb-native).\n\n## Fluent API\n\n- [mquery](#mquery)\n  - [Features](#features)\n  ",
./services/_archive/restored_documents.json.bak-msallis:27190:      "content": "<[Feature][7]<[GeometryObject][9], [GeoJsonProperties][7]>>** input features\n*   `options` **[Object][15]** Optional Parameters (optional, default `{}`)\n\n    *   `options.bbox` **[BBox][16]?** Bounding Box Array \\[west, south, east, north] associated with the Feature\n    *   `options.id` **Id?** Identifier associated with the Feature\n\n### Examples\n\n```javascript\nvar locationA = turf.point([-75.343, 39.984], {name: 'Location A'});\nvar locationB = turf.point([-75.833, 39.284], {name: 'Location B'});\nvar locationC = turf.point([-75.534, 39.123], {name: 'Location C'});\n\nvar collection = turf.featureCollection([\n  locationA,\n  locationB,\n  locationC\n]);\n\n//=collection\n```\n\nReturns **[FeatureCollection][8]<[GeometryObject][9], [GeoJsonProperties][7]>** FeatureCollection of Features\n\n## multiLineString\n\nCreates a [Feature][7]<[MultiLineString][4]> based on a\ncoordinate array. Properties can be added optionally.\n\n### Parameters\n\n*   `coordinates` **[Array][17]<[Array][17]<[Position][20]>>**&#x20;\n*   `properties` **[GeoJsonProperties][7]** an Object of key-value pairs to add as properties (optional, default `{}`)\n*   `options` **[Object][15]** Optional Parameters (optional, default `{}`)\n\n    *   `options.bbox` **[BBox][16]?** Bounding Box Array \\[west, south, east, north] associated with the Feature\n    *   `options.id` **Id?** Identifier associated with the Feature\n\n### Examples\n\n```javascript\nvar multiLine = turf.multiLineString([[[0,0],[10,10]]]);\n\n//=multiLine\n```\n\n*   Throws **",
./services/_archive/restored_documents.json.bak-msallis:34486:      "content": "rg/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)]** an Object of key-value pairs to add as properties\n\n**Examples**\n\n```javascript\nvar multiPoly = turf.multiPolygon([[[[0,0],[0,10],[10,10],[10,0],[0,0]]]);\n\n//=multiPoly\n```\n\n-   Throws **[Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)** if no coordinates are passed\n\nReturns **Feature&lt;MultiPolygon>** a multipolygon feature\n\n# geometryCollection\n\nCreates a [Feature&lt;GeometryCollection>](Feature<GeometryCollection>) based on a\ncoordinate array. Properties can be added optionally.\n\n**Parameters**\n\n-   `geometries` **[Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)&lt;{Geometry}>** an array of GeoJSON Geometries\n-   `properties` **\\[[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)]** an Object of key-value pairs to add as properties\n\n**Examples**\n\n```javascript\nvar pt = {\n    \"type\": \"Point\",\n      \"coordinates\": [100, 0]\n    };\nvar line = {\n    \"type\": \"LineString\",\n    \"coordinates\": [ [101, 0], [102, 1] ]\n  };\nvar collection = turf.geometrycollection([[0,0],[10,10]]);\n\n//=collection\n```\n\nReturns **Feature&lt;GeometryCollection>** a geometrycollection feature\n\n---\n\nThis module is part of the [Turfjs project](http://turfjs.org/), an open source\nmodule collection dedicated to geographic algorithms. It is maintained in the\n[Turfjs/turf](https://github.com/Turfjs/turf) repo",
./services/_archive/restored_documents.json.bak-msallis:45062:      "content": "bled ([--ipv6 mongod option documentation](https://www.mongodb.com/docs/manual/reference/program/mongod/#std-option-mongod.--ipv6))\n> - using a host of `127.0.0.1` in place of localhost\n> - specifying the DNS resolution ordering with the `--dns-resolution-order` Node.js command line argument (e.g. `node --dns-resolution-order=ipv4first`)\n\n```js\nconst { MongoClient } = require('mongodb');\n// or as an es module:\n// import { MongoClient } from 'mongodb'\n\n// Connection URL\nconst url = 'mongodb://localhost:27017';\nconst client = new MongoClient(url);\n\n// Database Name\nconst dbName = 'myProject';\n\nasync function main() {\n  // Use connect method to connect to the server\n  await client.connect();\n  console.log('Connected successfully to server');\n  const db = client.db(dbName);\n  const collection = db.collection('documents');\n\n  // the following code examples can be pasted here...\n\n  return 'done.';\n}\n\nmain()\n  .then(console.log)\n  .catch(console.error)\n  .finally(() => client.close());\n```\n\nRun your app from the command line with:\n\n```bash\nnode app.js\n```\n\nThe application should print **Connected successfully to server** to the console.\n\n### Insert a Document\n\nAdd to **app.js** the following function which uses the **insertMany**\nmethod to add three documents to the **documents** collection.\n\n```js\nconst insertResult = await collection.insertMany([{ a: 1 }, { a: 2 }, { a: 3 }]);\nconsole.log('Inserted documents =>', insertResult);\n```\n\nThe **insertMany** command returns an object wit",
./services/_archive/restored_documents.json.bak-msallis:45430:      "content": "# mquery\n\n`mquery` is a fluent mongodb query builder designed to run in multiple environments.\n\n[![Build Status](https://travis-ci.org/aheckmann/mquery.svg?branch=master)](https://travis-ci.org/aheckmann/mquery)\n[![NPM version](https://badge.fury.io/js/mquery.svg)](http://badge.fury.io/js/mquery)\n\n[![npm](https://nodei.co/npm/mquery.png)](https://www.npmjs.com/package/mquery)\n\n## Features\n\n- fluent query builder api\n- custom base query support\n- MongoDB 2.4 geoJSON support\n- method + option combinations validation\n- node.js driver compatibility\n- environment detection\n- [debug](https://github.com/visionmedia/debug) support\n- separated collection implementations for maximum flexibility\n\n## Use\n\n```js\nconst mongo = require('mongodb');\n\nconst client = new mongo.MongoClient(uri);\nawait client.connect();\n// get a collection\nconst collection = client.collection('artists');\n\n// pass it to the constructor\nawait mquery(collection).find({...});\n\n// or pass it to the collection method\nconst docs = await mquery().find({...}).collection(collection);\n\n// or better yet, create a custom query constructor that has it always set\nconst Artist = mquery(collection).toConstructor();\nconst docs = await Artist().find(...).where(...);\n```\n\n`mquery` requires a collection object to work with. In the example above we just pass the collection object created using the official [MongoDB driver](https://github.com/mongodb/node-mongodb-native).\n\n## Fluent API\n\n- [mquery](#mquery)\n  - [Features](#features)\n  ",
./services/_archive/restored_documents.json.bak-msallis:55054:      "content": "bled ([--ipv6 mongod option documentation](https://www.mongodb.com/docs/manual/reference/program/mongod/#std-option-mongod.--ipv6))\n> - using a host of `127.0.0.1` in place of localhost\n> - specifying the DNS resolution ordering with the `--dns-resolution-order` Node.js command line argument (e.g. `node --dns-resolution-order=ipv4first`)\n\n```js\nconst { MongoClient } = require('mongodb');\n// or as an es module:\n// import { MongoClient } from 'mongodb'\n\n// Connection URL\nconst url = 'mongodb://localhost:27017';\nconst client = new MongoClient(url);\n\n// Database Name\nconst dbName = 'myProject';\n\nasync function main() {\n  // Use connect method to connect to the server\n  await client.connect();\n  console.log('Connected successfully to server');\n  const db = client.db(dbName);\n  const collection = db.collection('documents');\n\n  // the following code examples can be pasted here...\n\n  return 'done.';\n}\n\nmain()\n  .then(console.log)\n  .catch(console.error)\n  .finally(() => client.close());\n```\n\nRun your app from the command line with:\n\n```bash\nnode app.js\n```\n\nThe application should print **Connected successfully to server** to the console.\n\n### Insert a Document\n\nAdd to **app.js** the following function which uses the **insertMany**\nmethod to add three documents to the **documents** collection.\n\n```js\nconst insertResult = await collection.insertMany([{ a: 1 }, { a: 2 }, { a: 3 }]);\nconsole.log('Inserted documents =>', insertResult);\n```\n\nThe **insertMany** command returns an object wit",
./services/_archive/restored_documents.json.bak-msallis:55334:      "content": "# mquery\n\n`mquery` is a fluent mongodb query builder designed to run in multiple environments.\n\n[![Build Status](https://travis-ci.org/aheckmann/mquery.svg?branch=master)](https://travis-ci.org/aheckmann/mquery)\n[![NPM version](https://badge.fury.io/js/mquery.svg)](http://badge.fury.io/js/mquery)\n\n[![npm](https://nodei.co/npm/mquery.png)](https://www.npmjs.com/package/mquery)\n\n## Features\n\n- fluent query builder api\n- custom base query support\n- MongoDB 2.4 geoJSON support\n- method + option combinations validation\n- node.js driver compatibility\n- environment detection\n- [debug](https://github.com/visionmedia/debug) support\n- separated collection implementations for maximum flexibility\n\n## Use\n\n```js\nconst mongo = require('mongodb');\n\nconst client = new mongo.MongoClient(uri);\nawait client.connect();\n// get a collection\nconst collection = client.collection('artists');\n\n// pass it to the constructor\nawait mquery(collection).find({...});\n\n// or pass it to the collection method\nconst docs = await mquery().find({...}).collection(collection);\n\n// or better yet, create a custom query constructor that has it always set\nconst Artist = mquery(collection).toConstructor();\nconst docs = await Artist().find(...).where(...);\n```\n\n`mquery` requires a collection object to work with. In the example above we just pass the collection object created using the official [MongoDB driver](https://github.com/mongodb/node-mongodb-native).\n\n## Fluent API\n\n- [mquery](#mquery)\n  - [Features](#features)\n  ",
./services/_archive/restored_documents.json.bak-msallis:75054:      "content": "bled ([--ipv6 mongod option documentation](https://www.mongodb.com/docs/manual/reference/program/mongod/#std-option-mongod.--ipv6))\n> - using a host of `127.0.0.1` in place of localhost\n> - specifying the DNS resolution ordering with the `--dns-resolution-order` Node.js command line argument (e.g. `node --dns-resolution-order=ipv4first`)\n\n```js\nconst { MongoClient } = require('mongodb');\n// or as an es module:\n// import { MongoClient } from 'mongodb'\n\n// Connection URL\nconst url = 'mongodb://localhost:27017';\nconst client = new MongoClient(url);\n\n// Database Name\nconst dbName = 'myProject';\n\nasync function main() {\n  // Use connect method to connect to the server\n  await client.connect();\n  console.log('Connected successfully to server');\n  const db = client.db(dbName);\n  const collection = db.collection('documents');\n\n  // the following code examples can be pasted here...\n\n  return 'done.';\n}\n\nmain()\n  .then(console.log)\n  .catch(console.error)\n  .finally(() => client.close());\n```\n\nRun your app from the command line with:\n\n```bash\nnode app.js\n```\n\nThe application should print **Connected successfully to server** to the console.\n\n### Insert a Document\n\nAdd to **app.js** the following function which uses the **insertMany**\nmethod to add three documents to the **documents** collection.\n\n```js\nconst insertResult = await collection.insertMany([{ a: 1 }, { a: 2 }, { a: 3 }]);\nconsole.log('Inserted documents =>', insertResult);\n```\n\nThe **insertMany** command returns an object wit",
./services/_archive/restored_documents.json.bak-msallis:75422:      "content": "# mquery\n\n`mquery` is a fluent mongodb query builder designed to run in multiple environments.\n\n[![Build Status](https://travis-ci.org/aheckmann/mquery.svg?branch=master)](https://travis-ci.org/aheckmann/mquery)\n[![NPM version](https://badge.fury.io/js/mquery.svg)](http://badge.fury.io/js/mquery)\n\n[![npm](https://nodei.co/npm/mquery.png)](https://www.npmjs.com/package/mquery)\n\n## Features\n\n- fluent query builder api\n- custom base query support\n- MongoDB 2.4 geoJSON support\n- method + option combinations validation\n- node.js driver compatibility\n- environment detection\n- [debug](https://github.com/visionmedia/debug) support\n- separated collection implementations for maximum flexibility\n\n## Use\n\n```js\nconst mongo = require('mongodb');\n\nconst client = new mongo.MongoClient(uri);\nawait client.connect();\n// get a collection\nconst collection = client.collection('artists');\n\n// pass it to the constructor\nawait mquery(collection).find({...});\n\n// or pass it to the collection method\nconst docs = await mquery().find({...}).collection(collection);\n\n// or better yet, create a custom query constructor that has it always set\nconst Artist = mquery(collection).toConstructor();\nconst docs = await Artist().find(...).where(...);\n```\n\n`mquery` requires a collection object to work with. In the example above we just pass the collection object created using the official [MongoDB driver](https://github.com/mongodb/node-mongodb-native).\n\n## Fluent API\n\n- [mquery](#mquery)\n  - [Features](#features)\n  ",
./services/_archive/ms_jarvis_consciousness_bridge.py.backup_before_hierarchy:224:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/_archive/ms_jarvis_consciousness_bridge.py.backup_before_hierarchy:235:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/_archive/audit_attrs.py.backup_20251205234718:6:collection = client.get_collection('knowledge_docs')
./services/_archive/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.backup_vocabulary_cleanup:221:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/_archive/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.backup_vocabulary_cleanup:232:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/_archive/reload_all_knowledge.py.backup_vocabulary_cleanup:15:collection = client.get_or_create_collection(name="ms_jarvis_knowledge")
./services/_archive/RESTORE_NATURAL_PERSONALITY.sh.bak-msallis:17:collection = client.get_or_create_collection(name="ms_jarvis_memory")
./services/_archive/ms_jarvis_consciousness_bridge.py.backup_pre_location_integration:107:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/_archive/ms_jarvis_consciousness_bridge.py.backup_pre_location_integration:118:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/_archive/INSPECT_JARVIS_INTERNALS.sh.bak-msallis:20:if grep -q "collection_name = " ai_server_22llm.py; then
./services/_archive/INSPECT_JARVIS_INTERNALS.sh.bak-msallis:22:    grep "collection_name = " ai_server_22llm.py
./services/_archive/audit_attrs.py.backup_20251205234841:18:collection = client.get_collection('knowledge_docs')
./services/_archive/ms_jarvis_consciousness_bridge.py.backup_1759895250:220:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/_archive/ms_jarvis_consciousness_bridge.py.backup_1759895250:231:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/_archive/load_rag_knowledge.py.backup_vocabulary_cleanup:12:collection = chroma.get_or_create_collection(name="mountainshares_knowledge")
./services/_archive/ai_server_restored.py.backup_before_portmanager:106:            self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/_archive/ai_server_restored.py.backup_before_portmanager:115:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/_archive/LOAD_AAACPE_RAG.sh.bak-msallis:80:    collection = client.get_or_create_collection(name="ms_jarvis_memory")
./services/_archive/rag_server.py.backup_20251031:91:        self.knowledge_collection = self.chroma_client.get_or_create_collection(name="mountainshares_knowledge")
./services/_archive/conversation_memory_endpoints.py.backup_before_portmanager:24:collection = client.get_or_create_collection(name="mountainshares_knowledge")
./services/_archive/ai_server.py.backup.20251006_101858:96:        self.knowledge_memory = self.chroma_client.get_or_create_collection(name="mountainshares_knowledge")
./services/_archive/main_brain.py.broken-20260413-134536:1155:                        collection_name == "spiritual_texts"
./services/_archive/ms_jarvis_consciousness_bridge.py.backup_1760220435:220:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/_archive/ms_jarvis_consciousness_bridge.py.backup_1760220435:231:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/_archive/setup_rag.sh.bak-msallis:64:        self.knowledge_collection = self.chroma_client.get_or_create_collection(name="mountainshares_knowledge")
./services/_archive/ms_jarvis_autonomous_learner.py.backup_before_portmanager:63:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./services/_archive/ms_jarvis_consciousness_bridge.py.backup_pre_fixes:222:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/_archive/ms_jarvis_consciousness_bridge.py.backup_pre_fixes:233:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/_archive/ms_jarvis_facebook_dgm_woah.py.backup_vocabulary_cleanup:177:            self.community_wisdom = self.chroma_client.create_collection("community_wisdom")
./services/_archive/ms_jarvis_facebook_dgm_woah.py.backup_20251031:177:            self.community_wisdom = self.chroma_client.create_collection("community_wisdom")
./services/_archive/ms_jarvis_consciousness_bridge.py.backup_before_22llm:222:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/_archive/ms_jarvis_consciousness_bridge.py.backup_before_22llm:233:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/_archive/ms_jarvis_autonomous_learner_optimized.py.backup_before_auto_research:141:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./services/_archive/ms_jarvis_autonomous_learner.py.backup_day2:55:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./services/_archive/integrate_rag.sh.bak-msallis:83:        self.user_memory = self.chroma_client.get_or_create_collection(name="user_interactions")
./services/_archive/ms_jarvis_consciousness_bridge.py.backup_1759895606:220:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/_archive/ms_jarvis_consciousness_bridge.py.backup_1759895606:231:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/_archive/gpu_accelerated_rag_fixed.py.backup_before_portmanager:98:            collection_name = "ms_jarvis_knowledge"
./services/_archive/fix_persona.sh.bak-msallis:74:        self.user_memory = self.chroma_client.get_or_create_collection(name="user_interactions")
./services/_archive/ms_jarvis_autonomous_learner_optimized.py.backup_before_portmanager:90:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./services/_archive/improve_jarvis.sh.bak-msallis:84:        self.user_memory = self.chroma_client.get_or_create_collection(name="user_interactions")
./services/_archive/ms_jarvis_autonomous_learner_WITH_FIFTH_DGM.py.backup_before_portmanager:64:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./services/summarize_docs.py:12:collection = client.get_collection("knowledge_docs")
./services/setup_rag.sh:64:        self.knowledge_collection = self.chroma_client.get_or_create_collection(name="mountainshares_knowledge")
./services/conversation_memory_endpoints.py:24:collection = client.get_or_create_collection(name="mountainshares_knowledge")
./services/load_pdfs_spiritual.py:17:collection = client.get_or_create_collection(name="mountainshares_knowledge")
./services/bulk_load_MAXIMUM.py:19:collection = client.get_or_create_collection(name="mountainshares_knowledge")
./services/load_spiritual_library.py:17:collection = client.get_or_create_collection(name="spiritual_wisdom")
./services/ai/ai_server.py:119:            self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/ai/ai_server.py:131:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/main.py.current.safebak:626:                        collection_name == "spiritual_texts"
./services/ms_jarvis_consciousness_bridge.py.working_backup:224:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/ms_jarvis_consciousness_bridge.py.working_backup:235:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/ms_jarvis_consciousness_bridge.py.phase1_working:222:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/ms_jarvis_consciousness_bridge.py.phase1_working:233:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/audit_attrs.py:18:collection = client.get_collection('knowledge_docs')
./services/ms_jarvis_consciousness_bridge.py.safe_backup:222:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/ms_jarvis_consciousness_bridge.py.safe_backup:233:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/main_brain.py.bak.20260611-214706:2325:                        collection_name == "spiritual_texts"
./services/rag_server.psychology_patched.py:95:        self.knowledge_collection = self.chroma_client.get_or_create_collection(name="mountainshares_knowledge")
./services/REFERENCE_windows_swarm.py:119:            self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/REFERENCE_windows_swarm.py:131:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/gpu_accelerated_rag_fixed.py:98:            collection_name = "ms_jarvis_knowledge"
./services/main_brain.py.bak.20260607_192238:2292:                        collection_name == "spiritual_texts"
./services/load_knowledge.sh:33:collection = chroma.get_or_create_collection(name="mountainshares_knowledge")
./services/rag_server.py:134:            self.knowledge_collection_name = "msjarvis_docs"
./services/rag_server.py:137:            self.knowledge_collection = self.chroma_client.get_or_create_collection(
./services/ms_jarvis_autonomous_learner_WITH_FIFTH_DGM.py:85:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./services/ai_server_restored.py:107:            self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/ai_server_restored.py:116:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/ms_jarvis_complete_knowledge_ingestion.py:50:        collection = client.get_or_create_collection(
./services/ms_jarvis_complete_knowledge_ingestion.py:94:        collection = client.get_or_create_collection(
./services/ms_jarvis_complete_knowledge_ingestion.py:136:        collection = client.get_or_create_collection(
./services/test_knowledge_base.py:9:collection = client.get_collection("egeria_docs")
./services/rag_server_min.py:63:        self.knowledge_collection = self.chroma_client.get_or_create_collection(
./services/load_rag_knowledge.py:16:collection = chroma.get_or_create_collection(name="mountainshares_knowledge")
./services/main_brain.py:2340:                        collection_name == "spiritual_texts"
./services/ingest_knowledge_simple.py:19:    collection = client.get_collection("egeria_docs")
./services/ingest_knowledge_simple.py:22:    collection = client.create_collection("egeria_docs")
./services/load_rag_knowledge_9381.log:15:    collection = chroma.get_or_create_collection(name="mountainshares_knowledge")
./services/load_rag_knowledge_9381.log:18:    model = self._server.get_or_create_collection(
./services/load_rag_knowledge_9381.log:24:    return self.create_collection(
./services/export_attributes_to_gis.py:7:collection = client.get_collection('knowledge_docs')
./services/msjarvisautonomouslearner.py:85:            self.learned_knowledge = self.chroma_client.get_or_create_collection(
./services/reload_all_knowledge.py:19:collection = client.get_or_create_collection(name="ms_jarvis_knowledge")
./services/main_brain_LEGACY_32svc.py:1105:                        collection_name == "spiritual_texts"
grep: ./services/MountainShares6.pdf: No such file or directory
grep: ./data/local_resources: Permission denied
grep: ./data/mysql/#ib_16384_0.dblwr: Permission denied
grep: ./data/mysql/mysql.ibd: Permission denied
grep: ./data/mysql/private_key.pem: Permission denied
grep: ./data/mysql/sys: Permission denied
grep: ./data/mysql/binlog.000007: Permission denied
grep: ./data/mysql/ib_buffer_pool: Permission denied
grep: ./data/mysql/ibtmp1: Permission denied
grep: ./data/mysql/auto.cnf: Permission denied
grep: ./data/mysql/binlog.000005: Permission denied
grep: ./data/mysql/client-key.pem: Permission denied
grep: ./data/mysql/undo_002: Permission denied
grep: ./data/mysql/binlog.000008: Permission denied
grep: ./data/mysql/binlog.000002: Permission denied
grep: ./data/mysql/binlog.000013: Permission denied
grep: ./data/mysql/binlog.000012: Permission denied
grep: ./data/mysql/binlog.000009: Permission denied
grep: ./data/mysql/binlog.000003: Permission denied
grep: ./data/mysql/binlog.000001: Permission denied
grep: ./data/mysql/binlog.index: Permission denied
grep: ./data/mysql/server-key.pem: Permission denied
grep: ./data/mysql/binlog.000010: Permission denied
grep: ./data/mysql/ca-key.pem: Permission denied
grep: ./data/mysql/#innodb_temp: Permission denied
grep: ./data/mysql/mysql.sock: No such device or address
grep: ./data/mysql/binlog.000014: Permission denied
grep: ./data/mysql/quantum_ai: Permission denied
grep: ./data/mysql/mysql: Permission denied
grep: ./data/mysql/#ib_16384_1.dblwr: Permission denied
grep: ./data/mysql/ibdata1: Permission denied
grep: ./data/mysql/binlog.000011: Permission denied
grep: ./data/mysql/binlog.000004: Permission denied
grep: ./data/mysql/performance_schema: Permission denied
grep: ./data/mysql/binlog.000006: Permission denied
grep: ./data/mysql/#innodb_redo: Permission denied
grep: ./data/mysql/undo_001: Permission denied
grep: ./chroma_db/chroma_db: No such file or directory
./services/ms_jarvis_consciousness_bridge.py.original:220:# COMMENTED OUT - no chroma_client:             self.knowledge_memory = self.chroma_client.get_or_create_collection(
./services/ms_jarvis_consciousness_bridge.py.original:231:            self.knowledge_memory = self.chroma_client.create_collection("mountainshares_knowledge")
./services/host_bulk_loader.py:18:collection = client.get_or_create_collection(name="mountainshares_knowledge")
./services/export_metadata_csv.py:3:collection = client.get_collection('knowledge_docs')
./services/mountainshares_chain_monitor.py:54:        col = client.get_or_create_collection("mountainshares_knowledge")
./services/main_brain.py.bak.20260607_192243:2292:                        collection_name == "spiritual_texts"
./services/ms_jarvis_facebook_dgm_woah.py:181:            self.community_wisdom = self.chroma_client.create_collection("community_wisdom")
./services/load_complete_knowledge_base.py:36:    spiritual_col = client.create_collection(
./services/load_complete_knowledge_base.py:46:    ms_col = client.create_collection(
./services/load_complete_knowledge_base.py:56:    gis_col = client.create_collection(
./.fixbackups/20260530-102909/services/main_brain_LEGACY_32svc.py:1105:                        collection_name == "spiritual_texts"
./ms-allis-frontend/node_modules/@typescript-eslint/scope-manager/dist/lib/esnext.collection.js:7:exports.esnext_collection = void 0;
./ms-allis-frontend/node_modules/@typescript-eslint/scope-manager/dist/lib/esnext.collection.js:10:exports.esnext_collection = {
./ms-allis-frontend/node_modules/@typescript-eslint/scope-manager/dist/lib/es2024.collection.js:7:exports.es2024_collection = void 0;
./ms-allis-frontend/node_modules/@typescript-eslint/scope-manager/dist/lib/es2024.collection.js:9:exports.es2024_collection = {
./ms-allis-frontend/node_modules/@typescript-eslint/scope-manager/dist/lib/es2015.collection.js:7:exports.es2015_collection = void 0;
./ms-allis-frontend/node_modules/@typescript-eslint/scope-manager/dist/lib/es2015.collection.js:9:exports.es2015_collection = {
./ms-allis-frontend/node_modules/@typescript-eslint/scope-manager/dist/lib/es2023.collection.js:7:exports.es2023_collection = void 0;
./ms-allis-frontend/node_modules/@typescript-eslint/scope-manager/dist/lib/es2023.collection.js:9:exports.es2023_collection = {
./ms-allis-frontend/node_modules/@typescript-eslint/scope-manager/dist/lib/es2025.collection.js:7:exports.es2025_collection = void 0;
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild

find . -type f \( \
  -iname '*spiritual*' -o \
  -iname '*egeria*' -o \
  -iname '*allis*' -o \
  -iname '*commons*' -o \
  -iname '*.md' -o \
  -iname '*.txt' \
\) 2>/dev/null | sort > /tmp/spiritual_sources.txt

wc -l /tmp/spiritual_sources.txt
sed -n '1,120p' /tmp/spiritual_sources.txt
2726 /tmp/spiritual_sources.txt
./ai-server/requirements.txt
./all_gis_vectors_filtered.txt
./all_gis_vectors_full.txt
./all_gis_vectors_ingest.txt
./all_gis_vectors.txt
./all_gis_vectors_unique.txt
./_archive/generated_20260430/activate_egeria_persona.py
./_archive/generated_20260430/egeria_web_ui_dynamic.py
./_archive/generated_20260430/egeria_web_ui_final_biological.py
./_archive/generated_20260430/egeria_web_ui_FIXED.py
./_archive/generated_20260430/egeria_web_ui_fixed_simple.py
./_archive/generated_20260430/egeria_web_ui_plain_authentic.py
./_archive/generated_20260430/egeria_web_ui_v3_consciousness.py
./_archive/generated_20260430/egeria_web_ui_with_execution.py
./_archive/generated_20260430/egeria_web_ui_working.py
./_archive/generated_20260430/load_pdfs_spiritual.py
./_archive/generated_20260430/load_spiritual_library.py
./_archive/MOUNTED_FILES_CORRECTED_20260430.txt
./_archive/MOUNTED_FILES_DO_NOT_ARCHIVE.txt
./_archive/MOUNTED_FILES_GROUNDTRUTH_20260430.txt
./archives/connector_gateway_to_nbb_spiritual_maternal_integration.jsonl
./archives/connector_gateway_to_nbb_spiritual_root.jsonl
./_archive/service_baks_20260430/ai_server_19llm_CONSCIOUS.py.before_egeria
./_archive/service_baks_20260430/consciousness_with_egeria_voice.py.backup_vocabulary_cleanup
./_archive/service_baks_20260430/egeria_autonomous_inquiry.py.bak
./_archive/service_baks_20260430/egeria_facebook_perpetual_scheduler.py.backup
./_archive/service_baks_20260430/egeria_facebook_perpetual_scheduler.py.backup.1762961759
./_archive/service_baks_20260430/egeria_facebook_perpetual_scheduler.py.before_memory_20251108
./_archive/service_baks_20260430/main_brain.py.bak_egeria_patch_1777059405
./_archive/service_baks_20260430/main_brain.py.before_spiritual_integration
./_archive/service_baks_20260430/main_brain.py.before_spiritual_rag
./_archive/service_baks_20260430/ms_jarvis_command_orchestrator.py.backup_before_spiritual_fix
./audit_20260326_1050.txt
./BACKLOG_ASPIRATIONAL.md
./backup_filename_index.txt
./backup_roots.txt
./bbb_requirements.txt
./chroma_ingestion_sources.txt
./contracts/node_modules/abitype/README.md
./contracts/node_modules/@actions/core/LICENSE.md
./contracts/node_modules/@actions/core/README.md
./contracts/node_modules/@actions/exec/LICENSE.md
./contracts/node_modules/@actions/exec/README.md
./contracts/node_modules/@actions/http-client/README.md
./contracts/node_modules/@actions/io/LICENSE.md
./contracts/node_modules/@actions/io/README.md
./contracts/node_modules/adm-zip/README.md
./contracts/node_modules/@adraffy/ens-normalize/README.md
./contracts/node_modules/aes-js/lib.commonjs/README.md
./contracts/node_modules/aes-js/lib.esm/README.md
./contracts/node_modules/aes-js/LICENSE.txt
./contracts/node_modules/aes-js/misc/basedirs/lib.commonjs/README.md
./contracts/node_modules/aes-js/misc/basedirs/lib.esm/README.md
./contracts/node_modules/aes-js/README.md
./contracts/node_modules/ansi-colors/README.md
./contracts/node_modules/ansi-regex/readme.md
./contracts/node_modules/ansi-styles/readme.md
./contracts/node_modules/bn.js/README.md
./contracts/node_modules/brorand/README.md
./contracts/node_modules/cbor2/LICENSE.md
./contracts/node_modules/cbor2/README.md
./contracts/node_modules/chalk/readme.md
./contracts/node_modules/chokidar/README.md
./contracts/node_modules/color-convert/CHANGELOG.md
./contracts/node_modules/color-convert/README.md
./contracts/node_modules/color-name/README.md
./contracts/node_modules/diff-sequences/README.md
./contracts/node_modules/dotenv/CHANGELOG.md
./contracts/node_modules/dotenv/README-es.md
./contracts/node_modules/dotenv/README.md
./contracts/node_modules/dotenv/SECURITY.md
./contracts/node_modules/elliptic/node_modules/bn.js/README.md
./contracts/node_modules/elliptic/README.md
./contracts/node_modules/enquirer/README.md
./contracts/node_modules/env-paths/readme.md
./contracts/node_modules/esbuild/LICENSE.md
./contracts/node_modules/@esbuild/linux-x64/README.md
./contracts/node_modules/esbuild/README.md
./contracts/node_modules/ethereum-cryptography/node_modules/@noble/hashes/README.md
./contracts/node_modules/ethereum-cryptography/README.md
./contracts/node_modules/ethers/CHANGELOG.md
./contracts/node_modules/ethers/dist/README.md
./contracts/node_modules/ethers/lib.commonjs/README.md
./contracts/node_modules/ethers/lib.esm/README.md
./contracts/node_modules/ethers/LICENSE.md
./contracts/node_modules/ethers/node_modules/@noble/curves/README.md
./contracts/node_modules/ethers/node_modules/@noble/hashes/README.md
./contracts/node_modules/@ethersproject/abi/LICENSE.md
./contracts/node_modules/@ethersproject/abi/README.md
./contracts/node_modules/@ethersproject/abstract-provider/LICENSE.md
./contracts/node_modules/@ethersproject/abstract-provider/README.md
./contracts/node_modules/@ethersproject/abstract-signer/LICENSE.md
./contracts/node_modules/@ethersproject/abstract-signer/README.md
./contracts/node_modules/@ethersproject/address/LICENSE.md
./contracts/node_modules/@ethersproject/address/README.md
./contracts/node_modules/@ethersproject/base64/LICENSE.md
./contracts/node_modules/@ethersproject/base64/README.md
./contracts/node_modules/@ethersproject/bignumber/LICENSE.md
./contracts/node_modules/@ethersproject/bignumber/README.md
./contracts/node_modules/@ethersproject/bytes/LICENSE.md
./contracts/node_modules/@ethersproject/bytes/README.md
./contracts/node_modules/@ethersproject/constants/LICENSE.md
./contracts/node_modules/@ethersproject/constants/README.md
./contracts/node_modules/@ethersproject/hash/LICENSE.md
./contracts/node_modules/@ethersproject/hash/README.md
./contracts/node_modules/@ethersproject/keccak256/LICENSE.md
./contracts/node_modules/@ethersproject/keccak256/README.md
./contracts/node_modules/@ethersproject/logger/README.md
./contracts/node_modules/@ethersproject/networks/LICENSE.md
./contracts/node_modules/@ethersproject/networks/README.md
./contracts/node_modules/@ethersproject/properties/LICENSE.md
./contracts/node_modules/@ethersproject/properties/README.md
./contracts/node_modules/@ethersproject/rlp/LICENSE.md
./contracts/node_modules/@ethersproject/rlp/README.md
./contracts/node_modules/@ethersproject/signing-key/LICENSE.md
./contracts/node_modules/@ethersproject/signing-key/README.md
./contracts/node_modules/@ethersproject/strings/LICENSE.md
./contracts/node_modules/@ethersproject/strings/README.md
./contracts/node_modules/@ethersproject/transactions/LICENSE.md
./contracts/node_modules/@ethersproject/transactions/README.md
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

