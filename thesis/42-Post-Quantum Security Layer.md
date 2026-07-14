# 42. Post-Quantum Security Layer
*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 13, 2026*
---
## 42.1 Purpose
The Post-Quantum Security Layer protects Ms. Allis against adversaries who can exploit present or future cryptanalytic capabilities to observe, alter, replay, or counterfeit authority-bearing communication.

In this architecture, post-quantum security is not only a matter of external identity or public-facing transport. It applies directly to the governed path by which sandbox reasoning, guardian review, bridge transition, identity assertions, and promotion authority interact. The chapter therefore treats post-quantum security as part of the internal sovereignty of the system, not merely as a boundary defense at the edge of the network.
This matters because reasoning can remain formally sandboxed while still becoming unsafe if the channels governing promotion and review are weak. Secure channels are part of the reasoning architecture whenever those channels carry authority.

Unlike earlier drafts of this chapter, this revision separates the design requirements from the implementation record. Sections 42.2 through 42.10 state what the architecture requires. Sections 42.11 through 42.13 state what is verified as built, what is known to be broken, and what remains unprotected as of this writing. That separation is itself a governance decision: a security chapter that cannot distinguish its aspirations from its audit results is not a security chapter.

---
## 42.2 Scope of Protection
The protected scope includes all communication links whose compromise could distort authority transitions.
At minimum, this includes communication across:
- sandbox services;
- guardian or constitutional review services;
- consciousness or promotion bridge services;
- identity services;
- authority or governance services that participate in approval, classification, or promotion control.
These links are not secondary infrastructure. They are part of the path by which provisional reasoning becomes accepted state. If those channels are not secured, the architecture can lose sovereignty even when its logical gate design is otherwise sound.
The governed-belief pipeline introduced in Chapters 45–52 extends this scope. The promotion path now includes intake services, embedding services, the vector store, and the relational system of record. A collection promotion in the publication manifest is an authority transition in exactly the sense this chapter means: it changes what the system will retrieve, cite, and act upon. Those channels therefore fall inside the protected scope, whether or not they were originally conceived as security-relevant.
---
## 42.3 PQ-Secure Service Requirements
PQ-secure communication requirements should apply across the full authority path.
Each service participating in sandbox evaluation, guardian review, bridge handoff, identity assertion, or authority escalation should use communication methods resistant to both conventional attack and foreseeable quantum-enabled attack against key exchange, signatures, or integrity guarantees. The aim is to preserve authenticity, confidentiality where required, and message integrity across the internal promotion path as well as across external links.
This implies several practical requirements:
- authenticated service-to-service communication;
- integrity protection for request and response payloads;
- replay resistance for promotion-bearing messages;
- cryptographic binding between service identity and transmitted authority claims;
- secured channel establishment that remains defensible under post-quantum threat assumptions.
The chapter is therefore not limited to identity in the abstract. It covers the full set of channels through which identity, review, and promotion operate together.
---
## 42.4 Sandbox and Guardian Channels
The sandbox and guardian links deserve special emphasis.
A sandbox result is still provisional, but the communication carrying that result toward validation can become authority-relevant the moment it enters review. For that reason, the channel from sandbox service to validator or guardian service should be secured with the same seriousness applied to more visibly external security boundaries. If this channel is compromised, an adversary could alter candidate content, inject misleading metadata, tamper with provenance, or forge review context before gate evaluation.
Guardian channels are especially sensitive because they carry payloads that determine whether a candidate is constitutionally or procedurally admissible. PQ-secure transport at this stage helps ensure that review decisions are being made over the intended payload rather than over manipulated substitutes.
---
## 42.5 Bridge, Identity, and Authority Channels
Bridge, identity, and authority services also require PQ-secure communication.
The bridge is the point at which approved or limited-approved candidates are handed toward higher-authority system state. Identity and authority services establish who is permitted to assert, review, approve, or receive the resulting transition. If those channels are weak, the system may preserve logical gate structure on paper while losing practical control over who can trigger or impersonate an authority-bearing event.
This is why secured promotion channels are part of sovereignty-preserving reasoning. The system preserves sovereignty not only by thinking safely, but by ensuring that the path from thought to promoted action cannot be intercepted, forged, downgraded, replayed, or silently redirected.
---
## 42.6 Sovereignty-Preserving Reasoning
Sovereignty-preserving reasoning includes secured internal promotion, not only secured external communication.
In this thesis, sovereignty means that Ms. Allis retains governed control over how internal candidates become accepted, durable, or consequential system state. That control depends not only on formal review logic but also on the integrity of the channels connecting sandbox, guardian, bridge, identity, and authority services. If those channels can be manipulated, sovereignty is weakened from within even when perimeter protections appear strong.
For that reason, post-quantum security belongs inside the reasoning pipeline itself. A reasoning system is not fully sovereign if the communications that determine promotion can be forged by a more capable adversary.
---
## 42.7 Security in the Promotion Algebra
The broader promotion algebra should include an explicit security-gate component.
If \(x\) is a candidate state offered for promotion, the overall gate can be written as a structured conjunction of required conditions:
\[
G(x) = G_{\mathrm{truth}}(x)\, G_{\mathrm{guardian}}(x)\, G_{\mathrm{constitutional}}(x)\, G_{\mathrm{provenance}}(x)\, G_{\mathrm{coherence}}(x)\, G_{\mathrm{privacy}}(x)\, G_{\mathrm{security}}(x)
\]
Here \(G_{\mathrm{security}}(x)\) represents the security-gate component. It covers the security conditions necessary for the candidate to move across the authority boundary without channel compromise, cryptographic impersonation, or integrity loss. In a post-quantum framing, this includes whether the relevant service path satisfies the cryptographic and transport requirements needed for sovereignty-preserving promotion.
This expression is useful because it makes clear that secure communication is not external ornamentation. It is one of the constitutive conditions of valid promotion.
---
## 42.8 Security-Gate Meaning
The security gate should be interpreted broadly enough to cover the operational authority path.
\(G_{\mathrm{security}}(x)\) is not only a check for whether a message was encrypted somewhere in transit. It concerns whether the candidate’s full path across sandbox, validator, guardian, bridge, identity, and authority services remained protected against substitution, replay, unauthorized disclosure, forged approval, or cryptographic downgrade. A candidate should not be promotion-eligible if its transit path fails the security conditions required for trust in the resulting authority change.
This means the security gate can block promotion even when truth and policy checks are otherwise favorable. Safe content transmitted over an untrustworthy authority channel is still not safe to promote.
---
## 42.9 Internal and External Communications
The chapter should distinguish between two truths without separating them.
First, post-quantum security is still relevant to external communication, public interaction, and cross-boundary transport. Second, and equally important here, internal service-to-service communications involved in sandbox reasoning and promotion review also require protection when they carry authority-bearing consequences. The second point is what anchors this chapter to the internal path rather than to identity alone.
This architecture therefore treats internal security and external security as parts of one sovereignty problem. A system that secures its outer edge but leaves its internal promotion chain cryptographically weak has not preserved control over its own reasoning-to-authority transition.
---
## 42.10 Operational Consequences
Operationally, this chapter changes how the security layer should be discussed and evaluated.
Security review should ask whether sandbox-to-guardian communication is protected, whether guardian-to-bridge handoff is protected, whether identity assertions are cryptographically trustworthy, whether authority services can detect downgrade or replay conditions, and whether compromised or non-compliant channels prevent promotion. These are not optional hardening extras. They are requirements for the authority path itself.
This also means that fail-closed behavior should apply when required secured channels are unavailable or invalid. If the path cannot satisfy the security-gate conditions, promotion should not proceed.
---
## 42.11 Implementation Status (July 2026)
This section records what is verified as built, in the same demonstrated/not-yet-demonstrated discipline Chapter 52 applies to the epistemic loop.
**Demonstrated:**
- Post-quantum signing is active across all five judges in the judge pipeline. Verdict payloads are signed with a Dilithium-family scheme before reaching the Blood-Brain Barrier.
- The PQ crypto initialization defect discovered in May 2026 — `primary_kem` nested inside `.tls_outbound` rather than at the expected level — was repaired across twelve proxy files by correcting the fallback path to `SAFE_FALLBACK_SUITE.get("tls_outbound", {})`. This is the layer's first completed audit-and-remediation cycle.
- H_people membership proofs use BLAKE2b with structurally enforced salt-blindness, and kyc_vault isolation is enforced at the database layer via scoped roles. These are integrity and privacy controls that complement, but are not substitutes for, PQ transport.
- Network posture provides a compensating control: services bind to loopback only, with zero non-loopback bindings verified and ufw active. This narrows the practical attack surface to local compromise, but it is a perimeter property, not a cryptographic one, and this chapter does not treat it as satisfying \(G_{\mathrm{security}}\).
**Not yet demonstrated:**
- PQ-secured transport across the governed-belief promotion path (Section 42.13).
- Replay resistance and cryptographic binding of authority claims on promotion-bearing messages outside the judge pipeline.
- Fail-closed enforcement of the security gate: no service currently refuses a promotion because a channel failed a security condition.
---
## 42.12 Known Defect: Verification Failure at the BBB
The most consequential open defect in this layer is on the verification side, and it is recorded here rather than hidden, because a signature scheme whose verifier is broken provides authenticity in name only.
As found in the June–July 2026 chapter audit, `bbb_signature_verifier.py` carries a broken `DilithiumPublicKey` import from `dilithium_py`. The import failure causes every verdict presented to the Blood-Brain Barrier to be classified as `UNSIGNED_OR_FORGED_VERDICT`, regardless of whether the judges signed it correctly. Signing works; verification does not.
Two things should be said plainly about this state:
1. The failure mode is fail-closed in form — nothing verifies, so nothing is trusted on the basis of a forged-but-accepted signature. But a verifier that rejects everything provides no discrimination between authentic and forged verdicts, which means the BBB is currently operating without the authenticity guarantee this chapter assigns to it. Combined with the BBB's log-and-passthrough calibration, verdict authenticity is effectively unenforced at this boundary.
2. The remediation path is already identified and does not require new cryptography: route verification through the existing, working `verify_verdict` function in `judgesigner.py` rather than reconstructing key objects through the broken import. Until that routing is applied and a signed-verdict round trip is demonstrated, this chapter's claims about judge-to-BBB channel integrity must be read as design intent, not operational fact.
This defect is itself an instance of the pattern Chapter 52 names: discovering that a governance mechanism was silently non-functional is an epistemic event, and recording it is part of the layer's provenance.
---
## 42.13 Unprotected Surfaces in the Governed-Belief Path
The governed-belief infrastructure built out in Chapters 45–52 created authority-bearing channels that predate any PQ protection. As of this writing, the following operate over plain HTTP or unauthenticated local transport:
- the vector store (Chroma, port 8002), which holds every published governed collection and the commons;
- the relational system of record (PostgreSQL, port 5436, `msjarvisgis_v2`), which holds canonical identities, belief snapshots, and the publication manifest — the manifest being the literal promotion surface, since a row's advance to `active` changes what retrieval serves;
- the civic intake API (port 8100), which is a write path into H_p collections;
- the embedding services (Ollama, ports 11434 and 11435), whose output determines what a governed document means in vector space — a tampered embedding is a semantic substitution attack that no downstream hash of the text would catch;
- the HTTP client paths inside the ingest worker and the commons aggregator, which move candidate beliefs and anonymized centroids between these stores;
- GIS-RAG retrieval (port 8004) and the assertion gateway (port 8009).
The loopback-only binding discipline is the current compensating control for all of these. It is honest to state the consequence: against a local adversary or a compromised container on the shared Docker networks, the governed-belief promotion path currently fails \(G_{\mathrm{security}}\) across the board. The gate exists in the algebra; it is not yet wired into these services. Promotion in the publication manifest today is gated by human judgment and acceptance tests (Chapter 52's battery), not by any cryptographic condition.
Bringing these surfaces under the security gate — authenticated service identity, integrity protection on manifest writes, and signed promotion events at minimum — is the layer's next phase of work, and should be sequenced ahead of any expansion of autonomous action, since Chapter 52 conditions real-world action on exactly this kind of channel trust.
---
## 42.14 Closing Statement
The Post-Quantum Security Layer protects the integrity of the full promotion pathway in Ms. Allis.
PQ-secure communication therefore applies across sandbox, guardian, bridge, identity, and authority services — and now, explicitly, across the governed-belief promotion path of intake, embedding, vector publication, and manifest promotion — because secured promotion channels are part of sovereignty-preserving reasoning rather than merely a feature of external communications. By making the security gate an explicit component of the broader promotion algebra, and by recording candidly which of its conditions are demonstrated, which are broken, and which are not yet built, this chapter places post-quantum security exactly where it belongs: inside the governed path by which provisional reasoning becomes accepted system authority, held to the same evidentiary standard as the beliefs that path promotes.
