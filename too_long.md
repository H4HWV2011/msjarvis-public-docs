(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ cd /mnt/nvme1/msjarvis-rebuild
set +e
set +u
set +o pipefail

printf '\n=== Candidate Dockerfiles ===\n'
find . -maxdepth 5 -name 'Dockerfile' -print
find . -maxdepth 5 -name 'Dockerfile.*' -print

printf '\n=== Compose image/build lines ===\n'
grep -RIn --include='docker-compose*.yml' 'jarvis-main-brain' .
grep -RIn --include='docker-compose*.yml' 'build:' .
grep -RIn --include='docker-compose*.yml' 'image:' .

printf '\n=== Dockerfile references to hilbert state or services copy ===\n'
grep -RIn --include='Dockerfile*' 'jarvis_hilbert_state.py' .
grep -RIn --include='Dockerfile*' 'COPY ' .
grep -RIn --include='Dockerfile*' 'WORKDIR' .
grep -RIn --include='Dockerfile*' 'FROM ' .

=== Candidate Dockerfiles ===
./Dockerfile
./integration_layer/Dockerfile
./services/integration_layer.backup.1768269372/Dockerfile
./services/Dockerfile
./services/integration_layer.placeholder_1768012705/Dockerfile
./services/integration_layer/Dockerfile
./services/jarvis_steward/Dockerfile
./services/ai/Dockerfile
./services/python/Dockerfile
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile
./services/neurobiologicalbrain/i_containers/service/Dockerfile
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile
./services/neurobiologicalbrain/subconscious/service/Dockerfile
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/Dockerfile
./services/neurobiologicalbrain/neurobiological_brain/Dockerfile
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile
./services/ai-server/Dockerfile
./services/neurobiological_brain/qualia_engine/Dockerfile
./services/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile
./services/neurobiological_brain/qualia_engine/emotional_resonance/Dockerfile
./services/neurobiological_brain/qualia_engine/experience_generator/Dockerfile
./services/neurobiological_brain/Dockerfile
./services/alert_venv/Dockerfile
./neurobiologicalbrainmothercarrieprotocolsservice/Dockerfile
./ai/Dockerfile
./ai-server/Dockerfile
./neurobiological_brain/qualia_engine/service/Dockerfile
./neurobiological_brain/blood_brain_barrier/service/Dockerfile
./neurobiological_brain/i_containers/service/Dockerfile
./neurobiological_brain/spiritual_maternal_integration/service/Dockerfile
./neurobiological_brain/darwin_godel_machines/service/Dockerfile
./neurobiological_brain/spiritual_root/service/Dockerfile
./neurobiological_brain/subconscious/service/Dockerfile
./neurobiological_brain/woah_algorithms/service/Dockerfile
./neurobiological_brain/consciousness_containers/service/Dockerfile
./neurobiological_brain/pituitary_gland/service/Dockerfile
./neurobiological_brain/heteroglobulin_transport/service/Dockerfile
./neurobiological_brain/prefrontal_cortex/service/Dockerfile
./neurobiological_brain/neurobiological_brain/qualia_engine/Dockerfile
./neurobiological_brain/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile
./neurobiological_brain/neurobiological_brain/qualia_engine/emotional_resonance/Dockerfile
./neurobiological_brain/neurobiological_brain/qualia_engine/experience_generator/Dockerfile
./neurobiological_brain/neurobiological_brain/Dockerfile
./neurobiological_brain/mother_carrie_protocols/service/Dockerfile
find: ‘./data/mysql/aaacpe’: Permission denied
find: ‘./data/mysql/gis_rag’: Permission denied
find: ‘./data/local_resources’: Permission denied
./Dockerfile.hilbert_spatial_chat
./Dockerfile.gis_rag
./Dockerfile.nbb_icontainers_fastapi
./Dockerfile.full_neuro
./Dockerfile.agents
./Dockerfile.qualia
./services/Dockerfile.lm_synthesizer
./services/Dockerfile.pia-sampler
./services/Dockerfile.dgm_orchestrator
./services/Dockerfile.autonomous_learner
./services/Dockerfile.roche_llm.disabled
./services/Dockerfile.agents
./services/Dockerfile.hippocampus
./services/Dockerfile.icontainers_fastapi
./services/Dockerfile.dgm_worker
./services/Dockerfile.intake
./services/Dockerfile.bak_add_requests
./services/Dockerfile.qualia
./services/Dockerfile.fifth_dgm_real
./services/Dockerfile.web_research
./services/Dockerfile.temporal_consciousness
./services/Dockerfile.bak_add_service_discovery
./services/Dockerfile.memory
./services/Dockerfile.mother_protocols
./services/Dockerfile.toroidal
./services/Dockerfile.aaacpe_rag
./services/Dockerfile.nbb_*
./services/Dockerfile.semaphore
./services/Dockerfile.rag
./services/Dockerfile.icontainers
./services/Dockerfile.bak_before_bbb_copy_fix
./services/Dockerfile.judge
./services/Dockerfile.autonomous_complete
./services/Dockerfile.woah
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile.bak_add_flask
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile.bak_force_flask
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile.bak_add_flask
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile.bak_force_flask
./services/neurobiologicalbrain/i_containers/service/Dockerfile.bak_add_flask
./services/neurobiologicalbrain/i_containers/service/Dockerfile.bak_force_flask
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile.bak_add_flask
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile.bak_force_flask
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile.bak_add_flask
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile.bak_force_flask
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile.bak_add_flask
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile.bak_force_flask
./services/neurobiologicalbrain/subconscious/service/Dockerfile.bak_add_flask
./services/neurobiologicalbrain/subconscious/service/Dockerfile.bak_force_flask
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile.bak_add_flask
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile.bak_force_flask
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile.bak_add_flask
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile.bak_force_flask
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile.bak_add_flask
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile.bak_force_flask
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile.bak_add_flask
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile.bak_force_flask
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile.bak_add_flask
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile.bak_force_flask
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_use_nbb_base
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_flask_explicit
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_entrypoint
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_add_flask
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_bootstrap_cmd2
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_force_flask
./services/Dockerfile.nbb_base
./services/Dockerfile.autonomous_learner_complete
./services/Dockerfile.bak_runner_cmd
./services/Dockerfile.webdeploy
./services/Dockerfile.constitutional_guardian
./services/Dockerfile.bbb
./services/Dockerfile.crypto-policy
./services/Dockerfile.bak_add_redis
./services/Dockerfile.aaacpe_scraper
./services/Dockerfile.psychological_rag
./services/Dockerfile.69dgm_bridge
./services/Dockerfile.spiritual_rag
./services/Dockerfile.gateway
./services/Dockerfile.roche_llm
./services/Dockerfile.woah_algorithms
./services/Dockerfile.bak_add_deps
./services/Dockerfile.psychology_services
./services/Dockerfile.email
./Dockerfile.ragservermain
./Dockerfile.rag
./Dockerfile.rag_server_main
./Dockerfile.woah
./Dockerfile.neuro
./Dockerfile.neuro-prefrontal-patched
./Dockerfile.consciousnessbridge
./Dockerfile.local_resources
./Dockerfile.brain
./Dockerfile.bak_before_python3_fix
./Dockerfile.rag_server
./Dockerfile.20llm
./neurobiological_brain/i_containers/service/Dockerfile.nbb_icontainers_fastapi
./Dockerfile.swarm
./Dockerfile.gateway
find: ‘./data/mysql/aaacpe’: Permission denied
find: ‘./data/mysql/gis_rag’: Permission denied
find: ‘./data/local_resources’: Permission denied
./Dockerfile.qualia.bak

=== Compose image/build lines ===
./docker-compose.working.20260118-235132.yml:2:  jarvis-main-brain:
./docker-compose.working.20260118-235132.yml:6:    container_name: jarvis-main-brain
./docker-compose.working.20260118-235132.yml:690:    - MAINBRAIN_URL=http://jarvis-main-brain:8050
./docker-compose.RAG_WORKING_20260116.yml:113:    - MAINBRAIN_URL=http://jarvis-main-brain:8050
./docker-compose.RAG_WORKING_20260116.yml:317:  jarvis-main-brain:
./docker-compose.RAG_WORKING_20260116.yml:324:    container_name: jarvis-main-brain
./docker-compose.RAG_WORKING_20260116.yml:384:    image: jarvis-main-brain:latest
./docker-compose.RAG_WORKING_20260116.yml:603:    - MAIN_BRAIN_URL=http://jarvis-main-brain:8050/chat
./docker-compose.working.20260119-000202.yml:2:  jarvis-main-brain:
./docker-compose.working.20260119-000202.yml:6:    container_name: jarvis-main-brain
./docker-compose.working.20260119-000202.yml:690:    - MAINBRAIN_URL=http://jarvis-main-brain:8050
./docker-compose.golden.yml:17:  jarvis-main-brain:
./docker-compose.golden.yml:21:    container_name: jarvis-main-brain
./docker-compose.override.yml:37:  jarvis-main-brain:
./docker-compose.yml:535:    - jarvis-main-brain
./docker-compose.yml:1149:  jarvis-main-brain:
./docker-compose.yml:1153:    image: jarvis-main-brain:latest
./docker-compose.yml:1154:    container_name: jarvis-main-brain
./docker-compose.yml:1328:    - jarvis-main-brain
./docker-compose.yml:1516:    - JARVIS_URL=http://jarvis-main-brain:8050
./docker-compose.yml:1604:    image: jarvis-main-brain:latest
./docker-compose.yml:1777:    image: jarvis-main-brain:latest
./docker-compose.yml:1795:    image: jarvis-main-brain:latest
./docker-compose.yml:1825:    image: jarvis-main-brain:latest
./docker-compose.yml:1829:    image: jarvis-main-brain:latest
./docker-compose.yml:1845:    image: jarvis-main-brain:latest
./docker-compose.yml:1866:    image: jarvis-main-brain:latest
./docker-compose.yml:1891:    image: jarvis-main-brain:latest
./docker-compose.yml:1921:    image: jarvis-main-brain:latest
./docker-compose.yml:1955:    image: jarvis-main-brain:latest
./docker-compose.yml:1981:    image: jarvis-main-brain:latest
./docker-compose.yml:2021:    image: jarvis-main-brain:latest
./docker-compose.yml:2060:    image: jarvis-main-brain:latest
./docker-compose.yml:2063:    image: jarvis-main-brain:latest
./docker-compose.yml:2095:    image: jarvis-main-brain:latest
./docker-compose.yml:2097:    image: jarvis-main-brain:latest
./backups/docker-compose.STABLE_20260121_162220.yml:655:    - MAINBRAIN_URL=http://jarvis-main-brain:8050
grep: ./data/mysql/aaacpe: Permission denied
grep: ./data/mysql/gis_rag: Permission denied
grep: ./data/local_resources: Permission denied
./docker-compose.working.20260118-235132.yml:3:    build:
./docker-compose.working.20260118-235132.yml:81:    build:
./docker-compose.working.20260118-235132.yml:113:    build:
./docker-compose.working.20260118-235132.yml:143:    build:
./docker-compose.working.20260118-235132.yml:158:    build:
./docker-compose.working.20260118-235132.yml:173:    build:
./docker-compose.working.20260118-235132.yml:189:    build:
./docker-compose.working.20260118-235132.yml:217:    build:
./docker-compose.working.20260118-235132.yml:232:    build:
./docker-compose.working.20260118-235132.yml:247:    build:
./docker-compose.working.20260118-235132.yml:262:    build:
./docker-compose.working.20260118-235132.yml:277:    build:
./docker-compose.working.20260118-235132.yml:292:    build:
./docker-compose.working.20260118-235132.yml:307:    build:
./docker-compose.working.20260118-235132.yml:322:    build:
./docker-compose.working.20260118-235132.yml:337:    build:
./docker-compose.working.20260118-235132.yml:352:    build:
./docker-compose.working.20260118-235132.yml:367:    build:
./docker-compose.working.20260118-235132.yml:382:    build:
./docker-compose.working.20260118-235132.yml:397:    build:
./docker-compose.working.20260118-235132.yml:412:    build:
./docker-compose.working.20260118-235132.yml:427:    build:
./docker-compose.working.20260118-235132.yml:442:    build:
./docker-compose.working.20260118-235132.yml:457:    build:
./docker-compose.working.20260118-235132.yml:472:    build:
./docker-compose.working.20260118-235132.yml:487:    build:
./docker-compose.working.20260118-235132.yml:510:    build:
./docker-compose.working.20260118-235132.yml:550:    build:
./docker-compose.working.20260118-235132.yml:573:    build:
./docker-compose.working.20260118-235132.yml:595:    build:
./docker-compose.working.20260118-235132.yml:619:    build:
./docker-compose.working.20260118-235132.yml:639:    build:
./docker-compose.working.20260118-235132.yml:652:    build:
./docker-compose.working.20260118-235132.yml:665:    build:
./docker-compose.working.20260118-235132.yml:678:    build:
./docker-compose.working.20260118-235132.yml:707:    build:
./docker-compose.working.20260118-235132.yml:729:    build:
./docker-compose.working.20260118-235132.yml:750:    build:
./docker-compose.working.20260118-235132.yml:773:    build:
./docker-compose.working.20260118-235132.yml:797:    build:
./docker-compose.working.20260118-235132.yml:826:    build:
./docker-compose.working.20260118-235132.yml:849:    # build:
./docker-compose.working.20260118-235132.yml:964:    build: ./neurobiological_brain/i_containers/service
./docker-compose.working.20260118-235132.yml:974:    build: ./neurobiological_brain/consciousness_containers/service
./docker-compose.working.20260118-235132.yml:984:    build: ./neurobiological_brain/spiritual_root/service
./docker-compose.working.20260118-235132.yml:994:    build: ./neurobiological_brain/woah_algorithms/service
./docker-compose.working.20260118-235132.yml:1004:    build: ./neurobiological_brain/prefrontal_cortex/service
./docker-compose.working.20260118-235132.yml:1014:    build: ./neurobiological_brain/heteroglobulin_transport/service
./docker-compose.working.20260118-235132.yml:1024:    build: ./neurobiological_brain/mother_carrie_protocols/service
./docker-compose.working.20260118-235132.yml:1034:    build: ./neurobiological_brain/pituitary_gland/service
./docker-compose.working.20260118-235132.yml:1044:    build: ./neurobiological_brain/spiritual_maternal_integration/service
./docker-compose.working.20260118-235132.yml:1054:    build: ./neurobiological_brain/darwin_godel_machines/service
./docker-compose.working.20260118-235132.yml:1064:    build: ./neurobiological_brain/blood_brain_barrier/service
./docker-compose.working.20260118-235132.yml:1074:    build: ./neurobiological_brain/subconscious/service
./docker-compose.working.20260118-235132.yml:1084:    build: ./neurobiological_brain/qualia_engine/service
./docker-compose.restored.yml:3:    build: ./ai-server
./docker-compose.restored.yml:7:    build: ./ai
./docker-compose.restored.yml:11:    build: ./neurobiological_brain/i_containers/service
./docker-compose.restored.yml:15:    build: ./neurobiological_brain/consciousness_containers/service
./docker-compose.restored.yml:19:    build: ./neurobiological_brain/spiritual_root/service
./docker-compose.restored.yml:23:    build: ./neurobiological_brain/woah_algorithms/service
./docker-compose.restored.yml:27:    build: ./neurobiological_brain/prefrontal_cortex/service
./docker-compose.restored.yml:31:    build: ./neurobiological_brain/heteroglobulin_transport/service
./docker-compose.restored.yml:35:    build: ./neurobiological_brain/mother_carrie_protocols/service
./docker-compose.restored.yml:39:    build: ./neurobiological_brain/pituitary_gland/service
./docker-compose.restored.yml:43:    build: ./neurobiological_brain/spiritual_maternal_integration/service
./docker-compose.restored.yml:47:    build: ./neurobiological_brain/darwin_godel_machines/service
./docker-compose.restored.yml:51:    build: ./neurobiological_brain/blood_brain_barrier/service
./docker-compose.restored.yml:55:    build: ./neurobiological_brain/subconscious/service
./docker-compose.restored.yml:59:    build: ./neurobiological_brain/qualia_engine/service
./docker-compose.RAG_WORKING_20260116.yml:19:    build:
./docker-compose.RAG_WORKING_20260116.yml:48:    build:
./docker-compose.RAG_WORKING_20260116.yml:59:    build:
./docker-compose.RAG_WORKING_20260116.yml:81:    build:
./docker-compose.RAG_WORKING_20260116.yml:106:    build:
./docker-compose.RAG_WORKING_20260116.yml:127:    build:
./docker-compose.RAG_WORKING_20260116.yml:194:    build:
./docker-compose.RAG_WORKING_20260116.yml:214:    build:
./docker-compose.RAG_WORKING_20260116.yml:233:    build:
./docker-compose.RAG_WORKING_20260116.yml:254:    build:
./docker-compose.RAG_WORKING_20260116.yml:273:    build:
./docker-compose.RAG_WORKING_20260116.yml:296:    build:
./docker-compose.RAG_WORKING_20260116.yml:318:    build:
./docker-compose.RAG_WORKING_20260116.yml:401:    build:
./docker-compose.RAG_WORKING_20260116.yml:412:    build:
./docker-compose.RAG_WORKING_20260116.yml:462:    build:
./docker-compose.RAG_WORKING_20260116.yml:484:    build:
./docker-compose.RAG_WORKING_20260116.yml:535:    build:
./docker-compose.RAG_WORKING_20260116.yml:558:    build:
./docker-compose.RAG_WORKING_20260116.yml:569:    build:
./docker-compose.RAG_WORKING_20260116.yml:590:    build:
./docker-compose.RAG_WORKING_20260116.yml:618:    build:
./docker-compose.RAG_WORKING_20260116.yml:639:    build:
./docker-compose.RAG_WORKING_20260116.yml:660:    build:
./docker-compose.RAG_WORKING_20260116.yml:673:    build:
./docker-compose.RAG_WORKING_20260116.yml:686:    build:
./docker-compose.RAG_WORKING_20260116.yml:699:    build:
./docker-compose.RAG_WORKING_20260116.yml:712:    build:
./docker-compose.RAG_WORKING_20260116.yml:725:    build:
./docker-compose.RAG_WORKING_20260116.yml:738:    build:
./docker-compose.RAG_WORKING_20260116.yml:751:    build:
./docker-compose.RAG_WORKING_20260116.yml:764:    build:
./docker-compose.RAG_WORKING_20260116.yml:777:    build:
./docker-compose.RAG_WORKING_20260116.yml:790:    build:
./docker-compose.RAG_WORKING_20260116.yml:803:    build:
./docker-compose.RAG_WORKING_20260116.yml:816:    build:
./docker-compose.RAG_WORKING_20260116.yml:829:    build:
./docker-compose.RAG_WORKING_20260116.yml:842:    build:
./docker-compose.RAG_WORKING_20260116.yml:855:    build:
./docker-compose.RAG_WORKING_20260116.yml:868:    build:
./docker-compose.RAG_WORKING_20260116.yml:881:    build:
./docker-compose.RAG_WORKING_20260116.yml:894:    build:
./docker-compose.RAG_WORKING_20260116.yml:907:    build:
./docker-compose.RAG_WORKING_20260116.yml:920:    build:
./docker-compose.RAG_WORKING_20260116.yml:933:    build:
./docker-compose.RAG_WORKING_20260116.yml:961:    build: ./neurobiological_brain/blood_brain_barrier/service
./docker-compose.RAG_WORKING_20260116.yml:972:    build: ./neurobiological_brain/consciousness_containers/service
./docker-compose.RAG_WORKING_20260116.yml:983:    build: ./neurobiological_brain/darwin_godel_machines/service
./docker-compose.RAG_WORKING_20260116.yml:994:    build: ./neurobiological_brain/heteroglobulin_transport/service
./docker-compose.RAG_WORKING_20260116.yml:1005:    build: ./neurobiological_brain/i_containers/service
./docker-compose.RAG_WORKING_20260116.yml:1016:    build: ./neurobiological_brain/mother_carrie_protocols/service
./docker-compose.RAG_WORKING_20260116.yml:1027:    build: ./neurobiological_brain/pituitary_gland/service
./docker-compose.RAG_WORKING_20260116.yml:1038:    build: ./neurobiological_brain/prefrontal_cortex/service
./docker-compose.RAG_WORKING_20260116.yml:1064:    build: ./neurobiological_brain/qualia_engine/service
./docker-compose.RAG_WORKING_20260116.yml:1071:    build: ./neurobiological_brain/spiritual_maternal_integration/service
./docker-compose.RAG_WORKING_20260116.yml:1082:    build: ./neurobiological_brain/spiritual_root/service
./docker-compose.RAG_WORKING_20260116.yml:1093:    build: ./neurobiological_brain/subconscious/service
./docker-compose.RAG_WORKING_20260116.yml:1104:    build: ./neurobiological_brain/woah_algorithms/service
./docker-compose.working.20260119-000202.yml:3:    build:
./docker-compose.working.20260119-000202.yml:81:    build:
./docker-compose.working.20260119-000202.yml:113:    build:
./docker-compose.working.20260119-000202.yml:143:    build:
./docker-compose.working.20260119-000202.yml:158:    build:
./docker-compose.working.20260119-000202.yml:173:    build:
./docker-compose.working.20260119-000202.yml:189:    build:
./docker-compose.working.20260119-000202.yml:217:    build:
./docker-compose.working.20260119-000202.yml:232:    build:
./docker-compose.working.20260119-000202.yml:247:    build:
./docker-compose.working.20260119-000202.yml:262:    build:
./docker-compose.working.20260119-000202.yml:277:    build:
./docker-compose.working.20260119-000202.yml:292:    build:
./docker-compose.working.20260119-000202.yml:307:    build:
./docker-compose.working.20260119-000202.yml:322:    build:
./docker-compose.working.20260119-000202.yml:337:    build:
./docker-compose.working.20260119-000202.yml:352:    build:
./docker-compose.working.20260119-000202.yml:367:    build:
./docker-compose.working.20260119-000202.yml:382:    build:
./docker-compose.working.20260119-000202.yml:397:    build:
./docker-compose.working.20260119-000202.yml:412:    build:
./docker-compose.working.20260119-000202.yml:427:    build:
./docker-compose.working.20260119-000202.yml:442:    build:
./docker-compose.working.20260119-000202.yml:457:    build:
./docker-compose.working.20260119-000202.yml:472:    build:
./docker-compose.working.20260119-000202.yml:487:    build:
./docker-compose.working.20260119-000202.yml:510:    build:
./docker-compose.working.20260119-000202.yml:550:    build:
./docker-compose.working.20260119-000202.yml:573:    build:
./docker-compose.working.20260119-000202.yml:595:    build:
./docker-compose.working.20260119-000202.yml:619:    build:
./docker-compose.working.20260119-000202.yml:639:    build:
./docker-compose.working.20260119-000202.yml:652:    build:
./docker-compose.working.20260119-000202.yml:665:    build:
./docker-compose.working.20260119-000202.yml:678:    build:
./docker-compose.working.20260119-000202.yml:707:    build:
./docker-compose.working.20260119-000202.yml:729:    build:
./docker-compose.working.20260119-000202.yml:750:    build:
./docker-compose.working.20260119-000202.yml:773:    build:
./docker-compose.working.20260119-000202.yml:797:    build:
./docker-compose.working.20260119-000202.yml:826:    build:
./docker-compose.working.20260119-000202.yml:849:    # build:
./docker-compose.working.20260119-000202.yml:964:    build: ./neurobiological_brain/i_containers/service
./docker-compose.working.20260119-000202.yml:974:    build: ./neurobiological_brain/consciousness_containers/service
./docker-compose.working.20260119-000202.yml:984:    build: ./neurobiological_brain/spiritual_root/service
./docker-compose.working.20260119-000202.yml:994:    build: ./neurobiological_brain/woah_algorithms/service
./docker-compose.working.20260119-000202.yml:1004:    build: ./neurobiological_brain/prefrontal_cortex/service
./docker-compose.working.20260119-000202.yml:1014:    build: ./neurobiological_brain/heteroglobulin_transport/service
./docker-compose.working.20260119-000202.yml:1024:    build: ./neurobiological_brain/mother_carrie_protocols/service
./docker-compose.working.20260119-000202.yml:1034:    build: ./neurobiological_brain/pituitary_gland/service
./docker-compose.working.20260119-000202.yml:1044:    build: ./neurobiological_brain/spiritual_maternal_integration/service
./docker-compose.working.20260119-000202.yml:1054:    build: ./neurobiological_brain/darwin_godel_machines/service
./docker-compose.working.20260119-000202.yml:1064:    build: ./neurobiological_brain/blood_brain_barrier/service
./docker-compose.working.20260119-000202.yml:1074:    build: ./neurobiological_brain/subconscious/service
./docker-compose.working.20260119-000202.yml:1084:    build: ./neurobiological_brain/qualia_engine/service
./docker-compose.golden.yml:4:    build:
./docker-compose.golden.yml:18:    build:
./docker-compose.golden.yml:96:    build:
./docker-compose.golden.yml:128:    build:
./docker-compose.golden.yml:159:    build:
./docker-compose.golden.yml:174:    build:
./docker-compose.golden.yml:189:    build:
./docker-compose.golden.yml:204:    build:
./docker-compose.golden.yml:219:    build:
./docker-compose.golden.yml:234:    build:
./docker-compose.golden.yml:249:    build:
./docker-compose.golden.yml:264:    build:
./docker-compose.golden.yml:279:    build:
./docker-compose.golden.yml:294:    build:
./docker-compose.golden.yml:309:    build:
./docker-compose.golden.yml:324:    build:
./docker-compose.golden.yml:339:    build:
./docker-compose.golden.yml:354:    build:
./docker-compose.golden.yml:369:    build:
./docker-compose.golden.yml:384:    build:
./docker-compose.golden.yml:399:    build:
./docker-compose.golden.yml:414:    build:
./docker-compose.golden.yml:429:    build:
./docker-compose.golden.yml:444:    build:
./docker-compose.golden.yml:459:    build:
./docker-compose.golden.yml:474:    build:
./docker-compose.golden.yml:489:    build:
./docker-compose.golden.yml:512:    build:
./docker-compose.golden.yml:552:    build:
./docker-compose.golden.yml:575:    build:
./docker-compose.golden.yml:597:    build:
./docker-compose.golden.yml:621:    build:
./docker-compose.golden.yml:641:    build:
./docker-compose.golden.yml:654:    build:
./docker-compose.golden.yml:667:    build:
./docker-compose.golden.yml:680:    build:
./docker-compose.golden.yml:709:    build:
./docker-compose.golden.yml:730:    build:
./docker-compose.golden.yml:754:    build:
./docker-compose.golden.yml:779:    build:
./docker-compose.golden.yml:808:    build:
./docker-compose.golden.yml:832:    # build:
./docker-compose.mountainshares-override.yml:27:    build:
./docker-compose.override.yml:6:    build:
./docker-compose.override.yml:22:    build:
./docker-compose.override.yml:42:    build:
./docker-compose.llm-proxies.yml:5:    build:
./docker-compose.llm-proxies.yml:17:    build:
./docker-compose.llm-proxies.yml:29:    build:
./docker-compose.llm-proxies.yml:41:    build:
./docker-compose.llm-proxies.yml:53:    build:
./docker-compose.llm-proxies.yml:65:    build:
./docker-compose.llm-proxies.yml:77:    build:
./docker-compose.llm-proxies.yml:89:    build:
./docker-compose.llm-proxies.yml:101:    build:
./docker-compose.llm-proxies.yml:113:    build:
./docker-compose.llm-proxies.yml:125:    build:
./docker-compose.llm-proxies.yml:137:    build:
./docker-compose.llm-proxies.yml:149:    build:
./docker-compose.llm-proxies.yml:161:    build:
./docker-compose.llm-proxies.yml:173:    build:
./docker-compose.llm-proxies.yml:185:    build:
./docker-compose.llm-proxies.yml:197:    build:
./docker-compose.llm-proxies.yml:209:    build:
./docker-compose.llm-proxies.yml:221:    build:
./docker-compose.llm-proxies.yml:233:    build:
./docker-compose.llm-proxies.yml:245:    build:
./docker-compose.llm-proxies.yml:257:    build:
./docker-compose.yml:3:    build:
./docker-compose.yml:87:    build:
./docker-compose.yml:116:    build:
./docker-compose.yml:152:    build:
./docker-compose.yml:166:    build:
./docker-compose.yml:180:    build:
./docker-compose.yml:194:    build:
./docker-compose.yml:208:    build:
./docker-compose.yml:222:    build:
./docker-compose.yml:236:    build:
./docker-compose.yml:250:    build:
./docker-compose.yml:264:    build:
./docker-compose.yml:278:    build:
./docker-compose.yml:292:    build:
./docker-compose.yml:306:    build:
./docker-compose.yml:320:    build:
./docker-compose.yml:334:    build:
./docker-compose.yml:348:    build:
./docker-compose.yml:362:    build:
./docker-compose.yml:376:    build:
./docker-compose.yml:390:    build:
./docker-compose.yml:404:    build:
./docker-compose.yml:418:    build:
./docker-compose.yml:432:    build:
./docker-compose.yml:446:    build:
./docker-compose.yml:460:    build:
./docker-compose.yml:482:    build:
./docker-compose.yml:518:    build:
./docker-compose.yml:558:    build:
./docker-compose.yml:580:    build:
./docker-compose.yml:602:    build:
./docker-compose.yml:625:    build:
./docker-compose.yml:649:    build:
./docker-compose.yml:661:    build:
./docker-compose.yml:673:    build:
./docker-compose.yml:687:    build:
./docker-compose.yml:709:    build:
./docker-compose.yml:734:    build:
./docker-compose.yml:755:    build:
./docker-compose.yml:777:    build:
./docker-compose.yml:789:    build:
./docker-compose.yml:801:    build:
./docker-compose.yml:829:    build:
./docker-compose.yml:957:    build:
./docker-compose.yml:975:    build: ./neurobiological_brain/consciousness_containers/service
./docker-compose.yml:985:    build: ./neurobiological_brain/spiritual_root/service
./docker-compose.yml:996:    build: ./neurobiological_brain/woah_algorithms/service
./docker-compose.yml:1006:    build: ./neurobiological_brain/prefrontal_cortex/service
./docker-compose.yml:1019:    build: ./neurobiological_brain/heteroglobulin_transport/service
./docker-compose.yml:1032:    build: ./neurobiological_brain/mother_carrie_protocols/service
./docker-compose.yml:1046:    build: ./neurobiological_brain/pituitary_gland/service
./docker-compose.yml:1056:    build: ./neurobiological_brain/spiritual_maternal_integration/service
./docker-compose.yml:1070:    build: ./neurobiological_brain/darwin_godel_machines/service
./docker-compose.yml:1080:    build: ./neurobiological_brain/blood_brain_barrier/service
./docker-compose.yml:1090:    build: ./neurobiological_brain/subconscious/service
./docker-compose.yml:1100:    build: ./neurobiological_brain/qualia_engine/service
./docker-compose.yml:1150:    build:
./docker-compose.yml:1197:    build:
./docker-compose.yml:1232:    build:
./docker-compose.yml:1252:    build:
./docker-compose.yml:1275:    build:
./docker-compose.yml:1293:    build:
./docker-compose.yml:1315:    build:
./docker-compose.yml:1339:    build:
./docker-compose.yml:1356:    build:
./docker-compose.yml:1373:    build:
./docker-compose.yml:1390:    build:
./docker-compose.yml:1407:    build:
./docker-compose.yml:1435:    build:
./docker-compose.yml:1461:    build:
./docker-compose.yml:1483:    build:
./docker-compose.yml:1766:    build:
./docker-compose.yml:2008:    build:
./docker-compose.yml:2112:    build: ./neurobiological_brain/i_containers/service
./docker-compose.yml:2431:    build:
./docker-compose.yml:2446:    build:
./docker-compose.yml:2461:    build:
./docker-compose.yml:2476:    build:
./docker-compose.yml:2491:    build:
./docker-compose.yml:2506:    build:
./docker-compose.yml:2521:    build:
./docker-compose.yml:2536:    build:
./docker-compose.yml:2551:    build:
./docker-compose.yml:2566:    build:
./docker-compose.yml:2581:    build:
./docker-compose.yml:2596:    build:
./docker-compose.yml:2611:    build:
./docker-compose.yml:2626:    build:
./docker-compose.yml:2641:    build:
./docker-compose.yml:2656:    build:
./docker-compose.yml:2671:    build:
./docker-compose.yml:2686:    build:
./docker-compose.yml:2701:    build:
./docker-compose.yml:2716:    build:
./docker-compose.yml:2731:    build:
./docker-compose.yml:2746:    build:
./docker-compose.yml:2761:    build:
./docker-compose.rag.yml:3:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:2:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:78:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:108:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:123:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:138:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:154:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:182:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:197:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:212:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:227:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:242:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:257:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:272:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:287:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:302:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:317:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:332:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:347:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:362:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:377:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:392:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:407:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:422:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:437:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:452:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:475:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:515:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:538:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:560:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:584:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:604:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:617:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:630:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:643:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:672:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:694:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:715:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:738:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:762:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:791:    build:
./backups/docker-compose.STABLE_20260121_162220.yml:814:    # build:
./backups/docker-compose.STABLE_20260121_162220.yml:915:    build: ./neurobiological_brain/i_containers/service
./backups/docker-compose.STABLE_20260121_162220.yml:925:    build: ./neurobiological_brain/consciousness_containers/service
./backups/docker-compose.STABLE_20260121_162220.yml:935:    build: ./neurobiological_brain/spiritual_root/service
./backups/docker-compose.STABLE_20260121_162220.yml:945:    build: ./neurobiological_brain/woah_algorithms/service
./backups/docker-compose.STABLE_20260121_162220.yml:955:    build: ./neurobiological_brain/prefrontal_cortex/service
./backups/docker-compose.STABLE_20260121_162220.yml:965:    build: ./neurobiological_brain/heteroglobulin_transport/service
./backups/docker-compose.STABLE_20260121_162220.yml:975:    build: ./neurobiological_brain/mother_carrie_protocols/service
./backups/docker-compose.STABLE_20260121_162220.yml:985:    build: ./neurobiological_brain/pituitary_gland/service
./backups/docker-compose.STABLE_20260121_162220.yml:995:    build: ./neurobiological_brain/spiritual_maternal_integration/service
./backups/docker-compose.STABLE_20260121_162220.yml:1005:    build: ./neurobiological_brain/darwin_godel_machines/service
./backups/docker-compose.STABLE_20260121_162220.yml:1015:    build: ./neurobiological_brain/blood_brain_barrier/service
./backups/docker-compose.STABLE_20260121_162220.yml:1025:    build: ./neurobiological_brain/subconscious/service
./backups/docker-compose.STABLE_20260121_162220.yml:1035:    build: ./neurobiological_brain/qualia_engine/service
grep: ./data/mysql/aaacpe: Permission denied
grep: ./data/mysql/gis_rag: Permission denied
grep: ./data/local_resources: Permission denied
./docker-compose.working.20260118-235132.yml:852:    image: python:3.10
./docker-compose.working.20260118-235132.yml:871:    image: ollama/ollama:latest
./docker-compose.working.20260118-235132.yml:895:    image: redis:7-alpine
./docker-compose.working.20260118-235132.yml:920:    image: ipfs/kubo:latest
./docker-compose.working.20260118-235132.yml:933:    image: chromadb/chroma:latest
./docker-compose.gbim.yml:4:    image: postgis/postgis:15-3.4
./docker-compose.restored.yml:63:    image: chromadb/chroma:latest
./docker-compose.restored.yml:81:    image: redis:latest
./docker-compose.restored.yml:94:    image: neo4j:5.13-community
./docker-compose.restored.yml:103:    image: mysql:8.2
./docker-compose.restored.yml:115:    image: ipfs/kubo:latest
./docker-compose.RAG_WORKING_20260116.yml:10:    image: ipfs/kubo:latest
./docker-compose.RAG_WORKING_20260116.yml:33:    image: msjarvis-20llm-production:latest
./docker-compose.RAG_WORKING_20260116.yml:54:    image: msjarvis-69dgm-bridge:latest
./docker-compose.RAG_WORKING_20260116.yml:70:    image: msjarvis-agents-service:latest
./docker-compose.RAG_WORKING_20260116.yml:94:    image: msjarvis-autonomous-learner:latest
./docker-compose.RAG_WORKING_20260116.yml:115:    image: msjarvis-bbb:latest
./docker-compose.RAG_WORKING_20260116.yml:151:    image: msjarvis-brain-orchestrator:latest
./docker-compose.RAG_WORKING_20260116.yml:180:    image: chromadb/chroma:0.5.4
./docker-compose.RAG_WORKING_20260116.yml:204:    image: msjarvis-consciousness-bridge:latest
./docker-compose.RAG_WORKING_20260116.yml:223:    image: msjarvis-fifth-dgm:latest
./docker-compose.RAG_WORKING_20260116.yml:242:    image: msjarvis-fractal:latest
./docker-compose.RAG_WORKING_20260116.yml:262:    image: msjarvis-full-neuro:latest
./docker-compose.RAG_WORKING_20260116.yml:284:    image: msjarvis-i-containers:latest
./docker-compose.RAG_WORKING_20260116.yml:308:    image: msjarvis-lm-synthesizer:latest
./docker-compose.RAG_WORKING_20260116.yml:384:    image: jarvis-main-brain:latest
./docker-compose.RAG_WORKING_20260116.yml:407:    image: msjarvis-mother-protocols:latest
./docker-compose.RAG_WORKING_20260116.yml:427:    image: msjarvis-neuro:latest
./docker-compose.RAG_WORKING_20260116.yml:450:    image: ollama/ollama:latest
./docker-compose.RAG_WORKING_20260116.yml:472:    image: msjarvis-qualia:latest
./docker-compose.RAG_WORKING_20260116.yml:499:    image: msjarvis-rag-server:latest
./docker-compose.RAG_WORKING_20260116.yml:523:    image: redis:7-alpine
./docker-compose.RAG_WORKING_20260116.yml:547:    image: msjarvis-swarm-intelligence:latest
./docker-compose.RAG_WORKING_20260116.yml:564:    image: msjarvis-temporal-consciousness:latest
./docker-compose.RAG_WORKING_20260116.yml:580:    image: msjarvis-toroidal:latest
./docker-compose.RAG_WORKING_20260116.yml:605:    image: msjarvis-unified-gateway:latest
./docker-compose.RAG_WORKING_20260116.yml:629:    image: msjarvis-web-research:latest
./docker-compose.RAG_WORKING_20260116.yml:650:    image: msjarvis-woah:latest
./docker-compose.RAG_WORKING_20260116.yml:666:    image: msjarvis-llm1-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:679:    image: msjarvis-llm10-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:692:    image: msjarvis-llm11-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:705:    image: msjarvis-llm12-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:718:    image: msjarvis-llm13-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:731:    image: msjarvis-llm14-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:744:    image: msjarvis-llm15-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:757:    image: msjarvis-llm16-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:770:    image: msjarvis-llm17-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:783:    image: msjarvis-llm18-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:796:    image: msjarvis-llm19-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:809:    image: msjarvis-llm2-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:822:    image: msjarvis-llm20-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:835:    image: msjarvis-llm21-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:848:    image: msjarvis-llm22-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:861:    image: msjarvis-llm3-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:874:    image: msjarvis-llm4-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:887:    image: msjarvis-llm5-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:900:    image: msjarvis-llm6-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:913:    image: msjarvis-llm7-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:926:    image: msjarvis-llm8-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:939:    image: msjarvis-llm9-proxy:latest
./docker-compose.RAG_WORKING_20260116.yml:952:    image: mysql:8.2
./docker-compose.RAG_WORKING_20260116.yml:1051:    image: neuro-prefrontalcortex-service:latest
./docker-compose.RAG_WORKING_20260116.yml:1119:    image: neo4j:5.13-community
./docker-compose.working.20260119-000202.yml:852:    image: python:3.10
./docker-compose.working.20260119-000202.yml:871:    image: ollama/ollama:latest
./docker-compose.working.20260119-000202.yml:895:    image: redis:7-alpine
./docker-compose.working.20260119-000202.yml:920:    image: ipfs/kubo:latest
./docker-compose.working.20260119-000202.yml:933:    image: chromadb/chroma:latest
./docker-compose.golden.yml:835:    image: python:3.10
./docker-compose.golden.yml:855:    image: ollama/ollama:latest
./docker-compose.golden.yml:879:    image: redis:7-alpine
./docker-compose.golden.yml:903:    image: ipfs/kubo:latest
./docker-compose.golden.yml:916:    image: chromadb/chroma:latest
./docker-compose.golden.yml:947:    image: msjarvis-nbb-base
./docker-compose.golden.yml:959:    image: msjarvis-nbb-base
./docker-compose.golden.yml:971:    image: msjarvis-nbb-base
./docker-compose.golden.yml:983:    image: msjarvis-nbb-base
./docker-compose.golden.yml:995:    image: msjarvis-nbb-base
./docker-compose.golden.yml:1007:    image: msjarvis-nbb-base
./docker-compose.golden.yml:1019:    image: msjarvis-nbb-base
./docker-compose.golden.yml:1031:    image: msjarvis-nbb-base
./docker-compose.golden.yml:1043:    image: msjarvis-nbb-base
./docker-compose.golden.yml:1055:    image: msjarvis-nbb-base
./docker-compose.golden.yml:1067:    image: msjarvis-nbb-base
./docker-compose.golden.yml:1079:    image: msjarvis-nbb-base
./docker-compose.golden.yml:1091:    image: msjarvis-nbb-base
./docker-compose.llm-proxies.yml:8:    image: msjarvis-llm1-proxy:latest
./docker-compose.llm-proxies.yml:20:    image: msjarvis-llm2-proxy:latest
./docker-compose.llm-proxies.yml:32:    image: msjarvis-llm3-proxy:latest
./docker-compose.llm-proxies.yml:44:    image: msjarvis-llm4-proxy:latest
./docker-compose.llm-proxies.yml:56:    image: msjarvis-llm5-proxy:latest
./docker-compose.llm-proxies.yml:68:    image: msjarvis-llm6-proxy:latest
./docker-compose.llm-proxies.yml:80:    image: msjarvis-llm7-proxy:latest
./docker-compose.llm-proxies.yml:92:    image: msjarvis-llm8-proxy:latest
./docker-compose.llm-proxies.yml:104:    image: msjarvis-llm9-proxy:latest
./docker-compose.llm-proxies.yml:116:    image: msjarvis-llm10-proxy:latest
./docker-compose.llm-proxies.yml:128:    image: msjarvis-llm11-proxy:latest
./docker-compose.llm-proxies.yml:140:    image: msjarvis-llm12-proxy:latest
./docker-compose.llm-proxies.yml:152:    image: msjarvis-llm13-proxy:latest
./docker-compose.llm-proxies.yml:164:    image: msjarvis-llm14-proxy:latest
./docker-compose.llm-proxies.yml:176:    image: msjarvis-llm15-proxy:latest
./docker-compose.llm-proxies.yml:188:    image: msjarvis-llm16-proxy:latest
./docker-compose.llm-proxies.yml:200:    image: msjarvis-llm17-proxy:latest
./docker-compose.llm-proxies.yml:212:    image: msjarvis-llm18-proxy:latest
./docker-compose.llm-proxies.yml:224:    image: msjarvis-llm19-proxy:latest
./docker-compose.llm-proxies.yml:236:    image: msjarvis-llm20-proxy:latest
./docker-compose.llm-proxies.yml:248:    image: msjarvis-llm21-proxy:latest
./docker-compose.llm-proxies.yml:260:    image: msjarvis-llm22-proxy:latest
./docker-compose.yml:850:    image: msjarvis-rebuild-jarvis-rag-server:latest
./docker-compose.yml:875:    image: ollama/ollama:latest
./docker-compose.yml:903:    image: redis:7-alpine
./docker-compose.yml:926:    image: chromadb/chroma:0.6.3
./docker-compose.yml:1109:    image: neo4j:5.13-community
./docker-compose.yml:1122:    image: mysql:8.2
./docker-compose.yml:1138:    image: ipfs/kubo:latest
./docker-compose.yml:1153:    image: jarvis-main-brain:latest
./docker-compose.yml:1218:    image: postgis/postgis:15-3.4
./docker-compose.yml:1255:    image: msjarvis-toroidal:latest
./docker-compose.yml:1507:    image: msjarvis/jarvis-auth-api:patched
./docker-compose.yml:1531:    image: msjarvis-rebuild-jarvis-contracts
./docker-compose.yml:1547:    image: msjarvis-rebuild-jarvis-eeg-beta
./docker-compose.yml:1566:    image: msjarvis-rebuild-jarvis-eeg-delta
./docker-compose.yml:1585:    image: msjarvis-rebuild-jarvis-eeg-theta
./docker-compose.yml:1604:    image: jarvis-main-brain:latest
./docker-compose.yml:1627:    image: jaegertracing/all-in-one:1.52
./docker-compose.yml:1644:    image: msjarvis-rebuild-jarvis-kyc-vault
./docker-compose.yml:1665:    image: msjarvis-rebuild-jarvis-phi-probe
./docker-compose.yml:1683:    image: python:3.11-slim
./docker-compose.yml:1700:    image: msjarvis-rebuild-jarvis-provenance
./docker-compose.yml:1720:    image: msjarvis-rebuild-jarvis-rag-router
./docker-compose.yml:1742:    image: jarvis-session-sidecar:latest
./docker-compose.yml:1777:    image: jarvis-main-brain:latest
./docker-compose.yml:1795:    image: jarvis-main-brain:latest
./docker-compose.yml:1825:    image: jarvis-main-brain:latest
./docker-compose.yml:1829:    image: jarvis-main-brain:latest
./docker-compose.yml:1845:    image: jarvis-main-brain:latest
./docker-compose.yml:1866:    image: jarvis-main-brain:latest
./docker-compose.yml:1891:    image: jarvis-main-brain:latest
./docker-compose.yml:1921:    image: jarvis-main-brain:latest
./docker-compose.yml:1945:    image: python:3.11-slim
./docker-compose.yml:1955:    image: jarvis-main-brain:latest
./docker-compose.yml:1981:    image: jarvis-main-brain:latest
./docker-compose.yml:2021:    image: jarvis-main-brain:latest
./docker-compose.yml:2060:    image: jarvis-main-brain:latest
./docker-compose.yml:2063:    image: jarvis-main-brain:latest
./docker-compose.yml:2095:    image: jarvis-main-brain:latest
./docker-compose.yml:2097:    image: jarvis-main-brain:latest
./docker-compose.yml:2132:    image: msjarvis-rebuild-jarvis-dgm-bridge-01:latest
./docker-compose.yml:2145:    image: msjarvis-rebuild-jarvis-dgm-bridge-02:latest
./docker-compose.yml:2158:    image: msjarvis-rebuild-jarvis-dgm-bridge-03:latest
./docker-compose.yml:2171:    image: msjarvis-rebuild-jarvis-dgm-bridge-04:latest
./docker-compose.yml:2184:    image: msjarvis-rebuild-jarvis-dgm-bridge-05:latest
./docker-compose.yml:2197:    image: msjarvis-rebuild-jarvis-dgm-bridge-06:latest
./docker-compose.yml:2210:    image: msjarvis-rebuild-jarvis-dgm-bridge-07:latest
./docker-compose.yml:2223:    image: msjarvis-rebuild-jarvis-dgm-bridge-08:latest
./docker-compose.yml:2236:    image: msjarvis-rebuild-jarvis-dgm-bridge-09:latest
./docker-compose.yml:2249:    image: msjarvis-rebuild-jarvis-dgm-bridge-10:latest
./docker-compose.yml:2262:    image: msjarvis-rebuild-jarvis-dgm-bridge-11:latest
./docker-compose.yml:2275:    image: msjarvis-rebuild-jarvis-dgm-bridge-12:latest
./docker-compose.yml:2288:    image: msjarvis-rebuild-jarvis-dgm-bridge-13:latest
./docker-compose.yml:2301:    image: msjarvis-rebuild-jarvis-dgm-bridge-14:latest
./docker-compose.yml:2314:    image: msjarvis-rebuild-jarvis-dgm-bridge-15:latest
./docker-compose.yml:2327:    image: msjarvis-rebuild-jarvis-dgm-bridge-16:latest
./docker-compose.yml:2340:    image: msjarvis-rebuild-jarvis-dgm-bridge-17:latest
./docker-compose.yml:2353:    image: msjarvis-rebuild-jarvis-dgm-bridge-18:latest
./docker-compose.yml:2366:    image: msjarvis-rebuild-jarvis-dgm-bridge-19:latest
./docker-compose.yml:2379:    image: msjarvis-rebuild-jarvis-dgm-bridge-20:latest
./docker-compose.yml:2392:    image: msjarvis-rebuild-jarvis-dgm-bridge-21:latest
./docker-compose.yml:2405:    image: msjarvis-rebuild-jarvis-dgm-bridge-22:latest
./docker-compose.yml:2418:    image: msjarvis-rebuild-jarvis-dgm-bridge-23:latest
./docker-compose.rag.yml:6:    image: msjarvis-rag-server:latest
./backups/docker-compose.STABLE_20260121_162220.yml:817:    image: python:3.10
./backups/docker-compose.STABLE_20260121_162220.yml:836:    image: ollama/ollama:latest
./backups/docker-compose.STABLE_20260121_162220.yml:860:    image: redis:7-alpine
./backups/docker-compose.STABLE_20260121_162220.yml:884:    image: chromadb/chroma:latest
./backups/docker-compose.STABLE_20260121_162220.yml:1045:    image: neo4j:5.13-community
./backups/docker-compose.STABLE_20260121_162220.yml:1059:    image: mysql:8.2
./backups/docker-compose.STABLE_20260121_162220.yml:1076:    image: ipfs/kubo:latest
grep: ./data/mysql/aaacpe: Permission denied
grep: ./data/mysql/gis_rag: Permission denied
grep: ./data/local_resources: Permission denied

=== Dockerfile references to hilbert state or services copy ===
grep: ./data/mysql/aaacpe: Permission denied
grep: ./data/mysql/gis_rag: Permission denied
grep: ./data/local_resources: Permission denied
./Dockerfile.hilbert_spatial_chat:4:COPY services/hilbert_spatial_chat.py .
./Dockerfile.gis_rag:4:COPY services/gis_rag_service.py /app/gis_rag_service.py
./Dockerfile-llm19-proxy:3:COPY llm19_health_proxy.py .
./Dockerfile-llm1-proxy:3:COPY llm1_health_proxy.py .
./Dockerfile.nbb_icontainers_fastapi:8:COPY neurobiological_brain/ /app/neurobiological_brain/
./Dockerfile.nbb_icontainers_fastapi:9:COPY services/ /app/services/
./Dockerfile.nbb_icontainers_fastapi:12:COPY requirements.txt /app/requirements.txt
./Dockerfile.full_neuro:5:COPY services/requirements.txt /app/requirements.txt
./Dockerfile.full_neuro:8:COPY services /app/services
./Dockerfile.agents:5:COPY services/requirements.txt /app/requirements.txt
./Dockerfile.agents:8:COPY services /app/services
./Dockerfile-llm16-proxy:3:COPY llm16_health_proxy.py .
./Dockerfile:10:COPY requirements.txt /app/
./Dockerfile:14:COPY services/ /app/services/
./Dockerfile:17:COPY neurobiological_brain/ /app/neurobiological_brain/
./Dockerfile-llm17-proxy:3:COPY llm17_health_proxy.py .
./Dockerfile-llm2-proxy:3:COPY llm2_health_proxy.py .
./Dockerfile-llm3-proxy:3:COPY llm3_health_proxy.py .
./integration_layer/Dockerfile:3:COPY . /app
./services/Dockerfile.lm_synthesizer:4:COPY requirements.txt /app/requirements.txt
./services/Dockerfile.lm_synthesizer:11:COPY lm_synthesizer.py /app/lm_synthesizer.py
./services/Dockerfile.pia-sampler:3:COPY . /app/services/
./services/Dockerfile.dgm_orchestrator:3:COPY . /app
./services/Dockerfile.autonomous_learner:17:COPY ms_jarvis_autonomous_learner.py /app/ms_jarvis_autonomous_learner.py
./services/Dockerfile.autonomous_learner:18:COPY gisgeodb_storage.py           /app/gisgeodb_storage.py
./services/Dockerfile.roche_llm.disabled:6:COPY ../requirements.txt /app/requirements.txt
./services/Dockerfile.roche_llm.disabled:10:COPY services/roche_llm.py /app/roche_llm.py
./services/Dockerfile.roche_llm.disabled:11:COPY services/llm_consensus_22.py /app/llm_consensus_22.py
./services/Dockerfile-llm19-proxy:3:COPY llm19_health_proxy.py .
./services/Dockerfile-llm1-proxy:3:COPY llm1_health_proxy.py .
./services/integration_layer.backup.1768269372/Dockerfile:3:COPY . /app
./services/Dockerfile.agents:3:COPY services /app/services
./services/Dockerfile.hippocampus:17:COPY hippocampus_service.py /app/hippocampus_service.py
./services/Dockerfile.icontainers_fastapi:7:COPY icontainers_fastapi.py /app/icontainers_fastapi.py
./services/Dockerfile-llm16-proxy:3:COPY llm16_health_proxy.py .
./services/Dockerfile.dgm_worker:5:COPY requirements.txt /app/requirements.txt
./services/Dockerfile.dgm_worker:7:COPY dgm_worker.py /app/dgm_worker.py
./services/Dockerfile:6:COPY web_research_requirements.txt /app/web_research_requirements.txt
./services/Dockerfile:10:COPY neurobiological_brain/ /app/neurobiological_brain/
./services/Dockerfile:11:COPY integration_layer/ /app/integration_layer/
./services/Dockerfile:12:COPY ms_jarvis_web_research_simple.py /app/ms_jarvis_web_research_simple.py
./services/Dockerfile.intake:3:COPY . /app/
./services/Dockerfile.bak_add_requests:12:COPY neurobiologicalbrain /app/neurobiologicalbrain
./services/Dockerfile.bak_add_requests:13:COPY . /app
./services/Dockerfile.qualia:18:COPY requirements.txt .
./services/Dockerfile.qualia:35:COPY . .
./services/Dockerfile-llm17-proxy:3:COPY llm17_health_proxy.py .
./services/integration_layer.placeholder_1768012705/Dockerfile:3:COPY . /app
./services/Dockerfile-llm2-proxy:3:COPY llm2_health_proxy.py .
./services/Dockerfile.fifth_dgm_real:9:COPY requirements.txt /app/requirements.txt
./services/Dockerfile.fifth_dgm_real:13:COPY ms_jarvis_fifth_dgm_orchestrator.py /app/ms_jarvis_fifth_dgm_orchestrator.py
./services/Dockerfile.fifth_dgm_real:14:COPY dynamic_port_service.py /app/dynamic_port_service.py
./services/Dockerfile.fifth_dgm_real:15:COPY fifth_dgm_integration.py /app/fifth_dgm_integration.py
./services/Dockerfile.fifth_dgm_real:16:COPY service_discovery.py /app/service_discovery.py
./services/Dockerfile-llm3-proxy:3:COPY llm3_health_proxy.py .
./services/integration_layer/Dockerfile:3:COPY . /app
./services/jarvis_steward/Dockerfile:8:COPY main.py .
./services/Dockerfile.web_research:5:COPY web_research_requirements.txt /app/web_research_requirements.txt
./services/Dockerfile.web_research:8:COPY neurobiological_brain/ /app/neurobiological_brain/
./services/Dockerfile.web_research:9:COPY integration_layer/ /app/integration_layer/
./services/Dockerfile.web_research:10:COPY ms_jarvis_web_research_simple.py /app/ms_jarvis_web_research_simple.py
./services/Dockerfile.temporal_consciousness:3:COPY requirements_temporal.txt /app/requirements_temporal.txt
./services/Dockerfile.temporal_consciousness:5:COPY temporal_consciousness.py /app/temporal_consciousness.py
./services/Dockerfile.bak_add_service_discovery:12:COPY neurobiologicalbrain /app/neurobiologicalbrain
./services/Dockerfile.memory:3:COPY ms_jarvis_memory_service.py /app/
./services/Dockerfile.memory:4:COPY chroma_client.py /app/
./services/Dockerfile-llm10-proxy:3:COPY llm10_health_proxy.py .
./services/Dockerfile-llm8-proxy:3:COPY llm8_health_proxy.py .
./services/Dockerfile.mother_protocols:3:COPY ../requirements.txt /app/requirements.txt
./services/Dockerfile.mother_protocols:5:COPY mother_protocols.py /app/mother_protocols.py
./services/Dockerfile.toroidal:10:COPY requirements_toroidal.txt /app/requirements.txt
./services/Dockerfile.toroidal:17:COPY toroidal_service.py /app/toroidal_service.py
./services/Dockerfile.aaacpe_rag:14:COPY aaacpe_rag_service.py /app/
./services/Dockerfile.semaphore:9:COPY requirements_semaphore.txt /app/requirements.txt
./services/Dockerfile.semaphore:12:COPY msjarvis_semaphore.py /app/msjarvis_semaphore.py
./services/Dockerfile-llm4-proxy:3:COPY llm4_health_proxy.py .
./services/Dockerfile.rag:7:COPY requirements.txt /app/
./services/Dockerfile.rag:10:COPY neurobiological_brain/ /app/neurobiological_brain/
./services/Dockerfile.rag:11:COPY integration_layer/ /app/integration_layer/
./services/Dockerfile.rag:12:COPY *.py /app/
./services/Dockerfile.icontainers:13:COPY . /app
./services/Dockerfile.icontainers:16:COPY neurobiologicalbrain /app/neurobiologicalbrain
./services/Dockerfile.icontainers:17:COPY integration_layer/ /app/integration_layer/
./services/Dockerfile.icontainers:18:COPY ms_jarvis_i_containers_service.py /app/ms_jarvis_i_containers_service.py
./services/Dockerfile.icontainers:19:COPY msjarvisconsciousnessbridge.py /app/msjarvisconsciousnessbridge.py
./services/Dockerfile.bak_before_bbb_copy_fix:6:COPY services /app/services
./services/Dockerfile.bak_before_bbb_copy_fix:9:COPY neurobiological_brain/__init__.py /app/neurobiological_brain/__init__.py
./services/Dockerfile.bak_before_bbb_copy_fix:10:COPY neurobiological_brain/blood_brain_barrier /app/neurobiological_brain/blood_brain_barrier
./services/ai/Dockerfile:3:COPY . /app
./services/Dockerfile.judge:14:COPY judge_*.py /app/
./services/Dockerfile.judge:15:COPY lm_synthesizer.py /app/
./services/python/Dockerfile:3:COPY . /app
./services/Dockerfile-llm15-proxy:3:COPY llm15_health_proxy.py .
./services/Dockerfile-llm12-proxy:3:COPY llm12_health_proxy.py .
./services/Dockerfile.autonomous_complete:14:COPY *.py /app/
./services/Dockerfile.woah:9:COPY services/requirements.txt /app/requirements.txt
./services/Dockerfile.woah:12:COPY services/ms_jarvis_woah_algorithms.py /app/ms_jarvis_woah_algorithms.py
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile:3:COPY . /app
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile.bak_add_flask:3:COPY . /app
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile.bak_force_flask:3:COPY . /app
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile:3:COPY . /app
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile.bak_add_flask:3:COPY . /app
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile.bak_force_flask:3:COPY . /app
./services/neurobiologicalbrain/i_containers/service/Dockerfile:5:COPY requirements.txt /app/requirements.txt
./services/neurobiologicalbrain/i_containers/service/Dockerfile:8:COPY . /app
./services/neurobiologicalbrain/i_containers/service/Dockerfile.bak_add_flask:5:COPY requirements.txt /app/requirements.txt
./services/neurobiologicalbrain/i_containers/service/Dockerfile.bak_add_flask:8:COPY . /app
./services/neurobiologicalbrain/i_containers/service/Dockerfile.bak_force_flask:5:COPY requirements.txt /app/requirements.txt
./services/neurobiologicalbrain/i_containers/service/Dockerfile.bak_force_flask:8:COPY . /app
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile:5:COPY . /app
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile.bak_add_flask:4:COPY . /app
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile.bak_force_flask:4:COPY . /app
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile:3:COPY . /app
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile.bak_add_flask:3:COPY . /app
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile.bak_force_flask:3:COPY . /app
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile:5:COPY . /app
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile.bak_add_flask:4:COPY . /app
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile.bak_force_flask:4:COPY . /app
./services/neurobiologicalbrain/subconscious/service/Dockerfile:5:COPY . /app
./services/neurobiologicalbrain/subconscious/service/Dockerfile.bak_add_flask:4:COPY . /app
./services/neurobiologicalbrain/subconscious/service/Dockerfile.bak_force_flask:4:COPY . /app
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile:5:COPY . /app
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile.bak_add_flask:4:COPY . /app
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile.bak_force_flask:4:COPY . /app
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile:5:COPY . /app
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile.bak_add_flask:4:COPY . /app
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile.bak_force_flask:4:COPY . /app
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile:5:COPY . /app
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile.bak_add_flask:4:COPY . /app
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile.bak_force_flask:4:COPY . /app
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile:5:COPY . /app
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile.bak_add_flask:4:COPY . /app
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile.bak_force_flask:4:COPY . /app
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile:5:COPY . /app
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile.bak_add_flask:4:COPY . /app
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile.bak_force_flask:4:COPY . /app
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/Dockerfile:3:COPY . /app
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile:3:COPY . /app
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/emotional_resonance/Dockerfile:3:COPY . /app
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/experience_generator/Dockerfile:3:COPY . /app
./services/neurobiologicalbrain/neurobiological_brain/Dockerfile:3:COPY . /app
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_use_nbb_base:7:COPY . /app
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_flask_explicit:5:COPY . /app
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_entrypoint:7:COPY . /app
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile:4:COPY . .
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_add_flask:4:COPY . /app
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_bootstrap_cmd2:7:COPY . /app
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_force_flask:4:COPY . /app
./services/Dockerfile-llm13-proxy:3:COPY llm13_health_proxy.py .
./services/Dockerfile-llm6-proxy:3:COPY llm6_health_proxy.py .
./services/Dockerfile.nbb_base:12:COPY neurobiological_brain /app/neurobiological_brain
./services/Dockerfile.nbb_base:15:COPY . /app
./services/Dockerfile-llm22-proxy:3:COPY llm22_health_proxy.py .
./services/Dockerfile.autonomous_learner_complete:15:COPY ms_jarvis_autonomous_learner.py /app/
./services/Dockerfile.autonomous_learner_complete:16:COPY fifth_dgm_integration.py /app/ 2>/dev/null || echo "No fifth_dgm_integration.py"
./services/Dockerfile.autonomous_learner_complete:17:COPY i_container_interest_algorithm.py /app/ 2>/dev/null || echo "No i_container file"
./services/Dockerfile.autonomous_learner_complete:18:COPY autonomous_learner_topic_source.py /app/ 2>/dev/null || echo "No topic source"
./services/Dockerfile-llm20-proxy:3:COPY llm20_health_proxy.py .
./services/Dockerfile-llm21-proxy:3:COPY llm21_health_proxy.py .
./services/ai-server/Dockerfile:5:COPY requirements.txt .
./services/ai-server/Dockerfile:8:COPY . /app
./services/Dockerfile.bak_runner_cmd:9:COPY services /app/services
./services/Dockerfile-chroma-proxy:3:COPY chroma_health_proxy.py .
./services/Dockerfile-llm14-proxy:3:COPY llm14_health_proxy.py .
./services/Dockerfile.webdeploy:7:COPY ms_jarvis_web_deployer.py /app/
./services/Dockerfile-llm7-proxy:3:COPY llm7_health_proxy.py .
./services/Dockerfile.constitutional_guardian:6:COPY requirements.txt /app/requirements.txt
./services/Dockerfile.constitutional_guardian:11:COPY constitutional_api.py /app/constitutional_api.py
./services/Dockerfile.bbb:5:COPY bbb_requirements.txt /app/bbb_requirements.txt
./services/Dockerfile.bbb:8:COPY . /app/services
./services/Dockerfile-llm5-proxy:3:COPY llm5_health_proxy.py .
./services/Dockerfile.crypto-policy:3:COPY . /app/
./services/Dockerfile.bak_add_redis:12:COPY neurobiologicalbrain /app/neurobiologicalbrain
./services/Dockerfile-llm11-proxy:3:COPY llm11_health_proxy.py .
./services/Dockerfile-llm9-proxy:3:COPY llm9_health_proxy.py .
./services/Dockerfile.aaacpe_scraper:14:COPY aaacpe_scraper_service.py /app/
./services/Dockerfile.psychological_rag:5:COPY psychological_rag_domain.py .
./services/Dockerfile-llm18-proxy:3:COPY llm18_health_proxy.py .
./services/neurobiological_brain/qualia_engine/Dockerfile:3:COPY . /app
./services/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile:3:COPY . /app
./services/neurobiological_brain/qualia_engine/emotional_resonance/Dockerfile:3:COPY . /app
./services/neurobiological_brain/qualia_engine/experience_generator/Dockerfile:3:COPY . /app
./services/neurobiological_brain/Dockerfile:3:COPY . /app
./services/alert_venv/Dockerfile:3:COPY . /app
./services/Dockerfile.69dgm_bridge:3:COPY ../requirements.txt /app/requirements.txt
./services/Dockerfile.69dgm_bridge:5:COPY bridge_69dgm.py /app/bridge_69dgm.py
./services/Dockerfile.69dgm_bridge:6:COPY chroma_client.py /app/chroma_client.py
./services/Dockerfile.spiritual_rag:4:COPY spiritual_rag_domain.py /app/
./services/Dockerfile.gateway:3:COPY services /app/services
./services/Dockerfile.roche_llm:6:COPY ../requirements.txt /app/requirements.txt
./services/Dockerfile.roche_llm:10:COPY roche_llm.py /app/roche_llm.py
./services/Dockerfile.roche_llm:11:COPY llm_consensus_22.py /app/llm_consensus_22.py
./services/Dockerfile.woah_algorithms:11:COPY services/requirements.txt /app/requirements.txt
./services/Dockerfile.woah_algorithms:14:COPY services/ms_jarvis_woah_algorithms.py /app/ms_jarvis_woah_algorithms.py
./services/Dockerfile.bak_add_deps:9:COPY services /app/services
./services/Dockerfile.psychology_services:5:COPY ms_jarvis_psychology_services.py .
./services/Dockerfile.psychology_services:6:COPY psychology_integration_adapter.py .
./services/Dockerfile.email:7:COPY ms_jarvis_email_service.py /app/
./services/Dockerfile.email:8:COPY email_rag_integration.py /app/
./Dockerfile.ragservermain:7:COPY requirements.txt /app/
./Dockerfile.ragservermain:11:COPY ragservermain.py /app/
./Dockerfile.ragservermain:12:COPY neurobiological_brain/ /app/neurobiological_brain/
./Dockerfile.ragservermain:13:COPY integration_layer/ /app/integration_layer/
./neurobiologicalbrainmothercarrieprotocolsservice/Dockerfile:6:COPY services ./services
./neurobiologicalbrainmothercarrieprotocolsservice/Dockerfile:7:COPY neurobiologicalbrainmothercarrieprotocolsservice/main.py ./main.py
./neurobiologicalbrainmothercarrieprotocolsservice/Dockerfile:8:COPY services/requirements.nbb.txt ./requirements.txt
./Dockerfile-llm10-proxy:3:COPY llm10_health_proxy.py .
./Dockerfile-llm8-proxy:3:COPY llm8_health_proxy.py .
./Dockerfile-llm4-proxy:3:COPY llm4_health_proxy.py .
./Dockerfile.rag:7:COPY requirements.txt /app/
./Dockerfile.rag:10:COPY neurobiological_brain/ /app/neurobiological_brain/
./Dockerfile.rag:11:COPY integration_layer/ /app/integration_layer/
./Dockerfile.rag:12:COPY *.py /app/
./Dockerfile.rag_server_main:9:COPY services/ ./
./ai/Dockerfile:3:COPY . /app
./Dockerfile-llm15-proxy:3:COPY llm15_health_proxy.py .
./Dockerfile-llm12-proxy:3:COPY llm12_health_proxy.py .
./Dockerfile.woah:9:COPY services /app/services
./Dockerfile.neuro:5:COPY services/requirements.txt /app/requirements.txt
./Dockerfile.neuro:8:COPY neurobiological_brain /app/neurobiological_brain
./Dockerfile.neuro:9:COPY services /app/services
./Dockerfile-llm13-proxy:3:COPY llm13_health_proxy.py .
./Dockerfile-llm6-proxy:3:COPY llm6_health_proxy.py .
./Dockerfile-llm22-proxy:3:COPY llm22_health_proxy.py .
./Dockerfile-llm20-proxy:3:COPY llm20_health_proxy.py .
./Dockerfile.neuro-prefrontal-patched:2:COPY neuro-prefrontalcortex-patched.tar /tmp/app.tar
./Dockerfile-llm21-proxy:3:COPY llm21_health_proxy.py .
./Dockerfile.consciousnessbridge:3:COPY ../requirements.txt /app/requirements.txt
./Dockerfile.consciousnessbridge:5:COPY temporal_consciousness.py /app/temporal_consciousness.py
./ai-server/Dockerfile:3:COPY . /app
./Dockerfile-llm14-proxy:3:COPY llm14_health_proxy.py .
./Dockerfile.local_resources:4:COPY services/local_resources_resolver.py /app/local_resources_resolver.py
./Dockerfile.brain:4:COPY services/ /app/services/
./Dockerfile-llm7-proxy:3:COPY llm7_health_proxy.py .
./Dockerfile-llm5-proxy:3:COPY llm5_health_proxy.py .
./Dockerfile.bak_before_python3_fix:4:COPY services /app/services
./Dockerfile.bak_before_python3_fix:7:COPY gateway-entrypoint.sh /app/gateway-entrypoint.sh
./Dockerfile-llm11-proxy:3:COPY llm11_health_proxy.py .
./Dockerfile-llm9-proxy:3:COPY llm9_health_proxy.py .
./Dockerfile.rag_server:12:COPY services /app/services
./Dockerfile.20llm:4:COPY services/ /app/services/
./Dockerfile-llm18-proxy:3:COPY llm18_health_proxy.py .
./neurobiological_brain/qualia_engine/service/Dockerfile:3:COPY . /app
./neurobiological_brain/blood_brain_barrier/service/Dockerfile:3:COPY . /app
./neurobiological_brain/i_containers/service/Dockerfile.nbb_icontainers_fastapi:8:COPY . /app
./neurobiological_brain/i_containers/service/Dockerfile:5:COPY requirements.txt /app/requirements.txt
./neurobiological_brain/i_containers/service/Dockerfile:8:COPY . /app
./neurobiological_brain/spiritual_maternal_integration/service/Dockerfile:4:COPY . /app
./neurobiological_brain/spiritual_maternal_integration/service/Dockerfile:17:COPY service_discovery.py /app/service_discovery.py
./neurobiological_brain/spiritual_maternal_integration/service/Dockerfile:23:COPY service_registry_client.py /app/service_registry_client.py
./neurobiological_brain/darwin_godel_machines/service/Dockerfile:3:COPY . /app
./neurobiological_brain/spiritual_root/service/Dockerfile:4:COPY . /app
./neurobiological_brain/spiritual_root/service/Dockerfile:7:COPY requirements.txt /tmp/requirements.txt
./neurobiological_brain/subconscious/service/Dockerfile:4:COPY . /app
./neurobiological_brain/subconscious/service/Dockerfile:7:COPY requirements.txt /tmp/requirements.txt
./neurobiological_brain/woah_algorithms/service/Dockerfile:5:COPY . /app
./neurobiological_brain/consciousness_containers/service/Dockerfile:4:COPY . /app
./neurobiological_brain/consciousness_containers/service/Dockerfile:7:COPY requirements.txt /tmp/requirements.txt
./neurobiological_brain/pituitary_gland/service/Dockerfile:4:COPY . /app
./neurobiological_brain/pituitary_gland/service/Dockerfile:6:COPY requirements.txt /tmp/requirements.txt
./neurobiological_brain/heteroglobulin_transport/service/Dockerfile:4:COPY . /app
./neurobiological_brain/heteroglobulin_transport/service/Dockerfile:17:COPY service_discovery.py /app/service_discovery.py
./neurobiological_brain/heteroglobulin_transport/service/Dockerfile:23:COPY service_registry_client.py /app/service_registry_client.py
./neurobiological_brain/prefrontal_cortex/service/Dockerfile:4:COPY . /app
./neurobiological_brain/prefrontal_cortex/service/Dockerfile:15:COPY service_discovery.py /app/service_discovery.py
./neurobiological_brain/prefrontal_cortex/service/Dockerfile:21:COPY service_registry_client.py /app/service_registry_client.py
./neurobiological_brain/neurobiological_brain/qualia_engine/Dockerfile:3:COPY . /app
./neurobiological_brain/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile:3:COPY . /app
./neurobiological_brain/neurobiological_brain/qualia_engine/emotional_resonance/Dockerfile:3:COPY . /app
./neurobiological_brain/neurobiological_brain/qualia_engine/experience_generator/Dockerfile:3:COPY . /app
./neurobiological_brain/neurobiological_brain/Dockerfile:3:COPY . /app
./neurobiological_brain/mother_carrie_protocols/service/Dockerfile:4:COPY . /app
./neurobiological_brain/mother_carrie_protocols/service/Dockerfile:17:COPY service_discovery.py /app/service_discovery.py
./neurobiological_brain/mother_carrie_protocols/service/Dockerfile:23:COPY service_registry_client.py /app/service_registry_client.py
./Dockerfile.swarm:5:COPY services/requirements.txt /app/requirements.txt
./Dockerfile.swarm:8:COPY services /app/services
./Dockerfile.gateway:4:COPY services /app/services
./Dockerfile.gateway:7:COPY gateway-entrypoint.sh /app/gateway-entrypoint.sh
grep: ./data/mysql/aaacpe: Permission denied
grep: ./data/mysql/gis_rag: Permission denied
grep: ./data/local_resources: Permission denied
./Dockerfile.hilbert_spatial_chat:2:WORKDIR /app
./Dockerfile.gis_rag:3:WORKDIR /app
./Dockerfile-llm19-proxy:2:WORKDIR /app
./Dockerfile-llm1-proxy:2:WORKDIR /app
./Dockerfile.nbb_icontainers_fastapi:5:WORKDIR /app
./Dockerfile.full_neuro:3:WORKDIR /app
./Dockerfile.agents:3:WORKDIR /app
./Dockerfile-llm16-proxy:2:WORKDIR /app
./Dockerfile:4:WORKDIR /app
./Dockerfile-llm17-proxy:2:WORKDIR /app
./Dockerfile-llm2-proxy:2:WORKDIR /app
./Dockerfile-llm3-proxy:2:WORKDIR /app
./integration_layer/Dockerfile:2:WORKDIR /app
./services/Dockerfile.lm_synthesizer:3:WORKDIR /app
./services/Dockerfile.pia-sampler:2:WORKDIR /app
./services/Dockerfile.pia-sampler:4:WORKDIR /app/services
./services/Dockerfile.dgm_orchestrator:2:WORKDIR /app
./services/Dockerfile.autonomous_learner:3:WORKDIR /app
./services/Dockerfile.roche_llm.disabled:3:WORKDIR /app
./services/Dockerfile-llm19-proxy:2:WORKDIR /app
./services/Dockerfile-llm1-proxy:2:WORKDIR /app
./services/integration_layer.backup.1768269372/Dockerfile:2:WORKDIR /app
./services/Dockerfile.agents:2:WORKDIR /app/services
./services/Dockerfile.hippocampus:3:WORKDIR /app
./services/Dockerfile.icontainers_fastapi:3:WORKDIR /app
./services/Dockerfile-llm16-proxy:2:WORKDIR /app
./services/Dockerfile.dgm_worker:2:WORKDIR /app
./services/Dockerfile:3:WORKDIR /app
./services/Dockerfile.intake:2:WORKDIR /app
./services/Dockerfile.bak_add_requests:3:WORKDIR /app
./services/Dockerfile.bak_add_requests:15:WORKDIR /app/neurobiologicalbrain
./services/Dockerfile.qualia:3:WORKDIR /app
./services/Dockerfile.qualia:36:WORKDIR /app/services
./services/Dockerfile-llm17-proxy:2:WORKDIR /app
./services/integration_layer.placeholder_1768012705/Dockerfile:2:WORKDIR /app
./services/Dockerfile-llm2-proxy:2:WORKDIR /app
./services/Dockerfile.fifth_dgm_real:3:WORKDIR /app
./services/Dockerfile-llm3-proxy:2:WORKDIR /app
./services/integration_layer/Dockerfile:2:WORKDIR /app
./services/jarvis_steward/Dockerfile:3:WORKDIR /app
./services/Dockerfile.web_research:3:WORKDIR /app
./services/Dockerfile.temporal_consciousness:2:WORKDIR /app
./services/Dockerfile.bak_add_service_discovery:3:WORKDIR /app
./services/Dockerfile.bak_add_service_discovery:14:WORKDIR /app/neurobiologicalbrain
./services/Dockerfile.memory:2:WORKDIR /app
./services/Dockerfile-llm10-proxy:2:WORKDIR /app
./services/Dockerfile-llm8-proxy:2:WORKDIR /app
./services/Dockerfile.mother_protocols:2:WORKDIR /app
./services/Dockerfile.toroidal:3:WORKDIR /app
./services/Dockerfile.aaacpe_rag:3:WORKDIR /app
./services/Dockerfile.semaphore:3:WORKDIR /app
./services/Dockerfile-llm4-proxy:2:WORKDIR /app
./services/Dockerfile.rag:3:WORKDIR /app
./services/Dockerfile.icontainers:10:WORKDIR /app
./services/Dockerfile.bak_before_bbb_copy_fix:3:WORKDIR /app
./services/ai/Dockerfile:2:WORKDIR /app
./services/Dockerfile.judge:3:WORKDIR /app
./services/python/Dockerfile:2:WORKDIR /app
./services/Dockerfile-llm15-proxy:2:WORKDIR /app
./services/Dockerfile-llm12-proxy:2:WORKDIR /app
./services/Dockerfile.autonomous_complete:3:WORKDIR /app
./services/Dockerfile.woah:3:WORKDIR /app
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile:2:WORKDIR /app
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile.bak_add_flask:2:WORKDIR /app
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile.bak_force_flask:2:WORKDIR /app
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile:2:WORKDIR /app
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile.bak_add_flask:2:WORKDIR /app
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile.bak_force_flask:2:WORKDIR /app
./services/neurobiologicalbrain/i_containers/service/Dockerfile:3:WORKDIR /app
./services/neurobiologicalbrain/i_containers/service/Dockerfile.bak_add_flask:3:WORKDIR /app
./services/neurobiologicalbrain/i_containers/service/Dockerfile.bak_force_flask:3:WORKDIR /app
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile:4:WORKDIR /app
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile.bak_add_flask:3:WORKDIR /app
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile.bak_force_flask:3:WORKDIR /app
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile:2:WORKDIR /app
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile.bak_add_flask:2:WORKDIR /app
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile.bak_force_flask:2:WORKDIR /app
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile:4:WORKDIR /app
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile.bak_add_flask:3:WORKDIR /app
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile.bak_force_flask:3:WORKDIR /app
./services/neurobiologicalbrain/subconscious/service/Dockerfile:4:WORKDIR /app
./services/neurobiologicalbrain/subconscious/service/Dockerfile.bak_add_flask:3:WORKDIR /app
./services/neurobiologicalbrain/subconscious/service/Dockerfile.bak_force_flask:3:WORKDIR /app
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile:4:WORKDIR /app
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile.bak_add_flask:3:WORKDIR /app
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile.bak_force_flask:3:WORKDIR /app
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile:4:WORKDIR /app
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile.bak_add_flask:3:WORKDIR /app
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile.bak_force_flask:3:WORKDIR /app
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile:4:WORKDIR /app
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile.bak_add_flask:3:WORKDIR /app
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile.bak_force_flask:3:WORKDIR /app
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile:4:WORKDIR /app
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile.bak_add_flask:3:WORKDIR /app
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile.bak_force_flask:3:WORKDIR /app
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile:4:WORKDIR /app
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile.bak_add_flask:3:WORKDIR /app
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile.bak_force_flask:3:WORKDIR /app
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/Dockerfile:2:WORKDIR /app
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile:2:WORKDIR /app
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/emotional_resonance/Dockerfile:2:WORKDIR /app
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/experience_generator/Dockerfile:2:WORKDIR /app
./services/neurobiologicalbrain/neurobiological_brain/Dockerfile:2:WORKDIR /app
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_use_nbb_base:4:WORKDIR /app
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_flask_explicit:4:WORKDIR /app
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_entrypoint:4:WORKDIR /app
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile:3:WORKDIR /app/neurobiologicalbrain/mother_carrie_protocols/service
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_add_flask:3:WORKDIR /app
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_bootstrap_cmd2:4:WORKDIR /app
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_force_flask:3:WORKDIR /app
./services/Dockerfile-llm13-proxy:2:WORKDIR /app
./services/Dockerfile-llm6-proxy:2:WORKDIR /app
./services/Dockerfile.nbb_base:3:WORKDIR /app
./services/Dockerfile.nbb_base:20:WORKDIR /app
./services/Dockerfile-llm22-proxy:2:WORKDIR /app
./services/Dockerfile.autonomous_learner_complete:3:WORKDIR /app
./services/Dockerfile-llm20-proxy:2:WORKDIR /app
./services/Dockerfile-llm21-proxy:2:WORKDIR /app
./services/ai-server/Dockerfile:3:WORKDIR /app
./services/Dockerfile.bak_runner_cmd:3:WORKDIR /app/services
./services/Dockerfile-chroma-proxy:2:WORKDIR /app
./services/Dockerfile-llm14-proxy:2:WORKDIR /app
./services/Dockerfile.webdeploy:3:WORKDIR /app
./services/Dockerfile-llm7-proxy:2:WORKDIR /app
./services/Dockerfile.constitutional_guardian:3:WORKDIR /app
./services/Dockerfile.bbb:3:WORKDIR /app/services
./services/Dockerfile-llm5-proxy:2:WORKDIR /app
./services/Dockerfile.crypto-policy:2:WORKDIR /app
./services/Dockerfile.bak_add_redis:3:WORKDIR /app
./services/Dockerfile.bak_add_redis:14:WORKDIR /app/neurobiologicalbrain
./services/Dockerfile-llm11-proxy:2:WORKDIR /app
./services/Dockerfile-llm9-proxy:2:WORKDIR /app
./services/Dockerfile.aaacpe_scraper:3:WORKDIR /app
./services/Dockerfile.psychological_rag:3:WORKDIR /app
./services/Dockerfile-llm18-proxy:2:WORKDIR /app
./services/neurobiological_brain/qualia_engine/Dockerfile:2:WORKDIR /app
./services/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile:2:WORKDIR /app
./services/neurobiological_brain/qualia_engine/emotional_resonance/Dockerfile:2:WORKDIR /app
./services/neurobiological_brain/qualia_engine/experience_generator/Dockerfile:2:WORKDIR /app
./services/neurobiological_brain/Dockerfile:2:WORKDIR /app
./services/alert_venv/Dockerfile:2:WORKDIR /app
./services/Dockerfile.69dgm_bridge:2:WORKDIR /app
./services/Dockerfile.spiritual_rag:2:WORKDIR /app
./services/Dockerfile.gateway:2:WORKDIR /app/services
./services/Dockerfile.roche_llm:3:WORKDIR /app
./services/Dockerfile.woah_algorithms:3:WORKDIR /app
./services/Dockerfile.bak_add_deps:3:WORKDIR /app/services
./services/Dockerfile.psychology_services:3:WORKDIR /app
./services/Dockerfile.email:3:WORKDIR /app
./Dockerfile.ragservermain:3:WORKDIR /app
./neurobiologicalbrainmothercarrieprotocolsservice/Dockerfile:3:WORKDIR /app
./Dockerfile-llm10-proxy:2:WORKDIR /app
./Dockerfile-llm8-proxy:2:WORKDIR /app
./Dockerfile-llm4-proxy:2:WORKDIR /app
./Dockerfile.rag:3:WORKDIR /app
./Dockerfile.rag_server_main:3:WORKDIR /app/services
./ai/Dockerfile:2:WORKDIR /app
./Dockerfile-llm15-proxy:2:WORKDIR /app
./Dockerfile-llm12-proxy:2:WORKDIR /app
./Dockerfile.woah:3:WORKDIR /app/services
./Dockerfile.neuro:3:WORKDIR /app
./Dockerfile-llm13-proxy:2:WORKDIR /app
./Dockerfile-llm6-proxy:2:WORKDIR /app
./Dockerfile-llm22-proxy:2:WORKDIR /app
./Dockerfile-llm20-proxy:2:WORKDIR /app
./Dockerfile.neuro-prefrontal-patched:4:WORKDIR /app
./Dockerfile-llm21-proxy:2:WORKDIR /app
./Dockerfile.consciousnessbridge:2:WORKDIR /app
./ai-server/Dockerfile:2:WORKDIR /app
./Dockerfile-llm14-proxy:2:WORKDIR /app
./Dockerfile.local_resources:3:WORKDIR /app
./Dockerfile.brain:3:WORKDIR /app
./Dockerfile.brain:5:WORKDIR /app/services
./Dockerfile-llm7-proxy:2:WORKDIR /app
./Dockerfile-llm5-proxy:2:WORKDIR /app
./Dockerfile.bak_before_python3_fix:3:WORKDIR /app/services
./Dockerfile-llm11-proxy:2:WORKDIR /app
./Dockerfile-llm9-proxy:2:WORKDIR /app
./Dockerfile.rag_server:3:WORKDIR /app
./Dockerfile.rag_server:13:WORKDIR /app/services
./Dockerfile.20llm:3:WORKDIR /app
./Dockerfile.20llm:5:WORKDIR /app/services
./Dockerfile-llm18-proxy:2:WORKDIR /app
./neurobiological_brain/qualia_engine/service/Dockerfile:2:WORKDIR /app
./neurobiological_brain/blood_brain_barrier/service/Dockerfile:2:WORKDIR /app
./neurobiological_brain/i_containers/service/Dockerfile.nbb_icontainers_fastapi:6:WORKDIR /app
./neurobiological_brain/i_containers/service/Dockerfile:3:WORKDIR /app
./neurobiological_brain/spiritual_maternal_integration/service/Dockerfile:3:WORKDIR /app
./neurobiological_brain/darwin_godel_machines/service/Dockerfile:2:WORKDIR /app
./neurobiological_brain/spiritual_root/service/Dockerfile:3:WORKDIR /app
./neurobiological_brain/subconscious/service/Dockerfile:3:WORKDIR /app
./neurobiological_brain/woah_algorithms/service/Dockerfile:3:WORKDIR /app
./neurobiological_brain/consciousness_containers/service/Dockerfile:3:WORKDIR /app
./neurobiological_brain/pituitary_gland/service/Dockerfile:3:WORKDIR /app
./neurobiological_brain/heteroglobulin_transport/service/Dockerfile:3:WORKDIR /app
./neurobiological_brain/prefrontal_cortex/service/Dockerfile:3:WORKDIR /app
./neurobiological_brain/neurobiological_brain/qualia_engine/Dockerfile:2:WORKDIR /app
./neurobiological_brain/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile:2:WORKDIR /app
./neurobiological_brain/neurobiological_brain/qualia_engine/emotional_resonance/Dockerfile:2:WORKDIR /app
./neurobiological_brain/neurobiological_brain/qualia_engine/experience_generator/Dockerfile:2:WORKDIR /app
./neurobiological_brain/neurobiological_brain/Dockerfile:2:WORKDIR /app
./neurobiological_brain/mother_carrie_protocols/service/Dockerfile:3:WORKDIR /app
./Dockerfile.swarm:3:WORKDIR /app
./Dockerfile.gateway:3:WORKDIR /app/services
grep: ./data/mysql/aaacpe: Permission denied
grep: ./data/mysql/gis_rag: Permission denied
grep: ./data/local_resources: Permission denied
./Dockerfile.hilbert_spatial_chat:1:FROM python:3.11-slim
./Dockerfile.gis_rag:1:FROM python:3.11-slim
./Dockerfile-llm19-proxy:1:FROM python:3.12-slim
./Dockerfile-llm1-proxy:1:FROM python:3.12-slim
./Dockerfile.nbb_icontainers_fastapi:1:FROM python:3.12-slim
./Dockerfile.full_neuro:1:FROM python:3.11-slim
./Dockerfile.agents:1:FROM python:3.11-slim
./Dockerfile-llm16-proxy:1:FROM python:3.12-slim
./Dockerfile:1:FROM python:3.10-slim
./Dockerfile-llm17-proxy:1:FROM python:3.12-slim
./Dockerfile-llm2-proxy:1:FROM python:3.12-slim
./Dockerfile-llm3-proxy:1:FROM python:3.12-slim
./integration_layer/Dockerfile:1:FROM python:3.12-slim
./services/Dockerfile.lm_synthesizer:1:FROM python:3.12-slim
./services/Dockerfile.pia-sampler:1:FROM python:3.11-slim
./services/Dockerfile.dgm_orchestrator:1:FROM python:3.10-slim
./services/Dockerfile.autonomous_learner:1:FROM python:3.11-slim
./services/Dockerfile.roche_llm.disabled:1:FROM python:3.12-slim
./services/Dockerfile-llm19-proxy:1:FROM python:3.12-slim
./services/Dockerfile-llm1-proxy:1:FROM python:3.12-slim
./services/integration_layer.backup.1768269372/Dockerfile:1:FROM python:3.12-slim
./services/Dockerfile.agents:1:FROM python:3.10-slim
./services/Dockerfile.hippocampus:1:FROM python:3.11-slim
./services/Dockerfile.icontainers_fastapi:1:FROM python:3.11-slim
./services/Dockerfile-llm16-proxy:1:FROM python:3.12-slim
./services/Dockerfile.dgm_worker:1:FROM python:3.11-slim
./services/Dockerfile:1:FROM python:3.11-slim
./services/Dockerfile.intake:1:FROM python:3.11-slim
./services/Dockerfile.bak_add_requests:1:FROM python:3.10-slim
./services/Dockerfile.qualia:1:FROM python:3.10-slim
./services/Dockerfile-llm17-proxy:1:FROM python:3.12-slim
./services/integration_layer.placeholder_1768012705/Dockerfile:1:FROM python:3.12-slim
./services/Dockerfile-llm2-proxy:1:FROM python:3.12-slim
./services/Dockerfile.fifth_dgm_real:1:FROM python:3.11-slim
./services/Dockerfile-llm3-proxy:1:FROM python:3.12-slim
./services/integration_layer/Dockerfile:1:FROM python:3.12-slim
./services/jarvis_steward/Dockerfile:1:FROM python:3.11-slim
./services/Dockerfile.web_research:1:FROM python:3.11-slim
./services/Dockerfile.temporal_consciousness:1:FROM python:3.12-slim
./services/Dockerfile.bak_add_service_discovery:1:FROM python:3.10-slim
./services/Dockerfile.memory:1:FROM python:3.11-slim
./services/Dockerfile-llm10-proxy:1:FROM python:3.12-slim
./services/Dockerfile-llm8-proxy:1:FROM python:3.12-slim
./services/Dockerfile.mother_protocols:1:FROM python:3.12-slim
./services/Dockerfile.toroidal:1:FROM python:3.11-slim
./services/Dockerfile.aaacpe_rag:1:FROM python:3.10-slim
./services/Dockerfile.semaphore:1:FROM python:3.11-slim
./services/Dockerfile-llm4-proxy:1:FROM python:3.12-slim
./services/Dockerfile.rag:1:FROM python:3.11-slim
./services/Dockerfile.icontainers:1:FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04
./services/Dockerfile.bak_before_bbb_copy_fix:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/ai/Dockerfile:1:FROM python:3.12-slim
./services/Dockerfile.judge:1:FROM python:3.11-slim
./services/python/Dockerfile:1:FROM python:3.12-slim
./services/Dockerfile-llm15-proxy:1:FROM python:3.12-slim
./services/Dockerfile-llm12-proxy:1:FROM python:3.12-slim
./services/Dockerfile.autonomous_complete:1:FROM python:3.11-slim
./services/Dockerfile.woah:1:FROM python:3.11-slim
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile:1:FROM python:3.12-slim
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile.bak_add_flask:1:FROM python:3.12-slim
./services/neurobiologicalbrain/qualia_engine/service/Dockerfile.bak_force_flask:1:FROM python:3.12-slim
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile:1:FROM python:3.12-slim
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile.bak_add_flask:1:FROM python:3.12-slim
./services/neurobiologicalbrain/blood_brain_barrier/service/Dockerfile.bak_force_flask:1:FROM python:3.12-slim
./services/neurobiologicalbrain/i_containers/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/i_containers/service/Dockerfile.bak_add_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/i_containers/service/Dockerfile.bak_force_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile.bak_add_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/spiritual_maternal_integration/service/Dockerfile.bak_force_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile:1:FROM python:3.12-slim
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile.bak_add_flask:1:FROM python:3.12-slim
./services/neurobiologicalbrain/darwin_godel_machines/service/Dockerfile.bak_force_flask:1:FROM python:3.12-slim
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile.bak_add_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/spiritual_root/service/Dockerfile.bak_force_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/subconscious/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/subconscious/service/Dockerfile.bak_add_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/subconscious/service/Dockerfile.bak_force_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile.bak_add_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/woah_algorithms/service/Dockerfile.bak_force_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile.bak_add_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/consciousness_containers/service/Dockerfile.bak_force_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile.bak_add_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/pituitary_gland/service/Dockerfile.bak_force_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile.bak_add_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/heteroglobulin_transport/service/Dockerfile.bak_force_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile.bak_add_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/prefrontal_cortex/service/Dockerfile.bak_force_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/Dockerfile:1:FROM python:3.12-slim
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile:1:FROM python:3.12-slim
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/emotional_resonance/Dockerfile:1:FROM python:3.12-slim
./services/neurobiologicalbrain/neurobiological_brain/qualia_engine/experience_generator/Dockerfile:1:FROM python:3.12-slim
./services/neurobiologicalbrain/neurobiological_brain/Dockerfile:1:FROM python:3.12-slim
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_use_nbb_base:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_flask_explicit:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_entrypoint:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile:1:FROM msjarvis-nbb-base
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_add_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_bootstrap_cmd2:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/neurobiologicalbrain/mother_carrie_protocols/service/Dockerfile.bak_force_flask:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./services/Dockerfile-llm13-proxy:1:FROM python:3.12-slim
./services/Dockerfile-llm6-proxy:1:FROM python:3.12-slim
./services/Dockerfile.nbb_base:1:FROM python:3.10-slim
./services/Dockerfile-llm22-proxy:1:FROM python:3.12-slim
./services/Dockerfile.autonomous_learner_complete:1:FROM python:3.11-slim
./services/Dockerfile-llm20-proxy:1:FROM python:3.12-slim
./services/Dockerfile-llm21-proxy:1:FROM python:3.12-slim
./services/ai-server/Dockerfile:1:FROM python:3.11-slim
./services/Dockerfile.bak_runner_cmd:1:FROM python:3.10-slim
./services/Dockerfile-chroma-proxy:1:FROM python:3.12-slim
./services/Dockerfile-llm14-proxy:1:FROM python:3.12-slim
./services/Dockerfile.webdeploy:1:FROM python:3.11-slim
./services/Dockerfile-llm7-proxy:1:FROM python:3.12-slim
./services/Dockerfile.constitutional_guardian:1:FROM python:3.10-slim
./services/Dockerfile.bbb:1:FROM python:3.11-slim
./services/Dockerfile-llm5-proxy:1:FROM python:3.12-slim
./services/Dockerfile.crypto-policy:1:FROM python:3.11-slim
./services/Dockerfile.bak_add_redis:1:FROM python:3.10-slim
./services/Dockerfile-llm11-proxy:1:FROM python:3.12-slim
./services/Dockerfile-llm9-proxy:1:FROM python:3.12-slim
./services/Dockerfile.aaacpe_scraper:1:FROM python:3.11-slim
./services/Dockerfile.psychological_rag:1:FROM python:3.12-slim
./services/Dockerfile-llm18-proxy:1:FROM python:3.12-slim
./services/neurobiological_brain/qualia_engine/Dockerfile:1:FROM python:3.12-slim
./services/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile:1:FROM python:3.12-slim
./services/neurobiological_brain/qualia_engine/emotional_resonance/Dockerfile:1:FROM python:3.12-slim
./services/neurobiological_brain/qualia_engine/experience_generator/Dockerfile:1:FROM python:3.12-slim
./services/neurobiological_brain/Dockerfile:1:FROM python:3.12-slim
./services/alert_venv/Dockerfile:1:FROM python:3.12-slim
./services/Dockerfile.69dgm_bridge:1:FROM python:3.12-slim
./services/Dockerfile.spiritual_rag:1:FROM python:3.10-slim
./services/Dockerfile.gateway:1:FROM python:3.10-slim
./services/Dockerfile.roche_llm:1:FROM python:3.12-slim
./services/Dockerfile.woah_algorithms:1:FROM python:3.11-slim
./services/Dockerfile.bak_add_deps:1:FROM python:3.10-slim
./services/Dockerfile.psychology_services:1:FROM python:3.12-slim
./services/Dockerfile.email:1:FROM python:3.11-slim
./Dockerfile.ragservermain:1:FROM python:3.11-slim
./neurobiologicalbrainmothercarrieprotocolsservice/Dockerfile:1:FROM python:3.12-slim
./Dockerfile-llm10-proxy:1:FROM python:3.12-slim
./Dockerfile-llm8-proxy:1:FROM python:3.12-slim
./Dockerfile-llm4-proxy:1:FROM python:3.12-slim
./Dockerfile.rag:1:FROM python:3.11-slim
./Dockerfile.rag_server_main:1:FROM python:3.10-slim
./ai/Dockerfile:1:FROM python:3.12-slim
./Dockerfile-llm15-proxy:1:FROM python:3.12-slim
./Dockerfile-llm12-proxy:1:FROM python:3.12-slim
./Dockerfile.woah:1:FROM python:3.10-slim
./Dockerfile.neuro:1:FROM python:3.11-slim
./Dockerfile-llm13-proxy:1:FROM python:3.12-slim
./Dockerfile-llm6-proxy:1:FROM python:3.12-slim
./Dockerfile-llm22-proxy:1:FROM python:3.12-slim
./Dockerfile-llm20-proxy:1:FROM python:3.12-slim
./Dockerfile.neuro-prefrontal-patched:1:FROM neuro-prefrontalcortex-service:latest
./Dockerfile-llm21-proxy:1:FROM python:3.12-slim
./Dockerfile.consciousnessbridge:1:FROM python:3.12-slim
./ai-server/Dockerfile:1:FROM python:3.11-slim
./Dockerfile-llm14-proxy:1:FROM python:3.12-slim
./Dockerfile.local_resources:1:FROM python:3.11-slim
./Dockerfile.brain:1:FROM python:3.10-slim
./Dockerfile-llm7-proxy:1:FROM python:3.12-slim
./Dockerfile-llm5-proxy:1:FROM python:3.12-slim
./Dockerfile.bak_before_python3_fix:1:FROM python:3.10
./Dockerfile-llm11-proxy:1:FROM python:3.12-slim
./Dockerfile-llm9-proxy:1:FROM python:3.12-slim
./Dockerfile.rag_server:1:FROM python:3.10-slim
./Dockerfile.20llm:1:FROM python:3.10-slim
./Dockerfile-llm18-proxy:1:FROM python:3.12-slim
./neurobiological_brain/qualia_engine/service/Dockerfile:1:FROM python:3.12-slim
./neurobiological_brain/blood_brain_barrier/service/Dockerfile:1:FROM python:3.12-slim
./neurobiological_brain/i_containers/service/Dockerfile.nbb_icontainers_fastapi:1:FROM python:3.12-slim
./neurobiological_brain/i_containers/service/Dockerfile:1:FROM python:3.11-slim
./neurobiological_brain/spiritual_maternal_integration/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./neurobiological_brain/darwin_godel_machines/service/Dockerfile:1:FROM python:3.12-slim
./neurobiological_brain/spiritual_root/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./neurobiological_brain/subconscious/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./neurobiological_brain/woah_algorithms/service/Dockerfile:1:FROM python:3.12-slim
./neurobiological_brain/consciousness_containers/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./neurobiological_brain/pituitary_gland/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./neurobiological_brain/heteroglobulin_transport/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./neurobiological_brain/prefrontal_cortex/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./neurobiological_brain/neurobiological_brain/qualia_engine/Dockerfile:1:FROM python:3.12-slim
./neurobiological_brain/neurobiological_brain/qualia_engine/meaning_maker/Dockerfile:1:FROM python:3.12-slim
./neurobiological_brain/neurobiological_brain/qualia_engine/emotional_resonance/Dockerfile:1:FROM python:3.12-slim
./neurobiological_brain/neurobiological_brain/qualia_engine/experience_generator/Dockerfile:1:FROM python:3.12-slim
./neurobiological_brain/neurobiological_brain/Dockerfile:1:FROM python:3.12-slim
./neurobiological_brain/mother_carrie_protocols/service/Dockerfile:1:FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim
./Dockerfile.swarm:1:FROM python:3.11-slim
./Dockerfile.gateway:1:FROM python:3.10
grep: ./data/mysql/aaacpe: Permission denied
grep: ./data/mysql/gis_rag: Permission denied
grep: ./data/local_resources: Permission denied
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ cd /mnt/nvme1/msjarvis-rebuild
set -euo pipefail

echo '=== Confirm host file is patched before rebuild ==='
grep -nE 'def register_time_event|state_set:|state_transition:|entanglement:' services/jarvis_hilbert_state.py || true
sed -n '1,220p' services/jarvis_hilbert_state.py

echo '=== Rebuild jarvis-main-brain from repo-root Dockerfile ==='
docker build --no-cache --pull -t jarvis-main-brain:latest -f ./Dockerfile .

echo '=== Recreate hilbert-state from rebuilt image ==='
docker compose rm -sf jarvis-hilbert-state
docker compose up -d --force-recreate --no-deps jarvis-hilbert-state
sleep 5

echo '=== Verify new image and baked file ==='
docker image inspect jarvis-main-brain:latest --format 'LATEST_IMAGE_ID={{.Id}} CREATED={{.Created}}'
docker inspect jarvis-hilbert-state --format 'CONTAINER_IMAGE_ID={{.Image}} CMD={{json .Config.Cmd}}'
docker exec jarvis-hilbert-state /bin/sh -lc "grep -nE 'def register_time_event|state_set:|state_transition:|entanglement:' /app/services/jarvis_hilbert_state.py"
docker exec jarvis-hilbert-state /bin/sh -lc "sed -n '1,220p' /app/services/jarvis_hilbert_state.pdocker logs --tail 80 jarvis-hilbert-state
=== Confirm host file is patched before rebuild ===
51:def register_time_event(entity_id: str, payload: str):
86:    register_time_event(sv.state_id, f"state_set:{sv.state_id}")
109:    register_time_event(t.to_state, f"state_transition:{t.from_state}->{t.to_state}:{t.operator}")
149:    key = f"hilbert:entanglement:{min(entity_a,entity_b)}:{max(entity_a,entity_b)}"
172:    key = f"hilbert:entanglement:{min(q.entity_a,q.entity_b)}:{max(q.entity_a,q.entity_b)}"
182:    register_time_event(q.entity_a, f"entanglement:{q.entity_a}<->{q.entity_b}:{score}")
183:    register_time_event(q.entity_b, f"entanglement:{q.entity_a}<->{q.entity_b}:{score}")
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
=== Rebuild jarvis-main-brain from repo-root Dockerfile ===
[+] Building 300.7s (12/12) FINISHED                                               docker:default
 => [internal] load build definition from Dockerfile                                         0.0s
 => => transferring dockerfile: 590B                                                         0.0s
 => [internal] load metadata for docker.io/library/python:3.10-slim                          0.9s
 => [internal] load .dockerignore                                                            0.0s
 => => transferring context: 127B                                                            0.0s
 => [1/7] FROM docker.io/library/python:3.10-slim@sha256:a0c2acf33d1ad5355112e8ae578908f867  0.0s
 => [internal] load build context                                                            2.1s
 => => transferring context: 6.58MB                                                          1.6s
 => CACHED [2/7] WORKDIR /app                                                                0.0s
 => [3/7] RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*      18.7s
 => [4/7] COPY requirements.txt /app/                                                        0.0s 
 => [5/7] RUN pip install --no-cache-dir -r requirements.txt                               153.0s 
 => [6/7] COPY services/ /app/services/                                                     85.7s 
 => [7/7] COPY neurobiological_brain/ /app/neurobiological_brain/                            0.4s 
 => exporting to image                                                                      41.8s 
 => => exporting layers                                                                     41.7s 
 => => writing image sha256:8396642c3d7f64c57af7d5ccb096d9e70618294ae12e7dcd33faab5964e5a39  0.0s 
 => => naming to docker.io/library/jarvis-main-brain:latest                                  0.0s 
=== Recreate hilbert-state from rebuilt image ===
[+] stop 1/1
[+] remove 1/1arvis-hilbert-state Stopped                                                     0.8s
 ✔ Container jarvis-hilbert-state Removed                                                     0.8s
[+] up 1/1
 ✔ Container jarvis-hilbert-state Started                                                     0.3s
=== Verify new image and baked file ===
LATEST_IMAGE_ID=sha256:8396642c3d7f64c57af7d5ccb096d9e70618294ae12e7dcd33faab5964e5a39f CREATED=2026-06-26T13:00:28.901806379-04:00
CONTAINER_IMAGE_ID=sha256:8396642c3d7f64c57af7d5ccb096d9e70618294ae12e7dcd33faab5964e5a39f CMD=["uvicorn","jarvis_hilbert_state:app","--host","0.0.0.0","--port","8081"]
51:def register_time_event(entity_id: str, payload: str):
86:    register_time_event(sv.state_id, f"state_set:{sv.state_id}")
109:    register_time_event(t.to_state, f"state_transition:{t.from_state}->{t.to_state}:{t.operator}")
149:    key = f"hilbert:entanglement:{min(entity_a,entity_b)}:{max(entity_a,entity_b)}"
172:    key = f"hilbert:entanglement:{min(q.entity_a,q.entity_b)}:{max(q.entity_a,q.entity_b)}"
182:    register_time_event(q.entity_a, f"entanglement:{q.entity_a}<->{q.entity_b}:{score}")
183:    register_time_event(q.entity_b, f"entanglement:{q.entity_a}<->{q.entity_b}:{score}")
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
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8081 (Press CTRL+C to quit)
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ 

