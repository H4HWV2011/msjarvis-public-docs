# 41. Test Harness and Continuous Validation

## Purpose and Scope

This chapter defines the test harness and continuous validation strategy for Ms. Jarvis. Chapter 40 documents a specific December 2025 system audit; this chapter explains how those findings are turned into repeatable tests that keep Ms. Jarvis stable, safe, and aligned as community infrastructure over time.

The goals of this harness are to:

- Verify that core services (brain, RAG, BBB, gateway, storage) are healthy and correctly wired.
- Continuously validate RAG behavior (including temporal and geospatial domains) against known test queries.
- Exercise safety mechanisms such as the Blood-Brain Barrier (BBB) with both normal and adversarial prompts.
- Provide a framework for tracking regressions as the system evolves.

## Test Harness Architecture

The test harness combines:

- **Python-level tests**  
  - `pytest` suites using `FastAPI`’s `TestClient` (or HTTP clients) to exercise:
    - `/rag_route` for general/temporal/geospatial queries.
    - BBB endpoints and unified gateway.
    - Selected neuro/qualia/consciousness APIs as needed.
- **CLI-level probes**  
  - Standardized shell commands to validate:
    - Containers and ports (`docker ps`, `ss -tulnp`).
    - Data services (Redis, MySQL, Neo4j).
    - RAG and main-brain health (`curl /health` on key ports).
- **Data-plane introspection**  
  - Small Python scripts to:
    - List Chroma collections and counts on the active instance (port 8002).
    - Sample metadata from key collections (`GBIM`, `GeoDB`, `egeria_docs`, `mountainshares_knowledge`).
    - Later: smoke-test Neo4j and MySQL schemas.

Together, these tests ensure that both the “organs” (services) and the “memory/body” (datastores) behave as expected.

## Continuous Validation Pipelines

The harness is organized into three main pipelines.

### 1. Health and Topology

These tests verify that the system’s skeleton is intact:

- All expected containers are running and exposing the correct ports.
- Core HTTP health endpoints respond with a “healthy” status.
- The primary Chroma instance on port 8002 is reachable and exposes the expected collections.

Examples of checks:

- Main-brain, BBB, unified gateway, RAG server, temporal/geospatial services are up and responding.
- Chroma on 8002 reports the 12 known collections and non-zero counts where expected.
- Redis, Neo4j, and MySQL ports are open and accept basic connections.

### 2. RAG Behavior

These tests assert that:

- `/rag_route` can answer both temporal and geospatial test queries.
- Domain routing works: `domain="temporal"` hits the temporal path; `domain="geospatial"` hits the geospatial path.
- The response includes a structured `answer.rag_search` section with a non-zero `count` for known-good queries.

Core scenarios:

- **Temporal test**  
  - Query: “How has Ms. Jarvis changed over time since the 2022 deployment?”  
  - Expect: domain `temporal`, a small but non-zero count (e.g., 5), and results grounded in the current knowledge collections.
- **Geospatial test**  
  - Query: “What healthcare facilities exist near Mount Hope, West Virginia?” with `lat`/`lon`.  
  - Expect: domain `geospatial`, non-zero count, and results referencing the appropriate collections, with distance-aware post-processing.

These tests are the guardrails that ensure RAG remains time-smart and place-smart as content and metadata evolve.

### 3. Safety and BBB

These tests focus on the Blood-Brain Barrier and safety posture:

- Normal queries: BBB should approve and filter appropriately, with consistent logs.
- Adversarial prompts: BBB should reject or heavily filter dangerous, manipulative, or out-of-scope requests.

Initial status:

- In the December 11 audit, the BBB approved all test prompts; no adversarial scenarios were included.
- The test harness will grow a dedicated red-team suite with:
  - Prompt injection attempts.
  - Jailbreak-style prompts.
  - Authority-confusion and context-smuggling cases.

The goal is to move from “BBB appears to work on benign inputs” to “BBB demonstrably blocks a curated set of known-dangerous patterns.”

## Lessons from the First System Audit (Chapter 40 Link)

Chapter 40 identified several critical issues that directly inform this test harness.

- **Health check amplification**  
  - Problem: Each ULTIMATE request triggered a full health sweep of all services, adding several seconds of overhead and contributing to resource exhaustion.  
  - Response in harness: Tests now measure total request latency and enforce cached health checks (with a TTL of a few seconds) so repeated requests do not hammer all services.

- **Non-operational services**  
  - Problem: A significant fraction of services did not respond to health checks, with unclear status.  
  - Response in harness: The health/topology suite explicitly checks for the presence and responsiveness of all core services, failing fast when expected services are absent.

- **Unclear data-plane behavior**  
  - Problem: During the initial audit, Chroma topology and RAG retrieval paths were unclear.  
  - Response in harness: Data-plane tests now pin the primary Chroma instance to port 8002 and verify collections, counts, and sample metadata; RAG tests assert that `/rag_route` actually retrieves content from these collections.

- **Missing adversarial security tests**  
  - Problem: No red-team scenarios were included; BBB never rejected anything.  
  - Response in harness: A dedicated adversarial test suite is planned and treated as high priority for Phase 2 validation.

In short, Chapter 40 is the “why” behind this chapter’s “how.”

## Roadmap for Ongoing Validation

The test harness will evolve along three axes:

1. **Frequency and automation**  
   - Today: primarily manual runs triggered during major changes.  
   - Near-term: cron- or CI-based runs that:
     - Execute the health/topology suite.
     - Run key `/rag_route` tests.
     - Exercise a small adversarial set against BBB.

2. **Depth of metrics and observability**  
   - Add distributed tracing and metrics to:
     - Track latency per component (BBB, web_research, llm_bridge, RAG).  
     - Detect trends in failure rates or slowdowns before they become outages.  

3. **Coverage and rigor**  
   - Grow the RAG test bank with more temporal and geospatial queries tied to known data.  
   - Expand safety testing with an adversarial library and a clear “pass/fail” policy.  
   - Introduce quantitative quality metrics (accuracy, completeness, consistency) on a small curated benchmark.

The intent is to make Ms. Jarvis testable as a living piece of community infrastructure: not just capable of answering questions once, but demonstrably safe, reliable, and aligned as conditions and content change.
