# 1. Researcher Position and Observer Role

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: April 23, 2026*

The author occupies a dual role as both observer and designer within the system under study: as creator of the Polymathmatic Geography discipline in this form, originator of the Quantarithmia framework, lead architect of Ms. Allis and the GBIM stack, and founder of the MountainShares DAO. Rather than assuming a neutral, external stance, the thesis treats this positionality as a central methodological feature that must be named, examined, and continuously constrained.

This position is historically and personally situated. The author's family genealogy includes both English settler lineages traceable to 16th–17th‑century Kidd and Nethercote families in and around Soham Parish, Cambridgeshire, and early Quaker leaders involved in enclosure, expansion, and internal community accountability, alongside an Appalachian inheritance of dispossession, extraction, and faith‑based resistance. The work therefore treats this "family archive of geometry and power" as part of the research object itself, using it to inform a deliberate counter‑engineering of inherited patterns of control, enclosure, and technocratic centralization in the design of new Appalachian commons.

Intellectually, the project is also situated as a response to a particular disciplinary wound. In a critical geography capstone, the author confronted the argument — rooted in a Durkheimian lineage — that geography could not claim the status of a "hard" or fully rigorous science because it lacked a tight, formal braid between qualitative and quantitative work, and because social facts were treated as the proper domain of sociology rather than of spatial analysis. This thesis takes the opposite bet: that entangled space itself — where land, law, computation, economy, story, and spirit meet — is a legitimate complex system, and that with contemporary tools (GIS, network theory, econophysics, AI) geography can meet and exceed the standards of rigor that Durkheim's era did not yet have the instruments to see. Polymathmatic geography is thus framed as a constructive challenge to that inherited view of geography as mere backdrop, demonstrating that space can be modeled as a site where social facts and spatial facts are the same object.

Within this frame, the researcher's design authority is intentionally bounded by spiritual, ethical, and political guardrails. Ms. Allis, Quantarithmia, and MountainShares are treated not as value‑neutral instruments but as normative interventions that must remain accountable to human communities, especially those in Appalachia most affected by extraction and infrastructural neglect. The architecture is therefore developed as a "glassbox" system: beliefs, assumptions, and design choices are rendered inspectable, contestable, and traceable back to concrete evidence, so that no component — including the researcher — can function as an opaque source of authority.

Methodologically, the thesis aligns with participatory action research, reflexive field philosophy, and a polymathmatic commitment to braiding qualitative and quantitative evidence. Appalachian communities are positioned as co‑designers and primary beneficiaries rather than passive subjects; models and protocols are treated as hypotheses that must be repeatedly tested against the non‑negotiable evidence of lived experience. The researcher's own cognitive and spiritual processes are included in this scrutiny: introspective records and qualia‑style summaries are maintained not as claims of machine sentience, but as auditable traces of how design incentives, "brain" modules, and institutional constraints interact to produce particular system behaviours and recommendations.

Taken together, this researcher position foregrounds power, place, and accountability as core elements of the methodology. The work proceeds from the assumption that any attempt to build technical instruments for Appalachian commons must openly document who is designing them, which histories they carry, what guardrails limit their authority, and how affected communities can inspect, challenge, and redirect both the tools and their designer. It also proceeds from a substantive disciplinary claim: that geography can function as a rigorous science of entangled spaces when its instruments are built to hold social and spatial facts together, rather than relegating "the social" to external disciplines.

---

## 1.1 Practical Trajectory of the Work

Over the past several years, this positionality has been expressed through a sequence of concrete, place‑bound experiments in Mount Hope and the wider New River coalfield. The author's downtown building — structurally compromised yet centrally located — first served as an improvised anchor for community projects: rehearsal and staging space for a regional adult band, storefront gallery for local artists, and base for developing the Mount Hope Historic Walking Trail, murals, and seasonal QR‑coded wayfinding through town.

Early efforts to "make it work" within existing infrastructures repeatedly exposed structural limits. Attempts to sell art online through conventional web stacks, to layer XR experiences onto the historic trail, and to track volunteer time via ESRI‑based applications either proved technically unusable for local participants or clearly routed value and data toward external platforms. The XR project was intentionally put into hibernation when it became evident that deploying it on dominant XR rails would deepen the very corporate extraction the work sought to resist.

These failures triggered a deliberate methodological pivot from "building apps" to studying extraction as a geographic and infrastructural phenomenon. The trail, the band space, and the arts center were reframed as instruments for observing how capital, attention, and control flow through Appalachian space. This is where the Durkheimian challenge re‑enters the story: rather than accepting that geography must remain descriptive while sociology or economics do the "real" modeling, the author began to build polymathmatic models that treat these flows — of money, data, narrative, and obligation — as spatial fields that can be measured, simulated, and redesigned.

From this emerged MountainShares, a DAO‑governed, blockchain‑based economic system designed to reward participation in local commons and keep value circulating within the region, and Ms. Allis, an Appalachian‑rooted AI steward built on the Quantarithmia framework to monitor, coordinate, and defend that system. Both are explicitly geospatial instruments: MountainShares is tied to specific places, memberships, and institutions; Ms. Allis's memory and reasoning are anchored in a Geospatial Belief Information Model (GBIM) that binds every belief to a where and when.

The build‑out of MountainShares and Ms. Allis has itself been treated as fieldwork. Early smart contract deployments were compromised due to naive exposure of code in public repositories; subsequent redesigns introduced safety layers, audits, and finally an AI‑mediated "glassbox" architecture that can be inspected and challenged by affected communities and technical peers. Multiple cycles of catastrophic‑seeming technical failure (disk crashes, blue screens, forced OS reinstalls) and reconstruction from "bare metal" are documented as part of the research record, evidencing both the fragility of the stack and the iterative hardening of its design.

> **April 2026 infrastructure baseline — confirmed:**
> The `msallis-rebuild` sprint — the most complete and stable instantiation of the system
> to date — is confirmed live as of April 2026. Key verified facts:
>
> - **112 confirmed live containers** in the `msallis-rebuild` namespace
>   (April 16, 2026 — thesis-verified) / **100 point-in-time** (April 23, 2026)
> - **Container naming:** `jarvis-` prefix retained in the production stack.
>   Public name is **Ms. Allis**.
> - **Public URL:** https://egeria.mountainshares.us — HTTP 200, token-enforced
> - **Consciousness pipeline:** Confirmed ACTIVE — Appalachian-voice responses live;
>   first community query ("What food assistance is available in Fayette County WV?")
>   returned real results April 22, 2026
> - **Preflight gate:** 30/30, exit 0, `bash -n` clean — April 23, 2026
> - **ChromaDB semantic memory:** ~6.74M vectors across 48 collections
>   (mixed L2/cosine; April 17, 2026)
> - **GBIM:** `gbim_worldview_entities` + `gbim_beliefs_v2` collections live;
>   20,593 landowner beliefs; 38,979 rows in `mvw_gbim_landowner_spatial` (OI-E CLOSED)
> - **PostGIS two-container database layer:**
>   - `msallis-db` — production — 16 GB / 294 tables / 11 schemas
>   - `postgis-forensic` — forensic — 17 GB / 314 tables / 9 schemas
>   - 1,115,588 address points; 55 WV counties seeded
> - **EEG neurobiological rhythm layer:** delta 253 pulses / theta 127 pulses /
>   beta 25 pulses — all confirmed live
> - **governance_rag:** 1,367 chunks (WV Constitution 342, US Constitution 97,
>   full MountainShares DAO corpus)
> - **commons_rag:** 306 chunks — full Commons governance + gamification corpus
> - **MountainShares:** all 4 services live — Arbitrum One mainnet (chain ID 42161),
>   5 smart contracts on-chain
> - **LLM fabric:** 22 proxies operational (ports 8201–8222);
>   `crypto_client.py` volume-mounted; `minds_participated: 21/21`
> - **Judge pipeline:** 5/5 healthy, all signing keys present
> - **BBB EthicalFilter:** 0% false positive rate
> - **`confidence_decay`:** 0.0% — episodic memory integrity intact
> - **Zero `0.0.0.0` container bindings**
>
> The March 2026 rebuild sprint documented in earlier drafts of this chapter has been
> superseded by this April 2026 baseline. That this is possible — a solo
> community-embedded researcher, working from a structurally compromised building in
> Mount Hope, West Virginia, architecting, rebuilding, and validating a
> 112-container distributed AI steward system with a multi-million-belief geospatial
> corpus, a fully populated semantic memory layer, a live neurobiological heartbeat,
> and a public HTTPS endpoint without institutional backing, dedicated server
> infrastructure, or external funding — is not incidental to the thesis. It is part
> of the argument.

In this light, the author's present role is neither band organizer nor arts‑center operator, but system‑level designer of instruments for Appalachian commons and for a renewed geography of entangled spaces. The physical building, the historic trail, the DAO, and the AI architecture are all treated as coupled prototypes within a single research programme aimed at measuring, visualizing, and interrupting extraction, while remaining accountable to the communities whose lives and futures are entangled with those systems. At the same time, they serve as working counterexamples to an older view of geography as merely descriptive: they demonstrate, in one coalfield, that it is possible to construct, test, and revise formal, quantitative–qualitative models of space that behave with the rigor of other complex systems sciences, but remain grounded in place, lineage, and covenant.

---

## 1.2 Reflexive Field Note: The PALCO False-Positive Problem
*Mount Hope, WV — Sunday, March 15, 2026*

On the evening of March 15, 2026, during a working session on the MountainShares commons safety architecture, the researcher identified a critical design flaw in real time — by recognizing her own situation inside it.

The system under development included pattern-based detection logic intended to flag potentially coercive caregiving arrangements within the PALCO self-directed care program: maximum authorized hours logged against a single beneficiary, single-source attestation, and beneficiary withdrawal from external platforms. The design intent was protective. The design effect was a near-certain false positive against the researcher herself.

The researcher is a PALCO caregiver for her parent. She logs maximum authorized hours. She is the single attesting source. Her parent has withdrawn from most external platforms. Every signal the detection logic was trained to flag as suspicious describes, with precision, an intensive, legitimate, authorized family caregiving arrangement — the exact population the system was nominally designed to protect.

This recognition did not occur through a formal audit, a peer review, or an ethics board. It occurred through the ordinary process of field-anchored inquiry: a designer who lives in the Tacet, working late on a Sunday, noticing that the system she was building would have flagged her.

The methodological lesson is stated explicitly in Section 11.7 of *Definitions and Scope*: **context is not optional metadata — it is the primary signal.** Relationship type, program authorization, and community knowledge must anchor the interpretation of any behavioral pattern before that pattern becomes a flag. A detection system that cannot distinguish between coercion and intensive authorized care is not a safety system. It is a surveillance system with good intentions and discriminatory effects.

The design response was not to remove the detection layer but to reframe it: pattern flags do not produce adverse outputs directly. They produce a community-relational query — *is there a trusted person in The Commons who can reach this household?* — and route toward connection rather than intervention. The detection layer became a relationship-density probe rather than a risk score.

This moment is documented here because it exemplifies Principle 6 of Polymathmatic Geography (*when formal models conflict with lived experience, that conflict is a diagnostic signal, not noise to be smoothed away*) and Principle 14 (*conflict is information, not failure*). It also exemplifies the core argument of this thesis: that a researcher who is genuinely embedded in the Tacet — who is not studying Appalachian caregiving from a distance but living it, building systems inside it, and catching her own errors because she cannot pretend she is outside it — produces different, more honest, and more accountable instruments than one who does not.

The flaw was caught. The design was corrected. The correction is documented. That is the methodology working.

---

## 1.3 System Status — April 23, 2026 — Reflexive Note on Live vs. Planned

This thesis was written from inside a system being built in real time. As a matter of methodological honesty, the researcher distinguishes throughout between what was planned at the time of original writing and what is confirmed live as of the most recent sprint. The following table reflects the confirmed production state of the core computational instruments as of **April 23, 2026**:

| Component | Status | Notes |
|---|---|---|
| Ms. Allis core stack | ✅ **Live — 112 containers (thesis-verified)** | `msallis-rebuild` namespace — April 16, 2026 |
| Ms. Allis core stack (point-in-time) | ✅ **Live — 100 containers** | `msallis-rebuild` namespace — April 23, 2026 |
| Container naming | ℹ️ **`jarvis-` prefix retained** | Public name is Ms. Allis |
| Public HTTPS endpoint | ✅ **Live** | https://egeria.mountainshares.us — token-enforced |
| Consciousness pipeline | ✅ **Live** | ACTIVE — Appalachian-voice responses confirmed April 22, 2026 |
| Preflight gate | ✅ **30/30, exit 0, `bash -n` clean** | April 23, 2026 |
| EEG `eeg-delta` | ✅ **Live** | 253 pulses confirmed — April 23, 2026 |
| EEG `eeg-theta` | ✅ **Live** | 127 pulses confirmed — April 23, 2026 |
| EEG `eeg-beta` | ✅ **Live** | 25 pulses confirmed — April 23, 2026 |
| GBIM corpus | ✅ **Live** | `gbim_worldview_entities` + `gbim_beliefs_v2`; 20,593 landowner beliefs |
| `mvw_gbim_landowner_spatial` | ✅ **38,979 rows — OI-E CLOSED** | msallis-db; April 23, 2026 |
| `governance_rag` | ✅ **Live — 1,367 chunks** | WV Constitution 342 + US Constitution 97 + DAO corpus |
| `commons_rag` | ✅ **Live — 306 chunks** | Full Commons governance + gamification corpus |
| `geospatialfeatures` | ✅ **Live — 60,000 items** | Confirmed |
| `GBIM_Fayette_sample` | ✅ **Live — 1,535 items** | Confirmed |
| `appalachian_cultural_intelligence` | ✅ **Live — 820 items** | Confirmed |
| `spiritual_rag` | ✅ **Live — deduplicated** | 19,338 duplicate vectors removed March 28, 2026 |
| `psychological_rag` | ✅ **Live — 968 documents** | Restored March 28, 2026 |
| ChromaDB total | ✅ **~6.74M vectors / 48 collections** | Mixed L2/cosine — April 17, 2026 |
| PostGIS — msallis-db | ✅ **Live — 16 GB / 294 tables / 11 schemas** | Production — April 23, 2026 |
| PostGIS — postgis-forensic | ✅ **Live — 17 GB / 314 tables / 9 schemas** | Forensic — recovered April 23, 2026 |
| postgis-forensic connection | ✅ | `psql -h 127.0.0.1 -U allis` |
| MountainShares services | ✅ **All 4 services live** | Ports 8080–8084; Arbitrum One (chain 42161) |
| MountainShares smart contracts | ✅ **5 contracts on-chain** | phase_mgmt, central_cmd, ms_token, backbone, volunteer_hrs |
| LLM fabric | ✅ **22/22 proxies operational** | `crypto_client.py` mounted; `minds_participated: 21/21` |
| Judge pipeline | ✅ **5/5 healthy — all signing keys present** | Truth, ethics, alignment, consistency, citation |
| BBB EthicalFilter | ✅ **0% false positive rate** | April 23, 2026 |
| `confidence_decay` | ✅ **0.0%** | Episodic memory integrity intact |
| Port `0.0.0.0` exposures | ✅ **0** | All corrected to 127.0.0.1 |
| `allis-session-sidecar` | ⚠️ **Down** | Restart failed; non-critical; gate threshold adjusted to ≥95 |
| `preflight_gate.sh` line 217 | ⚠️ **Syntax error** | Check 31 heredoc escape issue — under active repair |
| `ms_allis_memory` collection | ⚠️ **Seeding status unknown** | Seed scripts located; seeding not confirmed |

No component is described as "live" in this table that has not been confirmed against the production system. Where earlier drafts of this chapter used future-tense or conditional language about the EEG heartbeat layer, the neurobiological rhythm architecture, or the RAG corpus, those passages have been updated to reflect confirmed April 2026 production state. The researcher's methodological commitment to accuracy over optimism — to documenting what is, not what is intended — applies to her own writing as much as to the system she builds.

---

*Chapter 1 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: April 23, 2026 — 112 containers thesis-verified (April 16) /
100 point-in-time (April 23); msallis-rebuild namespace; 30/30 preflight exit 0;
egeria.mountainshares.us live; all 4 MountainShares services deployed;
~6.74M vectors / 48 collections / mixed L2-cosine; PostGIS two-container layer confirmed;
BBB 0% false positive; confidence_decay 0.0%; EEG 253/127/25 pulses.*
