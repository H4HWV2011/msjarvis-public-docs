(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild

docker logs jarvis-neurobiological-master --tail 200

docker exec jarvis-neurobiological-master python - <<'PY'
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import json

tests = [
    ("self_health", "http://127.0.0.1:8018/health", None),
    ("self_process", "http://127.0.0.1:8018/process", {"user_input":"test pulse"}),
    ("bridge_8018", "http://jarvis-consciousness-bridge:8018/health", None),
    ("i_containers", "http://jarvis-i-containers:8015/health", None),
    ("bbb", "http://jarvis-blood-brain-barrier:8016/health", None),
    ("qualia", "http://jarvis-qualia-engine:8017/health", None),
]

for name, url, payload in tests:
    try:
        if payload is None:
            r = urlopen(url, timeout=8)
bridge\|uvicorn.run" services neurobiological_brain 2>/dev/null | grep -i bridge
INFO:__main__:🧠 Initializing Neurobiological Master System...
INFO:__main__:✅ Neurobiological Master System operational!
INFO:__main__:🚀 Starting Neurobiological Master Integration on port 8018...
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8018 (Press CTRL+C to quit)
ERROR:__main__:Integration error: Timeout reading from socket
[DynamicPortService] Redis init failed: Error -2 connecting to redis:6379. Name or service not known.
INFO:     172.18.0.81:51140 - "POST /eeg_pulse HTTP/1.1" 500 Internal Server Error
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
INFO:     172.18.0.112:54618 - "GET /health HTTP/1.1" 200 OK
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
INFO:     172.18.0.112:53860 - "GET /health HTTP/1.1" 200 OK
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
services/main_brain.py.bak.20260522T192625Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/ms_jarvis_unified_gateway.py.bak.20260515T124756:56:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.bak.20260522T125014Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.pre-aaacpe-fix-20260413-154757:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/pituitary_gland.py:19:    "http://jarvis-consciousness-bridge:8020",
services/ms_jarvis_ULTIMATE.py.OLD:52:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak_sedpatch:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/examine_extracted_services.sh:12:cat "$EXTRACT/root/ms-jarvis-consciousness-bridge/main.py"
services/main_brain.py.bak.mcfix.1780455458:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.bak.remove-debug-banner.20260601-215513:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/integrate_discovered_services.sh:11:cp "$EXTRACT/ms-jarvis-consciousness-bridge/main.py" "$DEST/ms_jarvis_consciousness_bridge.py"
services/pituitary_gland.py.bak2:19:    "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.pre-local-summary-fix-20260413-154816:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak-20260528193958:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/ms_jarvis_unified_gateway.py.pre_constitutional:55:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
services/ms_jarvis_unified_gateway.py.bak_1768841920:42:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/analyze_advanced_modules.sh:11:head -50 $WORK/consciousness_bridge/root/ms-jarvis-consciousness-bridge/main.py
services/main_brain_legacy_backup.py.bak-msallis:250:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak_localnet_fixed2:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main.py.BACKUP:214:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.pre-community-fullfix-20260413-135255:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.manualbak5:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/ms_jarvis_ULTIMATE.py.before_fixes:52:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.backup_1771192185:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260509-214158:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/ms_jarvis_ULTIMATE.py.before_agent_fix:52:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.backup_nbb_fixed:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/bridge_cross_dgm_10023.py:3:Upstream:   http://jarvis-consciousness-bridge:8018
services/bridge_cross_dgm_10023.py:27:UPSTREAM_URL       = os.getenv("UPSTREAM_URL",           "http://jarvis-consciousness-bridge:8018")
services/main_brain.py.pre-phase4-fix-20260413-154833:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.before_spiritual_integration:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260522T202653Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.bak.1771185442:126:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/inspect_key_services.sh:21:head -30 $WORK/root/ms-jarvis-consciousness-bridge/main.py 2>/dev/null || echo "File not readable"
services/inspect_key_services.sh:32:grep -r "PORT" $WORK/root/ms-jarvis-consciousness-bridge/ 2>/dev/null | head -10
services/main_brain.py.bak.20260601-193118:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.pre_judges:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.pre-community-fix-20260413-134958:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.identity.20260601-213536:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main.py.bak-msallis:251:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.bak.20260530T152332:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/ai_server_11llm_OPTIMIZED.py.bak_1765074137:220:    # "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/running_services.log:21:  ms-jarvis-consciousness-bridge.service                                                    loaded active     running      Ms. Jarvis Consciousness Bridge (4-Agent System)
services/main.py.working_backup_20251020_110429:102:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.morning.1780490876:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/ms_jarvis_unified_gateway.py.bak.20260501_154501:194:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
services/ms_jarvis_unified_gateway.py.bak.20260501_154501:1045:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
services/main.py.FINALHEALTH.bak:214:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/extract_all_big_archives.sh:30:echo "📦 Archive 3: ms-jarvis-consciousness-bridge (13KB)"
services/extract_all_big_archives.sh:33:tar -xzf $DIR/ms-jarvis-consciousness-bridge.tar.gz -C consciousness_bridge
services/real_services_prod.txt:67:ms-jarvis-consciousness-bridge-8051-async
services/real_services_prod.txt:83:ms-jarvis-consciousness-bridge-8051-async-final
services/real_services_prod.txt:118:ms-jarvis-consciousness-bridge-8051
services/main_brain.py.bak.20260530T153529:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.pre-aaacpe-fix-20260413-135408:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/ms_jarvis_consciousness_bridge_enhanced.py.bak-msallis:110:                'http://jarvis-consciousness-bridge:8018/chat',  # Docker service name
services/main_brain.py.bak.20260530T152342:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/inventory_services.sh:37:tar -xzf $BACKUP/ms-jarvis-consciousness-bridge.tar.gz 2>/dev/null || echo "  Partial extraction"
services/main_brain.py.bak.20260601-192147:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main.py.backup:214:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/ms_jarvis_unified_gateway.py.BEFORE_REAL_CHAT_1768842649:48:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/nbb/pituitary_gland.py:19:    "http://jarvis-consciousness-bridge:8018",
services/nbb/pituitary_gland.py:160:    "http://jarvis-consciousness-bridge:8018/health",
services/nbb/pituitary_gland.py.bak:19:    "http://jarvis-consciousness-bridge:8018",
services/nbb/pituitary_gland.py.bak:160:    "http://jarvis-consciousness-bridge:8018/health",
services/nbb/pituitary_gland.py.bak-msallis:19:    "http://jarvis-consciousness-bridge:8018",
services/nbb/pituitary_gland.py.bak-msallis:160:    "http://jarvis-consciousness-bridge:8018/health",
services/build_dir_audit.txt:365:MISSING DIR: ./ms-jarvis-consciousness-bridge
services/build_dir_audit.txt:367:MISSING DIR: ./ms-jarvis-consciousness-bridge-enhanced
services/build_dir_audit.txt:368:MISSING DIR: ./ms-jarvis-consciousness-bridge-parallel-woah
services/build_dir_audit.txt:369:MISSING DIR: ./ms-jarvis-consciousness-bridge-service
services/build_dir_audit.txt:370:ONLY STUB: ./ms-jarvis-consciousness-bridge-with-fifth-dgm
services/build_dir_audit.txt:371:MISSING DIR: ./ms-jarvis-consciousness-bridge-woah
services/build_dir_audit.txt:372:MISSING DIR: ./ms-jarvis-consciousness-bridge-woah-psychology-patched
services/main_brain.py.bak_ultimate_1770573774:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.broken-20260413-134536:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260507-223435:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.before_final_fix:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.pre-verified-fix-20260413-134834:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.pre-local-summary-fix-20260413-135507:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260530T114539:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.bak.identity2.20260601-213734:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/ms_jarvis_unified_gateway.py.bak_1768840523:42:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/bridge_cross_dgm_10002.py:3:Upstream:   http://jarvis-consciousness-bridge:8018
services/bridge_cross_dgm_10002.py:27:UPSTREAM_URL       = os.getenv("UPSTREAM_URL",           "http://jarvis-consciousness-bridge:8018")
services/main_brain.py.bak.20260522T122413Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/jarvis-woah_dgm_supervisor_woah_fixed.py:103:        ("consciousness_bridge",    "jarvis-consciousness-bridge",       8020, ["consciousness","bridge"]),
services/main_brain.py.bak.20260530T153030:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/real_services_detected.txt:81:ms-jarvis-consciousness-bridge-8051-async
services/real_services_detected.txt:98:ms-jarvis-consciousness-bridge-8051-async-final
services/real_services_detected.txt:141:ms-jarvis-consciousness-bridge-8051
services/main_brain.py.bak:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.bak_1771728143:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.manualbak3:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/extract_service_tarballs.sh:21:    "ms-jarvis-consciousness-bridge.tar.gz" \
services/inventory_services.sh.bak-msallis:37:tar -xzf $BACKUP/ms-jarvis-consciousness-bridge.tar.gz 2>/dev/null || echo "  Partial extraction"
services/main_brain.py.pre-phase4-dedupe-20260413-150822:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/COMPLETE_DISCOVERY_REPORT.md:142:ms-jarvis-consciousness-bridge.tar.gz
services/main_brain.py.before_mother_carrie_v2:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260524_000429:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.bak.20260522T123325Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.bak.20260522T191836Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/jarvis-semaphore_msjarvis_semaphore.py.bak-msallis:113:    "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.bak.remove-debug-banner.20260601-222403:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.manualbak4:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.before_mother_carrie:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260430-211100:707:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.remove-debug-banner.20260601-222116:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/msjarvis_unified_gateway.py:55:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.pre-community-fullfix-20260413-154742:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/ms_jarvis_consciousness_bridge_enhanced.py:110:                'http://jarvis-consciousness-bridge:8018/chat',  # Docker service name
services/main.py.from_container:203:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/all_build_dirs.txt:365:./ms-jarvis-consciousness-bridge
services/all_build_dirs.txt:367:./ms-jarvis-consciousness-bridge-enhanced
services/all_build_dirs.txt:368:./ms-jarvis-consciousness-bridge-parallel-woah
services/all_build_dirs.txt:369:./ms-jarvis-consciousness-bridge-service
services/all_build_dirs.txt:370:./ms-jarvis-consciousness-bridge-with-fifth-dgm
services/all_build_dirs.txt:371:./ms-jarvis-consciousness-bridge-woah
services/all_build_dirs.txt:372:./ms-jarvis-consciousness-bridge-woah-psychology-patched
services/main.py.backup.broken:63:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.before_direct_fix:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak_pre_rag_fix_1778364422:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py:1137:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/ms_jarvis_ULTIMATE.py.before_bbb:52:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain_legacy_backup.py:250:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/restart_all_services.sh:9:sudo systemctl stop ms-jarvis-consciousness-bridge.service
services/restart_all_services.sh:44:sudo systemctl start ms-jarvis-consciousness-bridge.service
services/main_brain.py.manualbak:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak_legacy_chatlight:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260522T193224Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.pre-synthesis-lines-fix-20260413-160601:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main.py.bak:251:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.bak_ultimate_1770575025:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main.py.backup.before_auto_storage:63:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260601-205714:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/real_services_final.txt:8:ms-jarvis-consciousness-bridge-8051-async
services/real_services_final.txt:10:ms-jarvis-consciousness-bridge-8051-async-final
services/real_services_final.txt:17:ms-jarvis-consciousness-bridge-8051
services/main_brain.py.bak.20260530T152956:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.backup_1771192386:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260603-200957:1137:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260509-212923:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/woah_service.py:103:        ("consciousness_bridge",    "jarvis-consciousness-bridge",       8020, ["consciousness","bridge"]),
services/ms_jarvis_unified_gateway.py.WORKING_1768842334:48:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260527T114431Z:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.backup:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain_LEGACY_32svc.py:304:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/ms_jarvis_unified_gateway.py.bak.20260507-222001:50:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.pre_aaacpe_patch:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260509-213917:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260601-193421:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/ms_jarvis_unified_gateway.py.FORCED_UNIFIED_BACKUP:48:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/ms_jarvis_ULTIMATE.py.backup_1760806129:52:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/bridge_cross_dgm_10022.py:4:Downstream: http://jarvis-consciousness-bridge:8018
services/bridge_cross_dgm_10022.py:28:DOWNSTREAM_URL     = os.getenv("DOWNSTREAM_URL",         "http://jarvis-consciousness-bridge:8018")
services/main_brain.py.bak_20260603_135724:1096:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260508-071052:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak_localnet_fixed:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak_localnet:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260601-195059:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.bak-20260528193426:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.before_spiritual_rag:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260509-214526:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak_persona_1779997582:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain_container_2055.py:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.pre-synthesis-lines-fix2-20260413-161153:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260530T114441:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
services/main_brain_LEGACY_32svc.py.bak-msallis:304:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/COMPLETE_DISCOVERY_REPORT.md.bak-msallis:142:ms-jarvis-consciousness-bridge.tar.gz
services/jarvis-semaphore_msjarvis_semaphore.py:113:    "http://jarvis-consciousness-bridge:8018",
services/main_brain.py.pre-phase4-dedupe-20260413-154851:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main.py:253:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
services/ai_server_11llm_OPTIMIZED.py:242:    # "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.pre-phase4-fix-20260413-150714:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
services/main_brain.py.bak.20260522T192930Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
neurobiological_brain/pituitary_gland/service/pituitary_gland.py:41:    "http://jarvis-consciousness-bridge:8020",
neurobiological_brain/pituitary_gland/service/pituitary_gland.py.bak:19:    "http://jarvis-consciousness-bridge:8020",
docker-compose-core.yml:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose-core.yml:168:  jarvis-consciousness-bridge:
docker-compose-core.yml:169:    container_name: jarvis-consciousness-bridge
docker-compose-core.yml:170:    image: msjarvis-rebuild-jarvis-consciousness-bridge
docker-compose-core.yml.bak.20260430-120237:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose-core.yml.bak.20260430-120237:155:  jarvis-consciousness-bridge:
docker-compose-core.yml.bak.20260430-120237:156:    container_name: jarvis-consciousness-bridge
docker-compose-core.yml.bak.20260430-120237:157:    image: msjarvis-rebuild-jarvis-consciousness-bridge
docker-compose-core.yml.bak.20260507-222001:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose-core.yml.bak.20260507-222001:167:  jarvis-consciousness-bridge:
docker-compose-core.yml.bak.20260507-222001:168:    container_name: jarvis-consciousness-bridge
docker-compose-core.yml.bak.20260507-222001:169:    image: msjarvis-rebuild-jarvis-consciousness-bridge
docker-compose-core.yml.bak.20260507-222222:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose-core.yml.bak.20260507-222222:167:  jarvis-consciousness-bridge:
docker-compose-core.yml.bak.20260507-222222:168:    container_name: jarvis-consciousness-bridge
docker-compose-core.yml.bak.20260507-222222:169:    image: msjarvis-rebuild-jarvis-consciousness-bridge
docker-compose.gateway-only.generated.yml:24:      jarvis-consciousness-bridge:
docker-compose.gateway-only.generated.yml:104:      CONSCIOUSNESS_BRIDGE_URL: http://jarvis-consciousness-bridge:8018
docker-compose.golden.bak_bbb_clean_proxy:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.golden.bak_bbb_clean_proxy:34:    - jarvis-consciousness-bridge
docker-compose.golden.bak_bbb_clean_proxy:725:  jarvis-consciousness-bridge:
docker-compose.golden.bak_bbb_clean_proxy:728:    container_name: jarvis-consciousness-bridge
docker-compose.golden.bak_bbb_proxy_cmd_fix:32:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.golden.bak_bbb_proxy_cmd_fix:48:    - jarvis-consciousness-bridge
docker-compose.golden.bak_bbb_proxy_cmd_fix:712:  jarvis-consciousness-bridge:
docker-compose.golden.bak_bbb_proxy_cmd_fix:715:    container_name: jarvis-consciousness-bridge
docker-compose.golden.bak_bbb_uvicorn_fix:35:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.golden.bak_bbb_uvicorn_fix:51:    - jarvis-consciousness-bridge
docker-compose.golden.bak_bbb_uvicorn_fix:715:  jarvis-consciousness-bridge:
docker-compose.golden.bak_bbb_uvicorn_fix:718:    container_name: jarvis-consciousness-bridge
docker-compose.golden.bak_before_bbb_proxy2:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.golden.bak_before_bbb_proxy2:34:    - jarvis-consciousness-bridge
docker-compose.golden.bak_before_bbb_proxy2:726:  jarvis-consciousness-bridge:
docker-compose.golden.bak_before_bbb_proxy2:729:    container_name: jarvis-consciousness-bridge
docker-compose.golden.bak_before_brain_ports_cleanup:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.golden.bak_before_brain_ports_cleanup:36:    - jarvis-consciousness-bridge
docker-compose.golden.bak_before_brain_ports_cleanup:728:  jarvis-consciousness-bridge:
docker-compose.golden.bak_before_brain_ports_cleanup:731:    container_name: jarvis-consciousness-bridge
docker-compose.golden.bak_before_python3_cmd_fix:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.golden.bak_before_python3_cmd_fix:34:    - jarvis-consciousness-bridge
docker-compose.golden.bak_before_python3_cmd_fix:726:  jarvis-consciousness-bridge:
docker-compose.golden.bak_before_python3_cmd_fix:729:    container_name: jarvis-consciousness-bridge
docker-compose.golden.bak_nbb_base_final:36:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.golden.bak_nbb_base_final:52:    - jarvis-consciousness-bridge
docker-compose.golden.bak_nbb_base_final:715:  jarvis-consciousness-bridge:
docker-compose.golden.bak_nbb_base_final:718:    container_name: jarvis-consciousness-bridge
docker-compose.golden.bak_python310_compose_all:36:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.golden.bak_python310_compose_all:52:    - jarvis-consciousness-bridge
docker-compose.golden.bak_python310_compose_all:716:  jarvis-consciousness-bridge:
docker-compose.golden.bak_python310_compose_all:719:    container_name: jarvis-consciousness-bridge
docker-compose.golden.bak_services_mapping_fix:32:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.golden.bak_services_mapping_fix:48:    - jarvis-consciousness-bridge
docker-compose.golden.bak_services_mapping_fix:712:  jarvis-consciousness-bridge:
docker-compose.golden.bak_services_mapping_fix:715:    container_name: jarvis-consciousness-bridge
docker-compose.golden.bak_web_research_cmd:36:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.golden.bak_web_research_cmd:52:    - jarvis-consciousness-bridge
docker-compose.golden.bak_web_research_cmd:716:  jarvis-consciousness-bridge:
docker-compose.golden.bak_web_research_cmd:719:    container_name: jarvis-consciousness-bridge
docker-compose.golden.yml:36:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.golden.yml:52:      - jarvis-consciousness-bridge
docker-compose.golden.yml:708:  jarvis-consciousness-bridge:
docker-compose.golden.yml:711:    container_name: jarvis-consciousness-bridge
docker-compose.MOTHERCARRIE.BAK.20260216-132826:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.MOTHERCARRIE.BAK.20260216-132826:38:      - jarvis-consciousness-bridge
docker-compose.MOTHERCARRIE.BAK.20260216-132826:725:  jarvis-consciousness-bridge:
docker-compose.MOTHERCARRIE.BAK.20260216-132826:728:    container_name: jarvis-consciousness-bridge
docker-compose.MOTHERCARRIE.BAK.20260216-132826:1268:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.MOTHERCARRIE.BAK.20260216-132826:1271:      - jarvis-consciousness-bridge
docker-compose.MOTHERCARRIE.BAK.20260216-132834:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.MOTHERCARRIE.BAK.20260216-132834:38:      - jarvis-consciousness-bridge
docker-compose.MOTHERCARRIE.BAK.20260216-132834:725:  jarvis-consciousness-bridge:
docker-compose.MOTHERCARRIE.BAK.20260216-132834:728:    container_name: jarvis-consciousness-bridge
docker-compose.MOTHERCARRIE.BAK.20260216-132834:1268:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.MOTHERCARRIE.BAK.20260216-132834:1271:      - jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml:193:  jarvis-consciousness-bridge:
docker-compose.RAG_WORKING_20260116.yml:196:    container_name: jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml:204:    image: msjarvis-consciousness-bridge:latest
docker-compose.RAG_WORKING_20260116.yml:336:    - jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml:368:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.RAG_WORKING_20260116.yml:574:    - jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml:577:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:193:  jarvis-consciousness-bridge:
docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:196:    container_name: jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:204:    image: msjarvis-consciousness-bridge:latest
docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:336:    - jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:368:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:574:    - jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:577:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:193:  jarvis-consciousness-bridge:
docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:196:    container_name: jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:204:    image: msjarvis-consciousness-bridge:latest
docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:336:    - jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:368:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:574:    - jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:577:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:193:  jarvis-consciousness-bridge:
docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:196:    container_name: jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:204:    image: msjarvis-consciousness-bridge:latest
docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:336:    - jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:368:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:574:    - jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:577:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:193:  jarvis-consciousness-bridge:
docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:196:    container_name: jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:204:    image: msjarvis-consciousness-bridge:latest
docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:336:    - jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:368:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:574:    - jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:577:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:193:  jarvis-consciousness-bridge:
docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:196:    container_name: jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:204:    image: msjarvis-consciousness-bridge:latest
docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:336:    - jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:368:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:574:    - jarvis-consciousness-bridge
docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:577:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.working.20260118-235132.yml:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.working.20260118-235132.yml:36:    - jarvis-consciousness-bridge
docker-compose.working.20260118-235132.yml:728:  jarvis-consciousness-bridge:
docker-compose.working.20260118-235132.yml:731:    container_name: jarvis-consciousness-bridge
docker-compose.working.20260119-000202.yml:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.working.20260119-000202.yml:36:    - jarvis-consciousness-bridge
docker-compose.working.20260119-000202.yml:728:  jarvis-consciousness-bridge:
docker-compose.working.20260119-000202.yml:731:    container_name: jarvis-consciousness-bridge
docker-compose.yml:34:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml:55:      - jarvis-consciousness-bridge
docker-compose.yml:755:  jarvis-consciousness-bridge:
docker-compose.yml:759:    container_name: jarvis-consciousness-bridge
docker-compose.yml:1315:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml:1320:      - jarvis-consciousness-bridge
docker-compose.yml:1670:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml:1686:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml:1789:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml:1857:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml:1975:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.20llm.bak:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.20llm.bak:36:    - jarvis-consciousness-bridge
docker-compose.yml.20llm.bak:722:  jarvis-consciousness-bridge:
docker-compose.yml.20llm.bak:725:    container_name: jarvis-consciousness-bridge
docker-compose.yml.after-bbb.bak:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.after-bbb.bak:36:    - jarvis-consciousness-bridge
docker-compose.yml.after-bbb.bak:722:  jarvis-consciousness-bridge:
docker-compose.yml.after-bbb.bak:725:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup:38:      - jarvis-consciousness-bridge
docker-compose.yml.backup:725:  jarvis-consciousness-bridge:
docker-compose.yml.backup:728:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup:1268:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup:1271:      - jarvis-consciousness-bridge
docker-compose.yml.backup.1768311648:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup.1768311648:37:    - jarvis-consciousness-bridge
docker-compose.yml.backup.1768311648:682:  jarvis-consciousness-bridge:
docker-compose.yml.backup.1768311648:685:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.backup.1768311648:686:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup.1768311648:712:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup.1768311648:714:    - jarvis-consciousness-bridge
docker-compose.yml.backup.1768313257:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup.1768313257:37:    - jarvis-consciousness-bridge
docker-compose.yml.backup.1768313257:682:  jarvis-consciousness-bridge:
docker-compose.yml.backup.1768313257:685:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.backup.1768313257:686:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup.1768313257:712:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup.1768313257:714:    - jarvis-consciousness-bridge
docker-compose.yml.backup.1768313407:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup.1768313407:37:    - jarvis-consciousness-bridge
docker-compose.yml.backup.1768313407:686:  jarvis-consciousness-bridge:
docker-compose.yml.backup.1768313407:689:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.backup.1768313407:690:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup.1768313407:716:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup.1768313407:718:    - jarvis-consciousness-bridge
docker-compose.yml.backup.1768786837:24:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup.1768786837:42:      - jarvis-consciousness-bridge
docker-compose.yml.backup.1768786837:718:  jarvis-consciousness-bridge:
docker-compose.yml.backup.1768786837:721:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.backup.1768786837:722:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup.1768786837:749:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup.1768786837:751:      - jarvis-consciousness-bridge
docker-compose.yml.backup.1768788421:24:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup.1768788421:42:      - jarvis-consciousness-bridge
docker-compose.yml.backup.1768788421:711:  jarvis-consciousness-bridge:
docker-compose.yml.backup.1768788421:714:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.backup.1768788421:715:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup.1768788421:742:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup.1768788421:744:      - jarvis-consciousness-bridge
docker-compose.yml.backup-1780140997:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup-1780140997:43:      - jarvis-consciousness-bridge
docker-compose.yml.backup-1780140997:744:  jarvis-consciousness-bridge:
docker-compose.yml.backup-1780140997:748:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup-1780140997:1308:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup-1780140997:1316:      - jarvis-consciousness-bridge
docker-compose.yml.backup-1780140997:1663:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup-1780140997:1679:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup-1780140997:1782:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup-1780140997:1850:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup-1780140997:1968:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup-1780141699:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup-1780141699:43:      - jarvis-consciousness-bridge
docker-compose.yml.backup-1780141699:744:  jarvis-consciousness-bridge:
docker-compose.yml.backup-1780141699:748:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup-1780141699:1308:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup-1780141699:1316:      - jarvis-consciousness-bridge
docker-compose.yml.backup-1780141699:1663:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup-1780141699:1679:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup-1780141699:1782:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup-1780141699:1850:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup-1780141699:1968:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup_20260215_232944:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_20260215_232944:38:      - jarvis-consciousness-bridge
docker-compose.yml.backup_20260215_232944:725:  jarvis-consciousness-bridge:
docker-compose.yml.backup_20260215_232944:728:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_20260215_232944:1268:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_20260215_232944:1271:      - jarvis-consciousness-bridge
docker-compose.yml.backup_20260218_085941:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup_20260218_085941:38:      - jarvis-consciousness-bridge
docker-compose.yml.backup_20260218_085941:693:  jarvis-consciousness-bridge:
docker-compose.yml.backup_20260218_085941:696:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_20260218_085941:1191:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup_20260218_085941:1194:      - jarvis-consciousness-bridge
docker-compose.yml.backup_20260318_102158:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_20260318_102158:39:    - jarvis-consciousness-bridge
docker-compose.yml.backup_20260318_102158:636:  jarvis-consciousness-bridge:
docker-compose.yml.backup_20260318_102158:637:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
docker-compose.yml.backup_20260318_102158:638:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_20260318_103245:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_20260318_103245:39:    - jarvis-consciousness-bridge
docker-compose.yml.backup_20260318_103245:636:  jarvis-consciousness-bridge:
docker-compose.yml.backup_20260318_103245:637:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
docker-compose.yml.backup_20260318_103245:638:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_20260318_103829:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_20260318_103829:39:    - jarvis-consciousness-bridge
docker-compose.yml.backup_20260318_103829:636:  jarvis-consciousness-bridge:
docker-compose.yml.backup_20260318_103829:637:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
docker-compose.yml.backup_20260318_103829:638:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_20260318_110053:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_20260318_110053:39:    - jarvis-consciousness-bridge
docker-compose.yml.backup_20260318_110053:636:  jarvis-consciousness-bridge:
docker-compose.yml.backup_20260318_110053:637:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
docker-compose.yml.backup_20260318_110053:638:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_20260318_110223:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_20260318_110223:39:    - jarvis-consciousness-bridge
docker-compose.yml.backup_20260318_110223:636:  jarvis-consciousness-bridge:
docker-compose.yml.backup_20260318_110223:637:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
docker-compose.yml.backup_20260318_110223:638:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_20260318_110927:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_20260318_110927:39:    - jarvis-consciousness-bridge
docker-compose.yml.backup_20260318_110927:636:  jarvis-consciousness-bridge:
docker-compose.yml.backup_20260318_110927:637:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
docker-compose.yml.backup_20260318_110927:638:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_20260323_205752:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_20260323_205752:39:    - jarvis-consciousness-bridge
docker-compose.yml.backup_20260323_205752:658:  jarvis-consciousness-bridge:
docker-compose.yml.backup_20260323_205752:659:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
docker-compose.yml.backup_20260323_205752:660:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_20260323_211407:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_20260323_211407:39:    - jarvis-consciousness-bridge
docker-compose.yml.backup_20260323_211407:658:  jarvis-consciousness-bridge:
docker-compose.yml.backup_20260323_211407:659:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
docker-compose.yml.backup_20260323_211407:660:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_20260406_newservices:22:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_20260406_newservices:40:    - jarvis-consciousness-bridge
docker-compose.yml.backup_20260406_newservices:754:  jarvis-consciousness-bridge:
docker-compose.yml.backup_20260406_newservices:757:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_20260406_newservices:840:    - CONSCIOUSNESS_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_autonomous_learner_20260109-074048:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_autonomous_learner_20260109-074048:36:    - jarvis-consciousness-bridge
docker-compose.yml.backup_autonomous_learner_20260109-074048:728:  jarvis-consciousness-bridge:
docker-compose.yml.backup_autonomous_learner_20260109-074048:731:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_gateway_ports_20260109-091103:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_gateway_ports_20260109-091103:36:    - jarvis-consciousness-bridge
docker-compose.yml.backup_gateway_ports_20260109-091103:728:  jarvis-consciousness-bridge:
docker-compose.yml.backup_gateway_ports_20260109-091103:731:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_jan13_consciousness:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_jan13_consciousness:37:    - jarvis-consciousness-bridge
docker-compose.yml.backup_jan13_consciousness:682:  jarvis-consciousness-bridge:
docker-compose.yml.backup_jan13_consciousness:685:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.backup_jan13_consciousness:686:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_jan13_consciousness:712:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.backup_jan13_consciousness:714:    - jarvis-consciousness-bridge
docker-compose.yml.backup_nbb_ports:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup_nbb_ports:38:      - jarvis-consciousness-bridge
docker-compose.yml.backup_nbb_ports:693:  jarvis-consciousness-bridge:
docker-compose.yml.backup_nbb_ports:696:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_nbb_ports:1191:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup_nbb_ports:1194:      - jarvis-consciousness-bridge
docker-compose.yml.backup_nbb_ports_fixed:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup_nbb_ports_fixed:38:      - jarvis-consciousness-bridge
docker-compose.yml.backup_nbb_ports_fixed:693:  jarvis-consciousness-bridge:
docker-compose.yml.backup_nbb_ports_fixed:696:    container_name: jarvis-consciousness-bridge
docker-compose.yml.backup_nbb_ports_fixed:1191:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.backup_nbb_ports_fixed:1194:      - jarvis-consciousness-bridge
docker-compose.yml.bak:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak:38:    - jarvis-consciousness-bridge
docker-compose.yml.bak:732:  jarvis-consciousness-bridge:
docker-compose.yml.bak:735:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak:1286:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak:1289:    - jarvis-consciousness-bridge
docker-compose.yml.bak.1768500857:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.1768500857:37:    - jarvis-consciousness-bridge
docker-compose.yml.bak.1768500857:692:  jarvis-consciousness-bridge:
docker-compose.yml.bak.1768500857:695:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.bak.1768500857:696:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.1768500857:722:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.1768500857:724:    - jarvis-consciousness-bridge
docker-compose.yml.bak.1768781706:26:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.1768781706:50:      - jarvis-consciousness-bridge
docker-compose.yml.bak.1768781706:727:  jarvis-consciousness-bridge:
docker-compose.yml.bak.1768781706:730:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.bak.1768781706:731:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.1768781706:758:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.1768781706:760:      - jarvis-consciousness-bridge
docker-compose.yml.bak-1768791131:24:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak-1768791131:42:      - jarvis-consciousness-bridge
docker-compose.yml.bak-1768791131:711:  jarvis-consciousness-bridge:
docker-compose.yml.bak-1768791131:714:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.bak-1768791131:715:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak-1768791131:742:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak-1768791131:744:      - jarvis-consciousness-bridge
docker-compose.yml.bak-1768791194:24:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak-1768791194:42:      - jarvis-consciousness-bridge
docker-compose.yml.bak-1768791194:711:  jarvis-consciousness-bridge:
docker-compose.yml.bak-1768791194:714:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.bak-1768791194:715:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak-1768791194:742:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak-1768791194:744:      - jarvis-consciousness-bridge
docker-compose.yml.bak-1768791760:24:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak-1768791760:42:      - jarvis-consciousness-bridge
docker-compose.yml.bak-1768791760:711:  jarvis-consciousness-bridge:
docker-compose.yml.bak-1768791760:714:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.bak-1768791760:715:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak-1768791760:742:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak-1768791760:744:      - jarvis-consciousness-bridge
docker-compose.yml.bak_1778453637:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak_1778453637:38:      - jarvis-consciousness-bridge
docker-compose.yml.bak_1778453637:732:  jarvis-consciousness-bridge:
docker-compose.yml.bak_1778453637:735:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak_1778453637:1243:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak_1778453637:1246:      - jarvis-consciousness-bridge
docker-compose.yml.bak2:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak2:40:      - jarvis-consciousness-bridge
docker-compose.yml.bak2:741:  jarvis-consciousness-bridge:
docker-compose.yml.bak2:745:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak2:1303:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak2:1309:      - jarvis-consciousness-bridge
docker-compose.yml.bak2:1656:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak2:1672:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak2:1775:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak2:1843:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak2:1961:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260206142334:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260206142334:34:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260206142334:677:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260206142334:680:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260206142646:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260206142646:34:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260206142646:677:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260206142646:680:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260407-221457:39:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260407-221457:57:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260407-221457:761:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260407-221457:764:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260416-141203:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260416-141203:60:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260416-141203:763:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260416-141203:767:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260416-141224:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260416-141224:60:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260416-141224:763:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260416-141224:767:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260416-141309:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260416-141309:60:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260416-141309:763:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260416-141309:767:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260416-141316:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260416-141316:60:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260416-141316:763:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260416-141316:767:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260416-141425:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260416-141425:60:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260416-141425:763:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260416-141425:767:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260416-141603:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260416-141603:60:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260416-141603:763:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260416-141603:767:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260416-141709:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260416-141709:60:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260416-141709:763:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260416-141709:767:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260416_144451:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260416_144451:60:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260416_144451:763:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260416_144451:767:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260416_144808:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260416_144808:60:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260416_144808:763:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260416_144808:767:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260416_145312:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260416_145312:60:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260416_145312:763:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260416_145312:767:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak-20260417-144354:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak-20260417-144354:60:    - jarvis-consciousness-bridge
docker-compose.yml.bak-20260417-144354:763:  jarvis-consciousness-bridge:
docker-compose.yml.bak-20260417-144354:767:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260422-204609:41:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260422-204609:59:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260422-204609:834:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260422-204609:838:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260422-204722:41:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260422-204722:59:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260422-204722:834:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260422-204722:838:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260422_220748:41:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260422_220748:59:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260422_220748:834:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260422_220748:838:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260423_095331:41:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260423_095331:59:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260423_095331:834:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260423_095331:838:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260430-115408:48:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260430-115408:72:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260430-115408:863:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260430-115408:867:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260430-202630:49:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260430-202630:83:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260430-202630:883:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260430-202630:887:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260501:49:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260501:84:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260501:884:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260501:888:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260501-200948:49:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak.20260501-200948:84:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260501-200948:884:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260501-200948:888:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260510-192741:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260510-192741:38:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260510-192741:732:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260510-192741:735:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260510-192741:1243:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260510-192741:1246:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260510-194401:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260510-194401:38:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260510-194401:732:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260510-194401:735:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260510-194401:1253:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260510-194401:1256:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260510-195030:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260510-195030:38:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260510-195030:732:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260510-195030:735:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260510-195030:1257:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260510-195030:1260:    - jarvis-consciousness-bridge
docker-compose.yml.bak.20260517-162627:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260517-162627:38:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260517-162627:737:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260517-162627:740:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260517-162627:1257:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260517-162627:1260:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260517-163017:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260517-163017:38:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260517-163017:737:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260517-163017:740:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260517-163017:1257:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260517-163017:1260:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260518-215027:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260518-215027:38:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260518-215027:737:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260518-215027:740:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260518-215027:1261:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260518-215027:1264:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260522_204447:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260522_204447:38:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260522_204447:737:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260522_204447:740:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260522_204447:1267:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260522_204447:1270:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260522T193400Z:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260522T193400Z:38:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260522T193400Z:737:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260522T193400Z:740:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260522T193400Z:1267:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260522T193400Z:1270:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260601-183350:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260601-183350:39:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260601-183350:739:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260601-183350:743:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260601-183350:1299:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260601-183350:1304:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260601-183350:1654:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260601-183350:1670:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260601-183350:1773:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260601-183350:1841:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260601-183350:1959:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260601-184933:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260601-184933:39:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260601-184933:739:  jarvis-consciousness-bridge:
docker-compose.yml.bak.20260601-184933:743:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak.20260601-184933:1299:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260601-184933:1304:      - jarvis-consciousness-bridge
docker-compose.yml.bak.20260601-184933:1654:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260601-184933:1670:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260601-184933:1773:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260601-184933:1841:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak.20260601-184933:1959:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.bak_add_clock:24:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_add_clock:48:      - jarvis-consciousness-bridge
docker-compose.yml.bak_add_clock:759:  jarvis-consciousness-bridge:
docker-compose.yml.bak_add_clock:762:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.bak_add_clock:763:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak_add_clock:790:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_add_clock:792:      - jarvis-consciousness-bridge
docker-compose.yml.bak_before_unified_fix:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_before_unified_fix:36:    - jarvis-consciousness-bridge
docker-compose.yml.bak_before_unified_fix:728:  jarvis-consciousness-bridge:
docker-compose.yml.bak_before_unified_fix:731:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak_drop_images:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_drop_images:38:    - jarvis-consciousness-bridge
docker-compose.yml.bak_drop_images:772:  jarvis-consciousness-bridge:
docker-compose.yml.bak_drop_images:775:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.bak_drop_images:776:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak_drop_images:803:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_drop_images:806:    - jarvis-consciousness-bridge
docker-compose.yml.bak_drop_roche:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_drop_roche:37:    - jarvis-consciousness-bridge
docker-compose.yml.bak_drop_roche:734:  jarvis-consciousness-bridge:
docker-compose.yml.bak_drop_roche:737:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak_drop_roche:763:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_drop_roche:766:    - jarvis-consciousness-bridge
docker-compose.yml.bak_ports_20260118163828:26:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_ports_20260118163828:50:      - jarvis-consciousness-bridge
docker-compose.yml.bak_ports_20260118163828:727:  jarvis-consciousness-bridge:
docker-compose.yml.bak_ports_20260118163828:730:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.bak_ports_20260118163828:731:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak_ports_20260118163828:758:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_ports_20260118163828:760:      - jarvis-consciousness-bridge
docker-compose.yml.bak_redis_env_1769196600:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_redis_env_1769196600:34:      - jarvis-consciousness-bridge
docker-compose.yml.bak_redis_env_1769196600:692:  jarvis-consciousness-bridge:
docker-compose.yml.bak_redis_env_1769196600:695:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak_redis_fix_1769195136:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_redis_fix_1769195136:34:      - jarvis-consciousness-bridge
docker-compose.yml.bak_redis_fix_1769195136:692:  jarvis-consciousness-bridge:
docker-compose.yml.bak_redis_fix_1769195136:695:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak_redis_fix_1769195657:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_redis_fix_1769195657:34:      - jarvis-consciousness-bridge
docker-compose.yml.bak_redis_fix_1769195657:692:  jarvis-consciousness-bridge:
docker-compose.yml.bak_redis_fix_1769195657:695:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak_unified_cycle_fix:17:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_unified_cycle_fix:34:      - jarvis-consciousness-bridge
docker-compose.yml.bak_unified_cycle_fix:694:  jarvis-consciousness-bridge:
docker-compose.yml.bak_unified_cycle_fix:697:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak_woah_20260118163402:26:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_woah_20260118163402:50:      - jarvis-consciousness-bridge
docker-compose.yml.bak_woah_20260118163402:727:  jarvis-consciousness-bridge:
docker-compose.yml.bak_woah_20260118163402:730:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.bak_woah_20260118163402:731:    container_name: jarvis-consciousness-bridge
docker-compose.yml.bak_woah_20260118163402:758:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bak_woah_20260118163402:760:      - jarvis-consciousness-bridge
docker-compose.yml.bbb.bak:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.bbb.bak:36:    - jarvis-consciousness-bridge
docker-compose.yml.bbb.bak:728:  jarvis-consciousness-bridge:
docker-compose.yml.bbb.bak:731:    container_name: jarvis-consciousness-bridge
docker-compose.yml.before_fix:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.before_fix:38:      - jarvis-consciousness-bridge
docker-compose.yml.before_fix:725:  jarvis-consciousness-bridge:
docker-compose.yml.before_fix:728:    container_name: jarvis-consciousness-bridge
docker-compose.yml.before_fix:1268:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.before_fix:1271:      - jarvis-consciousness-bridge
docker-compose.yml.before_fix_20260122:17:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.before_fix_20260122:33:      - jarvis-consciousness-bridge
docker-compose.yml.before_fix_20260122:693:  jarvis-consciousness-bridge:
docker-compose.yml.before_fix_20260122:696:    container_name: jarvis-consciousness-bridge
docker-compose.yml.before_neuro_fix_1768012948:19:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.before_neuro_fix_1768012948:38:      - jarvis-consciousness-bridge
docker-compose.yml.before_neuro_fix_1768012948:711:  jarvis-consciousness-bridge:
docker-compose.yml.before_neuro_fix_1768012948:714:    container_name: jarvis-consciousness-bridge
docker-compose.yml.broken:21:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.broken-1768013498:19:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.broken-1768013498:38:      - jarvis-consciousness-bridge
docker-compose.yml.broken-1768013498:711:  jarvis-consciousness-bridge:
docker-compose.yml.broken-1768013498:714:    container_name: jarvis-consciousness-bridge
docker-compose.yml.broken-20260326-175632:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.broken-20260326-175632:36:    - jarvis-consciousness-bridge
docker-compose.yml.broken-20260326-175632:685:  jarvis-consciousness-bridge:
docker-compose.yml.broken-20260326-175632:688:    container_name: jarvis-consciousness-bridge
docker-compose.yml.broken_backup:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.broken_backup:38:      - jarvis-consciousness-bridge
docker-compose.yml.broken_backup:725:  jarvis-consciousness-bridge:
docker-compose.yml.broken_backup:728:    container_name: jarvis-consciousness-bridge
docker-compose.yml.broken_backup:1268:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.broken_backup:1271:      - jarvis-consciousness-bridge
docker-compose.yml.BROKEN_BACKUP:24:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.BROKEN_BACKUP:44:      - jarvis-consciousness-bridge
docker-compose.yml.BROKEN_BACKUP:721:  jarvis-consciousness-bridge:
docker-compose.yml.BROKEN_BACKUP:724:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.BROKEN_BACKUP:725:    container_name: jarvis-consciousness-bridge
docker-compose.yml.BROKEN_BACKUP:752:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.BROKEN_BACKUP:754:      - jarvis-consciousness-bridge
docker-compose.yml.broken_spiritual:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.broken_spiritual:38:      - jarvis-consciousness-bridge
docker-compose.yml.broken_spiritual:725:  jarvis-consciousness-bridge:
docker-compose.yml.broken_spiritual:728:    container_name: jarvis-consciousness-bridge
docker-compose.yml.broken_spiritual:1268:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.broken_spiritual:1271:      - jarvis-consciousness-bridge
docker-compose.yml.chroma-backup-20260114054916:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.chroma-backup-20260114054916:37:    - jarvis-consciousness-bridge
docker-compose.yml.chroma-backup-20260114054916:686:  jarvis-consciousness-bridge:
docker-compose.yml.chroma-backup-20260114054916:689:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.chroma-backup-20260114054916:690:    container_name: jarvis-consciousness-bridge
docker-compose.yml.chroma-backup-20260114054916:716:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.chroma-backup-20260114054916:718:    - jarvis-consciousness-bridge
docker-compose.yml.chroma-backup-20260114060013:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.chroma-backup-20260114060013:37:    - jarvis-consciousness-bridge
docker-compose.yml.chroma-backup-20260114060013:686:  jarvis-consciousness-bridge:
docker-compose.yml.chroma-backup-20260114060013:689:    image: msjarvis-consciousness-bridge:latest
docker-compose.yml.chroma-backup-20260114060013:690:    container_name: jarvis-consciousness-bridge
docker-compose.yml.chroma-backup-20260114060013:716:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.chroma-backup-20260114060013:718:    - jarvis-consciousness-bridge
docker-compose.yml.full_backup_20260122:19:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.full_backup_20260122:35:      - jarvis-consciousness-bridge
docker-compose.yml.full_backup_20260122:695:  jarvis-consciousness-bridge:
docker-compose.yml.full_backup_20260122:698:    container_name: jarvis-consciousness-bridge
docker-compose.yml.nbb.bak:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.nbb.bak:36:    - jarvis-consciousness-bridge
docker-compose.yml.nbb.bak:722:  jarvis-consciousness-bridge:
docker-compose.yml.nbb.bak:725:    container_name: jarvis-consciousness-bridge
docker-compose.yml.pre_dsn_fix:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.pre_dsn_fix:36:    - jarvis-consciousness-bridge
docker-compose.yml.pre_dsn_fix:737:  jarvis-consciousness-bridge:
docker-compose.yml.pre_dsn_fix:740:    container_name: jarvis-consciousness-bridge
docker-compose.yml.pre_judges:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.pre_judges:38:      - jarvis-consciousness-bridge
docker-compose.yml.pre_judges:727:  jarvis-consciousness-bridge:
docker-compose.yml.pre_judges:730:    container_name: jarvis-consciousness-bridge
docker-compose.yml.pre_judges:1271:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.pre_judges:1274:      - jarvis-consciousness-bridge
docker-compose.yml.pre_ollama_env_bak:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.pre_ollama_env_bak:38:      - jarvis-consciousness-bridge
docker-compose.yml.pre_ollama_env_bak:732:  jarvis-consciousness-bridge:
docker-compose.yml.pre_ollama_env_bak:735:    container_name: jarvis-consciousness-bridge
docker-compose.yml.pre_ollama_env_bak:1243:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
docker-compose.yml.pre_ollama_env_bak:1246:      - jarvis-consciousness-bridge
docker-compose.yml.pre-secrets-fix:41:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
docker-compose.yml.pre-secrets-fix:59:    - jarvis-consciousness-bridge
docker-compose.yml.pre-secrets-fix:834:  jarvis-consciousness-bridge:
docker-compose.yml.pre-secrets-fix:838:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup.1768788421:24:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup.1768788421:42:      - jarvis-consciousness-bridge
./docker-compose.yml.backup.1768788421:711:  jarvis-consciousness-bridge:
./docker-compose.yml.backup.1768788421:714:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.backup.1768788421:715:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup.1768788421:742:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup.1768788421:744:      - jarvis-consciousness-bridge
./last-build.log:49: Image msjarvis-rebuild-jarvis-consciousness-bridge Building 
./last-build.log:173:#29 [jarvis-consciousness-bridge 1/4] FROM docker.io/library/python:3.12-slim
./last-build.log:235:#38 [jarvis-consciousness-bridge internal] load build context
./last-build.log:414: > [jarvis-consciousness-bridge internal] load build context:
./debug_consciousness_bridge.md:4:- Container `jarvis-consciousness-bridge` is running `msjarvisunifiedswaggergatewayFIXED.py`
./debug_consciousness_bridge.md:10:docker inspect jarvis-consciousness-bridge | grep Cmd
./docker-compose.yml.bak.20260501:49:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260501:84:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260501:884:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260501:888:    container_name: jarvis-consciousness-bridge
./docker-compose.gateway-only.generated.yml:24:      jarvis-consciousness-bridge:
./docker-compose.gateway-only.generated.yml:104:      CONSCIOUSNESS_BRIDGE_URL: http://jarvis-consciousness-bridge:8018
./docker-compose.golden.yml:36:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.golden.yml:52:      - jarvis-consciousness-bridge
./docker-compose.golden.yml:708:  jarvis-consciousness-bridge:
./docker-compose.golden.yml:711:    container_name: jarvis-consciousness-bridge
./healthy-state-20260412-1126.txt:15:jarvis-consciousness-bridge	Up 11 hours	
./docker-compose.yml.backup:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup:38:      - jarvis-consciousness-bridge
./docker-compose.yml.backup:725:  jarvis-consciousness-bridge:
./docker-compose.yml.backup:728:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup:1268:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup:1271:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260206142334:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260206142334:34:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260206142334:677:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260206142334:680:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260601-183350:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260601-183350:39:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260601-183350:739:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260601-183350:743:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260601-183350:1299:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260601-183350:1304:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260601-183350:1654:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260601-183350:1670:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260601-183350:1773:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260601-183350:1841:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260601-183350:1959:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260422-204722:41:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260422-204722:59:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260422-204722:834:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260422-204722:838:    container_name: jarvis-consciousness-bridge
./docker-compose.golden.bak_nbb_base_final:36:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.golden.bak_nbb_base_final:52:    - jarvis-consciousness-bridge
./docker-compose.golden.bak_nbb_base_final:715:  jarvis-consciousness-bridge:
./docker-compose.golden.bak_nbb_base_final:718:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.chroma-backup-20260114054916:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.chroma-backup-20260114054916:37:    - jarvis-consciousness-bridge
./docker-compose.yml.chroma-backup-20260114054916:686:  jarvis-consciousness-bridge:
./docker-compose.yml.chroma-backup-20260114054916:689:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.chroma-backup-20260114054916:690:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.chroma-backup-20260114054916:716:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.chroma-backup-20260114054916:718:    - jarvis-consciousness-bridge
./.env:164:CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.broken:21:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./.env.bak.20260601-160603:13:CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./last-build-no-llm12.log:13: Image msjarvis-rebuild-jarvis-consciousness-bridge Building 
./docker-compose.yml.bak.20260422-204609:41:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260422-204609:59:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260422-204609:834:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260422-204609:838:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak-1768791760:24:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak-1768791760:42:      - jarvis-consciousness-bridge
./docker-compose.yml.bak-1768791760:711:  jarvis-consciousness-bridge:
./docker-compose.yml.bak-1768791760:714:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.bak-1768791760:715:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak-1768791760:742:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak-1768791760:744:      - jarvis-consciousness-bridge
./docker-compose.yml.bak-1768791194:24:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak-1768791194:42:      - jarvis-consciousness-bridge
./docker-compose.yml.bak-1768791194:711:  jarvis-consciousness-bridge:
./docker-compose.yml.bak-1768791194:714:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.bak-1768791194:715:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak-1768791194:742:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak-1768791194:744:      - jarvis-consciousness-bridge
./docker-compose.yml.bak_unified_cycle_fix:17:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_unified_cycle_fix:34:      - jarvis-consciousness-bridge
./docker-compose.yml.bak_unified_cycle_fix:694:  jarvis-consciousness-bridge:
./docker-compose.yml.bak_unified_cycle_fix:697:    container_name: jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:193:  jarvis-consciousness-bridge:
./docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:196:    container_name: jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:204:    image: msjarvis-consciousness-bridge:latest
./docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:336:    - jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:368:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:574:    - jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:577:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.pre-secrets-fix:41:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.pre-secrets-fix:59:    - jarvis-consciousness-bridge
./docker-compose.yml.pre-secrets-fix:834:  jarvis-consciousness-bridge:
./docker-compose.yml.pre-secrets-fix:838:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260517-162627:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260517-162627:38:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260517-162627:737:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260517-162627:740:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260517-162627:1257:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260517-162627:1260:      - jarvis-consciousness-bridge
./docker-compose.golden.bak_services_mapping_fix:32:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.golden.bak_services_mapping_fix:48:    - jarvis-consciousness-bridge
./docker-compose.golden.bak_services_mapping_fix:712:  jarvis-consciousness-bridge:
./docker-compose.golden.bak_services_mapping_fix:715:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.full_backup_20260122:19:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.full_backup_20260122:35:      - jarvis-consciousness-bridge
./docker-compose.yml.full_backup_20260122:695:  jarvis-consciousness-bridge:
./docker-compose.yml.full_backup_20260122:698:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup_nbb_ports_fixed:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup_nbb_ports_fixed:38:      - jarvis-consciousness-bridge
./docker-compose.yml.backup_nbb_ports_fixed:693:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_nbb_ports_fixed:696:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup_nbb_ports_fixed:1191:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup_nbb_ports_fixed:1194:      - jarvis-consciousness-bridge
./docker-compose.yml.backup_20260318_110223:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_20260318_110223:39:    - jarvis-consciousness-bridge
./docker-compose.yml.backup_20260318_110223:636:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_20260318_110223:637:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
./docker-compose.yml.backup_20260318_110223:638:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260407-221457:39:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260407-221457:57:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260407-221457:761:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260407-221457:764:    container_name: jarvis-consciousness-bridge
./docker-compose.yml:34:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml:55:      - jarvis-consciousness-bridge
./docker-compose.yml:755:  jarvis-consciousness-bridge:
./docker-compose.yml:759:    container_name: jarvis-consciousness-bridge
./docker-compose.yml:1315:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml:1320:      - jarvis-consciousness-bridge
./docker-compose.yml:1670:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml:1686:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml:1789:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml:1857:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml:1975:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260601-184933:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260601-184933:39:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260601-184933:739:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260601-184933:743:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260601-184933:1299:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260601-184933:1304:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260601-184933:1654:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260601-184933:1670:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260601-184933:1773:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260601-184933:1841:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260601-184933:1959:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.golden.bak_bbb_proxy_cmd_fix:32:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.golden.bak_bbb_proxy_cmd_fix:48:    - jarvis-consciousness-bridge
./docker-compose.golden.bak_bbb_proxy_cmd_fix:712:  jarvis-consciousness-bridge:
./docker-compose.golden.bak_bbb_proxy_cmd_fix:715:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup-1780141699:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup-1780141699:43:      - jarvis-consciousness-bridge
./docker-compose.yml.backup-1780141699:744:  jarvis-consciousness-bridge:
./docker-compose.yml.backup-1780141699:748:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup-1780141699:1308:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup-1780141699:1316:      - jarvis-consciousness-bridge
./docker-compose.yml.backup-1780141699:1663:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup-1780141699:1679:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup-1780141699:1782:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup-1780141699:1850:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup-1780141699:1968:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
./.env.backup-20260505:15:CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260510-194401:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260510-194401:38:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260510-194401:732:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260510-194401:735:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260510-194401:1253:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260510-194401:1256:    - jarvis-consciousness-bridge
./docker-compose.yml.broken-1768013498:19:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.broken-1768013498:38:      - jarvis-consciousness-bridge
./docker-compose.yml.broken-1768013498:711:  jarvis-consciousness-bridge:
./docker-compose.yml.broken-1768013498:714:    container_name: jarvis-consciousness-bridge
./_archive/generated_20260430/ai_server_11llm_OPTIMIZED.py:242:    # "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak_ch29:471:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak_bbb_obs_20260415-125908:176:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak_bbb_obs_20260415-125908:935:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./_archive/service_baks_20260430/main_brain.py.bak3:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak_sedpatch:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak_gate_v3:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak_1768841920:42:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak_egeria_patch_1777059405:471:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak_localnet_fixed2:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.checkpoint.20260329_214153:155:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.checkpoint.20260329_214153:712:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./_archive/service_baks_20260430/ms_jarvis_ULTIMATE.py.before_fixes:52:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.backup_1771192185:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ms_jarvis_ULTIMATE.py.before_agent_fix:52:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.backup_nbb_fixed:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak_indent_fix:135:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak.1775579935:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.before_spiritual_integration:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak.20260416-212709:341:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak.1771185442:126:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak.ch22fix:343:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.checkpoint.20260329_213555:155:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.checkpoint.20260329_213555:712:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./_archive/service_baks_20260430/main_brain.py.bak_auth:301:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak.20260425_210943:471:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ai_server_11llm_OPTIMIZED.py.bak_1765074137:220:    # "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main.py.FINALHEALTH.bak:214:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak.20260415-225542:200:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak.20260415-225542:993:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./_archive/service_baks_20260430/main_brain.py.bak.1774448411:304:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak_1777342937:488:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main.py.backup:214:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak_clean:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.checkpoint.20260329_212043:155:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.checkpoint.20260329_212043:718:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./_archive/service_baks_20260430/main_brain.py.bak.20260416-141747:341:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak_ultimate_1770573774:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.before_final_fix:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak3.20260428_160451:668:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak.20260415-225131:200:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak.20260415-225131:993:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak_1768840523:42:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak.20260407_205446:329:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak.20260428_154533:668:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak.20260415-224852:208:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak.20260415-224852:1001:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./_archive/service_baks_20260430/main_brain.py.bak:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak_1771728143:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak.autopatch.20260415-221952:180:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak.autopatch.20260415-221952:973:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./_archive/service_baks_20260430/main_brain.py.before_mother_carrie_v2:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.before_mother_carrie:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main.py.backup.broken:63:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.before_direct_fix:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak2:134:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./_archive/service_baks_20260430/ms_jarvis_ULTIMATE.py.before_bbb:52:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak_legacy_chatlight:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak_ultimate_1770575025:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak2.20260428_155604:668:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main.py.backup.before_auto_storage:63:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak-20260419-1422:203:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak-20260419-1422:998:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./_archive/service_baks_20260430/main_brain.py.backup_1771192386:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.backup:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ms_jarvis_ULTIMATE.py.backup_1760806129:52:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak.1777320408:488:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak_localnet_fixed:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.bak_localnet:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/main_brain.py.before_spiritual_rag:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.checkpoint.20260329_211609:155:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak.20260415-224730:209:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./_archive/service_baks_20260430/ms_jarvis_unified_gateway.py.bak.20260415-224730:1002:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./_archive/service_baks_20260430/main_brain.py.bak_session_patch:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./docker-compose.golden.bak_web_research_cmd:36:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.golden.bak_web_research_cmd:52:    - jarvis-consciousness-bridge
./docker-compose.golden.bak_web_research_cmd:716:  jarvis-consciousness-bridge:
./docker-compose.golden.bak_web_research_cmd:719:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416_145312:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260416_145312:60:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416_145312:763:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260416_145312:767:    container_name: jarvis-consciousness-bridge
./.env.complete:15:CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./.env.bak:13:CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup-1780140997:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup-1780140997:43:      - jarvis-consciousness-bridge
./docker-compose.yml.backup-1780140997:744:  jarvis-consciousness-bridge:
./docker-compose.yml.backup-1780140997:748:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup-1780140997:1308:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup-1780140997:1316:      - jarvis-consciousness-bridge
./docker-compose.yml.backup-1780140997:1663:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup-1780140997:1679:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup-1780140997:1782:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup-1780140997:1850:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup-1780140997:1968:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260510-195030:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260510-195030:38:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260510-195030:732:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260510-195030:735:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260510-195030:1257:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260510-195030:1260:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:21:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:46:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:683:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:686:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/ms_jarvis_neurobiological_master.py:26:    "consciousness_bridge":os.getenv("CONSCIOUSNESS_URL",    "http://jarvis-consciousness-bridge:8018"),
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:44:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:681:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:684:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml:23:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml:48:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml:683:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml:686:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:21:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:46:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:683:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:686:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/ms_jarvis_unified_gateway.py.bak.20260428_215837:176:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./msjarvis-rebuild/ms_jarvis_unified_gateway.py.bak.20260428_215837:918:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./msjarvis-rebuild/ms_jarvis_unified_gateway.py.bak.20260524T220526:176:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8018"),
./msjarvis-rebuild/ms_jarvis_unified_gateway.py.bak.20260524T220526:926:    return await _m09_proxy("http://jarvis-consciousness-bridge:8018", True, path, request)
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:45:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:682:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:685:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:21:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:46:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:683:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:686:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:27:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:52:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:689:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:692:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:23:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:48:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:685:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:688:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:27:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:52:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:689:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:692:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:21:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:46:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:683:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:686:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:21:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:46:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:683:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:686:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:45:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:682:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:685:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak:673:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak:676:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:21:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:46:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:683:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:686:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/ms_jarvis_unified_gateway.py.bak.20260428_220139:176:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./msjarvis-rebuild/ms_jarvis_unified_gateway.py.bak.20260428_220139:918:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./msjarvis-rebuild/backups/fix-20260411-080355/main_brain.py.bak:343:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./msjarvis-rebuild/backups/fix-20260411-080355/ms_jarvis_unified_gateway.py.bak:176:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./msjarvis-rebuild/backups/fix-20260411-080355/ms_jarvis_unified_gateway.py.bak:918:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./msjarvis-rebuild/docker-compose.yml.bak-sec-20260410-001058:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak-sec-20260410-001058:44:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak-sec-20260410-001058:782:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak-sec-20260410-001058:785:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak_20260410_171707:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak_20260410_171707:44:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak_20260410_171707:783:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak_20260410_171707:786:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:679:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:682:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak-20260410-000750:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak-20260410-000750:44:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak-20260410-000750:782:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak-20260410-000750:785:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:41:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:678:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:681:    container_name: jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:27:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:52:    - jarvis-consciousness-bridge
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:689:  jarvis-consciousness-bridge:
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:692:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.1768781706:26:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.1768781706:50:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.1768781706:727:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.1768781706:730:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.bak.1768781706:731:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.1768781706:758:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.1768781706:760:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260423_095331:41:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260423_095331:59:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260423_095331:834:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260423_095331:838:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.before_fix_20260122:17:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.before_fix_20260122:33:      - jarvis-consciousness-bridge
./docker-compose.yml.before_fix_20260122:693:  jarvis-consciousness-bridge:
./docker-compose.yml.before_fix_20260122:696:    container_name: jarvis-consciousness-bridge
./last-build-full.log:33: Image msjarvis-rebuild-jarvis-consciousness-bridge Building 
./docker-compose.MOTHERCARRIE.BAK.20260216-132834:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.MOTHERCARRIE.BAK.20260216-132834:38:      - jarvis-consciousness-bridge
./docker-compose.MOTHERCARRIE.BAK.20260216-132834:725:  jarvis-consciousness-bridge:
./docker-compose.MOTHERCARRIE.BAK.20260216-132834:728:    container_name: jarvis-consciousness-bridge
./docker-compose.MOTHERCARRIE.BAK.20260216-132834:1268:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.MOTHERCARRIE.BAK.20260216-132834:1271:      - jarvis-consciousness-bridge
./STATUS_MARCH15_2026_FINAL.md:31:- jarvis-consciousness-bridge (8018) - Phase 4 bridge
./docker-compose.yml.bak.20260430-115408:48:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260430-115408:72:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260430-115408:863:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260430-115408:867:    container_name: jarvis-consciousness-bridge
./docker-compose-core.yml.bak.20260507-222222:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose-core.yml.bak.20260507-222222:167:  jarvis-consciousness-bridge:
./docker-compose-core.yml.bak.20260507-222222:168:    container_name: jarvis-consciousness-bridge
./docker-compose-core.yml.bak.20260507-222222:169:    image: msjarvis-rebuild-jarvis-consciousness-bridge
./docker-compose.yml.backup_20260318_103245:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_20260318_103245:39:    - jarvis-consciousness-bridge
./docker-compose.yml.backup_20260318_103245:636:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_20260318_103245:637:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
./docker-compose.yml.backup_20260318_103245:638:    container_name: jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:193:  jarvis-consciousness-bridge:
./docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:196:    container_name: jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:204:    image: msjarvis-consciousness-bridge:latest
./docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:336:    - jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:368:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:574:    - jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:577:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:41:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:59:    - jarvis-consciousness-bridge
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:834:  jarvis-consciousness-bridge:
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:838:    container_name: jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml:193:  jarvis-consciousness-bridge:
./docker-compose.RAG_WORKING_20260116.yml:196:    container_name: jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml:204:    image: msjarvis-consciousness-bridge:latest
./docker-compose.RAG_WORKING_20260116.yml:336:    - jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml:368:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.RAG_WORKING_20260116.yml:574:    - jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml:577:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose-core.yml.bak.20260507-222001:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose-core.yml.bak.20260507-222001:167:  jarvis-consciousness-bridge:
./docker-compose-core.yml.bak.20260507-222001:168:    container_name: jarvis-consciousness-bridge
./docker-compose-core.yml.bak.20260507-222001:169:    image: msjarvis-rebuild-jarvis-consciousness-bridge
./docker-compose.yml.backup_nbb_ports:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup_nbb_ports:38:      - jarvis-consciousness-bridge
./docker-compose.yml.backup_nbb_ports:693:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_nbb_ports:696:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup_nbb_ports:1191:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup_nbb_ports:1194:      - jarvis-consciousness-bridge
./docker-compose.yml.pre_ollama_env_bak:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.pre_ollama_env_bak:38:      - jarvis-consciousness-bridge
./docker-compose.yml.pre_ollama_env_bak:732:  jarvis-consciousness-bridge:
./docker-compose.yml.pre_ollama_env_bak:735:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.pre_ollama_env_bak:1243:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.pre_ollama_env_bak:1246:      - jarvis-consciousness-bridge
./pituitary_gland.py.bak:19:    "http://jarvis-consciousness-bridge:8020",
./output/ch18_verifyandtest_final.log:4:{"status":"degraded","systems":{"consciousness_bridge":{"status":"unavailable","url":"http://jarvis-consciousness-bridge:8020","responsive":false},"neurobiological_master":{"status":"unavailable","url":"http://jarvis-neurobiological-master:8018","responsive":false},"i_containers":{"status":"unavailable","url":"http://jarvis-i-containers:8015","responsive":false},"blood_brain_barrier":{"status":"unavailable","url":"http://jarvis-blood-brain-barrier:8016","responsive":false},"qualia_engine":{"status":"unavailable","url":"http://jarvis-qualia-engine:8017","responsive":false}},"total_queries":87,"timestamp":"2026-04-15T00:09:33.744211"}--- session-sidecar /health (best-effort) ---
./services/main_brain.py.bak.20260522T192625Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/ms_jarvis_unified_gateway.py.bak.20260515T124756:56:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.bak.20260522T125014Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.pre-aaacpe-fix-20260413-154757:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/pituitary_gland.py:19:    "http://jarvis-consciousness-bridge:8020",
./services/ms_jarvis_ULTIMATE.py.OLD:52:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak_sedpatch:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/examine_extracted_services.sh:12:cat "$EXTRACT/root/ms-jarvis-consciousness-bridge/main.py"
./services/main_brain.py.bak.mcfix.1780455458:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.bak.remove-debug-banner.20260601-215513:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/integrate_discovered_services.sh:11:cp "$EXTRACT/ms-jarvis-consciousness-bridge/main.py" "$DEST/ms_jarvis_consciousness_bridge.py"
./services/pituitary_gland.py.bak2:19:    "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.pre-local-summary-fix-20260413-154816:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak-20260528193958:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/ms_jarvis_unified_gateway.py.pre_constitutional:55:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
./services/ms_jarvis_unified_gateway.py.bak_1768841920:42:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/analyze_advanced_modules.sh:11:head -50 $WORK/consciousness_bridge/root/ms-jarvis-consciousness-bridge/main.py
./services/main_brain_legacy_backup.py.bak-msallis:250:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak_localnet_fixed2:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main.py.BACKUP:214:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.pre-community-fullfix-20260413-135255:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.manualbak5:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/ms_jarvis_ULTIMATE.py.before_fixes:52:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.backup_1771192185:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260509-214158:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/ms_jarvis_ULTIMATE.py.before_agent_fix:52:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.backup_nbb_fixed:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/bridge_cross_dgm_10023.py:3:Upstream:   http://jarvis-consciousness-bridge:8018
./services/bridge_cross_dgm_10023.py:27:UPSTREAM_URL       = os.getenv("UPSTREAM_URL",           "http://jarvis-consciousness-bridge:8018")
./services/main_brain.py.pre-phase4-fix-20260413-154833:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.before_spiritual_integration:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260522T202653Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.bak.1771185442:126:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/inspect_key_services.sh:21:head -30 $WORK/root/ms-jarvis-consciousness-bridge/main.py 2>/dev/null || echo "File not readable"
./services/inspect_key_services.sh:32:grep -r "PORT" $WORK/root/ms-jarvis-consciousness-bridge/ 2>/dev/null | head -10
./services/main_brain.py.bak.20260601-193118:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.pre_judges:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.pre-community-fix-20260413-134958:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.identity.20260601-213536:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main.py.bak-msallis:251:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.bak.20260530T152332:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/ai_server_11llm_OPTIMIZED.py.bak_1765074137:220:    # "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/running_services.log:21:  ms-jarvis-consciousness-bridge.service                                                    loaded active     running      Ms. Jarvis Consciousness Bridge (4-Agent System)
./services/main.py.working_backup_20251020_110429:102:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.morning.1780490876:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/ms_jarvis_unified_gateway.py.bak.20260501_154501:194:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./services/ms_jarvis_unified_gateway.py.bak.20260501_154501:1045:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./services/main.py.FINALHEALTH.bak:214:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/extract_all_big_archives.sh:30:echo "📦 Archive 3: ms-jarvis-consciousness-bridge (13KB)"
./services/extract_all_big_archives.sh:33:tar -xzf $DIR/ms-jarvis-consciousness-bridge.tar.gz -C consciousness_bridge
./services/real_services_prod.txt:67:ms-jarvis-consciousness-bridge-8051-async
./services/real_services_prod.txt:83:ms-jarvis-consciousness-bridge-8051-async-final
./services/real_services_prod.txt:118:ms-jarvis-consciousness-bridge-8051
./services/main_brain.py.bak.20260530T153529:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.pre-aaacpe-fix-20260413-135408:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/ms_jarvis_consciousness_bridge_enhanced.py.bak-msallis:110:                'http://jarvis-consciousness-bridge:8018/chat',  # Docker service name
./services/main_brain.py.bak.20260530T152342:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/inventory_services.sh:37:tar -xzf $BACKUP/ms-jarvis-consciousness-bridge.tar.gz 2>/dev/null || echo "  Partial extraction"
./services/main_brain.py.bak.20260601-192147:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main.py.backup:214:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/ms_jarvis_unified_gateway.py.BEFORE_REAL_CHAT_1768842649:48:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/nbb/pituitary_gland.py:19:    "http://jarvis-consciousness-bridge:8018",
./services/nbb/pituitary_gland.py:160:    "http://jarvis-consciousness-bridge:8018/health",
./services/nbb/pituitary_gland.py.bak:19:    "http://jarvis-consciousness-bridge:8018",
./services/nbb/pituitary_gland.py.bak:160:    "http://jarvis-consciousness-bridge:8018/health",
./services/nbb/pituitary_gland.py.bak-msallis:19:    "http://jarvis-consciousness-bridge:8018",
./services/nbb/pituitary_gland.py.bak-msallis:160:    "http://jarvis-consciousness-bridge:8018/health",
./services/build_dir_audit.txt:365:MISSING DIR: ./ms-jarvis-consciousness-bridge
./services/build_dir_audit.txt:367:MISSING DIR: ./ms-jarvis-consciousness-bridge-enhanced
./services/build_dir_audit.txt:368:MISSING DIR: ./ms-jarvis-consciousness-bridge-parallel-woah
./services/build_dir_audit.txt:369:MISSING DIR: ./ms-jarvis-consciousness-bridge-service
./services/build_dir_audit.txt:370:ONLY STUB: ./ms-jarvis-consciousness-bridge-with-fifth-dgm
./services/build_dir_audit.txt:371:MISSING DIR: ./ms-jarvis-consciousness-bridge-woah
./services/build_dir_audit.txt:372:MISSING DIR: ./ms-jarvis-consciousness-bridge-woah-psychology-patched
./services/main_brain.py.bak_ultimate_1770573774:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.broken-20260413-134536:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260507-223435:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.before_final_fix:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.pre-verified-fix-20260413-134834:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.pre-local-summary-fix-20260413-135507:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260530T114539:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.bak.identity2.20260601-213734:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/ms_jarvis_unified_gateway.py.bak_1768840523:42:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/bridge_cross_dgm_10002.py:3:Upstream:   http://jarvis-consciousness-bridge:8018
./services/bridge_cross_dgm_10002.py:27:UPSTREAM_URL       = os.getenv("UPSTREAM_URL",           "http://jarvis-consciousness-bridge:8018")
./services/main_brain.py.bak.20260522T122413Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/jarvis-woah_dgm_supervisor_woah_fixed.py:103:        ("consciousness_bridge",    "jarvis-consciousness-bridge",       8020, ["consciousness","bridge"]),
./services/main_brain.py.bak.20260530T153030:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/real_services_detected.txt:81:ms-jarvis-consciousness-bridge-8051-async
./services/real_services_detected.txt:98:ms-jarvis-consciousness-bridge-8051-async-final
./services/real_services_detected.txt:141:ms-jarvis-consciousness-bridge-8051
./services/main_brain.py.bak:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.bak_1771728143:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.manualbak3:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/extract_service_tarballs.sh:21:    "ms-jarvis-consciousness-bridge.tar.gz" \
./services/inventory_services.sh.bak-msallis:37:tar -xzf $BACKUP/ms-jarvis-consciousness-bridge.tar.gz 2>/dev/null || echo "  Partial extraction"
./services/main_brain.py.pre-phase4-dedupe-20260413-150822:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/COMPLETE_DISCOVERY_REPORT.md:142:ms-jarvis-consciousness-bridge.tar.gz
./services/main_brain.py.before_mother_carrie_v2:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260524_000429:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.bak.20260522T123325Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.bak.20260522T191836Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/jarvis-semaphore_msjarvis_semaphore.py.bak-msallis:113:    "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.bak.remove-debug-banner.20260601-222403:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.manualbak4:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.before_mother_carrie:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260430-211100:707:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.remove-debug-banner.20260601-222116:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/msjarvis_unified_gateway.py:55:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.pre-community-fullfix-20260413-154742:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/ms_jarvis_consciousness_bridge_enhanced.py:110:                'http://jarvis-consciousness-bridge:8018/chat',  # Docker service name
./services/main.py.from_container:203:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/all_build_dirs.txt:365:./ms-jarvis-consciousness-bridge
./services/all_build_dirs.txt:367:./ms-jarvis-consciousness-bridge-enhanced
./services/all_build_dirs.txt:368:./ms-jarvis-consciousness-bridge-parallel-woah
./services/all_build_dirs.txt:369:./ms-jarvis-consciousness-bridge-service
./services/all_build_dirs.txt:370:./ms-jarvis-consciousness-bridge-with-fifth-dgm
./services/all_build_dirs.txt:371:./ms-jarvis-consciousness-bridge-woah
./services/all_build_dirs.txt:372:./ms-jarvis-consciousness-bridge-woah-psychology-patched
./services/main.py.backup.broken:63:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.before_direct_fix:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak_pre_rag_fix_1778364422:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py:1137:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/ms_jarvis_ULTIMATE.py.before_bbb:52:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain_legacy_backup.py:250:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/restart_all_services.sh:9:sudo systemctl stop ms-jarvis-consciousness-bridge.service
./services/restart_all_services.sh:44:sudo systemctl start ms-jarvis-consciousness-bridge.service
./services/main_brain.py.manualbak:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak_legacy_chatlight:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260522T193224Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.pre-synthesis-lines-fix-20260413-160601:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main.py.bak:251:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.bak_ultimate_1770575025:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main.py.backup.before_auto_storage:63:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260601-205714:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/real_services_final.txt:8:ms-jarvis-consciousness-bridge-8051-async
./services/real_services_final.txt:10:ms-jarvis-consciousness-bridge-8051-async-final
./services/real_services_final.txt:17:ms-jarvis-consciousness-bridge-8051
./services/main_brain.py.bak.20260530T152956:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.backup_1771192386:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260603-200957:1137:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260509-212923:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/woah_service.py:103:        ("consciousness_bridge",    "jarvis-consciousness-bridge",       8020, ["consciousness","bridge"]),
./services/ms_jarvis_unified_gateway.py.WORKING_1768842334:48:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260527T114431Z:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.backup:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain_LEGACY_32svc.py:304:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/ms_jarvis_unified_gateway.py.bak.20260507-222001:50:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.pre_aaacpe_patch:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260509-213917:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260601-193421:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/ms_jarvis_unified_gateway.py.FORCED_UNIFIED_BACKUP:48:            "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/ms_jarvis_ULTIMATE.py.backup_1760806129:52:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/bridge_cross_dgm_10022.py:4:Downstream: http://jarvis-consciousness-bridge:8018
./services/bridge_cross_dgm_10022.py:28:DOWNSTREAM_URL     = os.getenv("DOWNSTREAM_URL",         "http://jarvis-consciousness-bridge:8018")
./services/main_brain.py.bak_20260603_135724:1096:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260508-071052:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak_localnet_fixed:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak_localnet:136:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260601-195059:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.bak-20260528193426:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.before_spiritual_rag:127:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260509-214526:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak_persona_1779997582:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain_container_2055.py:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.pre-synthesis-lines-fix2-20260413-161153:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260530T114441:110:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./services/main_brain_LEGACY_32svc.py.bak-msallis:304:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/COMPLETE_DISCOVERY_REPORT.md.bak-msallis:142:ms-jarvis-consciousness-bridge.tar.gz
./services/jarvis-semaphore_msjarvis_semaphore.py:113:    "http://jarvis-consciousness-bridge:8018",
./services/main_brain.py.pre-phase4-dedupe-20260413-154851:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main.py:253:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
./services/ai_server_11llm_OPTIMIZED.py:242:    # "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.pre-phase4-fix-20260413-150714:344:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./services/main_brain.py.bak.20260522T192930Z:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./.fixbackups/20260530-102909/services/main_brain_legacy_backup.py:250:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./.fixbackups/20260530-102909/services/main_brain_LEGACY_32svc.py:304:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./.fixbackups/20260530-102909/services/main_brain_container_2055.py:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./.fixbackups/20260530-102909/services/main.py:253:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8018",
./.fixbackups/20260530-102909/services/ai_server_11llm_OPTIMIZED.py:242:    # "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./.fixbackups/main_brain.py.pre-hippocampus-20260603-111453:112:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8018",
./cb-logs-20260312-160957.log:1:jarvis-consciousness-bridge  | INFO:     Started server process [1]
./cb-logs-20260312-160957.log:2:jarvis-consciousness-bridge  | INFO:     Waiting for application startup.
./cb-logs-20260312-160957.log:3:jarvis-consciousness-bridge  | INFO:     Application startup complete.
./cb-logs-20260312-160957.log:4:jarvis-consciousness-bridge  | INFO:     Uvicorn running on http://0.0.0.0:8018 (Press CTRL+C to quit)
./cb-logs-20260312-160957.log:5:jarvis-consciousness-bridge  | INFO:     172.18.0.62:56056 - "POST /chat HTTP/1.1" 404 Not Found
./cb-logs-20260312-160957.log:6:jarvis-consciousness-bridge  | INFO:     172.18.0.62:43246 - "POST /chat HTTP/1.1" 404 Not Found
./docker-compose.yml.bak.20260501-200948:49:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260501-200948:84:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260501-200948:884:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260501-200948:888:    container_name: jarvis-consciousness-bridge
./running_containers_20260326.txt:11:jarvis-consciousness-bridge
./docker-compose.yml.backup_20260215_232944:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_20260215_232944:38:      - jarvis-consciousness-bridge
./docker-compose.yml.backup_20260215_232944:725:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_20260215_232944:728:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup_20260215_232944:1268:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_20260215_232944:1271:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416-141203:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260416-141203:60:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416-141203:763:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260416-141203:767:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak_1778453637:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak_1778453637:38:      - jarvis-consciousness-bridge
./docker-compose.yml.bak_1778453637:732:  jarvis-consciousness-bridge:
./docker-compose.yml.bak_1778453637:735:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak_1778453637:1243:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak_1778453637:1246:      - jarvis-consciousness-bridge
./docker-compose.yml.nbb.bak:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.nbb.bak:36:    - jarvis-consciousness-bridge
./docker-compose.yml.nbb.bak:722:  jarvis-consciousness-bridge:
./docker-compose.yml.nbb.bak:725:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260518-215027:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260518-215027:38:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260518-215027:737:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260518-215027:740:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260518-215027:1261:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260518-215027:1264:      - jarvis-consciousness-bridge
./docker-compose.yml.BROKEN_BACKUP:24:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.BROKEN_BACKUP:44:      - jarvis-consciousness-bridge
./docker-compose.yml.BROKEN_BACKUP:721:  jarvis-consciousness-bridge:
./docker-compose.yml.BROKEN_BACKUP:724:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.BROKEN_BACKUP:725:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.BROKEN_BACKUP:752:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.BROKEN_BACKUP:754:      - jarvis-consciousness-bridge
./last-build-final.log:45: Image msjarvis-rebuild-jarvis-consciousness-bridge Building 
./last-build-final.log:176:#28 [jarvis-consciousness-bridge internal] load build context
./last-build-final.log:205:#28 [jarvis-consciousness-bridge internal] load build context
./docker-compose.yml.bak.20260416_144451:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260416_144451:60:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416_144451:763:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260416_144451:767:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup_20260218_085941:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup_20260218_085941:38:      - jarvis-consciousness-bridge
./docker-compose.yml.backup_20260218_085941:693:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_20260218_085941:696:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup_20260218_085941:1191:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.backup_20260218_085941:1194:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416-141709:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260416-141709:60:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416-141709:763:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260416-141709:767:    container_name: jarvis-consciousness-bridge
./docker-compose-core.yml.bak.20260430-120237:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose-core.yml.bak.20260430-120237:155:  jarvis-consciousness-bridge:
./docker-compose-core.yml.bak.20260430-120237:156:    container_name: jarvis-consciousness-bridge
./docker-compose-core.yml.bak.20260430-120237:157:    image: msjarvis-rebuild-jarvis-consciousness-bridge
./docker-compose.yml.bak-20260417-144354:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak-20260417-144354:60:    - jarvis-consciousness-bridge
./docker-compose.yml.bak-20260417-144354:763:  jarvis-consciousness-bridge:
./docker-compose.yml.bak-20260417-144354:767:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak:38:    - jarvis-consciousness-bridge
./docker-compose.yml.bak:732:  jarvis-consciousness-bridge:
./docker-compose.yml.bak:735:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak:1286:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak:1289:    - jarvis-consciousness-bridge
./docker-compose.yml.backup_gateway_ports_20260109-091103:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_gateway_ports_20260109-091103:36:    - jarvis-consciousness-bridge
./docker-compose.yml.backup_gateway_ports_20260109-091103:728:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_gateway_ports_20260109-091103:731:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.broken-20260326-175632:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.broken-20260326-175632:36:    - jarvis-consciousness-bridge
./docker-compose.yml.broken-20260326-175632:685:  jarvis-consciousness-bridge:
./docker-compose.yml.broken-20260326-175632:688:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260206142646:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260206142646:34:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260206142646:677:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260206142646:680:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak-1768791131:24:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak-1768791131:42:      - jarvis-consciousness-bridge
./docker-compose.yml.bak-1768791131:711:  jarvis-consciousness-bridge:
./docker-compose.yml.bak-1768791131:714:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.bak-1768791131:715:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak-1768791131:742:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak-1768791131:744:      - jarvis-consciousness-bridge
./docker-compose.yml.after-bbb.bak:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.after-bbb.bak:36:    - jarvis-consciousness-bridge
./docker-compose.yml.after-bbb.bak:722:  jarvis-consciousness-bridge:
./docker-compose.yml.after-bbb.bak:725:    container_name: jarvis-consciousness-bridge
./running_containers_GOLDEN_94_20260326.txt:11:jarvis-consciousness-bridge
./docker-compose.yml.backup_jan13_consciousness:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_jan13_consciousness:37:    - jarvis-consciousness-bridge
./docker-compose.yml.backup_jan13_consciousness:682:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_jan13_consciousness:685:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.backup_jan13_consciousness:686:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup_jan13_consciousness:712:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_jan13_consciousness:714:    - jarvis-consciousness-bridge
./docker-compose.yml.before_fix:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.before_fix:38:      - jarvis-consciousness-bridge
./docker-compose.yml.before_fix:725:  jarvis-consciousness-bridge:
./docker-compose.yml.before_fix:728:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.before_fix:1268:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.before_fix:1271:      - jarvis-consciousness-bridge
./tmp-aaacpe-patch/main_brain.py.bak:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./tmp-aaacpe-patch/main_brain.py:300:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./docker-compose.yml.bak.20260510-192741:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260510-192741:38:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260510-192741:732:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260510-192741:735:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260510-192741:1243:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260510-192741:1246:      - jarvis-consciousness-bridge
./docker-compose.golden.bak_before_brain_ports_cleanup:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.golden.bak_before_brain_ports_cleanup:36:    - jarvis-consciousness-bridge
./docker-compose.golden.bak_before_brain_ports_cleanup:728:  jarvis-consciousness-bridge:
./docker-compose.golden.bak_before_brain_ports_cleanup:731:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416-141224:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260416-141224:60:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416-141224:763:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260416-141224:767:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak_redis_fix_1769195657:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_redis_fix_1769195657:34:      - jarvis-consciousness-bridge
./docker-compose.yml.bak_redis_fix_1769195657:692:  jarvis-consciousness-bridge:
./docker-compose.yml.bak_redis_fix_1769195657:695:    container_name: jarvis-consciousness-bridge
./running_containers_93clean_20260326.txt:25:jarvis-consciousness-bridge
./docker-compose.yml.backup.1768786837:24:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup.1768786837:42:      - jarvis-consciousness-bridge
./docker-compose.yml.backup.1768786837:718:  jarvis-consciousness-bridge:
./docker-compose.yml.backup.1768786837:721:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.backup.1768786837:722:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup.1768786837:749:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup.1768786837:751:      - jarvis-consciousness-bridge
./docker-compose.yml.bak2:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak2:40:      - jarvis-consciousness-bridge
./docker-compose.yml.bak2:741:  jarvis-consciousness-bridge:
./docker-compose.yml.bak2:745:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak2:1303:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak2:1309:      - jarvis-consciousness-bridge
./docker-compose.yml.bak2:1656:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak2:1672:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak2:1775:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak2:1843:      - DOWNSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak2:1961:      - UPSTREAM_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.MOTHERCARRIE.BAK.20260216-132826:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.MOTHERCARRIE.BAK.20260216-132826:38:      - jarvis-consciousness-bridge
./docker-compose.MOTHERCARRIE.BAK.20260216-132826:725:  jarvis-consciousness-bridge:
./docker-compose.MOTHERCARRIE.BAK.20260216-132826:728:    container_name: jarvis-consciousness-bridge
./docker-compose.MOTHERCARRIE.BAK.20260216-132826:1268:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.MOTHERCARRIE.BAK.20260216-132826:1271:      - jarvis-consciousness-bridge
./backups/fix-20260411-080527/main_brain.py.bak:343:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./backups/fix-20260411-080527/ms_jarvis_unified_gateway.py.bak:176:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./backups/fix-20260411-080527/ms_jarvis_unified_gateway.py.bak:918:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./backups/fix-20260411-080124/main_brain.py.bak:343:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./backups/fix-20260411-080124/ms_jarvis_unified_gateway.py.bak:176:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./backups/fix-20260411-080124/ms_jarvis_unified_gateway.py.bak:918:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./backups/fix-20260411-080158/main_brain.py.bak:343:    "consciousness_bridge": "http://jarvis-consciousness-bridge:8020",
./backups/fix-20260411-080158/ms_jarvis_unified_gateway.py.bak:176:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./backups/fix-20260411-080158/ms_jarvis_unified_gateway.py.bak:918:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./docker-compose.yml.bak_drop_roche:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_drop_roche:37:    - jarvis-consciousness-bridge
./docker-compose.yml.bak_drop_roche:734:  jarvis-consciousness-bridge:
./docker-compose.yml.bak_drop_roche:737:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak_drop_roche:763:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_drop_roche:766:    - jarvis-consciousness-bridge
./docker-compose.yml.bak_add_clock:24:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_add_clock:48:      - jarvis-consciousness-bridge
./docker-compose.yml.bak_add_clock:759:  jarvis-consciousness-bridge:
./docker-compose.yml.bak_add_clock:762:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.bak_add_clock:763:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak_add_clock:790:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_add_clock:792:      - jarvis-consciousness-bridge
./docker-compose.yml.backup_20260318_110053:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_20260318_110053:39:    - jarvis-consciousness-bridge
./docker-compose.yml.backup_20260318_110053:636:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_20260318_110053:637:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
./docker-compose.yml.backup_20260318_110053:638:    container_name: jarvis-consciousness-bridge
./ms_jarvis_unified_gateway.py.bak:194:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./ms_jarvis_unified_gateway.py.bak:949:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./docker-compose.yml.before_neuro_fix_1768012948:19:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.before_neuro_fix_1768012948:38:      - jarvis-consciousness-bridge
./docker-compose.yml.before_neuro_fix_1768012948:711:  jarvis-consciousness-bridge:
./docker-compose.yml.before_neuro_fix_1768012948:714:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak_redis_fix_1769195136:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_redis_fix_1769195136:34:      - jarvis-consciousness-bridge
./docker-compose.yml.bak_redis_fix_1769195136:692:  jarvis-consciousness-bridge:
./docker-compose.yml.bak_redis_fix_1769195136:695:    container_name: jarvis-consciousness-bridge
./KNOWN_ISSUES.md:6:- **Root cause**: `jarvis-consciousness-bridge` has no `CHROMA_URL` env var; hardcoded `localhost:8000` inside container; `jarvis-chroma` maps `8000→8002` on host
./docker-compose.yml.bak.20260517-163017:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260517-163017:38:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260517-163017:737:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260517-163017:740:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260517-163017:1257:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260517-163017:1260:      - jarvis-consciousness-bridge
./complete_service_mapping.json:9:  "jarvis-consciousness-bridge_ms_jarvis_consciousness_unified": "services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py",
./docker-compose.yml.broken_backup:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.broken_backup:38:      - jarvis-consciousness-bridge
./docker-compose.yml.broken_backup:725:  jarvis-consciousness-bridge:
./docker-compose.yml.broken_backup:728:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.broken_backup:1268:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.broken_backup:1271:      - jarvis-consciousness-bridge
./error_summary.log:16:=== jarvis-consciousness-bridge ===
./docker-compose.yml.bak.1768500857:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.1768500857:37:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.1768500857:692:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.1768500857:695:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.bak.1768500857:696:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.1768500857:722:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.1768500857:724:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260522_204447:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260522_204447:38:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260522_204447:737:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260522_204447:740:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260522_204447:1267:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260522_204447:1270:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416-141425:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260416-141425:60:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416-141425:763:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260416-141425:767:    container_name: jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:193:  jarvis-consciousness-bridge:
./docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:196:    container_name: jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:204:    image: msjarvis-consciousness-bridge:latest
./docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:336:    - jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:368:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:574:    - jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:577:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./fix_jarvis.log:72:jarvis-consciousness-bridge                             Up 8 hours
./docker-compose.yml.bak.20260416_144808:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260416_144808:60:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416_144808:763:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260416_144808:767:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bbb.bak:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bbb.bak:36:    - jarvis-consciousness-bridge
./docker-compose.yml.bbb.bak:728:  jarvis-consciousness-bridge:
./docker-compose.yml.bbb.bak:731:    container_name: jarvis-consciousness-bridge
./hilbert_verification_20260508_193018.log:36:jarvis-consciousness-bridge	Up 21 hours
./docker-compose.yml.backup.1768313257:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup.1768313257:37:    - jarvis-consciousness-bridge
./docker-compose.yml.backup.1768313257:682:  jarvis-consciousness-bridge:
./docker-compose.yml.backup.1768313257:685:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.backup.1768313257:686:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup.1768313257:712:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup.1768313257:714:    - jarvis-consciousness-bridge
./docker-compose.golden.bak_python310_compose_all:36:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.golden.bak_python310_compose_all:52:    - jarvis-consciousness-bridge
./docker-compose.golden.bak_python310_compose_all:716:  jarvis-consciousness-bridge:
./docker-compose.golden.bak_python310_compose_all:719:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416-141603:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260416-141603:60:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416-141603:763:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260416-141603:767:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260522T193400Z:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260522T193400Z:38:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260522T193400Z:737:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260522T193400Z:740:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak.20260522T193400Z:1267:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.bak.20260522T193400Z:1270:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260430-202630:49:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260430-202630:83:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260430-202630:883:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260430-202630:887:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup_autonomous_learner_20260109-074048:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_autonomous_learner_20260109-074048:36:    - jarvis-consciousness-bridge
./docker-compose.yml.backup_autonomous_learner_20260109-074048:728:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_autonomous_learner_20260109-074048:731:    container_name: jarvis-consciousness-bridge
./docker-compose.working.20260118-235132.yml:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.working.20260118-235132.yml:36:    - jarvis-consciousness-bridge
./docker-compose.working.20260118-235132.yml:728:  jarvis-consciousness-bridge:
./docker-compose.working.20260118-235132.yml:731:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup.1768311648:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup.1768311648:37:    - jarvis-consciousness-bridge
./docker-compose.yml.backup.1768311648:682:  jarvis-consciousness-bridge:
./docker-compose.yml.backup.1768311648:685:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.backup.1768311648:686:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup.1768311648:712:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup.1768311648:714:    - jarvis-consciousness-bridge
./docker-compose.yml.backup_20260406_newservices:22:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_20260406_newservices:40:    - jarvis-consciousness-bridge
./docker-compose.yml.backup_20260406_newservices:754:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_20260406_newservices:757:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup_20260406_newservices:840:    - CONSCIOUSNESS_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:193:  jarvis-consciousness-bridge:
./docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:196:    container_name: jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:204:    image: msjarvis-consciousness-bridge:latest
./docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:336:    - jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:368:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:574:    - jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:577:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./hilbert_audit_20260508_193423.log:31:jarvis-consciousness-bridge	Up 21 hours
./last-build-after-woah-llm22.log:8: Image msjarvis-rebuild-jarvis-consciousness-bridge Building 
./last-build-after-woah-llm22.log:466:#34 [jarvis-consciousness-bridge internal] load build context
./docker-compose.yml.broken_spiritual:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.broken_spiritual:38:      - jarvis-consciousness-bridge
./docker-compose.yml.broken_spiritual:725:  jarvis-consciousness-bridge:
./docker-compose.yml.broken_spiritual:728:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.broken_spiritual:1268:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.broken_spiritual:1271:      - jarvis-consciousness-bridge
./restart_unified_msjarvis.sh:7:  jarvis-unified-gateway jarvis-blood-brain-barrier jarvis-consciousness-bridge
./restart_unified_msjarvis.sh:12:  jarvis-blood-brain-barrier jarvis-consciousness-bridge jarvis-unified-gateway
./docker-compose.yml.bak_woah_20260118163402:26:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_woah_20260118163402:50:      - jarvis-consciousness-bridge
./docker-compose.yml.bak_woah_20260118163402:727:  jarvis-consciousness-bridge:
./docker-compose.yml.bak_woah_20260118163402:730:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.bak_woah_20260118163402:731:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak_woah_20260118163402:758:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_woah_20260118163402:760:      - jarvis-consciousness-bridge
./docker-compose-core.yml:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose-core.yml:168:  jarvis-consciousness-bridge:
./docker-compose-core.yml:169:    container_name: jarvis-consciousness-bridge
./docker-compose-core.yml:170:    image: msjarvis-rebuild-jarvis-consciousness-bridge
./docker-compose.yml.20llm.bak:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.20llm.bak:36:    - jarvis-consciousness-bridge
./docker-compose.yml.20llm.bak:722:  jarvis-consciousness-bridge:
./docker-compose.yml.20llm.bak:725:    container_name: jarvis-consciousness-bridge
./logs/ch40_closeout/main_brain.py.pre_otel_cleanup.snapshot.py:128:    "consciousnessbridge": "http://jarvis-consciousness-bridge:8020",
./logs/ch40_closeout/ms_jarvis_unified_gateway.snapshot.py:155:            "consciousness_bridge": os.environ.get("CONSCIOUSNESS_BRIDGE_URL", "http://jarvis-consciousness-bridge:8020"),
./logs/ch40_closeout/ms_jarvis_unified_gateway.snapshot.py:874:    return await _m09_proxy("http://jarvis-consciousness-bridge:8020", True, path, request)
./logs/verifyandtest/verifyandtest_20260423T040042Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":3,"timestamp":"2026-04-23T04:00:42.582847"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260414T235717Z.log:4:{"status":"degraded","systems":{"consciousness_bridge":{"status":"unavailable","url":"http://jarvis-consciousness-bridge:8020","responsive":false},"neurobiological_master":{"status":"unavailable","url":"http://jarvis-neurobiological-master:8018","responsive":false},"i_containers":{"status":"unavailable","url":"http://jarvis-i-containers:8015","responsive":false},"blood_brain_barrier":{"status":"unavailable","url":"http://jarvis-blood-brain-barrier:8016","responsive":false},"qualia_engine":{"status":"unavailable","url":"http://jarvis-qualia-engine:8017","responsive":false}},"total_queries":86,"timestamp":"2026-04-14T23:57:17.621460"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260416T184125Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":5,"timestamp":"2026-04-16T18:41:25.974015"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260415T000059Z.log:4:{"status":"degraded","systems":{"consciousness_bridge":{"status":"unavailable","url":"http://jarvis-consciousness-bridge:8020","responsive":false},"neurobiological_master":{"status":"unavailable","url":"http://jarvis-neurobiological-master:8018","responsive":false},"i_containers":{"status":"unavailable","url":"http://jarvis-i-containers:8015","responsive":false},"blood_brain_barrier":{"status":"unavailable","url":"http://jarvis-blood-brain-barrier:8016","responsive":false},"qualia_engine":{"status":"unavailable","url":"http://jarvis-qualia-engine:8017","responsive":false}},"total_queries":86,"timestamp":"2026-04-15T00:00:59.723657"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260423T001610Z.log:4:{"status":"degraded","systems":{"consciousness_bridge":{"status":"unavailable","url":"http://jarvis-consciousness-bridge:8020","responsive":false},"neurobiological_master":{"status":"unavailable","url":"http://jarvis-neurobiological-master:8018","responsive":false},"i_containers":{"status":"unavailable","url":"http://jarvis-i-containers:8015","responsive":false},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"unavailable","url":"http://jarvis-qualia-engine:8017","responsive":false}},"total_queries":0,"timestamp":"2026-04-23T00:16:10.966406"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260412T123709Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":101,"timestamp":"2026-04-12T12:37:09.090770"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260423T031830Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":5,"timestamp":"2026-04-23T03:18:30.183411"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260416T202233Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":11,"timestamp":"2026-04-16T20:22:33.884099"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260416T201605Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":11,"timestamp":"2026-04-16T20:16:05.575953"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260416T204329Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":17,"timestamp":"2026-04-16T20:43:29.603604"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260416T191413Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":7,"timestamp":"2026-04-16T19:14:14.001920"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260416T195043Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":9,"timestamp":"2026-04-16T19:50:43.522563"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260416T184325Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":5,"timestamp":"2026-04-16T18:43:25.595779"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260416T201920Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":11,"timestamp":"2026-04-16T20:19:20.457767"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260415T001023Z.log:4:{"status":"degraded","systems":{"consciousness_bridge":{"status":"unavailable","url":"http://jarvis-consciousness-bridge:8020","responsive":false},"neurobiological_master":{"status":"unavailable","url":"http://jarvis-neurobiological-master:8018","responsive":false},"i_containers":{"status":"unavailable","url":"http://jarvis-i-containers:8015","responsive":false},"blood_brain_barrier":{"status":"unavailable","url":"http://jarvis-blood-brain-barrier:8016","responsive":false},"qualia_engine":{"status":"unavailable","url":"http://jarvis-qualia-engine:8017","responsive":false}},"total_queries":87,"timestamp":"2026-04-15T00:10:24.225566"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260422T184544Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":55,"timestamp":"2026-04-22T18:45:44.689401"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260414T011115Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"unavailable","url":"http://jarvis-neurobiological-master:8018","responsive":false},"i_containers":{"status":"unavailable","url":"http://jarvis-i-containers:8015","responsive":false},"blood_brain_barrier":{"status":"unavailable","url":"http://jarvis-blood-brain-barrier:8016","responsive":false},"qualia_engine":{"status":"unavailable","url":"http://jarvis-qualia-engine:8017","responsive":false}},"total_queries":11,"timestamp":"2026-04-14T01:11:16.409685"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260416T160245Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":3,"timestamp":"2026-04-16T16:02:45.153622"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260416T204906Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":17,"timestamp":"2026-04-16T20:49:06.667031"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260415T000933Z.log:4:{"status":"degraded","systems":{"consciousness_bridge":{"status":"unavailable","url":"http://jarvis-consciousness-bridge:8020","responsive":false},"neurobiological_master":{"status":"unavailable","url":"http://jarvis-neurobiological-master:8018","responsive":false},"i_containers":{"status":"unavailable","url":"http://jarvis-i-containers:8015","responsive":false},"blood_brain_barrier":{"status":"unavailable","url":"http://jarvis-blood-brain-barrier:8016","responsive":false},"qualia_engine":{"status":"unavailable","url":"http://jarvis-qualia-engine:8017","responsive":false}},"total_queries":87,"timestamp":"2026-04-15T00:09:33.744211"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260404T104850Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":4,"timestamp":"2026-04-04T10:48:50.794989"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260416T231242Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":26,"timestamp":"2026-04-16T23:12:42.115122"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260416T202436Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":11,"timestamp":"2026-04-16T20:24:36.743684"}--- session-sidecar /health (best-effort) ---
./logs/verifyandtest/verifyandtest_20260416T184822Z.log:4:{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","responsive":true},"i_containers":{"status":"healthy","url":"http://jarvis-i-containers:8015","responsive":true},"blood_brain_barrier":{"status":"healthy","url":"http://jarvis-blood-brain-barrier:8016","responsive":true},"qualia_engine":{"status":"healthy","url":"http://jarvis-qualia-engine:8017","responsive":true}},"total_queries":5,"timestamp":"2026-04-16T18:48:22.245895"}--- session-sidecar /health (best-effort) ---
./service_build_matrix.txt:10:jarvis-consciousness-bridge|/home/cakidd/msjarvis-rebuild/services|Dockerfile|-|-
./docker-compose.yml.bak_redis_env_1769196600:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_redis_env_1769196600:34:      - jarvis-consciousness-bridge
./docker-compose.yml.bak_redis_env_1769196600:692:  jarvis-consciousness-bridge:
./docker-compose.yml.bak_redis_env_1769196600:695:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup_20260323_205752:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_20260323_205752:39:    - jarvis-consciousness-bridge
./docker-compose.yml.backup_20260323_205752:658:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_20260323_205752:659:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
./docker-compose.yml.backup_20260323_205752:660:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup_20260318_102158:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_20260318_102158:39:    - jarvis-consciousness-bridge
./docker-compose.yml.backup_20260318_102158:636:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_20260318_102158:637:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
./docker-compose.yml.backup_20260318_102158:638:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak_drop_images:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_drop_images:38:    - jarvis-consciousness-bridge
./docker-compose.yml.bak_drop_images:772:  jarvis-consciousness-bridge:
./docker-compose.yml.bak_drop_images:775:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.bak_drop_images:776:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak_drop_images:803:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_drop_images:806:    - jarvis-consciousness-bridge
./docker-compose.yml.pre_judges:18:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.pre_judges:38:      - jarvis-consciousness-bridge
./docker-compose.yml.pre_judges:727:  jarvis-consciousness-bridge:
./docker-compose.yml.pre_judges:730:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.pre_judges:1271:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8018
./docker-compose.yml.pre_judges:1274:      - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260422_220748:41:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260422_220748:59:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260422_220748:834:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260422_220748:838:    container_name: jarvis-consciousness-bridge
./docker-compose.golden.bak_bbb_uvicorn_fix:35:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.golden.bak_bbb_uvicorn_fix:51:    - jarvis-consciousness-bridge
./docker-compose.golden.bak_bbb_uvicorn_fix:715:  jarvis-consciousness-bridge:
./docker-compose.golden.bak_bbb_uvicorn_fix:718:    container_name: jarvis-consciousness-bridge
./docker-compose.golden.bak_before_python3_cmd_fix:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.golden.bak_before_python3_cmd_fix:34:    - jarvis-consciousness-bridge
./docker-compose.golden.bak_before_python3_cmd_fix:726:  jarvis-consciousness-bridge:
./docker-compose.golden.bak_before_python3_cmd_fix:729:    container_name: jarvis-consciousness-bridge
./neurobiological_brain/pituitary_gland/service/pituitary_gland.py:41:    "http://jarvis-consciousness-bridge:8020",
./neurobiological_brain/pituitary_gland/service/pituitary_gland.py.bak:19:    "http://jarvis-consciousness-bridge:8020",
./docker-compose.yml.bak.20260416-141309:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260416-141309:60:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416-141309:763:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260416-141309:767:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup_20260323_211407:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_20260323_211407:39:    - jarvis-consciousness-bridge
./docker-compose.yml.backup_20260323_211407:658:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_20260323_211407:659:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
./docker-compose.yml.backup_20260323_211407:660:    container_name: jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:193:  jarvis-consciousness-bridge:
./docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:196:    container_name: jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:204:    image: msjarvis-consciousness-bridge:latest
./docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:336:    - jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:368:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:574:    - jarvis-consciousness-bridge
./docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:577:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260416-141316:42:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak.20260416-141316:60:    - jarvis-consciousness-bridge
./docker-compose.yml.bak.20260416-141316:763:  jarvis-consciousness-bridge:
./docker-compose.yml.bak.20260416-141316:767:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup.1768313407:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup.1768313407:37:    - jarvis-consciousness-bridge
./docker-compose.yml.backup.1768313407:686:  jarvis-consciousness-bridge:
./docker-compose.yml.backup.1768313407:689:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.backup.1768313407:690:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup.1768313407:716:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup.1768313407:718:    - jarvis-consciousness-bridge
./docker-compose.yml.bak_ports_20260118163828:26:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_ports_20260118163828:50:      - jarvis-consciousness-bridge
./docker-compose.yml.bak_ports_20260118163828:727:  jarvis-consciousness-bridge:
./docker-compose.yml.bak_ports_20260118163828:730:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.bak_ports_20260118163828:731:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.bak_ports_20260118163828:758:      - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_ports_20260118163828:760:      - jarvis-consciousness-bridge
./docker-compose.yml.chroma-backup-20260114060013:19:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.chroma-backup-20260114060013:37:    - jarvis-consciousness-bridge
./docker-compose.yml.chroma-backup-20260114060013:686:  jarvis-consciousness-bridge:
./docker-compose.yml.chroma-backup-20260114060013:689:    image: msjarvis-consciousness-bridge:latest
./docker-compose.yml.chroma-backup-20260114060013:690:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.chroma-backup-20260114060013:716:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.chroma-backup-20260114060013:718:    - jarvis-consciousness-bridge
./docker-compose.yml.bak_before_unified_fix:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.bak_before_unified_fix:36:    - jarvis-consciousness-bridge
./docker-compose.yml.bak_before_unified_fix:728:  jarvis-consciousness-bridge:
./docker-compose.yml.bak_before_unified_fix:731:    container_name: jarvis-consciousness-bridge
./docker-compose.golden.bak_bbb_clean_proxy:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.golden.bak_bbb_clean_proxy:34:    - jarvis-consciousness-bridge
./docker-compose.golden.bak_bbb_clean_proxy:725:  jarvis-consciousness-bridge:
./docker-compose.golden.bak_bbb_clean_proxy:728:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup_20260318_110927:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_20260318_110927:39:    - jarvis-consciousness-bridge
./docker-compose.yml.backup_20260318_110927:636:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_20260318_110927:637:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
./docker-compose.yml.backup_20260318_110927:638:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.pre_dsn_fix:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.pre_dsn_fix:36:    - jarvis-consciousness-bridge
./docker-compose.yml.pre_dsn_fix:737:  jarvis-consciousness-bridge:
./docker-compose.yml.pre_dsn_fix:740:    container_name: jarvis-consciousness-bridge
./docker-compose.yml.backup_20260318_103829:16:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.yml.backup_20260318_103829:39:    - jarvis-consciousness-bridge
./docker-compose.yml.backup_20260318_103829:636:  jarvis-consciousness-bridge:
./docker-compose.yml.backup_20260318_103829:637:    image: msjarvis-rebuild-jarvis-consciousness-bridge:latest
./docker-compose.yml.backup_20260318_103829:638:    container_name: jarvis-consciousness-bridge
./docker-compose.working.20260119-000202.yml:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.working.20260119-000202.yml:36:    - jarvis-consciousness-bridge
./docker-compose.working.20260119-000202.yml:728:  jarvis-consciousness-bridge:
./docker-compose.working.20260119-000202.yml:731:    container_name: jarvis-consciousness-bridge
./docker-compose.golden.bak_before_bbb_proxy2:18:    - CONSCIOUSNESS_BRIDGE_URL=http://jarvis-consciousness-bridge:8020
./docker-compose.golden.bak_before_bbb_proxy2:34:    - jarvis-consciousness-bridge
./docker-compose.golden.bak_before_bbb_proxy2:726:  jarvis-consciousness-bridge:
./docker-compose.golden.bak_before_bbb_proxy2:729:    container_name: jarvis-consciousness-bridge
services/ms_jarvis_consciousness_unified_bridge.py:211:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/bridge_cross_dgm_10001.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py:252:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/port_9000_69dgm_bridge.py:297:    uvicorn.run(
services/bridge_cross_dgm_10008.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py.before_judge_fix:3:from dynamic_port_service import DynamicPortService
services/ms_jarvis_consciousness_bridge.py.before_judge_fix:19:Integrates multi-agent consciousness with dynamic port scheduling
services/ms_jarvis_consciousness_bridge.py.before_judge_fix:23:# Dynamic Port Integration
services/ms_jarvis_consciousness_bridge.py.before_judge_fix:28:# Initialize dynamic port service
services/ms_jarvis_consciousness_bridge.py.before_judge_fix:29:port_service = DynamicPortService()
services/ms_jarvis_consciousness_bridge.py.before_judge_fix:30:port_service.register_service({
services/ms_jarvis_consciousness_bridge.py.before_judge_fix:168:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_judge_fix:172:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py.before_judge_fix:186:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_judge_fix:190:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py.before_judge_fix:198:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_judge_fix:238:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_judge_fix:249:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port}")
services/ms_jarvis_consciousness_bridge.py.before_judge_fix:250:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/bridge_cross_dgm_10054.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_unified_rag_bridge.py.bak-msallis:294:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8092)))
services/bridge_manifest_FULL_BACKUP.csv:138:bridge_cross_dgm.py,ms_jarvis_main_gateway,dynamic_port_service,9174
services/bridge_manifest_FULL_BACKUP.csv:139:bridge_cross_dgm.py,ms_jarvis_main_gateway,dynamic_port_service_enhanced,9414
services/msjarvisconsciousnessbridge_ACTUAL.py.bak-msallis:129:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/port_9000_69dgm_bridge.py.bak-msallis:297:    uvicorn.run(
services/msjarvisconsciousnessbridge_ACTUAL.py:132:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/woah_qualia_bridge.py:38:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8052)))
services/bridge_cross_dgm_10014.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py.bak-msallis:4:Integrates multi-agent consciousness with dynamic port scheduling
services/ms_jarvis_consciousness_bridge.py.bak-msallis:18:from dynamic_port_service import DynamicPortService
services/ms_jarvis_consciousness_bridge.py.bak-msallis:30:# Dynamic port + discovery
services/ms_jarvis_consciousness_bridge.py.bak-msallis:33:# Initialize dynamic port service
services/ms_jarvis_consciousness_bridge.py.bak-msallis:34:port_service = DynamicPortService()
services/ms_jarvis_consciousness_bridge.py.bak-msallis:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/ms_jarvis_consciousness_bridge.py.bak-msallis:37:port_service.register_service()
services/ms_jarvis_consciousness_bridge.py.bak-msallis:48:        port=port_service.port,
services/ms_jarvis_consciousness_bridge.py.bak-msallis:176:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py.bak-msallis:193:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py.bak-msallis:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/ms_jarvis_consciousness_bridge.py.bak-msallis:255:        f"(type={type(port_service.port)})"
services/ms_jarvis_consciousness_bridge.py.bak-msallis:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/bridge_cross_dgm_10005.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/bridge_cross_dgm_10032.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py.before_mamma_protocol:851:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/bridge_cross_dgm_10010.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/bridge_cross_dgm_10038.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10064.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py.backup_before_hierarchy:936:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/bridge_cross_dgm_10017.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/bridge_cross_dgm_10028.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.backup_vocabulary_cleanup:850:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/bridge_cross_dgm_10033.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10050.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.bak-msallis:9:Integrates multi-agent consciousness with dynamic port scheduling
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.bak-msallis:26:# Dynamic Port Integration (use services_old)
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.bak-msallis:28:from services_old.dynamic_port_service import DynamicPortService
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.bak-msallis:34:# Initialize dynamic port service and register this bridge
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.bak-msallis:35:port_service = DynamicPortService()
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.bak-msallis:36:bridge_port = port_service.find_free_port()
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.bak-msallis:39:    port_service.register_service(bridge_port, health_endpoint="/health")
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.bak-msallis:41:    logger.warning(f"DynamicPortService register_service failed for consciousness bridge: {e}")
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.bak-msallis:276:    uvicorn.run(app, host="127.0.0.1", port=bridge_port)
services/rag/gbim_gis_bridge.py:44:    uvicorn.run(app, host="127.0.0.1", port=port)
services/bridge_cross_dgm_10031.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py.backup_pre_location_integration:645:    uvicorn.run(app, host="0.0.0.0", port=8004, log_level="info")
services/bridge_cross_dgm_10023.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/bridge_cross_dgm.py:87:    uvicorn.run(app, host="127.0.0.1", port=PORT)
services/PORT_SEG_ac:10:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_llm_bridge.py:        self.port = port_service.port
services/PORT_SEG_ac:11:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_llm_bridge.py:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/PORT_SEG_ac:13:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_llm_bridge_simple.py:    uvicorn.run(app, host="0.0.0.0", port=port)
services/PORT_SEG_ac:74:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_rag_bridge.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/bridge_manifest_batch2.csv:8:bridge_cross_dgm.py,ms_jarvis_main_gateway,dynamic_port_service,9174
services/bridge_manifest_batch2.csv:9:bridge_cross_dgm.py,ms_jarvis_main_gateway,dynamic_port_service_enhanced,9414
services/bridge_cross_dgm_10009.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/bridge_cross_dgm_10006.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py.bak-msallis:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py.bak-msallis:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py.bak-msallis:30:# Dynamic port + discovery
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py.bak-msallis:33:# Initialize dynamic port service
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py.bak-msallis:34:port_service = DynamicPortService()
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py.bak-msallis:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py.bak-msallis:37:port_service.register_service()
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py.bak-msallis:48:        port=port_service.port,
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py.bak-msallis:176:        "port": port_service.port,
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py.bak-msallis:193:        "port": port_service.port,
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py.bak-msallis:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py.bak-msallis:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py.bak-msallis:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/woah_algorithms/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:18:from neurobiologicalbrain.i_containers.service.dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:30:# Dynamic port + discovery
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:33:# Initialize dynamic port service
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:34:port_service = DynamicPortService()
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:37:port_service.register_service()
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:48:        port=port_service.port,
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:176:        "port": port_service.port,
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:193:        "port": port_service.port,
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/i_containers/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:18:from neurobiologicalbrain.i_containers.service.dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/consciousness_bridge/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py.bak-msallis:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py.bak-msallis:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py.bak-msallis:30:# Dynamic port + discovery
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py.bak-msallis:33:# Initialize dynamic port service
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py.bak-msallis:34:port_service = DynamicPortService()
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py.bak-msallis:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py.bak-msallis:37:port_service.register_service()
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py.bak-msallis:48:        port=port_service.port,
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py.bak-msallis:176:        "port": port_service.port,
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py.bak-msallis:193:        "port": port_service.port,
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py.bak-msallis:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py.bak-msallis:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py.bak-msallis:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/spiritual_root/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py.bak-msallis:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py.bak-msallis:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py.bak-msallis:30:# Dynamic port + discovery
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py.bak-msallis:33:# Initialize dynamic port service
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py.bak-msallis:34:port_service = DynamicPortService()
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py.bak-msallis:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py.bak-msallis:37:port_service.register_service()
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py.bak-msallis:48:        port=port_service.port,
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py.bak-msallis:176:        "port": port_service.port,
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py.bak-msallis:193:        "port": port_service.port,
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py.bak-msallis:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py.bak-msallis:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py.bak-msallis:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/prefrontal_cortex/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py.bak-msallis:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py.bak-msallis:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py.bak-msallis:30:# Dynamic port + discovery
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py.bak-msallis:33:# Initialize dynamic port service
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py.bak-msallis:34:port_service = DynamicPortService()
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py.bak-msallis:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py.bak-msallis:37:port_service.register_service()
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py.bak-msallis:48:        port=port_service.port,
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py.bak-msallis:176:        "port": port_service.port,
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py.bak-msallis:193:        "port": port_service.port,
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py.bak-msallis:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py.bak-msallis:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py.bak-msallis:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/pituitary_gland/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py.bak-msallis:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py.bak-msallis:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py.bak-msallis:30:# Dynamic port + discovery
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py.bak-msallis:33:# Initialize dynamic port service
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py.bak-msallis:34:port_service = DynamicPortService()
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py.bak-msallis:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py.bak-msallis:37:port_service.register_service()
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py.bak-msallis:48:        port=port_service.port,
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py.bak-msallis:176:        "port": port_service.port,
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py.bak-msallis:193:        "port": port_service.port,
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py.bak-msallis:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py.bak-msallis:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py.bak-msallis:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/subconscious/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py.bak-msallis:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py.bak-msallis:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py.bak-msallis:30:# Dynamic port + discovery
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py.bak-msallis:33:# Initialize dynamic port service
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py.bak-msallis:34:port_service = DynamicPortService()
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py.bak-msallis:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py.bak-msallis:37:port_service.register_service()
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py.bak-msallis:48:        port=port_service.port,
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py.bak-msallis:176:        "port": port_service.port,
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py.bak-msallis:193:        "port": port_service.port,
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py.bak-msallis:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py.bak-msallis:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py.bak-msallis:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/mother_carrie_protocols/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py.bak-msallis:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py.bak-msallis:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py.bak-msallis:30:# Dynamic port + discovery
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py.bak-msallis:33:# Initialize dynamic port service
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py.bak-msallis:34:port_service = DynamicPortService()
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py.bak-msallis:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py.bak-msallis:37:port_service.register_service()
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py.bak-msallis:48:        port=port_service.port,
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py.bak-msallis:176:        "port": port_service.port,
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py.bak-msallis:193:        "port": port_service.port,
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py.bak-msallis:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py.bak-msallis:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py.bak-msallis:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/spiritual_maternal_integration/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py.bak-msallis:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py.bak-msallis:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py.bak-msallis:30:# Dynamic port + discovery
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py.bak-msallis:33:# Initialize dynamic port service
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py.bak-msallis:34:port_service = DynamicPortService()
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py.bak-msallis:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py.bak-msallis:37:port_service.register_service()
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py.bak-msallis:48:        port=port_service.port,
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py.bak-msallis:176:        "port": port_service.port,
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py.bak-msallis:193:        "port": port_service.port,
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py.bak-msallis:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py.bak-msallis:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py.bak-msallis:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/heteroglobulin_transport/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:30:# Dynamic port + discovery
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:33:# Initialize dynamic port service
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:34:port_service = DynamicPortService()
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:37:port_service.register_service()
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:48:        port=port_service.port,
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:176:        "port": port_service.port,
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:193:        "port": port_service.port,
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py.bak-msallis:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/neurobiologicalbrain/consciousness_containers/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/bridge_cross_dgm_10055.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10036.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10053.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/judge_to_pituitary_bridge.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10041.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/jarvis-69dgm-bridge_jarvis-fractal-consciousness_baseline.py:20:    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("SERVICE_PORT", 8018)))
services/bridge_cross_dgm_10060.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/llm_bridge_main.py.bak-msallis:109:    uvicorn.run(app, host="127.0.0.1", port=port)
services/ms_jarvis_llm_bridge_simple.py:93:    uvicorn.run(app, host="0.0.0.0", port=port)
services/bridge_cross_dgm_10013.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py.before_complete_architecture:3:from dynamic_port_service import DynamicPortService
services/ms_jarvis_consciousness_bridge.py.before_complete_architecture:19:Integrates multi-agent consciousness with dynamic port scheduling
services/ms_jarvis_consciousness_bridge.py.before_complete_architecture:23:# Dynamic Port Integration
services/ms_jarvis_consciousness_bridge.py.before_complete_architecture:28:# Initialize dynamic port service
services/ms_jarvis_consciousness_bridge.py.before_complete_architecture:29:port_service = DynamicPortService()
services/ms_jarvis_consciousness_bridge.py.before_complete_architecture:30:port_service.register_service({
services/ms_jarvis_consciousness_bridge.py.before_complete_architecture:168:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_complete_architecture:172:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py.before_complete_architecture:186:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_complete_architecture:190:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py.before_complete_architecture:198:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_complete_architecture:238:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_complete_architecture:249:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port}")
services/ms_jarvis_consciousness_bridge.py.before_complete_architecture:250:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/PORT_AUDIT_SEG_ac:160:/home/ms-jarvis/msjarvis-rebuild/services/judge_to_pituitary_bridge.py:51:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/PORT_AUDIT_SEG_ac:162:/home/ms-jarvis/msjarvis-rebuild/services/llm_bridge_main.py:10:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/ms_jarvis_consciousness_bridge.py.before_persona_fix:883:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/msjarvisconsciousnessbridge.py.bak-msallis:115:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/bridge_cross_dgm_10020.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/bridge_manifest_services_only.csv:108:bridge_cross_dgm.py,ms_jarvis_main_gateway,dynamic_port_service,9174
services/bridge_manifest_services_only.csv:109:bridge_cross_dgm.py,ms_jarvis_main_gateway,dynamic_port_service_enhanced,9414
services/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py:211:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/PORT_SEG_ad:27:/home/ms-jarvis/msjarvis-rebuild/services/woah_qualia_bridge.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
services/ms_jarvis_consciousness_bridge.py.backup_1759895250:807:    uvicorn.run(app, host="0.0.0.0", port=8004, log_level="info")
services/bridge_cross_dgm_10067.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py:211:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/bridge_cross_dgm_10040.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10025.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/main.py.bak_enable_llmbridge_20251212_233317:768:    uvicorn.run(app, host="0.0.0.0", port=8050)
services/bridge_cross_dgm_10056.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_llm_bridge_simple_9303.log:6:INFO:     Uvicorn running on http://0.0.0.0:8004 (Press CTRL+C to quit)
services/python/consciousness_bridge.py.broken_backup:3:Ms. Jarvis Consciousness Bridge - Dynamic Port Version
services/python/consciousness_bridge.py.broken_backup:9:# Get dynamic port from environment
services/python/consciousness_bridge.py.broken_backup:19:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT, log_level="info")
services/python/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
services/bridge/bridge_cross_dgm.py:87:    uvicorn.run(app, host="127.0.0.1", port=PORT)
services/bridge/dgm_orchestrator.py:137:    uvicorn.run(app, host="127.0.0.1", port=9999)
services/bridge/dgm_bridge.py:243:    uvicorn.run("dgm_bridge:app", host="127.0.0.1", port=SERVICE_PORT)
services/bridge/dgm_orchestrator.py.bak-msallis:137:    uvicorn.run(app, host="127.0.0.1", port=9999)
services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery:7:Ms. Jarvis LLM Bridge - Language Model Gateway with Dynamic Port Scheduling
services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery:19:# Dynamic Port Integration
services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery:20:from dynamic_port_service import DynamicPortService
services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery:26:# Initialize dynamic port service
services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery:27:port_service = DynamicPortService()
services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery:28:port_service.register_service({
services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery:54:        self.port = port_service.port
services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery:103:    port_service.heartbeat()
services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery:118:    port_service.heartbeat()
services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery:131:    port_service.heartbeat()
services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery:150:    port_service.heartbeat()
services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery:157:    port_service.heartbeat()
services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery:170:    logger.info(f"🤖 Starting LLM Bridge on dynamically allocated port {port_service.port}")
services/ms_jarvis_llm_bridge.py.pre_dynamic_discovery:172:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/bridge_cross_dgm_10026.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10061.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10063.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10044.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/jarvis-agents-service_ms_jarvis_consciousness_unified_bridge.py:211:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/ms_jarvis_consciousness_bridge.py.working_backup:936:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/ms_jarvis_consciousness_bridge.py.before_prompt_fix:851:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/bridge_cross_dgm_10046.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/PORT_SEG_ab:70:/home/ms-jarvis/msjarvis-rebuild/services/judge_to_pituitary_bridge.py:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/PORT_SEG_ab:72:/home/ms-jarvis/msjarvis-rebuild/services/llm_bridge_main.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/PORT_SEG_ab:134:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_bridge_enhanced.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/PORT_SEG_ab:135:/home/ms-jarvis/msjarvis-rebuild/services/msjarvisconsciousnessbridge.py:    uvicorn.run(app, host="0.0.0.0", port=8008)
services/PORT_SEG_ab:136:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_bridge.py:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/PORT_SEG_ab:142:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_unified_bridge.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/ms_jarvis_consciousness_bridge_enhanced.py.bak-msallis:168:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/bridge_cross_dgm_10048.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py.phase1_working:903:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/bridge_cross_dgm_10039.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_llm_bridge.py.broken:101:    uvicorn.run(app, host="0.0.0.0", port=port)
services/ms_jarvis_consciousness_bridge.py.safe_backup:851:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/bridge_cross_dgm_10029.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/dgm_bridge.py:243:    uvicorn.run("dgm_bridge:app", host="127.0.0.1", port=SERVICE_PORT)
services/main.py.bak_before_bridge_20251212_232206:768:    uvicorn.run(app, host="0.0.0.0", port=8050)
services/bridge_cross_dgm_10012.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy:3:from dynamic_port_service import DynamicPortService
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy:19:Integrates multi-agent consciousness with dynamic port scheduling
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy:23:# Dynamic Port Integration
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy:28:# Initialize dynamic port service
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy:29:port_service = DynamicPortService()
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy:30:port_service.register_service({
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy:231:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy:235:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy:249:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy:253:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy:261:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy:301:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy:312:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port}")
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm_hierarchy:313:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/ms_jarvis_consciousness_bridge.py.before_final_fix:8:Integrates multi-agent consciousness with dynamic port scheduling
services/ms_jarvis_consciousness_bridge.py.before_final_fix:22:# Dynamic Port Integration
services/ms_jarvis_consciousness_bridge.py.before_final_fix:23:from dynamic_port_service import DynamicPortService
services/ms_jarvis_consciousness_bridge.py.before_final_fix:29:# Initialize dynamic port service
services/ms_jarvis_consciousness_bridge.py.before_final_fix:30:port_service = DynamicPortService()
services/ms_jarvis_consciousness_bridge.py.before_final_fix:31:port_service.register_service({
services/ms_jarvis_consciousness_bridge.py.before_final_fix:61:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_final_fix:65:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py.before_final_fix:78:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_final_fix:82:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py.before_final_fix:89:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_final_fix:126:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_final_fix:136:    logger.info(f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port}")
services/ms_jarvis_consciousness_bridge.py.before_final_fix:137:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/bridge_cross_dgm_10034.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py.backup_1760220435:807:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/bridge_cross_dgm_10047.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10018.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/bridge_cross_dgm_10030.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10007.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/bridge_cross_dgm_10002.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/bridge_cross_dgm_10065.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10062.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
services/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
services/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
services/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
services/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
services/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
services/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
services/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
services/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
services/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
services/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
services/bridge_cross_dgm_10027.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10015.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/main.py.bak_enable_llmbridge_20251212_233118:768:    uvicorn.run(app, host="0.0.0.0", port=8050)
services/bridge_cross_dgm_10003.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/main.py.bak_before_bridge_20251212_232349:768:    uvicorn.run(app, host="0.0.0.0", port=8050)
services/ms_jarvis_consciousness_bridge.py.before_small_models:894:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/bridge_cross_dgm_10045.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10059.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_llm_bridge.py.bak-msallis:22:# Dynamic Port Integration (used only to hold port; no register_service dict call)
services/ms_jarvis_llm_bridge.py.bak-msallis:23:from dynamic_port_service import DynamicPortService
services/ms_jarvis_llm_bridge.py.bak-msallis:30:port_service = DynamicPortService()
services/ms_jarvis_llm_bridge.py.bak-msallis:31:port_service.port = int(os.getenv("SERVICE_PORT", "8006"))
services/ms_jarvis_llm_bridge.py.bak-msallis:60:        self.port = port_service.port
services/ms_jarvis_llm_bridge.py.bak-msallis:314:    logger.info(f"🤖 Starting LLM Bridge on fixed port {port_service.port}")
services/ms_jarvis_llm_bridge.py.bak-msallis:317:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/bridge_cross_dgm_10058.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/PORT_AUDIT_SEG_ad:38:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_bridge_enhanced.py:168:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/PORT_AUDIT_SEG_ad:39:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_bridge.py:237:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/PORT_AUDIT_SEG_ad:40:/home/ms-jarvis/msjarvis-rebuild/services/msjarvisconsciousnessbridge.py:100:    uvicorn.run(app, host="0.0.0.0", port=8008)
services/PORT_AUDIT_SEG_ad:46:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_unified_bridge.py:211:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/PORT_AUDIT_SEG_ad:117:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_llm_bridge.py:55:        self.port = port_service.port
services/PORT_AUDIT_SEG_ad:118:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_llm_bridge.py:173:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/PORT_AUDIT_SEG_ad:121:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_llm_bridge_simple.py:93:    uvicorn.run(app, host="0.0.0.0", port=port)
services/PORT_AUDIT_SEG_ad:183:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_rag_bridge.py:278:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/jarvis-neurobiological-master_ms_jarvis_consciousness_unified_bridge.py:211:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/ms_jarvis_llm_bridge_9908.log:4:    port_service.register_service({
services/ms_jarvis_llm_bridge_9908.log:6:AttributeError: 'DynamicPortService' object has no attribute 'register_service'
services/bridge_cross_dgm_10042.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py.pre_agent_identity:892:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/bridge_cross_dgm_10051.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10057.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/msjarvisconsciousnessbridge.py.bak.20260507-222706:115:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/bridge_cross_dgm_10069.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/PORT_AUDIT_SEG_ae:154:/home/ms-jarvis/msjarvis-rebuild/services/woah_qualia_bridge.py:32:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
services/bridge_cross_dgm_10066.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge_enhanced.py:168:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/ms_jarvis_consciousness_bridge_9188.log:4:    port_service.register_service({
services/ms_jarvis_consciousness_bridge_9188.log:6:AttributeError: 'DynamicPortService' object has no attribute 'register_service'
services/dgm_bridge.log:4:INFO:     Uvicorn running on http://0.0.0.0:9479 (Press CTRL+C to quit)
services/bridge_cross_dgm_10019.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/bridge_manifest.csv:108:bridge_cross_dgm.py,ms_jarvis_main_gateway,dynamic_port_service,9174
services/bridge_manifest.csv:109:bridge_cross_dgm.py,ms_jarvis_main_gateway,dynamic_port_service_enhanced,9414
services/ms_jarvis_consciousness_bridge.py.backup_pre_fixes:851:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/PORTS_REGISTRY_RAW.txt:270:/home/ms-jarvis/msjarvis-rebuild/services/judge_to_pituitary_bridge.py:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/PORTS_REGISTRY_RAW.txt:272:/home/ms-jarvis/msjarvis-rebuild/services/llm_bridge_main.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/PORTS_REGISTRY_RAW.txt:334:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_bridge_enhanced.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/PORTS_REGISTRY_RAW.txt:335:/home/ms-jarvis/msjarvis-rebuild/services/msjarvisconsciousnessbridge.py:    uvicorn.run(app, host="0.0.0.0", port=8008)
services/PORTS_REGISTRY_RAW.txt:336:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_bridge.py:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/PORTS_REGISTRY_RAW.txt:342:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_unified_bridge.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/PORTS_REGISTRY_RAW.txt:410:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_llm_bridge.py:        self.port = port_service.port
services/PORTS_REGISTRY_RAW.txt:411:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_llm_bridge.py:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/PORTS_REGISTRY_RAW.txt:413:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_llm_bridge_simple.py:    uvicorn.run(app, host="0.0.0.0", port=port)
services/PORTS_REGISTRY_RAW.txt:474:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_rag_bridge.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/PORTS_REGISTRY_RAW.txt:627:/home/ms-jarvis/msjarvis-rebuild/services/woah_qualia_bridge.py:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
services/bridge_cross_dgm_10004.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/bridge_cross_dgm_10035.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10052.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery:8:Integrates multi-agent consciousness with dynamic port scheduling
services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery:22:# Dynamic Port Integration
services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery:23:from dynamic_port_service import DynamicPortService
services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery:29:# Initialize dynamic port service
services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery:30:port_service = DynamicPortService()
services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery:31:port_service.register_service({
services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery:160:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery:164:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery:177:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery:181:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery:188:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery:225:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery:235:    logger.info(f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port}")
services/ms_jarvis_consciousness_bridge.py.pre_dynamic_discovery:236:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/bridge_cross_dgm_10068.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10049.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_llm_bridge_simple.py.bak-msallis:93:    uvicorn.run(app, host="0.0.0.0", port=port)
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM_9327.log:4:    port_service.register_service({
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM_9327.log:6:AttributeError: 'DynamicPortService' object has no attribute 'register_service'
services/bridge_cross_dgm_10024.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/bridge_cross_dgm_10011.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/msjarvisconsciousnessbridge.py:115:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/bridge_cross_dgm_10037.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_llm_bridge.py:22:# Dynamic Port Integration (used only to hold port; no register_service dict call)
services/ms_jarvis_llm_bridge.py:23:from dynamic_port_service import DynamicPortService
services/ms_jarvis_llm_bridge.py:30:port_service = DynamicPortService()
services/ms_jarvis_llm_bridge.py:31:port_service.port = int(os.getenv("SERVICE_PORT", "8006"))
services/ms_jarvis_llm_bridge.py:60:        self.port = port_service.port
services/ms_jarvis_llm_bridge.py:314:    logger.info(f"🤖 Starting LLM Bridge on fixed port {port_service.port}")
services/ms_jarvis_llm_bridge.py:317:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/msjarvisconsciousnessbridge.py.FULL_BACKUP_BEFORE_BRIDGE_RESET:11:    uvicorn.run(app, host="0.0.0.0", port=8020)
services/bridge_manifest_with_utilities_backup.csv:138:bridge_cross_dgm.py,ms_jarvis_main_gateway,dynamic_port_service,9174
services/bridge_manifest_with_utilities_backup.csv:139:bridge_cross_dgm.py,ms_jarvis_main_gateway,dynamic_port_service_enhanced,9414
services/bridge_cross_dgm_10016.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py.backup_before_22llm:905:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/PORT_AUDIT_RAW.txt:560:/home/ms-jarvis/msjarvis-rebuild/services/judge_to_pituitary_bridge.py:51:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/PORT_AUDIT_RAW.txt:562:/home/ms-jarvis/msjarvis-rebuild/services/llm_bridge_main.py:10:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/PORT_AUDIT_RAW.txt:638:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_bridge_enhanced.py:168:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/PORT_AUDIT_RAW.txt:639:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_bridge.py:237:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/PORT_AUDIT_RAW.txt:640:/home/ms-jarvis/msjarvis-rebuild/services/msjarvisconsciousnessbridge.py:100:    uvicorn.run(app, host="0.0.0.0", port=8008)
services/PORT_AUDIT_RAW.txt:646:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_consciousness_unified_bridge.py:211:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/PORT_AUDIT_RAW.txt:717:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_llm_bridge.py:55:        self.port = port_service.port
services/PORT_AUDIT_RAW.txt:718:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_llm_bridge.py:173:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/PORT_AUDIT_RAW.txt:721:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_llm_bridge_simple.py:93:    uvicorn.run(app, host="0.0.0.0", port=port)
services/PORT_AUDIT_RAW.txt:783:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_unified_rag_bridge.py:278:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/PORT_AUDIT_RAW.txt:954:/home/ms-jarvis/msjarvis-rebuild/services/woah_qualia_bridge.py:32:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8000)))
services/gbim_gis_bridge.py:44:    uvicorn.run(app, host="127.0.0.1", port=port)
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:9:Integrates multi-agent consciousness with dynamic port scheduling
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:26:# Dynamic Port Integration (use services_old)
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:28:from services_old.dynamic_port_service import DynamicPortService
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:34:# Initialize dynamic port service and register this bridge
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:35:port_service = DynamicPortService()
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:36:bridge_port = port_service.find_free_port()
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:39:    port_service.register_service(bridge_port, health_endpoint="/health")
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:41:    logger.warning(f"DynamicPortService register_service failed for consciousness bridge: {e}")
services/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py:276:    uvicorn.run(app, host="127.0.0.1", port=bridge_port)
services/bridge_manifest_priority_services.csv:38:bridge_cross_dgm.py,ms_jarvis_main_gateway,dynamic_port_service,9174
services/bridge_manifest_priority_services.csv:39:bridge_cross_dgm.py,ms_jarvis_main_gateway,dynamic_port_service_enhanced,9414
services/ms_jarvis_unified_rag_bridge.py:294:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8092)))
services/msjarvisconsciousnessbridge_ACTUAL.py.bak.1780325456:129:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/llm_bridge_main.py:109:    uvicorn.run(app, host="127.0.0.1", port=port)
services/ms_jarvis_consciousness_bridge.py.backup_1759895606:807:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/ms_jarvis_consciousness_bridge.py.pre_identity_integration:883:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/jarvis-swarm-intelligence_ms_jarvis_consciousness_unified_bridge.py:211:    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVICE_PORT", 8018)))
services/bridge_cross_dgm_10043.py:51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py.original:853:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/bridge_cross_dgm_10022.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
services/ms_jarvis_consciousness_bridge.py.before_theology:645:    uvicorn.run(app, host="0.0.0.0", port=8018, log_level="info")
services/ms_jarvis_consciousness_bridge.py.before_rag_web:828:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
services/RESTORATION_CERTIFICATE.txt:43:4. ✅ Created Python-JavaScript bridge with dynamic ports
services/ms_jarvis_consciousness_bridge.py.before_full_integration:8:Integrates multi-agent consciousness with dynamic port scheduling
services/ms_jarvis_consciousness_bridge.py.before_full_integration:22:# Dynamic Port Integration
services/ms_jarvis_consciousness_bridge.py.before_full_integration:23:from dynamic_port_service import DynamicPortService
services/ms_jarvis_consciousness_bridge.py.before_full_integration:29:# Initialize dynamic port service
services/ms_jarvis_consciousness_bridge.py.before_full_integration:30:port_service = DynamicPortService()
services/ms_jarvis_consciousness_bridge.py.before_full_integration:31:port_service.register_service({
services/ms_jarvis_consciousness_bridge.py.before_full_integration:61:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_full_integration:65:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py.before_full_integration:78:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_full_integration:82:        "port": port_service.port,
services/ms_jarvis_consciousness_bridge.py.before_full_integration:89:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_full_integration:126:    port_service.heartbeat()
services/ms_jarvis_consciousness_bridge.py.before_full_integration:136:    logger.info(f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port}")
services/ms_jarvis_consciousness_bridge.py.before_full_integration:137:    uvicorn.run(app, host="0.0.0.0", port=port_service.port)
services/bridge_cross_dgm_10021.py:210:    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="error")
neurobiological_brain/woah_algorithms/service/consciousness_bridge.py:13:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT, log_level="info")
neurobiological_brain/woah_algorithms/service/Dockerfile:12:# Redis client for dynamic_port_service / consciousness_bridge
neurobiological_brain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:30:            port=int(port_service.port),
neurobiological_brain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:45:# Dynamic port + discovery
neurobiological_brain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:48:# Initialize dynamic port service
neurobiological_brain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:49:port_service = DynamicPortService()
neurobiological_brain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:168:        "port": port_service.port,
neurobiological_brain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:185:        "port": port_service.port,
neurobiological_brain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:246:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:247:        f"(type={type(port_service.port)})"
neurobiological_brain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:254:            port=int(port_service.port),
neurobiological_brain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:259:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:18:from neurobiologicalbrain.i_containers.service.dynamic_port_service import DynamicPortService
neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_bridge/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/i_containers/service/consciousness_bridge.py:13:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT, log_level="info")
neurobiological_brain/i_containers/service/Dockerfile:10:# Ensure Flask is available for dynamic_port_service / consciousness_bridge
neurobiological_brain/i_containers/service/Dockerfile:13:# Redis client for dynamic_port_service / consciousness_bridge
neurobiological_brain/i_containers/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/i_containers/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/i_containers/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/i_containers/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/i_containers/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/i_containers/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/i_containers/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/i_containers/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
neurobiological_brain/i_containers/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
neurobiological_brain/i_containers/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
neurobiological_brain/i_containers/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/i_containers/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
neurobiological_brain/i_containers/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/i_containers/service/msjarvisconsciousnessbridge.py:115:    uvicorn.run(app, host="0.0.0.0", port=8020, log_level="info")
neurobiological_brain/consciousness_bridge/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
neurobiological_brain/spiritual_root/service/consciousness_bridge.py:13:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT, log_level="info")
neurobiological_brain/spiritual_root/service/Dockerfile:12:# Ensure Flask is available for dynamic_port_service / consciousness_bridge
neurobiological_brain/spiritual_root/service/Dockerfile:15:# Redis client for dynamic_port_service / consciousness_bridge
neurobiological_brain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:36:# # (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:165:        "port": port_service.port,
neurobiological_brain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:182:        "port": port_service.port,
neurobiological_brain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:243:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:244:        f"(type={type(port_service.port)})"
neurobiological_brain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:246:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/prefrontal_cortex/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
neurobiological_brain/prefrontal_cortex/service/Dockerfile:8:# Ensure Flask is available for dynamic_port_service / consciousness_bridge
neurobiological_brain/prefrontal_cortex/service/Dockerfile:11:# Redis client for dynamic_port_service / consciousness_bridge
neurobiological_brain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:234:    uvicorn.run(app, host="0.0.0.0", port=FIXED_PORT)
neurobiological_brain/pituitary_gland/service/consciousness_bridge.py:13:    uvicorn.run(app, host="127.0.0.1", port=SERVICE_PORT, log_level="info")
neurobiological_brain/pituitary_gland/service/Dockerfile:10:# Ensure Flask is available for dynamic_port_service / consciousness_bridge
neurobiological_brain/pituitary_gland/service/Dockerfile:13:# Redis client for dynamic_port_service / consciousness_bridge
neurobiological_brain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:36:# # (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:165:        "port": port_service.port,
neurobiological_brain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:182:        "port": port_service.port,
neurobiological_brain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:243:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:244:        f"(type={type(port_service.port)})"
neurobiological_brain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:246:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/subconscious/service/consciousness_bridge.py:13:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT, log_level="info")
neurobiological_brain/subconscious/service/Dockerfile:12:# Ensure Flask is available for dynamic_port_service / consciousness_bridge
neurobiological_brain/subconscious/service/Dockerfile:15:# Redis client for dynamic_port_service / consciousness_bridge
neurobiological_brain/subconscious/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/subconscious/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/subconscious/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/subconscious/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/subconscious/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/subconscious/service/ms_jarvis_consciousness_bridge.py:36:# # (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/subconscious/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/subconscious/service/ms_jarvis_consciousness_bridge.py:165:        "port": port_service.port,
neurobiological_brain/subconscious/service/ms_jarvis_consciousness_bridge.py:182:        "port": port_service.port,
neurobiological_brain/subconscious/service/ms_jarvis_consciousness_bridge.py:243:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/subconscious/service/ms_jarvis_consciousness_bridge.py:244:        f"(type={type(port_service.port)})"
neurobiological_brain/subconscious/service/ms_jarvis_consciousness_bridge.py:246:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/mother_carrie_protocols/service/consciousness_bridge.py:13:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT, log_level="info")
neurobiological_brain/mother_carrie_protocols/service/Dockerfile:10:# Ensure Flask is available for dynamic_port_service / consciousness_bridge
neurobiological_brain/mother_carrie_protocols/service/Dockerfile:13:# Redis client for dynamic_port_service / consciousness_bridge
neurobiological_brain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
neurobiological_brain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
neurobiological_brain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
neurobiological_brain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
neurobiological_brain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/spiritual_maternal_integration/service/consciousness_bridge.py:13:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT, log_level="info")
neurobiological_brain/spiritual_maternal_integration/service/Dockerfile:10:# Ensure Flask is available for dynamic_port_service / consciousness_bridge
neurobiological_brain/spiritual_maternal_integration/service/Dockerfile:13:# Redis client for dynamic_port_service / consciousness_bridge
neurobiological_brain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
neurobiological_brain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
neurobiological_brain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
neurobiological_brain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
neurobiological_brain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/heteroglobulin_transport/service/consciousness_bridge.py:13:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT, log_level="info")
neurobiological_brain/heteroglobulin_transport/service/Dockerfile:10:# Ensure Flask is available for dynamic_port_service / consciousness_bridge
neurobiological_brain/heteroglobulin_transport/service/Dockerfile:13:# Redis client for dynamic_port_service / consciousness_bridge
neurobiological_brain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:36:# (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:48:        port=port_service.port,
neurobiological_brain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:176:        "port": port_service.port,
neurobiological_brain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:193:        "port": port_service.port,
neurobiological_brain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:254:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:255:        f"(type={type(port_service.port)})"
neurobiological_brain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:257:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
neurobiological_brain/blood_brain_barrier/service/Dockerfile:10:# Ensure Flask is available for dynamic_port_service / consciousness_bridge
neurobiological_brain/blood_brain_barrier/service/Dockerfile:13:# Redis client for dynamic_port_service / consciousness_bridge
neurobiological_brain/consciousness_containers/service/consciousness_bridge.py:13:    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT, log_level="info")
neurobiological_brain/consciousness_containers/service/Dockerfile:12:# Ensure Flask is available for dynamic_port_service / consciousness_bridge
neurobiological_brain/consciousness_containers/service/Dockerfile:15:# Redis client for dynamic_port_service / consciousness_bridge
neurobiological_brain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:4:Integrates multi-agent consciousness with dynamic port scheduling
neurobiological_brain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:18:from dynamic_port_service import DynamicPortService
neurobiological_brain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:30:# Dynamic port + discovery
neurobiological_brain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:33:# Initialize dynamic port service
neurobiological_brain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:34:port_service = DynamicPortService()
neurobiological_brain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:36:# # (Assumes DynamicPortService.register_service() exists and is non-blocking)
neurobiological_brain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:37:port_service.register_service()
neurobiological_brain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:165:        "port": port_service.port,
neurobiological_brain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:182:        "port": port_service.port,
neurobiological_brain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:243:        f"🌉 Starting Consciousness Bridge on dynamically allocated port {port_service.port} "
neurobiological_brain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:244:        f"(type={type(port_service.port)})"
neurobiological_brain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:246:    uvicorn.run(app, host="0.0.0.0", port=int(port_service.port))
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

