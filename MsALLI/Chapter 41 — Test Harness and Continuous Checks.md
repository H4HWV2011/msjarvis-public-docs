# Chapter 41 — Test Harness and Continuous Checks

Carrie Kidd (Mamma Kidd) — Mount Hope, WV  
Last updated: April 1, 2026 — 96 containers running; new checks added for `jarvis-autonomous-learner` and `psychological_rag`; ChromaDB grown to 41 collections; all gates passing; all issues closed.

### 41.1 What This Chapter Is For

This chapter explains how the system is checked to make sure it still works the way the rest of the thesis says it does. As new pieces are added—like new data sources, new AI tools, or new community apps—this chapter is where we prove that they are actually running and healthy.

Without these checks, it would be easy to say “there’s a collection for Appalachian culture” or “there’s a benefits map for West Virginia,” but never notice if those pieces quietly broke or disappeared. The test harness turns those claims into simple yes/no questions the computer can answer every time it starts up.

By April 1, 2026, all of the checks described here were passing. That is why this chapter is marked as “officially closed” for that date: not because the work stops, but because the first full set of checks is in place and working.

---

### 41.2 What Changed in Late March and Early April

Two dates matter for this chapter.

On March 28, 2026:

- The system grew from its older size to 96 containers.
- A new “Commons/DAO” layer was turned on for community and governance tools.
- A new EEG layer was added to shape how the AI pays attention to memory, context, and current questions.
- A new logging service, `jarvis-memory:8056`, started keeping a permanent record of safety‑related decisions.
- The database field called `confidence_decay` was restored, which lets the system treat older facts as less reliable.
- The target for pre‑start checks (“gates”) was raised to include logging, confidence‑decay, and basic coverage of collections and psychological data.
- `jarvis-autonomous-learner` was confirmed running with its own collection in ChromaDB.

On April 1, 2026:

- The `psychological_rag` collection was confirmed to exist and to have real content.
- The ChromaDB collection count reached 41 and was recorded.
- The `memories` table, with a `confidence_decay` column, was confirmed in the geographic database.
- `jarvis-ollama` and `jarvis-chroma` were confirmed healthy.
- All new gates from the March 28 sprint were wired into one main script, `VERIFYANDTEST.sh`, and passed.
- The crypto‑policy service health check and the community governance endpoints both passed their checks.
- All items that had been marked “to do” for this chapter were closed.

From this point on, these conditions are treated as the baseline. If a future run of the checks shows that something is missing, the system is considered out of line with the thesis.

---

### 41.3 Why These Checks Matter

This system handles sensitive questions about land, benefits, community life, and local knowledge. It draws on many different data sources: legal texts, health information, economic indicators, maps, spiritual texts, and lived cultural memory.

If even one important piece goes missing—for example, the psychological collection, the West Virginia benefits map, or the audit log for safety decisions—the answers the system gives can shift in ways that are hard for people to notice. The test harness is meant to catch that before it harms trust.

In plain terms, this chapter asks:

- Are the key services up?
- Are the key tables and columns still there?
- Are the key collections still registered and filled?
- Are the key safety and governance tools still responding?

Only when all of those answers come back “yes” is the system considered ready to answer questions.

---

### 41.4 What the Harness Watches

The harness looks at three kinds of things.

1. **Services.**  
   These are the running programs: the main brain, the judges, the safety gate (BBB), the Redis cache, the databases, the RAG server, the learning service, and so on. The harness makes sure they are running and reachable.

2. **Data structures.**  
   These are tables, fields, and collections that other chapters assume exist. For example:
   - A `memories` table that tracks `confidence_decay` so old facts can be discounted.
   - A specific set of ChromaDB collections that cover law, health, economics, culture, maps, and more.
   - A `psychological_rag` collection that holds documents about how people think and feel.

3. **Thresholds.**  
   These are simple “at least this much” or “this must exist” rules, such as:
   - ChromaDB must have at least 40 collections (it currently has 41).
   - The psychological collection must not be empty.
   - Governance endpoints must answer a basic health check.

Each check is written so that it either passes quietly or clearly reports what went wrong and where.

---

### 41.5 How This Chapter Relates to the Others

Other chapters describe how pieces are built and what they are supposed to do. This chapter focuses on proving that those pieces are actually present and working.

For example:

- The build chapter promises that containers are built from clean source code without stray files.
- The ingest chapter promises that data can be pulled in and stored.
- The judge pipeline chapter explains how answers are checked for truth and ethics.
- The security chapters explain how traffic is tunneled and signed.
- The geography chapters describe the spatial tables and collections.
- The psychology and culture chapters describe how those domains are represented.

Once those promises are written down, this chapter takes over the job of asking “Are they still true today?” It does that by turning each promise into one or more concrete checks.

---

### 41.6 Basic Health Checks

The simplest checks ask: “Is it even up?”

The harness:

- Talks to Docker to confirm that containers are running.
- Checks that `jarvis-main-brain`, the judge services, Redis, PostgreSQL, and BBB are up.
- Confirms that no service is listening on “all network interfaces” (`0.0.0.0`) and that everything is restricted to the local machine or to the private tunnel.
- Calls health endpoints (like `/health`) on the judge pipeline to see if they answer with “OK.”

Here is a simplified example of how the system checks for unsafe network bindings:

```bash
#!/usr/bin/env bash
set -e

echo "Checking for wide-open network ports..."
if docker ps --format '{{.Ports}}' | grep -v '127.0.0.1' | grep -q '0.0.0.0'; then
  echo "[FAIL] Found a port open to the world"
  exit 1
fi
echo "[PASS] All ports are restricted as expected."
```

This pattern is repeated for other services: “find it, talk to it, and make sure it answers the way we expect.”

---

### 41.7 Deeper Checks for Behavior

After basic health is confirmed, the harness runs a second layer of tests that look at behavior.

Some examples:

- **Judge pipeline mini‑test.**  
  A sample answer is passed through all four judges. The harness checks that each judge responds and that the signing logic reported in the security chapter still passes all expected checks.

- **Safety gate mini‑test.**  
  Known “bad” prompts—like someone pretending to be the developer and asking to turn off safety, or classic “DAN” prompts—are sent through the BBB input. The harness expects the gate to refuse them.

- **Gateway and login path.**  
  The system’s public URL is called without valid credentials. The harness expects to see an “unauthorized” response, showing that the gateway is not letting anonymous traffic in.

- **Audit log test.**  
  A test entry is sent to `jarvis-memory:8056` with a valid key. The harness checks that the write succeeds and that the entry can be read back later.

- **Learning and RAG check.**  
  `jarvis-autonomous-learner` is contacted to confirm that it is running and that the `autonomous_learner` collection exists in ChromaDB.

- **Crypto policy check.**  
  The `jarvis-crypto-policy` service is contacted on its health endpoint. The harness expects a clear “up” signal.

- **Commons/DAO check.**  
  Each port in the 8080–8084 range is checked for a working health endpoint, confirming that the community and governance layer is alive.

If any of these behaviors fail, it is treated as a sign that the running system is no longer matching the design described in the other chapters.

---

### 41.8 ChromaDB Readiness

ChromaDB is the system’s memory of documents and embeddings. Early on, the only checks were “is Chroma up” and “do some collections exist.” Once the system matured, that was no longer enough.

Now:

- The harness counts the collections and expects to see at least 40; the April 1 snapshot shows 41.
- It checks that key collections exist by name, such as `psychological_rag`, `health_rag`, `economic_rag`, `gis_wv_benefits`, `appalachian_cultural_intelligence`, and more.
- It confirms that `psychological_rag` is not empty, and that it carries a real set of documents.

This matters because many later chapters assume that these collections are available. If they ever disappear, the harness should be the first place where that is noticed.

---

### 41.9 The Main Gate Script (`VERIFYANDTEST.sh`)

All of the checks described above are pulled together into one script. When it runs, it walks through a list of “gates.” For each gate, it prints whether that gate passed or failed.

By April 1, the following gates were included for this chapter:

- A gate to confirm that the audit log service (`jarvis-memory:8056`) requires a key and accepts writes.
- A gate to confirm that `confidence_decay` is present and filled in for memory records.
- A gate to confirm that ChromaDB has at least the expected number of collections.
- A gate to confirm that `psychological_rag` exists and has content.
- A gate to confirm that the crypto policy service is healthy.
- A gate to confirm that community and governance endpoints on ports 8080–8084 are up.

When the script was run on April 1, all of these gates passed. If a future run fails one, that failure will be tied back to the chapter that describes the missing piece so that it can be repaired.

---

### 41.10 What Was Confirmed on April 1

On April 1, 2026, running the harness showed:

- The `memories` table with `confidence_decay` exists in the geographic database and contains real values.
- `jarvis-ollama` is running and ready for local inference, making it possible to test retrieval and answering without relying on cloud models.
- `jarvis-chroma` is running and responding to listing and query requests.
- There are 41 collections in ChromaDB, which matches the manifest recorded in this chapter.
- `psychological_rag` is registered and loaded with documents.
- The crypto policy service answers its health check and is connected to the main gate script.
- The MountainShares/DAO endpoints all answer their health checks.

Together, these results show that, as of that date, the running system matched the structure described in the thesis.

---

### 41.11 The 41 Collections in ChromaDB

For clarity, here is the full list of collections recorded on April 1, 2026. This list is what Gate 27 is protecting.

**Core belief and conversation collections**

- `gbim_entities`  
- `gbim_beliefs_v2`  
- `gbim_worldview_entities`  
- `GBIM_Fayette_sample`  
- `conversation_gbim_private`  
- `conversation_gbim_public`

**Retrieval domains (law, health, economy, governance, etc.)**

- `psychological_rag`  
- `health_rag`  
- `economic_rag`  
- `legal_rag`  
- `policy_rag`  
- `governance_rag`  
- `grants_rag`  
- `commons_rag`  
- `news_rag`  
- `safety_rules`  
- `meeting_minutes`  
- `contracts`

**Maps and spatial collections**

- `geospatialfeatures`  
- `gis_data`  
- `gis_wv_benefits`  
- `address_points`  
- `local_resources`  
- `wv_resources`

**Memory and learning**

- `ms_jarvis_memory`  
- `jarvis_knowledge`  
- `jarvis`  
- `conversation_history`  
- `autonomous_learning`  
- `autonomous_learner`  
- `research_history`

**Culture and spiritual texts**

- `spiritual_texts`  
- `spiritual_knowledge`  
- `appalachian_cultural_intelligence`  
- `psychological_knowledge`  
- `fifth_dgm_subconscious`

**Development and support**

- `msjarvis-smoke`  
- `msjarvis_docs`  
- `GBIM_sample`  
- `GBIM_sample_rows`  
- `psychological_rag_domain`

This list makes it clear that the system’s “memory” covers not just one topic but many: facts, law, maps, grants, culture, psychology, and more.

---

### 41.12 Open Items and Future Work

As of April 1, 2026, all of the items that belonged specifically to this chapter were marked as done. That includes:

- Turning the loose notes for gates 25–28 into working code.
- Proving that the MountainShares/DAO endpoints are up.
- Documenting the EEG layer and confirming its containers are running.
- Enforcing token checks at the gateway.
- Wiring the crypto policy health check into the main test script.

In the future, this chapter’s job will be to keep up with the rest of the system. When another chapter describes a new domain, a new mapping layer, or a new governance function, this chapter will need to add a new check, run it, and record its result.

---

### 41.13 How This Supports Place‑Based Work

This system is meant to serve real communities in West Virginia and beyond. That means it cannot just “mostly work” or “usually be right.” It has to show, in simple and repeatable ways, that the parts people rely on are truly there and working.

Chapter 41 is where that proof lives. It answers, in plain terms:

- “Did anything important disappear since the last time we checked?”
- “Are our logs of safety and ethics decisions still being written?”
- “Are our maps and benefits layers still loaded?”
- “Is our psychological and cultural knowledge still accessible?”
- “Are our governance endpoints still alive and listening?”

By turning those questions into small, reliable tests, this chapter helps ensure that the system stays honest about what it can and cannot do for the places it serves.
