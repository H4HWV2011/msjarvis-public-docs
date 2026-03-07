## Why this matters for Polymathmatic Geography

This chapter establishes the foundational commitments of Polymathmatic Geography and explains what it means for a Steward System like Ms. Jarvis to hold structured claims about West Virginia and Appalachia. It specifies how claims must be organized so that they remain accountable to people, places, institutions, and evidence, rather than existing as opaque, unstructured text. By doing so, it frames the later geospatial and institutional machinery not as optional additions, but as necessary consequences of the commitments made here.

It supports:  
- **P1 – Every where is entangled** by insisting that legal, economic, infrastructural, social, and cultural facts be treated as aspects of one interconnected belief space, rather than isolated map layers or siloed datasets.  
- **P3 – Power has a geometry** by requiring that exposure, access, obligation, and flow be representable as explicit relationships between entities and regions, so that institutional power can be examined and contested in spatial form.  
- **P5 – Design is a geographic act** by treating design decisions about schemas, keys, pipelines, and retrieval rules as world‑shaping acts that structure how Appalachia appears in analysis, governance, and search, and by requiring that these decisions be documented rather than hidden inside black‑box systems.  
- **P12 – Intelligence with a ZIP code** by insisting that reasoning be anchored to specific West Virginia and Appalachian locations, with explicit ZIP‑ and county‑level contexts, rather than relying on abstract national averages.  
- **P16 – Power accountable to place** by demanding that system recommendations be inspectable and challengeable, traceable back to concrete claims about particular communities, including the datasets, epochs, and paths through which those claims enter the system.  

Within the thesis structure, this chapter belongs to the **Theoretical Framework** tier: it specifies conceptual commitments and constraints that later chapters show realized concretely in computational instruments such as GBIM, GeoDB, Chroma, and the retrieval‑and‑routing services that now operate in the production Ms. Jarvis deployment.

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

Later chapters (including the detailed GBIM chapter and the GeoDB chapter) show how these conceptual commitments are implemented over PostgreSQL/PostGIS, CSV‑derived tables, embeddings, and programme registries in the running system. Here, the chapter’s role is to make clear that a Steward System like Ms. Jarvis cannot be considered place‑accountable unless it supports beliefs that can be interrogated along these dimensions.

## What a geospatial belief model must support

This chapter uses GBIM as a guiding example of what a geospatial belief model must support, while focusing on requirements rather than on a particular schema. A compliant model must allow beliefs to be situated along nine coordinated axes:

- **Who** – people and institutions involved in or responsible for the feature or situation (agencies, operators, governing bodies, communities).  
- **What** – the type of thing or state being described (infrastructure, land use, facility, event, condition, etc.).  
- **Where** – spatial information, including coordinates, boundaries, and named areas, so that beliefs can be grouped and compared across counties, hollows, ZIP codes, and corridors.  
- **When** – temporal aspects such as dataset vintage, period, or epoch, so that change, persistence, and lag can be analyzed.  
- **How** – methods, processes, and mechanisms (survey designs, engineering processes, institutional procedures) that give rise to the state of affairs.  
- **Why** – motivations and purposes where they can be known, such as policy objectives or reasons for maintaining certain infrastructures or programmes.  
- **For whom** – beneficiaries and affected communities, making explicit who gains, who bears risk, and who is left out.  
- **Under whose authority** – legal and institutional bases: statutes, regulations, charters, and formal powers associated with the infrastructure or programme.  
- **On what evidence** – links to source documentation, clearinghouse entries, archival records, and logs that justify the belief.  

From the standpoint of this chapter, these axes are obligations: any system that claims to implement Polymathmatic Geography must be able to express and interrogate beliefs along these lines. The later GBIM implementation chapter shows one concrete schema that satisfies these obligations; other implementations would still need to meet the same requirements, even if they choose different internal encodings.

## Conceptual layers of representation

The chapter also sets out a layered view of representation that the programme requires, independent of any particular technology stack. In this view, a place‑accountable Steward System must include at least the following conceptual layers:

1. **Schema layer** – A logical structure that can store and query beliefs across the nine axes, with stable identities for features and institutions, explicit handling of epochs and vintages, and clear separation between different kinds of entities (people, places, programmes, infrastructures, norms).  

2. **Spatial layer** – A representation of West Virginia and Appalachia as a coherent, queryable geospatial mesh of structures, hazards, networks, facilities, and governance boundaries, rather than as a set of disjoint files. This layer must support operations such as selection, buffering, intersection, and region‑based aggregation.  

3. **Semantic layer** – Mechanisms that allow beliefs and texts to be compared and retrieved by meaning, not just by identifiers. This layer must support “neighborhoods” of related beliefs, so that conceptually or institutionally similar items can be clustered and examined together.  

4. **Programme and institutional layer** – Structures that encode real programmes, services, and institutions, including who they serve, where they operate, and under what rules. This layer must connect spatial features and beliefs to the concrete assistance and governance structures that affect households and communities.  

5. **Retrieval and logging layer** – Processes that answer questions by drawing on the other layers, and that record which beliefs, datasets, regions, and services were involved in each answer. This layer is critical for inspection, contestation, and governance, because it makes visible how the system has actually used its knowledge.  

The chapter’s purpose is to articulate these layers as conceptual necessities. Later, instrument‑level chapters show how they are realized using PostGIS, belief tables, vector collections, registries, and orchestrated retrieval and routing services in the live Ms. Jarvis deployment.

## How these foundations are realized (high‑level)

While this chapter focuses on theory, it also acknowledges that, as of early 2026, the commitments it articulates are already realized in a running Steward System. In that system:

- Beliefs about West Virginia are stored in structures that encode the nine axes listed above, rather than in unstructured text alone.  
- A statewide spatial corpus allows features, hazards, infrastructures, facilities, and governance geometries to be selected and analyzed as a coherent mesh.  
- Semantic collections support similarity search and clustering over beliefs and programme descriptions, enabling neighborhood‑style reasoning over both spatial and institutional content.  
- External programme registries model community resources such as food assistance, housing, utilities, senior services, and education, keyed to ZIPs and counties where deployed.  
- Retrieval and coordination services route real questions through these structures and log which beliefs, collections, and programme entries are used, enabling inspection and refinement.  

These concrete implementations are documented in detail in later chapters, especially those devoted to GBIM, GeoDB, semantic memory, and case studies. The role of this chapter is to make explicit that those implementations are not arbitrary engineering choices, but answers to the foundational questions posed here about what a place‑accountable, polymathmatic Steward System must do.

## Status as of March 2026

As of March 2026, the framework described in this chapter is not merely aspirational. The live Ms. Jarvis deployment over West Virginia data already conforms to the commitments laid down here: it records beliefs along multiple axes, ties them to concrete geographies and institutions, supports layered reasoning and retrieval, and logs the pathways through which recommendations are produced. Remaining theoretical work at this level involves refining how distributional impacts and “for whom” questions are expressed, extending the framework beyond West Virginia, and deepening community‑facing mechanisms for inspection and contestation. Subsequent chapters provide the detailed evidence that these foundations have been realized in a way that can be measured, queried, and audited.
