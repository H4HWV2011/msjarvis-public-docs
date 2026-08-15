# Chapter 54 — Pilot Trust Boundary

## 54.1 Purpose and Scope

This chapter defines the trust boundary governing the relationship between the MountainShares / Ms. Jarvis controlled-pilot environment and the administrative-production environment.

Its purpose is to prevent an operational, recovered, experimental, historical, or partially governed runtime from being represented as administrative production merely because selected services are healthy, reachable, responsive, or currently useful.

The chapter establishes the following governing principle:

> A recovered runtime is evidence of current behavior. It is not, by itself, an approved administrative-production authority.

The distinction is material. A service may be live, a dependency may return a health response, a model pipeline may complete, and a portal may render an answer while the surrounding environment remains outside administrative-production closure. Administrative production requires declared authority, reproducibility, immutable release binding, governed secret delivery, owned state, operational ownership, change control, and evidence that the live state conforms to the approved contract.

This chapter applies to:

- the recovered administrative core pair;
- all services and dependencies necessary to operate that pair;
- the Ms. Allis authenticated portal and asynchronous chat path;
- persistent stores used by retained administrative services;
- Docker containers, images, volumes, networks, ports, Compose projects, systemd units, scripts, scheduled tasks, and host-level automation;
- the historical `msjarvis-rebuild` aggregate environment;
- controlled pilots, candidates, recovery artifacts, and historical remnants that could affect administrative operation;
- all future promotion, migration, containment, decommissioning, rollback, and evidence activities.

This chapter does not establish that all listed components are approved for production. It defines the conditions under which they may be evaluated, retained, promoted, contained, migrated, or decommissioned.

## 54.2 Boundary Statement

The controlled pilot and administrative-production environments are separate trust domains.

The controlled pilot exists to conduct bounded evaluation, exercise selected capabilities, establish technical evidence, verify interfaces, observe failure behavior, and identify unresolved governance requirements. Pilot services, candidate images, temporary credentials, experimental routing, recovery procedures, and pilot-state data do not become administrative-production assets by continued operation or successful test results.

Administrative production exists to deliver approved capabilities through an explicit declarative lifecycle authority. It must be reproducible from approved manifests, bound to immutable releases, operated with governed secrets, supported by documented contracts, and recoverable through tested procedures.

The boundary is therefore not a label applied to a host or repository. It is an enforceable difference in authority and evidence.

A component belongs to administrative production only when all applicable requirements are satisfied:

1. Its purpose and classification are formally recorded.
2. Its lifecycle authority is explicit and singular.
3. Its release is bound to an approved immutable artifact.
4. Its dependencies and interfaces are declared.
5. Its secrets are delivered through an approved governed mechanism.
6. Its persistent data is owned and recoverable.
7. Its health, readiness, restart, and failure behavior are declared.
8. Its operators, escalation paths, and maintenance duties are assigned.
9. Its live state can be compared with the approved declared state using redacted evidence.
10. Its promotion has received the required approval.

No other condition substitutes for these requirements.

In particular, the following do not independently establish administrative-production status:

- a container being in a running state;
- a service responding on an expected port;
- an HTTP health endpoint returning success;
- a successful manual test;
- a completed multi-model response;
- a recovered service surviving a restart;
- an image being present on a host;
- a mutable image tag resolving successfully;
- a local environment file supplying required values;
- a historical Compose project continuing to run;
- a prior pilot approval;
- an undocumented manual recovery procedure.

## 54.3 Trust-Domain Definitions

### 54.3.1 Administrative Production

Administrative production is the governed runtime domain used to operate approved MountainShares / Ms. Jarvis administrative capabilities.

Administrative-production services must be under an approved declarative lifecycle owner and must satisfy the production-closure gates in this chapter.

Administrative production is responsible for:

- controlled operation of retained services;
- authorized administrative workflows;
- governed change and release management;
- security-boundary enforcement;
- persistent-state protection and recovery;
- evidence generation;
- incident response and rollback;
- protection against accidental control by historical, candidate, pilot, or unmanaged runtime authorities.

### 54.3.2 Controlled Pilot

The controlled pilot is an intentionally bounded domain for evaluating capabilities and collecting evidence without automatically granting production authority.

A pilot may include:

- candidate services;
- temporary integrations;
- experimental routing;
- prototype user experiences;
- non-production credentials;
- isolated datasets;
- manual interventions;
- test-only infrastructure;
- trial release artifacts;
- evidence-gathering workflows.

A controlled pilot may be useful, reliable, or operationally valuable. Those characteristics do not remove its pilot classification.

Promotion from pilot to administrative production requires explicit approval against the administrative-production requirements. Pilot success supplies evidence for promotion review; it does not constitute promotion.

### 54.3.3 Candidate

A candidate is a component, image, manifest, configuration, dependency, or operational procedure under evaluation for possible retention or promotion.

Candidate status means the item is not yet an approved lifecycle authority. It must not become the implicit owner of an administrative-production service.

Candidates may be deployed only within approved scope and must remain identifiable as candidates in inventories, manifests, labels, evidence, and operational records.

### 54.3.4 Historical Remnant

A historical remnant is a component, image, volume, network, service definition, script, environment file, archive, or host configuration retained from prior work but not currently approved as a lifecycle authority for administrative production.

Historical remnants are particularly important because they may retain hidden control paths, old credentials, mutable tags, implicit host dependencies, or conflicting service definitions.

The broad `msjarvis-rebuild` aggregate environment must be treated as a historical environment until each retained component has been individually classified and assigned a disposition.

### 54.3.5 Recovered Baseline

A recovered baseline is a runtime state restored or stabilized from an existing environment so that it can be inspected, tested, and brought under governance.

A recovered baseline may establish a useful operational starting point. It does not establish that the running configuration is reproducible, approved, immutable, secret-governed, or complete.

The recovered administrative baseline currently includes the core pair:

```text
jarvis-main-brain
jarvis-hilbert-state
```

This pair is treated as recovered administrative state pending full administrative-production closure.

## 54.4 Governing Promotion Rule

The promotion rule is:

> Production authority is declared, reviewed, and evidenced. It is never inferred from recovery, availability, convenience, or historical operation.

Before a component can be promoted into administrative production, the approving authority must be able to answer all of the following:

```text
What is this component?
Why is it retained?
Who owns its lifecycle?
Which manifest declares it?
Which immutable release artifact is approved?
Which dependencies does it require?
Which interfaces does it expose or consume?
How are its secrets delivered?
Who owns its persistent data?
How is it backed up and restored?
How is it monitored?
How does it fail?
How is it restarted?
How is it rolled back?
What evidence demonstrates that live state matches the approved contract?
```

If any answer is unavailable, incomplete, unreviewed, or dependent on undocumented host state, the component is not fully closed as administrative production.

A component may remain operational while it is being assessed, but its classification and limitations must remain explicit.

## 54.5 Administrative Recovery Status

The administrative environment has established a recovered local baseline for `jarvis-main-brain` and `jarvis-hilbert-state`.

This recovery establishes the following limited but meaningful facts:

- the identified core pair can run in the current administrative environment;
- the core pair can be inspected as live runtime evidence;
- the environment supports targeted health and dependency assessment;
- the recovered pair can serve as a starting point for declarative reconstruction;
- administrative closure work can proceed without treating the broad historical aggregate as automatically authoritative.

The recovery does not establish the following claims:

- that all dependencies are approved for administrative production;
- that all images are bound to approved immutable digests;
- that all runtime configuration is represented in source-controlled manifests;
- that secret delivery is fully governed;
- that all persistent stores have approved ownership and recovery procedures;
- that the broad `msjarvis-rebuild` environment has been safely decomposed or contained;
- that all legacy automation has been identified;
- that all service-to-service contracts are documented;
- that complete operational ownership is assigned;
- that all rollback procedures have been exercised.

The recovered baseline must therefore be described precisely as:

```text
Recovered administrative core baseline pending full production-closure governance.
```

It must not be described as fully closed administrative production until the gates in this chapter are satisfied.

## 54.6 Service Inventory Requirement

Administrative-production closure begins with a complete authoritative inventory.

The inventory must include every relevant runtime object in the broad historical and current environment, including:

```text
containers
images
image digests
volumes
networks
ports
Compose projects
systemd units
service files
environment files
secrets references
mounts
restart policies
health checks
scheduled tasks
cron entries
startup scripts
deployment scripts
CI/CD workflows
host-level reverse proxies
runtime labels
dependency references
persistent data stores
historical artifacts that can influence runtime behavior
```

The inventory must be captured before broad destructive, migratory, or decommissioning actions are performed.

The inventory is not merely a list of active containers. It is a map of every object capable of affecting lifecycle control, network reachability, persistence, credential delivery, startup, restart, deployment, recovery, or removal.

The inventory must identify whether an object is:

```text
running
stopped
referenced by a manifest
referenced by a systemd unit
referenced by a scheduled task
referenced by a script
referenced by a reverse proxy
bound to a host port
attached to a network
mounted to persistent state
using a mutable image reference
using a local secret source
dependent on a historical authority
```

## 54.7 Classification Requirement

Every inventoried object must receive one primary classification.

The approved classification vocabulary is:

```text
core-production
platform-dependency
data-service
security-boundary
controlled-pilot
candidate
historical-remnant
decommissioned
```

The classification must be recorded in the administrative service-classification ledger.

No retained production component may remain classified as `UNCLASSIFIED`.

A working ledger must include at least:

```csv
service_or_object,object_type,runtime_identifier,compose_project,image_reference,image_digest,classification,approved_lifecycle_owner,authority_manifest,network_exposure,persistent_state,secret_delivery,health_contract,dependency_contract,disposition,evidence_reference,review_status
```

The classification process must not assume that all currently running components should be retained. The purpose is to make retention, migration, containment, and decommissioning decisions explicit.

A classification is not itself a production approval. It is a prerequisite to approval.

## 54.8 Historical Aggregate Boundary

The historical `msjarvis-rebuild` aggregate environment must not retain implicit authority over the recovered administrative core or over any future retained production service.

The aggregate may contain valuable implementations, operational evidence, data dependencies, images, networks, persistent volumes, scripts, and service definitions. It may also contain conflicting lifecycle authorities, experimental dependencies, mutable images, pilot credentials, stale configuration, or implicit host-state assumptions.

Accordingly, the aggregate must be decomposed into individual components and classified before it is changed broadly.

The following actions are prohibited until dependency and rollback review is complete:

```text
docker compose down
docker rm
docker system prune
docker volume prune
broad network removal
bulk image deletion
bulk credential rotation without dependency mapping
migration of persistent volumes without tested restoration
replacement of shared network configuration without interface review
```

Each retained component must be assigned one of the following dispositions:

```text
retain under a new approved declarative owner
migrate to an approved administrative-production authority
contain as a controlled pilot or candidate
archive as historical evidence
decommission after approved rollback and state disposition
```

No component may be silently retained merely because it is difficult to classify.

## 54.9 Lifecycle Ownership Requirement

Every retained administrative-production service must have exactly one approved declarative lifecycle owner.

A lifecycle owner is the approved source of truth that defines how a service is created, configured, started, stopped, updated, monitored, recovered, and retired.

Acceptable lifecycle-owner forms include:

```text
runtime-authority/admin-production-compose
runtime-authority/admin-production-systemd
kubernetes/namespace-msjarvis-production
approved infrastructure repository and controlled deployment pipeline
```

Unacceptable lifecycle-owner forms include:

```text
a developer shell history
a manually started container
an undocumented host procedure
a historical Compose project with unclear scope
a recovery command copied from a terminal transcript
an image tag without an approved manifest
a stale environment file
an informal operator memory
```

The lifecycle authority must be source controlled and reviewed. It must specify the approved manifest path, release binding, configuration inputs, secret references, state dependencies, health contract, restart policy, interface contract, and rollback procedure.

Competing lifecycle authorities are prohibited. A retained service must not be simultaneously controlled by multiple Compose projects, systemd units, scripts, scheduled jobs, or manual recovery procedures.

The service-classification ledger must record the approved lifecycle owner for every retained production service.

## 54.10 Administrative Core Recovery and As-Built Status

The administrative environment has recovered and validated a limited operational baseline for the core pair:

```text
jarvis-main-brain
jarvis-hilbert-state
```

This recovery establishes a local administrative baseline from which the environment can be inventoried, assessed, governed, and progressively reconstructed under approved declarative authority.

The recovery must not be interpreted as a declaration that the complete historical stack is administrative production.

### 54.10.1 What Has Been Established

The recovered administrative baseline establishes the following operational facts:

- The identified core pair can run in the current administrative environment.
- The core pair can be inspected as live-state evidence.
- The environment supports targeted service health and dependency assessment.
- Administrative recovery work can proceed without treating the broad historical aggregate as automatically authoritative.
- The administrative portal can authenticate a session and submit an owned asynchronous Ms. Allis chat job.
- The job is persisted in Redis and scoped to the authenticated owner.
- The unified processing path can complete the full 21-model stage and return a synthesized result.
- The portal can wait for completion-aware job state rather than converting an extended request into a terminal browser timeout.
- The Next.js standalone frontend deployment has a defined static-asset synchronization procedure, and public portal script assets can be verified after deployment.

These facts are evidence of recovered capability. They are not substitutes for release approval, lifecycle ownership, immutable binding, governed secrets, state ownership, or complete operational readiness.

### 54.10.2 Ms. Allis As-Built Recovery

The recovered Ms. Allis administrative path operates as an authenticated asynchronous workflow.

The request flow is:

```text
Authenticated portal session
        |
        v
Administrative auth service
        |
        +--> Validate authenticated session
        +--> Create owner-scoped job identifier
        +--> Persist queued job state
        |
        v
Background unified-gateway request
        |
        v
Redis-backed running, completed, or failed job state
        |
        v
Authenticated portal status polling
        |
        v
Completed response rendered in the originating conversation
```

The administrative auth service creates a unique job identifier and records the authenticated owner before the background pipeline begins.

The job record is retained for a bounded operational period and contains a lifecycle state such as:

```text
queued
running
completed
failed
```

The status endpoint validates that the requester is the authenticated owner of the requested job before returning state or a completed result.

This prevents a job identifier from becoming a standalone bearer credential for another user’s conversation result.

### 54.10.3 Long-Running Completion Behavior

The recovered pipeline has demonstrated that a complete request may require several minutes to pass through the bounded 21-model workflow and final synthesis.

The browser-facing frontend must therefore not equate elapsed client wait time with job failure.

The current operational contract is:

```text
A browser submits a request and receives a job identifier quickly.

The server continues the work asynchronously.

The portal polls the owner-scoped status endpoint.

A queued or running job remains nonterminal.

A final response is rendered only after completed status is stored.

An error is shown only after explicit failed status is stored.
```

The portal polling implementation is completion-aware and no longer uses a terminal five-minute client timeout. It polls at a bounded interval while the job remains queued or running, may provide a nonterminal extended-processing notice, and continues until the server reports either `completed` or `failed`.

This behavior is required because a completed long-running job must not be represented as a failed request merely because the browser would otherwise stop waiting.

### 54.10.4 Frontend As-Built Deployment Control

The Ms. Allis portal is served as a Next.js standalone runtime.

Administrative recovery identified that a successful application build alone does not guarantee that the runtime serves all generated frontend assets. The standalone runtime must include the matching `.next/static` asset tree. If it does not, the public portal may reference a hashed JavaScript chunk that returns `404`, causing browser `ChunkLoadError` and MIME-type refusal.

The required frontend deployment sequence is:

```bash
cd /opt/msjarvis-rebuild/ms-allis-frontend-tsx

rm -rf .next
npm run build

mkdir -p .next/standalone/.next
rsync -a --delete .next/static/ .next/standalone/.next/static/

if [ -d public ]; then
  rsync -a --delete public/ .next/standalone/public/
fi

sudo systemctl restart ms-allis-frontend.service
```

Post-deployment verification must establish:

```text
The frontend systemd service is active.

The public portal HTML is served by the current runtime.

Every JavaScript chunk referenced in the public portal HTML returns HTTP 200.

Every referenced JavaScript chunk has an executable JavaScript content type.

A fresh browser session loads the portal without a missing-chunk, MIME-type, or ChunkLoadError condition.
```

This procedure is an as-built operational control for the recovered frontend. It does not replace the need to place the frontend service, its image or build artifact, its runtime configuration, and its deployment process under approved administrative lifecycle authority.

### 54.10.5 What Recovery Has Not Established

The recovered administrative core and Ms. Allis path do not establish any of the following without separate evidence and approval:

```text
Complete inventory of the broad historical environment.

Formal classification of every container, volume, network, image, port, service, script, and host-level authority.

A single approved declarative lifecycle owner for every retained production service.

Immutable approved image digest bindings for the recovered core pair and dependencies.

Complete version-controlled runtime authority manifests.

Declared health, readiness, restart, dependency, and failure contracts for all retained services.

Governed external production secret delivery.

Rotation of pilot, recovery, temporary, and pre-production credentials.

Documented ownership and tested recovery procedures for all persistent state.

Approved rollback procedures for containment, migration, or decommissioning.

Assigned operational ownership, incident response, and maintenance responsibilities.

A completed redacted contract-versus-live-state verification record.
```

The correct status statement is therefore:

```text
Recovered administrative operational baseline with validated asynchronous portal completion behavior; administrative-production closure remains subject to the requirements of this chapter.
```

### 54.10.6 Recovery Evidence Use

Recovery evidence must be preserved and used for assessment, not treated as a replacement for governance.

Appropriate recovery evidence includes:

```text
redacted container inspection records
redacted image inspection records
service logs
health and readiness observations
public frontend asset checks
authenticated asynchronous job lifecycle records
Redis job-state evidence
interface request and response evidence
runtime network and port inventory
systemd service definitions
Compose and manifest discovery results
```

Any raw evidence containing secrets, bearer tokens, API keys, database credentials, private material, or sensitive user information must remain protected and must not be published without review and redaction.

Recovery evidence supports the transition from unknown live state to governed declared state. It does not create authority by itself.

## 54.11 Immutable Image and Manifest Binding

Administrative-production services must be bound to approved immutable release artifacts.

A mutable image reference may be operationally convenient during development, pilot work, recovery, or candidate testing, but it does not provide sufficient release identity for administrative production. Tags can be changed, reused, retargeted, locally shadowed, or resolved differently across environments.

The authoritative production reference form is:

```yaml
image: registry.example.org/msjarvis/service-name@sha256:<approved-image-digest>
```

The digest must be approved in association with:

- the source revision;
- the build record;
- the software bill of materials;
- signature or attestation verification;
- the applicable policy revision;
- the release approval record;
- the runtime authority manifest revision;
- known operational constraints and dependency compatibility.

The following references are not sufficient as final administrative-production bindings:

```text
latest
main
stable
candidate
recovery
release without a digest
an image ID copied from a live host
a locally tagged image
an unqualified image name
```

A recovered image digest is evidence about the currently running artifact. It does not, by itself, establish that the artifact is approved for retention or promotion.

### 54.11.1 Recovered Core Pair

The recovered core pair must be inspected and represented in the authoritative inventory as it currently exists:

```text
jarvis-main-brain
jarvis-hilbert-state
```

The inspection record must capture at least:

```text
container name
container identifier
configured image reference
resolved image identifier
repository digest, if available
repository tags, if available
creation timestamp
runtime command
entrypoint
environment-variable names only
mounts
networks
published ports
restart policy
health configuration
labels
dependency references
```

The current image configuration must then be compared with the approved release manifest.

For `jarvis-hilbert-state`, any mutable image reference must be replaced during approved cutover with an immutable approved digest. The digest must be selected through the release-approval process, not inferred solely from the image currently running on the recovery host.

### 54.11.2 Runtime Authority Manifest

The core pair and every required retained dependency must be represented in version-controlled runtime authority manifests.

The manifest is the approved declaration of intended operation. It must be capable of recreating the intended service configuration without reliance on undocumented host state, interactive recovery commands, stale local files, or operator memory.

Each retained service manifest must include or reference:

```text
service identity
service classification
approved lifecycle owner
immutable image digest
source revision and build provenance reference
runtime command and entrypoint
non-root runtime identity
declared configuration inputs
secret references, never secret values
network attachments
published ports and internal ports
mounts and persistent-state references
health and readiness configuration
restart policy
resource constraints where required
dependency declarations
interface contracts
logging destination
observability endpoints
backup and restore references
rollback target
approval metadata
```

The manifest repository and deployment pipeline must be identified as part of the lifecycle ownership record.

A service is not declaratively governed if its required configuration exists only in:

```text
a shell command
a recovery transcript
a Docker inspect record
a local .env file
a manually edited container
a hidden host directory
an untracked Compose file
an ad hoc service override
```

### 54.11.3 Runtime Authority Is Distinct From Discovery

Docker inspection, running-container configuration, logs, and host state are discovery sources. They are not runtime authority manifests.

The administrative closure process must use live inspection to discover the current state, identify unknown dependencies, and produce a migration plan. It must then express the approved retained state in source-controlled manifests.

The required direction is:

```text
live recovered state
        |
        v
redacted inventory and evidence
        |
        v
reviewed classification and ownership
        |
        v
approved declarative runtime manifest
        |
        v
reproducible governed deployment
        |
        v
contract-versus-live verification
```

The direction must not be reversed. A live host must not become authoritative merely because it is difficult to reconstruct.

## 54.12 Declared Health, Readiness, and Dependency Contracts

Every retained administrative-production service must have declared health, readiness, restart, dependency, and failure contracts.

A service is not fully governed merely because it has a process ID, an open TCP port, or an HTTP endpoint that returns success.

The contract must distinguish at least:

```text
startup
readiness
liveness
degraded operation
dependency loss
transient failure
terminal failure
restart eligibility
operator intervention threshold
safe shutdown
recovery condition
```

### 54.12.1 Docker-Native Health Contracts

Where Docker is the runtime, retained services must define Docker-native health checks or an equivalent explicitly declared health mechanism appropriate to their runtime.

The health contract must identify:

```text
health command or endpoint
expected response
check interval
timeout
retry count
start period
unhealthy behavior
restart relationship
external alert condition
dependency assumptions
```

A service must not be marked healthy solely because a generic endpoint responds if the declared contract requires additional dependency checks.

For example, a service whose purpose depends on a state store, security policy service, model gateway, or required secret must define whether health means:

```text
process is alive
port is reachable
application accepts requests
required dependencies are reachable
required credentials are available
required policy material is loaded
required persistent state is available
full intended capability is available
```

These meanings must not be conflated.

### 54.12.2 Readiness Contracts

Readiness determines whether a service is prepared to receive production traffic or accept dependency calls.

Readiness must account for initialization that can occur after a process begins, including:

```text
configuration loading
secret retrieval
database connection
state migration
policy loading
model discovery
cache warming
dependency registration
message-bus subscription
index availability
network attachment
certificate availability
```

A service may be live but not ready. Routing traffic to a live-but-not-ready service is not an acceptable substitute for a declared readiness contract.

### 54.12.3 Restart and Failure Contracts

Each retained service must define:

```text
restart policy
restart trigger
restart limit
restart delay
dependency restart behavior
operator alert threshold
persistent-failure behavior
safe degradation behavior
manual intervention conditions
rollback trigger
```

The service contract must explain whether a dependency failure causes the service to:

```text
fail closed
return a bounded degraded response
queue work for later completion
retry with a bounded backoff
reject new work
continue with explicitly declared reduced capability
stop and require operator intervention
```

The declared behavior must be consistent with the service’s classification and security role.

Security-boundary services must not silently fail open.

## 54.13 Administrative Interface Contracts

Every retained service-to-service path must be documented as an interface contract.

The contract must identify:

```text
caller
callee
purpose
network path
DNS or host reference
port
protocol
request method
request shape
response shape
authentication mechanism
authorization expectation
timeout
retry policy
circuit-breaker or failure behavior
rate limit where applicable
data classification
logging behavior
audit behavior
health dependency
owner of each endpoint
```

Internal reachability is not equivalent to authorization. A service may be reachable through an internal Docker network while still requiring authentication, policy enforcement, or a constrained caller identity.

The administrative environment must not rely on undocumented paths such as:

```text
an assumed localhost port
an implicit container name
an inherited Docker network
a stale proxy route
an ad hoc host alias
an environment variable with no manifest declaration
a manually inserted firewall rule
```

### 54.13.1 Recovered Ms. Allis Chat Path

The recovered Ms. Allis path is an administrative interface whose boundary must remain explicit.

The intended administrative request path is:

```text
authenticated portal
        |
        v
administrative auth service
        |
        v
owned asynchronous job record
        |
        v
internal unified gateway
        |
        v
declared downstream processing stages
        |
        v
owned authenticated job-status retrieval
        |
        v
portal rendering of completed result
```

The browser does not receive direct authority to invoke the internal unified gateway as an unbounded public orchestration endpoint.

The administrative auth service is responsible for:

```text
session validation
user identification
quota or request-policy enforcement where configured
job identifier generation
job ownership persistence
job-state persistence
internal gateway invocation
safe terminal-state handling
status authorization
```

The unified gateway is responsible for pipeline processing within its declared administrative interface. It must not be treated as the authority for browser session validation.

### 54.13.2 Owner-Scoped Asynchronous Job Contract

The recovered asynchronous job model establishes an important boundary control.

The administrative auth service creates an owned job mapping before background execution begins.

The logical key form is:

```text
auth:unified_chat:job:<job_id>
auth:unified_chat:job_owner:<job_id>
```

The owner mapping binds the generated job identifier to the authenticated user identity recorded at submission time.

The job-status endpoint must validate that the current authenticated identity matches the stored owner before it returns job state or result data.

A requester with a job identifier but without the matching authenticated identity must not receive the job result.

The lifecycle states are:

```text
queued
running
completed
failed
```

A representative queued record is:

```json
{
  "status": "queued",
  "job_id": "<job-id>",
  "owner": "<authenticated-user-id>",
  "queued_at": "<UTC timestamp>"
}
```

A representative running record is:

```json
{
  "status": "running",
  "job_id": "<job-id>",
  "owner": "<authenticated-user-id>",
  "started_at": "<UTC timestamp>"
}
```

A representative completed record is:

```json
{
  "status": "completed",
  "job_id": "<job-id>",
  "owner": "<authenticated-user-id>",
  "completed_at": "<UTC timestamp>",
  "result": {
    "status": "complete",
    "response": "<final grounded response>"
  }
}
```

A representative failed record is:

```json
{
  "status": "failed",
  "job_id": "<job-id>",
  "owner": "<authenticated-user-id>",
  "error": "<safe user-facing failure description>",
  "failed_at": "<UTC timestamp>"
}
```

The durable job record allows a long-running request to complete after the original browser interaction would otherwise have expired.

### 54.13.3 Long-Running Processing Boundary

The full unified pipeline can run for several minutes. This is expected behavior for the current bounded multi-model processing path and cannot be safely represented as a single short-lived synchronous browser request.

The recovered workflow has demonstrated successful completion of all 21 model responses in long-running requests. The portal must therefore distinguish between:

```text
the browser waiting for a result
the asynchronous job continuing to run
the job reaching an explicit completed state
the job reaching an explicit failed state
```

A browser-side wait limit, reverse-proxy deadline, temporary network interruption, or page reload must not be treated as proof that the server-side durable job failed.

The portal polling contract is:

```text
submit request
receive job identifier
poll authenticated owned job status
continue while queued or running
render final result only when completed
render explicit error only when failed
```

The polling implementation has been updated to use completion-aware polling rather than a terminal fixed-duration client timeout.

The active behavior is:

```text
poll at a bounded interval
continue while the job remains queued or running
emit a nonterminal extended-processing notice when appropriate
continue polling after that notice
return the actual final response when the job becomes completed
stop with an error only when the job is explicitly failed
```

This ensures that a pipeline which completes after several minutes is represented as a completed request rather than as a false browser timeout.

## 54.14 Grounded Output and Administrative Claims

The completion of an asynchronous request does not authorize unsupported output.

The multi-model pipeline must remain grounded in authorized context, approved policy material, and permitted retrieval sources.

The recovered administrative behavior has demonstrated that when a requested fact is absent from the available Judge Context Packet or authorized grounded source, the response may state that the information is unavailable rather than inventing a policy, role, authority, or commitment.

This behavior is required.

The system must distinguish:

| Condition | Required behavior |
|---|---|
| Authorized grounded information is available | Provide only the supported answer |
| Available information is incomplete | State the limitation and avoid extrapolation |
| No authorized grounded information is available | Do not invent policy, roles, authority, or facts |
| Session identity is available | Report only authorized session claims |
| Real-world identity is not independently verified | Do not claim independent real-world identity verification |

The absence of authoritative data is a data-governance gap. It is not permission to relax the grounding boundary.

The administrative-production closure process must preserve this behavior even when operational pressure favors a more fluent but unsupported answer.

## 54.15 Governed Production Secret Delivery

Administrative production requires a governed secret-delivery model that is distinct from pilot, recovery, development, and local-host convenience mechanisms.

A secret may be necessary for a service to operate, but possession of a secret does not authorize an environment, image, container, script, or operator to be treated as production.

The administrative-production secret model must preserve the trust boundary by ensuring that sensitive values are delivered only to approved workloads, through approved identities, for approved purposes, with auditable rotation and recovery procedures.

The target state is governed external secret management compatible with non-root runtime identities.

The target state is not:

```text
an untracked .env file
a plaintext credential in a Compose file
a secret copied into a Docker image
a value embedded in a shell command
a token retained in shell history
a credential exposed in Docker inspect output
a secret placed in a repository
a local file treated as permanent production authority
a credential inherited from pilot or recovery work
```

### 54.15.1 Secret Classes

The administrative inventory must identify each secret-bearing input by class and intended scope.

The minimum classification includes:

```text
service-to-service credentials
API keys
database credentials
message-bus credentials
bearer tokens
session-signing material
encryption keys
TLS private keys
third-party integration credentials
registry credentials
backup-encryption material
break-glass credentials
operator credentials
pilot-only credentials
recovery-only credentials
```

Each secret record must identify:

```text
secret name or opaque identifier
owning service or authority
consuming workload
environment classification
delivery mechanism
rotation requirement
revocation method
expiry behavior
audit location
break-glass policy
recovery dependency
migration status
```

The record must not contain the secret value.

### 54.15.2 Non-Root Workload Identity

Retained administrative-production workloads must use non-root runtime identities unless a narrowly documented exception is approved.

Secret delivery must be compatible with those identities.

A valid production secret mechanism must support:

```text
least-privilege access
service-specific identity
non-root file or API access
time-bounded or renewable credentials where applicable
revocation
rotation without undocumented manual changes
auditability
separation between operator identity and workload identity
```

A secret file that is readable only by root does not satisfy the requirement if the retained workload is expected to run as a non-root user. Conversely, granting broad host-level permissions merely to make secret access work is not an acceptable production solution.

### 54.15.3 Migration From Local Recovery Delivery

The administrative recovery environment may contain temporary local secret delivery through environment files, local secret files, systemd environment overrides, Docker secrets, or host configuration.

These sources must be inventoried as discovery evidence and classified as temporary, transitional, pilot, recovery, or approved production mechanisms.

Before administrative-production closure:

1. Each retained secret consumer must be identified.
2. Each local or temporary secret source must be mapped to a governed replacement.
3. Workload identities and access policies must be defined.
4. The replacement delivery path must be tested without exposing values in evidence.
5. Required credentials must be rotated.
6. The previous secret source must be revoked, removed, or retained only under a documented time-bounded exception.
7. Logs, manifests, shell history, and evidence artifacts must be checked for accidental exposure.

The migration must not be performed as an unreviewed bulk replacement. Secret delivery often affects service startup, database connectivity, inter-service authentication, TLS, backup access, and recovery procedures.

### 54.15.4 Credential Rotation

All pilot, recovery, pre-production, temporary, and locally delivered credentials used by retained administrative-production services must be rotated during approved production cutover.

Rotation must include, as applicable:

```text
application API keys
service bearer tokens
database usernames and passwords
session-signing keys
encryption keys
registry credentials
third-party integration credentials
TLS private material
backup credentials
operator access credentials
break-glass credentials
```

A rotation plan must define:

```text
credential owner
affected consumers
rotation sequence
dual-read or overlap behavior where necessary
validation steps
revocation timing
rollback conditions
post-rotation evidence
incident response if rotation fails
```

No credential rotation is complete until the prior credential is revoked or its continuing exception is documented and approved.

### 54.15.5 Secret-Manager Outage and Recovery

The secret-management design must define expected behavior when the secret manager is unavailable.

The design must specify:

```text
startup behavior during secret-manager outage
runtime renewal behavior
cached-secret policy
maximum acceptable cached lifetime
failure mode
fail-open or fail-closed decision
operator notification
break-glass procedure
break-glass authorization
break-glass audit record
return-to-normal procedure
post-incident credential review
```

Security-boundary services must not silently fall back to broad static credentials or uncontrolled local files.

A break-glass procedure may exist, but it must be narrow, time bounded, auditable, and subject to post-use review.

## 54.16 Secret Exposure Prevention and Evidence Redaction

Administrative-production evidence must be useful for review without becoming a secret-distribution mechanism.

Raw runtime evidence may contain sensitive information, including environment variables, command arguments, container labels, mounted paths, connection strings, bearer tokens, database credentials, API keys, private material, user identifiers, and internal infrastructure details.

Raw evidence must remain protected.

Only reviewed redacted evidence may be shared outside the approved evidence boundary.

### 54.16.1 Prohibited Secret Locations

Secret values must not appear in:

```text
public repositories
public documentation
unredacted architecture diagrams
Dockerfiles
container image layers
Compose manifests
Kubernetes manifests
systemd unit files
shell history
terminal screenshots
chat transcripts
application logs
reverse-proxy logs
exception traces
evidence bundles
rendered CI logs
issue comments
pull-request descriptions
release notes
static frontend bundles
client-side source code
```

A reference to a secret identifier, secret path, or secret-management policy may be documented where necessary. The value itself must not be documented.

### 54.16.2 Redacted Evidence Workflow

The evidence workflow must separate raw capture from redacted publication.

The minimum process is:

```text
capture raw evidence in restricted storage
identify files that may contain secret material
produce redacted copies
scan redacted copies for likely secret indicators
review all scanner findings
correct redaction where necessary
hash the final redacted evidence set
publish or review only the redacted set
retain raw evidence according to restricted retention policy
```

A representative protected evidence structure is:

```text
evidence-root/
  raw/
  redacted/
  hashes/
  notes/
```

The raw directory must not be committed, published, attached to public issues, or copied into general documentation.

### 54.16.3 Redaction Stop Conditions

The following are stop conditions for evidence publication until reviewed and corrected:

```text
private-key headers
bearer tokens
API-key assignments
password assignments
database connection strings with embedded credentials
session-signing material
cloud-access key patterns
registry credentials
unredacted authorization headers
secret-manager recovery values
unredacted encrypted backup credentials
```

Suppressing scanner output is not remediation.

A publication candidate that contains a suspected secret must be manually reviewed, sanitized, and re-hashed before it is used as closure evidence.

## 54.17 Persistent-Data Governance

Persistent data must have explicit ownership, classification, recovery, retention, and migration governance.

A retained service is not administratively closed if its data depends on an undocumented host directory, an unmanaged Docker volume, an unowned database, a recovery-only snapshot, or an untested restoration procedure.

Every persistent store must have a record identifying:

```text
state-store name
service or organizational owner
data classification
physical or logical location
runtime consumer
backup mechanism
backup frequency
retention period
encryption requirement
restore procedure
restore test cadence
migration procedure
rollback procedure
decommission disposition
evidence reference
```

### 54.17.1 State Categories

The administrative inventory must distinguish among at least:

```text
authoritative business data
identity and authentication state
session state
application configuration state
job and queue state
audit state
policy state
model or retrieval indexes
cache state
derived analytics state
ephemeral runtime state
recovery artifacts
pilot-only data
historical data pending classification
```

The retention and recovery obligations for these categories differ. A cache may be reconstructable; an authoritative record may not be. A job-state store may be operationally temporary but still contain user-associated content requiring classification and retention controls.

### 54.17.2 Redis-Backed Job State

The recovered Ms. Allis asynchronous chat workflow uses Redis-backed job state.

The operational job keys include owner-scoped job records and owner mappings. These records permit a completed result to be retrieved after extended processing and after a browser-side request would otherwise have expired.

The Redis operational-state contract must define:

```text
Redis service owner
Redis runtime authority
network exposure
authentication requirement
encryption expectations
persistence mode
durability expectations
job retention period
key-expiration behavior
backup requirement
restore behavior
privacy classification of stored job content
access-control boundary
incident response for job-state loss
```

The current job retention behavior must not be confused with a complete data-retention policy. A time-to-live value is an implementation detail. The approved retention policy must define why the period exists, what it covers, and how it aligns with the data classification.

### 54.17.3 Recreate Without Undocumented Host State

The retained administrative core must be capable of recreation from approved manifests, approved artifacts, governed configuration, approved secret references, and documented state-recovery procedures.

The following must not be required for normal recreation:

```text
an undocumented host directory
a manually copied local image
a shell history command
a hidden environment file
a manually edited container
an undocumented network
a stale mounted volume
a recovery-only service override
an untracked generated configuration file
an operator's memory of a prior repair
```

If any such dependency is found, it must be added to the inventory and assigned one of these dispositions:

```text
formalize into the approved runtime authority
migrate into governed state
replace with an approved mechanism
contain as transitional recovery state
decommission after safe migration
```

### 54.17.4 Backup, Restore, and Migration Testing

Backup existence is not sufficient evidence of recoverability.

Each retained persistent store must have tested procedures for:

```text
backup creation
backup integrity validation
restricted backup access
backup retention
restore to an isolated target
application-level validation after restore
migration to an approved target
rollback from a failed migration
decommission of the prior store
```

The restoration test must produce redacted evidence and must not expose sensitive payloads in public records.

## 54.18 Change Governance

Administrative-production changes require explicit governance before mutable operations are performed.

A change record must identify:

```text
change objective
scope
affected services
affected interfaces
affected secrets
affected persistent stores
approved manifest revision
approved image digest
pre-change evidence
implementation steps
success criteria
failure criteria
rollback procedure
rollback owner
approval threshold
maintenance window where applicable
post-change verification
evidence retention location
```

The change process must distinguish between:

```text
read-only discovery
evidence capture
candidate testing
controlled pilot modification
administrative recovery
approved production change
emergency break-glass action
decommissioning
```

These categories have different approval, evidence, and rollback expectations.

### 54.18.1 Pre-Change Evidence

Before a mutable change, capture sufficient redacted evidence to establish:

```text
current running state
current image binding
current network attachment
current ports
current mounts
current health state
current dependency state
current secret-delivery method
current persistent-state references
current lifecycle owner
current rollback position
```

The evidence must be adequate to distinguish a successful change from an accidental drift or partial rollback.

### 54.18.2 Post-Change Evidence

After a mutable change, the operator must verify:

```text
the intended declarative authority is active
the intended immutable artifact is running
the expected non-root identity is in use
the expected health and readiness contracts pass
approved interfaces function as declared
unapproved interfaces remain unavailable
state stores remain accessible and consistent
secret delivery works through the approved mechanism
no historical authority reclaimed control
rollback remains available
redacted evidence has been captured and integrity-bound
```

A successful service start is not sufficient post-change evidence.

### 54.18.3 Rollback Requirement

Every approved production change must have a tested or testable rollback path before it is made irreversible.

The rollback record must identify:

```text
rollback trigger
rollback authority
rollback artifact or manifest revision
state compatibility assumptions
data-loss risk
secret compatibility requirements
network compatibility requirements
validation steps after rollback
conditions requiring incident declaration
```

A rollback that depends on an undocumented host state is not a valid production rollback.

## 54.19 Operational Readiness and Administrative Ownership

Administrative-production closure requires named operational ownership. Technical operation without identified responsibility is not a closed production condition.

For every retained administrative-production service, the administrative record must identify:

```text
service owner
technical operator
platform owner
security owner
data owner
release approver
rollback authority
incident commander
on-call or escalation contact
maintenance owner
backup and restore owner
secret-rotation owner
evidence-review owner
```

One individual or team may hold more than one role where approved, but each responsibility must be explicit.

The ownership model must distinguish between:

```text
the person or team that operates a service
the authority that approves changes
the authority that owns data
the authority that owns the runtime platform
the authority that accepts residual risk
the authority that may authorize break-glass actions
```

These distinctions matter especially where a recovered environment is being brought under administrative control. The person who recovered a component is not automatically the ongoing production owner, and the team operating an infrastructure dependency is not automatically the owner of every workload that depends on it.

### 54.19.1 Incident Response

Every retained service must have an incident response path proportionate to its classification.

The incident record must define:

```text
detection source
severity criteria
initial responder
escalation path
service owner
security escalation path
data-owner notification requirement
containment options
rollback options
communication responsibility
evidence capture requirement
post-incident review requirement
```

Security-boundary services, identity services, secret-delivery systems, policy-enforcement services, and authoritative state stores require heightened incident handling because failures may affect authorization, confidentiality, integrity, or availability across multiple services.

### 54.19.2 Maintenance Responsibilities

Maintenance responsibilities must include:

```text
patch cadence
dependency update process
image refresh policy
artifact approval process
certificate renewal
secret rotation
backup verification
restore testing
capacity review
health-contract review
interface-contract review
log-retention review
evidence-retention review
decommission review
```

A component that has no named maintenance responsibility must not be retained as administrative production merely because it is currently working.

### 54.19.3 Administrative Readiness Record

Administrative readiness should be recorded for each retained production service using a structured record.

A minimum record is:

```text
service:
classification:
lifecycle owner:
manifest path:
approved image digest:
service owner:
platform owner:
security owner:
data owner:
on-call or escalation path:
health contract:
readiness contract:
dependency contract:
secret-delivery mechanism:
persistent-state owner:
backup procedure:
restore-test evidence:
rollback procedure:
last contract-versus-live verification:
open exceptions:
approval status:
```

The readiness record must be updated as part of approved changes, not only during initial promotion.

## 54.20 Contract-Versus-Live-State Verification

Administrative production requires a repeatable method to compare approved declared state with the live runtime state.

The purpose is to identify drift, undisclosed dependencies, unexpected exposure, stale artifacts, conflicting lifecycle ownership, and recovery-state assumptions before they become production incidents.

The verification process must be able to produce redacted evidence suitable for administrative review.

### 54.20.1 Required Comparison Categories

The approved manifest and the live runtime must be compared for each retained service across, at minimum:

```text
service identity
classification
lifecycle owner
image reference
image digest
entrypoint
command
runtime identity
environment input names
secret references
network attachments
published ports
internal ports
reverse-proxy routes
mounts
persistent volumes
restart policy
health checks
readiness behavior
dependency references
resource controls where declared
labels
log destination
observability endpoint
backup references
rollback reference
```

The comparison must identify whether the live object is:

```text
conformant
drifted
unknown
partially conformant
temporarily excepted
not applicable
decommissioned
```

A conformity result must be attributable to specific redacted evidence.

### 54.20.2 Live-State Discovery Sources

Live-state verification may draw on:

```text
docker container inspection
docker image inspection
docker volume inspection
docker network inspection
Docker Compose project inventory
systemd unit definitions
systemd runtime state
listening-port inventory
reverse-proxy configuration
service health endpoints
service readiness endpoints
service logs
manifest repository state
approved release metadata
secret-manager audit records
backup-system records
network-policy records
runtime labels
host mount information
```

Live discovery sources are evidence sources. They do not become authoritative configuration merely because they reveal current behavior.

### 54.20.3 Drift Handling

A detected difference between live state and declared state must be handled explicitly.

The permitted outcomes are:

```text
remediate the runtime to match the approved manifest
update the manifest through approved change control
contain the component as candidate or recovery state
record a time-bounded approved exception
decommission the component
```

Silent drift acceptance is prohibited.

The verification record must identify:

```text
the drifted field
the expected value or condition
the observed value or condition
the impact assessment
the responsible owner
the remediation or exception decision
the due date
the approval reference
the follow-up evidence
```

### 54.20.4 Redacted Verification Evidence

The contract-versus-live comparison must produce evidence without exposing secret values or unnecessary sensitive infrastructure detail.

A useful evidence package includes:

```text
inventory snapshot
classification ledger
manifest revision identifier
image-digest comparison
service and dependency matrix
network and port comparison
mount and state comparison
health-contract comparison
secret-delivery mechanism comparison
open drift and exception register
integrity hash manifest
```

Raw inspection output may be retained in restricted storage. The redacted comparison output is the reviewable administrative artifact.

## 54.21 Historical Aggregate Containment

The broad historical `msjarvis-rebuild` environment must be treated as an aggregate requiring controlled decomposition and containment.

It must not be assumed that the aggregate is a valid production lifecycle owner. It may contain overlapping service definitions, recovery artifacts, outdated images, candidate workloads, pilot configuration, unmanaged volumes, stale networks, or automation that can interfere with recovered administrative services.

The containment objective is:

```text
Prevent historical aggregate state from unintentionally creating,
restarting, modifying, routing to, credentialing, or otherwise
reclaiming control of retained administrative-production services.
```

### 54.21.1 Dependency Mapping Before Change

Before a historical component is stopped, removed, migrated, or isolated, the administrative team must identify:

```text
dependent services
dependent networks
persistent volumes
shared mounts
shared secrets
reverse-proxy routes
published ports
scheduled jobs
systemd dependencies
Compose-project references
image dependencies
external clients
backup dependencies
recovery dependencies
rollback dependencies
```

A component may not be decommissioned safely merely because it appears unused in a short container listing.

### 54.21.2 Containment Options

A historical component may be handled through one of the following approved dispositions:

```text
retain and formalize under an approved administrative lifecycle owner
migrate to an approved production manifest and state contract
contain as a controlled pilot
contain as a candidate
archive as historical evidence
decommission after approved dependency, state, and rollback review
```

Containment must be deliberate. A component that remains running but has no production owner must be visible in the classification ledger as controlled pilot, candidate, or historical remnant.

### 54.21.3 Prohibited Broad Actions

The following actions are prohibited until required inventory, dependency analysis, state disposition, approval, and rollback conditions are satisfied:

```text
docker compose down against a broad historical project
docker system prune
docker volume prune
bulk container removal
bulk image removal
bulk network removal
bulk credential revocation
bulk host-path deletion
replacement of shared reverse-proxy configuration
mass migration of persistent volumes
undeclared host reboot as a decommissioning substitute
```

These actions can destroy recovery evidence, break undeclared dependencies, remove rollback paths, expose data-loss conditions, or allow a historical authority to reappear unpredictably during recovery.

### 54.21.4 Historical Authority References

The administrative inventory must locate potential lifecycle authorities and control paths, including:

```text
Compose files
Docker Compose project labels
systemd units
systemd drop-ins
cron jobs
at jobs
shell scripts
deployment scripts
CI/CD configuration
environment files
reverse-proxy configuration
host startup files
user-level services
Docker restart policies
volume mounts
network definitions
image build scripts
registry pull scripts
backup scripts
recovery scripts
```

References to the historical aggregate must be recorded for review.

A component cannot be considered contained until the team can explain whether historical automation can still alter it.

## 54.22 Evidence Baseline and Inventory Procedure

Administrative-production closure requires a complete, protected, redacted evidence baseline before significant mutable changes are made.

The evidence baseline creates a factual starting point for classification, manifest creation, release binding, change control, and rollback planning.

The initial evidence workspace should be separate from public repositories and should use restrictive permissions.

A representative capture context includes:

```text
as-built identifier
capture time in UTC
host identifier
operator identity
operator identifier
applicable documentation revision
manifest repository revision
change-record identifier
```

### 54.22.1 Required Inventory Artifacts

The inventory must capture, at minimum:

```text
Docker engine version
Docker engine information
container inventory
image inventory
volume inventory
network inventory
Compose project inventory
Docker disk usage
listening-port inventory
container inspection output
image inspection output
volume inspection output
network inspection output
container ledger
systemd service inventory
systemd service runtime state
candidate runtime files
runtime-authority references
historical aggregate membership
targeted core-service inspection
targeted core-service logs
targeted core-image bindings
```

The inventory process must be read-only unless a separately approved change is underway.

### 54.22.2 Container Ledger

The container ledger must provide an initial concise view suitable for classification.

A representative ledger includes:

```text
container identifier
container name
image reference
runtime status
published ports
Compose project label
other relevant labels
classification
lifecycle owner
manifest reference
disposition
review status
```

The ledger is an administrative working artifact. It must be updated as classifications and dispositions are approved.

### 54.22.3 Targeted Core Evidence

The recovered core pair requires targeted evidence capture because it is the current administrative baseline.

Targeted evidence for `jarvis-main-brain` and `jarvis-hilbert-state` must include:

```text
container inspection
tail logs with timestamps
configured image reference
resolved image identifier
repository digests where available
repository tags where available
network attachments
mounts
published ports
restart policy
health configuration
labels
dependency references
```

The resulting evidence supports the move from recovered state to approved manifest binding. It does not itself authorize the running state as production.

### 54.22.4 Evidence Integrity Binding

The redacted evidence set must be integrity-bound.

A cryptographic hash manifest must be generated over the final redacted files after redaction review is complete.

The hash manifest must be retained with the associated change or closure record.

If evidence is updated, it must receive a new capture identifier and hash manifest. Historical evidence must not be silently overwritten.

## 54.23 Administrative Production Closure Gates

Administrative production is not closed until every required gate is approved or an explicit documented exception is accepted by the appropriate authority.

The required closure gates are:

1. The authoritative inventory is complete.
2. Every relevant runtime object has a recorded classification.
3. Every retained production service has exactly one approved declarative lifecycle owner.
4. The historical aggregate has an approved containment, migration, archival, or decommissioning plan.
5. The recovered core pair and required dependencies are represented by approved version-controlled manifests.
6. Each retained service is bound to an approved immutable image digest.
7. Required SBOM, provenance, signature, or attestation evidence is available for retained images.
8. Health, readiness, restart, dependency, and failure contracts are declared.
9. Service-to-service interfaces are documented and tested.
10. Network exposure and reverse-proxy routing are approved and documented.
11. External governed secret delivery is implemented for retained production workloads.
12. Pilot, recovery, temporary, and pre-production credentials have been rotated or explicitly excepted.
13. Persistent-state ownership, backup, restoration, retention, migration, and rollback procedures are approved and tested.
14. Operational ownership, on-call, maintenance, and incident response responsibilities are assigned.
15. Contract-versus-live verification produces redacted evidence.
16. Change-control and rollback procedures have been established and exercised.
17. Historical automation cannot unintentionally reclaim authority over retained production services.
18. Open exceptions have named owners, risk acceptance, remediation dates, and review requirements.

The existence of an open gate means the environment must be described accurately as recovered, transitional, candidate, pilot, or partially governed according to its recorded classification.

It must not be described as fully closed administrative production.

## 54.24 Administrative As-Built Status Statement

The MountainShares / Ms. Jarvis administrative environment has established a recovered operational baseline. It has not yet established complete administrative-production closure for the broad historical environment.

The current status must be stated accurately:

```text
Recovered administrative operational baseline with validated core-pair recovery,
authenticated owner-scoped asynchronous chat execution, durable job-state retrieval,
completion-aware long-running portal polling, and verified standalone frontend asset delivery.

Administrative-production closure remains conditional on completion of the governance,
manifest, immutable-release, secret, state, operational-ownership, and
contract-versus-live verification requirements defined in this chapter.
```

This statement recognizes completed recovery work without overstating the maturity or governance status of the environment.

### 54.24.1 Verified Recovered Capabilities

The following capabilities have been established and may be represented as verified recovered administrative functionality:

```text
Recovered local baseline for jarvis-main-brain and jarvis-hilbert-state.

Authenticated portal access through the administrative Ms. Allis path.

Administrative auth-service ownership of asynchronous Ms. Allis job creation.

Unique job identifiers bound to the authenticated submitting user.

Redis-backed queued, running, completed, and failed job-state persistence.

Authenticated owner validation before chat-job status or result retrieval.

Internal asynchronous submission from the auth service to the unified gateway.

Long-running processing through the declared multi-model pipeline.

Observed completion of all 21 model responses in the active processing stage.

Completion-aware frontend polling that does not end the job because a fixed
five-minute client deadline has elapsed.

Nonterminal extended-processing status behavior while a durable job remains active.

Return of the final completed response to the originating portal conversation.

Next.js standalone frontend asset synchronization after build.

Verification that JavaScript assets referenced by the public portal are available
from the active standalone frontend runtime with executable JavaScript content types.

Grounded-response behavior that does not invent unsupported policy or role claims
when the authorized context does not contain the required information.
```

These verified capabilities do not waive any remaining administrative-production closure requirement.

### 54.24.2 Explicit Non-Claims

The following claims must not be made until separate evidence and approvals are complete:

```text
The entire historical msjarvis-rebuild aggregate is administrative production.

All current containers are approved retained services.

All running images are approved immutable releases.

All lifecycle authority has been consolidated under one approved declarative owner.

All secrets are governed through an external production secret manager.

All pilot, recovery, temporary, and pre-production credentials have been rotated.

All persistent data has named ownership and tested backup, restore, migration,
retention, and rollback procedures.

All inter-service interfaces have approved, tested contracts.

All health, readiness, restart, dependency, and failure behaviors are declared.

All operational roles, on-call duties, incident procedures, and maintenance
responsibilities have been assigned.

All historical automation has been located and prevented from reclaiming authority.

A full contract-versus-live-state evidence package has been reviewed and approved.

Administrative-production closure has been completed.
```

A recovered capability must not be used to imply completion of a broader governance requirement.

## 54.25 Required Closure Evidence

The final administrative-production closure decision must be supported by a redacted evidence package.

The evidence package must be sufficient for an independent authorized reviewer to determine:

```text
what is retained
what is decommissioned
who owns each retained service
which manifests are authoritative
which immutable artifacts are approved
how secrets are delivered
how data is recovered
how services are monitored and operated
how interfaces are secured
how rollback occurs
how live state conforms to declared state
which exceptions remain
who accepted each exception
```

### 54.25.1 Minimum Evidence Set

The minimum closure evidence set includes:

```text
authoritative inventory snapshot
service-classification ledger
lifecycle-owner mapping
approved runtime authority manifest inventory
immutable image-digest binding record
release provenance, SBOM, signature, or attestation references
network and interface contract matrix
health, readiness, restart, and failure-contract matrix
secret-delivery architecture and rotation record
persistent-state ownership and recovery matrix
backup and restore test evidence
migration and rollback evidence
operational ownership and incident-response record
contract-versus-live comparison report
drift and exception register
historical aggregate containment or decommissioning record
redaction review record
hash manifest for redacted evidence
final approval record
```

The evidence package may reference restricted internal records where necessary, but it must not include secret values or unnecessary sensitive operational details.

### 54.25.2 Evidence Currency

Evidence must be current enough to support the decision being made.

A stale inventory, old image-digest record, expired health result, prior secret rotation record, or historical backup test cannot establish the condition of a newly changed environment without an explicit approved rationale.

The closure record must identify:

```text
evidence capture period
applicable manifest revisions
applicable image digests
applicable policy versions
applicable secret-rotation state
applicable state-store versions
applicable approval record
```

### 54.25.3 Evidence Integrity

All redacted evidence submitted for closure must be integrity-bound.

The evidence package must include:

```text
file inventory
cryptographic hash manifest
capture identifier
capture timestamp
operator identity
host or environment identifier
redaction review record
revision references
```

If any material evidence is changed after hashing, the package must be re-hashed and its supersession recorded.

## 54.26 Exception Management

An exception does not erase a production requirement. It records a temporary, reviewed deviation while preserving accountability for remediation.

An exception may be used only when:

```text
the affected requirement is identified
the reason for nonconformance is documented
the risk is assessed
compensating controls are defined
an accountable owner is named
an expiration date is recorded
a remediation plan exists
the appropriate approval authority accepts the risk
the exception is included in the contract-versus-live report
```

The exception register must contain:

```text
exception identifier
affected service or object
affected requirement
observed condition
risk description
compensating controls
owner
approval authority
approval date
expiration date
remediation milestone
verification method
closure condition
status
```

Exceptions must not be used to permanently normalize:

```text
unowned services
mutable production images
plaintext secret delivery
untested restore procedures
undocumented dependencies
unreviewed network exposure
unknown lifecycle authority
unbounded historical aggregate control
unapproved persistent state
missing rollback paths
```

Expired exceptions must be treated as nonconformances until renewed through the appropriate approval process or remediated.

## 54.27 Promotion Decision Record

Promotion of a service, dependency, or recovered baseline into administrative production requires an explicit decision record.

The decision record must state:

```text
promotion scope
service or component identifiers
classification
approved lifecycle owner
authoritative manifest revision
approved immutable image digest
approved interfaces
approved secret-delivery mechanism
approved persistent-state contract
health and readiness contract
dependency and failure contract
operational ownership
evidence package identifier
open exceptions
rollback plan
approval authorities
effective date
review date
```

The decision must use one of the following outcomes:

```text
approved for administrative production
approved with time-bounded exceptions
retained as controlled pilot
retained as candidate
retained as historical remnant
requires remediation before approval
approved for decommissioning
decommissioned
```

The decision record must not use ambiguous outcomes such as:

```text
probably production
working well enough
operational for now
assumed approved
legacy but required
temporary forever
```

## 54.28 Administrative Closure Sequence

The recommended administrative-production closure sequence is:

```text
1. Capture protected raw inventory and evidence.

2. Produce reviewed redacted inventory artifacts and integrity hashes.

3. Classify every object in the historical and current environment.

4. Identify every lifecycle authority and conflicting control path.

5. Assign one approved declarative lifecycle owner to each retained production service.

6. Define retained, migrated, contained, archived, and decommissioned dispositions.

7. Create or approve version-controlled runtime authority manifests.

8. Bind retained images to approved immutable digests.

9. Declare service health, readiness, restart, dependency, interface, and failure contracts.

10. Implement governed external secret delivery and rotate pre-production,
    pilot, recovery, and temporary credentials.

11. Define persistent-state ownership, backup, restoration, retention,
    migration, and rollback procedures.

12. Assign operational roles, incident ownership, maintenance duties,
    and on-call escalation.

13. Perform redacted contract-versus-live verification.

14. Resolve drift or record time-bounded approved exceptions.

15. Test rollback and restoration procedures.

16. Contain, migrate, archive, or decommission historical aggregate components
    only after their dependencies and rollback paths are understood.

17. Assemble and integrity-bind the final closure evidence package.

18. Obtain the required approval decision.

19. Continue recurring verification after approval.
```

The sequence may be iterated as new dependencies or drift are discovered. Iteration is not a failure; it is an expected outcome of moving from recovered state to governed declared state.

## 54.29 Final Boundary Rule

The final administrative-production boundary rule is:

> No service, image, volume, network, secret, state store, script, workflow, or host configuration becomes administrative production by implication.

It becomes administrative production only through explicit classification, declared lifecycle ownership, immutable release binding, governed secret delivery, owned state, documented operational contracts, verified live-state conformity, and authorized approval.

The inverse rule is equally important:

> A recovered, pilot, candidate, or historical component remains outside administrative production until it has been explicitly promoted.

This rule protects the MountainShares / Ms. Jarvis administrative environment from accidental authority transfer, hidden historical dependencies, undeclared state, mutable releases, secret exposure, and unsupported production claims.

## 54.30 Continuing Obligations

Administrative production is not a one-time state achieved only at initial closure.

After approval, the environment must continue to enforce:

```text
immutable release review
manifest review
secret rotation
credential revocation
backup verification
restore testing
health-contract review
dependency-contract review
interface review
network exposure review
drift detection
exception review
incident review
rollback testing
operational ownership review
decommission review
evidence refresh
```

A service may lose administrative-production conformity through drift, expired credentials, obsolete dependencies, unsupported images, missing backups, changed interfaces, unreviewed configuration, or ownership changes.

The closure model therefore requires recurring verification, not a permanent assumption of compliance.

## 54.31 Closing Statement

The MountainShares / Ms. Jarvis administrative environment may operate from a recovered baseline while it is being brought under full governance.

The recovered baseline is valuable because it provides concrete evidence of current behavior, including authenticated asynchronous job ownership, durable result retrieval, long-running completion-aware portal behavior, and verified frontend asset delivery.

Those accomplishments must be preserved.

They must also be described accurately.

They do not replace the remaining work required to establish complete administrative production:

```text
authoritative inventory
classification
single declarative lifecycle ownership
immutable release binding
approved manifests
declared interfaces and health contracts
governed secret delivery
credential rotation
persistent-state governance
backup and restore testing
rollback governance
operational ownership
redacted contract-versus-live verification
historical aggregate containment or decommissioning
formal approval
```

The trust boundary remains intact only when recovery evidence is used to build governed authority rather than being mistaken for governed authority itself.
