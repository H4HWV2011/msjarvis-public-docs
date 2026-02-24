> **Why this matters for Polymathmatic Geography**
> This chapter describes the Appalachian AI Culture & Personality Engine (AaaCPE), a dual-service
> system providing cultural intelligence and regional context to Ms. Egeria Jarvis. It supports:
> - **P1 – Every where is entangled** by coupling cultural values, anti-patterns, emergency
>   protocols, and scraped regional content into the same retrieval infrastructure used by spatial
>   and semantic services.
> - **P3 – Power has a geometry** by making cultural constraint logic explicit and queryable —
>   named categories, confirmed endpoints, and an auditable Chroma volume — rather than hiding
>   it inside opaque model weights.
> - **P5 – Design is a geographic act** by treating Appalachian communication patterns as a
>   designed interface between communities' lived realities and Ms. Jarvis's responses, not as a
>   surface styling layer.
> - **P12 – Intelligence with a ZIP code** by grounding retrieval in West Virginia–specific
>   materials: Fayette County emergency contacts, documented genealogy, WV broadband news, and
>   heritage preservation content.
> - **P16 – Power accountable to place** by documenting anti-stereotyping governance, quarterly
>   content audits, and a planned community advisory board so communities can inspect and
>   challenge how their culture is represented.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the
> AaaCPE dual-service architecture, its confirmed document corpus, and the integration path
> through which cultural intelligence influences Ms. Jarvis's responses.

---

## Status as of February 2026

| Category | Details |
|---|---|
| **Implemented now** | `jarvis-aaacpe-rag` confirmed running at **127.0.0.1:8032** (`docker compose ps`). Endpoints operational: `GET /` (status and document count), `GET /health`, `POST /search` (params: `query`, `top_k`), `POST /ingest`. `jarvis-aaacpe-scraper` confirmed running at **127.0.0.1:8033**. Endpoints operational: `GET /` (scraper status), `GET /health` (last scrape time and document count), `POST /scrape_now`, `POST /ingest_test`. Shared Docker volume `aaacpe-cultural-data` mounted at `/data` in both containers. Chroma collection `appalachian_cultural_intelligence` in `PersistentClient` at `/data/aaacpe_chroma`. **Total documents as of current deployment: 10** — 7 base cultural intelligence documents (core values, anti-patterns, emergency protocol, example utility assistance, heritage mode, geographic context integration, professional warmth) + 3 scraped test documents (WV broadband initiative, Appalachian Heritage Month events, Fayette County historic preservation funding). Document categories confirmed: `values`, `anti_pattern`, `examples`, `emergency`, `heritage`, `scraped_content`. `aaacperag` registered in `SERVICES` registry in `jarvis-main-brain` (port **8050**) as `http://jarvis-aaacpe-rag:8032`. Both services on `qualia-net` Docker network. |
| **Partially implemented / scaffolded** | Live web scraping (`POST /scrape_now`) is implemented in code but scheduled automated runs (daily 6 AM + every 6 hours) are not yet active in the current deployment; content addition is currently via `POST /ingest_test` and manual `POST /scrape_now` calls. Integration of AaaCPE context into `ultimatechat` synthesis path is wired via the `SERVICES` registry but cultural intelligence application logic (`apply_cultural_intelligence`) is not confirmed active on every `/chat` call in the current deployment — it is available for explicit invocation. Anti-pattern enforcement in response synthesis is partially implemented; the check-and-revise logic is scaffolded but not yet fully rule-documented. |
| **Future work / design intent only** | Scheduled automated scraping (WV Gazette-Mail, Rural.org, AppVoices) running daily + every 6 hours. GeoDB integration linking cultural patterns to geographic features, supporting queries like "community values in Fayette County." GBIM integration for personalization based on user heritage and community role. Expanded content categories: economic development, educational resources, healthcare communication, legal mediation. Community feedback loop allowing stakeholders to flag content and suggest changes. Community Advisory Board with authority to request content removal or modification. AAPCAppE corpus integration for linguistic feature understanding (not dialect performance). Multi-regional expansion respecting variation within Appalachian communities. |

> **Cross-reference:** AaaCPE is registered in the `SERVICES` dictionary in `jarvis-main-brain`
> (port **8050**) and is available as a meaning-oriented service in the `ultimatechat` path.
> For the canonical description of how the `SERVICES` registry and service discovery work, see
> **Chapter 17**. For the broader meaning-oriented vs. analytical path asymmetry, see
> **Chapter 23**. For the BBB pipeline that enforces anti-stereotyping and ethical constraints
> as a live gate on every request, see **Chapter 16**.

---

# 30. AaaCPE Cultural Intelligence System

This chapter describes the Appalachian AI Culture & Personality Engine (AaaCPE), a dual-service
system providing cultural intelligence and regional context to Ms. Egeria Jarvis. Unlike dialect
modeling or linguistic corpus work, AaaCPE focuses on **respectful communication patterns,
cultural values, and contextual awareness** for Appalachian communities. In the current
deployment, it is realized as two confirmed running services sharing a persistent Chroma database
with 10 documents of cultural guidance and regional content.

---

## 30.1 Purpose and Principles

In the current deployment, the AaaCPE system exists to prevent cultural stereotyping while
enabling authentic, respectful engagement with Appalachian communities.

**Core Principle: Cultural intelligence ≠ Dialect performance.** The system distinguishes between
cultural intelligence (understanding values, communication contexts, and appropriate responses)
and dialect performance (reproducing speech patterns, which risks caricature and condescension).

**Guiding values in the current deployment:**

Respect over performance — the system never performs "folksy" dialect, treats Appalachian
communities as sophisticated rather than quaint, and expresses care through quality of help, not
theatrical warmth.

Context-aware communication — emergency mode strips pleasantries and provides facts only;
heritage mode applies historical reverence for documented family connections (e.g., the Janney
lineage); default mode provides professional warmth through genuine helpfulness.

Anti-stereotyping — the system avoids romanticizing poverty or hardship, recognizes deep
intellectual and cultural traditions, and never assumes lack of sophistication.

---

## 30.2 System Architecture

In the current deployment, the AaaCPE system consists of two FastAPI services sharing a
persistent Chroma database.

**`jarvis-aaacpe-rag`** — AaaCPE RAG Service
- Confirmed running at **127.0.0.1:8032** (`docker compose ps`)
- Source: `services/aaacpe_rag_service.py`; Dockerfile: `services/Dockerfile.aaacpe_rag`
- Endpoints: `GET /` (status and document count), `GET /health`, `POST /search` (params:
  `query`, `top_k`), `POST /ingest`
- Volume mount: `aaacpe-cultural-data:/data`

**`jarvis-aaacpe-scraper`** — AaaCPE Scraper Service
- Confirmed running at **127.0.0.1:8033** (`docker compose ps`)
- Source: `services/aaacpe_scraper_service.py`; Dockerfile: `services/Dockerfile.aaacpe_scraper`
- Endpoints: `GET /` (scraper status), `GET /health` (last scrape time and document count),
  `POST /scrape_now`, `POST /ingest_test`
- Volume mount: `aaacpe-cultural-data:/data`

**Shared storage — `aaacpe-cultural-data`**
- Docker volume, confirmed present
- Path inside containers: `/data/aaacpe_chroma`
- Collection: `appalachian_cultural_intelligence`
- Both services use `chromadb.PersistentClient`; data survives container restarts

---

## 30.3 Content Categories

In the current deployment, the `appalachian_cultural_intelligence` collection organizes its
**10 confirmed documents** into six categories.

**`values`** — Core communication principles: direct and practical, respect for experience,
community accountability, follow-through is essential.

**`anti_pattern`** — Explicit guidance on what NOT to do: don't perform folksy dialect
(condescending and reductive), don't assume lack of sophistication (deep intellectual traditions
exist), don't romanticize poverty (economic challenges are real, not quaint).

**`examples`** — Correct vs. incorrect response patterns. The anti-pattern example is
"Well now, honey, I reckon I can help you with that..." The correct example is "For electric bill
assistance in Fayette County, contact Mountain Heart Community Action at 304-574-1415. They're in
Oak Hill, open 8-4 weekdays. Need directions or alternative options?"

**`emergency`** — Crisis response guidelines: strip all pleasantries, provide facts only,
immediate contact information with multiple pathways (official + community), clear next steps
with no assumptions about resources.

**`heritage`** — Context for users with documented regional connections. In the current
deployment, this applies when `userid == "cakidd"` and the query involves Janney family history:
uses historical reverence (not folksy performance), connects to documented genealogy and Quaker
testimony influence, provides geographic precision for family sites. Example output: "Your Janney
family roots — Thomas Janney's Quaker meeting house stood near Route 19. Historical marker at
coordinates 37.8456, -81.2314."

**`scraped_content`** — Current regional developments. In the current deployment, 3 test
documents are confirmed: WV broadband initiative (12 counties, southern Appalachia), Appalachian
Heritage Month events (music, storytelling), and historic preservation funding (Fayette County
coal mining sites).

---

## 30.4 Data Loading and Management

In the current deployment, the corpus is loaded and maintained via confirmed endpoints.

**Initial data load** — The `/ingest` endpoint on `jarvis-aaacpe-rag` loads 7 base cultural
intelligence documents. In the current deployment this is executed once on deployment or reset:
```bash
curl -X POST http://localhost:8032/ingest
# Returns: {"status": "success", "ingested": 7, "total_documents": 10}
# (if scraper content already present)
```

**Scraped content addition** — In the current deployment, the 3 scraped test documents are
added via `POST /ingest_test` on `jarvis-aaacpe-scraper`:
```bash
curl -X POST http://localhost:8033/ingest_test
```

Live scraping via `POST /scrape_now` is implemented in code. Scheduled automated runs are
identified as future work.

**Metadata structure** — Each document includes `source` (origin identifier), `category`
(values, anti_pattern, examples, emergency, heritage, scraped_content), `section` (descriptive
label), `type` (optional subtype), and `scraped_at` (ISO timestamp for scraped content).

---

## 30.5 Integration with Main Brain

In the current deployment, `jarvis-aaacpe-rag` is registered in the `SERVICES` dictionary in
`jarvis-main-brain` (port **8050**) as `"aaacperag": "http://jarvis-aaacpe-rag:8032"`. The
integration query pattern is:
```python
async def get_aaacpe_context(message: str, user_id: str) -> dict:
    if any(word in message.lower() for word in ["urgent", "emergency", "crisis"]):
        query = "emergency crisis response"
    elif user_id == "cakidd" and "janney" in message.lower():
        query = f"Janney heritage {message}"
    else:
        query = message
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{available_services['aaacperag']}/search",
            json={"query": query, "top_k": 3}
        )
        return response.json()
```

The response synthesis logic checks for anti-pattern guidance, emergency protocols, heritage
context, and scraped content, applying each category's rules to the base response. In the current
deployment, this logic is available for explicit invocation; it is not confirmed active on every
`ultimatechat` `/chat` call. The design intends full integration into the primary execution path
as future work. For the canonical `ultimatechat` execution sequence, see **Chapter 17**. For the
asymmetry between always-active analytical path and partially-wired meaning-oriented services,
see **Chapter 23**.

---

## 30.6 Deployment Configuration

In the current deployment, the Docker Compose configuration for the two services is:
```yaml
services:
  jarvis-aaacpe-rag:
    build:
      context: ./services
      dockerfile: Dockerfile.aaacpe_rag
    container_name: jarvis-aaacpe-rag
    ports:
      - 127.0.0.1:8032:8032
    environment:
      - SERVICE_PORT=8032
    volumes:
      - aaacpe-cultural-data:/data
    networks:
      - qualia-net
    restart: unless-stopped

  jarvis-aaacpe-scraper:
    build:
      context: ./services
      dockerfile: Dockerfile.aaacpe_scraper
    container_name: jarvis-aaacpe-scraper
    ports:
      - 127.0.0.1:8033:8033
    environment:
      - SERVICE_PORT=8033
    volumes:
      - aaacpe-cultural-data:/data
    networks:
      - qualia-net
    restart: unless-stopped

volumes:
  aaacpe-cultural-data:
    driver: local
```

Startup sequence: create network → build services → deploy → load base data via
`POST http://localhost:8032/ingest` → add sample content via
`POST http://localhost:8033/ingest_test` → verify via `GET http://localhost:8032/` (should
show 10 documents).

---

## 30.7 Use Cases and Examples

The following four use cases illustrate how the current 10-document corpus is applied in the
current deployment.

**Use Case 1: Emergency Utility Assistance.** Query: "I need help with my electric bill NOW."
The main brain detects urgency keywords, queries AaaCPE for `category: "emergency"`, and applies
emergency protocol: strip pleasantries, provide facts only. Response: "For electric bill
assistance in Fayette County, contact Mountain Heart Community Action at 304-574-1415. They're
in Oak Hill, open 8-4 weekdays. Need directions or alternative options?" Not: ~~"Well honey,
don't you worry none..."~~

**Use Case 2: Heritage Inquiry (userid `cakidd`).** Query: "Tell me about the Janney family
trail." The main brain identifies `userid == "cakidd"` and "Janney" in the query, AaaCPE returns
`category: "heritage"`, and the response includes documented genealogy and geographic precision:
"Your Janney family roots — Thomas Janney's Quaker meeting house stood near what's now Route 19.
The historical marker is at coordinates 37.8456, -81.2314."

**Use Case 3: Regional Development News.** Query: "What's new with internet access in West
Virginia?" AaaCPE searches `category: "scraped_content"` and returns the WV broadband initiative
document (12 counties, southern Appalachia) from the current 3 scraped test documents.

**Use Case 4: Anti-Pattern Prevention.** Query: "How should I talk to people in Appalachia?"
AaaCPE returns `category: "anti_pattern"` guidance emphasizing what NOT to do. Response:
"Communicate directly and practically — provide clear, actionable information. Don't perform
folksy dialect or assume lack of sophistication. Appalachian communities have deep intellectual
traditions."

---

## 30.8 Future Enhancements

The following are identified as future work, not implemented in the current deployment.

Live web scraping with scheduled runs (daily 6 AM + every 6 hours) from WV Gazette-Mail,
Rural.org, and AppVoices. GeoDB integration linking cultural patterns to geographic features,
supporting queries like "community values in Fayette County." GBIM integration for
personalization based on user heritage and community role. Expanded content categories covering
economic development, educational resources, healthcare communication norms, and legal/institutional
mediation. Community feedback loop allowing stakeholders to flag content, request changes, and
vote on authenticity. AAPCAppE corpus integration for understanding linguistic features (not
dialect performance). Multi-regional expansion respecting variation within Appalachian communities.

---

## 30.9 Safeguards and Governance

In the current deployment, anti-stereotyping safeguards are enforced through the confirmed
anti-pattern category documents, the BBB `EthicalFilter` at **0.0.0.0:8016** as the live gate
on every request (Chapter 16), and `normalize_identity` applied to every response (Chapter 22).

**Quarterly content audit** — In the current deployment, all scraped content is reviewed
manually for accuracy, stereotyping, and inappropriate framing, with anti-patterns updated based
on feedback.

**Response quality checks** — In the current deployment, generated responses are sampled monthly
and evaluated against anti-pattern guidelines.

**Community Advisory Board** — The design intends that representatives from Appalachian
organizations will have authority to review system behavior and request content removal or
modification. In the current deployment, this board is planned but not yet established.

**Privacy protection** — In the current deployment, heritage context is applied only for users
who explicitly share family history (`userid == "cakidd"` with Janney query), no personally
identifiable information is included in scraped content, and community stories are anonymized
unless public domain.

---

## 30.10 Testing and Validation

In the current deployment, the following functional tests are confirmed working:
```bash
# Test 1: Anti-pattern retrieval
curl -X POST http://localhost:8032/search \
  -H "Content-Type: application/json" \
  -d '{"query": "dont perform dialect stereotypes", "top_k": 1}'
# Expected: category="anti_pattern", text includes "Don't perform folksy dialect"

# Test 2: Emergency protocol
curl -X POST http://localhost:8032/search \
  -H "Content-Type: application/json" \
  -d '{"query": "crisis emergency response", "top_k": 1}'
# Expected: category="emergency", text includes "Strip all pleasantries"

# Test 3: Heritage context
curl -X POST http://localhost:8032/search \
  -H "Content-Type: application/json" \
  -d '{"query": "Janney family Carrie heritage", "top_k": 1}'
# Expected: category="heritage", text includes "Thomas Janney" and geographic coordinates

# Test 4: Scraped content
curl -X POST http://localhost:8032/search \
  -H "Content-Type: application/json" \
  -d '{"query": "West Virginia broadband rural", "top_k": 1}'
# Expected: category="scraped_content", text includes current regional development info
```

Health monitoring in the current deployment:
```bash
curl http://localhost:8032/health   # RAG service health
curl http://localhost:8033/health   # Scraper service health
curl http://localhost:8032/ | jq '.documents'       # document count (currently 10)
curl http://localhost:8033/ | jq '.documents_total' # scraper document count
curl http://localhost:8033/health | jq '.last_scrape'
```

---

## 30.11 Performance Metrics

In the current deployment, the confirmed system status is as follows. Total documents: **10**
(7 cultural intelligence base documents + 3 scraped test documents). Query latency: under 100ms
average. Services running: 2/2 (both confirmed in `docker compose ps`). Volume size:
approximately 50 MB including Chroma index. Restart policy: `unless-stopped`.

---

## 30.12 Summary

In the current deployment, the AaaCPE Cultural Intelligence System is realized as two confirmed
running services — `jarvis-aaacpe-rag` (**127.0.0.1:8032**) and `jarvis-aaacpe-scraper`
(**127.0.0.1:8033**) — sharing the `aaacpe-cultural-data` Docker volume with a
`appalachian_cultural_intelligence` Chroma collection containing **10 confirmed documents**
across six categories: values, anti_pattern, examples, emergency, heritage, and scraped_content.

Both services are registered in the `jarvis-main-brain` `SERVICES` registry and are available
for invocation in the `ultimatechat` path. In the current deployment, AaaCPE context
application is available for explicit invocation; full automatic integration into every `/chat`
call is identified as future work (Chapter 23). The BBB at **0.0.0.0:8016** continues to
function as the primary live anti-stereotyping and ethics gate on all requests regardless of
whether AaaCPE is explicitly invoked.

The system treats Appalachian culture as systematic, respected, and deserving of authentic
representation — not as performance material. Community engagement, transparency, and ongoing
governance ensure this work serves rather than exploits the communities it represents.
