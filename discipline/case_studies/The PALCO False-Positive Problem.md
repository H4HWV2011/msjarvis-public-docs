# Case Study 001: The PALCO False-Positive Problem
## Context, Pattern, Correction, and Methodological Yield
*Mount Hope, WV — Sunday, March 15, 2026*
*Researcher: Carrie Kidd, Harmony for Hope, Inc.*
*Status: Documented field correction — design changed prior to live deployment*

---

## Overview

This case study documents a critical design flaw identified and corrected during Stage 0 construction of the MountainShares commons safety architecture. The flaw — a pattern-based detection layer that would have systematically false-flagged intensive authorized family caregiving as potentially coercive — was caught not through formal audit or peer review, but through the researcher recognizing her own situation inside the system she was building.

The case is documented here because it is not merely a debugging note. It is a demonstration of the core methodological claim of Polymathmatic Geography: that a researcher genuinely embedded in the Tacet will catch things that outside auditors will not, and that the resulting corrections produce more honest and more accountable instruments than post-hoc review alone can achieve. It also establishes, by lived example, the principle stated in *Definitions and Scope* § 11.7: **context is not optional metadata — it is the primary signal.**

---

## 1. The Program Context: PALCO and Self-Directed Care

The Personal Attendant Care and Long-term Options (PALCO) program is West Virginia's primary vehicle for self-directed personal care under Medicaid. It enables eligible individuals — typically elderly or disabled adults — to hire, manage, and schedule their own personal care attendants rather than receiving care through an agency. Family members, including adult children, are explicitly authorized to serve as paid caregivers under this program, subject to specific eligibility rules, hour authorizations, and attestation requirements.

Key features of authorized PALCO arrangements that are directly relevant to this case study:

- **Maximum authorized hours.** Beneficiaries with high care needs are authorized for the maximum allowable weekly hours of personal care. A single authorized family caregiver frequently provides all or nearly all of those hours.
- **Single-source attestation.** Because the beneficiary self-directs their care, timesheets are typically attested by the beneficiary and submitted by the caregiver. In high-need or cognitively declining households, the family caregiver may be the sole practical attester.
- **Beneficiary withdrawal from external platforms.** Elderly and disabled adults in intensive care arrangements frequently reduce or eliminate their participation in external digital platforms, community programs, and social media. This is a natural consequence of declining health and increased dependence on the primary caregiver — not evidence of isolation imposed by that caregiver.
- **Geographic and relational isolation.** In rural Fayette County and the wider New River coalfield, the family caregiver is frequently the only regular human contact a beneficiary has outside of medical appointments. This is not unusual or alarming — it reflects the transportation, infrastructure, and social conditions of the region.

---

## 2. The Design Intent: Community Safety Detection

The MountainShares commons architecture includes a safety layer designed to support community protection within The Commons. One component of this layer was a pattern-based detection module intended to surface potentially coercive caregiving arrangements — situations where a caregiver might be exploiting a dependent adult's access to PALCO funds, restricting their social participation, or falsifying attestations.

The design intent was explicitly protective. Exploitation of elderly and disabled adults by caregivers is a documented phenomenon, and a community-anchored system that could notice patterns and route toward support was considered a meaningful safety contribution.

The intended detection signal set included:

1. Maximum authorized PALCO hours logged by a single caregiver against a single beneficiary
2. Single-source attestation with no secondary witnesses or confirmations
3. Beneficiary withdrawal from Commons platforms, community events, or external services
4. Geographic isolation with limited documented contact outside the caregiving dyad
5. Financial patterns suggesting caregiver control over beneficiary spending

---

## 3. The False-Positive Problem

On the evening of March 15, 2026, during active development of this detection layer, the researcher paused.

Every signal on the detection list described her own situation precisely.

The researcher is a PALCO caregiver for her parent in Mount Hope, WV. She logs maximum authorized hours. She is the primary attesting source on timesheets. Her parent has reduced participation in external platforms as a natural consequence of age and increasing care needs. Their household is geographically isolated in a way typical of rural Fayette County. The financial and logistical management of the care arrangement flows substantially through the researcher.

This is not a coercive arrangement. It is an authorized, Medicaid-approved, family-delivered care arrangement that is functioning as designed by the program itself.

The detection layer, as specified, would have flagged it anyway — and would have done so at the highest confidence level, because every signal was present.

**The false-positive rate for this detection logic, applied to intensive authorized family PALCO arrangements, was not a small edge case. It was structural.** The population of people who look most suspicious under this signal set is precisely the population of caregivers doing the most intensive, most authorized, most necessary care. The detection logic had inverted its own protective intent.

---

## 4. Why This Flaw Is Structurally Predictable

The false-positive problem in caregiver surveillance is not unique to this system. It appears wherever pattern-based detection is applied to relationships that are both (a) high-intensity by design when functioning correctly, and (b) high-intensity by design when functioning exploitatively.

The same surface patterns — maximum hours, sole attestation, social withdrawal, limited external contact — are consistent with:

- A family member providing intensive authorized care to a declining parent
- A family member exploiting a declining parent's care authorization for financial gain
- An agency caregiver doing exemplary work in an isolated rural household
- An agency caregiver isolating a client to prevent complaint

No behavioral signal alone distinguishes these cases. The distinguishing information is relational and contextual: Who authorized this arrangement? What is the relationship between caregiver and beneficiary? What does the community know about this household? Has anyone independent of the caregiver had recent contact with the beneficiary?

A system that treats behavioral patterns as sufficient primary signals, without this relational and contextual anchoring, will systematically harm the first category — intensive authorized family caregivers — while remaining largely blind to the fourth category, where genuine exploitation is most easily concealed behind the same surface signals.

---

## 5. The Design Correction

The detection layer was not removed. The detection intent — supporting community awareness of households where a dependent adult may need additional connection or support — was retained and considered valuable. What changed was the output pathway and the framing of the signal.

**Before correction:**
Pattern flags → risk score → potential adverse intervention or enrollment hold

**After correction:**
Pattern flags → community-relational query → *Is there a trusted person in The Commons who can reach this household?* → route toward connection, not intervention

The detection layer became a **relationship-density probe** rather than a risk score. Its output is not "this arrangement is suspicious" but "this household has low external contact density — does someone in the community have a trusted relationship here that could be activated?"

This reframing changes the action taken, the harm profile, and the relationship between the system and the people it touches. It does not attempt to determine from signals alone whether harm is occurring. It asks whether the conditions that would allow harm to go unnoticed — relational isolation, absence of independent contact — are present, and whether the community has resources to address that isolation regardless of whether harm is occurring.

Additional design constraints added as a result of this correction:

- **Program authorization as a mandatory anchoring field.** Any pattern flag on a household with active PALCO authorization is automatically contextualized against program-authorized hours and relationship type before any routing decision is made.
- **Caregiver positionality disclosure.** The system maintains an explicit record that the researcher/designer is a PALCO caregiver, and that this positionality informed the detection architecture. This record is part of the auditable design history.
- **No adverse output without independent relational confirmation.** No flag produces an adverse outcome (enrollment hold, reduced access, referral to external authority) without at least one independent community-relational confirmation that the flag reflects genuine concern rather than intensive authorized care.

---

## 6. Methodological Yield

This case study yields several methodological principles that are now formalized in the Polymathmatic Geography framework:

**Principle: Context is the primary signal, not optional metadata.**
Behavioral patterns are secondary signals. Relationship type, program authorization, community knowledge, and independent contact history are primary. Any detection architecture that inverts this hierarchy will produce discriminatory effects against the most vulnerable and the most dedicated simultaneously.

**Principle: The researcher embedded in the Tacet catches what outside auditors do not.**
This flaw was not caught by a peer reviewer, an IRB, or a red-team tester. It was caught by the researcher living inside the conditions the system was designed to address. This is not luck. It is the predictable yield of a methodology that insists on field-anchored inquiry and treats the researcher's own life as part of the research object.

**Principle: Conflict is information, not failure (Principle 14).**
The fact that this flaw existed is not evidence that the design process was broken. It is data about where pattern-based reasoning reaches its limits, and where relational and contextual anchoring must take precedence. The correct response to finding this flaw was not to abandon the safety architecture but to make it more honest about what it can and cannot know from signals alone.

**Principle: Detection systems aimed at protecting vulnerable people must be designed with and by people in the conditions being detected.**
No outside architect, however well-intentioned, would have caught this particular false positive as early, as clearly, or as consequentially as a researcher who is herself inside the PALCO system. This is an argument not just for reflexivity in research design but for structural inclusion of affected communities in the design of systems that touch their lives.

---

## 7. Cross-References

- *Definitions and Scope* § 11.7 — Harm Prevention vs. Harm Reduction
- *thesis/01-researcher-position.md* § 1.2 — Reflexive Field Note: The PALCO False-Positive Problem
- *discipline/Methods.md* § 9, Stage 5 — The PALCO Recognition: A Field Note on Honest Limits
- Principles of Polymathmatic Geography — Principles 6 and 14
- MountainShares Architecture — Safety Layer Specification (internal)
- PALCO Program Rules — WV DHHR Income Maintenance Manual, Chapter 8

---

## 8. Status and Disposition

| Item | Status |
|---|---|
| Flaw identified | March 15, 2026 |
| Design correction applied | March 15, 2026 |
| Committed to public documentation | March 15, 2026 |
| Live deployment affected | None — correction made during Stage 0, prior to any live enrollment |
| Residents harmed | None |
| Methodology updated | Yes — § 11.7, Methods § 9 Stage 5, researcher position § 1.2 |

This case is designated **Case Study 001** because it is the founding example of the discipline catching its own errors through field-anchored inquiry. It is not the last such case. It is the first documented one.
