# Chapter 52 — The Recurrent Epistemic Commons

## From Vector Memory to Governed Belief, Community Intelligence, and Authorized Action

Ms. Allis does not operate as a linear retrieval system.

A conventional retrieval-augmented generation pipeline moves primarily in one direction:

```text
documents
→ embeddings
→ retrieval
→ response
```

That pattern is useful, but incomplete. It can retrieve representations without governing what they mean, where they came from, when they remain valid, which entity they describe, who may access them, or whether an interpretation should become part of future system knowledge.

Ms. Allis instead implements a recurrent epistemic architecture. Source representations are projected into governed state. Governed state is resolved against identity, place, time, provenance, authority, coverage, access, and permitted use. Validated state can then be rendered as governed prose, embedded into a new semantic collection, retrieved under explicit constraints, and traced back to its authoritative relational source.

The complete intended loop is:

```text
observation
→ source representation
→ candidate belief
→ governed identity
→ validated belief
→ governed semantic memory
→ situated reasoning
→ authorized action
→ changed world
→ new observation
```

The loop is recurrent because outputs may become later inputs. It is epistemic because the system distinguishes observations, assertions, representations, inferences, uncertainties, refusals, and validated beliefs. It is a commons because the knowledge infrastructure is intended to remain accountable to the communities and places from which its meaning arises.

Recurrence alone does not make a system intelligent. An ungoverned recurrent system can amplify error, preserve fabrication, harden stereotypes, collapse uncertainty into false certainty, and convert provisional interpretations into apparent facts.

The defining property of the Ms. Allis loop is therefore not repetition.

It is governed recurrence.

---

## 52.1 The Epistemic Problem

A vector database answers a narrow but valuable question:

> Which stored representations are geometrically near this query in embedding space?

It does not, by itself, answer:

- whether the nearest representation is true;
- whether it describes the correct entity;
- whether it applies to the correct jurisdiction;
- whether it remains temporally valid;
- whether the source has authority to make the claim;
- whether zero means absence or merely missing coverage;
- whether the record has been superseded;
- whether it may be retained or disclosed;
- whether it should influence action;
- whether a generated interpretation should become future memory.

Semantic proximity proposes relevance. It does not establish truth.

This distinction is the reason the recurrent loop requires both vector memory and governed relational state. Chroma supplies semantic accessibility. PostgreSQL/PostGIS and GBIM supply identity, structure, lineage, geographic grounding, constraints, version history, and auditable promotion.

Neither layer replaces the other.

---

## 52.2 The Architectural Loop

The recurrent architecture joins:

- source vector collections;
- PostgreSQL/PostGIS;
- the GeoBelief Information Model;
- governed snapshot and publication views;
- ChromaDB;
- GIS-RAG and other retrieval services;
- toroidal and linear temporal state;
- semantic, geographic, temporal, and people Hilbert spaces;
- authorization and constitutional governance;
- observation, response, and action surfaces.

At a simplified level:

\[
C_s
\xrightarrow{\mathcal{E}}
G_c
\xrightarrow{\mathcal{P}}
G_v
\xrightarrow{\mathcal{V}}
C_g
\xrightarrow{\mathcal{R}}
Q
\xrightarrow{\mathcal{A}}
O'
\]

where:

- \(C_s\) is a source semantic collection;
- \(\mathcal{E}\) is epistemic extraction, normalization, and identity resolution;
- \(G_c\) is candidate governed state;
- \(\mathcal{P}\) is promotion, quarantine, supersession, or refusal;
- \(G_v\) is validated GBIM state;
- \(\mathcal{V}\) is governed rendering, embedding, and collection construction;
- \(C_g\) is a governed vector collection;
- \(\mathcal{R}\) is governed retrieval;
- \(Q\) is a query, synthesis, or decision context;
- \(\mathcal{A}\) is an authorized response or action;
- \(O'\) is a subsequent observation produced by interaction or a changed world.

The cycle may continue:

\[
O' \rightarrow C_s' \rightarrow G_c' \rightarrow G_v' \rightarrow C_g'
\]

This is not an uncontrolled feedback loop. Every arrow represents a state transition with entry conditions, validation rules, destination constraints, audit requirements, and refusal paths.

A retrieved item does not become a belief merely because it was retrieved. A belief does not become actionable merely because it was validated. An action does not become future knowledge merely because it occurred.

Each stage requires separate certification.

\[
\text{retrieval certification}
\neq
\text{claim certification}
\neq
\text{response certification}
\neq
\text{action authorization}
\neq
\text{memory certification}
\]

---

## 52.3 Observations, Representations, Identities, and Beliefs

The recurrent system must preserve distinctions that ordinary RAG systems often collapse.

### Observation

An observation is an event, measurement, submission, record, or detected state.

Examples include:

- a geographic feature received from an official source;
- a sensor summary;
- a community-submitted report;
- a public document;
- an administrative record;
- a retrieval result;
- the outcome of an authorized intervention.

### Representation

A representation is a physical or semantic encoding of something observed or asserted.

Examples include:

- a row in PostGIS;
- a county polygon;
- a tract polygon;
- a document;
- an embedding;
- a JSON belief document;
- a Chroma record.

A representation is not the entity itself.

### Canonical identity

A canonical identity is the stable entity to which one or more representations refer.

For example, Fayette County remains the same canonical county whether it is represented by:

- a UTM83 polygon;
- a web-map polygon;
- a second source-family polygon;
- a county GEOID;
- a governed belief document;
- a Chroma embedding.

Coordinate reference system, file format, source row, and geometry table are representation properties. They are not identity.

### Governed belief

A governed belief is a versioned epistemic state that joins an identity to evidence, provenance, place, time, coverage, authority, uncertainty, access, and permitted use.

A governed belief may be:

- provisional;
- derived;
- verified;
- disputed;
- superseded;
- quarantined;
- refused;
- expired.

The system therefore preserves the chain:

```text
observation
→ representation
→ canonical identity
→ governed belief
→ published semantic representation
```

---

## 52.4 Source Collections and Source Layers

Source vector collections and physical GIS layers are evidence surfaces. They are not automatically canonical governance.

A source may include:

- official geographic layers;
- Census boundaries;
- infrastructure datasets;
- public facilities;
- hazards;
- hydrology;
- environmental features;
- health and education resources;
- heritage records;
- community knowledge;
- organizational documents;
- sensor summaries;
- public submissions.

Each source collection and representation should possess stable identifiers and content-derived hashes.

For a collection:

\[
h_C =
H(
\text{collection identity}
\parallel
\text{embedding model}
\parallel
\text{schema version}
\parallel
\text{source manifest}
)
\]

For a physical feature representation:

\[
h_F =
H(
\text{table identity}
\parallel
\text{source feature identity}
\parallel
\text{canonical entity identity}
\parallel
\text{normalized geometry}
\parallel
\text{relevant source attributes}
)
\]

For a governed belief:

\[
h_B =
H(
\operatorname{CanonicalJSON}(
\text{belief document}
)
)
\]

These hashes do not prove truth. They establish integrity, lineage, stable comparison, and change detection.

They allow the system to ask:

- Is this the same physical representation previously governed?
- Has its geometry changed?
- Has its source identity changed?
- Has the governed belief changed?
- Does a vector record correspond to the current belief snapshot?
- Must the representation be revalidated or re-embedded?

The source surface answers:

> What representation was received or retrieved?

GBIM answers:

> What entity does it describe, and what is its governed epistemic status?

---

## 52.5 GBIM as the Governed System of Record

GBIM is the GeoBelief Information Model: the governed state layer in which semantic content is joined to identity, provenance, geography, time, authority, confidence, coverage, access, retention, and permitted use.

A governed belief may be represented as:

\[
b_i =
(
u_i,
e_i,
\tau_i,
\gamma_i,
\pi_i,
\sigma_i,
\kappa_i,
\alpha_i,
\omega_i
)
\]

where:

- \(u_i\) is stable identity;
- \(e_i\) is semantic content or a reference to it;
- \(\tau_i\) is temporal state;
- \(\gamma_i\) is geographic state;
- \(\pi_i\) is provenance;
- \(\sigma_i\) is epistemic status;
- \(\kappa_i\) is confidence and uncertainty;
- \(\alpha_i\) is authority and access state;
- \(\omega_i\) is governance, retention, consent, and permitted-use state.

These are not incidental metadata fields surrounding an embedding. Together, they constitute the governed meaning of the record.

Chroma is not the sole system of record. It is optimized for semantic search, not for relational integrity, foreign-key enforcement, version history, spatial computation, transactional updates, or authoritative identity management.

PostgreSQL/PostGIS provides the durable relational and geographic body of GBIM.

---

## 52.6 Identity and Representation as Separate Surfaces

The West Virginia implementation demonstrates the distinction between canonical identity and physical representation.

For counties:

```text
55 canonical county identities
220 physical county representations
4 representations per county
```

The four boundary representations occupy two source families and two spatial-reference forms. Each remains traceable to:

- its physical table;
- its source feature ID;
- its canonical county;
- its source name;
- its normalized geometry hash.

The canonical county is not duplicated merely because four physical polygons exist.

For tracts:

```text
546 canonical tract identities
546 governed physical tract representations
1 current registered representation per tract
```

The tract bridge originally contained 1,092 rows because two incompatible forms of tract identity had been registered:

```text
54019020101
1400000US54019020101
```

Only the fully qualified canonical identity belonged to the governed identity surface. The 546 short-form orphan mappings were removed, leaving a one-to-one bridge between physical tract features and canonical tract identities.

This repair illustrates an important recurrent rule:

> Duplicate representations must not be mistaken for duplicate entities, and alternate identifier formats must not be mistaken for separate canonical identities.

---

## 52.7 Geographic Identity and Geometry

Geographic identity is not reducible to geometry, but geometry materially constrains geographic meaning.

A county may have multiple polygon representations, yet retain one canonical identity. A tract may be represented in UTM83 or another coordinate system, yet retain one Census GEOID. A place name without spatial scope may remain ambiguous even when its semantic embedding appears highly relevant.

The geographic state of a belief may include:

- canonical geographic identifier;
- source geometry;
- source spatial reference;
- normalized geometry;
- centroid;
- bounding box;
- jurisdiction;
- spatial grain;
- containment relationships;
- adjacency;
- intersection;
- distance;
- source authority.

PostGIS remains the authoritative location for polygon geometry and spatial computation. Raw polygons are not inserted into the text presented for embedding. Instead, the governed vector metadata carries scalar spatial descriptors and reverse links to the physical representation.

This preserves the division of labor:

```text
PostGIS:
  authoritative geometry
  spatial relationships
  containment and intersection
  coordinate transformations
  feature-level provenance

Chroma:
  semantic representation
  similarity retrieval
  governed textual memory
  scalar filtering metadata
```

Meaning does not collapse into geometry. But geographic meaning cannot be governed honestly while ignoring geometry.

---

## 52.8 Coverage Is an Epistemic State

A count of zero is not automatically a geographic fact.

It may mean:

- verified absence;
- no source records intersected the entity;
- the source has not been loaded;
- the layer has incomplete jurisdictional coverage;
- identity resolution failed;
- the spatial join has not been performed;
- the source is temporally stale;
- access restrictions prevented evaluation;
- the data remains under investigation.

Therefore:

\[
0_{\text{unknown}}
\neq
0_{\text{verified absent}}
\]

The West Virginia county and tract slices preserve this distinction through explicit coverage records.

County coverage currently contains:

```text
55 counties × 5 dataset types = 275 rows
```

Tract coverage contains:

```text
546 tracts × 3 dataset types = 1,638 rows
```

Coverage records include:

- canonical entity identity;
- parent county identity where applicable;
- dataset type;
- source table;
- feature count;
- coverage state;
- calculation time;
- source-layer hash;
- notes.

The vector-ready prose carries this distinction into semantic retrieval. A tract with zero address points and `coverage_state = unknown` states that the count must not be interpreted as verified absence.

This is not merely cautious wording. It prevents semantic memory from converting a pipeline gap into a claim about the world.

---

## 52.9 Versioned Belief Snapshots

Governed state is versioned rather than overwritten.

The authoritative West Virginia governance database is:

```text
Database: msjarvisgis_v2
Host:     localhost
Port:     5436
```

Its core governed relations currently contain:

```text
Relation                        Rows
-------------------------------------
wv_layer_categories             254
wv_entity_registry               65
wv_county_identity               55
wv_county_representation        220
wv_county_dataset_coverage      275
wv_county_belief_snapshot       110
wv_tract_identity               546
wv_tract_representation         546
wv_tract_dataset_coverage     1,638
wv_tract_belief_snapshot      1,092
```

The snapshot totals preserve two versions:

```text
County snapshots:
  55 v1 + 55 v2 = 110

Tract snapshots:
  546 v1 + 546 v2 = 1,092
```

The v1 tract snapshots preserve the earlier unresolved county state. The v2 snapshots preserve the reconciled canonical county relationships and corrected representation lineage.

This historical retention matters. If v2 simply replaced v1, the system would preserve the answer but lose the epistemic history of how the answer changed.

A belief snapshot therefore records not only what the system currently believes, but which governed state existed at a particular version.

---

## 52.10 Vector-Ready Publication Views

Snapshot tables are durable history. They are not automatically the active semantic publication surface.

The current West Virginia v2 publication is expressed through:

```text
wv_county_belief_vector_ready
wv_tract_belief_vector_ready
```

These views select and render the current governed snapshot state.

Their validated cardinalities are:

```text
wv_county_belief_vector_ready:
  55 rows
  55 distinct document_id values

wv_tract_belief_vector_ready:
  546 rows
  546 distinct document_id values
```

Each published document contains:

- governed prose;
- canonical entity identity;
- county or tract GEOID;
- parent county identity where applicable;
- entity type;
- snapshot version;
- belief hash;
- source feature hash;
- source table;
- source feature ID;
- authority class;
- access class;
- verification state;
- spatial-reference identifier;
- centroid coordinates;
- bounding-box coordinates;
- coverage language.

The belief hash functions as the stable vector document ID:

\[
\text{document\_id} = h_B
\]

This creates a reversible path:

```text
Chroma document ID
→ belief hash
→ snapshot row
→ canonical identity
→ representation bridge
→ physical PostGIS feature
→ source geometry and provenance
```

That path is the core of governed retrieval.

---

## 52.11 Governed Chroma Collections

The v2 publication views were embedded using:

```text
Embedding model: all-minilm:latest
Dimension:       384
```

They were published as:

```text
gbim_wv_counties_v2
gbim_wv_tracts_v2
```

The validated collection cardinalities are:

```text
gbim_wv_counties_v2: 55 documents
gbim_wv_tracts_v2:  546 documents
```

Publication validation established:

- PostgreSQL row count equals Chroma record count;
- every expected document ID is present;
- no unexpected document IDs are present;
- belief hashes are distinct within each publication;
- county and tract snapshot versions are represented in metadata;
- canonical identities remain available as filters;
- coverage semantics remain present in the embedded prose.

The collections were then entered into a publication manifest and promoted as the active physical collections for their logical county and tract collection names.

A governed collection is therefore not merely a bag of embeddings. It is a versioned materialization of a defined relational view under a declared rendering version, embedding model, dimensionality, record count, and collection hash.

---

## 52.12 Governed Retrieval Through GIS-RAG

The governed collections are exposed through the GIS-RAG service.

The current application-level service version is:

```text
GIS-RAG 0.4.1
```

This number identifies the GIS-RAG application implementation. It is not the Chroma client-library version.

GIS-RAG 0.4.1:

- queries both governed v2 collections;
- resolves collections by governed name;
- applies canonical county filters;
- maps tract requests to `entity_type = census_tract`;
- supports exact `tract_geoid` filtering;
- returns collection name, document ID, distance, governed text, and metadata;
- preserves belief hashes and source feature hashes;
- returns snapshot and verification state;
- preserves the unknown-coverage warning.

An exact tract request for:

```text
Tract GEOID: 54019020101
County GEOID: 54019
County: Fayette
```

returned:

- the correct record from `gbim_wv_tracts_v2`;
- the correct canonical tract identity;
- the correct Fayette County parent;
- the v2 snapshot version;
- the matching belief hash and document ID;
- the physical source feature hash;
- the source table and feature ID;
- the governed statement that zero with unknown coverage is not verified absence.

This proves the path:

```text
API request
→ constrained governed collection
→ exact tract retrieval
→ belief hash
→ governed snapshot
→ canonical identity
→ physical representation
```

The county collection has also been published and directly retrieval-tested. Final application-level county acceptance should be retained as a separate regression test so that both entity paths remain continuously certified.

---

## 52.13 What Has Been Demonstrated

The completed West Virginia county-and-tract vertical slice demonstrates:

1. canonical geographic identity;
2. multiple physical representations per canonical county;
3. canonical tract-to-county relationships;
4. deterministic representation hashing;
5. explicit dataset coverage state;
6. preservation of unknown rather than false absence;
7. versioned belief snapshots;
8. belief-document hashing;
9. vector-ready governed prose;
10. deterministic Chroma document identity;
11. publication manifests;
12. versioned collection promotion;
13. semantic retrieval with canonical metadata filters;
14. reverse traceability from vector result to PostGIS representation;
15. recovery of the governed state from a damaged deployment context;
16. reproducible database dumps and integrity hashes.

This is more than a diagram of a recurrent epistemic loop. It is an operational demonstration of the central transition:

\[
G_v \rightarrow C_g \rightarrow \mathcal{R}(Q)
\]

for two canonical geographic entity types.

---

## 52.14 What Has Not Yet Been Demonstrated

The vertical slice does not establish that every part of the complete recurrent architecture is finished.

It does not yet prove, across the whole system:

- automatic promotion of arbitrary observations into governed beliefs;
- automated contradiction adjudication;
- belief decay across all domains;
- constitutional authorization of consequential real-world actions;
- complete toroidal-time integration for county and tract beliefs;
- automatic ingestion of every downloaded WVGISTC dataset;
- full geographic coverage for address points, D-FIRM, infrastructure, hazards, heritage, health, education, or environmental data;
- a completed observation-action-observation cycle in which an authorized intervention changes the world and is then independently re-observed;
- national replication across all intended jurisdictions.

The completed slice closes the governed memory and retrieval portion of the loop. It establishes the machinery required for recurrence. It does not justify claiming that every downstream action and re-observation pathway is complete.

That distinction is essential. A governed epistemic system must describe its own implementation state truthfully.

---

## 52.15 Recovery as an Epistemic Event

The implementation itself demonstrated why provenance and governance matter.

During development, similar database names, multiple PostgreSQL instances, a damaged Docker database, a native PostgreSQL cluster, copied governance tables, and temporary reconstruction databases created ambiguity about which state was authoritative.

The system had to determine:

- which server was actually listening;
- which database contained physical layers;
- which database contained governed state;
- which relation names were authoritative;
- which representations pointed to valid physical features;
- which bridge rows were orphaned;
- which snapshots represented v1 versus v2;
- which database could be dumped and restored;
- which vector collections corresponded to which relational publication.

The authoritative database was resolved as:

```text
msjarvisgis_v2
```

A temporary similarly named database without the underscore was inspected and removed after it was shown to be redundant and incomplete.

This was not merely operational housekeeping. It was an epistemic process: competing claims about system state were tested against physical evidence, constraints, counts, hashes, foreign relationships, and reproducibility.

The recovery therefore instantiated the chapter’s central principle:

> A representation of system state is not authoritative merely because it exists. Authority must be established through governed identity, evidence, validation, and reproducibility.

---

## 52.16 The Remaining WVGISTC Ingestion Frontier

The files in `/home/cakidd/Downloads/files` remain an important source inventory, but the directory must not be treated as a simple queue in which every archive is blindly imported.

The directory contains:

- layers already represented in PostgreSQL;
- alternate coordinate-system versions of the same source;
- duplicated downloads marked with suffixes such as `(1)` and `(2)`;
- older and newer editions of similar datasets;
- shapefiles;
- file geodatabases;
- E00 archives;
- rasters and SID imagery;
- CSV and TSV attribute files;
- address-point directories;
- archives with uncertain or missing projections;
- source families with spelling inconsistencies;
- supporting files that may not contain geometry.

Examples include:

- county and tract boundaries;
- block groups and ZCTAs;
- address points and building footprints;
- roads, bridges, rail, and intermodal facilities;
- hospitals, health departments, nursing homes, and education facilities;
- dams, high-water marks, flood-risk layers, and stream gauges;
- public lands, wildlife resources, fisheries, and watersheds;
- mines, geology, mineral operations, and abandoned mine lands;
- historic properties and heritage resources;
- communications towers and public-safety facilities;
- Census population and community layers.

Some of these source families already appear as physical tables in `msjarvisgis_v2`. Others have not yet been ingested, reconciled, governed, or joined to canonical entities.

Therefore, the correct statement is:

> The remaining downloads must be reconciled against the governed catalog and physical database, and only missing or materially different source representations should be ingested.

File presence in `Downloads` does not prove absence from PostgreSQL. Likewise, a similarly named PostgreSQL table does not prove that the exact archive, edition, projection, or source version has already been governed.

---

## 52.17 Controlled Source-Ingestion Protocol

Each remaining archive should pass through a governed intake process.

### Phase 1 — Inventory

For each archive, record:

- archive filename;
- file size;
- SHA-256 hash;
- modification time;
- internal layer names;
- format;
- geometry type;
- declared or detected CRS;
- source organization;
- publication or temporal date;
- apparent jurisdiction;
- apparent spatial grain.

### Phase 2 — Duplicate and representation analysis

Compare the archive with:

- `wv_layer_categories`;
- PostGIS relation names;
- existing source-layer hashes;
- geometry metadata;
- prior archive hashes;
- source version and date;
- alternate coordinate representations.

Classify each archive as:

```text
already represented
duplicate download
alternate CRS representation
new source version
new physical layer
attribute-only supplement
raster or imagery
projection unresolved
quarantine required
```

### Phase 3 — Staged import

New layers should enter a staging schema or controlled import transaction rather than immediately becoming authoritative public relations.

The import should preserve:

- the original source filename;
- archive hash;
- source layer name;
- unmodified source attributes;
- original CRS;
- import time;
- import tool and version;
- row count;
- geometry count;
- invalid geometry count.

### Phase 4 — Geometry validation

Validate:

- geometry type;
- spatial reference;
- empty geometries;
- invalid geometries;
- duplicate geometries;
- geographic extent;
- state or county containment;
- coordinate plausibility;
- transformation behavior.

A layer with an unknown or unreliable projection must not be silently assigned one.

### Phase 5 — Catalog registration

Only after physical validation should the layer be registered in `wv_layer_categories` with:

- category;
- description;
- source system;
- jurisdiction;
- geometry type;
- SRID;
- spatial grain;
- temporal coverage;
- authority class;
- access class;
- update time.

### Phase 6 — Provenance and representation registration

Where the layer represents canonical entities, create or update:

- entity registry mappings;
- representation bridges;
- deterministic feature hashes;
- canonical county or tract relationships;
- provenance state;
- permitted use;
- confidence and verification state.

Not every layer requires a new canonical identity table. Some layers are evidence, coverage, observations, or infrastructure features associated with existing identities.

### Phase 7 — Coverage computation

Recompute coverage only after:

- identity resolution;
- geometry validation;
- source registration;
- spatial joins;
- provenance classification.

A newly imported address-point or flood layer may convert coverage from `unknown` to `present`, but it must not silently convert unknown zeroes into verified absence.

### Phase 8 — Snapshot regeneration

If the new source changes governed belief state:

1. create a new snapshot version;
2. retain prior snapshots;
3. calculate new belief hashes;
4. render new vector-ready documents;
5. compare old and new belief hashes;
6. publish a new governed collection version;
7. validate ID sets and record counts;
8. promote only after acceptance tests pass.

This protocol extends the recurrent loop from the completed county-and-tract spine to the remaining geographic evidence layers.

---

## 52.18 Contradiction, Supersession, and Decay

A recurrent epistemic system must govern disagreement over time.

Suppose two sources make conflicting claims about the same entity:

\[
c_1 \neq c_2
\]

The system must not resolve the conflict by selecting whichever embedding is nearest to the current query.

Conflict resolution may consider:

- source authority;
- temporal recency;
- jurisdiction;
- measurement method;
- provenance completeness;
- direct observation versus inference;
- spatial precision;
- declared uncertainty;
- statutory or administrative authority;
- community validation;
- prior supersession rules.

A later claim does not automatically erase an earlier claim. It may:

- supersede it;
- narrow its valid interval;
- dispute it;
- coexist under a different jurisdiction;
- remain unresolved;
- trigger quarantine.

Temporal validity can be represented as:

\[
b_i(t) \in
\{
\text{current},
\text{stale},
\text{superseded},
\text{expired},
\text{disputed}
\}
\]

Decay is not deletion. It is a governed reduction in current applicability or confidence while preserving the historical record.

---

## 52.19 Toroidal Time and Recurrent State

Linear time answers:

> When did this event occur?

Toroidal time additionally asks:

> In what recurring civic, ecological, organizational, or seasonal phase did it occur?

A belief may therefore possess both:

\[
\tau_i =
(
t_{\text{linear}},
\theta_{\text{daily}},
\theta_{\text{weekly}},
\theta_{\text{seasonal}},
\theta_{\text{civic}},
\theta_{\text{project}}
)
\]

This supports distinctions such as:

- a stream condition measured during flood season;
- a public facility available only during operating hours;
- a heritage event recurring annually;
- a grant obligation active during a reporting cycle;
- a road condition that reappears under seasonal weather;
- a community need that recurs without belonging to the same individual.

The current county-and-tract vertical slice establishes versioned time through snapshot history. Full toroidal recurrence remains an extension of the slice rather than a completed property of every county and tract belief.

---

## 52.20 Hilbert-State Interpretation

The recurrent epistemic commons operates across several representational spaces:

\[
\mathcal{H}_{\text{semantic}}
\otimes
\mathcal{H}_{\text{geo}}
\otimes
\mathcal{H}_{\text{time}}
\otimes
\mathcal{H}_{\text{people}}
\]

where:

- \(\mathcal{H}_{\text{semantic}}\) represents semantic similarity;
- \(\mathcal{H}_{\text{geo}}\) represents place and spatial relationship;
- \(\mathcal{H}_{\text{time}}\) represents linear and recurrent temporal state;
- \(\mathcal{H}_{\text{people}}\) represents governed relationships to people, roles, consent, and public accountability.

A query is not interpreted solely as a vector in semantic space. It is situated through constrained projections across these spaces.

Conceptually:

\[
q^*
=
\Pi_{\text{authority}}
\Pi_{\text{access}}
\Pi_{\text{time}}
\Pi_{\text{geo}}
q
\]

The projections restrict the eligible retrieval domain before or during semantic ranking.

This is the operational meaning of governed similarity: semantic distance is evaluated inside an admissible domain rather than across an undifferentiated memory surface.

---

## 52.21 Community Intelligence Without Surveillance

The recurrent commons is designed to increase shared knowledge without requiring increased exposure of individuals.

Its moral invariant is:

\[
\Delta K_{\text{community}} > 0
\]

while:

\[
\Delta E_{\text{individual}} \leq 0
\]

where:

- \(\Delta K_{\text{community}}\) is the change in useful shared knowledge;
- \(\Delta E_{\text{individual}}\) is the change in unnecessary personal exposure.

This requires:

- data minimization;
- separation of KYC identity from pseudonymous participation;
- public identity only by affirmative choice or legitimate public-accountability rule;
- aggregation where individual detail is unnecessary;
- purpose limitation;
- retention controls;
- access classification;
- provenance without indiscriminate personal tracking;
- refusal where a query would convert community infrastructure into surveillance.

The system should be able to learn:

- that a service gap exists;
- that a road corridor is repeatedly inaccessible;
- that a community resource is underused;
- that a hazard affects a geographic area;
- that a program produces public benefit;

without automatically learning or exposing the private identity of every person involved.

The commons governs relationships between knowledge, place, and public purpose. It is not a mechanism for total observation.

---

## 52.22 Authority, Access, and Permitted Use

A record’s presence in the governed system does not imply universal availability or unrestricted use.

A governed record may include:

```text
authority_class
access_class
verification_state
retention_class
permitted_use
consent_state
jurisdiction
valid_from
valid_to
```

Retrieval eligibility is therefore conditional:

\[
\operatorname{Eligible}(b,q,u)
\iff
A_b(q)
\land
X_b(u)
\land
P_b(q)
\land
T_b(q)
\land
G_b(q)
\]

where:

- \(A_b(q)\) is authority applicability;
- \(X_b(u)\) is access eligibility for user or service \(u\);
- \(P_b(q)\) is permitted-use compatibility;
- \(T_b(q)\) is temporal compatibility;
- \(G_b(q)\) is geographic compatibility.

A semantically relevant record may still be excluded because it is:

- outside the requested jurisdiction;
- temporally invalid;
- insufficiently verified;
- restricted;
- prohibited for the requested purpose;
- derived from a source lacking authority;
- unsafe to disclose;
- under unresolved contradiction.

Refusal is therefore an epistemic output, not merely an application error.

---

## 52.23 Scaling the Pattern Beyond West Virginia

West Virginia is the first completed county-and-tract implementation of this pattern. It should be treated as a reusable governed vertical slice, not as a template for blind duplication.

For each additional region:

1. identify authoritative geographic identities;
2. inventory physical representations;
3. preserve source-specific geometry and provenance;
4. establish canonical identity bridges;
5. define coverage states;
6. build versioned belief snapshots;
7. render governed vector-ready documents;
8. publish versioned collections;
9. validate relational and vector ID equality;
10. test reverse traceability;
11. configure governed retrieval;
12. retain refusal and unknown states;
13. document what has and has not been demonstrated.

Suggested naming patterns may include:

```text
gbim_{region}_counties_vN
gbim_{region}_tracts_vN
gbim_{region}_places_vN
gbim_{region}_infrastructure_vN
gbim_{region}_hazards_vN
gbim_{region}_heritage_vN
```

The naming convention is less important than preserving:

- canonical identity;
- snapshot version;
- source lineage;
- rendering version;
- embedding model;
- document hash;
- collection hash;
- validation status;
- promotion status.

---

## 52.24 Acceptance Tests for a Governed Vertical Slice

A governed publication should not be promoted merely because an ingestion script completed.

Minimum acceptance tests include:

### Relational integrity

- expected identity count;
- expected representation count;
- zero identity orphans;
- zero physical feature orphans;
- zero unbridged governed features;
- correct foreign-key relationships;
- correct parent geography;
- valid canonical identifiers.

### Hash integrity

- every governed representation has a hash;
- hashes are deterministic under unchanged inputs;
- expected distinctness is maintained;
- belief documents have stable canonical hashes;
- collection manifests have stable content identities.

### Coverage integrity

- every expected entity/dataset pair has a coverage record;
- unknown remains distinct from verified absence;
- parent geography is resolved where required;
- source-table identity is present;
- coverage recalculation is versioned.

### Snapshot integrity

- one snapshot per entity per version;
- prior versions remain available;
- belief hashes are populated;
- snapshot documents contain canonical identity and coverage state;
- current views select the intended version.

### Vector-publication integrity

- view row count equals collection count;
- relational document-ID set equals vector document-ID set;
- no missing IDs;
- no unexpected IDs;
- embedding dimensionality matches the declared model;
- metadata uses scalar, filterable fields;
- collection manifest records validation and promotion.

### Retrieval integrity

- exact county retrieval;
- exact tract retrieval;
- parent-child geographic consistency;
- belief-hash reverse trace;
- correct snapshot version;
- correct source feature hash;
- preservation of unknown-coverage language;
- refusal or empty result for incompatible filters.

### Recovery integrity

- successful database dump;
- successful dump listing or test restore;
- source and deployment configuration hashes;
- reproducible container build;
- pinned dependency versions;
- documented active collection mapping.

---

## 52.25 Operational Status of the West Virginia Slice

As of the current implementation checkpoint:

### Demonstrated

- authoritative governance database resolved;
- county and tract identities established;
- physical representations reconciled;
- deterministic representation hashes populated;
- county and tract coverage tables populated;
- v1 and v2 snapshots retained;
- v2 vector-ready views validated;
- governed Chroma collections published;
- collection counts and IDs verified;
- active collection mappings recorded;
- exact tract retrieval demonstrated through GIS-RAG 0.4.1;
- reverse trace from Chroma document to governed belief demonstrated;
- unknown-coverage semantics preserved;
- database dumps and SHA-256 checkpoints created.

### Pending final operational closure

- retain a machine-readable county endpoint acceptance result alongside the tract test;
- pin and record compatible GIS-RAG/Chroma client dependencies;
- preserve the final GIS-RAG image and source hashes;
- reconcile the Downloads inventory against the physical and governance catalogs;
- ingest only missing or materially changed layers;
- recompute coverage and create later snapshot versions as new governed evidence enters the system.

The epistemic spine is complete. The evidence surface is still expanding.

---

## 52.26 The Moral Center of Recurrence

The recurrent loop exists to serve human and community flourishing, not to maximize data accumulation.

A system that remembers everything without governing purpose becomes a surveillance archive. A system that repeats its own outputs without checking them becomes an error amplifier. A system that retrieves semantically similar text without place, time, authority, and provenance becomes persuasive but unreliable.

The recurrent epistemic commons therefore imposes a moral ordering:

```text
human dignity
before data completeness

community benefit
before extraction

truthful uncertainty
before apparent confidence

governed identity
before convenient aggregation

provenance
before repetition

authorization
before action

public knowledge
without unnecessary personal exposure
```

Its purpose is not to know everything about everyone.

Its purpose is to help communities know enough—accurately, accountably, and safely—to act together.

---

## 52.27 The Complete Intended Loop

The full architecture can be summarized as:

```text
world
→ observation
→ source representation
→ source hash
→ candidate identity
→ canonical entity resolution
→ representation bridge
→ coverage evaluation
→ candidate belief
→ validation, quarantine, supersession, or refusal
→ versioned governed snapshot
→ belief hash
→ vector-ready governed prose
→ governed collection manifest
→ embedding and publication
→ governed retrieval
→ situated reasoning
→ authorization or refusal
→ response or action
→ changed world
→ new observation
```

The West Virginia county-and-tract implementation now occupies a concrete segment of this loop:

```text
official geographic source
→ PostGIS representation
→ canonical county or tract
→ governed coverage
→ versioned belief snapshot
→ vector-ready document
→ governed Chroma collection
→ GIS-RAG retrieval
→ reverse trace to governed source
```

That completed segment matters because it transforms the recurrent epistemic commons from a purely architectural proposition into a working governed information pathway.

The remaining work is not to invent the loop again. It is to extend the loop carefully:

- from counties and tracts to additional entities;
- from current coverage states to newly ingested evidence;
- from governed retrieval to more complete situated reasoning;
- from reasoning to constitutionally authorized action;
- from action to independently observed outcomes;
- from West Virginia to other communities without abandoning local sovereignty.

---

## 52.28 Conclusion

Ms. Allis is not defined by the presence of a vector database, a large language model, a GIS database, or a collection of microservices.

She is defined by the governed relationships among them.

Vector memory provides semantic reach. PostGIS provides geographic grounding. Canonical identities prevent representations from fragmenting the world into disconnected rows. Coverage states prevent ignorance from masquerading as absence. Versioned snapshots preserve the history of belief. Hashes preserve lineage. Governed collections return validated state to semantic memory. GIS-RAG makes that state retrievable under place-aware constraints. Constitutional governance determines whether retrieval may become response, memory, or action.

The resulting architecture is recurrent, but not self-certifying. It is adaptive, but not unbounded. It remembers, but does not treat memory as truth. It reasons, but preserves refusal. It serves a commons, but does not require surveillance.

The core principle is simple:

> The system may learn from its own operation only when it can preserve the distinction between what was observed, what was represented, what was inferred, what was validated, what remains unknown, and what the community has authorized it to do.

# West Virginia GIS Corpus – GBIM Manifest Overview

This document describes the West Virginia (WV) GIS corpus as captured in the GBIM checkpoint, and explains how the manifests relate raw source files to published tables and governance surfaces.

It assumes the following files exist in this directory:

- `msjarvisgis_v2-final.dump` – GBIM database dump.
- `wv_source_files_manifest.csv` – inventory of source GIS files.
- `wv_source_manifest_layers.csv` – dataset‑level source→table manifest.
- `wv_derived_governance_tables.csv` – governance/derived/internal tables manifest.

***

## 1. Purpose and Scope

This corpus represents a curated, production‑grade set of West Virginia GIS datasets designed for:

- Spatial analytics and mapping.
- RAG (retrieval‑augmented generation) over geospatial content.
- Governance and data lineage tracking inside GBIM.

The manifests are intended to answer two core questions:

1. For a given `public.wv_*` table, which source file(s) define it?
2. For a given source ZIP/GDB/shapefile, which GBIM table(s) depend on it?

Governance and identity tables that have no single source file are documented separately.

***

## 2. File Roles

### 2.1 `msjarvisgis_v2-final.dump`

- PostgreSQL/GBIM dump containing:
  - All `public.wv_*` tables.
  - Governance, identity, coverage, belief, and vector‑ready views.
- Serves as the authoritative schema and data snapshot for this checkpoint.

You should restore this dump into a GBIM‑compatible PostgreSQL instance before using the manifests for automated ETL or RAG indexing.

### 2.2 `wv_source_files_manifest.csv`

High‑level inventory of raw GIS assets originally under:

- `/home/cakidd/Downloads/files`

Columns (typical):

- `filename` – Source dataset file name (ZIP, GDB, SHP bundle, etc.).
- `path` – Relative or absolute path at time of collection.
- `provider` – Data steward or origin agency (e.g., WVDOT, USGS, NPS, WVDEP).
- `crs` – Coordinate reference system (e.g., UTM83, GCS83, WMA84).
- Optional metadata columns for notes, acquisition date, or category.

This file is the “file‑side checklist” and is used to ensure every relevant GIS dataset has either a mapping in `wv_source_manifest_layers.csv` or an explicit exclusion/variant note in governance metadata.

### 2.3 `wv_source_manifest_layers.csv`

Dataset‑level manifest mapping source files to GBIM tables and semantic roles.

Typical columns:

1. `layer_label`  
   - Human‑readable name for the dataset.  
   - Example: `Roads Interstates WVDOT/SAMB 2009`, `Watershed Boundary HU12 NRCS 2009`.

2. `source_filename`  
   - Exact filename of the GIS source in `wv_source_files_manifest.csv`.  
   - Example: `roadsInterstates_WVDOTAndSAMB_200910_utm83_shp.zip`.

3. `provider`  
   - Agency or organization providing the data.  
   - Example: `WVDOT/SAMB`, `USGS`, `NRCS`, `WVDNR`, `WVGES`, `USACE`.

4. `crs`  
   - Coordinate reference system used in the source dataset.  
   - Example: `UTM83`, `GCS83`, `WMA84`.

5. `gbim_table`  
   - GBIM table name (including schema), usually `public.wv_*`.  
   - Example: `public.wv_trn_roads_interstate`, `public.wv_hyd_watershed_boundary_12digit_hu`.

6. `role`  
   - Semantic description of the geometry/feature role in the GBIM model.  
   - Example: `interstate_road_lines`, `watershed_boundary_hu12_polygons`, `airport_facility_points`.

This manifest:

- Covers nearly all core datasets in the WV corpus:
  - Boundaries (counties, voting districts, workforce areas, public lands).
  - Hydrology (streams, dams, watershed boundaries).
  - Transportation (roads, railroads, trails, airports, intermodal terminals).
  - Public lands and recreation (national forests, state parks, wilderness, recreation sites).
  - Environmental and energy (coal fields, wind energy, air nonattainment, abandoned mine lands).
  - Social and facilities (schools, hospitals, higher ed, libraries, VA facilities).
  - Structures (bridges, correctional institutions, at‑risk structures, building points/polygons).
  - Locations and demographics (urbanized areas, populated places, ZCTAs, blockgroups, tracts).
- Ensures every dataset‑like `public.wv_*` table that corresponds to a real GIS source file has:
  - A unique manifest row.
  - A clear CRS.
  - A data steward/provider.
  - A semantic role label.

### 2.4 `wv_derived_governance_tables.csv`

Manifest for tables that do *not* have a single defining source GIS file and instead serve governance, identity, coverage, or derived roles in GBIM.

Columns:

1. `table_name`  
   - GBIM table name (no schema prefix, e.g. `wv_county_identity`).

2. `category`  
   - Governance classification, such as:
     - `governance_identity`
     - `governance_coverage`
     - `governance_belief_snapshot`
     - `governance_view`
     - `governance_summary`
     - `governance_boundary_union`
     - `governance_boundary_variant`
     - `governance_layer_catalog`
     - `governance_entity_registry`
     - `governance_structure_view`
     - `governance_transport_view`
     - `governance_boundary_base`

3. `notes`  
   - Free‑text explanation of how the table is derived and what it represents.  
   - Example:
     - Identity: “county identity keyed by canonical IDs and GEOIDs, derived from boundary + registry”.
     - Coverage: “tract dataset coverage table, derived from multiple source layers”.
     - Belief: “county belief snapshots v1+v2, internal governance history”.
     - Vector‑ready view: “vector‑ready v2 county publication surface, derived from snapshots”.
     - Registry/catalog: “canonical GBIM entity registry, derived from many datasets”; “internal GBIM layer taxonomy, no single source ZIP”.
     - Boundary variant: “WMA84 variant of county boundaries 24k topo updated 2026, alternative CRS for UTM83 base”.
     - Transport/structure views: “airport facility GBIM view, derived from FAA/WVDOT airports datasets”; “SAMB building polygons GBIM view, derived from WVDOT/SAMB building dataset”.

This file intentionally captures the remaining `public.wv_*` tables that:

- Aggregate or union multiple physical datasets.
- Encode governance logic, identity keys, and belief or publication‑ready views.
- Represent CRS variants and internal catalog/registry surfaces.

These tables are vital for GBIM’s data governance but are not “single‑source GIS layers” in the same way as the shapefile/GDB datasets in `wv_source_manifest_layers.csv`.

***

## 3. Completed Mapping State

At this checkpoint:

- All GIS dataset tables in `public.wv_*` that correspond to real, external source files are mapped in `wv_source_manifest_layers.csv`.
- The only `public.wv_*` tables without source mappings are:
  - Identity tables (`wv_county_identity`, `wv_tract_identity`).
  - Coverage tables (`wv_county_dataset_coverage`, `wv_tract_dataset_coverage`).
  - Belief snapshot tables (`wv_county_belief_snapshot`, `wv_tract_belief_snapshot`).
  - Representation tables (`wv_county_representation`, `wv_county_representation_pre_gid_rebind`, `wv_tract_representation`, `wv_tract_representation_pre_gid_rebind`).
  - Registry and catalog tables (`wv_entity_registry`, `wv_layer_categories`).
  - Boundary base and variants (`wv_wv_county_boundaries_24k_topo_updated_2026_utm83`, `wv_wv_county_boundaries_24k_topo_updated_2026_wma84`, and related GDB/variant tables).

These are all:

- **Governance/derived tables** documented in `wv_derived_governance_tables.csv`.
- Known to be built from multiple datasets or as internal GBIM views, not from a single shapefile/ZIP.

As a result, the WV corpus is “manifest‑complete”:

- Every relevant GIS file is either:
  - Linked to one or more GBIM tables in `wv_source_manifest_layers.csv`, or
  - Participating indirectly via unions/derivations described in `wv_derived_governance_tables.csv`.
- Every `public.wv_*` table is either:
  - Directly mapped to a source dataset, or
  - Classified as governance/identity/coverage/belief/variant/catalog/registry.

***

## 4. How to Use These Manifests

### 4.1 ETL and Lineage

- Use `wv_source_manifest_layers.csv` to drive ETL pipelines:
  - For each row, load the source file into the specified CRS.
  - Normalize schema to match the target `gbim_table`.
  - Preserve the `provider` and `role` metadata as lineage attributes.
- Use `wv_derived_governance_tables.csv` to understand:
  - Which tables should **not** be overwritten directly from external sources.
  - How identity and coverage is constructed on top of base datasets.
  - What joins and unions may be required to reconstruct publication surfaces.

### 4.2 RAG and Search

- Index geometry and attributes from `wv_source_manifest_layers.csv` tables for spatial RAG:
  - Attach manifest metadata (provider, CRS, role) to each indexed layer.
- Treat governance tables as:
  - Context for understanding counties, tracts, entity identity, and dataset coverage.
  - Sources of high‑level summaries and publication‑ready surfaces, not raw geometry.

### 4.3 CRS and Variants

- Favor UTM83 tables (e.g., `wv_wv_county_boundaries_24k_topo_updated_2026_utm83`) as the **primary spatial reference** for analysis.  
- Use WMA84 variants and GDB‑based boundary tables when:
  - Integrating with WMA84 workflows.
  - Comparing or validating CRS transformations.

All such variants are explicitly flagged as `governance_boundary_variant` or `governance_boundary_base` in the governance manifest.

***

## 5. Maintenance Notes

If you add new WV datasets or GBIM tables:

1. Append new source files to `wv_source_files_manifest.csv` with filename, provider, CRS, and notes.
2. Add rows to `wv_source_manifest_layers.csv` for:
   - New `public.wv_*` dataset tables with direct source files.
3. For internal views, identity, coverage, or belief tables:
   - Append entries to `wv_derived_governance_tables.csv` with:
     - `table_name`
     - `category`
     - `notes` describing derivation and purpose.
4. Re‑run your “unmapped table” check to ensure:
   - No dataset‑like tables are left without manifest rows or governance classification.

This keeps the WV corpus consistent and future‑proof for new GBIM revisions.

***

That is the recurrent epistemic commons.
