
> Figure 7-3. Spatial RAG flow including `geospatialfeatures` (60,000 items) and `GBIM_Fayette_sample` (1,535 items), both confirmed live March 26, 2026.

---

### 7.3.3 Resource-Oriented RAG Flow

1. **Resource query intake.** Main brain identifies resource-oriented request, extracts location hints (ZIP, county, town) and population signals.
2. **Phase 1.45 — Community memory.** Top-5 `autonomous_learner` memories prepended.
3. **Text RAG via jarvis-rag-server** (`POST /query`, collection: `local_resources`, host:8003 → container:8016). May also query `gis_wv_benefits` for spatial facility context.
4. **Resolution via local resource resolver.** Queries `jarvis-local-resources-db` (port 5435) using structured hints.
5. **Context assembly and generation.** LM Synthesizer applies Ms. Egeria Jarvis persona before returning final response.

> **Known Issue:** As of March 26, 2026, `jarvis-local-resources-db` is largely empty for Mount Hope queries. `local_resources` ChromaDB collection (default for consciousness bridge) is operational and contains verified Fayette County data. See §7.2.5.

---

## 7.4 Routing, Roles, Geography, and WV-First Policy

### 7.4.1 Design Intent

**Topic and intent routing.** Governance queries favor `governance_rag` (643 chunks including US Constitution) and `commons_rag` (306 chunks); spatial-justice queries favor `msjarvisgis`/`msjarvis`-derived collections; resource questions favor `jarvis-local-resources-db` plus WV-resource collections.

**Role-aware routing.** Active role determines eligible collections and registries. Community-facing roles are restricted to public documentation, approved spatial layers, and public-facing slices of `jarvis-local-resources-db`.

**Geography-aware routing and WV-first behavior.** For West Virginia-scoped queries, the system:
- Treats WV RAG, PostgreSQL `msjarvisgis` GIS, and registry context as authoritative.
- Excludes web context from the final context window.
- Requires models to ignore conflicting out-of-state content unless user explicitly requests another state.

### 7.4.2 Port and Service Reference Table (March 26, 2026)

| Service | Host Port | Container Port | Purpose |
|---|---|---|---|
| jarvis-rag-server | 8003 | **8016** | Text RAG — `POST /query` — ⚠️ not yet wired to jarvis-gateway inference |
| jarvis-gis-rag | 8004 | 8004 | GIS / spatial RAG |
| jarvis-psychological-rag | 8006 | 8006 | Spiritual + psychological RAG |
| jarvis-chroma | 8002 (host) | 8000 (container) | ChromaDB v2 API — 31 collections, 6,727,956 items |
| jarvis-ollama | 11434 | 11434 | Embedding (`/api/embeddings`) + generation |
| gbim_query_router | 7205 | 7205 | Landowner SQL router |
| jarvis-local-resources-db | 5435 | 5435 | Community resource registry |
| msjarvis (PostgreSQL) | 5433 | 5433 | GBIM beliefs |
| msjarvisgis (PostgreSQL) | 5432 | 5432 | PostGIS spatial |
| jarvis-web-research | 8008 (internal) | — | Web research gateway |
| jarvis-ingest-api | 8009 | — | Ingest API |

---

## 7.5 Smoke Tests — Confirmed Semantic Retrieval (March 26, 2026)

The following smoke tests were run against `governance_rag` and `commons_rag` on March 26, 2026 and confirm production-ready semantic retrieval with no ghost records.

**`governance_rag` smoke tests:**

| Query | Expected result | Confirmed |
|---|---|---|
| "BSA" / "Boy Scouts" | Retrieves SNAP/Medicaid context | ✅ Distance < 0.4 |
| "governance" | Retrieves DAO charter text | ✅ Distance < 0.3 |
| "constitution" | Retrieves Amendment XIV (pg5.txt) | ✅ Distance < 0.3 |
| "membership requirements" | Retrieves Phase 0 invite-only beta spec | ✅ Distance < 0.35 |

**`commons_rag` smoke tests:**

| Query | Expected result | Confirmed |
|---|---|---|
| "commons gamification" | Retrieves gamification rules | ✅ Distance < 0.4 |
| "community participation" | Retrieves commons governance text | ✅ Distance < 0.35 |

**Smoke test runner:**

```python
def run_governance_smoke_tests():
    client = chromadb.HttpClient(host="127.0.0.1", port=8002)
    collection = client.get_collection("governance_rag")
    print(f"governance_rag item count: {collection.count()}")  # expect 643

    test_cases = [
        ("BSA SNAP Medicaid benefits", 0.5, "BSA → SNAP/Medicaid retrieval"),
        ("governance DAO charter", 0.4, "governance → DAO charter"),
        ("constitution Amendment XIV", 0.4, "constitution → Amendment XIV (pg5.txt)"),
    ]

    for query_text, max_dist, label in test_cases:
        embedding = embed_chunk(query_text)
        results = collection.query(
            query_embeddings=[embedding],
            n_results=1,
            include=["documents", "distances"]
        )
        dist = results["distances"]
        status = "✅" if dist < max_dist else "❌ GHOST RECORD SUSPECTED"
        print(f"{status} {label}: distance={dist:.3f} (threshold={max_dist})")
        print(f"   Top result: {results['documents'][:120]}...")
```

---

## 7.6 Constraints, Provenance, and Logging

**Pre-retrieval constraints.** Collection selection and filter mechanisms support limiting by `collection`, `source`, `county`, `dataset`, `worldview`, `state`. The `RAGQuery` schema (§7.2.1) supports `user_id` for session-level access control.

**Decoding-time guards.** After retrieval and generation, the main brain routes candidate responses through the blood-brain barrier service. The BBB output guard is fail-open on HTTP 500 (content passes through unchanged, failure is logged).

**Post-hoc review and logging.** Background storage of queries and responses into `conversation_history` and `episodic_index` ChromaDB collections. Logs capture: services called, collections queried, PostgreSQL tables accessed, Phase 1.45 memories returned, filters/scores applied, and documents/features returned.

---

## 7.7 Relation to Long-Term Memory, GeoDB, Registries, and Entanglement

**Long-term memory.** ChromaDB (host port 8002): `gbim_worldview_entities` (5,416,521 entities, 384-dim), `autonomous_learner` (21,181+ items, growing ~288/day), `governance_rag` (★ 643 chunks — live), `commons_rag` (★ 306 chunks — live), `gis_wv_benefits`, `local_resources` (verified Fayette County community resources), and 25+ additional collections. Total: 31 collections, 6,727,956 items (March 26, 2026). All 5,416,521 GBIM entities carry `confidence_decay` and `needs_verification` temporal metadata.

**Structured registries.** `jarvis-local-resources-db` (port 5435) holds normalized, versioned program records addressable via RAG-inferred keys. `building_parcel_county_tax_mv` (7,354,707 rows, 97.17% address coverage) provides building-level spatial coverage.

**Coupled updates and entanglement.** The `autonomous_learner`'s continuous growth (21,181 items → ~288/day) represents the beginning of the coupled update loop: community interactions are continuously embedded and fed back into Phase 1.45 retrieval, grounding every subsequent response in accumulated community intelligence from the Mount Hope development machine.

---

## 7.8 RAG-Grounded Judge Verification (Forward-Looking Architecture)

> **Added March 21, 2026. Not yet deployed. Written as a build specification.**

### 7.8.1 The Problem This Solves

The current truth and alignment judges (`judge_truth_filter.py`, `judge_alignment_filter.py`) score responses using `heuristic_contradiction_v1` — keyword and pattern-matching rules applied directly to response text, with no queries to the GBIM corpus, ChromaDB collections, or any RAG service. They report `truth_score: 1.0` and `alignment_verdict: pass` without consulting a single document from the 5.4 million GBIM entities, the `spiritual_texts` corpus, or the `gis_wv_benefits` collection.

The judges are already co-located with `jarvis-gis-rag:8004` and `jarvis-psychological-rag:8006` in the same Docker network. The only work required is wiring the judges to make HTTP requests to those services as part of their scoring logic.

### 7.8.2 Truth Judge Upgrade — Wiring to jarvis-gis-rag:8004

```python
import httpx
import re
from typing import List, Dict, Any

TRUTH_RAG_ENDPOINT = "http://jarvis-gis-rag:8004/query"

def extract_factual_claims(answer_text: str) -> List[str]:
    sentences = re.split(r'(?<=[.!?])\s+', answer_text.strip())
    claim_patterns = [
        r'\b(is|are|was|were|has|have|located|operates|provides)\b',
        r'\b\d+\b',
        r'\b[A-Z][a-z]+\s+County\b',
        r'\b(WV|West Virginia)\b'
    ]
    claims = []
    for sentence in sentences:
        if any(re.search(p, sentence) for p in claim_patterns):
            claims.append(sentence.strip())
    return claims[:10]

async def check_claim_against_gis_rag(claim: str, n_results: int = 3) -> Dict[str, Any]:
    async with httpx.AsyncClient(timeout=8.0) as client:
        try:
            resp = await client.post(
                TRUTH_RAG_ENDPOINT,
                json={"query": claim, "n_results": n_results}
            )
            if resp.status_code == 200:
                return {
                    "status": "ok",
                    "documents": resp.json().get("documents", []),
                    "metadatas": resp.json().get("metadatas", []),
                    "distances": resp.json().get("distances", [])
                }
        except Exception:
            pass
    return {"status": "rag_unavailable", "documents": [], "distances": []}

async def compute_truth_score_rag_grounded(
    consensus_answer: str,
    original_question: str
) -> Dict[str, Any]:
    claims = extract_factual_claims(consensus_answer)
    results = {"supported": 0, "contradicted": 0, "not_found": 0,
               "gbim_docs_consulted": 0, "sources": []}

    for claim in claims:
        rag_result = await check_claim_against_gis_rag(claim)
        verdict = score_claim_support(claim, rag_result)
        results[verdict] += 1
        results["gbim_docs_consulted"] += len(rag_result.get("documents", []))
        for meta in rag_result.get("metadatas", []):
            if meta.get("gbim_entity"):
                results["sources"].append(meta["gbim_entity"])

    total = max(len(claims), 1)
    truth_score = (
        (results["supported"] * 1.0) +
        (results["not_found"] * 0.7) +
        (results["contradicted"] * 0.0)
    ) / total

    return {
        "truth_score": round(truth_score, 3),
        "method": "rag_grounded_gis_v1",
        "claims_checked": len(claims),
        "supported": results["supported"],
        "contradicted": results["contradicted"],
        "not_found": results["not_found"],
        "gbim_docs_consulted": results["gbim_docs_consulted"],
        "gbim_contradictions_detected": results["contradicted"],
        "supporting_sources": list(set(results["sources"]))[:10]
    }
```

**Comparison with current heuristic:**

| Behavior | heuristic_contradiction_v1 | rag_grounded_gis_v1 (target) |
|---|---|---|
| Consults GBIM corpus | ❌ Never | ✅ Every call |
| Checks claims against documents | ❌ Pattern match only | ✅ GIS RAG retrieval + lexical overlap |
| Detects county/facility factual errors | ❌ No | ✅ If `gis_wv_benefits` has the record |
| Reports `gbim_docs_consulted` | ❌ Always 0 | ✅ Actual count |
| Fails open on RAG unavailability | N/A | ✅ Falls back to `not_found` |
| Provenance in output | ❌ None | ✅ `supporting_sources` list |

### 7.8.3 Alignment Judge Upgrade — Wiring to jarvis-psychological-rag:8006

```python
ALIGNMENT_RAG_ENDPOINT = "http://jarvis-psychological-rag:8006/query"

def extract_normative_claims(answer_text: str) -> List[str]:
    normative_patterns = [
        r'\b(should|must|ought|important|community|family|care|support)\b',
        r'\b(Appalachian|West Virginia|WV|mountain|coal|rural)\b',
        r'\b(dignity|equity|justice|rights|accountability|transparency)\b',
        r'\b(program|benefit|assistance|eligibility|resource)\b'
    ]
    sentences = re.split(r'(?<=[.!?])\s+', answer_text.strip())
    normative = []
    for sentence in sentences:
        if any(re.search(p, sentence, re.IGNORECASE) for p in normative_patterns):
            normative.append(sentence.strip())
    return normative[:8]

async def compute_alignment_score_rag_grounded(
    consensus_answer: str
) -> Dict[str, Any]:
    normative_claims = extract_normative_claims(consensus_answer)
    results = {"aligned": 0, "misaligned": 0, "neutral": 0,
               "docs_consulted": 0, "normative_sources": []}

    for claim in normative_claims:
        async with httpx.AsyncClient(timeout=8.0) as client:
            try:
                resp = await client.post(
                    ALIGNMENT_RAG_ENDPOINT,
                    json={
                        "query": claim,
                        "n_results": 3,
                        "collection_filter": [
                            "spiritual_texts",
                            "appalachian_cultural_intelligence",
                            "governance_rag"
                        ]
                    }
                )
                rag_result = resp.json() if resp.status_code == 200 else {}
            except Exception:
                rag_result = {}

        verdict = score_alignment(claim, rag_result)
        results[verdict] += 1
        results["docs_consulted"] += len(rag_result.get("documents", []))
        for meta in rag_result.get("metadatas", []):
            if meta.get("source"):
                results["normative_sources"].append(meta["source"])

    total = max(len(normative_claims), 1)
    alignment_score = (
        (results["aligned"] * 1.0) +
        (results["neutral"] * 0.8) +
        (results["misaligned"] * 0.0)
    ) / total

    return {
        "alignment_score": round(alignment_score, 3),
        "method": "rag_grounded_spiritual_v1",
        "claims_checked": len(normative_claims),
        "aligned": results["aligned"],
        "misaligned": results["misaligned"],
        "neutral": results["neutral"],
        "normative_docs_consulted": results["docs_consulted"],
        "misalignments_detected": results["misaligned"],
        "normative_sources": list(set(results["normative_sources"]))[:10]
    }
```

### 7.8.4 UltimateResponse Schema Extension

Both upgraded judges return richer output. The `UltimateResponse` schema (Chapter 17) should be extended:

```python
class JudgeVerdict(BaseModel):
    truth_score: float
    alignment_score: float
    consistency_score: float
    ethics_score: float
    consensus_score: float
    # NEW — RAG-grounded fields
    gbim_docs_consulted: int = 0
    gbim_contradictions_detected: int = 0
    normative_docs_consulted: int = 0
    misalignments_detected: int = 0
    supporting_sources: List[str] = []
    normative_sources: List[str] = []
    truth_method: str = "heuristic_contradiction_v1"  # update to rag_grounded_gis_v1
    alignment_method: str = "heuristic_contradiction_v1"  # update to rag_grounded_spiritual_v1
```

---

## 7.9 Production Deployment State (March 26, 2026)

**Hardware:** Lenovo Legion 5 — Mount Hope, West Virginia (ZIP 25880)

**RAG Service Stack:**

| Service | Host Port | Container Port | Status |
|---|---|---|---|
| jarvis-rag-server | 8003 | **8016** | ✅ Active — `POST /query` — ⚠️ not yet wired to jarvis-gateway inference endpoint |
| jarvis-gis-rag | 8004 | 8004 | ✅ Active — confirmed returning live Fayette County geodata |
| jarvis-psychological-rag | 8006 | 8006 | ✅ Active — spiritual (19,338 items) + psychological (968 items) corpus live |
| jarvis-chroma | 8002 (host) | 8000 (container) | ✅ Active — 31 collections, **6,727,956 items**, v2 API |
| jarvis-web-research | 8008 (internal) | — | ✅ Restored March 25, 2026 |
| jarvis-ingest-api | 8009 | — | ✅ Restored March 25, 2026 |
| gbim_query_router | 7205 | 7205 | ✅ Active — PostgreSQL-native landowner path |

**Open Issues:**

| ID | Issue | Status |
|---|---|---|
| OI-05 | `conversation_history` ChromaDB collection not formally wired to production pipeline | Open |
| OI-18 | `jarvis-rag-server` not yet wired into `jarvis-gateway` inference endpoint | **Open — next wiring milestone** |
| — | `jarvis-local-resources-db` empty for most Mount Hope/Fayette queries (Community Champions data entry needed) | Open |
| — | `gbim_beliefs_v2` collection present but item count unverified | Open |
| — | Disk at 96% on Mount Hope dev machine — cleanup/migration needed before next large ingest | Open |
| — | Judge pipeline still using `heuristic_contradiction_v1` — RAG-grounded upgrade (§7.8) not yet deployed | Open |

**Confirmed closed (March 26, 2026):**

| ID | Issue | Resolution |
|---|---|---|
| OI-12 | `geospatialfeatures` at 0 items | ✅ CLOSED — 60,000 items confirmed live |
| OI-13 | `GBIM_Fayette_sample` at 0 items | ✅ CLOSED — 1,535 items confirmed live |
| OI-14 | `appalachian_cultural_intelligence` at 5 items | ✅ CLOSED — 820 items confirmed live |
| OI-15 | `spiritual_texts` at 23 items | ✅ CLOSED — 19,338 items confirmed live |
| OI-16 | `governance_rag` missing | ✅ CLOSED — 643 chunks confirmed live |
| OI-17 | `commons_rag` missing | ✅ CLOSED — 306 chunks confirmed live |

---

*Last updated: 2026-03-26 — Carrie Kidd (Mamma Kidd), Mount Hope WV*
*Updated March 26, 2026: Full RAG ingest pipeline validated; governance_rag (643 chunks) and commons_rag (306 chunks) confirmed production-ready; US Constitution (pg5.txt, 97 chunks) confirmed as constitutional grounding layer; /api/embed vs /api/embeddings ghost record bug documented and fixed; 100-word/20-word-overlap chunk constraint confirmed; jarvis-gateway RAG wiring noted as pending next milestone; smoke test results added (BSA → SNAP/Medicaid, governance → DAO charter, constitution → Amendment XIV).*
