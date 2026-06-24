(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ # 1. Find Hilbert by grepping all service files and running scripts
grep -r -i "hilbert" /mnt/nvme1/msjarvis-rebuild/services/ \
  /mnt/nvme1/msjarvis-rebuild/scripts/ \
  /etc/systemd/system/ 2>/dev/null | grep -v ".pyc" | head -30

# 2. Find which port Hilbert state is on
grep -r -i "hilbert" /mnt/nvme1/msjarvis-rebuild/ \
  --include="*.py" --include="*.sh" --include="*.json" --include="*.yaml" \
  -l 2>/dev/null

# 3. Test the /communicate endpoint — this is the gateway's actual chat route
curl -s -X POST http://localhost:8300/communicate \
  -H "Content-Type: application/json" \
  -d '{"query": "ping", "context": {}}' | python3 -m json.tool

# 4. List all DGMs registered to see if Hilbert appears there
curl -s http://localhost:8300/dgms | python3 -m json.tool
/mnt/nvme1/msjarvis-rebuild/services/gateway_4_layers.log:✅ Hilbert: OK
/mnt/nvme1/msjarvis-rebuild/services/route_declarations_raw.txt:hilbert_spatial_chat.py:130:@app.get("/hilbert-space")
/mnt/nvme1/msjarvis-rebuild/services/route_declarations_raw.txt:hilbert_spatial_chat.py:154:@app.get("/graph/nearby_resources")
/mnt/nvme1/msjarvis-rebuild/services/route_declarations_raw.txt:hilbert_spatial_chat.py:204:@app.get("/graph/project_impact")
/mnt/nvme1/msjarvis-rebuild/services/route_declarations_raw.txt:hilbert_spatial_chat.py:259:@app.get("/health")
/mnt/nvme1/msjarvis-rebuild/services/route_declarations_raw.txt:hilbert_spatial_chat.py:290:@app.get("/")
/mnt/nvme1/msjarvis-rebuild/services/route_declarations_raw.txt:hilbert_spatial_chat.py:300:@app.post("/chat")
/mnt/nvme1/msjarvis-rebuild/services/hilbert_5002_restart.log:  File "/home/ms-jarvis/msjarvis-rebuild/services/hilbert_spatial_chat.py", line 4, in <module>
/mnt/nvme1/msjarvis-rebuild/services/METHOD_AUDIT_RAW.txt:/home/ms-jarvis/msjarvis-rebuild/services/hilbert_spatial_chat.py:16:def hilbert_space(
/mnt/nvme1/msjarvis-rebuild/services/METHOD_AUDIT_RAW.txt:/home/ms-jarvis/msjarvis-rebuild/services/hilbert_spatial_chat.py:83:def get_chromadb_client():
/mnt/nvme1/msjarvis-rebuild/services/METHOD_AUDIT_RAW.txt:/home/ms-jarvis/msjarvis-rebuild/services/hilbert_spatial_chat.py:92:def health():
/mnt/nvme1/msjarvis-rebuild/services/METHOD_AUDIT_RAW.txt:/home/ms-jarvis/msjarvis-rebuild/services/hilbert_spatial_chat.py:111:def root():
/mnt/nvme1/msjarvis-rebuild/services/METHOD_AUDIT_RAW.txt:/home/ms-jarvis/msjarvis-rebuild/services/hilbert_spatial_chat.py:120:async def chat_endpoint(request: Request):
/mnt/nvme1/msjarvis-rebuild/services/METHOD_AUDIT_RAW.txt:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED.py:545:async def hilbert_space_proxy(data: str = Query("", description="Data/vector for Hilbert computation/query")):
/mnt/nvme1/msjarvis-rebuild/services/METHOD_AUDIT_RAW.txt:/home/ms-jarvis/msjarvis-rebuild/services/register_to_hilbert_chromadb.py:8:def register_service(service_name, service_path):
/mnt/nvme1/msjarvis-rebuild/services/register_to_hilbert_chromadb.py:print("\n✓ All services registered into Hilbert Quantum ChromaDB!")
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py:logger = logging.getLogger("hilbert_spatial_chat")
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py:app = FastAPI(title="Hilbert Spatial Chat Service")
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py:    Discover and cache the set of collections Hilbert should search.
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py:    logger.info(f"Hilbert TARGET_COLLECTIONS = {TARGET_COLLECTIONS_CACHE}")
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py:@app.get("/hilbert-space")
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py:def hilbert_space(
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py:    data: str = Query(..., description="Query text for Hilbert vector search"),
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py:    Query Hilbert space vectors across multiple ChromaDB collections and
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py:            "error": f"Hilbert/ChromaDB vector query failed: {str(e)[:200]}",
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py:        "service": "hilbert_spatial_chat",
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py:        "service": "hilbert_spatial_chat",
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py:        "description": "Hilbert space vector embeddings with quantum-aware spatial reasoning + LLM consensus",
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py:                    "agent_used": "Hilbert spatial/LLM",
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py:                    "processing_flow": "Hilbert→ChromaDB→Consensus",
/mnt/nvme1/msjarvis-rebuild/gisgeodb_storage.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/sparse/linalg/tests/test_propack.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/linalg/interpolative.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/linalg/__init__.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/linalg/special_matrices.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/linalg/tests/test_interpolative.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/linalg/tests/test_special_matrices.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/linalg/_special_matrices.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/fftpack/__init__.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/fftpack/pseudo_diffs.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/fftpack/tests/test_pseudo_diffs.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/fftpack/_pseudo_diffs.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/signal/_delegators.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/signal/_support_alternative_backends.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/signal/__init__.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/signal/tests/test_signaltools.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/signal/tests/test_fir_filter_design.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/signal/_fir_filter_design.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/signal/signaltools.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/scipy/signal/_signaltools.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sklearn/linear_model/tests/test_least_angle.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sklearn/preprocessing/_data.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/mpmath/matrices/calculus.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/mpmath/matrices/matrices.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/mpmath/matrices/linalg.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/mpmath/__init__.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/mpmath/tests/test_linalg.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/mpmath/tests/test_matrices.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/ftfy/fixes.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/geopandas/array.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/geopandas/base.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/geopandas/tools/tests/test_hilbert_curve.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/geopandas/tools/hilbert_curve.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/pygments/lexers/_scilab_builtins.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/pygments/lexers/_csound_builtins.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/pygments/lexers/macaulay2.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/pygments/lexers/idl.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/pygments/lexers/igor.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/printing/tests/test_mathml.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/printing/mathml.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/state.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/fermion.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/cartesian.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/qubit.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/qexpr.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/spin.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/operator.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/represent.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/grover.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/__init__.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/gate.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/qft.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/sho1d.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_qexpr.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_piab.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_cartesian.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_state.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_sho1d.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_printing.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_operator.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_hilbert.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/piab.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/pauli.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/boson.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/operatorordering.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/physics/quantum/hilbert.py
/mnt/nvme1/msjarvis-rebuild/.venv/lib/python3.12/site-packages/sympy/core/tests/test_args.py
/mnt/nvme1/msjarvis-rebuild/services/register_to_hilbert_chromadb.py
/mnt/nvme1/msjarvis-rebuild/services/hilbert_spatial_chat.py
/mnt/nvme1/msjarvis-rebuild/services/quantum_state_engine.py
/mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_web_research.py
/mnt/nvme1/msjarvis-rebuild/services/msjarvisconsciousnessbridge.py
/mnt/nvme1/msjarvis-rebuild/services/gdb_integration_service.py
/mnt/nvme1/msjarvis-rebuild/services/register_hilbert_services.py
/mnt/nvme1/msjarvis-rebuild/services/load_geodb_health_providers_to_neo4j.py
/mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_autonomous_learner_optimized.py
/mnt/nvme1/msjarvis-rebuild/services/load_geodb_hospitals_to_neo4j.py
/mnt/nvme1/msjarvis-rebuild/services/rag_server_main.py
/mnt/nvme1/msjarvis-rebuild/services/retrieval_router.py
/mnt/nvme1/msjarvis-rebuild/services/msjarvisunifiedswaggergatewayFIXED.py
/mnt/nvme1/msjarvis-rebuild/services/register_all_services.sh
/mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway_FIXED.py
/mnt/nvme1/msjarvis-rebuild/services/start_hilbert_8235.sh
/mnt/nvme1/msjarvis-rebuild/services/jarvis_llm1.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/sparse/linalg/tests/test_propack.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/linalg/interpolative.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/linalg/__init__.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/linalg/special_matrices.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/linalg/tests/test_interpolative.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/linalg/tests/test_special_matrices.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/linalg/_special_matrices.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/fftpack/__init__.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/fftpack/pseudo_diffs.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/fftpack/tests/test_pseudo_diffs.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/fftpack/_pseudo_diffs.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/signal/_delegators.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/signal/_support_alternative_backends.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/signal/__init__.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/signal/tests/test_signaltools.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/signal/tests/test_fir_filter_design.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/signal/_fir_filter_design.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/signal/signaltools.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/scipy/signal/_signaltools.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sklearn/linear_model/tests/test_least_angle.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sklearn/preprocessing/_data.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/mpmath/matrices/calculus.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/mpmath/matrices/matrices.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/mpmath/matrices/linalg.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/mpmath/__init__.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/mpmath/tests/test_linalg.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/mpmath/tests/test_matrices.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/pygments/lexers/_scilab_builtins.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/pygments/lexers/_csound_builtins.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/pygments/lexers/macaulay2.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/pygments/lexers/idl.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/pygments/lexers/igor.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/printing/tests/test_mathml.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/printing/mathml.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/state.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/fermion.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/cartesian.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/qubit.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/qexpr.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/spin.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/operator.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/represent.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/grover.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/__init__.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/gate.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/qft.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/sho1d.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_qexpr.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_piab.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_cartesian.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_state.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_sho1d.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_printing.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_operator.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_hilbert.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/piab.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/pauli.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/boson.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/operatorordering.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/physics/quantum/hilbert.py
/mnt/nvme1/msjarvis-rebuild/services/venv/lib/python3.12/site-packages/sympy/core/tests/test_args.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/mpmath/matrices/calculus.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/mpmath/matrices/matrices.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/mpmath/matrices/linalg.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/mpmath/__init__.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/mpmath/tests/test_linalg.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/mpmath/tests/test_matrices.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/pygments/lexers/_scilab_builtins.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/pygments/lexers/_csound_builtins.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/pygments/lexers/macaulay2.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/pygments/lexers/idl.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/pygments/lexers/igor.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/tests/test_mathml.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/printing/mathml.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/state.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/fermion.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/cartesian.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/qubit.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/qexpr.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/spin.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/operator.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/represent.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/grover.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/__init__.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/gate.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/qft.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/sho1d.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_qexpr.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_piab.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_cartesian.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_state.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_sho1d.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_printing.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_operator.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_hilbert.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/piab.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/pauli.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/boson.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/operatorordering.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/physics/quantum/hilbert.py
/mnt/nvme1/msjarvis-rebuild/services/chroma_inspect_venv/lib/python3.12/site-packages/sympy/core/tests/test_args.py
/mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_web_research_aggregate.safe.20260119-094221.py
/mnt/nvme1/msjarvis-rebuild/services/msjarvis_gateway_with_judge_filtering.py
/mnt/nvme1/msjarvis-rebuild/services/consciousness_coordinator.py
/mnt/nvme1/msjarvis-rebuild/services/quantum_insight_llm.py
/mnt/nvme1/msjarvis-rebuild/services/batch_patch_services.py
/mnt/nvme1/msjarvis-rebuild/services/gbim_chroma.py
/mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_web_research_aggregate.py
/mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_autonomous_learner.py
/mnt/nvme1/msjarvis-rebuild/services/dgm_bridge.py
/mnt/nvme1/msjarvis-rebuild/services/agi_test.sh
/mnt/nvme1/msjarvis-rebuild/services/msjarvis_gateway_v2_final.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/mpmath/matrices/calculus.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/mpmath/matrices/matrices.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/mpmath/matrices/linalg.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/mpmath/__init__.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/mpmath/tests/test_linalg.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/mpmath/tests/test_matrices.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/pygments/lexers/_scilab_builtins.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/pygments/lexers/_csound_builtins.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/pygments/lexers/macaulay2.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/pygments/lexers/idl.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/pygments/lexers/igor.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/printing/tests/test_mathml.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/printing/mathml.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/state.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/fermion.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/cartesian.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/qubit.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/qexpr.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/spin.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/operator.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/represent.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/grover.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/__init__.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/gate.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/qft.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/sho1d.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_qexpr.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_piab.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_cartesian.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_state.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_sho1d.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_printing.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_operator.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_hilbert.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/piab.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/pauli.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/boson.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/operatorordering.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/physics/quantum/hilbert.py
/mnt/nvme1/msjarvis-rebuild/msjarvis_tests/.venv/lib/python3.12/site-packages/sympy/core/tests/test_args.py
/mnt/nvme1/msjarvis-rebuild/rag_server_main.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/mpmath/matrices/calculus.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/mpmath/matrices/matrices.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/mpmath/matrices/linalg.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/mpmath/__init__.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/mpmath/tests/test_linalg.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/mpmath/tests/test_matrices.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/pygments/lexers/_scilab_builtins.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/pygments/lexers/_csound_builtins.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/pygments/lexers/macaulay2.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/pygments/lexers/idl.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/pygments/lexers/igor.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/printing/tests/test_mathml.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/printing/mathml.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/state.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/fermion.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/cartesian.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/qubit.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/qexpr.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/spin.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/operator.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/represent.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/grover.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/__init__.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/gate.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/qft.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/sho1d.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_qexpr.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_piab.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_cartesian.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_state.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_sho1d.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_printing.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_operator.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_hilbert.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/piab.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/pauli.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/boson.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/operatorordering.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/physics/quantum/hilbert.py
/mnt/nvme1/msjarvis-rebuild/.venv-chroma/lib/python3.12/site-packages/sympy/core/tests/test_args.py
/mnt/nvme1/msjarvis-rebuild/gbim_orchestrator.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/mpmath/matrices/calculus.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/mpmath/matrices/matrices.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/mpmath/matrices/linalg.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/mpmath/__init__.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/mpmath/tests/test_linalg.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/mpmath/tests/test_matrices.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/pygments/lexers/_scilab_builtins.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/pygments/lexers/_csound_builtins.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/pygments/lexers/macaulay2.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/pygments/lexers/idl.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/pygments/lexers/igor.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/printing/tests/test_mathml.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/printing/mathml.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/state.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/fermion.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/cartesian.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/qubit.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/qexpr.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/spin.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/operator.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/represent.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/grover.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/__init__.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/gate.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/qft.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/sho1d.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_qexpr.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_piab.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_cartesian.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_state.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_sho1d.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_printing.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_operator.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/tests/test_hilbert.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/piab.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/pauli.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/boson.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/operatorordering.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/physics/quantum/hilbert.py
/mnt/nvme1/msjarvis-rebuild/oldchroma-venv/lib/python3.12/site-packages/sympy/core/tests/test_args.py
/mnt/nvme1/msjarvis-rebuild/backups/rag_server_main.STABLE_20260121_162220.py
/mnt/nvme1/msjarvis-rebuild/gdb_result_snapshot.json
{
    "detail": [
        {
            "type": "missing",
            "loc": [
                "body",
                "message"
            ],
            "msg": "Field required",
            "input": {
                "query": "ping",
                "context": {}
            }
        }
    ]
}
{
    "status": "qualia_69dgm_map",
    "layers": {
        "layer_1_input_validation": [
            {
                "id": "validator_1",
                "layer": 1,
                "port": 5201
            },
            {
                "id": "validator_2",
                "layer": 1,
                "port": 5202
            },
            {
                "id": "validator_3",
                "layer": 1,
                "port": 5203
            },
            {
                "id": "validator_4",
                "layer": 1,
                "port": 5204
            },
            {
                "id": "validator_5",
                "layer": 1,
                "port": 5205
            },
            {
                "id": "validator_6",
                "layer": 1,
                "port": 5206
            },
            {
                "id": "validator_7",
                "layer": 1,
                "port": 5207
            },
            {
                "id": "validator_8",
                "layer": 1,
                "port": 5208
            },
            {
                "id": "validator_9",
                "layer": 1,
                "port": 5209
            },
            {
                "id": "validator_10",
                "layer": 1,
                "port": 5210
            },
            {
                "id": "validator_11",
                "layer": 1,
                "port": 5211
            },
            {
                "id": "validator_12",
                "layer": 1,
                "port": 5212
            },
            {
                "id": "validator_13",
                "layer": 1,
                "port": 5213
            },
            {
                "id": "validator_14",
                "layer": 1,
                "port": 5214
            },
            {
                "id": "validator_15",
                "layer": 1,
                "port": 5215
            },
            {
                "id": "validator_16",
                "layer": 1,
                "port": 5216
            },
            {
                "id": "validator_17",
                "layer": 1,
                "port": 5217
            },
            {
                "id": "validator_18",
                "layer": 1,
                "port": 5218
            },
            {
                "id": "validator_19",
                "layer": 1,
                "port": 5219
            },
            {
                "id": "validator_20",
                "layer": 1,
                "port": 5220
            },
            {
                "id": "validator_21",
                "layer": 1,
                "port": 5221
            },
            {
                "id": "validator_22",
                "layer": 1,
                "port": 5222
            },
            {
                "id": "validator_23",
                "layer": 1,
                "port": 5223
            }
        ],
        "layer_2_knowledge_validation": [
            {
                "id": "validator_1",
                "layer": 2,
                "port": 5224
            },
            {
                "id": "validator_2",
                "layer": 2,
                "port": 5225
            },
            {
                "id": "validator_3",
                "layer": 2,
                "port": 5226
            },
            {
                "id": "validator_4",
                "layer": 2,
                "port": 5227
            },
            {
                "id": "validator_5",
                "layer": 2,
                "port": 5228
            },
            {
                "id": "validator_6",
                "layer": 2,
                "port": 5229
            },
            {
                "id": "validator_7",
                "layer": 2,
                "port": 5230
            },
            {
                "id": "validator_8",
                "layer": 2,
                "port": 5231
            },
            {
                "id": "validator_9",
                "layer": 2,
                "port": 5232
            },
            {
                "id": "validator_10",
                "layer": 2,
                "port": 5233
            },
            {
                "id": "validator_11",
                "layer": 2,
                "port": 5234
            },
            {
                "id": "validator_12",
                "layer": 2,
                "port": 5235
            },
            {
                "id": "validator_13",
                "layer": 2,
                "port": 5236
            },
            {
                "id": "validator_14",
                "layer": 2,
                "port": 5237
            },
            {
                "id": "validator_15",
                "layer": 2,
                "port": 5238
            },
            {
                "id": "validator_16",
                "layer": 2,
                "port": 5239
            },
            {
                "id": "validator_17",
                "layer": 2,
                "port": 5240
            },
            {
                "id": "validator_18",
                "layer": 2,
                "port": 5241
            },
            {
                "id": "validator_19",
                "layer": 2,
                "port": 5242
            },
            {
                "id": "validator_20",
                "layer": 2,
                "port": 5243
            },
            {
                "id": "validator_21",
                "layer": 2,
                "port": 5244
            },
            {
                "id": "validator_22",
                "layer": 2,
                "port": 5245
            },
            {
                "id": "validator_23",
                "layer": 2,
                "port": 5246
            }
        ],
        "layer_3_output_validation": [
            {
                "id": "validator_1",
                "layer": 3,
                "port": 5247
            },
            {
                "id": "validator_2",
                "layer": 3,
                "port": 5248
            },
            {
                "id": "validator_3",
                "layer": 3,
                "port": 5249
            },
            {
                "id": "validator_4",
                "layer": 3,
                "port": 5250
            },
            {
                "id": "validator_5",
                "layer": 3,
                "port": 5251
            },
            {
                "id": "validator_6",
                "layer": 3,
                "port": 5252
            },
            {
                "id": "validator_7",
                "layer": 3,
                "port": 5253
            },
            {
                "id": "validator_8",
                "layer": 3,
                "port": 5254
            },
            {
                "id": "validator_9",
                "layer": 3,
                "port": 5255
            },
            {
                "id": "validator_10",
                "layer": 3,
                "port": 5256
            },
            {
                "id": "validator_11",
                "layer": 3,
                "port": 5257
            },
            {
                "id": "validator_12",
                "layer": 3,
                "port": 5258
            },
            {
                "id": "validator_13",
                "layer": 3,
                "port": 5259
            },
            {
                "id": "validator_14",
                "layer": 3,
                "port": 5260
            },
            {
                "id": "validator_15",
                "layer": 3,
                "port": 5261
            },
            {
                "id": "validator_16",
                "layer": 3,
                "port": 5262
            },
            {
                "id": "validator_17",
                "layer": 3,
                "port": 5263
            },
            {
                "id": "validator_18",
                "layer": 3,
                "port": 5264
            },
            {
                "id": "validator_19",
                "layer": 3,
                "port": 5265
            },
            {
                "id": "validator_20",
                "layer": 3,
                "port": 5266
            },
            {
                "id": "validator_21",
                "layer": 3,
                "port": 5267
            },
            {
                "id": "validator_22",
                "layer": 3,
                "port": 5268
            },
            {
                "id": "validator_23",
                "layer": 3,
                "port": 5269
            }
        ]
    },
    "total_dgms": 69
}
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ 

