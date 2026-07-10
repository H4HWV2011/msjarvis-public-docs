# 36. Identity and Registration

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 10, 2026*

---

## 36.1 Identity in a Governed System

Identity in Ms. Allis is not a single undifferentiated object. It is a governed relationship among session state, validated continuity, consent, registration, and bounded disclosure.

This chapter treats identity as something that must be carefully tiered. A passing internal state, a live sandbox session, a durable registered profile, and a publicly visible representation are not the same thing and must not be collapsed into one another. The architecture therefore distinguishes among temporary identity-bearing context, durable registered identity state, and any outwardly disclosed identity surface.

Identity is thus inseparable from governance. It depends on how information is retained, how it is promoted, how it is linked, and under what conditions it is allowed to become durable or visible.

---

## 36.2 Ephemeral Session Identity State

Ephemeral session identity state is the temporary identity-bearing context that exists during an active reasoning or interaction session.

This state may include session-specific continuity markers, local preference cues, temporary working self-reference, unresolved hypotheses, and internal tags needed to preserve coherence inside the sandbox. It is operationally important, but it is not yet durable identity. It exists to support bounded reasoning and interaction during the life of the session.

The crucial property of ephemeral identity state is that it is **session-scoped**. It should remain tied to a sandbox session ID or equivalent temporary container and should not be treated as automatically fit for durable registration, public disclosure, or identity-wide propagation.

---

## 36.3 Durable Registered Identity State

Durable registered identity state is different in kind, not only in duration.

Registered identity state is the part of identity that has crossed the relevant governance boundary and is allowed to persist beyond the immediate sandbox session. It may support continuity across sessions, stable identity-linked services, authenticated personalization, or governed memory and registration flows. Because it is durable, it must be held to stricter standards than ephemeral session state.

This chapter therefore distinguishes clearly between:

- **ephemeral session identity state**, which supports live bounded cognition and may expire or flush with the session;
- **durable registered identity state**, which has crossed a promotion and retention threshold and is allowed to persist under governed conditions.

The system should not assume that what is useful in-session is automatically fit for registration.

---

## 36.4 Session IDs and Promotion Paths

Sandbox session IDs are an important part of the promotion and retention flow.

A sandbox session ID provides the temporary anchor under which candidate conclusions, local identity cues, validation results, and transition records can be grouped during a bounded reasoning episode. When an approved conclusion crosses the relevant gate, the session ID should remain part of the provenance chain so that the resulting durable write can be traced back to the session in which it arose.

This means approved conclusions should not appear inside durable identity-linked systems as detached facts with no transitional lineage. They should remain linked to:

- the originating sandbox session ID;
- the relevant validation or gate outcome;
- any promotion receipt or promotion event identifier;
- the identity-linked destination system or promotion script that accepted the conclusion.

That linkage protects continuity without erasing provenance.

---

## 36.5 Identity-Linked Promotion Scripts

Approved conclusions may connect to identity-linked systems through governed promotion scripts or equivalent promotion paths.

This chapter understands such scripts as the mechanisms that move a validated conclusion from sandbox-bounded state into a durable identity-bearing domain. The point is not that every approved conclusion must become identity state. The point is that whenever such movement occurs, it should be explicit, gated, and reconstructable.

A proper identity-linked promotion flow therefore requires:

- an originating session or run identifier;
- an approved conclusion or approved identity-relevant artifact;
- a recorded gate outcome showing why promotion was allowed;
- a durable destination such as an identity-linked store, memory layer, graph, or registration mechanism;
- a retention rule governing how long the promoted state remains in effect.

This keeps promotion from becoming an invisible or magical jump from temporary cognition to registered identity.

---

## 36.6 Retention and Registration

Registration is not just storage. It is storage under named retention and governance conditions.

When identity-bearing material becomes durable, the system should record whether it is retained as short-horizon continuity, long-horizon registered identity, auditable history, or some narrower role-specific form. The retention rule matters because durable identity creates a stronger claim about continuity, accountability, and possible downstream effect than sandbox state does.

For that reason, registration should include at least the following distinctions:

- what was retained;
- why it was retained;
- which gate or approval path authorized retention;
- whether the retained item is revocable, expiring, or persistent;
- whether it is private, shared within bounded services, or eligible for further disclosure under separate consent.

This chapter treats retention as part of identity governance, not as an afterthought.

---

## 36.7 Nested Disclosure Projections

Identity should be disclosed through nested projections rather than a single all-or-nothing exposure model.

A nested disclosure projection is a bounded identity view shaped for a particular context, audience, or authority level. One projection may expose only minimal continuity markers needed for session coherence. Another may expose authenticated service-level identity fields. Another may expose a narrower public-facing representation. These are projections from a governed identity structure, not independent identities.

This chapter therefore rejects the assumption that registered identity must be fully surfaced wherever identity is needed. Instead, disclosure should proceed by layers:

- internal ephemeral projection for live session coherence;
- internal durable projection for authorized identity-linked services;
- limited external projection for explicitly approved sharing contexts;
- public projection only where there is a distinct and justified basis for public disclosure.

Nested projection protects both utility and restraint.

---

## 36.8 Consent-Controlled Escalation

Movement from one disclosure layer to another must be consent-controlled wherever consent is relevant and structurally available.

Consent-controlled escalation means that the system should not automatically widen the visibility or consequence of identity-bearing material merely because it has become durable. Durability is not the same as shareability, and shareability is not the same as publicity. A registered identity element may be valid for retention but still not be valid for broader exposure.

Escalation should therefore be governed by:

- the scope of the original interaction;
- the consent state associated with the identity-bearing material;
- the destination context requesting additional disclosure;
- any policy or guardian constraint limiting expanded exposure;
- whether the requested escalation is necessary, proportional, and reversible where possible.

This preserves the difference between continuity and exposure.

---

## 36.9 No Automatic Public Exposure

This chapter states plainly that automatic public exposure is prohibited.

An approved conclusion, a durable registration event, or a successful identity-linked promotion does not by itself authorize public revelation. The fact that something is true, useful, durable, or identity-relevant does not mean it should be made public. Public disclosure is a separate category of act and requires its own justification.

The prohibition on automatic public exposure applies especially where identity-bearing material originates in sandbox reasoning, session continuity, or protected internal registration flows. Public exposure must be treated as a distinct outer transition, not as the default endpoint of successful internal promotion.

---

## 36.10 Identity, Consent, and Bounded Visibility

Identity governance in this architecture depends on bounded visibility.

A well-governed system should be able to preserve continuity without overexposing the person, agent, or identity-bearing structure to every downstream context. This is why the chapter pairs registration with disclosure control. To register is not necessarily to broadcast. To retain is not necessarily to reveal.

The architecture should therefore support visibility rules such as:

- visible only within the originating session;
- visible to approved internal continuity services;
- visible to a named identity-linked subsystem;
- visible under user or policy consent to a bounded external context;
- not visible publicly absent a separate disclosure basis.

Bounded visibility is what turns identity registration into a governed practice rather than a leakage path.

---

## 36.11 Transition Discipline

Identity and registration require transition discipline just as memory and promotion do.

A useful way to describe the structure is:

\[
I_{\mathrm{session}} \rightarrow I_{\mathrm{approved}} \rightarrow I_{\mathrm{registered}} \rightarrow I_{\mathrm{disclosed}}
\]

but each arrow is conditional rather than automatic. Session identity may never become approved identity. Approved identity-relevant state may never become durable registration. Registered identity may never become disclosed identity. Each movement must satisfy its own governance conditions.

This chapter therefore treats identity not as a static record but as a path of controlled transitions among differently authorized states. What matters is not only what identity exists, but how it became durable, who may see which projection of it, and under what consent or gate conditions it may travel further.

---

## 36.12 Closing Statement

Identity and registration in Ms. Allis are governed flows rather than a single container of selfhood. Sandbox session IDs, approved conclusions, and promotion scripts connect ephemeral session identity to durable identity-linked systems only through explicit retention and promotion paths.

The chapter distinguishes ephemeral session identity state from durable registered identity state, requires nested disclosure projections and consent-controlled escalation, and prohibits automatic public exposure. In this architecture, identity continuity is preserved by disciplined promotion and bounded disclosure rather than by collapsing session life, registration, and publicity into one undifferentiated state.
