Chapter 42 — Post‑Quantum Security

This chapter explains how the post‑quantum security layer protects Appalachian communities, their data, and the AI decisions made in their name, without relying on diagrams or port maps. Instead of focusing on low‑level commands, it focuses on what the cryptographic pieces are for, what they do, and how they reinforce the constitutional commitments already laid out in earlier chapters.

### 42.1 Why Post‑Quantum Security Matters Here

Post‑quantum cryptography refers to cryptographic methods designed to stay secure even if future attackers gain access to powerful quantum computers. In this system, the core methods are ML‑DSA‑65 for digital signatures and ML‑KEM‑768 combined with a classical curve (X25519) for key exchange, with AES‑256‑GCM and SHA3‑256 as the workhorse tools for encryption and hashing.

These choices are not about chasing a trend; they are about designing for the lifespan of the records and decisions the system will hold. Land use recommendations, benefit eligibility records, and community governance decisions may need to be trusted many years from now, long after today’s hardware has been replaced. The security layer is built on the assumption that future threats should not be able to quietly rewrite the stories told about these places or the people who live in them.

In the language of the thesis, this is one way that “power has a geometry.” The geometry of power here is shaped by who can edit a verdict, who can forge a decision, and who can change an answer without leaving a trace. Post‑quantum signing and key exchange lock that geometry in place so that even infrastructure operators cannot silently tamper with verdicts once they are issued.

### 42.2 The Human‑Level Goals of the Security Layer

The technical documentation names five design principles; in plain language, they become five goals.

1. **Flexibility when risk changes.**  
   A central “crypto policy” service describes which algorithms to use, rather than baking those choices into each container. When standards evolve or a new vulnerability appears, the policy can change and the whole stack adjusts without a rebuild.

2. **No deniability about AI decisions.**  
   Every judgment that passes through the judge pipeline is signed, so the system can later prove that a decision did or did not come from an authorized judge. This is called non‑repudiation in the technical text.

3. **Tamper‑evident verdicts.**  
   If someone tries to edit a verdict—changing a score, flipping a Boolean, or rewriting a label—the signature will fail to verify, and the altered verdict will be rejected before it can influence anything downstream.

4. **Built‑in privacy protections.**  
   On certain paths, differential privacy and schema rules limit what can be inferred about individual people from the system’s answers, especially when dealing with small counties, rare conditions, or thinly populated hollows.

5. **A durable trail of “yes” and “no.”**  
   Decisions made by input and output gates are written into a dedicated audit service, with authentication enforced. That trail is meant for community accountability and academic review, not just debugging.

These goals connect cryptography to geography and governance. They ensure that when the system answers questions about land, benefits, or local resources, those answers sit on top of a verifiable, reviewable record of how they were tested and approved.

### 42.3 The Crypto Policy Service as a Single Source of Truth

The jarvis‑crypto‑policy service is described in the technical chapter as the “cryptographic brain.” It runs continually, tracks which algorithms are approved, and reports a simple threat level: NOMINAL, ELEVATED, or CRITICAL.

- At NOMINAL, the documented post‑quantum and classical hybrid algorithms are available.
- At ELEVATED, the policy tightens, enforcing stricter key exchange groups and shorter signature validity windows.
- At CRITICAL, classical fallbacks are disabled and only the strongest suite remains.

Every AI proxy checks this policy at startup and periodically during operation, rather than making its own independent choices. If the policy service cannot be reached, the clients are designed to fall back to a hardcoded safe suite that is at least as strong as the normal configuration, rather than quietly dropping to something weaker.

This centralization is not about hoarding control; it is about visibility. Instead of having dozens of hidden cryptographic settings scattered across containers, there is one place where a community auditor, university partner, or regulator can see which algorithms are currently in use and under what conditions they change.

### 42.4 How the Judges Sign and Prove Their Work

The judge pipeline has five services: one orchestrator and four specialized judges for truth, ethics, alignment, and consistency. The question is how to ensure that a verdict entering the rest of the system really came from these judges and has not been altered in transit.

The answer is a module called `judgesigner.py`, installed into every judge container and backed by a shared post‑quantum keypair stored on the host and mounted into the containers at runtime. In practice, the module does two things:

- When a judge finishes evaluating a candidate answer, it calls a function that takes the verdict, computes a SHA3‑256 hash of its contents, signs that hash with ML‑DSA‑65, and attaches a signature block with metadata such as the algorithm, timestamp, and a short fingerprint of the public key.
- When another component receives the signed verdict, it calls a verification function that recomputes the hash, compares it to the stored value, and verifies the signature against the mounted public key.

All sub‑judges call the signing function, and the pipeline verifies their verdicts before aggregating them, then signs the final combined verdict again before handing it off to the next layer. Sprint scripts confirm that this signing path is active in all relevant files and that a suite of end‑to‑end checks passed during the validation window.

Key management is handled with the caution you would expect for something that can vouch for every decision in the system. The private key file is ignored by version control, backed up in encrypted form in multiple locations, and mirrored to an air‑gapped USB drive, with clear instructions for rotation if a compromise is suspected.

### 42.5 The BBB Gate and Its Relationship to Signatures

Between the judges and any user‑facing output stands the Behavioral Boundary and Blocking gate, or BBB. It examines verdicts and candidate responses through six lenses—ethical, spiritual, safety, threat detection, steganography, and truth—and can block, flag, or pass content.

For input, BBB is fully active and enforced. For the final output layer (Phase 4.5), the system is currently operating in log‑and‑passthrough mode: when the filter is unsure, it permits the content but logs the event for calibration instead of blocking it outright. This mode was chosen after the system misread a significant portion of maternal Appalachian voice as unethical or unsafe, with phrases like “Child, that’s just plain wrong!” wrongly flagged.

The logs for these borderline decisions are written into the dedicated audit service, jarvis‑memory, so that the false positives can be studied and the thresholds adjusted. The chapter marks the recalibration of this output gate as a priority for future work, including wiring in direct verification of the Dilithium signatures BBB already receives.

From a constitutional perspective, this arrangement shows how the system treats local voice as something to be preserved rather than scrubbed away by over‑cautious filters. It also lays out a path to harden the final gate so that no unsigned or improperly signed verdict can slip through unnoticed.

### 42.6 Protecting Data at Rest and in Transit

Beneath all of this, the system’s databases and transport pathways are protected in ways that matter for both security and community trust.

On the storage side, data in the local resources database is encrypted at rest using AES‑256‑GCM through transparent data encryption functions, with per‑record keys derived from a master key that is never stored in the tables themselves. That means that a stolen disk image or snapshot reveals only ciphertext, not a readable spreadsheet of addresses, benefits, or resource locations.

On the transport side, public traffic flows through a Cloudflare tunnel to a local Caddy server, with every step of the chain encrypted and all application services bound only to the loopback interface. Caddy enforces authentication by calling an internal auth service before letting any request reach the main pipeline, returning a 401 error when there is no valid token.

Together, these measures ensure that the cryptographic protections do not stop at signatures on verdicts. They extend to the channels that carry questions and answers and to the disks that hold the knowledge the system uses to reason about place and policy.

### 42.7 Audit Trails, Gates, and Ongoing Verification

The audit and verification story does not end when a verdict is signed or a gate passes. The dedicated memory service collects a record of gate decisions, while the `VERIFYANDTEST.sh` script exercises a growing set of “preflight gates” that must all pass before a stack is considered in‑thesis.

Recent work added gates to confirm that:

- The audit service is enforcing authentication and storing gate decisions.
- Confidence‑decay metadata exists and is non‑null in the relevant tables.
- ChromaDB has at least a documented minimum number of collections.
- A psychological retrieval domain is not only declared but populated.
- The crypto policy service is healthy and reachable.
- Governance‑related API endpoints are alive and responding to smoke tests.

All of these gates were passing as of the April 1, 2026 run, with zero failures or warnings after a round of duplicate line cleanup. The effect is to bind the abstract principles of the security layer—non‑repudiation, tamper‑evidence, accountability—to a concrete checklist that must be satisfied before new capabilities are accepted into the live system.

In combination, the signatures, the gates, the encrypted storage, the authenticated tunnel, and the durable audit trail make this security layer more than a schematic. They make it a lived practice of polymathmatic geography, where cryptography, land and benefits data, community voice, and local governance are kept in balance by design, not by accident.
