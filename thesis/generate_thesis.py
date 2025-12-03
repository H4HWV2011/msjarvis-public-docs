from pathlib import Path

# Mapping of Part titles to the files that belong in each Part,
# in the order they should appear in the thesis.
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
        "08-quantum-inspired-entanglement.md",
        "09-darwin-godel-machines.md",
        "10-woah-weighted-optimization-hierarchy.md",
        "18-limits-and-evaluation-of-metaphor.md",
        "34-spiritual-root-and-mother-carrie.md",
    ]),
    ("3. System Architecture and Implementation Methods", [
        "section_part_ii_system_architecture_llm_fabric.md",
        "05-chromadb-semantic-memory.md",
        "06-geodb-spatial-body.md",
        "07-rag-pipeline-and-routers.md",
        "11-llm-fabric-of-ms-jarvis.md",
        "19-container-architecture-and-routing.md",
        "21-background-store-and-patterns.md",
        "26-temporal-toroidal-semaphore-structure.md",
        "27-web-research-and-autonomy.md",
        "28-heartbeat-and-live-cycles.md",
        "31-mountainshares-and-infrastructure.md",
        "32-fractal-optimization-and-dgms.md",
        "33-llm-ensemble-and-judges.md",
    ]),
    ("4. Neurobiological Metaphors and Cognitive Architecture", [
        "section_part_iii_neurobiology.md",
        "12-neurobiological-architecture.md",
        "13-qualia-engine-and-introspective-state.md",
        "14-hippocampus-and-memory-consolidation.md",
        "15-pituitary-and-global-modes.md",
        "16-blood-brain-barrier-and-safeguards.md",
        "17-executive-coordination-overview.md",
    ]),
    ("5. Governance, Ethics, Identity, and Safeguards", [
        "section_part_v_live_feeds.md",
        "28-heartbeat-and-live-cycles.md",
        "29-psychological-safeguards-and-pia.md",
        "30-aapcappE-scraper-and-corpus.md",
        "35-swarm-functions-and-eternal-watchdogs.md",
        "36-identity-and-registration.md",
        "37-constitutional-principles-service.md",
        "38-external-communication-and-authority.md",
        "section_part_vi_spiritual_identity_governance.md",
    ]),
    ("6. Consciousness, Evaluation, and Synthesis", [
        "section_part_iv_consciousness.md",
        "22-identity-focused-retention.md",
        "23-dual-tracks-meaning-and-analysis.md",
        "24-feedback-into-broader-layers.md",
        "25-consciousness-coordinator-and-services.md",
        "39-operational-evaluation.md",
    ]),
]


def read_file(name: str) -> str:
    path = Path(__file__).parent / name
    return path.read_text(encoding="utf-8")


def main() -> None:
    out_path = Path(__file__).parent / "thesis.md"
    with out_path.open("w", encoding="utf-8") as out:
        # Optional: top-level thesis title or front matter can go here.

        for part_idx, (part_title, files) in enumerate(SUPER_CHAPTERS, start=1):
            # Part heading
            out.write(f"# {part_title}\n\n")

            for chapter_idx, filename in enumerate(files, start=1):
                # Section intros: include raw, no numbered subheading.
                if filename.startswith("section_part_"):
                    out.write(read_file(filename))
                    out.write("\n\n")
                    continue

                # Regular chapters: numbered subheading + content.
                chapter_num = f"{part_idx}.{chapter_idx}"
                # By default, use filename as label; you can plug in a map if desired.
                chapter_title = filename
                out.write(f"## {chapter_num} {chapter_title}\n\n")
                out.write(read_file(filename))
                out.write("\n\n")


if __name__ == "__main__":
    main()
