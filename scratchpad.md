crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild || cd ~/msjarvis-rebuild || exit 1
. crypto-venv/bin/activate
export PYTHONPATH="$PWD"

mkdir -p /tmp/msj_hilbert_pkg

printf '\n== compile hilbert package modules ==\n' | tee /tmp/msj_hilbert_pkg/10_compile.txt
python -m py_compile \
  services/__init__.py \
  services/hilbert/__init__.py \
  services/hilbert/collection_manifest.py \
  services/hilbert/civic_query.py \
  services/hilbert/ingest_worker.py \
  services/hilbert/jarvis_hilbert_state.py \
  services/hilbert/layer3_opt_in.py \
  services/hilbert_commons/commons_aggregator.py \
  services/jarvis_hilbert_time.py 2>&1 | tee -a /tmp/msj_hilbert_pkg/10_compile.txt

== compile hilbert package modules ==
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild || cd ~/msjarvis-rebuild || exit 1
. crypto-venv/bin/activate
export PYTHONPATH="$PWD"

mkdir -p /tmp/msj_hilbert_client

printf '\n== Hilbert Chroma client usage ==\n' | tee /tmp/msj_hilbert_client/20_client_usage.txt
grep -RInE 'chromadb.HttpClient|PersistentClient|EphemeralClient|CHROMA_HOST|CHROMA_PORT' \
  services/hilbert services/hilbert_commons services/jarvis_hilbert_time.py 2>/dev/null \ 
  | sort | tee -a /tmp/msj_hilbert_client/20_client_usage.txt

printf '\n== heads of Hilbert modules that touch Chroma ==\n' | tee /tmp/msj_hilbert_client/21_heads.txt
for f in \
  services/hilbert/chroma_policy.py \
  services/hilbert/civic_intake.py \
  services/hilbert/civic_query.py \
  services/hilbert/ingest_worker.py \
  services/hilbert/jarvis_hilbert_state.py \
  services/hilbert_commons/commons_aggregator.py
doneintf '\n' | tee -a /tmp/msj_hilbert_client/21_heads.txtheads.txtt

== Hilbert Chroma client usage ==
services/hilbert/civic_projector.py:39:CHROMA_HOST = os.environ.get("CHROMA_HOST", "localhost")
services/hilbert/civic_projector.py:40:CHROMA_PORT = int(os.environ.get("CHROMA_PORT", 8000))
services/hilbert/civic_projector.py:483:    chroma_client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
services/hilbert/civic_projector.py.bak.1783038099:33:CHROMA_HOST = os.environ.get("CHROMA_HOST", "localhost")
services/hilbert/civic_projector.py.bak.1783038099:34:CHROMA_PORT = int(os.environ.get("CHROMA_PORT", 8000))
services/hilbert/civic_projector.py.bak.1783038099:359:    chroma_client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
services/hilbert/civic_query.py:19:    return chromadb.HttpClient(
services/hilbert/civic_query.py:20:        host=os.getenv("CHROMA_HOST", "jarvis-chroma"),
services/hilbert/civic_query.py:21:        port=int(os.getenv("CHROMA_PORT", 8000)),
services/hilbert/civic_query.py.bak.20260713_171406:18:    return chromadb.HttpClient(
services/hilbert/civic_query.py.bak.20260713_171406:19:        host=os.getenv("CHROMA_HOST", "jarvis-chroma"),
services/hilbert/civic_query.py.bak.20260713_171406:20:        port=int(os.getenv("CHROMA_PORT", 8000)),
services/hilbert_commons/commons_aggregator.py:14:CHROMA_HOST = os.getenv("CHROMA_HOST", "jarvis-chroma")
services/hilbert_commons/commons_aggregator.py:15:CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8000"))
services/hilbert_commons/commons_aggregator.py:29:    client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
services/hilbert/ingest_worker.py:20:    return chromadb.HttpClient(
services/hilbert/ingest_worker.py:21:        host=os.getenv("CHROMA_HOST", "jarvis-chroma"),
services/hilbert/ingest_worker.py:22:        port=int(os.getenv("CHROMA_PORT", 8000)),
services/hilbert/ingest_worker.py.bak.20260713_171630:19:    return chromadb.HttpClient(
services/hilbert/ingest_worker.py.bak.20260713_171630:20:        host=os.getenv("CHROMA_HOST", "jarvis-chroma"),
services/hilbert/ingest_worker.py.bak.20260713_171630:21:        port=int(os.getenv("CHROMA_PORT", 8000)),
services/hilbert/jarvis_hilbert_state.py:281:            _col = _chromadb.HttpClient(
services/hilbert/jarvis_hilbert_state.py:282:                host=_os.environ.get("CHROMA_HOST", "jarvis-chroma"),
services/hilbert/jarvis_hilbert_state.py:283:                port=int(_os.environ.get("CHROMA_PORT", 8000)),
services/hilbert/jarvis_hilbert_state.py:336:        c = _chromadb.HttpClient(
services/hilbert/jarvis_hilbert_state.py:337:            host=_os.environ.get("CHROMA_HOST", "jarvis-chroma"),
services/hilbert/jarvis_hilbert_state.py:338:            port=int(_os.environ.get("CHROMA_PORT", 8000)),
services/hilbert/layer3_opt_in.py:21:    c = chromadb.HttpClient(
services/hilbert/layer3_opt_in.py:22:        host=os.getenv("CHROMA_HOST", "jarvis-chroma"),
services/hilbert/layer3_opt_in.py:23:        port=int(os.getenv("CHROMA_PORT", 8000)),
services/hilbert/layer3_opt_in.py.bak.20260713_171805:21:    c = chromadb.HttpClient(
services/hilbert/layer3_opt_in.py.bak.20260713_171805:22:        host=os.getenv("CHROMA_HOST", "jarvis-chroma"),
services/hilbert/layer3_opt_in.py.bak.20260713_171805:23:        port=int(os.getenv("CHROMA_PORT", 8000)),
services/hilbert/supervisord-civic-intake.conf:15:environment=CHROMA_HOST="jarvis-chroma",CHROMA_PORT="8000",INTAKE_PORT="8100"
services/hilbert/test_hilbert_state.py:42:    stub_chromadb.HttpClient.return_value = _MOCK_CC

== heads of Hilbert modules that touch Chroma ==
===== services/hilbert/chroma_policy.py =====
from typing import Any

HP_ALLOWED_COLLECTIONS = frozenset({
    "public_civic_appearances",
    "public_civic_roles",
    "public_civic_events",
    "public_civic_sources",

    "public_civic_documents",
    "public_civic_statements",
    "civic_role_temporal",})

HP_ALLOWED_METADATA_KEYS = frozenset({
    "source_id", "source_type", "source_uri", "source_label",
    "role_class", "role_label", "role_scope",
    "place_id", "place_label", "jurisdiction",
    "collection_hash",
    "feature_hash",
    "place_type",
    "time_label",
    "time_start", "time_end", "time_precision",
    "publicness_basis", "disclosure_status", "historical_status",
    "provenance_hash", "merkle_ref", "appearance_id", "entity_class",
    "display_name_public",
    # --- Constitutional review 2026-07-02 (cakidd) ---
    # public_civic_events collection — hp.suppression_event projection.
    # These keys describe administrative suppression decisions on civic
    # appearance records. No PII, no biometrics, no private identifiers.
    # All values are operational metadata: which field was acted on,
    # what type of suppression, why, at what pipeline stage, and by
    # which worker role (not a user identity). Approved for H_p allowlist.
    "field_name",        # which appearance field triggered suppression
    "suppression_type",  # 'withheld' or 'escalated' (CHECK constraint)
    "reason",            # free-text rationale, non-PII operational note
    "pipeline_stage",    # ingest stage that made the decision
    "decided_at",        # timestamp of decision (ISO date string)
    "decided_by",        # worker/role name, not a user identity
    # --- Constitutional review 2026-07-02 (cakidd) ---
    # public_civic_sources — hp.appearance_source projection.
    # retrieved_at is an operational timestamp of when a public URI
    # was fetched by the ingest pipeline. No PII. Approved.
    "retrieved_at",      # ISO date of source URI retrieval
    # --- Constitutional review 2026-07-03 (cakidd) ---
    # Layer/opt-in fields added to all H_p projections.
    # registration_layer: int 1-3, no PII. public_opt_in: bool. Approved.
    "registration_layer",  # int 1-3, privacy layer designation
    "public_opt_in",       # bool, Layer 3 explicit consent flag
    "merkle_ref",          # sha256 of feature content, used for dedup/audit

    # Civic event fields — approved: public meeting metadata, no PII
    "event_date",
    "event_id",
    "event_type",
    "location",
    "record_type",
    "source_url",
})

HP_FORBIDDEN_METADATA_KEYS = frozenset({
    "address", "street_address", "home_address",
    "email", "email_address", "phone", "phone_number",
    "dob", "date_of_birth", "ssn", "document_number",
    "face_embedding", "face_id", "face_ref",
    "session_id", "session_uuid", "device_fingerprint", "ip_address",
    "beliefid", "belief_id", "beliefstate", "worldviewid", "worldview_id",
    "vulnerability_score", "ideology", "kyc_provider_ref",
    "user_id", "auth_id", "legal_name",
})


class ChromaPolicyViolation(Exception):
    pass


def assert_collection_allowed(collection_name: str) -> None:
    if collection_name not in HP_ALLOWED_COLLECTIONS:
        raise ChromaPolicyViolation(
            f"Collection {collection_name!r} is not on the H_p allowlist. "
            f"Allowed: {sorted(HP_ALLOWED_COLLECTIONS)}"
        )


def assert_metadata_clean(metadata: dict) -> None:
    keys = set(metadata.keys())
    forbidden_present = keys & HP_FORBIDDEN_METADATA_KEYS
    if forbidden_present:
        raise ChromaPolicyViolation(
            f"Metadata contains forbidden keys: {sorted(forbidden_present)}"
        )
    unknown_keys = keys - HP_ALLOWED_METADATA_KEYS
    if unknown_keys:
        raise ChromaPolicyViolation(
            f"Metadata contains keys not on the H_p allowlist: {sorted(unknown_keys)}. "
            "Add to HP_ALLOWED_METADATA_KEYS only after constitutional review."
        )


def safe_chroma_add(collection_name, documents, metadatas, ids, chroma_client):
    assert_collection_allowed(collection_name)
    for meta in metadatas:
        assert_metadata_clean(meta)
    collection = chroma_client.get_collection(collection_name)
    collection.upsert(documents=documents, metadatas=metadatas, ids=ids)


def safe_chroma_query(collection_name, query_texts, n_results, chroma_client, where=None):
    assert_collection_allowed(collection_name)
    # Step 1: strip _caller_layer FIRST — it is never a Chroma filter key
    caller_layer = 1
    clean_where = None
    if where:
        caller_layer = int(where.get("_caller_layer", 1))
        clean_where = {k: v for k, v in where.items() if k != "_caller_layer"} or None
    # Step 2: THEN check for forbidden keys (now _caller_layer is already gone)
    if clean_where:
        forbidden_in_where = set(clean_where.keys()) & HP_FORBIDDEN_METADATA_KEYS
        if forbidden_in_where:
            raise ChromaPolicyViolation(
                f"Query where-filter uses forbidden keys: {sorted(forbidden_in_where)}"
            )
    collection = chroma_client.get_collection(collection_name)
    kwargs = {"query_texts": query_texts, "n_results": n_results}
    if clean_where:
        kwargs["where"] = clean_where
    results = collection.query(**kwargs)
    # Step 3: redact display fields based on caller clearance level
    from query_guard import redact_for_layer
    if results and results.get("metadatas"):
        results["metadatas"] = [
            [redact_for_layer(m, caller_layer) for m in batch]
            for batch in results["metadatas"]
        ]
    return results

===== services/hilbert/civic_intake.py =====
from __future__ import annotations
import logging, os
from typing import Optional, Dict, Any, List, Literal

from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel, Field
import uvicorn

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ingest_worker import ingest_document, ingest_statement, ingest_role_temporal
from civic_query import query_documents, query_statements, query_roles, query_all, get_by_entity

logger = logging.getLogger("hilbert.civic_intake")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")

app = FastAPI(ttle="Hilbert Civic Intake", version="1.1.0")

# -------------------------------------------------------------------------
# AUTH GUARD
# -------------------------------------------------------------------------

_HILBERT_KEY = os.getenv("HILBERT_INTAKE_KEY", "")


def _require_key(X_Hilbert_Key: str = Header(default="", alias="X-Hilbert-Key")):
    if not _HILBERT_KEY:
        return  # key not configured -> open (internal-only, trust network boundary)
    if X_Hilbert_Key != _HILBERT_KEY:
        raise HTTPException(status_code=403, detail="Invalid X-Hilbert-Key")


Auth = Depends(_require_key)


# -------------------------------------------------------------------------
# SCHEMAS
# -------------------------------------------------------------------------

class DocumentIngestRequest(BaseModel):
    content: str = Field(..., min_length=1)
    source: str
    entity_id: str
    display_name: str
    registration_layer: int = Field(1, ge=1, le=3)
    public_opt_in: bool = False
    doc_type: str = "general"
    extra_meta: Optional[Dict[str, Any]] = None


class StatementIngestRequest(BaseModel):
    content: str = Field(..., min_length=1)
    source: str
    entity_id: str
    display_name: str
    registration_layer: int = Field(1, ge=1, le=3)
    public_opt_in: bool = False
    statement_type: str = "general"
    extra_meta: Optional[Dict[str, Any]] = None


class RoleIngestRequest(BaseModel):
    content: str = Field(..., min_length=1)
    entity_id: str
    display_name: str
    role: str
    effective_date: str
    expiry_date: Optional[str] = None
    source: str
    registration_layer: int = Field(1, ge=1, le=3)
    public_opt_in: bool = False
    extra_meta: Optional[Dict[str, Any]] = None


class BatchRecord(BaseModel):
    """Single record within a bulk ingest batch."""
    collection: Literal["public_civic_documents", "public_civic_statements", "civic_role_temporal"]
    payload: Dict[str, Any]   # must match the fields of the corresponding IngestRequest


class BatchIngestRequest(BaseModel):
    records: List[BatchRecord] = Field(..., min_length=1, max_length=500)


class BatchResult(BaseModel):
    index: int
    status: str            # "ok" | "error"
    id: Optional[str] = None
    collection: Optional[str] = None
    error: Optional[str] = None


class QueryRequest(BaseModel):
    text: str = Field(..., min_length=1)
    n_results: int = Field(5, ge=1, le=50)
    registration_layer: Optional[int] = None
    doc_type: Optional[str] = None
    statement_type: Optional[str] = None
    role: Optional[str] = None
    effective_after: Optional[str] = None
    source: Optional[str] = None


# -------------------------------------------------------------------------
# INGEST_ROUTER (centralized dispatch for single + batch)
# -------------------------------------------------------------------------

def _dispatch(collection: str, payload: dict) -> str:
    """Route a single record to the correct ingest function. Returns doc_id."""
    if collection == "public_civic_documents":
        req = DocumentIngestRequest(**payload)
        return ingest_document(
            content=req.content, source=req.source, entity_id=req.entity_id,
            display_name=req.display_name, registration_layer=req.registration_layer,
            public_opt_in=req.public_opt_in, doc_type=req.doc_type,
            extra_meta=req.extra_meta,
        )
    elif collection == "public_civic_statements":
        req = StatementIngestRequest(**payload)
        return ingest_statement(
            content=req.content, source=req.source, entity_id=req.entity_id,
            display_name=req.display_name, registration_layer=req.registration_layer,
            public_opt_in=req.public_opt_in, statement_type=req.statement_type,
            extra_meta=req.extra_meta,
        )
    elif collection == "civic_role_temporal":
        req = RoleIngestRequest(**payload)
        return ingest_role_temporal(
            content=req.content, entity_id=req.entity_id,
            display_name=req.display_name, role=req.role,
            effective_date=req.effective_date, expiry_date=req.expiry_date,
            source=req.source, registration_layer=req.registration_layer,
            public_opt_in=req.public_opt_in, extra_meta=req.extra_meta,
        )
    else:
        raise ValueError(f"Unknown collection: {collection}")


# -------------------------------------------------------------------------
# INGEST_ENDPOINTS
# -------------------------------------------------------------------------

@app.post("/ingest/document")
def ingest_doc(req: DocumentIngestRequest, _: None = Auth):
    try:
        doc_id = _dispatch("public_civic_documents", req.model_dump())
        return {"status": "ok", "id": doc_id, "collection": "public_civic_documents"}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.exception("ingest_doc failed")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ingest/statement")
def ingest_stmt(req: StatementIngestRequest, _: None = Auth):
    try:
        doc_id = _dispatch("public_civic_statements", req.model_dump())
        return {"status": "ok", "id": doc_id, "collection": "public_civic_statements"}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.exception("ingest_stmt failed")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ingest/role")
def ingest_role(req: RoleIngestRequest, _: None = Auth):
    try:
        doc_id = _dispatch("civic_role_temporal", req.model_dump())
        return {"status": "ok", "id": doc_id, "collection": "civic_role_temporal"}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.exception("ingest_role failed")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ingest/batch", response_model=List[BatchResult])
def ingest_batch(req: BatchIngestRequest, _: None = Auth):
    """
    Bulk ingest up to 500 records across any mix of collections.
    Each record is processed independently -- failures are captured
    per-record and returned inline; one bad record does not abort the batch.
    """
    results = []
    ok_count = err_count = 0
    for i, rec in enumerate(req.records):
        try:
            doc_id = _dispatch(rec.collection, rec.payload)
            results.append(BatchResult(index=i, status="ok", id=doc_id, collection=rec.collection))
            ok_count += 1
        except Exception as e:
            results.append(BatchResult(index=i, status="error", error=str(e)))
            err_count += 1
            logger.warning("batch record %d failed: %s", i, e)
    logger.info("batch ingest complete: ok=%d err=%d", ok_count, err_count)
    return results


# -------------------------------------------------------------------------
# QUERY ENDPOINTS (no auth required -- read-only)
# -------------------------------------------------------------------------

@app.post("/query/documents")
def search_docs(req: QueryRequest):
    return {"results": query_documents(req.text, req.n_results, req.registration_layer, req.doc_type, req.source)}


@app.post("/query/statements")
def search_stmts(req: QueryRequest):
    return {"results": query_statements(req.text, req.n_results, req.registration_layer, req.statement_type, req.source)}


@app.post("/query/roles")
def search_roles(req: QueryRequest):
    return {"results": query_roles(req.text, req.n_results, req.registration_layer, req.role, req.effective_after)}


@app.post("/query/all")

===== services/hilbert/civic_query.py =====
import os, logging
from .collection_manifest import hp_public_appearances, hp_public_documents, hp_public_statements, civic_role_temporal
from typing import Optional, List, Dict, Any
import chromadb
from chromadb.utils import embedding_functions

logger = logging.getLogger("hilbert.civic_query")

_EMBED_FN = embedding_functions.DefaultEmbeddingFunction()

COLLECTIONS = [
    hp_public_documents(),
    hp_public_statements(),
    civic_role_temporal(),
]


def _chroma():
    return chromadb.HttpClient(
        host=os.getenv("CHROMA_HOST", "jarvis-chroma"),
        port=int(os.getenv("CHROMA_PORT", 8000)),
    )


def _col(client, name: str):
    return client.get_or_create_collection(
        name=name,
        embedding_function=_EMBED_FN,
        metadata={"hnsw:space": "cosine"},
    )


def _strip_placeholders(results: dict) -> list:
    out = []
    for i, doc_id in enumerate(results["ids"][0]):
        meta = results["metadatas"][0][i] or {}
        if meta.get("_placeholder") == "true":
            continue
        out.append({
            "id": doc_id,
            "document": results["documents"][0][i],
            "metadata": meta,
            "distance": results["distances"][0][i] if results.get("distances") else None,
        })
    return out


# -------------------------------------------------------------------------
# PUBLIC API
# -------------------------------------------------------------------------

def query_documents(
    text: str,
    n_results: int = 5,
    registration_layer: Optional[int] = None,
    doc_type: Optional[str] = None,
    source: Optional[str] = None,
) -> List[Dict]:
    """Semantic search over public_civic_documents."""
    where = _build_where(registration_layer, doc_type=doc_type, source=source)
    kwargs = dict(query_texts=[text], n_results=n_results, include=["documents", "metadatas", "distances"])
    if where:
        kwargs["where"] = where
    results = _col(_chroma(), hp_public_documents()).query(**kwargs)
    return _strip_placeholders(results)


def query_statements(
    text: str,
    n_results: int = 5,
    registration_layer: Optional[int] = None,
    statement_type: Optional[str] = None,
    source: Optional[str] = None,
) -> List[Dict]:
    """Semantic search over public_civic_statements."""
    where = _build_where(registration_layer, statement_type=statement_type, source=source)
    kwargs = dict(query_texts=[text], n_results=n_results, include=["documents", "metadatas", "distances"])
    if where:
        kwargs["where"] = where
    results = _col(_chroma(), hp_public_statements()).query(**kwargs)
    return _strip_placeholders(results)


def query_roles(
    text: str,
    n_results: int = 5,
    registration_layer: Optional[int] = None,
    role: Optional[str] = None,
    effective_after: Optional[str] = None,
) -> List[Dict]:
    """Semantic search over civic_role_temporal."""
    where_clauses = []
    if registration_layer is not None:
        where_clauses.append({"registration_layer": {"$eq": int(registration_layer)}})
    if role is not None:
        where_clauses.append({"role": {"$eq": role}})
    if effective_after is not None:
        where_clauses.append({"effective_date": {"$gte": effective_after}})
    where = _merge_where(where_clauses)
    kwargs = dict(query_texts=[text], n_results=n_results, include=["documents", "metadatas", "distances"])
    if where:
        kwargs["where"] = where
    results = _col(_chroma(), civic_role_temporal()).query(**kwargs)
    return _strip_placeholders(results)


def query_all(
    text: str,
    n_results: int = 3,
    registration_layer: Optional[int] = None,
) -> Dict[str, List]:
    """Semantic search across all three civic collections."""
    return {
        "documents":  query_documents(text, n_results, registration_layer),
        "statements": query_statements(text, n_results, registration_layer),
        "roles":      query_roles(text, n_results, registration_layer),
    }



def query_appearances(text: str, n_results: int = 5,
                      registration_layer: Optional[int] = None) -> List[Dict]:
    """Semantic search across public_civic_appearances."""
    c = _chroma()
    kwargs = dict(query_texts=[text], n_results=n_results,
                  include=["documents", "metadatas", "distances"])
    if registration_layer is not None:
        kwargs["where"] = {"registration_layer": {"$eq": registration_layer}}
    try:
        r = _col(c, hp_public_appearances()).query(**kwargs)
        return [
            {"id": i, "document": d, "metadata": m, "distance": dist}
            for i, d, m, dist in zip(
                r["ids"][0], r["documents"][0],
                r["metadatas"][0], r["distances"][0]
            )
        ]
    except Exception as e:
        return {"error": str(e)}

def get_by_entity(entity_id: str) -> Dict[str, List]:
    """Fetch all records across all collections for a given entity_id."""
    # Each collection stores the entity reference under a different field name
    COLLECTION_ID_FIELD = {
        hp_public_appearances(): "source_id",
        hp_public_documents():   "entity_id",
        "public_civic_roles":       "source_id",
        hp_public_statements():  "entity_id",
    }
    c = _chroma()
    out = {}
    found_any = False
    for name, id_field in COLLECTION_ID_FIELD.items():
        try:
            result = _col(c, name).get(
                where={id_field: {"$eq": entity_id}},
                include=["documents", "metadatas"]
            )
            rows = [{"id": i, "document": d, "metadata": m}
                    for i, d, m in zip(result["ids"], result["documents"], result["metadatas"])
                    if m.get("_placeholder") != "true"]
            if rows:
                found_any = True
            out[name] = rows
        except Exception as e:
            out[name] = {"error": str(e)}
    if not found_any:
        raise KeyError(f"Entity '{entity_id}' not found in any civic collection")
    return out


# -------------------------------------------------------------------------
# INTERNAL HELPERS
# -------------------------------------------------------------------------

def _build_where(registration_layer, **kw) -> Optional[dict]:
    clauses = []
    if registration_layer is not None:
        clauses.append({"registration_layer": {"$eq": int(registration_layer)}})
    for k, v in kw.items():
        if v is not None:
            clauses.append({k: {"$eq": v}})
    return _merge_where(clauses)


def _merge_where(clauses: list) -> Optional[dict]:
    if not clauses:
        return None
    if len(clauses) == 1:
        return clauses[0]
    return {"$and": clauses}

===== services/hilbert/ingest_worker.py =====
"""
H_p ingest worker — all writes go through write_pipeline before touching Chroma.
"""
import os, hashlib, logging
from datetime import datetime, timezone
from typing import Optional
import chromadb
from chromadb.utils import embedding_functions
from write_pipeline import (
    IngestRecord, run_pipeline, DisclosureVerdict
)
from .collection_manifest import hp_public_appearances, hp_public_documents, hp_public_statements, civic_role_temporal

logger = logging.getLogger("hilbert.ingest_worker")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")

_EMBED_FN = embedding_functions.DefaultEmbeddingFunction()

def _chroma():
    return chromadb.HttpClient(
        host=os.getenv("CHROMA_HOST", "jarvis-chroma"),
        port=int(os.getenv("CHROMA_PORT", 8000)),
    )

def _col(client, name: str):
    return client.get_or_create_collection(
        name=name,
        embedding_function=_EMBED_FN,
        metadata={"hnsw:space": "cosine"},
    )

def _doc_id(source: str, entity_id: str, content: str) -> str:
    raw = f"{source}::{entity_id}::{content[:128]}"
    return hashlib.sha256(raw.encode()).hexdigest()[:32]

def _validate_meta(meta: dict) -> dict:
    layer = int(meta.get("registration_layer", 1))
    if layer not in (1, 2, 3):
        raise ValueError(f"registration_layer must be 1, 2, or 3 -- got {layer}")
    opt_in = bool(meta.get("public_opt_in", False))
    base = {
        "registration_layer": layer,
        "public_opt_in": opt_in,
        "source": str(meta.get("source", "unknown")),
        "entity_id": str(meta.get("entity_id", "")),
        "display_name": str(meta.get("display_name", "")),
        "ingested_at": datetime.now(timezone.utc).isoformat(),
    }
    for k in ("role", "effective_date", "expiry_date", "doc_type", "statement_type"):
        if meta.get(k) is not None:
            base[k] = str(meta[k])
    return base

def ingest_appearance(
    source_id: str,
    display_name_public: str,
    entity_class: str,
    role_class: str,
    publicness_basis: str,
    place_id: Optional[str] = None,
    time_start: Optional[str] = None,
    time_end: Optional[str] = None,
    registration_layer: int = 1,
    public_opt_in: bool = False,
    extra_meta: Optional[dict] = None,
) -> dict:
    """
    Run the full 5-stage write_pipeline before writing to public_civic_appearances.
    Returns {"status": "permitted"|"suppressed"|"escalated", "id": ..., "reason": ...}
    """
    record = IngestRecord(
        source_id=source_id,
        display_name_public=display_name_public,
        entity_class=entity_class,
        role_class=role_class,
        place_id=place_id,
        time_start=time_start,
        time_end=time_end,
        publicness_basis=publicness_basis,
        raw_metadata=extra_meta or {},
    )
    result = run_pipeline(record)

    if result.verdict != DisclosureVerdict.PERMIT:
        logger.warning(
            "ingest_appearance BLOCKED source_id=%s verdict=%s reason=%s",
            source_id, result.verdict, result.suppression_reason
        )
        return {
            "status": str(result.verdict).split(".")[-1].lower(),
            "id": None,
            "provenance_hash": result.provenance_hash,
            "reason": result.suppression_reason,
        }

    payload = result.appearance_payload
    payload["registration_layer"] = registration_layer
    payload["public_opt_in"] = public_opt_in
    payload["ingested_at"] = datetime.now(timezone.utc).isoformat()
    if extra_meta:
        payload.update({
            k: v for k, v in extra_meta.items()
            if k not in payload
        })

    doc_id = _doc_id(source_id, source_id, display_name_public + str(role_class))
    content = f"{payload.get('role_class','')} {payload.get('place_id','')} {entity_class}"

    # Chroma rejects None — coerce all None values to empty string
    clean_payload = {k: ("" if v is None else v) for k, v in payload.items()}

    col = _col(_chroma(), hp_public_appearances())
    col.upsert(ids=[doc_id], documents=[content], metadatas=[clean_payload])
    logger.info(
        "ingest_appearance OK id=%s source_id=%s layer=%s verdict=%s",
        doc_id, source_id, registration_layer, result.verdict
    )
    return {
        "status": "permitted",
        "id": doc_id,
        "provenance_hash": result.provenance_hash,
        "reason": None,
    }

def ingest_document(content: str, source: str, entity_id: str, display_name: str,
                    registration_layer: int = 1, public_opt_in: bool = False,
                    doc_type: str = "general", extra_meta: Optional[dict] = None) -> str:
    if not content.strip(): raise ValueError("content must not be empty")
    meta = {"registration_layer": registration_layer, "public_opt_in": public_opt_in,
            "source": source, "entity_id": entity_id, "display_name": display_name,
            "doc_type": doc_type, **(extra_meta or {})}
    meta = _validate_meta(meta)
    doc_id = _doc_id(source, entity_id, content)
    _col(_chroma(), hp_public_documents()).upsert(
        ids=[doc_id], documents=[content], metadatas=[meta])
    logger.info("ingest_document OK id=%s layer=%s entity=%s", doc_id, registration_layer, entity_id)
    return doc_id

def ingest_statement(content: str, source: str, entity_id: str, display_name: str,
                     registration_layer: int = 1, public_opt_in: bool = False,
                     statement_type: str = "general", extra_meta: Optional[dict] = None) -> str:
    if not content.strip(): raise ValueError("content must not be empty")
    meta = {"registration_layer": registration_layer, "public_opt_in": public_opt_in,
            "source": source, "entity_id": entity_id, "display_name": display_name,
            "statement_type": statement_type, **(extra_meta or {})}
    meta = _validate_meta(meta)
    doc_id = _doc_id(source, entity_id, content)
    _col(_chroma(), hp_public_statements()).upsert(
        ids=[doc_id], documents=[content], metadatas=[meta])
    logger.info("ingest_statement OK id=%s layer=%s entity=%s", doc_id, registration_layer, entity_id)
    return doc_id

def ingest_role_temporal(content: str, entity_id: str, display_name: str, role: str,
                         effective_date: str, expiry_date: Optional[str], source: str,
                         registration_layer: int = 1, public_opt_in: bool = False,
                         extra_meta: Optional[dict] = None) -> str:
    if not content.strip(): raise ValueError("content must not be empty")
    meta = {"registration_layer": registration_layer, "public_opt_in": public_opt_in,
            "source": source, "entity_id": entity_id, "display_name": display_name,
            "role": role, "effective_date": effective_date,
            **({"expiry_date": expiry_date} if expiry_date else {}), **(extra_meta or {})}
    meta = _validate_meta(meta)
    doc_id = _doc_id(source, entity_id, content)
    _col(_chroma(), civic_role_temporal()).upsert(
        ids=[doc_id], documents=[content], metadatas=[meta])
    logger.info("ingest_role_temporal OK id=%s role=%s entity=%s eff=%s",
                doc_id, role, entity_id, effective_date)
    return doc_id

===== services/hilbert/jarvis_hilbert_state.py =====
"""
Jarvis Hilbert State Service
Manages quantum/Hilbert-space state representations for the Jarvis cognitive architecture.
Serves both jarvis-hilbert-state (port 8081) and jarvis-hilbert-gateway (port 8081).
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import logging, os, time, redis
import requests
from datetime import datetime, timezone

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hilbert_state")

app = FastAPI(title="Jarvis Hilbert State Service")

# Redis for state persistence
REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379")
HILBERT_TIME_URL = os.getenv("HILBERT_TIME_URL", "http://jarvis-hilbert-time:8092")
_redis = None

def get_redis():
    global _redis
    if _redis is None:
        try:
            _redis = redis.from_url(REDIS_URL, decode_responses=True)
            _redis.ping()
        except Exception as e:
            logger.warning(f"Redis unavailable: {e}")
            _redis = None
    return _redis

class StateVector(BaseModel):
    state_id: str
    dimensions: Optional[Dict[str, float]] = {}
    metadata: Optional[Dict[str, Any]] = {}
    timestamp: Optional[float] = None

class StateQuery(BaseModel):
    state_id: str
    projection: Optional[List[str]] = None

class StateTransition(BaseModel):
    from_state: str
    to_state: str
    operator: Optional[str] = "identity"
    payload: Optional[Dict[str, Any]] = {}


def register_time_event(entity_id: str, payload: str):
    try:
        ts = datetime.now(timezone.utc).isoformat()
        requests.post(
            f"{HILBERT_TIME_URL}/timeline/register-json",
            json={"entity_id": entity_id, "timestamp": ts, "payload": payload},
            timeout=3,
        )
    except Exception as e:
        logger.warning(f"hilbert time registration failed: {e}")


ENTANGLEMENT_PEERS = [
    "ms_allis_active", "nbb_mother_carrie_protocols", "mountainshares_dao",
    "wv_geospatial", "hippocampus_chromadb", "nbb_darwin_godel_machines",
]

def auto_entangle(entity_id: str, score: float = 0.75):
    """Auto-record entanglement between a newly-set state and known active peers."""
    import json, time as _time
    r = get_redis()
    for peer in ENTANGLEMENT_PEERS:
        if peer == entity_id:
            continue
        key = f"hilbert:entanglement:{min(entity_id,peer)}:{max(entity_id,peer)}"
        data = {"entity_a": entity_id, "entity_b": peer,
                "entanglement_score": score, "state": "entangled",
                "depth": 1, "timestamp": _time.time(), "source": "auto_ingest"}
        if r:
            try:
                r.setex(key, 86400, json.dumps(data))
            except Exception as e:
                logger.warning(f"Redis entanglement write failed: {e}")
        register_time_event(entity_id, f"entanglement:{entity_id}<->{peer}:{score}")
        register_time_event(peer, f"entanglement:{entity_id}<->{peer}:{score}")

@app.get("/health")
def health():
    r = get_redis()
    redis_ok = r is not None
    return {
        "status": "ok",
        "service": "jarvis_hilbert_state",
        "redis": "connected" if redis_ok else "unavailable",
        "clock_ts": os.getenv("CLOCK_TS", "unset"),
        "port": os.getenv("SERVICE_PORT", "8081")
    }

@app.post("/state/set")
def set_state(sv: StateVector):
    if sv.timestamp is None:
        sv.timestamp = time.time()
    r = get_redis()
    if r:
        try:
            import json
            r.setex(f"hilbert:state:{sv.state_id}", 3600, json.dumps(sv.dict()))
        except Exception as e:
            logger.warning(f"Redis write failed: {e}")
    logger.info(f"State set: {sv.state_id} dims={len(sv.dimensions)}")
    register_time_event(sv.state_id, f"state_set:{sv.state_id}")
    return {"status": "ok", "state_id": sv.state_id, "timestamp": sv.timestamp}

@app.post("/state/get")
def get_state(q: StateQuery):
    r = get_redis()
    if r:
        try:
            import json
            raw = r.get(f"hilbert:state:{q.state_id}")
            if raw:
                data = json.loads(raw)
                if q.projection:
                    data["dimensions"] = {k: v for k, v in data.get("dimensions", {}).items()
                                          if k in q.projection}
                return {"found": True, "state": data}
        except Exception as e:
            logger.warning(f"Redis read failed: {e}")
    return {"found": False, "state_id": q.state_id}

@app.post("/state/transition")
def transition(t: StateTransition):
    logger.info(f"Transition {t.from_state} -> {t.to_state} via {t.operator}")
    register_time_event(t.to_state, f"state_transition:{t.from_state}->{t.to_state}:{t.operator}")
    return {
        "status": "ok",
        "from_state": t.from_state,
        "to_state": t.to_state,
        "operator": t.operator,
        "applied": True
    }

@app.get("/state/list")
def list_states():
    r = get_redis()
    if r:
        try:
            keys = r.keys("hilbert:state:*")
            return {"states": [k.replace("hilbert:state:", "") for k in keys], "count": len(keys)}
        except Exception as e:
            logger.warning(f"Redis list failed: {e}")
    return {"states": [], "count": 0}

@app.delete("/state/{state_id}")
def delete_state(state_id: str):
    r = get_redis()
    if r:
        try:
            r.delete(f"hilbert:state:{state_id}")
        except Exception as e:
            logger.warning(f"Redis delete failed: {e}")
    return {"status": "deleted", "state_id": state_id}

class EntanglementQuery(BaseModel):
    entity_a: str
    entity_b: str
    depth: Optional[int] = 1

@app.get("/entanglement")
def get_entanglement(entity_a: str, entity_b: str, depth: int = 1):
    """Query entanglement state between two entities."""
    logger.info(f"Entanglement query: {entity_a} <-> {entity_b} depth={depth}")
    r = get_redis()
    key = f"hilbert:entanglement:{min(entity_a,entity_b)}:{max(entity_a,entity_b)}"
    if r:
        try:
            import json
            raw = r.get(key)
            if raw:
                return {"found": True, "entanglement": json.loads(raw)}
        except Exception as e:
            logger.warning(f"Redis entanglement read failed: {e}")
    # Return a default unentangled state rather than 404
    return {
        "found": False,
        "entity_a": entity_a,
        "entity_b": entity_b,
        "entanglement_score": 0.0,
        "state": "unentangled",
        "depth": depth
    }

@app.post("/entanglement")
def set_entanglement(q: EntanglementQuery, score: float = 0.0):
    """Record entanglement between two entities."""
    r = get_redis()
    key = f"hilbert:entanglement:{min(q.entity_a,q.entity_b)}:{max(q.entity_a,q.entity_b)}"
    data = {"entity_a": q.entity_a, "entity_b": q.entity_b,
            "entanglement_score": score, "state": "entangled" if score > 0 else "unentangled",
            "depth": q.depth, "timestamp": time.time()}
    if r:
        try:
            import json
            r.setex(key, 86400, json.dumps(data))
        except Exception as e:
            logger.warning(f"Redis entanglement write failed: {e}")
    register_time_event(q.entity_a, f"entanglement:{q.entity_a}<->{q.entity_b}:{score}")
    register_time_event(q.entity_b, f"entanglement:{q.entity_a}<->{q.entity_b}:{score}")
    return {"status": "ok", **data}


# ── H_p Civic Query Route ────────────────────────────────────────────────────
import sys as _sys
_sys.path.insert(0, "/app/services/hilbert")
import civic_query as _civic_query
import chromadb as _chromadb
import os as _os

class CivicQuery(BaseModel):
    query_text: str

===== services/hilbert_commons/commons_aggregator.py =====
"""
commons_aggregator.py
Reads all public-opt-in L1 vectors from H_p collections,
projects into H_commons via Π, enforces k-anonymity,
upserts visible cluster centroids into community_hilbert_commons.
"""
import os, json, hashlib
from datetime import datetime, timezone

import chromadb
from projector import project
from kanon    import enforce_kanon

CHROMA_HOST = os.getenv("CHROMA_HOST", "jarvis-chroma")
CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8000"))

SOURCE_COLLECTIONS = [
    "public_civic_appearances",
    "public_civic_roles",
    "public_civic_documents",
    "public_civic_statements",
    "civic_role_temporal",
]

COMMONS_COLLECTION = "community_hilbert_commons"


def run():
    client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)

    try:
        commons = client.get_collection(COMMONS_COLLECTION)
    except Exception:
        commons = client.create_collection(
            COMMONS_COLLECTION,
            metadata={"hnsw:space": "cosine"},
        )

    projected = []

    for col_name in SOURCE_COLLECTIONS:
        try:
            col = client.get_collection(col_name)
        except Exception:
            print(f"  skipping {col_name} — not found")
            continue

        total = col.count()
        print(f"  {col_name}: {total} total records")
        if total == 0:
            continue

        offset = 0
        while True:
            batch = col.get(
                where={"$and": [
                    {"registration_layer": {"$lte": 1}},
                    {"public_opt_in": {"$eq": 1}},
                ]},
                include=["embeddings", "metadatas"],
                limit=500,
                offset=offset,
            )

            ids   = batch.get("ids") or []
            # embeddings may be a numpy array — convert safely
            raw_embs = batch.get("embeddings")
            if raw_embs is None:
                embs = []
            else:
                try:
                    embs = list(raw_embs)
                except Exception:
                    embs = []

            metas = batch.get("metadatas") or []

            if not ids:
                break

            for eid, emb, meta in zip(ids, embs, metas):
                if emb is None:
                    continue
                # convert numpy row to plain list
                try:
                    emb_list = emb.tolist()
                except AttributeError:
                    emb_list = list(emb)

                subspace_id = meta.get("display_name_public", eid)
                projected.append(project(emb_list, subspace_id, meta=meta))

            offset += len(ids)
            if len(ids) < 500:
                break

        print(f"    → {len(projected)} projected vectors so far")

    ts = datetime.now(timezone.utc).isoformat()
    print(f"\nTotal projected vectors: {len(projected)}")

    result = enforce_kanon(projected, ts)

    visible = result["visible"]
    print(f"Visible clusters: {len(visible)}  Suppressed: {result['suppressed_count']}")

    if visible:
        commons.upsert(
            ids=[
                hashlib.sha256(
                    (json.dumps(c["centroid"][:8]) + ts).encode()
                ).hexdigest()[:32]
                for c in visible
            ],
            embeddings=[c["centroid"] for c in visible],
            metadatas=[{
                "density":          c["density"],
                "sensitive":        str(c["sensitive"]),
                "aggregated_at":    ts,
                "k_min_applied":    10 if c["sensitive"] else 5,
                "source":           "community_hilbert_commons_v1",
            } for c in visible],
        )
        print(f"Upserted {len(visible)} cluster centroids → {COMMONS_COLLECTION}")

    print(json.dumps({
        "ts":               ts,
        "projected_in":     len(projected),
        "clusters_visible": len(visible),
        "suppressed":       result["suppressed_count"],
    }))


if __name__ == "__main__":
    run()

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild || cd ~/msjarvis-rebuild || exit 1
. crypto-venv/bin/activate
export PYTHONPATH="$PWD"

mkdir -p /tmp/msj_hilbert_client

printf '\n== minimal commons_aggregator reproduction ==\n' | tee /tmp/msj_hilbert_client/30_commons_run.txt
timeout 60s python services/hilbert_commons/commons_aggregator.py > /tmp/msj_hilbert_client/commons_aggregator.out 2>&1 || true
tail -n 120 /tmp/msj_hilbert_client/commons_aggregator.out | tee -a /tmp/msj_hilbert_client/30_commons_run.txt

printf '\n== minimal ingest_worker reproduction ==\n' | tee /tmp/msj_hilbert_client/31_ingest_run.txt
timeout 60s python -m services.hilbert.ingest_worker > /tmp/msj_hilbert_client/ingest_worker.out 2>&1 || true
tail -n 120 /tmp/msj_hilbert_client/ingest_worker.out | tee -a /tmp/msj_hilbert_client/31_ingest_run.txt

== minimal commons_aggregator reproduction ==
Traceback (most recent call last):
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/base_http_client.py", line 99, in _raise_chroma_error
    resp.raise_for_status()
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/httpx/_models.py", line 761, in raise_for_status
    raise HTTPStatusError(message, request=request, response=self)
httpx.HTTPStatusError: Client error '404 Not Found' for url 'http://jarvis-chroma:8000/api/v2/auth/identity'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/client.py", line 101, in get_user_identity
    return self._server.get_user_identity()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/__init__.py", line 150, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/fastapi.py", line 182, in get_user_identity
    return UserIdentity(**self._make_request("get", "/auth/identity"))
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/fastapi.py", line 90, in _make_request
    BaseHTTPClient._raise_chroma_error(response)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/base_http_client.py", line 104, in _raise_chroma_error
    raise (Exception(resp.text))
Exception: {"detail":"Not Found"}

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/mnt/spiritual_drive/msjarvis-rebuild/services/hilbert_commons/commons_aggregator.py", line 135, in <module>
    run()
  File "/mnt/spiritual_drive/msjarvis-rebuild/services/hilbert_commons/commons_aggregator.py", line 29, in run
    client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/__init__.py", line 203, in HttpClient
    return ClientCreator(tenant=tenant, database=database, settings=settings)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/client.py", line 65, in __init__
    user_identity = self.get_user_identity()
                    ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/chromadb/api/client.py", line 110, in get_user_identity
    raise ValueError(str(e))
ValueError: {"detail":"Not Found"}

== minimal ingest_worker reproduction ==
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/mnt/spiritual_drive/msjarvis-rebuild/services/hilbert/ingest_worker.py", line 9, in <module>
    from write_pipeline import (
ModuleNotFoundError: No module named 'write_pipeline'
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild || cd ~/msjarvis-rebuild || exit 1
. crypto-venv/bin/activate

printf '\n== post-fix Chroma counts ==\n'
python - << 'PY'
import chromadb

client = chromadb.HttpClient(host="127.0.0.1", port=8002)
targets = [
    "community_hilbert_commons",
    "hilbert_time",
    "civic_role_temporal",
    "conversation_gbim_private",
    "conversation_gbim_public",
    "conversation_history",
    "gbim_wv_counties_v2",
    "gbim_wv_tracts_v2",
]
print("collection,count")
for name in targets:
    try:
        c = client.get_collection(name=name)
        print(f"{name},{c.count()}")
PY      print(f"{name},ERROR:{e}")

== post-fix Chroma counts ==
collection,count
community_hilbert_commons,0
hilbert_time,0
civic_role_temporal,0
conversation_gbim_private,0
conversation_gbim_public,0
conversation_history,0
gbim_wv_counties_v2,55
gbim_wv_tracts_v2,546
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

