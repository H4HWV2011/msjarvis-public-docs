# Public API Overview

This document summarizes the publicly documented endpoints exposed by the Ms. Jarvis system, grouped by function: gateway, consciousness, GIS, blockchain, background services, and autonomous learning. It is intended as a high-level map of capabilities; detailed schemas and examples are provided in the OpenAPI specification.

## Consciousness and Documentation

- `GET /consciousness/status`:
  - Returns high-level information about consciousness layers, active modes, and global constraints.
- `GET /consciousness/layers`:
  - Describes the configured consciousness layers and their roles.
- `GET /docs/architecture`:
  - Provides an overview of system architecture.
- `GET /docs/services-manifest`:
  - Lists services and their key endpoints.

## Authentication

- `POST /auth/token`:
  - Obtain a JWT token for API access (roles such as researcher, engineer, admin).
  - Request parameters include `username` and `password` in the query or body, depending on deployment.

## Infrastructure and Monitoring

- `GET /infrastructure/locks/active`:
  - Returns information about active locks in infrastructure management.
- `GET /infrastructure/nohup/processes`:
  - Lists long-running nohup processes managed by the system.
- `GET /infrastructure/status`:
  - Summarizes current infrastructure status and key metrics.

## Research and Knowledge Monitoring

- `GET /research/activity`:
  - Reports on recent research tasks and their outcomes.
- `GET /research/summary`:
  - Provides a higher-level summary of research trends over a window.
- `GET /knowledge/growth`:
  - Exposes coarse-grained indicators of knowledge growth in semantic memory.
- `GET /storage/complete`:
  - Returns results of comprehensive storage audits.
- `GET /data/inventory`:
  - Summarizes public data assets known to Ms. Jarvis.

## Autonomous learner APIs

### GET /learning/status

- Purpose:
  - Returns the current status of the optimized autonomous learner, including cycle counts, storage statistics, and the active topic.
- Response (JSON):
  - `active`: Boolean flag indicating whether the learning loop is running.
  - `total_cycles`: Integer count of completed learning cycles.
  - `items_stored`: Total number of unique items stored in semantic memory.
  - `items_deduplicated`: Total number of items skipped due to semantic similarity.
  - `deduplication_rate`: String expressing the proportion of skipped items versus total evaluated items.
  - `uptime_hours`: Floating-point number representing the learner’s uptime in hours.
  - `current_topic`: String describing the topic selected for the most recent cycle.
  - `optimizations`: Array of strings describing active features (for example, `"semantic_deduplication"`, `"summarization"`, `"periodic_cleanup"`, `"topic_planner"`).

### POST /learning/suggest

- Purpose:
  - Allows GBIMs and other system components to push short topic summaries into the autonomous learner’s suggestion pool.
- Request (JSON body):
  - `source_gbim`: String identifier for the source, such as `"user_gbim"` or `"mountainshares_gbim"`.
  - `topic_summary`: Short, human-readable phrase describing the suggested topic.
- Response (JSON):
  - `status`: Status string, typically `"queued"` if the suggestion was accepted for processing.
  - `topic`: Expanded topic label constructed by the learner from the source and summary.

These endpoints are intended for internal integrations and research workflows that need to monitor or guide autonomous learning cycles.

## GIS and GBIM

- `GET /gis/query`:
  - Query geospatial layers and GBIM-linked entities.
- `GET /gis/features/{id}`:
  - Retrieve detailed information for a specific feature, where permitted.
- `GET /storage/chromadb`:
  - Summarizes ChromaDB collections exposed through public interfaces.

## Blockchain and Cooperative Integration

- `GET /dgm`:
  - Returns Darwin–Gödel Machine integration status and configuration.
- `GET /analytics`:
  - Provides aggregate metrics and analytics relevant to governance and research.
- Additional cooperative- and DAO-related endpoints:
  - Documented in dedicated sections for MountainShares and related projects.

For the full machine-readable schema, see `api_specs/openapi.json`.
