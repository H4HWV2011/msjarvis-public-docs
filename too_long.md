(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ grep -Rni "async def register\|@app.post(\"/auth/register\"\|@router.post(\"/auth/register\"" /opt/msjarvis-rebuild /opt/msjarvis-rebuild/ms-allis-auth-install --include="*.py" | head -20
/opt/msjarvis-rebuild/_archive/generated_20260430/ms_jarvis_unified_swagger_gateway_BACKUP.py:312:async def register_user(
/opt/msjarvis-rebuild/_archive/generated_20260430/ms_jarvis_unified_swagger_gateway_BACKUP.py:359:async def register_user(
/opt/msjarvis-rebuild/_archive/generated_20260430/ms_jarvis_unified_swagger_gateway_BACKUP.py:397:async def register_stage1(
/opt/msjarvis-rebuild/_archive/generated_20260430/ms_jarvis_unified_swagger_gateway_BACKUP.py:429:async def register_stage2(
/opt/msjarvis-rebuild/_archive/generated_20260430/dgm_supervisor_woah.psychology_patched.py:150:async def register_service(service: ServiceRegistration):
/opt/msjarvis-rebuild/_archive/service_baks_20260430/ms_jarvis_main_gateway.backup_error.py:312:async def register_user(
/opt/msjarvis-rebuild/_archive/service_baks_20260430/ms_jarvis_main_gateway.backup_error.py:359:async def register_user(
/opt/msjarvis-rebuild/_archive/service_baks_20260430/ms_jarvis_main_gateway.backup_error.py:456:async def register_stage1(
/opt/msjarvis-rebuild/_archive/service_baks_20260430/ms_jarvis_main_gateway.backup_error.py:489:async def register_stage2_proxy(request: Request):
/opt/msjarvis-rebuild/_archive/service_baks_20260430/ms_jarvis_main_gateway.backup_error.py:503:async def register_complete_proxy(ueid: str = None):
/opt/msjarvis-rebuild/_archive/service_baks_20260430/ms_jarvis_main_gateway.backup_1762220815.py:312:async def register_user(
/opt/msjarvis-rebuild/_archive/service_baks_20260430/ms_jarvis_main_gateway.backup_1762220815.py:359:async def register_user(
/opt/msjarvis-rebuild/_archive/service_baks_20260430/ms_jarvis_main_gateway.backup_1762220815.py:397:async def register_stage1(
/opt/msjarvis-rebuild/_archive/service_baks_20260430/ms_jarvis_main_gateway.backup_1762220815.py:429:async def register_stage2(
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/redis/asyncio/multidb/failure_detector.py:8:    async def register_failure(self, exception: Exception, cmd: tuple) -> None:
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/redis/asyncio/multidb/failure_detector.py:13:    async def register_command_execution(self, cmd: tuple) -> None:
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/redis/asyncio/multidb/failure_detector.py:31:    async def register_failure(self, exception: Exception, cmd: tuple) -> None:
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/redis/asyncio/multidb/failure_detector.py:34:    async def register_command_execution(self, cmd: tuple) -> None:
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/redis/asyncio/multidb/failure_detector.py:8:    async def register_failure(self, exception: Exception, cmd: tuple) -> None:
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/redis/asyncio/multidb/failure_detector.py:13:    async def register_command_execution(self, cmd: tuple) -> None:
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ sed -n '1,260p' /opt/msjarvis-rebuild/ms-allis-auth-install/backend/auth_router.py 2>/dev/null
sed -n '1,220p' /opt/msjarvis-rebuild/auth_api.py.bak-cors 2>/dev/null
"""
Ms. Allis Auth + Application FastAPI service.
Routes:
  POST /apply          — submit Community Champion application
  GET  /login          — magic link token handler → sets cookie → redirect
  GET  /me             — current user profile (wallet, UEI, quota)
  POST /chat           — authenticated proxy to Egeria :18018
  GET  /health         — liveness check
"""
import os, json, httpx
from datetime import datetime, timezone
from dotenv import load_dotenv
load_dotenv()

import redis
from fastapi import FastAPI, Request, Response, Cookie, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr, field_validator

from services.token_service   import TokenService
from services.wallet_service  import WalletService

REDIS_URL    = os.getenv("REDIS_URL",    "redis://localhost:6379/0")
JARVIS_URL   = os.getenv("JARVIS_URL",   "http://localhost:18018")
JARVIS_TOKEN = os.getenv("JARVIS_TOKEN", "internal")
RESEND_KEY   = os.getenv("RESEND_API_KEY", "")
ADMIN_EMAIL  = os.getenv("ADMIN_EMAIL",  "kiddstechnical@gmail.com")
PORTAL_URL   = os.getenv("PORTAL_URL",   "https://egeria.mountainshares.us")
AGREEMENT_VERSION = "2026-04-25"

r  = redis.from_url(REDIS_URL, decode_responses=True)

def get_r():
    return r
ts = TokenService(r)
ws = WalletService(r)

app = FastAPI(title="Ms. Allis Auth API", version="1.0.0")

# ── Models ────────────────────────────────────────────────────────────────────

class ApplicationRequest(BaseModel):
    name:               str
    email:              EmailStr
    county:             str
    motivation:         str
    agreement_accepted: bool

    @field_validator("name")
    @classmethod
    def name_required(cls, v):
        if not v.strip():
            raise ValueError("name is required")
        return v.strip()

    @field_validator("motivation")
    @classmethod
    def motivation_length(cls, v):
        if len(v.strip()) < 20:
            raise ValueError("please share at least a sentence or two about why you want to participate")
        return v.strip()

    @field_validator("agreement_accepted")
    @classmethod
    def must_accept(cls, v):
        if not v:
            raise ValueError("you must accept the Community Champion Agreement")
        return v

class ChatRequest(BaseModel):
    message: str

# ── Helpers ───────────────────────────────────────────────────────────────────

def _send_email(to: str, subject: str, body: str):
    if not RESEND_KEY or RESEND_KEY.startswith("re_YOUR"):
        print(f"[DRY RUN EMAIL] To: {to}\nSubject: {subject}\n{body}\n")
        return
    import resend
    resend.api_key = RESEND_KEY
    resend.Emails.send({
        "from":    "ms.allis@mountainshares.us",
        "to":      to,
        "subject": subject,
        "text":    body,
    })

def _get_current_user(session_token: str | None) -> dict | None:
    if not session_token:
        return None
    return ts.validate_token(session_token)

# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    return {"status": "healthy", "service": "ms-allis-auth", "timestamp": datetime.now(timezone.utc).isoformat()}


@app.post("/apply")
async def apply(req: ApplicationRequest, request: Request):
    # Block duplicate emails
    email_key = f"email_index:{req.email.lower()}"
    if r.exists(email_key):
        raise HTTPException(400, "this email is already registered with Ms. Allis")

    # Build proposed userid
    base_id = req.name.lower().strip().replace(" ", "_")
    base_id = "".join(c for c in base_id if c.isalnum() or c == "_")
    proposed = base_id
    counter  = 2
    while r.exists(f"rt:{proposed}:tokens") or r.exists(f"pending:userid:{proposed}"):
        proposed = f"{base_id}{counter}"
        counter += 1

    # Store application
    import uuid
    app_id = str(uuid.uuid4())
    now    = datetime.now(timezone.utc).isoformat()
    r.hset(f"pending_application:{app_id}", mapping={
        "app_id":             app_id,
        "name":               req.name,
        "email":              req.email,
        "county":             req.county,
        "motivation":         req.motivation,
        "proposed_userid":    proposed,
        "agreement_accepted": "true",
        "agreement_version":  AGREEMENT_VERSION,
        "submitted_at":       now,
        "ip_address":         request.client.host if request.client else "",
        "status":             "pending",
    })
    r.sadd("pending_applications", app_id)
    r.set(f"pending:userid:{proposed}", app_id)
    r.set(email_key, proposed)

    # Notify admin
    _send_email(
        ADMIN_EMAIL,
        f"New Ms. Allis application: {req.name} ({req.county} County)",
        f"""A new Community Champion application is waiting for your review.

Name:       {req.name}
Email:      {req.email}
County:     {req.county}
Submitted:  {now}
Proposed userid: {proposed}

Why they want to participate:
{req.motivation}

Application ID: {app_id}

To approve:
  cdj && python3 admin_cli.py approve {app_id}

To deny:
  cdj && python3 admin_cli.py deny {app_id} --reason "..."
"""
    )

    return {"status": "received", "message": "Thank you! Carrie will review your application and send you a magic link to log in."}


@app.get("/login")
def login(token: str, response: Response):
    user = ts.validate_token(token)
    if not user:
        raise HTTPException(401, "invalid or expired token")
    resp = RedirectResponse(url="/chat", status_code=302)
    resp.set_cookie(
        key="msallis_session",
        value=token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60 * 60 * 24 * 30,  # 30 days
    )
    return resp


@app.get("/me")
def me(msallis_session: str | None = Cookie(default=None)):
    user = _get_current_user(msallis_session)
    if not user:
        raise HTTPException(401, "not logged in")
    userid = user["userid"]

    uei    = r.get(f"uei:by_user:{userid}")
    wallet = ws.get_wallet_public(userid)
    quota  = r.hgetall(f"redteam:quota:{userid}") or {}
    profile= r.hgetall(f"user:{userid}") or {}

    return {
        "userid":  userid,
        "name":    profile.get("name", userid),
        "email":   profile.get("email", ""),
        "role":    user.get("role", "user"),
        "uei":     uei,
        "wallet":  wallet,
        "quota": {
            "requests_today": int(quota.get("requests_today", 0)),
            "daily_limit":    int(quota.get("daily_limit",    50)),
            "blocked":        int(quota.get("blocked",         0)),
        }
    }


@app.post("/chat")
async def chat(req: ChatRequest, msallis_session: str | None = Cookie(default=None)):
    user = _get_current_user(msallis_session)
    if not user:
        raise HTTPException(401, "not logged in")

    userid = user["userid"]
    role   = user.get("role", "user")

    # Quota check
    quota_key = f"redteam:quota:{userid}"
    today     = datetime.now(timezone.utc).strftime("%Y-%m-%d")
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ grep -Rni "pending_application\|pending_applications\|status.*pending\|bsc_status" /opt/msjarvis-rebuild /opt/msjarvis-rebuild/ms-allis-auth-install --include="*.py" | head -100
/opt/msjarvis-rebuild/admin_cli.py:129:    if app['status'] != 'pending':
/opt/msjarvis-rebuild/admin_cli.py:130:        print(f"{RED}Application is already {app['status']}, not pending.{RESET}")
/opt/msjarvis-rebuild/admin_cli.py:203:    if app['status'] != 'pending':
/opt/msjarvis-rebuild/admin_cli.py:360:    if status == "pending":   return f"{YELLOW}pending{RESET}"
/opt/msjarvis-rebuild/_archive/generated_20260430/egeria_web_ui_dynamic.py:164:    query_status[query_id] = {'status': 'pending'}
/opt/msjarvis-rebuild/_archive/generated_20260430/egeria_web_ui_final_biological.py:332:    query_status[query_id] = {'status': 'pending'}
/opt/msjarvis-rebuild/_archive/generated_20260430/ingest_compliance_tasks_to_chroma.py:55:    status = task_status or "PENDING"
/opt/msjarvis-rebuild/_archive/generated_20260430/ms_jarvis_easyocr_processor_old.py:23:    verification_status: str = "pending"
/opt/msjarvis-rebuild/_archive/generated_20260430/egeria_web_ui_v3_consciousness.py:286:    query_status[query_id] = {'status': 'pending'}
/opt/msjarvis-rebuild/.scratch/test_services.py:94:    assert record["status"] == "pending"
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/scipy/optimize/tests/test_linprog.py:55:    # The status may be either 2 or 4 depending on why the feasible solution
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/transformers/generation/continuous_batching/scheduler.py:132:            state.remaining_prompt_ids if state.status == RequestStatus.SPLIT_PENDING_REMAINDER else state.prompt_ids
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/transformers/generation/continuous_batching/scheduler.py:136:            if state.status == RequestStatus.PENDING:
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/transformers/generation/continuous_batching/scheduler.py:140:            elif state.status == RequestStatus.SPLIT_PENDING_REMAINDER:
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/transformers/generation/continuous_batching/scheduler.py:146:            if state.status == RequestStatus.PENDING:
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/transformers/generation/continuous_batching/scheduler.py:150:            elif state.status == RequestStatus.SPLIT_PENDING_REMAINDER:
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/transformers/generation/continuous_batching/scheduler.py:179:            if state.status in [RequestStatus.SPLIT_PENDING_REMAINDER, RequestStatus.PREFILLING_SPLIT]:
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/transformers/generation/continuous_batching/scheduler.py:248:            if state.status in [RequestStatus.PREFILLING_SPLIT, RequestStatus.SPLIT_PENDING_REMAINDER]:
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/transformers/generation/continuous_batching/continuous_api.py:541:                state.status = RequestStatus.SPLIT_PENDING_REMAINDER
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/transformers/generation/continuous_batching/requests.py:84:    status: RequestStatus = RequestStatus.PENDING
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/transformers/generation/continuous_batching/requests.py:100:        status (RequestStatus): The status of the request: can be one of PENDING, PREFILLING, PREFILLING_SPLIT,
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/transformers/generation/continuous_batching/requests.py:116:    _status: RequestStatus = RequestStatus.PENDING  # Status of the request, hidden behind a property
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/transformers/generation/continuous_batching/requests.py:129:        if self._status == RequestStatus.PENDING:
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/joblib/parallel.py:726:            # The initial status for the job is TASK_PENDING.
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/joblib/parallel.py:728:            self.status = TASK_PENDING
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/joblib/parallel.py:784:        if timeout is None or self.status != TASK_PENDING:
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/joblib/parallel.py:787:        # The computation are running and the status is pending.
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/joblib/parallel.py:880:            if self.status not in (TASK_PENDING, None):
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/joblib/parallel.py:1798:                    self._jobs[0].get_status(timeout=self.timeout) == TASK_PENDING
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/google/oauth2/reauth.py:219:            msg["status"] == _CHALLENGE_REQUIRED or msg["status"] == _CHALLENGE_PENDING
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/google/oauth2/_reauth_async.py:183:            or msg["status"] == reauth._CHALLENGE_PENDING
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:471:        status (`Literal["pending", "accepted", "rejected"]`):
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:472:            Status of the request. Can be one of `["pending", "accepted", "rejected"]`.
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:481:    status: Literal["pending", "accepted", "rejected"]
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:7610:            InferenceEndpoint(name='my-endpoint-name', status="pending",...)
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:8669:                status='pending',
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:8808:        status: Literal["accepted", "rejected", "pending"],
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:8973:        status: Literal["accepted", "rejected", "pending"],
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/kubernetes/client/models/v1_watch_event.py:62:        Object is:  * If Type is Added or Modified: the new state of the object.  * If Type is Deleted: the state of the object immediately before deletion.  * If Type is Error: *Status is recommended; other types may make sense    depending on context.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/kubernetes/client/models/v1_watch_event.py:73:        Object is:  * If Type is Added or Modified: the new state of the object.  * If Type is Deleted: the state of the object immediately before deletion.  * If Type is Error: *Status is recommended; other types may make sense    depending on context.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/kubernetes/client/models/v1_persistent_volume_claim_status.py:117:        allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either:  * Un-prefixed keys:   - storage - the capacity of the volume.  * Custom resources must use implementation-defined prefixed names such as \"example.com/my-custom-resource\" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  ClaimResourceStatus can be in any of following states:  - ControllerResizeInProgress:   State set when resize controller starts resizing the volume in control-plane.  - ControllerResizeFailed:   State set when resize has failed in resize controller with a terminal error.  - NodeResizePending:   State set when resize controller has finished resizing the volume but further resizing of   volume is needed on the node.  - NodeResizeInProgress:   State set when kubelet starts resizing the volume.  - NodeResizeFailed:   State set when resizing has failed in kubelet with a terminal error. Transient errors don't set   NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states:  - pvc.status.allocatedResourceStatus['storage'] = \"ControllerResizeInProgress\"      - pvc.status.allocatedResourceStatus['storage'] = \"ControllerResizeFailed\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizePending\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizeInProgress\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizeFailed\" When this field is not set, it means that no resize operation is in progress for the given PVC.  A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/kubernetes/client/models/v1_persistent_volume_claim_status.py:128:        allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either:  * Un-prefixed keys:   - storage - the capacity of the volume.  * Custom resources must use implementation-defined prefixed names such as \"example.com/my-custom-resource\" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  ClaimResourceStatus can be in any of following states:  - ControllerResizeInProgress:   State set when resize controller starts resizing the volume in control-plane.  - ControllerResizeFailed:   State set when resize has failed in resize controller with a terminal error.  - NodeResizePending:   State set when resize controller has finished resizing the volume but further resizing of   volume is needed on the node.  - NodeResizeInProgress:   State set when kubelet starts resizing the volume.  - NodeResizeFailed:   State set when resizing has failed in kubelet with a terminal error. Transient errors don't set   NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states:  - pvc.status.allocatedResourceStatus['storage'] = \"ControllerResizeInProgress\"      - pvc.status.allocatedResourceStatus['storage'] = \"ControllerResizeFailed\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizePending\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizeInProgress\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizeFailed\" When this field is not set, it means that no resize operation is in progress for the given PVC.  A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/kubernetes/client/models/v1_pod_status.py:372:        The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:  Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.  More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/kubernetes/client/models/v1_pod_status.py:383:        The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:  Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.  More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/kubernetes/client/models/v1_pod_status.py:487:        Status of resources resize desired for pod's containers. It is empty if no resources resize is pending. Any changes to container resources will automatically set this to \"Proposed\" Deprecated: Resize status is moved to two pod conditions PodResizePending and PodResizeInProgress. PodResizePending will track states where the spec has been resized, but the Kubelet has not yet allocated the resources. PodResizeInProgress will track in-progress resizes, and should be present whenever allocated resources != acknowledged resources.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/kubernetes/client/models/v1_pod_status.py:498:        Status of resources resize desired for pod's containers. It is empty if no resources resize is pending. Any changes to container resources will automatically set this to \"Proposed\" Deprecated: Resize status is moved to two pod conditions PodResizePending and PodResizeInProgress. PodResizePending will track states where the spec has been resized, but the Kubelet has not yet allocated the resources. PodResizeInProgress will track in-progress resizes, and should be present whenever allocated resources != acknowledged resources.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/kubernetes/client/models/v1_modify_volume_status.py:63:        status is the status of the ControllerModifyVolume operation. It can be in any of following states:  - Pending    Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as    the specified VolumeAttributesClass not existing.  - InProgress    InProgress indicates that the volume is being modified.  - Infeasible   Infeasible indicates that the request has been rejected as invalid by the CSI driver. To    resolve the error, a valid VolumeAttributesClass needs to be specified. Note: New statuses can be added in the future. Consumers should check for unknown statuses and fail appropriately.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/kubernetes/client/models/v1_modify_volume_status.py:74:        status is the status of the ControllerModifyVolume operation. It can be in any of following states:  - Pending    Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as    the specified VolumeAttributesClass not existing.  - InProgress    InProgress indicates that the volume is being modified.  - Infeasible   Infeasible indicates that the request has been rejected as invalid by the CSI driver. To    resolve the error, a valid VolumeAttributesClass needs to be specified. Note: New statuses can be added in the future. Consumers should check for unknown statuses and fail appropriately.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/chromadb/test/test_api.py:2932:        where = Where.from_dict({"status": {"$in": ["active", "pending"]}})
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/chromadb/test/test_api.py:2976:        where = Where.from_dict({"$or": [{"status": "active"}, {"status": "pending"}]})
/opt/msjarvis-rebuild/.venv/lib64/python3.12/site-packages/chromadb/test/test_api.py:2986:                    {"$or": [{"status": "active"}, {"status": "pending"}]},
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/optimize/tests/test_linprog.py:55:    # The status may be either 2 or 4 depending on why the feasible solution
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/transformers/generation/continuous_batching/scheduler.py:132:            state.remaining_prompt_ids if state.status == RequestStatus.SPLIT_PENDING_REMAINDER else state.prompt_ids
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/transformers/generation/continuous_batching/scheduler.py:136:            if state.status == RequestStatus.PENDING:
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/transformers/generation/continuous_batching/scheduler.py:140:            elif state.status == RequestStatus.SPLIT_PENDING_REMAINDER:
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/transformers/generation/continuous_batching/scheduler.py:146:            if state.status == RequestStatus.PENDING:
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/transformers/generation/continuous_batching/scheduler.py:150:            elif state.status == RequestStatus.SPLIT_PENDING_REMAINDER:
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/transformers/generation/continuous_batching/scheduler.py:179:            if state.status in [RequestStatus.SPLIT_PENDING_REMAINDER, RequestStatus.PREFILLING_SPLIT]:
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/transformers/generation/continuous_batching/scheduler.py:248:            if state.status in [RequestStatus.PREFILLING_SPLIT, RequestStatus.SPLIT_PENDING_REMAINDER]:
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/transformers/generation/continuous_batching/continuous_api.py:541:                state.status = RequestStatus.SPLIT_PENDING_REMAINDER
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/transformers/generation/continuous_batching/requests.py:84:    status: RequestStatus = RequestStatus.PENDING
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/transformers/generation/continuous_batching/requests.py:100:        status (RequestStatus): The status of the request: can be one of PENDING, PREFILLING, PREFILLING_SPLIT,
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/transformers/generation/continuous_batching/requests.py:116:    _status: RequestStatus = RequestStatus.PENDING  # Status of the request, hidden behind a property
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/transformers/generation/continuous_batching/requests.py:129:        if self._status == RequestStatus.PENDING:
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/joblib/parallel.py:726:            # The initial status for the job is TASK_PENDING.
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/joblib/parallel.py:728:            self.status = TASK_PENDING
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/joblib/parallel.py:784:        if timeout is None or self.status != TASK_PENDING:
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/joblib/parallel.py:787:        # The computation are running and the status is pending.
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/joblib/parallel.py:880:            if self.status not in (TASK_PENDING, None):
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/joblib/parallel.py:1798:                    self._jobs[0].get_status(timeout=self.timeout) == TASK_PENDING
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/google/oauth2/reauth.py:219:            msg["status"] == _CHALLENGE_REQUIRED or msg["status"] == _CHALLENGE_PENDING
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/google/oauth2/_reauth_async.py:183:            or msg["status"] == reauth._CHALLENGE_PENDING
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:471:        status (`Literal["pending", "accepted", "rejected"]`):
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:472:            Status of the request. Can be one of `["pending", "accepted", "rejected"]`.
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:481:    status: Literal["pending", "accepted", "rejected"]
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:7610:            InferenceEndpoint(name='my-endpoint-name', status="pending",...)
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:8669:                status='pending',
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:8808:        status: Literal["accepted", "rejected", "pending"],
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/huggingface_hub/hf_api.py:8973:        status: Literal["accepted", "rejected", "pending"],
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/kubernetes/client/models/v1_watch_event.py:62:        Object is:  * If Type is Added or Modified: the new state of the object.  * If Type is Deleted: the state of the object immediately before deletion.  * If Type is Error: *Status is recommended; other types may make sense    depending on context.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/kubernetes/client/models/v1_watch_event.py:73:        Object is:  * If Type is Added or Modified: the new state of the object.  * If Type is Deleted: the state of the object immediately before deletion.  * If Type is Error: *Status is recommended; other types may make sense    depending on context.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/kubernetes/client/models/v1_persistent_volume_claim_status.py:117:        allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either:  * Un-prefixed keys:   - storage - the capacity of the volume.  * Custom resources must use implementation-defined prefixed names such as \"example.com/my-custom-resource\" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  ClaimResourceStatus can be in any of following states:  - ControllerResizeInProgress:   State set when resize controller starts resizing the volume in control-plane.  - ControllerResizeFailed:   State set when resize has failed in resize controller with a terminal error.  - NodeResizePending:   State set when resize controller has finished resizing the volume but further resizing of   volume is needed on the node.  - NodeResizeInProgress:   State set when kubelet starts resizing the volume.  - NodeResizeFailed:   State set when resizing has failed in kubelet with a terminal error. Transient errors don't set   NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states:  - pvc.status.allocatedResourceStatus['storage'] = \"ControllerResizeInProgress\"      - pvc.status.allocatedResourceStatus['storage'] = \"ControllerResizeFailed\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizePending\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizeInProgress\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizeFailed\" When this field is not set, it means that no resize operation is in progress for the given PVC.  A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/kubernetes/client/models/v1_persistent_volume_claim_status.py:128:        allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either:  * Un-prefixed keys:   - storage - the capacity of the volume.  * Custom resources must use implementation-defined prefixed names such as \"example.com/my-custom-resource\" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  ClaimResourceStatus can be in any of following states:  - ControllerResizeInProgress:   State set when resize controller starts resizing the volume in control-plane.  - ControllerResizeFailed:   State set when resize has failed in resize controller with a terminal error.  - NodeResizePending:   State set when resize controller has finished resizing the volume but further resizing of   volume is needed on the node.  - NodeResizeInProgress:   State set when kubelet starts resizing the volume.  - NodeResizeFailed:   State set when resizing has failed in kubelet with a terminal error. Transient errors don't set   NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states:  - pvc.status.allocatedResourceStatus['storage'] = \"ControllerResizeInProgress\"      - pvc.status.allocatedResourceStatus['storage'] = \"ControllerResizeFailed\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizePending\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizeInProgress\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizeFailed\" When this field is not set, it means that no resize operation is in progress for the given PVC.  A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/kubernetes/client/models/v1_pod_status.py:372:        The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:  Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.  More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/kubernetes/client/models/v1_pod_status.py:383:        The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:  Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.  More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/kubernetes/client/models/v1_pod_status.py:487:        Status of resources resize desired for pod's containers. It is empty if no resources resize is pending. Any changes to container resources will automatically set this to \"Proposed\" Deprecated: Resize status is moved to two pod conditions PodResizePending and PodResizeInProgress. PodResizePending will track states where the spec has been resized, but the Kubelet has not yet allocated the resources. PodResizeInProgress will track in-progress resizes, and should be present whenever allocated resources != acknowledged resources.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/kubernetes/client/models/v1_pod_status.py:498:        Status of resources resize desired for pod's containers. It is empty if no resources resize is pending. Any changes to container resources will automatically set this to \"Proposed\" Deprecated: Resize status is moved to two pod conditions PodResizePending and PodResizeInProgress. PodResizePending will track states where the spec has been resized, but the Kubelet has not yet allocated the resources. PodResizeInProgress will track in-progress resizes, and should be present whenever allocated resources != acknowledged resources.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/kubernetes/client/models/v1_modify_volume_status.py:63:        status is the status of the ControllerModifyVolume operation. It can be in any of following states:  - Pending    Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as    the specified VolumeAttributesClass not existing.  - InProgress    InProgress indicates that the volume is being modified.  - Infeasible   Infeasible indicates that the request has been rejected as invalid by the CSI driver. To    resolve the error, a valid VolumeAttributesClass needs to be specified. Note: New statuses can be added in the future. Consumers should check for unknown statuses and fail appropriately.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/kubernetes/client/models/v1_modify_volume_status.py:74:        status is the status of the ControllerModifyVolume operation. It can be in any of following states:  - Pending    Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as    the specified VolumeAttributesClass not existing.  - InProgress    InProgress indicates that the volume is being modified.  - Infeasible   Infeasible indicates that the request has been rejected as invalid by the CSI driver. To    resolve the error, a valid VolumeAttributesClass needs to be specified. Note: New statuses can be added in the future. Consumers should check for unknown statuses and fail appropriately.  # noqa: E501
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/test/test_api.py:2932:        where = Where.from_dict({"status": {"$in": ["active", "pending"]}})
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/test/test_api.py:2976:        where = Where.from_dict({"$or": [{"status": "active"}, {"status": "pending"}]})
/opt/msjarvis-rebuild/.venv/lib/python3.12/site-packages/chromadb/test/test_api.py:2986:                    {"$or": [{"status": "active"}, {"status": "pending"}]},
/opt/msjarvis-rebuild/services/query_benefits_system.py:25:                    {"user_task_status": "PENDING"},
/opt/msjarvis-rebuild/services/query_benefits_system.py:30:            where_clause = {"user_task_status": "PENDING"}
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:481:        status (`Literal["pending", "accepted", "rejected"]`):
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:482:            Status of the request. Can be one of `["pending", "accepted", "rejected"]`.
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:491:    status: Literal["pending", "accepted", "rejected"]
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:7726:            InferenceEndpoint(name='my-endpoint-name', status="pending",...)
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:8796:                status='pending',
/opt/msjarvis-rebuild/services/chroma_inspect_venv/lib64/python3.12/site-packages/huggingface_hub/hf_api.py:8935:        status: Literal["accepted", "rejected", "pending"],
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ docker exec -it jarvis-redis redis-cli KEYS "pending_application:*"
docker exec -it jarvis-redis redis-cli SMEMBERS "pending_applications"
docker exec -it jarvis-redis redis-cli KEYS "*bsc*"
(empty array)
(empty array)
(empty array)
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild/ms-allis-frontend$ 

