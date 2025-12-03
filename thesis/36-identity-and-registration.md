# 36. Identity, Registration, and Two-Part Access Control

This chapter describes how identity and registration are handled when people use capabilities that can affect more than a single exchange. It sets out a two-step process for confirming who is behind certain actions, how sensitive details are kept separate from general data, and how this structure connects to barrier, container, and governance layers. The same approach applies to anyone using these capabilities, including the original builder, once the system is exposed online.

## 35.1 Why Strong Identity Controls Exist

Some interactions reach beyond ordinary questions and answers:

- Higher-impact operations:
  - Actions that touch shared records, cooperative arrangements, or infrastructure-related settings can affect many people, not just the current session.
- Traceable responsibility:
  - There needs to be a way to see which person initiated or approved these actions, under rules agreed by communities and partners.
- Protection against misuse:
  - Without friction, one person could create many fronts or trigger sensitive operations without any way to distinguish them from others.

These pressures make it necessary to do more than accept anonymous input when certain roles or tools are involved.

## 35.2 Two-Step Registration for People

For roles that unlock stronger capabilities, sign-up works in two stages:

- Document check:
  - A check against a real-world identifier, such as a state-issued document or similar record, to confirm that basic attributes match a real person.
- Live check:
  - A separate step that confirms that the person in front of the system matches the document, using a live sample rather than a static copy.

The intent is that any person, including the builder, who wants to use these elevated features goes through the same process. Everyday, lower-risk use can still be possible without this, but anything that can move shared levers requires it.

## 35.3 How Sensitive Details Are Treated

Details collected during registration are handled differently from normal interaction data:

- Kept apart:
  - Raw identifiers and live samples are stored in tightly restricted locations and never put into the general semantic stores or routine logs.
- Indirect references:
  - Internal components work with opaque keys and flags that point back to registration records, rather than seeing or passing around full personal details.
- Limited visibility:
  - Parts of the system that only need to know “this session is cleared for role X” see that fact, not the underlying documents or samples.

This setup is meant to keep personal information out of areas where it is not needed while still allowing strong ties between certain actions and real people.

## 35.4 How Roles and Abilities Are Connected

Registration state is linked directly to what a person can do:

- Roles:
  - Once confirmed, a person can be assigned one or more roles that define which tools, data views, or decision processes they can reach.
- Gates:
  - Actions such as proposing changes to shared infrastructure, adjusting cooperative settings, or touching sensitive collections require both an appropriate role and an active, confirmed registration state.
- Changes over time:
  - Roles and permissions can be raised, lowered, or removed as responsibilities change, or if new safety measures are introduced.

Checks based on this structure are applied where routes are chosen and where global settings are enforced.

## 35.5 How Identity Signals Enter Other Layers

Information about identity does not flow everywhere, but it does shape behavior:

- Barrier policies:
  - Rules that govern which sources and contents are allowed can differ depending on whether a request comes from a registered person, a general channel, or an automated process.
- Container and memory records:
  - Events involving higher-impact actions include pseudonymous keys and roles, so later analysis can see patterns in how different roles are used, without exposing raw personal data.
- Learning from use:
  - Aggregated views of how registered sessions interact can be used to refine prompts, routes, and safeguards, so the system learns from real use while still respecting privacy boundaries.

In this way, identity-related structure influences decisions and learning without turning personal details into general training material.

## 35.6 Oversight and Rules for Identity Use

The mechanisms described here are themselves under shared control:

- Policy setting:
  - Cooperative partners and other stakeholders define which actions require registration, what forms of evidence are acceptable, and how long different kinds of records are kept.
- Review:
  - Records of sign-ups and higher-impact actions can be checked to see whether the rules are being applied consistently and without favoritism.
- Change management:
  - As laws, norms, or local expectations shift, both written policies and technical implementations can be updated, with changes recorded so that people can see how and why the system evolved.

The goal is to make identity use something that communities can understand and shape, rather than a hidden, fixed feature.

## 35.7 Summary

The registration and access structure described here is meant to tie certain kinds of actions to real people in a controlled way. It uses a two-step check for roles that can affect shared settings, keeps sensitive details out of general data flows, and ties roles and abilities to registration state. In practice, this means that anyone who wants to use higher-impact capabilities, including the original builder, does so under the same rules. At the same time, aggregated signals from registered sessions help the system learn how to serve people better, without treating their personal details as general-purpose data.
