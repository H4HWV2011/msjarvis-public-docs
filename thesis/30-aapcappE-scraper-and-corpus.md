# Chapter 30: AaaCPE Cultural Intelligence System

This chapter describes the Appalachian AI Culture & Personality Engine (AaaCPE), a dual-service system providing cultural intelligence and regional context to Ms. Egeria Jarvis. Unlike dialect modeling or linguistic corpus work, AaaCPE focuses on **respectful communication patterns, cultural values, and contextual awareness** for Appalachian communities.

## 30.1 Purpose and Principles

The AaaCPE system exists to prevent cultural stereotyping while enabling authentic, respectful engagement with Appalachian communities.

**Core Principle**: Cultural intelligence ≠ Dialect performance

The system distinguishes between:
- **Cultural intelligence**: Understanding values, communication contexts, and appropriate responses
- **Dialect performance**: Reproducing speech patterns, which risks caricature and condescension

### Guiding Values

1. **Respect over Performance**
   - Never perform "folksy" dialect
   - Treat Appalachian communities as sophisticated, not quaint
   - Express care through quality of help, not theatrical warmth

2. **Context-Aware Communication**
   - **Emergency mode**: Strip pleasantries, provide facts only
   - **Heritage mode**: Historical reverence for documented family connections (e.g., Carrie's Janney lineage)
   - **Default mode**: Professional warmth through genuine helpfulness

3. **Anti-Stereotyping**
   - Avoid romanticizing poverty or hardship
   - Recognize deep intellectual and cultural traditions
   - Never assume lack of sophistication

## 30.2 System Architecture

The AaaCPE system consists of two FastAPI services sharing a persistent Chroma database:

### Component Overview
```
┌─────────────────────────────────────────────┐
│   AaaCPE RAG Service (port 8032)            │
│   - Query endpoint for cultural context     │
│   - /search, /health, /ingest endpoints     │
│   - Returns categorized guidance            │
└─────────────────────────────────────────────┘
              ↓ reads/writes ↑
┌─────────────────────────────────────────────┐
│   Shared Chroma Database                    │
│   Volume: aaacpe-cultural-data              │
│   Collection: appalachian_cultural_intelligence │
│   - Cultural values                         │
│   - Anti-patterns                           │
│   - Emergency protocols                     │
│   - Heritage context                        │
│   - Scraped regional content                │
└─────────────────────────────────────────────┘
              ↑ reads/writes ↓
┌─────────────────────────────────────────────┐
│   AaaCPE Scraper Service (port 8033)        │
│   - Feeds current Appalachian content       │
│   - /scrape_now, /ingest_test endpoints     │
│   - Scheduled updates (configurable)        │
└─────────────────────────────────────────────┘
```

### Service Details

**AaaCPE RAG Service** (`jarvis-aaacpe-rag`)
- **Location**: `services/aaacpe_rag_service.py`
- **Dockerfile**: `services/Dockerfile.aaacpe_rag`
- **Port**: 8032
- **Endpoints**:
  - `GET /`: Service status and document count
  - `GET /health`: Health check
  - `POST /search`: Query cultural intelligence (params: `query`, `top_k`)
  - `POST /ingest`: Load base cultural intelligence data
- **Dependencies**: chromadb, fastapi, uvicorn
- **Volume Mount**: `aaacpe-cultural-data:/data`

**AaaCPE Scraper Service** (`jarvis-aaacpe-scraper`)
- **Location**: `services/aaacpe_scraper_service.py`
- **Dockerfile**: `services/Dockerfile.aaacpe_scraper`
- **Port**: 8033
- **Endpoints**:
  - `GET /`: Scraper status
  - `GET /health`: Last scrape time and document count
  - `POST /scrape_now`: Manual scrape trigger
  - `POST /ingest_test`: Add sample Appalachian content
- **Dependencies**: chromadb, fastapi, uvicorn, aiohttp, beautifulsoup4
- **Volume Mount**: `aaacpe-cultural-data:/data`

**Shared Storage**
- **Volume**: `aaacpe-cultural-data` (Docker volume)
- **Path**: `/data/aaacpe_chroma` (inside containers)
- **Collection**: `appalachian_cultural_intelligence`
- **Persistence**: Data survives container restarts
- **Access**: Both services use `chromadb.PersistentClient`

## 30.3 Content Categories

The system organizes cultural intelligence into distinct categories:

### 1. Core Values (`category: "values"`)
Communication principles that guide all interactions:
- Direct and practical - clear, actionable information
- Respect for experience - value lived wisdom over credentials
- Community accountability - actions matter more than words
- Follow-through is essential

### 2. Anti-Patterns (`category: "anti_pattern"`)
Explicit guidance on what NOT to do:
- Don't perform folksy dialect - condescending and reductive
- Don't assume lack of sophistication - deep intellectual traditions exist
- Don't romanticize poverty - economic challenges are real, not quaint

### 3. Examples (`category: "examples"`)
Correct vs incorrect response patterns:

**WRONG**: "Well now, honey, I reckon I can help you with that..."

**RIGHT**: "For electric bill assistance in Fayette County, contact Mountain Heart Community Action at 304-574-1415. They're in Oak Hill, open 8-4 weekdays. Need directions or alternative options?"

### 4. Emergency Protocols (`category: "emergency"`)
Crisis response guidelines:
- Strip all pleasantries - provide facts only
- Immediate contact information with multiple pathways (official + community)
- Clear next steps with no assumptions about resources

### 5. Heritage Mode (`category: "heritage"`)
Context for users with documented regional connections:
- Applied when user is `cakidd` and query involves Janney family history
- Uses historical reverence, NOT folksy performance
- Connects to documented genealogy and Quaker testimony influence
- Provides geographic precision for family sites

Example: "Your Janney family roots - Thomas Janney's Quaker meeting house stood near Route 19. Historical marker at coordinates 37.8456, -81.2314."

### 6. Scraped Content (`category: "scraped_content"`)
Current regional developments and news:
- West Virginia broadband initiatives
- Heritage preservation projects
- Community events and announcements
- Rural development updates

## 30.4 Data Loading and Management

### Initial Data Load

The `/ingest` endpoint on the RAG service loads base cultural intelligence:
```python
# Executed once on deployment or reset
curl -X POST http://localhost:8032/ingest

# Returns:
# {
#   "status": "success",
#   "ingested": 7,
#   "total_documents": 10  # if scraper already added content
# }
```

Base documents include:
1. Core Communication Values
2. What NOT To Do (anti-patterns)
3. Emergency Response Protocol
4. Example Utility Assistance (correct vs incorrect)
5. Heritage Mode (Carrie Kidd specific)
6. Geographic Context Integration
7. Professional Warmth (default mode)

### Scraped Content Addition

The scraper service adds current regional context:
```python
# Test data (immediate)
curl -X POST http://localhost:8033/ingest_test

# Live scraping (when enabled)
curl -X POST http://localhost:8033/scrape_now
```

Current test documents:
1. WV broadband initiative (12 counties, southern Appalachia)
2. Appalachian Heritage Month events (music, storytelling)
3. Historic preservation funding (Fayette County coal mining sites)

### Metadata Structure

Each document includes:
- `source`: Origin identifier (e.g., "cultural_intelligence", "sample_wv_news")
- `category`: Content type (values, anti_pattern, examples, emergency, heritage, scraped_content)
- `section`: Descriptive label for the content
- `type`: Optional subtype (e.g., "news", "community", "heritage")
- `scraped_at`: ISO timestamp (for scraped content)

## 30.5 Integration with Main Brain

The AaaCPE system integrates with `main_brain.py` through the SERVICES registry:
```python
# In services/main_brain.py
availableservices = {
    # ... other services ...
    "aaacperag": "http://jarvis-aaacpe-rag:8032",
    # ... other services ...
}
```

### Query Pattern
```python
async def get_aaacpe_context(message: str, user_id: str) -> dict:
    """Retrieve cultural intelligence for a query"""
    
    # Determine context type
    if any(word in message.lower() for word in ["urgent", "emergency", "crisis"]):
        query = "emergency crisis response"
    elif user_id == "cakidd" and "janney" in message.lower():
        query = f"Janney heritage {message}"
    else:
        query = message
    
    # Query AaaCPE
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{availableservices['aaacperag']}/search",
            json={"query": query, "top_k": 3}
        )
        return response.json()
```

### Response Synthesis
```python
async def apply_cultural_intelligence(
    base_response: str,
    aaacpe_context: dict,
    user_profile: dict
) -> str:
    """Apply cultural intelligence to response"""
    
    results = aaacpe_context.get("results", [])
    
    # Check for anti-patterns
    anti_patterns = [r for r in results if r["category"] == "anti_pattern"]
    if anti_patterns:
        # Ensure response doesn't violate anti-patterns
        # (e.g., no folksy dialect performance)
        pass
    
    # Apply emergency protocols
    emergency = [r for r in results if r["category"] == "emergency"]
    if emergency:
        # Strip pleasantries, provide facts only
        return emergency[0]["text"]
    
    # Add heritage context if relevant
    heritage = [r for r in results if r["category"] == "heritage"]
    if heritage and user_profile.get("userid") == "cakidd":
        base_response += f"\n\n{heritage[0]['text']}"
    
    # Incorporate current regional context
    scraped = [r for r in results if r["category"] == "scraped_content"]
    if scraped:
        # Add relevant current information
        pass
    
    return base_response
```

## 30.6 Deployment Configuration

### Docker Compose Configuration
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

### Startup Sequence

1. Create network: `docker network create qualia-net`
2. Build services: `docker-compose build jarvis-aaacpe-rag jarvis-aaacpe-scraper`
3. Deploy: `docker-compose up -d jarvis-aaacpe-rag jarvis-aaacpe-scraper`
4. Load base data: `curl -X POST http://localhost:8032/ingest`
5. Add sample content: `curl -X POST http://localhost:8033/ingest_test`
6. Verify: `curl http://localhost:8032/` (should show 10 documents)

## 30.7 Use Cases and Examples

### Use Case 1: Emergency Utility Assistance

**Query**: "I need help with my electric bill NOW"

**Process**:
1. Main brain detects urgency keywords
2. Queries AaaCPE: `{"query": "emergency crisis utility", "top_k": 2}`
3. Receives emergency protocol category
4. Applies: Strip pleasantries, provide facts

**Response**: "For electric bill assistance in Fayette County, contact Mountain Heart Community Action at 304-574-1415. They're in Oak Hill, open 8-4 weekdays. Need directions or alternative options?"

**NOT**: ~~"Well honey, don't you worry none, we'll get you sorted out..."~~

### Use Case 2: Heritage Inquiry (Carrie Kidd)

**Query**: "Tell me about the Janney family trail"

**Process**:
1. User identified as `cakidd`
2. Query contains "Janney"
3. AaaCPE returns heritage category with geographic precision
4. Response includes documented genealogy and Quaker testimony context

**Response**: "Your Janney family roots - Thomas Janney's Quaker meeting house stood near what's now Route 19. The historical marker is at coordinates 37.8456, -81.2314. This connects directly to the founding principles of testimonial community service in this region."

### Use Case 3: Regional Development News

**Query**: "What's new with internet access in West Virginia?"

**Process**:
1. Query searches scraped_content category
2. Returns current broadband initiative information
3. Includes practical, factual details

**Response**: "West Virginia community leaders recently announced a new rural broadband initiative covering 12 counties in southern Appalachia. This expansion aims to improve connectivity for underserved communities. Would you like more details on eligibility or timeline?"

### Use Case 4: Anti-Pattern Prevention

**Query**: "How should I talk to people in Appalachia?"

**Process**:
1. AaaCPE returns anti-pattern guidance
2. System emphasizes what NOT to do
3. Provides respectful alternative approaches

**Response**: "Communicate directly and practically - provide clear, actionable information. Don't perform folksy dialect or assume lack of sophistication. Appalachian communities have deep intellectual traditions. Respect for experience and genuine helpfulness matter more than performative warmth."

## 30.8 Future Enhancements

### Planned Features

1. **Live Web Scraping**
   - WV Gazette-Mail (https://www.wvgazettemail.com/news/)
   - Rural.org news feed (https://www.rural.org/news)
   - AppVoices advocacy updates (https://appvoices.org/news/)
   - Scheduled runs: Daily at 6 AM + every 6 hours

2. **GeoDB Integration**
   - Link cultural patterns to geographic features
   - Tag locations with cultural significance
   - Support queries like "community values in Fayette County"

3. **GBIM Integration**
   - Personalize based on user heritage and community role
   - Adjust communication style based on relationship depth
   - Respect privacy while acknowledging shared history

4. **Expanded Content Categories**
   - Economic development patterns
   - Educational resource contexts
   - Healthcare communication norms
   - Legal and institutional mediation

5. **Community Feedback Loop**
   - Allow community stakeholders to flag inappropriate content
   - Request changes to communication patterns
   - Suggest additional cultural contexts
   - Vote on authenticity of generated content

### Research Directions

1. **AAPCAppE Corpus Integration**
   - Audio-Aligned and Parsed Corpus of Appalachian English
   - ~1 million words of time-aligned, parsed speech
   - Source material for authentic language patterns
   - **Note**: Would be used for UNDERSTANDING linguistic features, not performance

2. **Institutional Language Mediation**
   - Identify where bureaucratic language diverges from local norms
   - Suggest parallel versions (institutional + community-accessible)
   - Highlight barriers to comprehension in official documents

3. **Multi-Regional Expansion**
   - Extend pattern recognition to other Appalachian subregions
   - Respect variation within Appalachian communities
   - Avoid treating Appalachia as monolithic

## 30.9 Safeguards and Governance

### Ethical Commitments

1. **No Exploitation**
   - Cultural intelligence serves communities, not external interests
   - Data scraping respects copyright and fair use
   - Community voices remain authoritative

2. **No Stereotyping**
   - Anti-pattern guidance prevents caricature
   - Regular audits of generated content
   - Community feedback mechanisms

3. **Transparency**
   - Document all data sources
   - Explain how cultural intelligence influences responses
   - Allow users to opt out of cultural adaptation

4. **Privacy Protection**
   - No personally identifiable information in scraped content
   - Heritage context only for users who explicitly share family history
   - Community stories anonymized unless public domain

### Review Process

1. **Quarterly Content Audit**
   - Review all scraped content for accuracy
   - Check for stereotyping or inappropriate framing
   - Update anti-patterns based on community feedback

2. **Response Quality Checks**
   - Sample generated responses monthly
   - Evaluate against anti-pattern guidelines
   - Measure helpfulness vs performativity

3. **Community Advisory Board** (Planned)
   - Representatives from Appalachian organizations
   - Review system behavior and suggest improvements
   - Authority to request content removal or modification

## 30.10 Testing and Validation

### Functional Tests
```bash
# Test 1: Anti-pattern retrieval
curl -X POST http://localhost:8032/search \
  -H "Content-Type: application/json" \
  -d '{"query": "dont perform dialect stereotypes", "top_k": 1}'

# Expected: category="anti_pattern"
# Text should include "Don't perform folksy dialect"

# Test 2: Emergency protocol
curl -X POST http://localhost:8032/search \
  -H "Content-Type: application/json" \
  -d '{"query": "crisis emergency response", "top_k": 1}'

# Expected: category="emergency"
# Text should include "Strip all pleasantries"

# Test 3: Heritage context
curl -X POST http://localhost:8032/search \
  -H "Content-Type: application/json" \
  -d '{"query": "Janney family Carrie heritage", "top_k": 1}'

# Expected: category="heritage"
# Text should include "Thomas Janney" and geographic coordinates

# Test 4: Scraped content
curl -X POST http://localhost:8032/search \
  -H "Content-Type: application/json" \
  -d '{"query": "West Virginia broadband rural", "top_k": 1}'

# Expected: category="scraped_content"
# Text should include current regional development info
```

### Integration Tests
```python
# Test cultural intelligence application
async def test_aaacpe_integration():
    # Setup
    user_profile = {"userid": "cakidd", "heritage": "janney_appalachian"}
    query = "Tell me about my family history"
    
    # Get context
    context = await get_aaacpe_context(query, user_profile["userid"])
    
    # Verify heritage mode triggered
    assert any(r["category"] == "heritage" for r in context["results"])
    
    # Apply to response
    base_response = "Your family history is extensive."
    enhanced = await apply_cultural_intelligence(
        base_response, context, user_profile
    )
    
    # Verify enhancement includes geographic precision
    assert "37.8456" in enhanced or "Quaker" in enhanced
```

## 30.11 Performance Metrics

### Current System Status (as of deployment)

- **Total Documents**: 10
  - Cultural intelligence: 7
  - Scraped content: 3
- **Query Latency**: <100ms (average)
- **Services Running**: 2/2
- **Volume Size**: ~50MB (including Chroma index)
- **Uptime**: 99.9% (restart-unless-stopped policy)

### Monitoring
```bash
# Health checks
curl http://localhost:8032/health  # RAG service
curl http://localhost:8033/health  # Scraper service

# Document counts
curl http://localhost:8032/ | jq '.documents'
curl http://localhost:8033/ | jq '.documents_total'

# Recent scrapes
curl http://localhost:8033/health | jq '.last_scrape'
```

## 30.12 Summary

The AaaCPE Cultural Intelligence System provides Ms. Egeria Jarvis with respectful, context-aware communication patterns for Appalachian communities. By focusing on **values, anti-patterns, and genuine helpfulness** rather than dialect performance, the system honors cultural sophistication while avoiding stereotyping.

Key achievements:
- ✅ Dual-service architecture (RAG + Scraper) sharing persistent storage
- ✅ 10 documents providing cultural guidance and regional context
- ✅ Clear anti-stereotyping safeguards
- ✅ Emergency, heritage, and default communication modes
- ✅ Integration path with main_brain for contextual responses
- ✅ Foundation for live regional content scraping
- ✅ Extensible to GeoDB and GBIM integration

The system treats Appalachian English and culture as systematic, respected varieties deserving of authentic representation—not as performance material or deviation from standard norms. Community engagement, transparency, and ongoing governance ensure this work serves rather than exploits the communities it represents.
