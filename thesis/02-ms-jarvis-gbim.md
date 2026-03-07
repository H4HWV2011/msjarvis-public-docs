## Why this matters for Polymathmatic Geography

This chapter establishes the foundational commitments of Polymathmatic Geography and explains what it means for a Steward System like Ms. Jarvis to hold structured claims about West Virginia and Appalachia. It specifies how claims must be organized so that they remain accountable to people, places, institutions, and evidence, rather than existing as opaque, unstructured text. By doing so, it frames the later geospatial, semantic, and institutional machinery not as optional additions, but as necessary consequences of the commitments made here.

It supports:  
- **P1 – Every where is entangled** by insisting that legal, economic, infrastructural, social, and cultural facts be treated as aspects of one interconnected belief space, rather than isolated map layers or siloed datasets. The chapter makes explicit that “beliefs” about a bridge, a benefits office, and a floodplain must live in a shared representational fabric, so that their interactions and conflicts can be examined together.  
- **P3 – Power has a geometry** by requiring that exposure, access, obligation, and flow be representable as explicit relationships between entities and regions, so that institutional power can be examined and contested in spatial form, not just as abstract policy language.  
- **P5 – Design is a geographic act** by treating design decisions about schemas, keys, pipelines, and retrieval rules as world‑shaping acts that structure how Appalachia appears in analysis, governance, and search, and by requiring that these decisions be documented and inspectable rather than hidden inside black‑box systems.  
- **P12 – Intelligence with a ZIP code** by insisting that reasoning be anchored to specific West Virginia and Appalachian locations, with explicit ZIP‑ and county‑level contexts, rather than relying on abstract national averages or placeless aggregates.  
- **P16 – Power accountable to place** by demanding that system recommendations be inspectable and challengeable, traceable back to concrete claims about particular communities, including the datasets, epochs, and paths through which those claims enter the system.  

Within the thesis structure, this chapter belongs to the **Theoretical Framework** tier: it specifies conceptual commitments and constraints that later chapters show realized concretely in computational instruments such as GBIM, GeoDB, Chroma, and the retrieval‑and‑routing services that now operate in the production Ms. Jarvis deployment.

---

## Ms. Jarvis and the Geospatial Belief Information Model (GBIM)

Within Polymathmatic Geography, Ms. Egeria Jarvis is a bounded, biologically inspired Steward System whose commitments are explicitly anchored in geography, time, community, and source. In this chapter, she appears primarily as an exemplar of what it means to hold beliefs in a way that satisfies the framework’s requirements, rather than as a fully detailed implementation. The emphasis is on the kinds of information that must be associated with each belief and on how those beliefs must relate to one another across space and institutions.

The Geospatial Belief Information Model (GBIM) is introduced here conceptually as the kind of structure a compliant Steward System must possess. At a minimum, such a model must be able to tie each belief about West Virginia or Appalachia to:

- who is involved in or responsible for the feature or situation,  
- what kind of thing or state is being described,  
- where it is located or felt,  
- when it applies or was observed,  
- how it came to exist or be recorded,  
- why it exists or is maintained (where such motives are knowable),  
- for whom it matters or has consequences,  
- under whose authority it operates, and  
- on what evidence it rests.  

In the Quantarithmia framework, these requirements imply that regions themselves—such as ZIP codes, counties, corridors, and neighborhoods—must appear as parameterizing elements. Each region can be treated as encoding local conditions in the global state, so that differences between places show up as differences in stored structure and in the “landscape” of beliefs and obligations. The key point for this chapter is that such differences must be representable and inspectable, not merely invoked metaphorically.

From this perspective, the nine axes do not just annotate records; they define coordinates in a structured belief space over Appalachia. Trajectories in this space—such as a programme moving from pilot to permanent status, or an infrastructure asset changing condition over time—are understood as structured changes along these axes: who is responsible, what has changed, where impacts occur, when shifts happen, how they are produced, why they are justified, for whom they matter, under whose authority, and on what evidence.

<p align="center">
  <img src="https://github.com/user-attachments/assets/6f5a2f9e-1f3f-4c2c-a1f6-4a2d3c5f9abc"
       alt="GBIM belief space over Appalachia"
       width="900">
</p>

> *Figure X – GBIM as a geospatial belief space. Each belief about West Virginia is located along nine coordinated axes (who, what, where, when, how, why, for whom, authority, evidence), allowing trajectories of obligation, risk, and benefit to be inspected over regions such as ZIP codes and counties.*

Later chapters (including the detailed GBIM chapter and the GeoDB chapter) show how these conceptual commitments are implemented over PostgreSQL/PostGIS, CSV‑derived tables, embeddings, and programme registries in the running system. Here, the chapter’s role is to make clear that a Steward System like Ms. Jarvis cannot be considered place‑accountable unless it supports beliefs that can be interrogated along these dimensions and traced through such trajectories.

---

## What a geospatial belief model must support

This chapter uses GBIM as a guiding example of what a geospatial belief model must support, while focusing on requirements rather than on a particular schema. A compliant model must allow beliefs to be situated along nine coordinated axes:

- **Who** – people and institutions involved in or responsible for the feature or situation (agencies, operators, governing bodies, communities).  
- **What** – the type of thing or state being described (infrastructure, land use, facility, event, condition, programme, norm).  
- **Where** – spatial information, including coordinates, boundaries, and named areas, so that beliefs can be grouped and compared across counties, hollows, ZIP codes, and corridors.  
- **When** – temporal aspects such as dataset vintage, period, or epoch, so that change, persistence, and lag can be analyzed and not treated as timeless facts.  
- **How** – methods, processes, and mechanisms (survey designs, engineering processes, institutional procedures) that give rise to the state of affairs.  
- **Why** – motivations and purposes where they can be known, such as policy objectives or reasons for maintaining certain infrastructures or programmes.  
- **For whom** – beneficiaries and affected communities, making explicit who gains, who bears risk, and who is left out.  
- **Under whose authority** – legal and institutional bases: statutes, regulations, charters, and formal powers associated with the infrastructure or programme.  
- **On what evidence** – links to source documentation, clearinghouse entries, archival records, and logs that justify the belief and allow it to be checked or contested.  

From the standpoint of this chapter, these axes are obligations, not optional metadata. Any system that claims to implement Polymathmatic Geography must be able to express and interrogate beliefs along these lines; otherwise, it cannot support the kind of spatial justice analysis the programme demands. The later GBIM implementation chapter shows one concrete schema that satisfies these obligations; other implementations would still need to meet the same requirements, even if they choose different internal encodings.

The chapter also emphasizes that these axes must support both static description and dynamic reasoning. For example, questions about “who is responsible for flood risk here, for whom, and under whose authority?” require traversing multiple axes at once, connecting physical infrastructures, hazard layers, governing institutions, and beneficiary communities into a single, inspectable chain of beliefs.

---

## Conceptual layers of representation

The chapter sets out a layered view of representation that the programme requires, independent of any particular technology stack. In this view, a place‑accountable Steward System must include at least the following conceptual layers:

1. **Schema layer** – A logical structure that can store and query beliefs across the nine axes, with stable identities for features and institutions, explicit handling of epochs and vintages, and clear separation between different kinds of entities (people, places, programmes, infrastructures, norms). This layer defines what counts as a belief and how it can be addressed, grouped, and transformed.  

2. **Spatial layer** – A representation of West Virginia and Appalachia as a coherent, queryable geospatial mesh of structures, hazards, networks, facilities, and governance boundaries, rather than as a set of disjoint files. This layer must support operations such as selection, buffering, intersection, and region‑based aggregation, so that questions can be posed and answered in explicitly geographic terms.  

3. **Semantic layer** – Mechanisms that allow beliefs and texts to be compared and retrieved by meaning, not just by identifiers. This layer must support “neighborhoods” of related beliefs, so that conceptually or institutionally similar items can be clustered and examined together, and so that questions like “what else looks like this programme here, but in another county?” become operational queries.  

4. **Programme and institutional layer** – Structures that encode real programmes, services, and institutions, including who they serve, where they operate, and under what rules. This layer must connect spatial features and beliefs to the concrete assistance and governance structures that affect households and communities, so that analysis of infrastructure and risk can be tied to analysis of available help and authority.  

5. **Retrieval and logging layer** – Processes that answer questions by drawing on the other layers, and that record which beliefs, datasets, regions, and services were involved in each answer. This layer is critical for inspection, contestation, and governance, because it makes visible how the system has actually used its knowledge and how power has been exercised through recommendations and omissions.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/7c4d6c47-0f63-4b3e-bf2d-1b4b5c8cdef0"
       alt="Layered representation in Polymathmatic Geography"
       width="900">
</p>

> *Figure Y – Conceptual layers in a place‑accountable Steward System. Schema, spatial, semantic, programme, and retrieval‑logging layers work together to make beliefs, obligations, and recommendations inspectable across West Virginia and Appalachia.*

Together, these layers define what it means for a Steward System to “see” a region in polymathmatic terms. Later, instrument‑level chapters show how they are realized using PostGIS, belief tables, vector collections, registries, and orchestrated retrieval and routing services in the live Ms. Jarvis deployment.

---

## How these foundations are realized (high‑level)

While this chapter focuses on theory, it also acknowledges that, as of early 2026, the commitments it articulates are already realized in a running Steward System. In that system:

- Beliefs about West Virginia are stored in structures that encode the nine axes listed above, rather than in unstructured text alone, with tables and collections keyed to stable identifiers for worldview entities and belief records.  
- A statewide spatial corpus allows features, hazards, infrastructures, facilities, and governance geometries to be selected and analyzed as a coherent mesh, so that questions about a corridor, a county, or a watershed can traverse multiple datasets without losing spatial context.  
- Semantic collections support similarity search and clustering over beliefs and programme descriptions, enabling neighborhood‑style reasoning over both spatial and institutional content and supporting questions like “who helps whom, where, and under what authority?”  
- External programme registries model community resources such as food assistance, housing, utilities, senior services, and education, keyed to ZIPs and counties where deployed, and linked back to beliefs about infrastructure, risk, and obligation.  
- Retrieval and coordination services route real questions through these structures and log which beliefs, collections, and programme entries are used, enabling inspection, refinement, and governance review of how answers were produced.  

These concrete implementations are documented in detail in later chapters, especially those devoted to GBIM, GeoDB, semantic memory, and case studies such as MountainShares. The role of this chapter is to make explicit that those implementations are not arbitrary engineering choices, but answers to the foundational questions posed here about what a place‑accountable, polymathmatic Steward System must do.

---

## Status as of March 2026

As of March 2026, the framework described in this chapter is not merely aspirational. The live Ms. Jarvis deployment over West Virginia data already conforms to the commitments laid down here: it records beliefs along multiple axes, ties them to concrete geographies and institutions, supports layered reasoning and retrieval, and logs the pathways through which recommendations are produced. Remaining theoretical work at this level involves refining how distributional impacts and “for whom” questions are expressed, extending the framework beyond West Virginia, and deepening community‑facing mechanisms for inspection and contestation. Subsequent chapters provide the detailed evidence that these foundations have been realized in a way that can be measured, queried, and audited, and outline how the same commitments can be carried into additional regions and governance settings.
