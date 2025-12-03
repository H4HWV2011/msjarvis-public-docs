#!/usr/bin/env python3
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
MANIFEST = ROOT / "thesis_manifest.txt"
OUT = ROOT / "thesis.md"

SUPER_CHAPTERS = [
    ("1. Foundations, Researcher Position, and Aims", [
        "00-thesis-overview.md",
        "00-overview.md",
        "01-researcher-position.md",
    ]),
    ("2. Theoretical and Conceptual Frameworks", [
        "01-quantarithmia.md",
        "02-ms-jarvis-gbim.md",
        "03-mountainshares-dao.md",
        "04-hilbert-space-state.md",
        "07-quantum-inspired-entanglement.md",
        "08-darwin-godel-machines.md",
        "09-woah-weighted-optimization-hierarchy.md",
        "17-limits-and-evaluation-of-metaphor.md",
        "33-spiritual-root-and-mother-carrie.md",
    ]),
    ("3. System Architecture and Implementation Methods", [
        "section_part_ii_system_architecture_llm_fabric.md",
        "05-chromadb-semantic-memory.md",
        "06-geodb-spatial-body.md",
        "06-rag-pipeline-and-routers.md",
        "10-llm-fabric-of-ms-jarvis.md",
        "18-container-architecture-and-routing.md",
        "20-background-store-and-patterns.md",
        "25-temporal-toroidal-semaphore-structure.md",
        "26-web-research-and-autonomy.md",
        "27-heartbeat-and-live-cycles.md",
        "30-mountainshares-and-infrastructure.md",
        "31-fractal-optimization-and-dgms.md",
        "32-llm-ensemble-and-judges.md",
    ]),
    ("4. Neurobiological Metaphors and Cognitive Architecture", [
        "section_part_iii_neurobiology.md",
        "11-neurobiological-architecture.md",
        "12-qualia-engine-and-introspective-state.md",
        "13-hippocampus-and-memory-consolidation.md",
        "14-pituitary-and-global-modes.md",
        "15-blood-brain-barrier-and-safeguards.md",
        "16-executive-coordination-overview.md",
    ]),
    ("5. Governance, Ethics, Identity, and Safeguards", [
        "section_part_v_live_feeds.md",
        "28-psychological-safeguards-and-pia.md",
        "29-aapcappE-scraper-and-corpus.md",
        "34-swarm-functions-and-eternal-watchdogs.md",
        "35-identity-and-registration.md",
        "36-constitutional-principles-service.md",
        "37-external-communication-and-authority.md",
        "section_part_vi_spiritual_identity_governance.md",
    ]),
    ("6. Consciousness, Evaluation, and Synthesis", [
        "section_part_iv_consciousness.md",
        "19-first-stage-evaluation.md",
        "21-identity-focused-retention.md",
        "22-dual-tracks-meaning-and-analysis.md",
        "23-feedback-into-broader-layers.md",
        "24-consciousness-coordinator-and-services.md",
        "38-operational-evaluation.md",
    ]),
]

def build():
    manifest_files = [
        l.strip()
        for l in MANIFEST.read_text(encoding="utf-8").splitlines()
        if l.strip()
    ]
    mapped = {f for _, files in SUPER_CHAPTERS for f in files}
    missing = set(manifest_files) - mapped
    if missing:
        raise SystemExit(f"Files in manifest not mapped to super-chapters: {missing}")

    lines = []
    for i, (title, files) in enumerate(SUPER_CHAPTERS, start=1):
        lines.append(f"# {title}\n")
        for j, fname in enumerate(files, start=1):
            stem = fname.replace(".md", "")
            pretty = stem.replace("_", " ").replace("-", " ").title()
            lines.append(f"## {i}.{j} {pretty}\n")
            path = ROOT / fname
            text = path.read_text(encoding="utf-8")
            lines.append(text.rstrip() + "\n\n")

    OUT.write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    build()
