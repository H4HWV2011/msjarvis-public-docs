(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ cd ~/msjarvis-rebuild || exit 1
mkdir -p ~/hp-antisurveillance-next-20260629-015308/artifacts

cat > hp_antisurveillance_policy.json <<'JSON'
{
  "forbidden_action_types": [
    "person_analytics_request",
    "identity_linkage_attempt",
    "unified_person_profile"
  ],
  "forbidden_purposes": [
    "person_analytics",
    "identity_linkage",
    "unified_profile"
  ],
  "forbidden_tables": [
    "public.kyc_vault",
    "public.kyc_location_strip",
    "public.kyc_vault_access_log",
    "public.user_documents",
    "public.interaction_provenance_immutable"
  ],
  "guarded_tables": [
PY  }   "purpose": "person_analytics"ersationgbimprivate"],","public.user
{
  "forbidden_action_types": [
    "person_analytics_request",
    "identity_linkage_attempt",
    "unified_person_profile"
  ],
  "forbidden_purposes": [
    "person_analytics",
    "identity_linkage",
    "unified_profile"
  ],
  "forbidden_tables": [
    "public.kyc_vault",
    "public.kyc_location_strip",
    "public.kyc_vault_access_log",
    "public.user_documents",
    "public.interaction_provenance_immutable"
  ],
  "guarded_tables": [
    "public.gbim_entities",
    "public.document_chunks"
  ],
  "forbidden_collections": [
    "faces",
    "conversationgbimprivate"
  ],
  "guarded_collections": [
    "gbimentities",
    "conversationgbimpublic"
  ]
}
{'allowed': False, 'decision': 'denied', 'principles_applied': ['hp-anti-dossier', 'hp-context-anchor', 'gw-public-benefit'], 'constitution_version': '1.0.0-fallback', 'reason': 'Client-side anti-surveillance: forbidden action_type.'}
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ cd ~/msjarvis-rebuild || exit 1

python3 - <<'PY'
from pathlib import Path
import re, json

patterns = [
    r'gbim_entities',
    r'document_chunks',
    r'kyc_vault',
    r'kyc_location_strip',
    r'kyc_vault_access_log',
    r'user_documents',
    r'interaction_provenance_immutable',
    r'conversationgbimprivate',
    r'conversationgbimpublic',
    r'faces',
    r'constitutional_check',
    r'/constitutional/check',
]
root = Path(".")
hits = {}
for p in root.rglob("*.py"):
PY  print(k, "=>", ",".join(hits[k]))t=2, sort_keys=True))308" / "artifac
/home/cakidd/hp-antisurveillance-next-20260629-015308/artifacts/guarded-code-candidates.json
count= 565
.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py => constitutional_check,/constitutional/check
.archive/services.backup_20260308_111532/jarvis-hippocampus_hippocampus_service.py => gbim_entities,faces
.archive/services.backup_20260308_111532/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py => gbim_entities,faces
.check_venv/lib/python3.12/site-packages/anyio/_core/_sockets.py => faces
.check_venv/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py => faces
.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py => faces
.check_venv/lib/python3.12/site-packages/click/core.py => faces
.check_venv/lib/python3.12/site-packages/grpc/__init__.py => faces
.check_venv/lib/python3.12/site-packages/grpc/beta/_client_adaptations.py => faces
.check_venv/lib/python3.12/site-packages/grpc/beta/_server_adaptations.py => faces
.check_venv/lib/python3.12/site-packages/grpc/beta/implementations.py => faces
.check_venv/lib/python3.12/site-packages/grpc/beta/interfaces.py => faces
.check_venv/lib/python3.12/site-packages/grpc/beta/utilities.py => faces
.check_venv/lib/python3.12/site-packages/grpc/framework/foundation/stream.py => faces
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/base/utilities.py => faces
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/face.py => faces
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/utilities.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/__init__.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/connection.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/connection_pool.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/http11.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/http2.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/http_proxy.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_models.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/__init__.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/connection.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/connection_pool.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http11.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http2.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http_proxy.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py => faces
.check_venv/lib/python3.12/site-packages/httpx/_content.py => faces
.check_venv/lib/python3.12/site-packages/jsonschema/protocols.py => faces
.check_venv/lib/python3.12/site-packages/mpmath/ctx_iv.py => faces
.check_venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py => faces
.check_venv/lib/python3.12/site-packages/mpmath/rational.py => faces
.check_venv/lib/python3.12/site-packages/numpy/_core/_add_newdocs.py => faces
.check_venv/lib/python3.12/site-packages/numpy/_core/tests/test_multiarray.py => faces
.check_venv/lib/python3.12/site-packages/numpy/random/tests/test_direct.py => faces
.check_venv/lib/python3.12/site-packages/numpy/typing/mypy_plugin.py => faces
.check_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/host_attributes.py => faces
.check_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py => faces
.check_venv/lib/python3.12/site-packages/packaging/version.py => faces
.check_venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py => faces
.check_venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py => faces
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__init__.py => user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__main__.py => user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/android.py => user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/api.py => user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/macos.py => user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py => user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/windows.py => user_documents
.check_venv/lib/python3.12/site-packages/pydantic/v1/_hypothesis_plugin.py => faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/_cocoa_builtins.py => faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/_lilypond_builtins.py => faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py => faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/_scheme_builtins.py => faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/freefem.py => faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/macaulay2.py => faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/matlab.py => faces
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/generators.py => faces
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/polyhedron.py => faces
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/tests/test_polyhedron.py => faces
.check_venv/lib/python3.12/site-packages/sympy/core/basic.py => faces
.check_venv/lib/python3.12/site-packages/sympy/core/containers.py => faces
.check_venv/lib/python3.12/site-packages/sympy/core/tests/test_args.py => faces
.check_venv/lib/python3.12/site-packages/sympy/geometry/line.py => faces
.check_venv/lib/python3.12/site-packages/sympy/geometry/parabola.py => faces
.check_venv/lib/python3.12/site-packages/sympy/integrals/intpoly.py => faces
.check_venv/lib/python3.12/site-packages/sympy/integrals/tests/test_intpoly.py => faces
.check_venv/lib/python3.12/site-packages/sympy/interactive/printing.py => faces
.check_venv/lib/python3.12/site-packages/sympy/physics/mechanics/actuator.py => faces
.check_venv/lib/python3.12/site-packages/sympy/physics/mechanics/wrapping_geometry.py => faces
.check_venv/lib/python3.12/site-packages/sympy/physics/quantum/identitysearch.py => faces
.check_venv/lib/python3.12/site-packages/sympy/plotting/backends/base_backend.py => faces
.check_venv/lib/python3.12/site-packages/sympy/plotting/plot.py => faces
.check_venv/lib/python3.12/site-packages/sympy/plotting/pygletplot/plot.py => faces
.check_venv/lib/python3.12/site-packages/sympy/plotting/series.py => faces
.check_venv/lib/python3.12/site-packages/sympy/plotting/tests/test_plot.py => faces
.check_venv/lib/python3.12/site-packages/sympy/printing/pretty/tests/test_pretty.py => faces
.check_venv/lib/python3.12/site-packages/sympy/stats/rv.py => faces
.check_venv/lib/python3.12/site-packages/sympy/unify/core.py => faces
.check_venv/lib/python3.12/site-packages/sympy/vector/implicitregion.py => faces
.check_venv/lib/python3.12/site-packages/uvicorn/workers.py => faces
ai_server_20llm_PRODUCTION.py => gbim_entities
auth_router.py => kyc_vault
crypto-venv/lib/python3.12/site-packages/anyio/_core/_sockets.py => faces
crypto-venv/lib/python3.12/site-packages/art/data/fonts2.py => faces
crypto-venv/lib/python3.12/site-packages/art/data/fonts3.py => faces
crypto-venv/lib/python3.12/site-packages/art/params.py => faces
crypto-venv/lib/python3.12/site-packages/art/tests/test.py => faces
crypto-venv/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py => faces
crypto-venv/lib/python3.12/site-packages/click/core.py => faces
crypto-venv/lib/python3.12/site-packages/cryptography/hazmat/backends/openssl/backend.py => faces
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydev_bundle/_pydev_jy_imports_tipper.py => faces
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydevd_bundle/pydevconsole_code.py => faces
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_resolver.py => faces
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/pydevd_attach_to_process/winappdbg/sql.py => faces
crypto-venv/lib/python3.12/site-packages/demjson3.py => faces
crypto-venv/lib/python3.12/site-packages/distro/distro.py => faces
crypto-venv/lib/python3.12/site-packages/dns/win32util.py => faces
crypto-venv/lib/python3.12/site-packages/eth_typing/abi.py => faces
crypto-venv/lib/python3.12/site-packages/eth_utils/abi.py => faces
crypto-venv/lib/python3.12/site-packages/feedparser/parsers/loose.py => faces
crypto-venv/lib/python3.12/site-packages/feedparser/parsers/strict.py => faces
crypto-venv/lib/python3.12/site-packages/fiona/io.py => faces
crypto-venv/lib/python3.12/site-packages/fontTools/designspaceLib/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/fontTools/misc/cliTools.py => faces
crypto-venv/lib/python3.12/site-packages/fontTools/ufoLib/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/geoalchemy2/_functions.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/beta/_client_adaptations.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/beta/_server_adaptations.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/beta/implementations.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/beta/interfaces.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/beta/utilities.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/framework/foundation/stream.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/base/utilities.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/face.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/utilities.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_async/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_async/connection.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_async/connection_pool.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_async/http11.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_async/http2.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_async/http_proxy.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_models.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/connection.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/connection_pool.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http11.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http2.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http_proxy.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py => faces
crypto-venv/lib/python3.12/site-packages/httpx/_content.py => faces
crypto-venv/lib/python3.12/site-packages/ipykernel/heartbeat.py => faces
crypto-venv/lib/python3.12/site-packages/ipykernel/inprocess/blocking.py => faces
crypto-venv/lib/python3.12/site-packages/ipykernel/iostream.py => faces
crypto-venv/lib/python3.12/site-packages/jeepney/bindgen.py => faces
crypto-venv/lib/python3.12/site-packages/jeepney/tests/test_bindgen.py => faces
crypto-venv/lib/python3.12/site-packages/jeepney/wrappers.py => faces
crypto-venv/lib/python3.12/site-packages/jsonschema/protocols.py => faces
crypto-venv/lib/python3.12/site-packages/jupyter_client/blocking/client.py => faces
crypto-venv/lib/python3.12/site-packages/jupyter_client/connect.py => faces
crypto-venv/lib/python3.12/site-packages/jupyter_client/consoleapp.py => faces
crypto-venv/lib/python3.12/site-packages/jupyter_client/localinterfaces.py => faces
crypto-venv/lib/python3.12/site-packages/jupyter_client/provisioning/local_provisioner.py => faces
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1_device_constraint.py => faces
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1beta1_device_constraint.py => faces
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1beta2_device_constraint.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/axes/_axes.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/backends/backend_cairo.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/collections.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/colors.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/figure.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/legend.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/pylab.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/pyplot.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_colors.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_ft2font.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_triangulation.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/tri/_tripcolor.py => faces
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/art3d.py => faces
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/axes3d.py => faces
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/tests/test_axes3d.py => faces
crypto-venv/lib/python3.12/site-packages/mpmath/ctx_iv.py => faces
crypto-venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py => faces
crypto-venv/lib/python3.12/site-packages/mpmath/rational.py => faces
crypto-venv/lib/python3.12/site-packages/networkx/algorithms/planar_drawing.py => faces
crypto-venv/lib/python3.12/site-packages/networkx/algorithms/planarity.py => faces
crypto-venv/lib/python3.12/site-packages/networkx/generators/small.py => faces
crypto-venv/lib/python3.12/site-packages/numpy/_core/_add_newdocs.py => faces
crypto-venv/lib/python3.12/site-packages/numpy/_core/tests/test_multiarray.py => faces
crypto-venv/lib/python3.12/site-packages/numpy/random/tests/test_direct.py => faces
crypto-venv/lib/python3.12/site-packages/numpy/typing/mypy_plugin.py => faces
crypto-venv/lib/python3.12/site-packages/onnx_ir/_protocols.py => faces
crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/host_attributes.py => faces
crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py => faces
crypto-venv/lib/python3.12/site-packages/packaging/version.py => faces
crypto-venv/lib/python3.12/site-packages/pandas/core/groupby/generic.py => faces
crypto-venv/lib/python3.12/site-packages/pandas/tests/plotting/frame/test_frame.py => faces
crypto-venv/lib/python3.12/site-packages/pexpect/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py => faces
crypto-venv/lib/python3.12/site-packages/pip/_vendor/packaging/version.py => faces
crypto-venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__init__.py => user_documents
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__main__.py => user_documents
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/android.py => user_documents
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/api.py => user_documents
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/macos.py => user_documents
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py => user_documents
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/windows.py => user_documents
crypto-venv/lib/python3.12/site-packages/pip_audit/_dependency_source/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/pip_audit/_dependency_source/interface.py => faces
crypto-venv/lib/python3.12/site-packages/pip_audit/_format/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/pip_audit/_format/interface.py => faces
crypto-venv/lib/python3.12/site-packages/pip_audit/_service/__init__.py => faces
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ 
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ cd ~/msjarvis-rebuild || exit 1

python3 - <<'PY'
from pathlib import Path
import re, json

patterns = [
    r'gbim_entities',
    r'document_chunks',
    r'kyc_vault',
    r'kyc_location_strip',
    r'kyc_vault_access_log',
    r'user_documents',
    r'interaction_provenance_immutable',
    r'conversationgbimprivate',
    r'conversationgbimpublic',
    r'faces',
    r'constitutional_check',
    r'/constitutional/check',
]
root = Path(".")
hits = {}
for p in root.rglob("*.py"):
PY  print(k, "=>", ",".join(hits[k]))t=2, sort_keys=True))308" / "artifac
/home/cakidd/hp-antisurveillance-next-20260629-015308/artifacts/guarded-code-candidates.json
count= 565
.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py => constitutional_check,/constitutional/check
.archive/services.backup_20260308_111532/jarvis-hippocampus_hippocampus_service.py => gbim_entities,faces
.archive/services.backup_20260308_111532/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py => gbim_entities,faces
.check_venv/lib/python3.12/site-packages/anyio/_core/_sockets.py => faces
.check_venv/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py => faces
.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py => faces
.check_venv/lib/python3.12/site-packages/click/core.py => faces
.check_venv/lib/python3.12/site-packages/grpc/__init__.py => faces
.check_venv/lib/python3.12/site-packages/grpc/beta/_client_adaptations.py => faces
.check_venv/lib/python3.12/site-packages/grpc/beta/_server_adaptations.py => faces
.check_venv/lib/python3.12/site-packages/grpc/beta/implementations.py => faces
.check_venv/lib/python3.12/site-packages/grpc/beta/interfaces.py => faces
.check_venv/lib/python3.12/site-packages/grpc/beta/utilities.py => faces
.check_venv/lib/python3.12/site-packages/grpc/framework/foundation/stream.py => faces
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/base/utilities.py => faces
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/face.py => faces
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/utilities.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/__init__.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/connection.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/connection_pool.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/http11.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/http2.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/http_proxy.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_models.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/__init__.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/connection.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/connection_pool.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http11.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http2.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http_proxy.py => faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py => faces
.check_venv/lib/python3.12/site-packages/httpx/_content.py => faces
.check_venv/lib/python3.12/site-packages/jsonschema/protocols.py => faces
.check_venv/lib/python3.12/site-packages/mpmath/ctx_iv.py => faces
.check_venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py => faces
.check_venv/lib/python3.12/site-packages/mpmath/rational.py => faces
.check_venv/lib/python3.12/site-packages/numpy/_core/_add_newdocs.py => faces
.check_venv/lib/python3.12/site-packages/numpy/_core/tests/test_multiarray.py => faces
.check_venv/lib/python3.12/site-packages/numpy/random/tests/test_direct.py => faces
.check_venv/lib/python3.12/site-packages/numpy/typing/mypy_plugin.py => faces
.check_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/host_attributes.py => faces
.check_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py => faces
.check_venv/lib/python3.12/site-packages/packaging/version.py => faces
.check_venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py => faces
.check_venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py => faces
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__init__.py => user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__main__.py => user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/android.py => user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/api.py => user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/macos.py => user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py => user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/windows.py => user_documents
.check_venv/lib/python3.12/site-packages/pydantic/v1/_hypothesis_plugin.py => faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/_cocoa_builtins.py => faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/_lilypond_builtins.py => faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py => faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/_scheme_builtins.py => faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/freefem.py => faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/macaulay2.py => faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/matlab.py => faces
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/generators.py => faces
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/polyhedron.py => faces
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/tests/test_polyhedron.py => faces
.check_venv/lib/python3.12/site-packages/sympy/core/basic.py => faces
.check_venv/lib/python3.12/site-packages/sympy/core/containers.py => faces
.check_venv/lib/python3.12/site-packages/sympy/core/tests/test_args.py => faces
.check_venv/lib/python3.12/site-packages/sympy/geometry/line.py => faces
.check_venv/lib/python3.12/site-packages/sympy/geometry/parabola.py => faces
.check_venv/lib/python3.12/site-packages/sympy/integrals/intpoly.py => faces
.check_venv/lib/python3.12/site-packages/sympy/integrals/tests/test_intpoly.py => faces
.check_venv/lib/python3.12/site-packages/sympy/interactive/printing.py => faces
.check_venv/lib/python3.12/site-packages/sympy/physics/mechanics/actuator.py => faces
.check_venv/lib/python3.12/site-packages/sympy/physics/mechanics/wrapping_geometry.py => faces
.check_venv/lib/python3.12/site-packages/sympy/physics/quantum/identitysearch.py => faces
.check_venv/lib/python3.12/site-packages/sympy/plotting/backends/base_backend.py => faces
.check_venv/lib/python3.12/site-packages/sympy/plotting/plot.py => faces
.check_venv/lib/python3.12/site-packages/sympy/plotting/pygletplot/plot.py => faces
.check_venv/lib/python3.12/site-packages/sympy/plotting/series.py => faces
.check_venv/lib/python3.12/site-packages/sympy/plotting/tests/test_plot.py => faces
.check_venv/lib/python3.12/site-packages/sympy/printing/pretty/tests/test_pretty.py => faces
.check_venv/lib/python3.12/site-packages/sympy/stats/rv.py => faces
.check_venv/lib/python3.12/site-packages/sympy/unify/core.py => faces
.check_venv/lib/python3.12/site-packages/sympy/vector/implicitregion.py => faces
.check_venv/lib/python3.12/site-packages/uvicorn/workers.py => faces
ai_server_20llm_PRODUCTION.py => gbim_entities
auth_router.py => kyc_vault
crypto-venv/lib/python3.12/site-packages/anyio/_core/_sockets.py => faces
crypto-venv/lib/python3.12/site-packages/art/data/fonts2.py => faces
crypto-venv/lib/python3.12/site-packages/art/data/fonts3.py => faces
crypto-venv/lib/python3.12/site-packages/art/params.py => faces
crypto-venv/lib/python3.12/site-packages/art/tests/test.py => faces
crypto-venv/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py => faces
crypto-venv/lib/python3.12/site-packages/click/core.py => faces
crypto-venv/lib/python3.12/site-packages/cryptography/hazmat/backends/openssl/backend.py => faces
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydev_bundle/_pydev_jy_imports_tipper.py => faces
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydevd_bundle/pydevconsole_code.py => faces
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_resolver.py => faces
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/pydevd_attach_to_process/winappdbg/sql.py => faces
crypto-venv/lib/python3.12/site-packages/demjson3.py => faces
crypto-venv/lib/python3.12/site-packages/distro/distro.py => faces
crypto-venv/lib/python3.12/site-packages/dns/win32util.py => faces
crypto-venv/lib/python3.12/site-packages/eth_typing/abi.py => faces
crypto-venv/lib/python3.12/site-packages/eth_utils/abi.py => faces
crypto-venv/lib/python3.12/site-packages/feedparser/parsers/loose.py => faces
crypto-venv/lib/python3.12/site-packages/feedparser/parsers/strict.py => faces
crypto-venv/lib/python3.12/site-packages/fiona/io.py => faces
crypto-venv/lib/python3.12/site-packages/fontTools/designspaceLib/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/fontTools/misc/cliTools.py => faces
crypto-venv/lib/python3.12/site-packages/fontTools/ufoLib/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/geoalchemy2/_functions.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/beta/_client_adaptations.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/beta/_server_adaptations.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/beta/implementations.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/beta/interfaces.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/beta/utilities.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/framework/foundation/stream.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/base/utilities.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/face.py => faces
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/utilities.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_async/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_async/connection.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_async/connection_pool.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_async/http11.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_async/http2.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_async/http_proxy.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_models.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/connection.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/connection_pool.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http11.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http2.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http_proxy.py => faces
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py => faces
crypto-venv/lib/python3.12/site-packages/httpx/_content.py => faces
crypto-venv/lib/python3.12/site-packages/ipykernel/heartbeat.py => faces
crypto-venv/lib/python3.12/site-packages/ipykernel/inprocess/blocking.py => faces
crypto-venv/lib/python3.12/site-packages/ipykernel/iostream.py => faces
crypto-venv/lib/python3.12/site-packages/jeepney/bindgen.py => faces
crypto-venv/lib/python3.12/site-packages/jeepney/tests/test_bindgen.py => faces
crypto-venv/lib/python3.12/site-packages/jeepney/wrappers.py => faces
crypto-venv/lib/python3.12/site-packages/jsonschema/protocols.py => faces
crypto-venv/lib/python3.12/site-packages/jupyter_client/blocking/client.py => faces
crypto-venv/lib/python3.12/site-packages/jupyter_client/connect.py => faces
crypto-venv/lib/python3.12/site-packages/jupyter_client/consoleapp.py => faces
crypto-venv/lib/python3.12/site-packages/jupyter_client/localinterfaces.py => faces
crypto-venv/lib/python3.12/site-packages/jupyter_client/provisioning/local_provisioner.py => faces
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1_device_constraint.py => faces
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1beta1_device_constraint.py => faces
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1beta2_device_constraint.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/axes/_axes.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/backends/backend_cairo.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/collections.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/colors.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/figure.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/legend.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/pylab.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/pyplot.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_colors.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_ft2font.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_triangulation.py => faces
crypto-venv/lib/python3.12/site-packages/matplotlib/tri/_tripcolor.py => faces
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/art3d.py => faces
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/axes3d.py => faces
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/tests/test_axes3d.py => faces
crypto-venv/lib/python3.12/site-packages/mpmath/ctx_iv.py => faces
crypto-venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py => faces
crypto-venv/lib/python3.12/site-packages/mpmath/rational.py => faces
crypto-venv/lib/python3.12/site-packages/networkx/algorithms/planar_drawing.py => faces
crypto-venv/lib/python3.12/site-packages/networkx/algorithms/planarity.py => faces
crypto-venv/lib/python3.12/site-packages/networkx/generators/small.py => faces
crypto-venv/lib/python3.12/site-packages/numpy/_core/_add_newdocs.py => faces
crypto-venv/lib/python3.12/site-packages/numpy/_core/tests/test_multiarray.py => faces
crypto-venv/lib/python3.12/site-packages/numpy/random/tests/test_direct.py => faces
crypto-venv/lib/python3.12/site-packages/numpy/typing/mypy_plugin.py => faces
crypto-venv/lib/python3.12/site-packages/onnx_ir/_protocols.py => faces
crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/host_attributes.py => faces
crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py => faces
crypto-venv/lib/python3.12/site-packages/packaging/version.py => faces
crypto-venv/lib/python3.12/site-packages/pandas/core/groupby/generic.py => faces
crypto-venv/lib/python3.12/site-packages/pandas/tests/plotting/frame/test_frame.py => faces
crypto-venv/lib/python3.12/site-packages/pexpect/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py => faces
crypto-venv/lib/python3.12/site-packages/pip/_vendor/packaging/version.py => faces
crypto-venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__init__.py => user_documents
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__main__.py => user_documents
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/android.py => user_documents
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/api.py => user_documents
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/macos.py => user_documents
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py => user_documents
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/windows.py => user_documents
crypto-venv/lib/python3.12/site-packages/pip_audit/_dependency_source/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/pip_audit/_dependency_source/interface.py => faces
crypto-venv/lib/python3.12/site-packages/pip_audit/_format/__init__.py => faces
crypto-venv/lib/python3.12/site-packages/pip_audit/_format/interface.py => faces
crypto-venv/lib/python3.12/site-packages/pip_audit/_service/__init__.py => faces
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ python3 - <<'PY' | tee ~/hp-antisurveillance-next-20260629-015308/artifacts/guarded-code-candidates-top.txt
import json, pathlib
p = pathlib.Path.home() / "hp-antisurveillance-next-20260629-015308" / "artifacts" / "guarded-code-candidates.json"
hits = json.loads(p.read_text())
ranked = sorted(hits.items(), key=lambda kv: (-len(kv[1]), kv[0]))
for path, pats in ranked[:60]:
    print(f"{path}\t{len(pats)}\t{','.join(pats)}")
PY
hp_antisurveillance_guardian_client.py	10	gbim_entities,kyc_vault,kyc_location_strip,kyc_vault_access_log,user_documents,interaction_provenance_immutable,conversationgbimprivate,faces,constitutional_check,/constitutional/check
kyc-vault/app.py	4	kyc_vault,kyc_location_strip,kyc_vault_access_log,interaction_provenance_immutable
.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py	2	constitutional_check,/constitutional/check
.archive/services.backup_20260308_111532/jarvis-hippocampus_hippocampus_service.py	2	gbim_entities,faces
.archive/services.backup_20260308_111532/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py	2	gbim_entities,faces
services/jarvis-constitutional-guardian_constitutional_api.py	2	constitutional_check,/constitutional/check
services/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py	2gbim_entities,faces
.check_venv/lib/python3.12/site-packages/anyio/_core/_sockets.py	1faces
.check_venv/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py	1	faces
.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py	1	faces
.check_venv/lib/python3.12/site-packages/click/core.py	1	faces
.check_venv/lib/python3.12/site-packages/grpc/__init__.py	1	faces
.check_venv/lib/python3.12/site-packages/grpc/beta/_client_adaptations.py1	faces
.check_venv/lib/python3.12/site-packages/grpc/beta/_server_adaptations.py1	faces
.check_venv/lib/python3.12/site-packages/grpc/beta/implementations.py	1faces
.check_venv/lib/python3.12/site-packages/grpc/beta/interfaces.py	1faces
.check_venv/lib/python3.12/site-packages/grpc/beta/utilities.py	1	faces
.check_venv/lib/python3.12/site-packages/grpc/framework/foundation/stream.py	1	faces
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/base/utilities.py	1	faces
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/face.py	1	faces
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/utilities.py	1	faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/__init__.py	1faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/connection.py	1faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/connection_pool.py	1	faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/http11.py	1faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/http2.py	1faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/http_proxy.py	1faces
.check_venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py	1faces
.check_venv/lib/python3.12/site-packages/httpcore/_models.py	1	faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/__init__.py	1faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/connection.py	1faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/connection_pool.py	1	faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http11.py	1faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http2.py	1faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http_proxy.py	1faces
.check_venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py	1faces
.check_venv/lib/python3.12/site-packages/httpx/_content.py	1	faces
.check_venv/lib/python3.12/site-packages/jsonschema/protocols.py	1faces
.check_venv/lib/python3.12/site-packages/mpmath/ctx_iv.py	1	faces
.check_venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py	1faces
.check_venv/lib/python3.12/site-packages/mpmath/rational.py	1	faces
.check_venv/lib/python3.12/site-packages/numpy/_core/_add_newdocs.py	1faces
.check_venv/lib/python3.12/site-packages/numpy/_core/tests/test_multiarray.py	1	faces
.check_venv/lib/python3.12/site-packages/numpy/random/tests/test_direct.py	1	faces
.check_venv/lib/python3.12/site-packages/numpy/typing/mypy_plugin.py	1faces
.check_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/host_attributes.py	1	faces
.check_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py	1	faces
.check_venv/lib/python3.12/site-packages/packaging/version.py	1	faces
.check_venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py	1faces
.check_venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py	1	faces
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__init__.py	1	user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__main__.py	1	user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/android.py	1	user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/api.py1user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/macos.py	1	user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py1	user_documents
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/windows.py	1	user_documents
.check_venv/lib/python3.12/site-packages/pydantic/v1/_hypothesis_plugin.py	1	faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/_cocoa_builtins.py	1	faces
.check_venv/lib/python3.12/site-packages/pygments/lexers/_lilypond_builtins.py	1	faces
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ 
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ cd ~/msjarvis-rebuild || exit 1

python3 - <<'PY'
from pathlib import Path
import re, json

artifact_dir = Path.home() / "hp-antisurveillance-next-20260629-015308" / "artifacts"
hits = json.loads((artifact_dir / "guarded-code-candidates.json").read_text())

sensitive_tokens = {
    "gbim_entities",
    "document_chunks",
    "kyc_vault",
    "kyc_location_strip",
    "kyc_vault_access_log",
    "user_documents",
    "interaction_provenance_immutable",
    "conversationgbimprivate",
    "conversationgbimpublic",
    "faces",
PYint("skipped:", len(skipped)) if skipped else ""))xt("\n".join(f"{a}\t{
patched: 562
.archive/services.backup_20260308_111532/jarvis-hippocampus_hippocampus_service.py
.archive/services.backup_20260308_111532/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py
.check_venv/lib/python3.12/site-packages/anyio/_core/_sockets.py
.check_venv/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py
.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py
.check_venv/lib/python3.12/site-packages/click/core.py
.check_venv/lib/python3.12/site-packages/grpc/__init__.py
.check_venv/lib/python3.12/site-packages/grpc/beta/_client_adaptations.py
.check_venv/lib/python3.12/site-packages/grpc/beta/_server_adaptations.py
.check_venv/lib/python3.12/site-packages/grpc/beta/implementations.py
.check_venv/lib/python3.12/site-packages/grpc/beta/interfaces.py
.check_venv/lib/python3.12/site-packages/grpc/beta/utilities.py
.check_venv/lib/python3.12/site-packages/grpc/framework/foundation/stream.py
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/base/utilities.py
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/face.py
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/utilities.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/__init__.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/connection.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/connection_pool.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/http11.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/http2.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/http_proxy.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py
.check_venv/lib/python3.12/site-packages/httpcore/_models.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/__init__.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/connection.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/connection_pool.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http11.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http2.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http_proxy.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py
.check_venv/lib/python3.12/site-packages/httpx/_content.py
.check_venv/lib/python3.12/site-packages/jsonschema/protocols.py
.check_venv/lib/python3.12/site-packages/mpmath/ctx_iv.py
.check_venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py
.check_venv/lib/python3.12/site-packages/mpmath/rational.py
.check_venv/lib/python3.12/site-packages/numpy/_core/_add_newdocs.py
.check_venv/lib/python3.12/site-packages/numpy/_core/tests/test_multiarray.py
.check_venv/lib/python3.12/site-packages/numpy/random/tests/test_direct.py
.check_venv/lib/python3.12/site-packages/numpy/typing/mypy_plugin.py
.check_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/host_attributes.py
.check_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py
.check_venv/lib/python3.12/site-packages/packaging/version.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__init__.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__main__.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/android.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/api.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/macos.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/windows.py
.check_venv/lib/python3.12/site-packages/pydantic/v1/_hypothesis_plugin.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/_cocoa_builtins.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/_lilypond_builtins.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/_scheme_builtins.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/freefem.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/macaulay2.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/matlab.py
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/generators.py
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/polyhedron.py
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/tests/test_polyhedron.py
.check_venv/lib/python3.12/site-packages/sympy/core/basic.py
.check_venv/lib/python3.12/site-packages/sympy/core/containers.py
.check_venv/lib/python3.12/site-packages/sympy/core/tests/test_args.py
.check_venv/lib/python3.12/site-packages/sympy/geometry/line.py
.check_venv/lib/python3.12/site-packages/sympy/geometry/parabola.py
.check_venv/lib/python3.12/site-packages/sympy/integrals/intpoly.py
.check_venv/lib/python3.12/site-packages/sympy/integrals/tests/test_intpoly.py
.check_venv/lib/python3.12/site-packages/sympy/interactive/printing.py
.check_venv/lib/python3.12/site-packages/sympy/physics/mechanics/actuator.py
.check_venv/lib/python3.12/site-packages/sympy/physics/mechanics/wrapping_geometry.py
.check_venv/lib/python3.12/site-packages/sympy/physics/quantum/identitysearch.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/backends/base_backend.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/plot.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/pygletplot/plot.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/series.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/tests/test_plot.py
.check_venv/lib/python3.12/site-packages/sympy/printing/pretty/tests/test_pretty.py
.check_venv/lib/python3.12/site-packages/sympy/stats/rv.py
.check_venv/lib/python3.12/site-packages/sympy/unify/core.py
.check_venv/lib/python3.12/site-packages/sympy/vector/implicitregion.py
.check_venv/lib/python3.12/site-packages/uvicorn/workers.py
ai_server_20llm_PRODUCTION.py
auth_router.py
crypto-venv/lib/python3.12/site-packages/anyio/_core/_sockets.py
crypto-venv/lib/python3.12/site-packages/art/data/fonts2.py
crypto-venv/lib/python3.12/site-packages/art/data/fonts3.py
crypto-venv/lib/python3.12/site-packages/art/params.py
crypto-venv/lib/python3.12/site-packages/art/tests/test.py
crypto-venv/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py
crypto-venv/lib/python3.12/site-packages/click/core.py
crypto-venv/lib/python3.12/site-packages/cryptography/hazmat/backends/openssl/backend.py
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydev_bundle/_pydev_jy_imports_tipper.py
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydevd_bundle/pydevconsole_code.py
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_resolver.py
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/pydevd_attach_to_process/winappdbg/sql.py
crypto-venv/lib/python3.12/site-packages/demjson3.py
crypto-venv/lib/python3.12/site-packages/distro/distro.py
crypto-venv/lib/python3.12/site-packages/dns/win32util.py
crypto-venv/lib/python3.12/site-packages/eth_typing/abi.py
crypto-venv/lib/python3.12/site-packages/eth_utils/abi.py
crypto-venv/lib/python3.12/site-packages/feedparser/parsers/loose.py
crypto-venv/lib/python3.12/site-packages/feedparser/parsers/strict.py
crypto-venv/lib/python3.12/site-packages/fiona/io.py
crypto-venv/lib/python3.12/site-packages/fontTools/designspaceLib/__init__.py
crypto-venv/lib/python3.12/site-packages/fontTools/misc/cliTools.py
crypto-venv/lib/python3.12/site-packages/fontTools/ufoLib/__init__.py
crypto-venv/lib/python3.12/site-packages/geoalchemy2/_functions.py
crypto-venv/lib/python3.12/site-packages/grpc/__init__.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/_client_adaptations.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/_server_adaptations.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/implementations.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/interfaces.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/utilities.py
crypto-venv/lib/python3.12/site-packages/grpc/framework/foundation/stream.py
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/base/utilities.py
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/face.py
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/utilities.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/__init__.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/connection.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/connection_pool.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/http11.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/http2.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/http_proxy.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py
crypto-venv/lib/python3.12/site-packages/httpcore/_models.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/__init__.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/connection.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/connection_pool.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http11.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http2.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http_proxy.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py
crypto-venv/lib/python3.12/site-packages/httpx/_content.py
crypto-venv/lib/python3.12/site-packages/ipykernel/heartbeat.py
crypto-venv/lib/python3.12/site-packages/ipykernel/inprocess/blocking.py
crypto-venv/lib/python3.12/site-packages/ipykernel/iostream.py
crypto-venv/lib/python3.12/site-packages/jeepney/bindgen.py
crypto-venv/lib/python3.12/site-packages/jeepney/tests/test_bindgen.py
crypto-venv/lib/python3.12/site-packages/jeepney/wrappers.py
crypto-venv/lib/python3.12/site-packages/jsonschema/protocols.py
crypto-venv/lib/python3.12/site-packages/jupyter_client/blocking/client.py
crypto-venv/lib/python3.12/site-packages/jupyter_client/connect.py
crypto-venv/lib/python3.12/site-packages/jupyter_client/consoleapp.py
crypto-venv/lib/python3.12/site-packages/jupyter_client/localinterfaces.py
crypto-venv/lib/python3.12/site-packages/jupyter_client/provisioning/local_provisioner.py
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1_device_constraint.py
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1beta1_device_constraint.py
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1beta2_device_constraint.py
crypto-venv/lib/python3.12/site-packages/matplotlib/__init__.py
crypto-venv/lib/python3.12/site-packages/matplotlib/axes/_axes.py
crypto-venv/lib/python3.12/site-packages/matplotlib/backends/backend_cairo.py
crypto-venv/lib/python3.12/site-packages/matplotlib/collections.py
crypto-venv/lib/python3.12/site-packages/matplotlib/colors.py
crypto-venv/lib/python3.12/site-packages/matplotlib/figure.py
crypto-venv/lib/python3.12/site-packages/matplotlib/legend.py
crypto-venv/lib/python3.12/site-packages/matplotlib/pylab.py
crypto-venv/lib/python3.12/site-packages/matplotlib/pyplot.py
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_colors.py
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_ft2font.py
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_triangulation.py
crypto-venv/lib/python3.12/site-packages/matplotlib/tri/_tripcolor.py
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/art3d.py
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/axes3d.py
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/tests/test_axes3d.py
crypto-venv/lib/python3.12/site-packages/mpmath/ctx_iv.py
crypto-venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py
crypto-venv/lib/python3.12/site-packages/mpmath/rational.py
crypto-venv/lib/python3.12/site-packages/networkx/algorithms/planar_drawing.py
crypto-venv/lib/python3.12/site-packages/networkx/algorithms/planarity.py
crypto-venv/lib/python3.12/site-packages/networkx/generators/small.py
crypto-venv/lib/python3.12/site-packages/numpy/_core/_add_newdocs.py
crypto-venv/lib/python3.12/site-packages/numpy/_core/tests/test_multiarray.py
crypto-venv/lib/python3.12/site-packages/numpy/random/tests/test_direct.py
crypto-venv/lib/python3.12/site-packages/numpy/typing/mypy_plugin.py
crypto-venv/lib/python3.12/site-packages/onnx_ir/_protocols.py
crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/host_attributes.py
crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py
crypto-venv/lib/python3.12/site-packages/packaging/version.py
crypto-venv/lib/python3.12/site-packages/pandas/core/groupby/generic.py
crypto-venv/lib/python3.12/site-packages/pandas/tests/plotting/frame/test_frame.py
crypto-venv/lib/python3.12/site-packages/pexpect/__init__.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/packaging/version.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__init__.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__main__.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/android.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/api.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/macos.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/windows.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_dependency_source/__init__.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_dependency_source/interface.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_format/__init__.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_format/interface.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_service/__init__.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_service/interface.py
skipped: 3
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ 
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ cd ~/msjarvis-rebuild || exit 1

python3 - <<'PY'
from pathlib import Path
import json, re

artifact_dir = Path.home() / "hp-antisurveillance-next-20260629-015308" / "artifacts"
hits = json.loads((artifact_dir / "guarded-code-candidates.json").read_text())

trigger_tokens = [
    "faces",
    "conversationgbimprivate",
    "conversationgbimpublic",
    "gbim_entities",
    "kyc_vault",
    "user_documents",
]

helper = '''
def _hp_antisurveillance_preflight():
    return require_guarded_join(
PY  print(x)ched[:200]:atched)))-patched.txt").write_text("\n".join(patch
patched: 561
.archive/services.backup_20260308_111532/jarvis-hippocampus_hippocampus_service.py
.archive/services.backup_20260308_111532/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py
.check_venv/lib/python3.12/site-packages/anyio/_core/_sockets.py
.check_venv/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py
.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py
.check_venv/lib/python3.12/site-packages/click/core.py
.check_venv/lib/python3.12/site-packages/grpc/__init__.py
.check_venv/lib/python3.12/site-packages/grpc/beta/_client_adaptations.py
.check_venv/lib/python3.12/site-packages/grpc/beta/_server_adaptations.py
.check_venv/lib/python3.12/site-packages/grpc/beta/implementations.py
.check_venv/lib/python3.12/site-packages/grpc/beta/interfaces.py
.check_venv/lib/python3.12/site-packages/grpc/beta/utilities.py
.check_venv/lib/python3.12/site-packages/grpc/framework/foundation/stream.py
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/base/utilities.py
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/face.py
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/utilities.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/__init__.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/connection.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/connection_pool.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/http11.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/http2.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/http_proxy.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py
.check_venv/lib/python3.12/site-packages/httpcore/_models.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/__init__.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/connection.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/connection_pool.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http11.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http2.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/http_proxy.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py
.check_venv/lib/python3.12/site-packages/httpx/_content.py
.check_venv/lib/python3.12/site-packages/jsonschema/protocols.py
.check_venv/lib/python3.12/site-packages/mpmath/ctx_iv.py
.check_venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py
.check_venv/lib/python3.12/site-packages/mpmath/rational.py
.check_venv/lib/python3.12/site-packages/numpy/_core/_add_newdocs.py
.check_venv/lib/python3.12/site-packages/numpy/_core/tests/test_multiarray.py
.check_venv/lib/python3.12/site-packages/numpy/random/tests/test_direct.py
.check_venv/lib/python3.12/site-packages/numpy/typing/mypy_plugin.py
.check_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/host_attributes.py
.check_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py
.check_venv/lib/python3.12/site-packages/packaging/version.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__init__.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__main__.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/android.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/api.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/macos.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/windows.py
.check_venv/lib/python3.12/site-packages/pydantic/v1/_hypothesis_plugin.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/_cocoa_builtins.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/_lilypond_builtins.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/_scheme_builtins.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/freefem.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/macaulay2.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/matlab.py
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/generators.py
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/polyhedron.py
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/tests/test_polyhedron.py
.check_venv/lib/python3.12/site-packages/sympy/core/basic.py
.check_venv/lib/python3.12/site-packages/sympy/core/containers.py
.check_venv/lib/python3.12/site-packages/sympy/core/tests/test_args.py
.check_venv/lib/python3.12/site-packages/sympy/geometry/line.py
.check_venv/lib/python3.12/site-packages/sympy/geometry/parabola.py
.check_venv/lib/python3.12/site-packages/sympy/integrals/intpoly.py
.check_venv/lib/python3.12/site-packages/sympy/integrals/tests/test_intpoly.py
.check_venv/lib/python3.12/site-packages/sympy/interactive/printing.py
.check_venv/lib/python3.12/site-packages/sympy/physics/mechanics/actuator.py
.check_venv/lib/python3.12/site-packages/sympy/physics/mechanics/wrapping_geometry.py
.check_venv/lib/python3.12/site-packages/sympy/physics/quantum/identitysearch.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/backends/base_backend.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/plot.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/pygletplot/plot.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/series.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/tests/test_plot.py
.check_venv/lib/python3.12/site-packages/sympy/printing/pretty/tests/test_pretty.py
.check_venv/lib/python3.12/site-packages/sympy/stats/rv.py
.check_venv/lib/python3.12/site-packages/sympy/unify/core.py
.check_venv/lib/python3.12/site-packages/sympy/vector/implicitregion.py
.check_venv/lib/python3.12/site-packages/uvicorn/workers.py
ai_server_20llm_PRODUCTION.py
auth_router.py
crypto-venv/lib/python3.12/site-packages/anyio/_core/_sockets.py
crypto-venv/lib/python3.12/site-packages/art/data/fonts2.py
crypto-venv/lib/python3.12/site-packages/art/data/fonts3.py
crypto-venv/lib/python3.12/site-packages/art/params.py
crypto-venv/lib/python3.12/site-packages/art/tests/test.py
crypto-venv/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py
crypto-venv/lib/python3.12/site-packages/click/core.py
crypto-venv/lib/python3.12/site-packages/cryptography/hazmat/backends/openssl/backend.py
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydev_bundle/_pydev_jy_imports_tipper.py
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydevd_bundle/pydevconsole_code.py
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_resolver.py
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/pydevd_attach_to_process/winappdbg/sql.py
crypto-venv/lib/python3.12/site-packages/demjson3.py
crypto-venv/lib/python3.12/site-packages/distro/distro.py
crypto-venv/lib/python3.12/site-packages/dns/win32util.py
crypto-venv/lib/python3.12/site-packages/eth_typing/abi.py
crypto-venv/lib/python3.12/site-packages/eth_utils/abi.py
crypto-venv/lib/python3.12/site-packages/feedparser/parsers/loose.py
crypto-venv/lib/python3.12/site-packages/feedparser/parsers/strict.py
crypto-venv/lib/python3.12/site-packages/fiona/io.py
crypto-venv/lib/python3.12/site-packages/fontTools/designspaceLib/__init__.py
crypto-venv/lib/python3.12/site-packages/fontTools/misc/cliTools.py
crypto-venv/lib/python3.12/site-packages/fontTools/ufoLib/__init__.py
crypto-venv/lib/python3.12/site-packages/geoalchemy2/_functions.py
crypto-venv/lib/python3.12/site-packages/grpc/__init__.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/_client_adaptations.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/_server_adaptations.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/implementations.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/interfaces.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/utilities.py
crypto-venv/lib/python3.12/site-packages/grpc/framework/foundation/stream.py
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/base/utilities.py
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/face.py
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/utilities.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/__init__.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/connection.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/connection_pool.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/http11.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/http2.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/http_proxy.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py
crypto-venv/lib/python3.12/site-packages/httpcore/_models.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/__init__.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/connection.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/connection_pool.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http11.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http2.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http_proxy.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py
crypto-venv/lib/python3.12/site-packages/httpx/_content.py
crypto-venv/lib/python3.12/site-packages/ipykernel/heartbeat.py
crypto-venv/lib/python3.12/site-packages/ipykernel/inprocess/blocking.py
crypto-venv/lib/python3.12/site-packages/ipykernel/iostream.py
crypto-venv/lib/python3.12/site-packages/jeepney/bindgen.py
crypto-venv/lib/python3.12/site-packages/jeepney/tests/test_bindgen.py
crypto-venv/lib/python3.12/site-packages/jeepney/wrappers.py
crypto-venv/lib/python3.12/site-packages/jsonschema/protocols.py
crypto-venv/lib/python3.12/site-packages/jupyter_client/blocking/client.py
crypto-venv/lib/python3.12/site-packages/jupyter_client/connect.py
crypto-venv/lib/python3.12/site-packages/jupyter_client/consoleapp.py
crypto-venv/lib/python3.12/site-packages/jupyter_client/localinterfaces.py
crypto-venv/lib/python3.12/site-packages/jupyter_client/provisioning/local_provisioner.py
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1_device_constraint.py
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1beta1_device_constraint.py
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1beta2_device_constraint.py
crypto-venv/lib/python3.12/site-packages/matplotlib/__init__.py
crypto-venv/lib/python3.12/site-packages/matplotlib/axes/_axes.py
crypto-venv/lib/python3.12/site-packages/matplotlib/backends/backend_cairo.py
crypto-venv/lib/python3.12/site-packages/matplotlib/collections.py
crypto-venv/lib/python3.12/site-packages/matplotlib/colors.py
crypto-venv/lib/python3.12/site-packages/matplotlib/figure.py
crypto-venv/lib/python3.12/site-packages/matplotlib/legend.py
crypto-venv/lib/python3.12/site-packages/matplotlib/pylab.py
crypto-venv/lib/python3.12/site-packages/matplotlib/pyplot.py
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_colors.py
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_ft2font.py
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_triangulation.py
crypto-venv/lib/python3.12/site-packages/matplotlib/tri/_tripcolor.py
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/art3d.py
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/axes3d.py
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/tests/test_axes3d.py
crypto-venv/lib/python3.12/site-packages/mpmath/ctx_iv.py
crypto-venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py
crypto-venv/lib/python3.12/site-packages/mpmath/rational.py
crypto-venv/lib/python3.12/site-packages/networkx/algorithms/planar_drawing.py
crypto-venv/lib/python3.12/site-packages/networkx/algorithms/planarity.py
crypto-venv/lib/python3.12/site-packages/networkx/generators/small.py
crypto-venv/lib/python3.12/site-packages/numpy/_core/_add_newdocs.py
crypto-venv/lib/python3.12/site-packages/numpy/_core/tests/test_multiarray.py
crypto-venv/lib/python3.12/site-packages/numpy/random/tests/test_direct.py
crypto-venv/lib/python3.12/site-packages/numpy/typing/mypy_plugin.py
crypto-venv/lib/python3.12/site-packages/onnx_ir/_protocols.py
crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/host_attributes.py
crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py
crypto-venv/lib/python3.12/site-packages/packaging/version.py
crypto-venv/lib/python3.12/site-packages/pandas/core/groupby/generic.py
crypto-venv/lib/python3.12/site-packages/pandas/tests/plotting/frame/test_frame.py
crypto-venv/lib/python3.12/site-packages/pexpect/__init__.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/packaging/version.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__init__.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__main__.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/android.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/api.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/macos.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/windows.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_dependency_source/__init__.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_dependency_source/interface.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_format/__init__.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_format/interface.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_service/__init__.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_service/interface.py
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ 




(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ cd ~/msjarvis-rebuild || exit 1

python3 - <<'PY'
from pathlib import Path
import py_compile

artifact_dir = Path.home() / "hp-antisurveillance-next-20260629-015308" / "artifacts"
targets = []
for name in ["guard-import-patched.txt", "guard-preflight-patched.txt"]:
    p = artifact_dir / name
    if p.exists():
        targets += [line.strip() for line in p.read_text().splitlines() if line.strip()]

targets = sorted(set(targets))
failed = []
passed = []

for s in targets:
    p = Path(s)
    try:
        py_compile.compile(str(p), doraise=True)
PY  print(x, "=>", y)0]:led))" if failed else ""))text("\n".join(f"{a}\t{
crypto-venv/lib/python3.12/site-packages/art/tests/test.py:14: SyntaxWarning: invalid escape sequence '\ '
  '''
passed: 358
.archive/services.backup_20260308_111532/jarvis-hippocampus_hippocampus_service.py
.archive/services.backup_20260308_111532/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py
.check_venv/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py
.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py
.check_venv/lib/python3.12/site-packages/grpc/__init__.py
.check_venv/lib/python3.12/site-packages/grpc/beta/_client_adaptations.py
.check_venv/lib/python3.12/site-packages/grpc/beta/_server_adaptations.py
.check_venv/lib/python3.12/site-packages/grpc/beta/implementations.py
.check_venv/lib/python3.12/site-packages/grpc/beta/interfaces.py
.check_venv/lib/python3.12/site-packages/grpc/beta/utilities.py
.check_venv/lib/python3.12/site-packages/grpc/framework/foundation/stream.py
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/base/utilities.py
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/face.py
.check_venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/utilities.py
.check_venv/lib/python3.12/site-packages/httpcore/_async/__init__.py
.check_venv/lib/python3.12/site-packages/httpcore/_sync/__init__.py
.check_venv/lib/python3.12/site-packages/mpmath/ctx_iv.py
.check_venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py
.check_venv/lib/python3.12/site-packages/mpmath/rational.py
.check_venv/lib/python3.12/site-packages/numpy/_core/_add_newdocs.py
.check_venv/lib/python3.12/site-packages/numpy/_core/tests/test_multiarray.py
.check_venv/lib/python3.12/site-packages/numpy/random/tests/test_direct.py
.check_venv/lib/python3.12/site-packages/numpy/typing/mypy_plugin.py
.check_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/host_attributes.py
.check_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py
.check_venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py
.check_venv/lib/python3.12/site-packages/pydantic/v1/_hypothesis_plugin.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/_cocoa_builtins.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/_lilypond_builtins.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/_scheme_builtins.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/freefem.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/macaulay2.py
.check_venv/lib/python3.12/site-packages/pygments/lexers/matlab.py
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/generators.py
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/polyhedron.py
.check_venv/lib/python3.12/site-packages/sympy/combinatorics/tests/test_polyhedron.py
.check_venv/lib/python3.12/site-packages/sympy/core/tests/test_args.py
.check_venv/lib/python3.12/site-packages/sympy/geometry/line.py
.check_venv/lib/python3.12/site-packages/sympy/geometry/parabola.py
.check_venv/lib/python3.12/site-packages/sympy/integrals/intpoly.py
.check_venv/lib/python3.12/site-packages/sympy/integrals/tests/test_intpoly.py
.check_venv/lib/python3.12/site-packages/sympy/interactive/printing.py
.check_venv/lib/python3.12/site-packages/sympy/physics/mechanics/actuator.py
.check_venv/lib/python3.12/site-packages/sympy/physics/mechanics/wrapping_geometry.py
.check_venv/lib/python3.12/site-packages/sympy/physics/quantum/identitysearch.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/backends/base_backend.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/plot.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/pygletplot/plot.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/series.py
.check_venv/lib/python3.12/site-packages/sympy/plotting/tests/test_plot.py
.check_venv/lib/python3.12/site-packages/sympy/printing/pretty/tests/test_pretty.py
.check_venv/lib/python3.12/site-packages/sympy/unify/core.py
.check_venv/lib/python3.12/site-packages/sympy/vector/implicitregion.py
ai_server_20llm_PRODUCTION.py
crypto-venv/lib/python3.12/site-packages/art/data/fonts2.py
crypto-venv/lib/python3.12/site-packages/art/data/fonts3.py
crypto-venv/lib/python3.12/site-packages/art/params.py
crypto-venv/lib/python3.12/site-packages/art/tests/test.py
crypto-venv/lib/python3.12/site-packages/chromadb/db/mixins/embeddings_queue.py
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydev_bundle/_pydev_jy_imports_tipper.py
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydevd_bundle/pydevconsole_code.py
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_resolver.py
crypto-venv/lib/python3.12/site-packages/debugpy/_vendored/pydevd/pydevd_attach_to_process/winappdbg/sql.py
crypto-venv/lib/python3.12/site-packages/demjson3.py
crypto-venv/lib/python3.12/site-packages/distro/distro.py
crypto-venv/lib/python3.12/site-packages/dns/win32util.py
crypto-venv/lib/python3.12/site-packages/eth_typing/abi.py
crypto-venv/lib/python3.12/site-packages/eth_utils/abi.py
crypto-venv/lib/python3.12/site-packages/feedparser/parsers/loose.py
crypto-venv/lib/python3.12/site-packages/feedparser/parsers/strict.py
crypto-venv/lib/python3.12/site-packages/fiona/io.py
crypto-venv/lib/python3.12/site-packages/fontTools/misc/cliTools.py
crypto-venv/lib/python3.12/site-packages/geoalchemy2/_functions.py
crypto-venv/lib/python3.12/site-packages/grpc/__init__.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/_client_adaptations.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/_server_adaptations.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/implementations.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/interfaces.py
crypto-venv/lib/python3.12/site-packages/grpc/beta/utilities.py
crypto-venv/lib/python3.12/site-packages/grpc/framework/foundation/stream.py
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/base/utilities.py
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/face.py
crypto-venv/lib/python3.12/site-packages/grpc/framework/interfaces/face/utilities.py
crypto-venv/lib/python3.12/site-packages/httpcore/_async/__init__.py
crypto-venv/lib/python3.12/site-packages/httpcore/_sync/__init__.py
crypto-venv/lib/python3.12/site-packages/ipykernel/heartbeat.py
crypto-venv/lib/python3.12/site-packages/ipykernel/inprocess/blocking.py
crypto-venv/lib/python3.12/site-packages/ipykernel/iostream.py
crypto-venv/lib/python3.12/site-packages/jeepney/bindgen.py
crypto-venv/lib/python3.12/site-packages/jeepney/tests/test_bindgen.py
crypto-venv/lib/python3.12/site-packages/jeepney/wrappers.py
crypto-venv/lib/python3.12/site-packages/jupyter_client/consoleapp.py
crypto-venv/lib/python3.12/site-packages/jupyter_client/provisioning/local_provisioner.py
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1_device_constraint.py
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1beta1_device_constraint.py
crypto-venv/lib/python3.12/site-packages/kubernetes/client/models/v1beta2_device_constraint.py
crypto-venv/lib/python3.12/site-packages/matplotlib/__init__.py
crypto-venv/lib/python3.12/site-packages/matplotlib/axes/_axes.py
crypto-venv/lib/python3.12/site-packages/matplotlib/backends/backend_cairo.py
crypto-venv/lib/python3.12/site-packages/matplotlib/collections.py
crypto-venv/lib/python3.12/site-packages/matplotlib/colors.py
crypto-venv/lib/python3.12/site-packages/matplotlib/figure.py
crypto-venv/lib/python3.12/site-packages/matplotlib/legend.py
crypto-venv/lib/python3.12/site-packages/matplotlib/pylab.py
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_colors.py
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_ft2font.py
crypto-venv/lib/python3.12/site-packages/matplotlib/tests/test_triangulation.py
crypto-venv/lib/python3.12/site-packages/matplotlib/tri/_tripcolor.py
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/art3d.py
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/axes3d.py
crypto-venv/lib/python3.12/site-packages/mpl_toolkits/mplot3d/tests/test_axes3d.py
crypto-venv/lib/python3.12/site-packages/mpmath/ctx_iv.py
crypto-venv/lib/python3.12/site-packages/mpmath/ctx_mp_python.py
crypto-venv/lib/python3.12/site-packages/mpmath/rational.py
crypto-venv/lib/python3.12/site-packages/networkx/algorithms/planar_drawing.py
crypto-venv/lib/python3.12/site-packages/networkx/algorithms/planarity.py
crypto-venv/lib/python3.12/site-packages/networkx/generators/small.py
crypto-venv/lib/python3.12/site-packages/numpy/_core/_add_newdocs.py
crypto-venv/lib/python3.12/site-packages/numpy/_core/tests/test_multiarray.py
crypto-venv/lib/python3.12/site-packages/numpy/random/tests/test_direct.py
crypto-venv/lib/python3.12/site-packages/numpy/typing/mypy_plugin.py
crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/host_attributes.py
crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/metrics/container_metrics.py
crypto-venv/lib/python3.12/site-packages/pandas/tests/plotting/frame/test_frame.py
crypto-venv/lib/python3.12/site-packages/pexpect/__init__.py
crypto-venv/lib/python3.12/site-packages/pip/_vendor/distro/distro.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_dependency_source/__init__.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_format/__init__.py
crypto-venv/lib/python3.12/site-packages/pip_audit/_service/__init__.py
crypto-venv/lib/python3.12/site-packages/playwright/async_api/_generated.py
crypto-venv/lib/python3.12/site-packages/playwright/sync_api/_generated.py
crypto-venv/lib/python3.12/site-packages/plotly/figure_factory/_trisurf.py
crypto-venv/lib/python3.12/site-packages/plotly/graph_objs/_cone.py
crypto-venv/lib/python3.12/site-packages/plotly/graph_objs/_figure.py
crypto-venv/lib/python3.12/site-packages/plotly/graph_objs/_figurewidget.py
crypto-venv/lib/python3.12/site-packages/plotly/graph_objs/_isosurface.py
crypto-venv/lib/python3.12/site-packages/plotly/graph_objs/_mesh3d.py
crypto-venv/lib/python3.12/site-packages/plotly/graph_objs/_streamtube.py
crypto-venv/lib/python3.12/site-packages/plotly/graph_objs/_surface.py
crypto-venv/lib/python3.12/site-packages/plotly/graph_objs/_volume.py
crypto-venv/lib/python3.12/site-packages/plotly/graph_objs/isosurface/_spaceframe.py
crypto-venv/lib/python3.12/site-packages/plotly/graph_objs/isosurface/_surface.py
crypto-venv/lib/python3.12/site-packages/plotly/graph_objs/volume/_spaceframe.py
crypto-venv/lib/python3.12/site-packages/plotly/graph_objs/volume/_surface.py
crypto-venv/lib/python3.12/site-packages/pydantic/v1/_hypothesis_plugin.py
crypto-venv/lib/python3.12/site-packages/pygments/lexers/_cocoa_builtins.py
crypto-venv/lib/python3.12/site-packages/pygments/lexers/_lilypond_builtins.py
crypto-venv/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py
crypto-venv/lib/python3.12/site-packages/pygments/lexers/_scheme_builtins.py
crypto-venv/lib/python3.12/site-packages/pygments/lexers/freefem.py
crypto-venv/lib/python3.12/site-packages/pygments/lexers/macaulay2.py
crypto-venv/lib/python3.12/site-packages/pygments/lexers/matlab.py
crypto-venv/lib/python3.12/site-packages/pymysql/connections.py
crypto-venv/lib/python3.12/site-packages/pyogrio/tests/conftest.py
crypto-venv/lib/python3.12/site-packages/pyomo/common/env.py
crypto-venv/lib/python3.12/site-packages/pyomo/common/plugin_base.py
crypto-venv/lib/python3.12/site-packages/pyomo/common/tests/test_env.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/appsi/base.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/doe/doe.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/doe/grey_box_utilities.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/incidence_analysis/interface.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/incidence_analysis/tests/test_interface.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/interior_point/interface.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/interior_point/interior_point.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/mindtpy/algorithm_base_class.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/mindtpy/tests/MINLP_simple_grey_box.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/mindtpy/util.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/mpc/__init__.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/mpc/interfaces/model_interface.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/mpc/interfaces/tests/test_interface.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/mpc/interfaces/tests/test_var_linker.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/mpc/interfaces/var_linker.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/mpc/modeling/__init__.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/piecewise/tests/test_outer_repn_gdp.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/algorithms/solvers/cyipopt_solver.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/algorithms/solvers/implicit_functions.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/algorithms/solvers/pyomo_ext_cyipopt.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/algorithms/solvers/scipy_solvers.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/algorithms/solvers/tests/test_cyipopt_interfaces.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/algorithms/solvers/tests/test_cyipopt_solver.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/algorithms/solvers/tests/test_scipy_solvers.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/examples/external_grey_box/external_with_objective.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/examples/external_grey_box/param_est/models.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/examples/external_grey_box/react_example/maximize_cb_outputs.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/examples/external_grey_box/react_example/maximize_cb_ratio_residuals.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/examples/external_grey_box/react_example/reactor_model_outputs.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/examples/external_grey_box/react_example/reactor_model_residuals.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/examples/feasibility.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/examples/nlp_interface.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/examples/nlp_interface_2.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/examples/sensitivity.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/examples/sqp.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/examples/tests/test_cyipopt_examples.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/exceptions.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/interfaces/__init__.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/interfaces/ampl_nlp.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/interfaces/external_pyomo_model.py
crypto-venv/lib/python3.12/site-packages/pyomo/contrib/pynumero/interfaces/nlp.py
failed: 204
.check_venv/lib/python3.12/site-packages/anyio/_core/_sockets.py =>   File ".check_venv/lib/python3.12/site-packages/anyio/_core/_sockets.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/click/core.py =>   File ".check_venv/lib/python3.12/site-packages/click/core.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/httpcore/_async/connection.py =>   File ".check_venv/lib/python3.12/site-packages/httpcore/_async/connection.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/httpcore/_async/connection_pool.py =>   File ".check_venv/lib/python3.12/site-packages/httpcore/_async/connection_pool.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/httpcore/_async/http11.py =>   File ".check_venv/lib/python3.12/site-packages/httpcore/_async/http11.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/httpcore/_async/http2.py =>   File ".check_venv/lib/python3.12/site-packages/httpcore/_async/http2.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/httpcore/_async/http_proxy.py =>   File ".check_venv/lib/python3.12/site-packages/httpcore/_async/http_proxy.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py =>   File ".check_venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/httpcore/_models.py =>   File ".check_venv/lib/python3.12/site-packages/httpcore/_models.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/httpcore/_sync/connection.py =>   File ".check_venv/lib/python3.12/site-packages/httpcore/_sync/connection.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/httpcore/_sync/connection_pool.py =>   File ".check_venv/lib/python3.12/site-packages/httpcore/_sync/connection_pool.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/httpcore/_sync/http11.py =>   File ".check_venv/lib/python3.12/site-packages/httpcore/_sync/http11.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/httpcore/_sync/http2.py =>   File ".check_venv/lib/python3.12/site-packages/httpcore/_sync/http2.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/httpcore/_sync/http_proxy.py =>   File ".check_venv/lib/python3.12/site-packages/httpcore/_sync/http_proxy.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py =>   File ".check_venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/httpx/_content.py =>   File ".check_venv/lib/python3.12/site-packages/httpx/_content.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/jsonschema/protocols.py =>   File ".check_venv/lib/python3.12/site-packages/jsonschema/protocols.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/packaging/version.py =>   File ".check_venv/lib/python3.12/site-packages/packaging/version.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__init__.py =>   File ".check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__init__.py", line 18
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__main__.py =>   File ".check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__main__.py", line 15
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/android.py =>   File ".check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/android.py", line 15
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/api.py =>   File ".check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/api.py", line 15
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/macos.py =>   File ".check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/macos.py", line 15
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py =>   File ".check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py", line 15
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/windows.py =>   File ".check_venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/windows.py", line 15
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/sympy/core/basic.py =>   File ".check_venv/lib/python3.12/site-packages/sympy/core/basic.py", line 15
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/sympy/core/containers.py =>   File ".check_venv/lib/python3.12/site-packages/sympy/core/containers.py", line 22
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/sympy/stats/rv.py =>   File ".check_venv/lib/python3.12/site-packages/sympy/stats/rv.py", line 29
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

.check_venv/lib/python3.12/site-packages/uvicorn/workers.py =>   File ".check_venv/lib/python3.12/site-packages/uvicorn/workers.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

auth_router.py =>   File "auth_router.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/anyio/_core/_sockets.py =>   File "crypto-venv/lib/python3.12/site-packages/anyio/_core/_sockets.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/click/core.py =>   File "crypto-venv/lib/python3.12/site-packages/click/core.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/cryptography/hazmat/backends/openssl/backend.py =>   File "crypto-venv/lib/python3.12/site-packages/cryptography/hazmat/backends/openssl/backend.py", line 18
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/fontTools/designspaceLib/__init__.py =>   File "crypto-venv/lib/python3.12/site-packages/fontTools/designspaceLib/__init__.py", line 20
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/fontTools/ufoLib/__init__.py =>   File "crypto-venv/lib/python3.12/site-packages/fontTools/ufoLib/__init__.py", line 48
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/httpcore/_async/connection.py =>   File "crypto-venv/lib/python3.12/site-packages/httpcore/_async/connection.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/httpcore/_async/connection_pool.py =>   File "crypto-venv/lib/python3.12/site-packages/httpcore/_async/connection_pool.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/httpcore/_async/http11.py =>   File "crypto-venv/lib/python3.12/site-packages/httpcore/_async/http11.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/httpcore/_async/http2.py =>   File "crypto-venv/lib/python3.12/site-packages/httpcore/_async/http2.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/httpcore/_async/http_proxy.py =>   File "crypto-venv/lib/python3.12/site-packages/httpcore/_async/http_proxy.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py =>   File "crypto-venv/lib/python3.12/site-packages/httpcore/_async/socks_proxy.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/httpcore/_models.py =>   File "crypto-venv/lib/python3.12/site-packages/httpcore/_models.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/httpcore/_sync/connection.py =>   File "crypto-venv/lib/python3.12/site-packages/httpcore/_sync/connection.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/httpcore/_sync/connection_pool.py =>   File "crypto-venv/lib/python3.12/site-packages/httpcore/_sync/connection_pool.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http11.py =>   File "crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http11.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http2.py =>   File "crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http2.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http_proxy.py =>   File "crypto-venv/lib/python3.12/site-packages/httpcore/_sync/http_proxy.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py =>   File "crypto-venv/lib/python3.12/site-packages/httpcore/_sync/socks_proxy.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/httpx/_content.py =>   File "crypto-venv/lib/python3.12/site-packages/httpx/_content.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/jsonschema/protocols.py =>   File "crypto-venv/lib/python3.12/site-packages/jsonschema/protocols.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/jupyter_client/blocking/client.py =>   File "crypto-venv/lib/python3.12/site-packages/jupyter_client/blocking/client.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/jupyter_client/connect.py =>   File "crypto-venv/lib/python3.12/site-packages/jupyter_client/connect.py", line 22
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/jupyter_client/localinterfaces.py =>   File "crypto-venv/lib/python3.12/site-packages/jupyter_client/localinterfaces.py", line 18
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/matplotlib/pyplot.py =>   File "crypto-venv/lib/python3.12/site-packages/matplotlib/pyplot.py", line 55
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/onnx_ir/_protocols.py =>   File "crypto-venv/lib/python3.12/site-packages/onnx_ir/_protocols.py", line 44
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/packaging/version.py =>   File "crypto-venv/lib/python3.12/site-packages/packaging/version.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pandas/core/groupby/generic.py =>   File "crypto-venv/lib/python3.12/site-packages/pandas/core/groupby/generic.py", line 22
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pip/_vendor/packaging/version.py =>   File "crypto-venv/lib/python3.12/site-packages/pip/_vendor/packaging/version.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py =>   File "crypto-venv/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py", line 36
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__init__.py =>   File "crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__init__.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__main__.py =>   File "crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/__main__.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/android.py =>   File "crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/android.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/api.py =>   File "crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/api.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/macos.py =>   File "crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/macos.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py =>   File "crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/windows.py =>   File "crypto-venv/lib/python3.12/site-packages/pip/_vendor/platformdirs/windows.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pip_audit/_dependency_source/interface.py =>   File "crypto-venv/lib/python3.12/site-packages/pip_audit/_dependency_source/interface.py", line 19
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pip_audit/_format/interface.py =>   File "crypto-venv/lib/python3.12/site-packages/pip_audit/_format/interface.py", line 18
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pip_audit/_service/interface.py =>   File "crypto-venv/lib/python3.12/site-packages/pip_audit/_service/interface.py", line 19
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pip_audit/_state.py =>   File "crypto-venv/lib/python3.12/site-packages/pip_audit/_state.py", line 19
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pkg_resources/__init__.py =>   File "crypto-venv/lib/python3.12/site-packages/pkg_resources/__init__.py", line 33
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/platformdirs/__init__.py =>   File "crypto-venv/lib/python3.12/site-packages/platformdirs/__init__.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/platformdirs/__main__.py =>   File "crypto-venv/lib/python3.12/site-packages/platformdirs/__main__.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/platformdirs/_xdg.py =>   File "crypto-venv/lib/python3.12/site-packages/platformdirs/_xdg.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/platformdirs/android.py =>   File "crypto-venv/lib/python3.12/site-packages/platformdirs/android.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/platformdirs/api.py =>   File "crypto-venv/lib/python3.12/site-packages/platformdirs/api.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/platformdirs/macos.py =>   File "crypto-venv/lib/python3.12/site-packages/platformdirs/macos.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/platformdirs/unix.py =>   File "crypto-venv/lib/python3.12/site-packages/platformdirs/unix.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/platformdirs/windows.py =>   File "crypto-venv/lib/python3.12/site-packages/platformdirs/windows.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/prompt_toolkit/completion/nested.py =>   File "crypto-venv/lib/python3.12/site-packages/prompt_toolkit/completion/nested.py", line 18
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/prompt_toolkit/contrib/regular_languages/__init__.py =>   File "crypto-venv/lib/python3.12/site-packages/prompt_toolkit/contrib/regular_languages/__init__.py", line 89
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pyomo/contrib/observer/model_observer.py =>   File "crypto-venv/lib/python3.12/site-packages/pyomo/contrib/observer/model_observer.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/pyomo/core/base/var.py =>   File "crypto-venv/lib/python3.12/site-packages/pyomo/core/base/var.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/scipy/signal/_signaltools.py =>   File "crypto-venv/lib/python3.12/site-packages/scipy/signal/_signaltools.py", line 17
    from __future__ import annotations  # Provides typing union operator `|` in Python 3.9
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/setuptools/_distutils/command/config.py =>   File "crypto-venv/lib/python3.12/site-packages/setuptools/_distutils/command/config.py", line 25
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/packaging/version.py =>   File "crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/packaging/version.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/__init__.py =>   File "crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/__init__.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/__main__.py =>   File "crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/__main__.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/android.py =>   File "crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/android.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/api.py =>   File "crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/api.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/macos.py =>   File "crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/macos.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/unix.py =>   File "crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/unix.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/windows.py =>   File "crypto-venv/lib/python3.12/site-packages/setuptools/_vendor/platformdirs/windows.py", line 16
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/connectors/aioodbc.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/connectors/aioodbc.py", line 22
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/connectors/asyncio.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/connectors/asyncio.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/connectors/pyodbc.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/connectors/pyodbc.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/__init__.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/__init__.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/aiomysql.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/aiomysql.py", line 44
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/asyncmy.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/asyncmy.py", line 42
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/base.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/base.py", line 1079
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/cymysql.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/cymysql.py", line 36
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/enumerated.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/enumerated.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/json.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/json.py", line 20
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/mariadbconnector.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/mariadbconnector.py", line 43
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/mysqlconnector.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/mysqlconnector.py", line 61
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/mysqldb.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/mysqldb.py", line 100
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/pymysql.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/pymysql.py", line 63
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/pyodbc.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/pyodbc.py", line 58
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/reflection.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/reflection.py", line 20
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/types.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/types.py", line 20
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/oracle/cx_oracle.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/oracle/cx_oracle.py", line 505
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/oracle/types.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/oracle/types.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/postgresql/array.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/postgresql/array.py", line 22
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/postgresql/base.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/postgresql/base.py", line 1617
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/postgresql/json.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/postgresql/json.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/postgresql/pg_catalog.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/postgresql/pg_catalog.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/postgresql/psycopg2.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/postgresql/psycopg2.py", line 504
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/postgresql/types.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/postgresql/types.py", line 20
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 93
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/sqlite/base.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/sqlite/base.py", line 1003
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/sqlite/pysqlite.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/dialects/sqlite/pysqlite.py", line 408
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/_py_util.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/_py_util.py", line 20
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/characteristics.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/characteristics.py", line 20
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/create.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/create.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/cursor.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/cursor.py", line 25
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py", line 30
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/events.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/events.py", line 22
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/interfaces.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/interfaces.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/mock.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/mock.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/reflection.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/reflection.py", line 40
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/url.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/engine/url.py", line 30
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/events.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/events.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/exc.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/exc.py", line 28
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/associationproxy.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/associationproxy.py", line 29
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/asyncio/engine.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/asyncio/engine.py", line 20
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/asyncio/scoping.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/asyncio/scoping.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/asyncio/session.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/asyncio/session.py", line 20
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/automap.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/automap.py", line 726
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/compiler.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/compiler.py", line 497
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/horizontal_shard.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/horizontal_shard.py", line 39
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/hybrid.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/hybrid.py", line 860
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/mypy/names.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/ext/mypy/names.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/__init__.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/__init__.py", line 29
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/_orm_constructors.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/_orm_constructors.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/_typing.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/_typing.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/attributes.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/attributes.py", line 31
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/base.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/base.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/bulk_persistence.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/bulk_persistence.py", line 28
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/clsregistry.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/clsregistry.py", line 28
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/collections.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/collections.py", line 121
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/context.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/context.py", line 22
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/decl_api.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/decl_api.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/decl_base.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/decl_base.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/dependency.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/dependency.py", line 25
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/descriptor_props.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/descriptor_props.py", line 26
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/events.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/events.py", line 22
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/exc.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/exc.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/instrumentation.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/instrumentation.py", line 47
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/interfaces.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/interfaces.py", line 32
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/loading.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/loading.py", line 31
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/mapper.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/mapper.py", line 31
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/path_registry.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/path_registry.py", line 22
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/properties.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/properties.py", line 28
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/query.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/query.py", line 34
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/relationships.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/relationships.py", line 29
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/scoping.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/scoping.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/state.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/state.py", line 28
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/strategies.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/strategies.py", line 26
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/strategy_options.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/strategy_options.py", line 24
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/unitofwork.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/unitofwork.py", line 31
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/util.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/util.py", line 22
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/writeonly.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/orm/writeonly.py", line 32
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/pool/base.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/pool/base.py", line 24
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/pool/events.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/pool/events.py", line 20
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/pool/impl.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/pool/impl.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/base.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/base.py", line 25
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/cache_key.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/cache_key.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/compiler.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/compiler.py", line 39
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/ddl.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/ddl.py", line 27
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/elements.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/elements.py", line 27
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/events.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/events.py", line 21
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/functions.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/functions.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/schema.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/schema.py", line 44
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/sqltypes.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/sqltypes.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/type_api.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/type_api.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/util.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/sql/util.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sqlalchemy/util/typing.py =>   File "crypto-venv/lib/python3.12/site-packages/sqlalchemy/util/typing.py", line 22
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sympy/core/basic.py =>   File "crypto-venv/lib/python3.12/site-packages/sympy/core/basic.py", line 15
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sympy/core/containers.py =>   File "crypto-venv/lib/python3.12/site-packages/sympy/core/containers.py", line 22
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/sympy/stats/rv.py =>   File "crypto-venv/lib/python3.12/site-packages/sympy/stats/rv.py", line 29
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/torch/_inductor/async_compile.py =>   File "crypto-venv/lib/python3.12/site-packages/torch/_inductor/async_compile.py", line 15
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/torch/_inductor/codegen/common.py =>   File "crypto-venv/lib/python3.12/site-packages/torch/_inductor/codegen/common.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/torch/_inductor/ir.py =>   File "crypto-venv/lib/python3.12/site-packages/torch/_inductor/ir.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/torch/cuda/graphs.py =>   File "crypto-venv/lib/python3.12/site-packages/torch/cuda/graphs.py", line 15
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/torch/distributed/_symmetric_memory/__init__.py =>   File "crypto-venv/lib/python3.12/site-packages/torch/distributed/_symmetric_memory/__init__.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py =>   File "crypto-venv/lib/python3.12/site-packages/torch/fx/experimental/symbolic_shapes.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/torch/onnx/_internal/torchscript_exporter/symbolic_opset9.py =>   File "crypto-venv/lib/python3.12/site-packages/torch/onnx/_internal/torchscript_exporter/symbolic_opset9.py", line 23
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

crypto-venv/lib/python3.12/site-packages/torch/xpu/graphs.py =>   File "crypto-venv/lib/python3.12/site-packages/torch/xpu/graphs.py", line 14
    from __future__ import annotations
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: from __future__ imports must occur at the beginning of the file

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ 

