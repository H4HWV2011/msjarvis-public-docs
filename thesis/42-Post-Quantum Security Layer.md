# 42. Post‑Quantum Security Layer

Carrie Kidd (Mamma Kidd) — Mount Hope, WV  
Last updated: July 16, 2026

---

## 42.1 Purpose

The Post‑Quantum Security Layer protects Ms. Allis against adversaries who can exploit present or future cryptanalytic capabilities to observe, alter, replay, or counterfeit authority‑bearing communication.

In this architecture, post‑quantum security is not only a matter of external identity or public‑facing transport. It applies directly to the governed path by which sandbox reasoning, guardian review, bridge transition, identity assertions, and promotion authority interact. The chapter therefore treats post‑quantum security as part of the internal sovereignty of the system, not merely as a boundary defense at the edge of the network. This matters because reasoning can remain formally sandboxed while still becoming unsafe if the channels governing promotion and review are weak. Secure channels are part of the reasoning architecture whenever those channels carry authority.

Sections 42.2 through 42.10 describe the architectural requirements. Sections 42.11 through 42.14 record what is verified as built, what has been remediated, and what remains unprotected as of this writing. Keeping these concerns distinct is a governance choice: a security chapter must clearly separate design intent from audit results.

---

## 42.2 Scope of Protection

The protected scope includes all communication links whose compromise could distort authority transitions. At minimum, this includes communication across:

- sandbox services  
- guardian or constitutional review services  
- consciousness or promotion bridge services  
- identity services  
- authority or governance services that participate in approval, classification, or promotion control  

These links are not secondary infrastructure. They are part of the path by which provisional reasoning becomes accepted state. If those channels are not secured, the architecture can lose sovereignty even when its logical gate design is otherwise sound.

The governed‑belief pipeline introduced in Chapters 45–52 extends this scope. The promotion path now includes intake services, embedding services, the vector store, and the relational system of record. A collection promotion in the publication manifest is an authority transition in exactly this sense: it changes what the system will retrieve, cite, and act upon. Those channels therefore fall inside the protected scope, whether or not they were originally conceived as security‑relevant.

---

## 42.3 PQ‑Secure Service Requirements

PQ‑secure communication requirements apply across the full authority path. Each service participating in sandbox evaluation, guardian review, bridge handoff, identity assertion, or authority escalation should use communication methods resistant to both conventional attack and foreseeable quantum‑enabled attack against key exchange, signatures, or integrity guarantees. The aim is to preserve authenticity, confidentiality where required, and message integrity across the internal promotion path as well as across external links.

This implies several practical requirements:

- authenticated service‑to‑service communication  
- integrity protection for request and response payloads  
- replay resistance for promotion‑bearing messages  
- cryptographic binding between service identity and transmitted authority claims  
- secured channel establishment that remains defensible under post‑quantum threat assumptions  

The chapter is therefore not limited to identity in the abstract. It covers the full set of channels through which identity, review, and promotion operate together.

---

## 42.4 Sandbox and Guardian Channels

The sandbox and guardian links deserve special emphasis. A sandbox result is still provisional, but the communication carrying that result toward validation can become authority‑relevant the moment it enters review. For that reason, the channel from sandbox service to validator or guardian service should be secured with the same seriousness applied to more visibly external security boundaries. If this channel is compromised, an adversary could alter candidate content, inject misleading metadata, tamper with provenance, or forge review context before gate evaluation.

Guardian channels are especially sensitive because they carry payloads that determine whether a candidate is constitutionally or procedurally admissible. PQ‑secure transport at this stage helps ensure that review decisions are being made over the intended payload rather than over manipulated substitutes.

---

## 42.5 Bridge, Identity, and Authority Channels

Bridge, identity, and authority services also require PQ‑secure communication. The bridge is the point at which approved or limited‑approved candidates are handed toward higher‑authority system state. Identity and authority services establish who is permitted to assert, review, approve, or receive the resulting transition. If those channels are weak, the system may preserve logical gate structure on paper while losing practical control over who can trigger or impersonate an authority‑bearing event.

Secured promotion channels are therefore part of sovereignty‑preserving reasoning. The system preserves sovereignty not only by thinking safely, but by ensuring that the path from thought to promoted action cannot be intercepted, forged, downgraded, replayed, or silently redirected.

---

## 42.6 Sovereignty‑Preserving Reasoning

Sovereignty‑preserving reasoning includes secured internal promotion, not only secured external communication. In this thesis, sovereignty means that Ms. Allis retains governed control over how internal candidates become accepted, durable, or consequential system state. That control depends not only on formal review logic but also on the integrity of the channels connecting sandbox, guardian, bridge, identity, and authority services. If those channels can be manipulated, sovereignty is weakened from within even when perimeter protections appear strong.

For that reason, post‑quantum security belongs inside the reasoning pipeline itself. A reasoning system is not fully sovereign if the communications that determine promotion can be forged by a more capable adversary.

---

## 42.7 Security in the Promotion Algebra

The broader promotion algebra should include an explicit security‑gate component. If \(x\) is a candidate state offered for promotion, the overall gate can be written as a structured conjunction of required conditions:

\[
G(x) = \big(G_{\mathrm{truth}}(x),\,
G_{\mathrm{guardian}}(x),\,
G_{\mathrm{constitutional}}(x),\,
G_{\mathrm{provenance}}(x),\,
G_{\mathrm{coherence}}(x),\,
G_{\mathrm{privacy}}(x),\,
G_{\mathrm{security}}(x)\big)
\]

Here \(G_{\mathrm{security}}(x)\) represents the security‑gate component. It covers the security conditions necessary for the candidate to move across the authority boundary without channel compromise, cryptographic impersonation, or integrity loss. In a post‑quantum framing, this includes whether the relevant service path satisfies the cryptographic and transport requirements needed for sovereignty‑preserving promotion. This expression makes clear that secure communication is not external ornamentation. It is one of the constitutive conditions of valid promotion.

---

## 42.8 Security‑Gate Meaning

The security gate should be interpreted broadly enough to cover the operational authority path. \(G_{\mathrm{security}}(x)\) is not only a check for whether a message was encrypted somewhere in transit. It concerns whether the candidate’s full path across sandbox, validator, guardian, bridge, identity, and authority services remained protected against substitution, replay, unauthorized disclosure, forged approval, or cryptographic downgrade. A candidate should not be promotion‑eligible if its transit path fails the security conditions required for trust in the resulting authority change.

This means the security gate can block promotion even when truth and policy checks are otherwise favorable. Safe content transmitted over an untrustworthy authority channel is still not safe to promote.

---

## 42.9 Internal and External Communications

Two facts both matter here. First, post‑quantum security is relevant to external communication, public interaction, and cross‑boundary transport. Second, internal service‑to‑service communications involved in sandbox reasoning and promotion review also require protection when they carry authority‑bearing consequences. The second point is what anchors this chapter to the internal path rather than to identity alone.

This architecture therefore treats internal security and external security as parts of one sovereignty problem. A system that secures its outer edge but leaves its internal promotion chain cryptographically weak has not preserved control over its own reasoning‑to‑authority transition.

---

## 42.10 Operational Consequences

Operationally, this chapter changes how the security layer should be discussed and evaluated. Security review should ask whether sandbox‑to‑guardian communication is protected, whether guardian‑to‑bridge handoff is protected, whether identity assertions are cryptographically trustworthy, whether authority services can detect downgrade or replay conditions, and whether compromised or non‑compliant channels prevent promotion. These are not optional hardening extras. They are requirements for the authority path itself.

This also means that fail‑closed behavior should apply when required secured channels are unavailable or invalid. If the path cannot satisfy the security‑gate conditions, promotion should not proceed.

---

## 42.11 Implementation Status (July 2026)

This section records what is verified as built, using the same demonstrated / not‑yet‑demonstrated discipline that governs the epistemic loop.

### 42.11.1 Demonstrated foundations

- Post‑quantum signing is active across all five judges in the judge pipeline. Verdict payloads are signed with a Dilithium‑family scheme before reaching the Blood‑Brain Barrier.  
- A PQ crypto initialization defect discovered in May 2026 — `primary_kem` nested inside `.tls_outbound` rather than at the expected level — was repaired across twelve proxy files by correcting the fallback path to `SAFE_FALLBACK_SUITE.get("tls_outbound", {})`. This constitutes the layer’s first completed audit‑and‑remediation cycle.  
- H\_people membership proofs use BLAKE2b with structurally enforced salt‑blindness, and `kyc_vault` isolation is enforced at the database layer via scoped roles. These are integrity and privacy controls that complement, but are not substitutes for, PQ transport.  
- Network posture provides a compensating control: services bind to loopback only, with zero non‑loopback bindings verified and `ufw` active. This narrows the practical attack surface to local compromise, but it is a perimeter property, not a cryptographic one, and does not by itself satisfy \(G_{\mathrm{security}}\).  

### 42.11.2 BBB verifier remediation (July 15, 2026)

A verification failure at the BBB was the most consequential open defect in this layer, and its resolution is recorded here in the same discipline as its discovery.

`bbb_signature_verifier.py` attempted `from dilithium_py import DilithiumPublicKey` on its first line. That import does not exist in the installed package. The failure caused `JUDGE_PK = None` on every startup, making every verdict presented to the BBB classify as `UNSIGNED_OR_FORGED_VERDICT` regardless of whether the judges signed it correctly. Signing worked; verification did not. The failure mode was fail‑closed in form but provided no discrimination between authentic and forged verdicts.

Remediation (July 15, 2026): `bbb_signature_verifier.py` was rewritten to delegate verification to the existing, working `verify_verdict` function in `judgesigner.py`, which carries the correct oqs / ML‑DSA fallback path and was already proven to work. The rewrite required no new cryptography: only the delegation path changed. The BBB was restarted, loaded the corrected file from its host‑mounted services volume, and confirmed clean startup with `JUDGESIGNER_AVAILABLE: True` and no error log entries. Five filters are operational and health status is confirmed healthy.

Two lessons belong in the permanent record:

1. A cryptographic verifier that fails at import and whose failure is masked by a `try/except` that sets the key to `None` is not a working verifier. It is a working silence. The fix closes the silence; the audit that discovered it is now part of the layer’s provenance.  
2. The services volume mount path matters: the same file exists under both `/opt/msjarvis-rebuild/msjarvis-rebuild/services/` and `/mnt/spiritual_drive/msjarvis-rebuild/services/`, and the container reads the latter. An edit to the former has no effect on the running service. The authoritative path for a live service must be recorded alongside the service definition, not assumed.  

---

## 42.12 Governed‑Belief Transport and Promotion Hardening (July 2026)

The governed‑belief infrastructure built out in Chapters 45–52 creates authority‑bearing channels that must satisfy \(G_{\mathrm{security}}\). This section describes the concrete protections in place along the WV GIS governed‑belief path.

### 42.12.1 mTLS sidecars for governed‑belief services

Three services on the WV GIS path are fronted by mutual‑TLS‑terminating sidecars:

- Chroma vector store: `jarvis-chroma-tls` → `jarvis-chroma`  
- Governed GIS RAG service: `jarvis-gis-rag-tls` → `jarvis-gis-rag`  
- Ollama embedding endpoint: `jarvis-ollama-tls` → `jarvis-ollama`  

Each sidecar:

- Presents a service‑specific certificate signed by an internal “MsJarvis Internal CA”.  
- Requires a valid client certificate on every HTTPS request.  
- Forwards only authenticated traffic to the backend service over HTTP.  

The internal CA issues:

- Server certificates for `CN=jarvis-chroma-tls`, `CN=jarvis-gis-rag-tls`, and `CN=jarvis-ollama-tls`.  
- A client certificate and key (`msjarvis-client`) used by authorized internal callers.  

From the host, calls to:

- `https://127.0.0.1:8443/api/v2/heartbeat`  
- `https://127.0.0.1:8444/health`  
- `https://127.0.0.1:11436/api/tags`  

without a client certificate complete the TLS handshake with the expected server identity but are rejected by nginx with `400 No required SSL certificate was sent`. This confirms fail‑closed client‑certificate enforcement at the transport layer.

From within the Docker network, authenticated curls using the CA certificate and client cert/key successfully reach:

- `https://jarvis-chroma-tls:8443/api/v2/heartbeat`  
- `https://jarvis-gis-rag-tls:8444/health`  
- `https://jarvis-ollama-tls:11436/api/tags`  

and receive `HTTP/1.1 200 OK` with valid JSON payloads. TLS 1.3 is negotiated with strong cipher suites and certificates chained to the internal CA. Together, these tests show that authority‑bearing calls to Chroma, GIS‑RAG, and Ollama on the WV GIS path are bound to authenticated TLS connections.

### 42.12.2 Governed GIS RAG as the belief gateway

The **Ms. Jarvis Governed GIS RAG** service (`services/gis_rag_service.py`, container `jarvis-gis-rag`) is the primary retrieval gateway for WV governed belief. It:

- Accepts structured `GISRAGRequest` payloads with query text, optional county identifiers, bounding boxes, entity type, tract GEOIDs, blockgroup GEOIDs, and optional collection names.  
- Validates West Virginia tract and blockgroup GEOIDs using strict regular expressions, rejecting malformed identifiers and constructing GEOIDs from textual patterns when appropriate.  
- Extracts semantic “band” filters from the query (for example, bridge presence, 100‑year floodplain presence, streamflow station presence, parcel intersection density) and maps them to normalized metadata values.  
- Embeds the query via Ollama using `GIS_EMBED_MODEL` (e.g. `all-minilm:latest`) and ensures embeddings match a fixed dimension (`GIS_EMBED_DIMENSION`, e.g. 384).  
- Queries Chroma collections representing WV counties, tracts, and blockgroups through two retrieval modes:
  - Exact metadata lookups on `canonical_blockgroup_id` when a 12‑digit WV blockgroup GEOID is supplied or inferred, returning hits with `retrieval_mode="exact_metadata"` and `distance=0.0`.  
  - Semantic vector queries with metadata filters when the question is more open‑ended, returning hits with `retrieval_mode="semantic_vector"` and distances.  

Collection access is tightly controlled. The service reads:

- `GIS_RAG_COLLECTIONS` (e.g. `gbimwvcountiesv2,gbimwvtractsv2,gbimwvblockgroupsv2`)  
- `GIS_RAG_CANDIDATE_COLLECTIONS` (e.g. `gbimwvblockgroupsv2governedcandidate`)  

builds `ALLOWED_COLLECTIONS`, and enforces that any `collection_names` in a request must fall within this set. Unapproved names yield a `422` error indicating that the collection is not permitted for GIS‑RAG retrieval. If, after filtering, no collections remain, a `422` error indicates that no permitted collection was selected.

Responses include collection name, document ID, retrieval mode, distance when applicable, table or layer name, canonical IDs, centroids, and full metadata. This gateway operates behind `jarvis-gis-rag-tls`, so governed retrieval is both logically constrained and protected by mutual TLS.

### 42.12.3 Publication manifest and promotion events

WV GIS publication decisions live in:

- `public.gbim_chroma_publication_manifest` (database `msjarvisgis`), with columns:
  - `logical_collection_name`  
  - `physical_collection_name`  
  - `collection_version_id` (UUID)  
  - `updated_at`  

Activating a new governed‑belief version is equivalent to inserting or updating a row in this table for a given logical collection name.

To control these changes cryptographically, the system introduces a `promotion_events` table:

```sql
CREATE TABLE IF NOT EXISTS promotion_events (
  id UUID PRIMARY KEY,
  manifest_row_id UUID NOT NULL,
  nonce BIGSERIAL NOT NULL,
  issued_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  issued_by TEXT NOT NULL,
  algorithm TEXT NOT NULL,
  public_key BYTEA NOT NULL,
  signature BYTEA NOT NULL,
  payload_sha256 TEXT,
  signature_valid BOOLEAN NOT NULL DEFAULT FALSE
);
```

Each promotion event:

- Sets `manifest_row_id` equal to the `collection_version_id` being authorized.  
- Records `issued_by`, `algorithm`, and the exact public key and signature used.  
- Stores a canonical payload hash in `payload_sha256`.  
- Is marked `signature_valid = TRUE` only after a separate verification step confirms the signature.  

A signer utility (`services/hilbert/sign_promotion_event.py`) creates a canonical JSON payload for a specified `collection_version_id`, signs it with the `msjarvis-client` key using RSASSA‑PSS‑SHA256, and outputs payload, base64‑encoded payload bytes, base64‑encoded signature, base64‑encoded certificate, and a SHA‑256 hash. A verifier utility (`services/hilbert/verify_promotion_event.py`) reads that JSON, verifies the signature against the certificate, and is used to drive updates that set `payload_sha256` and `signature_valid = TRUE` in `promotion_events`.

### 42.12.4 Database‑enforced promotion gate and WV GIS example

A Postgres trigger function now enforces that only verified promotion events can authorize changes to the GIS publication manifest:

```sql
CREATE OR REPLACE FUNCTION public.enforce_gbim_manifest_promotion()
RETURNS trigger
LANGUAGE plpgsql
AS $$
DECLARE
  manifest_id uuid;
BEGIN
  SELECT pe.manifest_row_id
  INTO manifest_id
  FROM public.promotion_events pe
  WHERE pe.manifest_row_id = NEW.collection_version_id
    AND pe.signature_valid IS TRUE
  LIMIT 1;

  IF manifest_id IS NULL THEN
    RAISE EXCEPTION 'missing verified promotion event for manifest activation (collection_version_id=%)', NEW.collection_version_id;
  END IF;

  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_enforce_gbim_manifest_promotion
ON public.gbim_chroma_publication_manifest;

CREATE TRIGGER trg_enforce_gbim_manifest_promotion
BEFORE INSERT OR UPDATE ON public.gbim_chroma_publication_manifest
FOR EACH ROW
EXECUTE FUNCTION public.enforce_gbim_manifest_promotion();
```

This trigger rejects any insert or update on `gbim_chroma_publication_manifest` unless there exists at least one row in `promotion_events` where `manifest_row_id = NEW.collection_version_id` and `signature_valid = TRUE`.

The behavior has been demonstrated concretely for the WV GIS blockgroups publication row:

- The manifest row for `logical_collection_name = 'gbim_wv_blockgroups'` has `collection_version_id = '4c6638de-274d-485c-bb64-ab078426a5a5'`.  
- With no promotion events present for this UUID, an update of the form:

  ```sql
  UPDATE public.gbim_chroma_publication_manifest
  SET physical_collection_name = physical_collection_name
  WHERE collection_version_id = '4c6638de-274d-485c-bb64-ab078426a5a5'::uuid;
  ```

  fails with:

  ```text
  ERROR:  missing verified promotion event for manifest activation (collection_version_id=4c6638de-274d-485c-bb64-ab078426a5a5)
  CONTEXT:  PL/pgSQL function enforce_gbim_manifest_promotion() line 13 at RAISE
  ```

- A signed promotion event is then generated for `4c6638de-274d-485c-bb64-ab078426a5a5` by running:

  ```text
  python3 services/hilbert/sign_promotion_event.py 4c6638de-274d-485c-bb64-ab078426a5a5 > /tmp/promotion_event_blockgroups.json
  ```

  The resulting payload includes:

  - `event_id = '57b59ac9-e5c9-4eeb-96c6-3583793f7510'`  
  - `manifest_row_id = '4c6638de-274d-485c-bb64-ab078426a5a5'`  
  - `issued_by = 'msjarvis-operator'`  
  - `algorithm = 'RSASSA-PSS-SHA256'`  

  along with base64‑encoded payload, signature, certificate, and a SHA‑256 hash.

- This event is inserted into `promotion_events` with `id = '57b59ac9-e5c9-4eeb-96c6-3583793f7510'` and later updated to set `payload_sha256` and `signature_valid = TRUE` after `verify_promotion_event.py` reports `signature-valid`.  
- Re‑running the same manifest update now succeeds and reports `UPDATE 1`.

This fail‑then‑pass sequence demonstrates that GIS publication‑manifest changes on the WV blockgroups collection are gated by the presence of a verified promotion event. The trigger enforces this gate at the database layer, independent of which application issues the write.

---

## 42.13 Remaining Surfaces and Next Steps

Several authority‑bearing surfaces related to governed belief remain to be brought under the same discipline:

- Additional governed‑belief collections beyond WV GIS that still use plain Chroma endpoints or unauthenticated internal HTTP.  
- Ingest workers and commons aggregators whose write paths can indirectly affect governed belief but which currently rely only on loopback and process‑level trust.  
- Civic intake and assertion gateways whose requests can eventually lead to manifest changes but are not yet cryptographically bound to promotion events.  

For the WV GIS path specifically, the transport and manifest layers now satisfy the security‑gate conditions described in this chapter. Work that remains is centered on:

- Adding explicit projection enforcement on role, purpose, time, and legal basis at the GIS‑RAG layer so that context, not only identity, governs which beliefs can be retrieved and how retrieved beliefs participate in promotion.  
- Extending promotion‑event and trigger patterns to any additional services that can change governed‑belief publication state.  

Documenting these surfaces makes clear where \(G_{\mathrm{security}}\) is currently satisfied and where it still needs to be applied.

---

## 42.14 Closing Statement

The Post‑Quantum Security Layer protects the integrity of the full promotion pathway in Ms. Allis. PQ‑secure communication therefore applies across sandbox, guardian, bridge, identity, and authority services — and, concretely, across the governed‑belief promotion path of intake, embedding, vector publication, and manifest promotion — because secured promotion channels are part of sovereignty‑preserving reasoning rather than merely a feature of external communications.

By making the security gate an explicit component of the broader promotion algebra, and by recording clearly which of its conditions are satisfied, which have been remediated, and which remain open, this chapter places post‑quantum security inside the governed path by which provisional reasoning becomes accepted system authority, held to the same evidentiary standard as the beliefs that path promotes.

The BBB verifier remediation of July 15 and the WV GIS mutual‑TLS plus promotion‑event enforcement of July 16 stand as concrete proofs that this evidentiary standard applies to the security layer itself. Defects that silenced authenticity checking or left promotion surfaces ungated were found, documented, fixed, and recorded. The chapter’s account of sovereignty is stronger because those failures and their corrections are part of its permanent memory rather than its forgotten history.
