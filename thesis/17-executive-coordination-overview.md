# 17. Executive Coordination Overview

This chapter outlines the high-level design of the control layer that decides which subsystems to invoke, in what order, and under which constraints. It serves as a conceptual bridge between the neuro-inspired layers described so far and the more concrete container and service designs that follow in later parts of the work. The focus here is on responsibilities and information flows rather than on specific deployment details.

## 17.1 Role in the System

The executive layer has three main jobs:

- Interpretation:
  - Understand the type of task or question being posed and identify relevant context such as roles, locations, and domains.
- Planning:
  - Decide which retrieval, analysis, and evaluation components to call for the task at hand.
- Integration:
  - Combine the outputs of those components into a single, coherent result, while enforcing applicable constraints.

In earlier chapters these ideas were introduced using brain-related metaphors. Here they are treated simply as design responsibilities that any coordinating mechanism must fulfill.

## 17.2 Inputs and Signals

To make decisions, the coordination layer draws on several kinds of information:

- Current request:
  - The incoming text or structured query, including any explicit tags or parameters.
- Introspective state:
  - Recent records describing what the system has been doing, including past decisions, evaluations, and mode settings.
- Consolidated memory:
  - Longer-term entries that record important precedents, patterns, and corrections.
- Global settings:
  - Active safety levels, role profiles, resource limits, and logging preferences.
- Service health:
  - Indicators of which subsystems are currently available and how they are performing.

These inputs give the coordinator a view of both the immediate task and the broader environment in which it is operating.

## 17.3 High-Level Decision Flow

At a high level, handling a request involves the following steps:

1. Characterization:
   - Classify the request by domain (for example, spatial analysis, governance support, or research) and by intended audience.
2. Mode application:
   - Apply global settings to determine which capabilities are allowed and how aggressively they can be used.
3. Route planning:
   - Select retrieval, analysis, and evaluation steps from the available components, such as vector search, graph queries, geospatial filters, and optimization routines.
4. Execution:
   - Call the selected components in an appropriate sequence, passing along intermediate results as needed.
5. Assembly and checks:
   - Combine the results into a final output, apply any last checks or constraints, and record the outcome in the introspective layer.

This structure is flexible enough to handle both simple and complex tasks while keeping the process inspectable.

## 17.4 Interaction with Other Layers

The executive layer sits at the point where several subsystems meet:

- Memory and spatial structures:
  - It decides when and how to query semantic collections, belief graphs, and geospatial features.
- Introspection and consolidation:
  - It both reads from and writes to introspective and consolidated records, using them as context and as a place to record new events.
- Global control:
  - It respects system-wide settings when choosing which operations to allow or prioritize.

Because of this position, changes in any of the underlying layers can affect how coordination is carried out, and observations gathered by the coordinator can motivate adjustments to those layers.

## 17.5 Relation to Container and Service Design

Subsequent parts of the work will describe concrete implementations that realize this coordination layer using specific services and deployment patterns. Those chapters will introduce:

- Distinct processing containers for different classes of tasks.
- A central controller that dispatches work to those containers.
- Detailed routing and error-handling strategies.

The conceptual structure described here provides the blueprint for those later designs, making it easier to see how individual components contribute to the overall behavior.

## 17.6 Summary

This chapter has outlined the responsibilities, inputs, and high-level flow of the system’s central coordination layer. It connects the earlier discussions of introspection, consolidation, and global control to the concrete mechanisms that will be developed in later parts, where the emphasis shifts from metaphor and intent to specific implementation patterns.


---

### Chapter 17: Executive Coordination Overview - UPDATE

**File**: `thesis/17-executive-coordination-overview.md`

**Add operational coordination pattern section**:

```markdown
## Operational Coordination Pattern (December 11, 2025)

### ✅ VALIDATED: Main-Brain Orchestration

main_brain successfully coordinates 8/23 operational services using validated pattern.

### Detailed Sequence Diagram
Client /chat Request
↓ [0ms]
main_brain receives request
↓ [10ms]
Health check sweep START
- PING: jarvis-main-brain ✅
- PING: jarvis-blood-brain-barrier ✅
- PING: jarvis-llm-bridge ✅
- PING: jarvis-web-research ✅
- PING: jarvis-qualia-engine ❌ (timeout)
- PING: jarvis-swarm-intelligence ❌ (timeout)
- ... (15 more failures)
↓ [2-5s total for health sweep]
Service selection logic
- use_all_services flag: true
- query_complexity: high (AGI reasoning)
- selected: [BBB, web_research, llm_bridge]
↓ [5ms]
Query BBB (query_service call)
- Input: raw user query
- Output: filtered_content + approval status
↓ [~1s]
Query web_research (query_service call)
- Input: filtered_content
- Output: enhanced_context + sources
↓ [~60s estimated]
Query llm_bridge (query_service call)
- Input: filtered_content + enhanced_context
### Performance Profile

| Phase | Latency | Bottleneck |
|-------|---------|-----------|
| Health check sweep | 2-5s | Fan-out PING to 23 services |
| Service selection | <10ms | Logic only |
| BBB processing | ~1s | Content filtering |
| web_research processing | ~60s | Context lookup + retrieval |
| llm_bridge processing | ~120s | 22-agent synthesis |
| Response aggregation | ~50ms | JSON formatting |
| RAG storage queue | ~10ms | Async enqueue |
| **Total ULTIMATE request** | **~195-353s** | **llm_bridge (22-agent synthesis)** |

### Critical Performance Issue: Health Check Amplification

**Discovered during testing**: Back-to-back heavy requests cause service restart

**Root cause**: Health check sweep happens EVERY request
- 23 PING operations × 195-353s request time = system under constant load
- Uvicorn memory/resource exhaustion after 2-3 sequential AGI requests
- Service restarts, losing context

**Impact**: Cannot sustain production workload with continuous health checks

### Proposed Optimization: TTL Cache

**Add health check TTL cache** (5-10 seconds):

```python
# In main_brain
HEALTH_CHECK_CACHE_TTL_SECONDS = 5
health_status_cache = {}  # {service_name: (status, timestamp)}

def get_service_health(service_name: str):
    now = time.time()
    if service_name in health_status_cache:
        status, timestamp = health_status_cache[service_name]
        if now - timestamp < HEALTH_CHECK_CACHE_TTL_SECONDS:
            return status  # Return cached
    
    # Fresh health check
    status = ping_service(service_name)
    health_status_cache[service_name] = (status, now)
    return status
Expected improvement:

    Before: 2-5s health check per request

    After: 2-5s once, then cached for 5s

    Net: 95% reduction in health check overhead for sustained workload

Implementation Status Badge

✅ OPERATIONAL (coordination successful) | 🔄 PARTIAL (performance issue identified)
Critical Recommendations

    URGENT: Implement health check TTL cache to prevent restart behavior

    Add coordination metrics (Prometheus):

        Health check latency (distribution)

        Service selection frequency

        Query_service call count per request

        RAG storage queue depth

    Add request-level tracing (OpenTelemetry):

        Trace ID propagation through service chain

        Latency breakdown by phase

        Error tracking per service

    Monitor service resource usage:

        Implement circuit breaker for failing services

        Auto-recovery logic when service restarts

        Graceful degradation when services unavailable

- Output: synthesized response
↓ [~120s estimated]
Response aggregation
- Combine: BBB approval + web_research sources + llm_bridge response
- Format: JSON response object
↓ [50ms]
RAG storage queuing
- Queue: {"response": "...", "timestamp": "..."}
- Target: ChromaDB (instance unknown)
- Async operation (non-blocking)
↓ [10ms]
Return to client
↓
Client receives response



