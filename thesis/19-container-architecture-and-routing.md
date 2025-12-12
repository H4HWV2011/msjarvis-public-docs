### Container Topology (December 11, 2025)

#### ✅ VALIDATED: Port Audit Complete

Complete inventory of 19 Docker containers and port mappings.

#### Core Orchestration Layer

| Container         | Image                          | Port Mapping | Status        | Role                                                                 |
|-------------------|--------------------------------|--------------|---------------|----------------------------------------------------------------------|
| jarvis-main-brain | msjarvis-main-brain:latest     | 8051→8050    | ✅ Operational | External API entry point; health check sweep; service orchestration |

#### Coordination Services (ULTIMATE Path)

| Container              | Image                             | Port Mapping | Status        | Role                                               |
|------------------------|-----------------------------------|--------------|---------------|----------------------------------------------------|
| jarvis-blood-brain-barrier | msjarvis-bbb:latest          | 8016→8016    | ✅ Operational | Content filter; context cleaning; safety enforcement |
| jarvis-llm-bridge      | msjarvis-llm-bridge:latest       | 18006→8006   | ✅ Operational | 22-agent ensemble coordination; response synthesis |
| jarvis-web-research    | msjarvis-web-research:latest     | 18009→8009   | ✅ Operational | Context enhancement; external knowledge retrieval  |

#### Consciousness & Coordination Services (Not Invoked)

| Container                  | Image                                  | Port Mapping | Status        | Role                               |
|----------------------------|----------------------------------------|--------------|---------------|------------------------------------|
| jarvis-qualia-engine       | msjarvis-qualia-engine:latest         | 18117→8017   | 🔄 Not invoked | Introspective state; qualia layer  |
| jarvis-swarm-intelligence  | msjarvis-swarm:latest                 | 18221→8021   | 🔄 Not invoked | Swarm coordination; multi-agent    |
| jarvis-consciousness-bridge| msjarvis-consciousness-bridge:latest  | 18220→8020   | 🔄 Not invoked | Inter-service consciousness sync   |
| jarvis-unified-gateway     | msjarvis-unified-gateway:latest       | 18001→8001   | 🔄 Not invoked | External communication authority   |

#### Memory & Learning Services

| Container               | Image                               | Port Mapping | Status        | Role                             |
|-------------------------|-------------------------------------|--------------|---------------|----------------------------------|
| jarvis-autonomous-learner | msjarvis-autonomous-learner:latest | 18053→8053  | 🔄 Unknown     | Autonomous learning; self-improve |
| jarvis-neurobiological-master | msjarvis-neuro-master:latest  | 18118→8018  | 🔄 Unknown     | Neurobiological coordination     |
| jarvis-i-containers     | msjarvis-i-containers:latest        | 18115→8015   | 🔄 Unknown     | Container orchestration          |
| jarvis-fifth-dgm        | msjarvis-fifth-dgm:latest           | 14002→4002   | 🔄 Unknown     | Darwin–Gödel machine; optimization |

#### Data Persistence & Semantics

| Container                 | Image                   | Port Mapping | Status     | Role                               |
|---------------------------|-------------------------|--------------|------------|------------------------------------|
| jarvis-chroma             | msjarvis-chroma:0.4.24 | 8000→8000    | ✅ Running | Primary semantic memory (ChromaDB) |
| services-chroma-1         | chromadb/chroma:latest | 8010→8010    | ✅ Running | Services-stack Chroma instance     |
| msjarvis-rebuild-chroma-1 | chromadb/chroma:latest | 8002→8000    | ✅ Running | Rebuild / development instance     |

#### External Access Points

Only two ports are exposed to the host (localhost):

- **8051**: External API endpoint (main_brain).  
- **11434**: Ollama LLM backend (local model access).

All other services communicate internally via Docker’s bridge network and DNS, using container names for service discovery.

#### Databases & Infrastructure

| Container          | Image                  | Port Mapping | Status     | Role                                              |
|--------------------|------------------------|--------------|------------|---------------------------------------------------|
| services-neo4j-1   | neo4j:5.13-community   | 7474, 7687   | ✅ Running | Graph DB; GBIM spatial and identity graphs       |
| services-mysql-1   | mysql:8.2              | 3307→3306    | ✅ Running | Relational data; users; audit logs               |
| services-ipfs-1    | ipfs/kubo:latest       | 5001         | ✅ Running | Distributed storage; content-addressed artifacts |

#### LLM Backend

| Container      | Image                  | Port Mapping  | Status     | Role                          |
|----------------|------------------------|---------------|------------|-------------------------------|
| jarvis-ollama  | ollama/ollama:latest   | 11434→11434   | ✅ Running | Local LLM execution backend   |

#### Narrative Summary

The validated container topology confirms a layered architecture: `jarvis-main-brain` on port 8051 acts as the external entry point, coordinates BBB, web_research, and llm_bridge, and relies on ChromaDB, Neo4j, MySQL, IPFS, and Ollama as backing services. This concrete layout provides the operational substrate for the routing concepts described earlier in this chapter, and it frames how future work on non-responsive services (qualia, swarm, consciousness-bridge, fifth-dgm, etc.) will extend the active container graph.
