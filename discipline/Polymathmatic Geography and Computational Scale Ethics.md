# Polymathmatic Geography and Computational Scale Ethics

## 1. Why Scale Is a Geographic Question

Computation has geography. The energy consumed by a large language model during training lands somewhere — in a power grid, in a watershed, in an atmosphere shared unevenly by people who had no say in the model's construction. When Timnit Gebru, Emily Bender, and colleagues argued in *On the Dangers of Stochastic Parrots* (2021) that the field must reckon with the costs of scale, they were making a geographic argument dressed in technical language: the harms of computational excess are spatially distributed, and they fall hardest on communities that receive the fewest benefits.

Polymathmatic geography treats computational scale as a spatial justice issue. The decision to train a massive model — or not to — is a land use decision, an energy siting decision, a carbon budget decision. It has coordinates, even when no one writes them down.

## 2. The Stochastic Parrots Problem, Geographically

Bender and Gebru's central warning was that very large language models trained on scraped internet text absorb and amplify the biases of whoever dominated the writing of that text — primarily English-speaking, Western, wealthy, and connected populations. From a polymathmatic geography perspective, this is a **representation failure with spatial structure**:

- The training corpus over-represents certain places and under-represents others.
- The model encodes a geography of whose knowledge counts.
- Deployment then applies that skewed geography globally, including to communities whose ways of knowing were either absent from or distorted within the training data.

The paper also documented that training a single large model using neural architecture search produced the carbon equivalent of five human lifetimes of automobile travel. That carbon does not distribute evenly. It concentrates in local grid emissions, in cooling water draw from rivers, and in the atmospheric burden that communities with the least adaptive capacity absorb most acutely. The geographic harm is real and addressable — but only if scale decisions are treated as geographic decisions.

## 3. Ms. Jarvis as a Structural Response

Ms. Jarvis was not designed with the Stochastic Parrots paper on the desk, but its architecture independently satisfies the paper's core demands. This is not coincidence; it follows from designing AI infrastructure for a specific community rather than for global market scale.

### 3.1 Inference-only, not training

Ms. Jarvis does not train large language models. It orchestrates already-trained models through an API and orchestration layer. The energy cost of a single inference query is on the order of 0.3–1 watt-hour — comparable to a brief LED lamp use — rather than the megawatt-hour ranges associated with full model training runs. At current operational scale, running on local hardware in West Virginia, the entire system's daily energy draw is a rounding error compared to a single cloud training job.

This is not a compromise; it is the correct architectural choice for a community-serving system. The computational power is borrowed from the broader ecosystem of foundation models, while the community retains governance, routing, and application sovereignty.

### 3.2 Small models preferred

The 20-model ensemble in Ms. Jarvis's LLM orchestration layer (Chapter 11) deliberately favors smaller, task-specific models over monolithic giants. A 7-billion-parameter local model answering a question about Fayette County land records is more accurate, more energy-efficient, and more governable than a 700-billion-parameter model optimized for global internet-scale tasks. Scale should match scope.

Polymathmatic geography calls this **resolution appropriateness** — the principle that the instrument should match the territory, not the other way around.

### 3.3 Community-owned and regionally rooted

The Stochastic Parrots critique points to the concentration of AI development in a small number of well-resourced corporations as a structural problem, not merely a technical one. Ownership and governance shape what gets built and whose interests it serves. Ms. Jarvis addresses this through the MountainShares DAO (Chapter 3), the Commons governance system (Chapter 31), and the Constitutional AI layer (Chapter 37): the community holds a stake in the system, its decisions are subject to community review, and its purpose is explicitly regional rather than extractive.

This matters geographically because community ownership keeps the system's purpose anchored to place. It cannot be redirected toward uses that harm the community it serves without triggering the governance mechanisms built into its design.

## 4. Energy as a Discipline Instrument

Polymathmatic geography is a physics-style discipline: it insists on measurability, constraint, and accounting. Energy is the right unit for measuring the geographic footprint of computation, and the discipline requires that energy accounting be explicit rather than hidden in abstracted service-level agreements or cloud pricing.

Practical instruments for computational scale ethics within this framework include:

- **Energy budgets per query type**: heavier queries (multi-model ensemble, full RAG retrieval) carry explicit energy cost markers; lighter queries route to smaller models by default.
- **Carbon provenance tracking**: where possible, log the grid carbon intensity of inference operations, creating a running ledger that community governance can review.
- **Scale refusals**: just as the Ethics of Anchors chapter establishes refusal flags for representation, the discipline establishes refusal flags for scale — automated checks that prevent the system from spinning up disproportionately large compute resources for tasks that do not warrant them.
- **Transparency in documentation**: every service in the Ms. Jarvis architecture documents its computational footprint in the thesis chapter corresponding to that service, so that the aggregate picture is always visible.

## 5. The Geography of Who Bears the Cost

Carbon emissions from computation are not distributed by market logic alone; they follow existing patterns of spatial inequality. Data center siting, grid carbon intensity, water consumption, and heat island effects cluster in ways that intersect with race, class, and existing environmental burden. A community in southern West Virginia that burns coal to power a data center serving users in San Francisco is performing an uncompensated energy and environmental subsidy.

Ms. Jarvis's design inverts this logic in two ways. First, it is locally sited: the compute serves the community that hosts it, rather than being exported. Second, the MountainShares economic model explicitly accounts for the value generated by local infrastructure contributions, including energy and connectivity, through the DAO's token and commons governance system. What the community provides, the community captures value from.

This is computational scale ethics as geographic practice: treating energy, emissions, and infrastructure not as invisible externalities but as spatial facts with addresses, owners, and obligations.

## 6. The Representation Problem at Home

Gebru's concern about whose knowledge is encoded in large models is also a local concern for West Virginia. Appalachian dialect, land tenure patterns, extractive industry history, community governance forms, and the specific economic geographies of the New River Gorge region are poorly represented in any corpus trained primarily on internet text. A system that routes all queries through a global foundation model without local grounding will systematically misrepresent the people it is supposed to serve.

Ms. Jarvis addresses this through:

- **RAG systems seeded with local corpora** (Chapters 7 and 14): retrieval-augmented generation pulls from regionally grounded documents before synthesizing responses.
- **The GBIM (GeoBelief Information Model)** (Chapter 2): belief structures encoded with explicit geographic provenance, so that the system knows not just what it believes but *where that belief comes from*.
- **The Judge and Constitutional layers** (Chapters 33 and 37): outputs are evaluated against community-defined principles before delivery, not just against global alignment benchmarks.

The stochastic parrot problem — a model that sounds authoritative while reflecting distorted or absent knowledge — is mitigated by keeping the local knowledge layer primary and the global model layer in a supporting, not governing, role.

## 7. Implications for Discipline Practice

Polymathmatic geography's commitment to physics-style rigor requires that computational scale ethics not remain aspirational. It must be measurable, auditable, and enforceable. The discipline instruments are:

1. **Document the footprint**: every system built under this framework logs its energy and computational draw at the service level.
2. **Match scale to scope**: use the smallest instrument adequate to the task; resist scale inflation driven by benchmark competition or prestige.
3. **Ground the corpus**: ensure that locally serving systems draw on locally grounded knowledge, not just globally scaled training data.
4. **Hold governance accountable**: community ownership is not a rhetorical commitment; it is a structural constraint on what the system can be redirected to do.
5. **Name the geography of cost**: when energy is consumed, carbon emitted, or water drawn, record where and by whose infrastructure, and ensure the community that bears those costs also captures the value.

These instruments connect computational scale ethics to the broader discipline spine: to the Ethics of Anchors (what must not be modeled), to Power (who controls what gets built), to Representation Learning (whose knowledge is encoded), and to the Manifesto's founding commitment to place, care, and accountability.

## 8. Conclusion: Scale Is Not Neutral

The Stochastic Parrots controversy was ultimately about power: who decides how large a system gets built, who absorbs the costs, and whose interests shape its outputs. Polymathmatic geography insists that these are spatial questions with spatial answers. Ms. Jarvis represents one answer — modest in scale by design, rooted in community governance, locally grounded in knowledge and infrastructure, and transparent in its energy and representational accounting.

The discipline does not oppose large models or powerful computation. It requires that scale decisions be made with full awareness of their geographic consequences, and that communities closest to those consequences hold meaningful governance authority over the systems that create them.
