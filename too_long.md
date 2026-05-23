(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ cd /home/cakidd/(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild$ cd /home/cakidd/msallis-diag-20260522-200208
printf '\n===== NEXT-STEPS =====\n'
printf '\n===== NEXT-STEPS =====\n'
cat NEXT-STEPS.txt
printf '\n===== SLOW PATH GREP =====\n'
printf '\n===== SLOW PATH GREP =====\n'
sed -n '1,240p' slow-path-grep.txt
printf '\n===== DOCKER LIMIT COMMANDS =====\n'
printf '\n===== DOCKER LIMIT COMMANDS =====\n'
cat docker-update-recommendations.sh
printf '\n===== TOP CPU SNAPSHOT =====\n'
printf '\n===== TOP CPU SNAPSHOT =====\n'
sed -n '1,220p' ps-top-sample.txt
printf '\n===== DOCKER STATS SNAPSHOT =====\n'
printf '\n===== DOCKER STATS SNAPSHOT =====\n'
sed -n '1,220p' docker-stats-sample.txt
if [ -f iostat-sample.txt ]; then
if [ -f iostat-sample.txt ]; then =====\n'
  printf '\n===== IOSTAT SNAPSHOT =====\n'
  sed -n '1,220p' iostat-sample.txt
elseintf '\n===== VMSTAT SNAPSHOT =====\n'
  printf '\n===== VMSTAT SNAPSHOT =====\n'
  sed -n '1,220p' vmstat-sample.txt
fi

===== NEXT-STEPS =====
1) Open: /home/cakidd/msallis-diag-20260522-200208/slow-path-grep.txt
2) Open: /home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt
3) Open: /home/cakidd/msallis-diag-20260522-200208/ps-top-sample.txt
4) If iostat exists, open: /home/cakidd/msallis-diag-20260522-200208/iostat-sample.txt ; otherwise open: /home/cakidd/msallis-diag-20260522-200208/vmstat-sample.txt
5) Apply one-at-a-time containment on noncritical containers from: /home/cakidd/msallis-diag-20260522-200208/docker-update-recommendations.sh
6) Re-run one real request after limits are applied.
7) Compare timestamps around Phase 4 / Finalizing answer against container CPU, memory, and Block I/O spikes.

===== SLOW PATH GREP =====
/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.end.log:1:2026-05-19T03:57:54.791666574Z INFO:lm_synthesizer:Starting LM Synthesizer on 0.0.0.0:8001
/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.end.log:76:2026-05-22T22:25:11.815499916Z INFO:lm_synthesizer:Starting LM Synthesizer on 0.0.0.0:8001
/home/cakidd/msallis-diag-20260522-200208/12d6dc1b1e49_jarvis-chroma.log:3:2026-05-19T03:59:34.041061144Z persist_path: "/data"
/home/cakidd/msallis-diag-20260522-200208/12d6dc1b1e49_jarvis-chroma.log:31:2026-05-22T22:25:11.072470362Z persist_path: "/data"
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:321:2026-05-22T01:40:31.067292655Z INFO:primp:response: https://www.bing.com/search?q=capture+every+status+response+to+debug+polling 200
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:322:2026-05-22T01:40:31.182196406Z INFO:__main__:🔍 Search: 'capture every status response to debug polling' → 5 results
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:327:2026-05-22T03:16:43.216931338Z INFO:primp:response: https://www.bing.com/search?q=capture+every+status+response+to+debug+polling 200
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:328:2026-05-22T03:16:43.608909548Z INFO:__main__:🔍 Search: 'capture every status response to debug polling' → 0 results
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:334:2026-05-22T03:36:18.995834946Z INFO:primp:response: https://www.bing.com/search?q=fast+poll+test 200
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:335:2026-05-22T03:36:19.049901472Z INFO:__main__:🔍 Search: 'fast poll test' → 5 results
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:340:2026-05-22T12:25:08.048205087Z INFO:primp:response: https://www.bing.com/search?q=patch+verification+-+does+assistant+response+persist+now 200
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:341:2026-05-22T12:25:08.101936984Z INFO:__main__:🔍 Search: 'patch verification - does assistant response persist now' → 0 results
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:346:2026-05-22T12:34:07.828926436Z INFO:primp:response: https://www.bing.com/search?q=patch+verification+-+does+assistant+response+persist+now 200
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:347:2026-05-22T12:34:07.974057233Z INFO:__main__:🔍 Search: 'patch verification - does assistant response persist now' → 5 results
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:372:2026-05-22T19:20:09.784029541Z INFO:primp:response: https://www.bing.com/search?q=ping+after+persist+move 200
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:373:2026-05-22T19:20:09.929174574Z INFO:__main__:🔍 Search: 'ping after persist move' → 0 results
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:402:2026-05-22T21:14:23.641553467Z INFO:primp:response: https://www.bing.com/search?q=assistant+persistence+final+proof 200
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:403:2026-05-22T21:14:23.743586499Z INFO:__main__:🔍 Search: 'assistant persistence final proof' → 0 results
/home/cakidd/msallis-diag-20260522-200208/docker-ps.txt:62:jarvis-lm-synthesizer                                   msjarvis-rebuild-jarvis-lm-synthesizer                Up 2 hours                      8001/tcp
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:111166:2026-05-17T01:34:13.254961649Z 	  ('wvgistc_air_nonattainment_wvdep_200802_utm83',      'WVDEP',            '2008-02-01', 'POLYGON', 4326, (SELECT COUNT(*) FROM wvgistc_air_nonattainment_wvdep_200802_utm83),      'WV air pollution non-attainment areas, WVDEP 2008, UTM17N→WGS84', NOW()),
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:112808:2026-05-17T01:45:19.261039704Z 	"user_poll_" varchar(100),
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:112809:2026-05-17T01:45:19.261040654Z 	"user_poll1" varchar(20),
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:114264:2026-05-20T00:44:08.720324522Z 	      UPDATE mountainshares_ledger SET amount = <YOUR_AMOUNT> WHERE ueid = 'fc238378-14f5-4a10-9865-ae241ea2ef74' AND transaction_type = 'founding_grant';
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:114296:2026-05-20T01:57:06.018920829Z 2026-05-20 01:57:06.018 UTC [37691] ERROR:  relation "ledger_entries" does not exist at character 15
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:114297:2026-05-20T01:57:06.018951677Z 2026-05-20 01:57:06.018 UTC [37691] STATEMENT:  SELECT * FROM ledger_entries ORDER BY created_at LIMIT 5;
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:114341:2026-05-22T14:24:50.404642486Z 	      WHERE session_id='persist-verify'
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:114353:2026-05-22T15:19:10.487046126Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:114361:2026-05-22T15:24:51.796790724Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:114368:2026-05-22T15:27:26.338476293Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:7:            "lm_synthesizer.py"
/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:27:        "Name": "/jarvis-lm-synthesizer",
/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:200:                "lm_synthesizer.py"
/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:202:            "Image": "msjarvis-rebuild-jarvis-lm-synthesizer",
/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:215:                "com.docker.compose.replace": "jarvis-lm-synthesizer",
/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:216:                "com.docker.compose.service": "jarvis-lm-synthesizer",
/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:231:                        "jarvis-lm-synthesizer",
/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:232:                        "jarvis-lm-synthesizer"
/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:246:                        "jarvis-lm-synthesizer",
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:32:2026-05-22T20:27:56.253064826Z 2026-05-22 20:27:56,252 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:57:2026-05-22T20:32:26.411693339Z 2026-05-22 20:32:26,411 INFO jarvis-main-brain - assistant-response-persisted
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:97:2026-05-22T21:09:25.409053119Z 2026-05-22 21:09:25,408 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:142:2026-05-22T21:13:39.564261633Z 2026-05-22 21:13:39,563 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:167:2026-05-22T21:14:34.798964227Z 2026-05-22 21:14:34,798 INFO jarvis-main-brain - assistant-response-persisted
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:182:2026-05-22T21:22:24.096716186Z 2026-05-22 21:22:24,096 INFO jarvis-main-brain - assistant-response-persisted
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:219:2026-05-22T23:52:47.381962344Z 2026-05-22 23:52:47,381 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:247:2026-05-22T23:57:53.208903422Z 2026-05-22 23:57:53,208 INFO jarvis-main-brain - assistant-response-persisted
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:285:2026-05-23T00:02:47.665388807Z 2026-05-23 00:02:47,665 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.inspect.json:253:                "ISPERSISTENT=TRUE",
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.inspect.json:271:                "PERSIST_DIRECTORY=/data",
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.inspect.json:357:                "ESCALATION_POLL_INTERVAL=60",
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:32:2026-05-22T20:27:56.253064826Z 2026-05-22 20:27:56,252 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:57:2026-05-22T20:32:26.411693339Z 2026-05-22 20:32:26,411 INFO jarvis-main-brain - assistant-response-persisted
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:97:2026-05-22T21:09:25.409053119Z 2026-05-22 21:09:25,408 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:142:2026-05-22T21:13:39.564261633Z 2026-05-22 21:13:39,563 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:167:2026-05-22T21:14:34.798964227Z 2026-05-22 21:14:34,798 INFO jarvis-main-brain - assistant-response-persisted
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:182:2026-05-22T21:22:24.096716186Z 2026-05-22 21:22:24,096 INFO jarvis-main-brain - assistant-response-persisted
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:219:2026-05-22T23:52:47.381962344Z 2026-05-22 23:52:47,381 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:247:2026-05-22T23:57:53.208903422Z 2026-05-22 23:57:53,208 INFO jarvis-main-brain - assistant-response-persisted
/home/cakidd/msallis-diag-20260522-200208/docker-compose-ps.txt:27:jarvis-lm-synthesizer                                   msjarvis-rebuild-jarvis-lm-synthesizer                "python lm_synthesiz…"   jarvis-lm-synthesizer                3 days ago          Up 2 hours                      8001/tcp
/home/cakidd/msallis-diag-20260522-200208/jarvis-20llm-production.end.log:3:2026-05-19T18:04:02.798508625Z INFO:__main__:   • Gemma -> model=gemma:2b endpoint=http://llm2-proxy:8202/generate weight=0.8 specialty=Synthesis active=True
/home/cakidd/msallis-diag-20260522-200208/jarvis-20llm-production.end.log:2512:2026-05-22T22:25:10.718572044Z INFO:__main__:   • Gemma -> model=gemma:2b endpoint=http://llm2-proxy:8202/generate weight=0.8 specialty=Synthesis active=True
/home/cakidd/msallis-diag-20260522-200208/12d6dc1b1e49_jarvis-chroma.inspect.json:246:                "ISPERSISTENT=TRUE",
/home/cakidd/msallis-diag-20260522-200208/12d6dc1b1e49_jarvis-chroma.inspect.json:249:                "PERSIST_DIRECTORY=/data",
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:111166:2026-05-17T01:34:13.254961649Z 	  ('wvgistc_air_nonattainment_wvdep_200802_utm83',      'WVDEP',            '2008-02-01', 'POLYGON', 4326, (SELECT COUNT(*) FROM wvgistc_air_nonattainment_wvdep_200802_utm83),      'WV air pollution non-attainment areas, WVDEP 2008, UTM17N→WGS84', NOW()),
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:112808:2026-05-17T01:45:19.261039704Z 	"user_poll_" varchar(100),
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:112809:2026-05-17T01:45:19.261040654Z 	"user_poll1" varchar(20),
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:114264:2026-05-20T00:44:08.720324522Z 	      UPDATE mountainshares_ledger SET amount = <YOUR_AMOUNT> WHERE ueid = 'fc238378-14f5-4a10-9865-ae241ea2ef74' AND transaction_type = 'founding_grant';
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:114296:2026-05-20T01:57:06.018920829Z 2026-05-20 01:57:06.018 UTC [37691] ERROR:  relation "ledger_entries" does not exist at character 15
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:114297:2026-05-20T01:57:06.018951677Z 2026-05-20 01:57:06.018 UTC [37691] STATEMENT:  SELECT * FROM ledger_entries ORDER BY created_at LIMIT 5;
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:114341:2026-05-22T14:24:50.404642486Z 	      WHERE session_id='persist-verify'
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:114353:2026-05-22T15:19:10.487046126Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:114361:2026-05-22T15:24:51.796790724Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:114368:2026-05-22T15:27:26.338476293Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
/home/cakidd/msallis-diag-20260522-200208/jarvis-unified-gateway.inspect.json:306:                "com.docker.compose.depends_on": "psychological_rag_domain:service_started:false,nbb_spiritual_maternal_integration:service_started:false,nbb_woah_algorithms:service_started:false,nbb-i-containers:service_started:false,nbb_subconscious:service_started:false,jarvis-toroidal:service_started:false,jarvis-fifth-dgm:service_started:false,jarvis-lm-synthesizer:service_started:false,nbb_spiritual_root:service_started:false,jarvis-ollama:service_started:false,jarvis-constitutional-guardian:service_started:false,jarvis-woah:service_started:false,jarvis-brain-orchestrator:service_started:false,jarvis-chroma:service_started:false,jarvis-qualia-engine:service_started:false,jarvis-neurobiological-master:service_started:false,nbb_prefrontal_cortex:service_started:false,jarvis-psychology-services:service_started:false,jarvis-fractal-consciousness:service_started:false,nbb_consciousness_containers:service_started:false,jarvis-consciousness-bridge:service_started:false,jarvis-20llm-production:service_started:false,nbb_mother_carrie_protocols:service_started:false,jarvis-blood-brain-barrier:service_started:false,nbb_heteroglobulin_transport:service_started:false,jarvis-redis:service_started:false,jarvis-i-containers:service_started:false,nbb_pituitary_gland:service_started:false",
/home/cakidd/msallis-diag-20260522-200208/jarvis-20llm-production.log:3:2026-05-19T18:04:02.798508625Z INFO:__main__:   • Gemma -> model=gemma:2b endpoint=http://llm2-proxy:8202/generate weight=0.8 specialty=Synthesis active=True
/home/cakidd/msallis-diag-20260522-200208/jarvis-20llm-production.log:2512:2026-05-22T22:25:10.718572044Z INFO:__main__:   • Gemma -> model=gemma:2b endpoint=http://llm2-proxy:8202/generate weight=0.8 specialty=Synthesis active=True
/home/cakidd/msallis-diag-20260522-200208/12d6dc1b1e49_jarvis-chroma.end.log:3:2026-05-19T03:59:34.041061144Z persist_path: "/data"
/home/cakidd/msallis-diag-20260522-200208/12d6dc1b1e49_jarvis-chroma.end.log:31:2026-05-22T22:25:11.072470362Z persist_path: "/data"
grep: /home/cakidd/msallis-diag-20260522-200208/slow-path-grep.txt: input file is also the output
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:168:2026-05-22T23:52:52.686012145Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 3200
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:249:2026-05-22T23:52:53.236862897Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 3200
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:361:2026-05-22T23:53:13.149684929Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:445:2026-05-22T23:53:17.557183580Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:562:2026-05-22T23:53:37.241514389Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:666:2026-05-22T23:53:47.330645735Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1195:2026-05-22T23:54:15.806807252Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1276:2026-05-22T23:54:18.978274494Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1388:2026-05-22T23:54:29.660032960Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1492:2026-05-22T23:54:41.631149448Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1609:2026-05-22T23:54:51.781936135Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1694:2026-05-22T23:54:53.397496085Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1811:2026-05-22T23:54:56.256453904Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1912:2026-05-22T23:55:10.347849077Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2025:2026-05-22T23:55:14.009307673Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2132:2026-05-22T23:55:21.236845252Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2251:2026-05-22T23:55:31.996226417Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2354:2026-05-22T23:55:48.851239652Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2468:2026-05-22T23:55:51.719707737Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2584:2026-05-22T23:56:04.845748307Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2715:2026-05-22T23:56:06.198228820Z llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2802:2026-05-22T23:56:08.299697925Z llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2929:2026-05-22T23:56:11.142780529Z llama_model_loader: - kv  12:                      phi3.embedding_length u32              = 3072
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3049:2026-05-22T23:56:27.687706746Z llama_model_loader: - kv  12:                      phi3.embedding_length u32              = 3072
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3174:2026-05-22T23:56:42.864626949Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3260:2026-05-22T23:56:49.300142341Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3377:2026-05-22T23:56:52.158691523Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3477:2026-05-22T23:57:04.289921868Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3589:2026-05-22T23:57:11.748896533Z llama_model_loader: - kv   4:                starcoder2.embedding_length u32              = 3072
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3694:2026-05-22T23:57:24.742290551Z llama_model_loader: - kv   4:                starcoder2.embedding_length u32              = 3072
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3811:2026-05-22T23:57:26.095016910Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3913:2026-05-22T23:57:32.620899339Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:4029:2026-05-22T23:57:40.859081243Z llama_model_loader: - kv   3:                      phi2.embedding_length u32              = 2560
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:4142:2026-05-23T00:02:50.741324046Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:4220:2026-05-23T00:02:50.903360061Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:4750:2026-05-23T00:02:54.256367952Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:4837:2026-05-23T00:03:00.142655315Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:4958:2026-05-23T00:03:11.203997380Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5058:2026-05-23T00:03:31.984325844Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5170:2026-05-23T00:03:39.650279766Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5269:2026-05-23T00:04:05.242015099Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5381:2026-05-23T00:04:11.641280899Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5497:2026-05-23T00:04:28.142344533Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5636:2026-05-23T00:04:29.495405178Z llama_model_loader: - kv  12:                      phi3.embedding_length u32              = 3072
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5736:2026-05-23T00:04:31.527847575Z llama_model_loader: - kv  12:                      phi3.embedding_length u32              = 3072
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5861:2026-05-23T00:04:35.648445887Z llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5950:2026-05-23T00:04:47.301717370Z llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:6068:2026-05-23T00:04:50.154647811Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:6169:2026-05-23T00:05:06.840391051Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:6282:2026-05-23T00:05:10.615082950Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:6387:2026-05-23T00:05:18.103365438Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:6504:2026-05-23T00:05:21.506464796Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:39:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:138:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:169:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:207:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:251:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:290:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:291:      PERSIST_DIRECTORY: /data
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:322:        source: /home/ms-jarvis/msjarvis-rebuild/persistent/chroma
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:339:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:388:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:420:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:511:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:703:  jarvis-lm-synthesizer:
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:706:      dockerfile: Dockerfile.lm_synthesizer
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:709:      - lm_synthesizer.py
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:710:    container_name: jarvis-lm-synthesizer
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:716:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:814:      jarvis-lm-synthesizer:
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:880:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1010:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1038:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1079:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1232:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1287:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1321:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1350:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1768:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1987:      IS_PERSISTENT: "TRUE"
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:321:2026-05-22T01:40:31.067292655Z INFO:primp:response: https://www.bing.com/search?q=capture+every+status+response+to+debug+polling 200
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:322:2026-05-22T01:40:31.182196406Z INFO:__main__:🔍 Search: 'capture every status response to debug polling' → 5 results
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:327:2026-05-22T03:16:43.216931338Z INFO:primp:response: https://www.bing.com/search?q=capture+every+status+response+to+debug+polling 200
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:328:2026-05-22T03:16:43.608909548Z INFO:__main__:🔍 Search: 'capture every status response to debug polling' → 0 results
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:334:2026-05-22T03:36:18.995834946Z INFO:primp:response: https://www.bing.com/search?q=fast+poll+test 200
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:335:2026-05-22T03:36:19.049901472Z INFO:__main__:🔍 Search: 'fast poll test' → 5 results
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:340:2026-05-22T12:25:08.048205087Z INFO:primp:response: https://www.bing.com/search?q=patch+verification+-+does+assistant+response+persist+now 200
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:341:2026-05-22T12:25:08.101936984Z INFO:__main__:🔍 Search: 'patch verification - does assistant response persist now' → 0 results
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:346:2026-05-22T12:34:07.828926436Z INFO:primp:response: https://www.bing.com/search?q=patch+verification+-+does+assistant+response+persist+now 200
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:347:2026-05-22T12:34:07.974057233Z INFO:__main__:🔍 Search: 'patch verification - does assistant response persist now' → 5 results
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:372:2026-05-22T19:20:09.784029541Z INFO:primp:response: https://www.bing.com/search?q=ping+after+persist+move 200
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:373:2026-05-22T19:20:09.929174574Z INFO:__main__:🔍 Search: 'ping after persist move' → 0 results
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:402:2026-05-22T21:14:23.641553467Z INFO:primp:response: https://www.bing.com/search?q=assistant+persistence+final+proof 200
/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:403:2026-05-22T21:14:23.743586499Z INFO:__main__:🔍 Search: 'assistant persistence final proof' → 0 results
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:168:2026-05-22T23:52:52.686012145Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 3200
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:249:2026-05-22T23:52:53.236862897Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 3200
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:361:2026-05-22T23:53:13.149684929Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:445:2026-05-22T23:53:17.557183580Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:562:2026-05-22T23:53:37.241514389Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:666:2026-05-22T23:53:47.330645735Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1195:2026-05-22T23:54:15.806807252Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1276:2026-05-22T23:54:18.978274494Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1388:2026-05-22T23:54:29.660032960Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1492:2026-05-22T23:54:41.631149448Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1609:2026-05-22T23:54:51.781936135Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1694:2026-05-22T23:54:53.397496085Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1811:2026-05-22T23:54:56.256453904Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1912:2026-05-22T23:55:10.347849077Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2025:2026-05-22T23:55:14.009307673Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2132:2026-05-22T23:55:21.236845252Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2251:2026-05-22T23:55:31.996226417Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2354:2026-05-22T23:55:48.851239652Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2468:2026-05-22T23:55:51.719707737Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2584:2026-05-22T23:56:04.845748307Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2715:2026-05-22T23:56:06.198228820Z llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2802:2026-05-22T23:56:08.299697925Z llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2929:2026-05-22T23:56:11.142780529Z llama_model_loader: - kv  12:                      phi3.embedding_length u32              = 3072
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3049:2026-05-22T23:56:27.687706746Z llama_model_loader: - kv  12:                      phi3.embedding_length u32              = 3072
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3174:2026-05-22T23:56:42.864626949Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3260:2026-05-22T23:56:49.300142341Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3377:2026-05-22T23:56:52.158691523Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3477:2026-05-22T23:57:04.289921868Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3589:2026-05-22T23:57:11.748896533Z llama_model_loader: - kv   4:                starcoder2.embedding_length u32              = 3072
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3694:2026-05-22T23:57:24.742290551Z llama_model_loader: - kv   4:                starcoder2.embedding_length u32              = 3072
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3811:2026-05-22T23:57:26.095016910Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3913:2026-05-22T23:57:32.620899339Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:4029:2026-05-22T23:57:40.859081243Z llama_model_loader: - kv   3:                      phi2.embedding_length u32              = 2560
/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.log:1:2026-05-19T03:57:54.791666574Z INFO:lm_synthesizer:Starting LM Synthesizer on 0.0.0.0:8001
/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.log:76:2026-05-22T22:25:11.815499916Z INFO:lm_synthesizer:Starting LM Synthesizer on 0.0.0.0:8001
/home/cakidd/msallis-diag-20260522-200208/jarvis-judge-pipeline.inspect.json:214:                "LM_SYNTHESIZER_URL=http://jarvis-lm-synthesizer:8001",
/home/cakidd/msallis-diag-20260522-200208/jarvis-judge-pipeline.inspect.json:237:                "com.docker.compose.depends_on": "jarvis-judge-ethics:service_started:false,jarvis-lm-synthesizer:service_started:false,jarvis-judge-truth:service_started:false,jarvis-judge-consistency:service_started:false,jarvis-judge-alignment:service_started:false",
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:63:jarvis-lm-synthesizer                                   0.12%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:153:jarvis-lm-synthesizer                                   0.13%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:243:jarvis-lm-synthesizer                                   0.16%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:333:jarvis-lm-synthesizer                                   0.15%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:423:jarvis-lm-synthesizer                                   0.11%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:513:jarvis-lm-synthesizer                                   0.15%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:603:jarvis-lm-synthesizer                                   0.14%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:693:jarvis-lm-synthesizer                                   0.16%     17.8MiB / 29.08GiB    0.06%     263kB / 910B      26.1MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:783:jarvis-lm-synthesizer                                   0.14%     17.8MiB / 29.08GiB    0.06%     263kB / 910B      26.1MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:873:jarvis-lm-synthesizer                                   0.16%     17.8MiB / 29.08GiB    0.06%     263kB / 910B      26.1MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:963:jarvis-lm-synthesizer                                   0.14%     17.8MiB / 29.08GiB    0.06%     263kB / 910B      26.1MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:1053:jarvis-lm-synthesizer                                   1.63%     29.57MiB / 29.08GiB   0.10%     266kB / 1.61kB    37.7MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:1143:jarvis-lm-synthesizer                                   0.11%     29.34MiB / 29.08GiB   0.10%     268kB / 1.61kB    37.7MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:1233:jarvis-lm-synthesizer                                   0.10%     29.34MiB / 29.08GiB   0.10%     268kB / 1.69kB    37.7MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:1323:jarvis-lm-synthesizer                                   0.11%     29.34MiB / 29.08GiB   0.10%     268kB / 1.69kB    37.7MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:1412:jarvis-lm-synthesizer                                   0.09%     29.34MiB / 29.08GiB   0.10%     268kB / 1.69kB    37.7MB / 26.1MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:1502:jarvis-lm-synthesizer                                   0.09%     28.98MiB / 29.08GiB   0.10%     268kB / 1.69kB    37.7MB / 26.5MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:1592:jarvis-lm-synthesizer                                   0.09%     20.85MiB / 29.08GiB   0.07%     268kB / 1.69kB    37.7MB / 30MB     5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:1682:jarvis-lm-synthesizer                                   0.11%     20.85MiB / 29.08GiB   0.07%     268kB / 1.69kB    37.7MB / 30MB     5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:1772:jarvis-lm-synthesizer                                   0.13%     20.86MiB / 29.08GiB   0.07%     268kB / 1.69kB    37.7MB / 30MB     5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:1862:jarvis-lm-synthesizer                                   0.12%     20.86MiB / 29.08GiB   0.07%     268kB / 1.69kB    37.7MB / 30MB     5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:1952:jarvis-lm-synthesizer                                   0.12%     20.86MiB / 29.08GiB   0.07%     268kB / 1.69kB    37.8MB / 30MB     5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:2042:jarvis-lm-synthesizer                                   0.13%     20.86MiB / 29.08GiB   0.07%     268kB / 1.69kB    37.8MB / 30MB     5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:2132:jarvis-lm-synthesizer                                   0.14%     20.86MiB / 29.08GiB   0.07%     268kB / 1.69kB    37.8MB / 30MB     5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:2222:jarvis-lm-synthesizer                                   0.17%     20.86MiB / 29.08GiB   0.07%     268kB / 1.69kB    37.8MB / 30MB     5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:2312:jarvis-lm-synthesizer                                   0.17%     20.86MiB / 29.08GiB   0.07%     269kB / 1.69kB    37.8MB / 30MB     5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:2402:jarvis-lm-synthesizer                                   0.14%     20.61MiB / 29.08GiB   0.07%     269kB / 1.69kB    37.8MB / 30.7MB   5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:2492:jarvis-lm-synthesizer                                   0.14%     19.23MiB / 29.08GiB   0.06%     269kB / 1.69kB    37.8MB / 32MB     5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:2582:jarvis-lm-synthesizer                                   0.12%     18.99MiB / 29.08GiB   0.06%     269kB / 1.69kB    37.8MB / 32MB     5
/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:2672:jarvis-lm-synthesizer                                   0.13%     18.99MiB / 29.08GiB   0.06%     269kB / 1.69kB    37.8MB / 32MB     5

===== DOCKER LIMIT COMMANDS =====
# Review and adapt these exact commands before applying in production
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-unified-gateway
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-brain-orchestrator
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-ollama
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-69dgm-bridge
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-main-brain
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-20llm-production
docker update --cpus 2 --memory 6g --memory-swap 6g llm21-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g llm22-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-wv-entangled-gateway
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-psychology-services
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-toroidal
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-autonomous-learner
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-rag-server
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-aaacpe-rag
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-gis-rag
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-spiritual-rag
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-hippocampus
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-neurobiological-master
docker update --cpus 2 --memory 6g --memory-swap 6g 591cd058cd26_jarvis-consciousness-bridge
docker update --cpus 2 --memory 6g --memory-swap 6g dd0340814f6d_jarvis-eeg-beta
docker update --cpus 2 --memory 6g --memory-swap 6g a1f602068b45_jarvis-eeg-delta
docker update --cpus 2 --memory 6g --memory-swap 6g llm7-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g llm11-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g llm17-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g llm3-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g 12d6dc1b1e49_jarvis-chroma
docker update --cpus 2 --memory 6g --memory-swap 6g llm19-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-local-resources
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-woah
docker update --cpus 2 --memory 6g --memory-swap 6g 11aba8ab78dd_jarvis-temporal-consciousness
docker update --cpus 2 --memory 6g --memory-swap 6g llm15-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-blood-brain-barrier
docker update --cpus 2 --memory 6g --memory-swap 6g msjarvis-rebuild-nbb_prefrontal_cortex-1
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-web-research
docker update --cpus 2 --memory 6g --memory-swap 6g msjarvis-rebuild-nbb_qualia_engine-1
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-redis
docker update --cpus 2 --memory 6g --memory-swap 6g llm8-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g llm2-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g llm5-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g msjarvis-rebuild-nbb_darwin_godel_machines-1
docker update --cpus 2 --memory 6g --memory-swap 6g msjarvis-rebuild-nbb_mother_carrie_protocols-1
docker update --cpus 2 --memory 6g --memory-swap 6g llm20-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g llm10-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g llm1-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g llm9-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g llm4-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-fractal-consciousness
docker update --cpus 2 --memory 6g --memory-swap 6g llm13-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-semaphore
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-agents-service
docker update --cpus 2 --memory 6g --memory-swap 6g llm14-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g llm6-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g llm12-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g llm18-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g llm16-proxy
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-judge-pipeline
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-judge-truth
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-judge-ethics
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-judge-consistency
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-judge-alignment
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-lm-synthesizer
docker update --cpus 2 --memory 6g --memory-swap 6g msjarvis-rebuild-nbb_pituitary_gland-1
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-eeg-theta
docker update --cpus 2 --memory 6g --memory-swap 6g nbb-i-containers
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-i-containers
docker update --cpus 2 --memory 6g --memory-swap 6g msjarvis-rebuild-nbb_spiritual_maternal_integration-1
docker update --cpus 2 --memory 6g --memory-swap 6g msjarvis-rebuild-nbb_heteroglobulin_transport-1
docker update --cpus 2 --memory 6g --memory-swap 6g msjarvis-rebuild-nbb_spiritual_root-1
docker update --cpus 2 --memory 6g --memory-swap 6g msjarvis-rebuild-nbb_blood_brain_barrier-1
docker update --cpus 2 --memory 6g --memory-swap 6g msjarvis-rebuild-nbb_consciousness_containers-1
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-hilbert-state
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-mother-protocols
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-swarm-intelligence
docker update --cpus 2 --memory 6g --memory-swap 6g mysql
docker update --cpus 2 --memory 6g --memory-swap 6g neo4j
docker update --cpus 2 --memory 6g --memory-swap 6g ipfs
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-session-sidecar
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-constitutional-guardian
docker update --cpus 2 --memory 6g --memory-swap 6g msjarvis-rebuild-nbb_woah_algorithms-1
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-qualia-engine
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-fifth-dgm
docker update --cpus 2 --memory 6g --memory-swap 6g msjarvis-rebuild-nbb_subconscious-1
docker update --cpus 2 --memory 6g --memory-swap 6g psychological_rag_domain
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-local-resources-db
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-gbim-temporal-indexer
docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-jaeger

===== TOP CPU SNAPSHOT =====
2026-05-22 20:02:09
    PID    PPID  NI PRI STAT %CPU %MEM   RSS     ELAPSED COMMAND         COMMAND
  15530    2891   0  19 Sl   41.3  1.4 432420   01:35:39 firefox         /snap/firefox/8306/usr/lib/firefox/firefox
  18778   15703   0  19 Sl    9.6  1.8 558784   01:33:02 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {ac5b4387-9da2-464f-b4d8-0e5ad08ea5b6} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 18 tab
 100436    3454   -   0 SNl   6.0  0.0 29820       00:00 tracker-extract /usr/libexec/tracker-extract-3 --socket-fd 3
   2891    2293   0  19 Ssl   5.5  0.4 127832   01:37:21 gnome-shell     /usr/bin/gnome-shell
   2483    2481   0  19 Sl+   5.0  0.1 39880    01:37:23 Xorg            /usr/lib/xorg/Xorg vt2 -displayfd 3 -auth /run/user/1000/gdm/Xauthority -nolisten tcp -background none -noreset -keeptty -novtswitch -verbose 3
  79812   15703   0  19 Sl    3.3  0.3 121232      12:25 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {27129b7f-ef84-4612-b180-3085916acbc2} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 90 tab
    980       2   -  90 S     2.4  0.0     0    01:37:26 irq/185-rtw89_p [irq/185-rtw89_pci]
   3783       1   0  19 Ssl   2.3  0.3 94808    01:37:12 dockerd         /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
  10937    8550   0  19 Sl    2.0  0.3 98740    01:36:58 ipfs            ipfs daemon --migrate=true --agent-version-suffix=docker
  15765   15703   0  19 Sl    1.6  0.3 120344   01:35:37 Privileged Cont /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:39334 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {b4f6c08e-b945-4945-a783-8654459f972e} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 3 tab
  98504    2891   0  19 Sl    1.3  0.6 186580      02:09 gnome-text-edit /usr/bin/gnome-text-editor
  14055   13977   0  19 Sl    0.8  0.1 37232    01:36:52 java            /opt/java/openjdk/bin/java -cp /var/lib/neo4j/plugins/*:/var/lib/neo4j/conf/*:/var/lib/neo4j/lib/* -XX:+UseG1GC -XX:-OmitStackTraceInFastThrow -XX:+AlwaysPreTouch -XX:+UnlockExperimentalVMOptions -XX:+TrustFinalNonStaticFields -XX:+DisableExplicitGC -Djdk.nio.maxCachedBufferSize=1024 -Dio.netty.tryReflectionSetAccessible=true -Djdk.tls.ephemeralDHKeySize=2048 -Djdk.tls.rejectClientInitiatedRenegotiation=true -XX:FlightRecorderOptions=stackdepth=256 -XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED -Dlog4j2.disable.jmx=true -Dfile.encoding=UTF-8 org.neo4j.server.CommunityEntryPoint --home-dir=/var/lib/neo4j --config-dir=/var/lib/neo4j/conf --console-mode
   7451    7350   0  19 Ssl   0.7  0.0  9256    01:36:59 redis-server    redis-server *:6379
  73538    2293   0  19 Ssl   0.7  0.1 49604       21:17 gnome-terminal- /usr/libexec/gnome-terminal-server
  10129    9422   0  19 Ssl   0.6  0.0 14712    01:36:58 mysqld          mysqld
   2256       1   0  19 Ssl   0.6  0.0 22496    01:37:24 mysqld          /usr/sbin/mysqld
  95425       2 -20  39 I<    0.4  0.0     0       04:32 kworker/u129:2- [kworker/u129:2-rtw89_tx_wq]
  81995       2 -20  39 I<    0.4  0.0     0       10:00 kworker/u129:0- [kworker/u129:0-rtw89_tx_wq]
  73712       2 -20  39 I<    0.4  0.0     0       20:58 kworker/u129:1- [kworker/u129:1-rtw89_tx_wq]
      1       0   0  19 Ss    0.4  0.0 15608    01:37:31 systemd         /sbin/init splash
  32706   32683   0  19 Ssl   0.3  0.0 29440    01:15:01 python3.10      python3.10 ms_jarvis_unified_gateway.py
   3094    2293   0  19 Ssl   0.3  0.0 11452    01:37:20 gvfs-udisks2-vo /usr/libexec/gvfs-udisks2-volume-monitor
   3781       1   0  19 Ssl   0.3  0.0 23432    01:37:12 cloudflared     /usr/bin/cloudflared --no-autoupdate --config /etc/cloudflared/config.yml tunnel run
    443       2   -  90 S     0.3  0.0     0    01:37:30 irq/136-FTCS003 [irq/136-FTCS0038:00]

----
2026-05-22 20:02:10
    PID    PPID  NI PRI STAT %CPU %MEM   RSS     ELAPSED COMMAND         COMMAND
 101032  100617   0  19 R+    100  0.0  4760       00:00 ps              ps -eo pid,ppid,ni,pri,stat,%cpu,%mem,rss,etime,comm,args --sort=-%cpu
  15530    2891   0  19 Sl   41.3  1.4 432420   01:35:40 firefox         /snap/firefox/8306/usr/lib/firefox/firefox
  18778   15703   0  19 Sl    9.6  1.8 558756   01:33:03 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {ac5b4387-9da2-464f-b4d8-0e5ad08ea5b6} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 18 tab
   2891    2293   0  19 Ssl   5.5  0.4 127840   01:37:22 gnome-shell     /usr/bin/gnome-shell
   2483    2481   0  19 Sl+   5.0  0.1 39880    01:37:24 Xorg            /usr/lib/xorg/Xorg vt2 -displayfd 3 -auth /run/user/1000/gdm/Xauthority -nolisten tcp -background none -noreset -keeptty -novtswitch -verbose 3
 100635  100618   0  19 Sl+   4.7  0.1 35696       00:01 docker          docker stats --no-stream --format table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.NetIO}}\t{{.BlockIO}}\t{{.PIDs}}
  79812   15703   0  19 Sl    3.3  0.3 121232      12:26 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {27129b7f-ef84-4612-b180-3085916acbc2} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 90 tab
    980       2   -  90 S     2.4  0.0     0    01:37:27 irq/185-rtw89_p [irq/185-rtw89_pci]
   3783       1   0  19 Ssl   2.3  0.3 98688    01:37:13 dockerd         /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
 100436    3454   -   0 SNl   2.3  0.0 29820       00:01 tracker-extract /usr/libexec/tracker-extract-3 --socket-fd 3
  10937    8550   0  19 Sl    2.0  0.3 98740    01:36:59 ipfs            ipfs daemon --migrate=true --agent-version-suffix=docker
  15765   15703   0  19 Sl    1.6  0.3 120344   01:35:38 Privileged Cont /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:39334 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {b4f6c08e-b945-4945-a783-8654459f972e} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 3 tab
  98504    2891   0  19 Sl    1.3  0.6 186580      02:10 gnome-text-edit /usr/bin/gnome-text-editor
  14055   13977   0  19 Sl    0.8  0.1 37256    01:36:53 java            /opt/java/openjdk/bin/java -cp /var/lib/neo4j/plugins/*:/var/lib/neo4j/conf/*:/var/lib/neo4j/lib/* -XX:+UseG1GC -XX:-OmitStackTraceInFastThrow -XX:+AlwaysPreTouch -XX:+UnlockExperimentalVMOptions -XX:+TrustFinalNonStaticFields -XX:+DisableExplicitGC -Djdk.nio.maxCachedBufferSize=1024 -Dio.netty.tryReflectionSetAccessible=true -Djdk.tls.ephemeralDHKeySize=2048 -Djdk.tls.rejectClientInitiatedRenegotiation=true -XX:FlightRecorderOptions=stackdepth=256 -XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED -Dlog4j2.disable.jmx=true -Dfile.encoding=UTF-8 org.neo4j.server.CommunityEntryPoint --home-dir=/var/lib/neo4j --config-dir=/var/lib/neo4j/conf --console-mode
   7451    7350   0  19 Ssl   0.7  0.0  9256    01:37:00 redis-server    redis-server *:6379
  73538    2293   0  19 Ssl   0.7  0.1 49604       21:18 gnome-terminal- /usr/libexec/gnome-terminal-server
  10129    9422   0  19 Ssl   0.6  0.0 14712    01:36:59 mysqld          mysqld
   2256       1   0  19 Ssl   0.6  0.0 22496    01:37:25 mysqld          /usr/sbin/mysqld
 100422   73551   0  19 S+    0.5  0.0  4228       00:01 bash            bash ./msallis_next_steps.sh
  95425       2 -20  39 I<    0.4  0.0     0       04:33 kworker/u129:2- [kworker/u129:2-rtw89_tx_wq]
  81995       2 -20  39 I<    0.4  0.0     0       10:01 kworker/u129:0- [kworker/u129:0-rtw89_tx_wq]
  73712       2 -20  39 I<    0.4  0.0     0       20:59 kworker/u129:1- [kworker/u129:1-rtw89_tx_wq]
      1       0   0  19 Ss    0.4  0.0 15608    01:37:32 systemd         /sbin/init splash
  32706   32683   0  19 Ssl   0.3  0.0 29440    01:15:02 python3.10      python3.10 ms_jarvis_unified_gateway.py

----
2026-05-22 20:02:11
    PID    PPID  NI PRI STAT %CPU %MEM   RSS     ELAPSED COMMAND         COMMAND
 101433  101428   0  19 Rl    133  0.1 55240       00:00 node            node /opt/msjarvis-rebuild/ms-allis-frontend/node_modules/.bin/next start -p 3001
 101418  101417   0  19 Sl    114  0.0 28664       00:00 docker          docker logs --timestamps jarvis-eeg-theta
 101350       1   0  19 Ssl  56.2  0.1 57344       00:00 npm start       npm start
  15530    2891   0  19 Sl   41.3  1.4 432424   01:35:41 firefox         /snap/firefox/8306/usr/lib/firefox/firefox
  18778   15703   0  19 Sl    9.6  1.8 554572   01:33:04 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {ac5b4387-9da2-464f-b4d8-0e5ad08ea5b6} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 18 tab
   2891    2293   0  19 Ssl   5.5  0.4 127840   01:37:23 gnome-shell     /usr/bin/gnome-shell
   2483    2481   0  19 Sl+   5.0  0.1 39880    01:37:25 Xorg            /usr/lib/xorg/Xorg vt2 -displayfd 3 -auth /run/user/1000/gdm/Xauthority -nolisten tcp -background none -noreset -keeptty -novtswitch -verbose 3
  79812   15703   0  19 Sl    3.3  0.3 121232      12:27 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {27129b7f-ef84-4612-b180-3085916acbc2} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 90 tab
    980       2   -  90 S     2.4  0.0     0    01:37:28 irq/185-rtw89_p [irq/185-rtw89_pci]
 100635  100618   0  19 Sl+   2.4  0.1 35700       00:02 docker          docker stats --no-stream --format table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.NetIO}}\t{{.BlockIO}}\t{{.PIDs}}
   3783       1   0  19 Ssl   2.4  0.3 104120   01:37:14 dockerd         /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
  10937    8550   0  19 Sl    2.0  0.3 98740    01:37:00 ipfs            ipfs daemon --migrate=true --agent-version-suffix=docker
  15765   15703   0  19 Sl    1.6  0.3 120344   01:35:39 Privileged Cont /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:39334 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {b4f6c08e-b945-4945-a783-8654459f972e} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 3 tab
 100436    3454   -   0 SNl   1.4  0.0 29820       00:02 tracker-extract /usr/libexec/tracker-extract-3 --socket-fd 3
  98504    2891   0  19 Sl    1.3  0.6 186580      02:11 gnome-text-edit /usr/bin/gnome-text-editor
  14055   13977   0  19 Sl    0.8  0.1 37296    01:36:54 java            /opt/java/openjdk/bin/java -cp /var/lib/neo4j/plugins/*:/var/lib/neo4j/conf/*:/var/lib/neo4j/lib/* -XX:+UseG1GC -XX:-OmitStackTraceInFastThrow -XX:+AlwaysPreTouch -XX:+UnlockExperimentalVMOptions -XX:+TrustFinalNonStaticFields -XX:+DisableExplicitGC -Djdk.nio.maxCachedBufferSize=1024 -Dio.netty.tryReflectionSetAccessible=true -Djdk.tls.ephemeralDHKeySize=2048 -Djdk.tls.rejectClientInitiatedRenegotiation=true -XX:FlightRecorderOptions=stackdepth=256 -XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED -Dlog4j2.disable.jmx=true -Dfile.encoding=UTF-8 org.neo4j.server.CommunityEntryPoint --home-dir=/var/lib/neo4j --config-dir=/var/lib/neo4j/conf --console-mode
   7451    7350   0  19 Ssl   0.7  0.0  9256    01:37:01 redis-server    redis-server *:6379
 100422   73551   0  19 S+    0.7  0.0  4228       00:02 bash            bash ./msallis_next_steps.sh
  73538    2293   0  19 Ssl   0.7  0.1 49604       21:19 gnome-terminal- /usr/libexec/gnome-terminal-server
  10129    9422   0  19 Ssl   0.6  0.0 14712    01:37:00 mysqld          mysqld
   2256       1   0  19 Ssl   0.6  0.0 22496    01:37:26 mysqld          /usr/sbin/mysqld
  95425       2 -20  39 I<    0.4  0.0     0       04:34 kworker/u129:2- [kworker/u129:2-rtw89_tx_wq]
  81995       2 -20  39 I<    0.4  0.0     0       10:02 kworker/u129:0- [kworker/u129:0-rtw89_tx_wq]
  73712       2 -20  39 I<    0.4  0.0     0       21:00 kworker/u129:1- [kworker/u129:1-rtw89_tx_wq]

----
2026-05-22 20:02:12
    PID    PPID  NI PRI STAT %CPU %MEM   RSS     ELAPSED COMMAND         COMMAND
  15530    2891   0  19 Sl   41.3  1.4 432420   01:35:42 firefox         /snap/firefox/8306/usr/lib/firefox/firefox
  18778   15703   0  19 Sl    9.6  1.8 554572   01:33:05 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {ac5b4387-9da2-464f-b4d8-0e5ad08ea5b6} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 18 tab
   2891    2293   0  19 Rsl   5.5  0.4 127812   01:37:24 gnome-shell     /usr/bin/gnome-shell
   2483    2481   0  19 Sl+   5.0  0.1 39880    01:37:26 Xorg            /usr/lib/xorg/Xorg vt2 -displayfd 3 -auth /run/user/1000/gdm/Xauthority -nolisten tcp -background none -noreset -keeptty -novtswitch -verbose 3
  79812   15703   0  19 Sl    3.3  0.3 121232      12:28 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {27129b7f-ef84-4612-b180-3085916acbc2} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 90 tab
    980       2   -  90 S     2.4  0.0     0    01:37:29 irq/185-rtw89_p [irq/185-rtw89_pci]
   3783       1   0  19 Ssl   2.4  0.3 104532   01:37:15 dockerd         /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
  10937    8550   0  19 Sl    2.0  0.3 98740    01:37:01 ipfs            ipfs daemon --migrate=true --agent-version-suffix=docker
  15765   15703   0  19 Sl    1.6  0.3 120344   01:35:40 Privileged Cont /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:39334 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {b4f6c08e-b945-4945-a783-8654459f972e} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 3 tab
  98504    2891   0  19 Sl    1.3  0.6 186580      02:12 gnome-text-edit /usr/bin/gnome-text-editor
 100436    3454   -   0 SNl   1.0  0.0 29820       00:03 tracker-extract /usr/libexec/tracker-extract-3 --socket-fd 3
  14055   13977   0  19 Sl    0.8  0.1 37328    01:36:55 java            /opt/java/openjdk/bin/java -cp /var/lib/neo4j/plugins/*:/var/lib/neo4j/conf/*:/var/lib/neo4j/lib/* -XX:+UseG1GC -XX:-OmitStackTraceInFastThrow -XX:+AlwaysPreTouch -XX:+UnlockExperimentalVMOptions -XX:+TrustFinalNonStaticFields -XX:+DisableExplicitGC -Djdk.nio.maxCachedBufferSize=1024 -Dio.netty.tryReflectionSetAccessible=true -Djdk.tls.ephemeralDHKeySize=2048 -Djdk.tls.rejectClientInitiatedRenegotiation=true -XX:FlightRecorderOptions=stackdepth=256 -XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED -Dlog4j2.disable.jmx=true -Dfile.encoding=UTF-8 org.neo4j.server.CommunityEntryPoint --home-dir=/var/lib/neo4j --config-dir=/var/lib/neo4j/conf --console-mode
   7451    7350   0  19 Ssl   0.7  0.0  9256    01:37:02 redis-server    redis-server *:6379
 100422   73551   0  19 S+    0.7  0.0  4228       00:03 bash            bash ./msallis_next_steps.sh
  73538    2293   0  19 Ssl   0.7  0.1 49624       21:20 gnome-terminal- /usr/libexec/gnome-terminal-server
  10129    9422   0  19 Ssl   0.6  0.0 14712    01:37:01 mysqld          mysqld
   2256       1   0  19 Ssl   0.6  0.0 22496    01:37:27 mysqld          /usr/sbin/mysqld
  95425       2 -20  39 I<    0.4  0.0     0       04:36 kworker/u129:2- [kworker/u129:2-rtw89_tx_wq]
  81995       2 -20  39 I<    0.4  0.0     0       10:03 kworker/u129:0- [kworker/u129:0-rtw89_tx_wq]
  73712       2 -20  39 I<    0.4  0.0     0       21:01 kworker/u129:1- [kworker/u129:1-rtw89_tx_wq]
      1       0   0  19 Ss    0.4  0.0 15608    01:37:34 systemd         /sbin/init splash
  32706   32683   0  19 Ssl   0.3  0.0 29440    01:15:04 python3.10      python3.10 ms_jarvis_unified_gateway.py
   3094    2293   0  19 Ssl   0.3  0.0 11452    01:37:23 gvfs-udisks2-vo /usr/libexec/gvfs-udisks2-volume-monitor
   3781       1   0  19 Ssl   0.3  0.0 23432    01:37:15 cloudflared     /usr/bin/cloudflared --no-autoupdate --config /etc/cloudflared/config.yml tunnel run

----
2026-05-22 20:02:13
    PID    PPID  NI PRI STAT %CPU %MEM   RSS     ELAPSED COMMAND         COMMAND
 101731       1   0  19 Rsl   100  0.2 73976       00:00 python          /opt/msjarvis-rebuild/crypto-venv/bin/python -m uvicorn auth_router_main:app --host 127.0.0.1 --port 8095
 101702  101700   0  19 Sl   66.6  0.0 28632       00:00 docker          docker logs --timestamps jarvis-local-resources-db
  15530    2891   0  19 Sl   41.3  1.4 432440   01:35:43 firefox         /snap/firefox/8306/usr/lib/firefox/firefox
 101689  100618   0  19 Sl+  11.7  0.1 36288       00:00 docker          docker stats --no-stream --format table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.NetIO}}\t{{.BlockIO}}\t{{.PIDs}}
  18778   15703   0  19 Sl    9.6  1.8 554576   01:33:06 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {ac5b4387-9da2-464f-b4d8-0e5ad08ea5b6} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 18 tab
   2891    2293   0  19 Ssl   5.5  0.4 127828   01:37:25 gnome-shell     /usr/bin/gnome-shell
   2483    2481   0  19 Rl+   5.0  0.1 39888    01:37:27 Xorg            /usr/lib/xorg/Xorg vt2 -displayfd 3 -auth /run/user/1000/gdm/Xauthority -nolisten tcp -background none -noreset -keeptty -novtswitch -verbose 3
  79812   15703   0  19 Sl    3.3  0.3 121232      12:29 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {27129b7f-ef84-4612-b180-3085916acbc2} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 90 tab
   3783       1   0  19 Ssl   2.4  0.3 113028   01:37:16 dockerd         /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
    980       2   -  90 S     2.4  0.0     0    01:37:30 irq/185-rtw89_p [irq/185-rtw89_pci]
  10937    8550   0  19 Sl    2.0  0.3 98740    01:37:02 ipfs            ipfs daemon --migrate=true --agent-version-suffix=docker
  15765   15703   0  19 Sl    1.6  0.3 120344   01:35:41 Privileged Cont /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:39334 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {b4f6c08e-b945-4945-a783-8654459f972e} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 3 tab
  98504    2891   0  19 Sl    1.3  0.6 186580      02:13 gnome-text-edit /usr/bin/gnome-text-editor
 100436    3454   -   0 SNl   0.8  0.0 29820       00:04 tracker-extract /usr/libexec/tracker-extract-3 --socket-fd 3
  14055   13977   0  19 Sl    0.8  0.1 37364    01:36:56 java            /opt/java/openjdk/bin/java -cp /var/lib/neo4j/plugins/*:/var/lib/neo4j/conf/*:/var/lib/neo4j/lib/* -XX:+UseG1GC -XX:-OmitStackTraceInFastThrow -XX:+AlwaysPreTouch -XX:+UnlockExperimentalVMOptions -XX:+TrustFinalNonStaticFields -XX:+DisableExplicitGC -Djdk.nio.maxCachedBufferSize=1024 -Dio.netty.tryReflectionSetAccessible=true -Djdk.tls.ephemeralDHKeySize=2048 -Djdk.tls.rejectClientInitiatedRenegotiation=true -XX:FlightRecorderOptions=stackdepth=256 -XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED -Dlog4j2.disable.jmx=true -Dfile.encoding=UTF-8 org.neo4j.server.CommunityEntryPoint --home-dir=/var/lib/neo4j --config-dir=/var/lib/neo4j/conf --console-mode
   7451    7350   0  19 Rsl   0.7  0.0  9256    01:37:03 redis-server    redis-server *:6379
  73538    2293   0  19 Ssl   0.7  0.1 49936       21:21 gnome-terminal- /usr/libexec/gnome-terminal-server
  10129    9422   0  19 Ssl   0.6  0.0 14712    01:37:02 mysqld          mysqld
   2256       1   0  19 Ssl   0.6  0.0 22496    01:37:28 mysqld          /usr/sbin/mysqld
 100422   73551   0  19 S+    0.6  0.0  4228       00:04 bash            bash ./msallis_next_steps.sh
  81995       2 -20  39 I<    0.4  0.0     0       10:04 kworker/u129:0- [kworker/u129:0-rtw89_tx_wq]
  95425       2 -20  39 I<    0.4  0.0     0       04:37 kworker/u129:2- [kworker/u129:2-rtw89_tx_wq]
  73712       2 -20  39 I<    0.4  0.0     0       21:02 kworker/u129:1- [kworker/u129:1-rtw89_tx_wq]
      1       0   0  19 Ss    0.4  0.0 15608    01:37:35 systemd         /sbin/init splash

----
2026-05-22 20:02:14
    PID    PPID  NI PRI STAT %CPU %MEM   RSS     ELAPSED COMMAND         COMMAND
  15530    2891   0  19 Sl   41.3  1.4 432400   01:35:44 firefox         /snap/firefox/8306/usr/lib/firefox/firefox
  18778   15703   0  19 Sl    9.6  1.8 556012   01:33:07 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {ac5b4387-9da2-464f-b4d8-0e5ad08ea5b6} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 18 tab
   2891    2293   0  19 Rsl   5.5  0.4 127828   01:37:26 gnome-shell     /usr/bin/gnome-shell
   2483    2481   0  19 Sl+   5.0  0.1 39888    01:37:28 Xorg            /usr/lib/xorg/Xorg vt2 -displayfd 3 -auth /run/user/1000/gdm/Xauthority -nolisten tcp -background none -noreset -keeptty -novtswitch -verbose 3
 101689  100618   0  19 Sl+   4.6  0.1 36300       00:01 docker          docker stats --no-stream --format table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.NetIO}}\t{{.BlockIO}}\t{{.PIDs}}
  79812   15703   0  19 Sl    3.3  0.3 121232      12:30 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {27129b7f-ef84-4612-b180-3085916acbc2} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 90 tab
   3783       1   0  19 Ssl   2.4  0.3 115064   01:37:17 dockerd         /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
    980       2   -  90 S     2.4  0.0     0    01:37:31 irq/185-rtw89_p [irq/185-rtw89_pci]
  10937    8550   0  19 Sl    2.0  0.3 98740    01:37:03 ipfs            ipfs daemon --migrate=true --agent-version-suffix=docker
  15765   15703   0  19 Sl    1.6  0.3 120344   01:35:42 Privileged Cont /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:39334 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {b4f6c08e-b945-4945-a783-8654459f972e} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 3 tab
  98504    2891   0  19 Sl    1.3  0.6 186580      02:14 gnome-text-edit /usr/bin/gnome-text-editor
  14055   13977   0  19 Sl    0.8  0.1 37392    01:36:57 java            /opt/java/openjdk/bin/java -cp /var/lib/neo4j/plugins/*:/var/lib/neo4j/conf/*:/var/lib/neo4j/lib/* -XX:+UseG1GC -XX:-OmitStackTraceInFastThrow -XX:+AlwaysPreTouch -XX:+UnlockExperimentalVMOptions -XX:+TrustFinalNonStaticFields -XX:+DisableExplicitGC -Djdk.nio.maxCachedBufferSize=1024 -Dio.netty.tryReflectionSetAccessible=true -Djdk.tls.ephemeralDHKeySize=2048 -Djdk.tls.rejectClientInitiatedRenegotiation=true -XX:FlightRecorderOptions=stackdepth=256 -XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED -Dlog4j2.disable.jmx=true -Dfile.encoding=UTF-8 org.neo4j.server.CommunityEntryPoint --home-dir=/var/lib/neo4j --config-dir=/var/lib/neo4j/conf --console-mode
   7451    7350   0  19 Ssl   0.7  0.0  9256    01:37:04 redis-server    redis-server *:6379
  73538    2293   0  19 Ssl   0.7  0.1 49936       21:22 gnome-terminal- /usr/libexec/gnome-terminal-server
 100436    3454   -   0 SNl   0.6  0.0 29820       00:05 tracker-extract /usr/libexec/tracker-extract-3 --socket-fd 3
  10129    9422   0  19 Ssl   0.6  0.0 14712    01:37:04 mysqld          mysqld
   2256       1   0  19 Ssl   0.6  0.0 22496    01:37:29 mysqld          /usr/sbin/mysqld
 100422   73551   0  19 S+    0.5  0.0  4228       00:05 bash            bash ./msallis_next_steps.sh
  81995       2 -20  39 I<    0.4  0.0     0       10:06 kworker/u129:0- [kworker/u129:0-rtw89_tx_wq]
  95425       2 -20  39 I<    0.4  0.0     0       04:38 kworker/u129:2- [kworker/u129:2-rtw89_tx_wq]
  73712       2 -20  39 I<    0.4  0.0     0       21:03 kworker/u129:1- [kworker/u129:1-rtw89_tx_wq]
      1       0   0  19 Ss    0.4  0.0 15608    01:37:36 systemd         /sbin/init splash
  32706   32683   0  19 Ssl   0.3  0.0 29440    01:15:06 python3.10      python3.10 ms_jarvis_unified_gateway.py
   3094    2293   0  19 Ssl   0.3  0.0 11452    01:37:25 gvfs-udisks2-vo /usr/libexec/gvfs-udisks2-volume-monitor

----
2026-05-22 20:02:15
    PID    PPID  NI PRI STAT %CPU %MEM   RSS     ELAPSED COMMAND         COMMAND
 101804  100617   0  19 R+    200  0.0  4768       00:00 ps              ps -eo pid,ppid,ni,pri,stat,%cpu,%mem,rss,etime,comm,args --sort=-%cpu
  15530    2891   0  19 Sl   41.3  1.4 432404   01:35:45 firefox         /snap/firefox/8306/usr/lib/firefox/firefox
  18778   15703   0  19 Sl    9.6  1.8 556216   01:33:08 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {ac5b4387-9da2-464f-b4d8-0e5ad08ea5b6} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 18 tab
   2891    2293   0  19 Ssl   5.5  0.4 127828   01:37:27 gnome-shell     /usr/bin/gnome-shell
   2483    2481   0  19 Sl+   5.0  0.1 39888    01:37:30 Xorg            /usr/lib/xorg/Xorg vt2 -displayfd 3 -auth /run/user/1000/gdm/Xauthority -nolisten tcp -background none -noreset -keeptty -novtswitch -verbose 3
  79812   15703   0  19 Sl    3.3  0.3 121232      12:31 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {27129b7f-ef84-4612-b180-3085916acbc2} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 90 tab
   3783       1   0  19 Ssl   2.4  0.3 107284   01:37:18 dockerd         /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
    980       2   -  90 S     2.4  0.0     0    01:37:32 irq/185-rtw89_p [irq/185-rtw89_pci]
  10937    8550   0  19 Sl    2.0  0.3 98740    01:37:04 ipfs            ipfs daemon --migrate=true --agent-version-suffix=docker
  15765   15703   0  19 Sl    1.6  0.3 120344   01:35:43 Privileged Cont /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:39334 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {b4f6c08e-b945-4945-a783-8654459f972e} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 3 tab
  98504    2891   0  19 Sl    1.3  0.6 186580      02:15 gnome-text-edit /usr/bin/gnome-text-editor
  14055   13977   0  19 Sl    0.8  0.1 37432    01:36:58 java            /opt/java/openjdk/bin/java -cp /var/lib/neo4j/plugins/*:/var/lib/neo4j/conf/*:/var/lib/neo4j/lib/* -XX:+UseG1GC -XX:-OmitStackTraceInFastThrow -XX:+AlwaysPreTouch -XX:+UnlockExperimentalVMOptions -XX:+TrustFinalNonStaticFields -XX:+DisableExplicitGC -Djdk.nio.maxCachedBufferSize=1024 -Dio.netty.tryReflectionSetAccessible=true -Djdk.tls.ephemeralDHKeySize=2048 -Djdk.tls.rejectClientInitiatedRenegotiation=true -XX:FlightRecorderOptions=stackdepth=256 -XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED -Dlog4j2.disable.jmx=true -Dfile.encoding=UTF-8 org.neo4j.server.CommunityEntryPoint --home-dir=/var/lib/neo4j --config-dir=/var/lib/neo4j/conf --console-mode
   7451    7350   0  19 Ssl   0.7  0.0  9256    01:37:05 redis-server    redis-server *:6379
  73538    2293   0  19 Ssl   0.7  0.1 49936       21:23 gnome-terminal- /usr/libexec/gnome-terminal-server
  10129    9422   0  19 Ssl   0.6  0.0 14712    01:37:05 mysqld          mysqld
   2256       1   0  19 Ssl   0.6  0.0 22496    01:37:30 mysqld          /usr/sbin/mysqld
 100436    3454   -   0 SNl   0.5  0.0 29820       00:06 tracker-extract /usr/libexec/tracker-extract-3 --socket-fd 3
  81995       2 -20  39 I<    0.4  0.0     0       10:07 kworker/u129:0- [kworker/u129:0-rtw89_tx_wq]
  95425       2 -20  39 I<    0.4  0.0     0       04:39 kworker/u129:2- [kworker/u129:2-rtw89_tx_wq]
  73712       2 -20  39 I<    0.4  0.0     0       21:04 kworker/u129:1- [kworker/u129:1-rtw89_tx_wq]
      1       0   0  19 Ss    0.4  0.0 15608    01:37:37 systemd         /sbin/init splash
 100422   73551   0  19 S+    0.4  0.0  4228       00:06 bash            bash ./msallis_next_steps.sh
  32706   32683   0  19 Ssl   0.3  0.0 29440    01:15:07 python3.10      python3.10 ms_jarvis_unified_gateway.py
   3094    2293   0  19 Ssl   0.3  0.0 11452    01:37:26 gvfs-udisks2-vo /usr/libexec/gvfs-udisks2-volume-monitor

----
2026-05-22 20:02:16
    PID    PPID  NI PRI STAT %CPU %MEM   RSS     ELAPSED COMMAND         COMMAND
  15530    2891   0  19 Sl   41.3  1.4 432408   01:35:46 firefox         /snap/firefox/8306/usr/lib/firefox/firefox
  18778   15703   0  19 Sl    9.6  1.8 556212   01:33:09 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {ac5b4387-9da2-464f-b4d8-0e5ad08ea5b6} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 18 tab
 101808  100618   0  19 Sl+   8.8  0.1 35644       00:00 docker          docker stats --no-stream --format table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.NetIO}}\t{{.BlockIO}}\t{{.PIDs}}
   2891    2293   0  19 Ssl   5.5  0.4 127828   01:37:28 gnome-shell     /usr/bin/gnome-shell
   2483    2481   0  19 Sl+   5.0  0.1 39888    01:37:31 Xorg            /usr/lib/xorg/Xorg vt2 -displayfd 3 -auth /run/user/1000/gdm/Xauthority -nolisten tcp -background none -noreset -keeptty -novtswitch -verbose 3
  79812   15703   0  19 Sl    3.3  0.3 121232      12:32 Isolated Web Co /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:45447 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {27129b7f-ef84-4612-b180-3085916acbc2} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 90 tab
   3783       1   0  19 Ssl   2.4  0.3 107404   01:37:20 dockerd         /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
    980       2   -  90 S     2.4  0.0     0    01:37:33 irq/185-rtw89_p [irq/185-rtw89_pci]
  10937    8550   0  19 Sl    2.0  0.3 98740    01:37:05 ipfs            ipfs daemon --migrate=true --agent-version-suffix=docker
  15765   15703   0  19 Sl    1.6  0.3 120344   01:35:44 Privileged Cont /snap/firefox/8306/usr/lib/firefox/firefox -contentproc -isForBrowser -prefsHandle 0:39334 -prefMapHandle 1:287340 -jsInitHandle 2:156120 -parentBuildID 20260512031714 -sandboxReporter 3 -chrootClient 4 -ipcHandle 5 -initialChannelId {b4f6c08e-b945-4945-a783-8654459f972e} -parentPid 15530 -crashReporter 6 -crashHelper 7 -greomni /snap/firefox/8306/usr/lib/firefox/omni.ja -appomni /snap/firefox/8306/usr/lib/firefox/browser/omni.ja -appDir /snap/firefox/8306/usr/lib/firefox/browser 3 tab
  98504    2891   0  19 Sl    1.2  0.6 186580      02:16 gnome-text-edit /usr/bin/gnome-text-editor
  14055   13977   0  19 Sl    0.8  0.1 37456    01:36:59 java            /opt/java/openjdk/bin/java -cp /var/lib/neo4j/plugins/*:/var/lib/neo4j/conf/*:/var/lib/neo4j/lib/* -XX:+UseG1GC -XX:-OmitStackTraceInFastThrow -XX:+AlwaysPreTouch -XX:+UnlockExperimentalVMOptions -XX:+TrustFinalNonStaticFields -XX:+DisableExplicitGC -Djdk.nio.maxCachedBufferSize=1024 -Dio.netty.tryReflectionSetAccessible=true -Djdk.tls.ephemeralDHKeySize=2048 -Djdk.tls.rejectClientInitiatedRenegotiation=true -XX:FlightRecorderOptions=stackdepth=256 -XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED -Dlog4j2.disable.jmx=true -Dfile.encoding=UTF-8 org.neo4j.server.CommunityEntryPoint --home-dir=/var/lib/neo4j --config-dir=/var/lib/neo4j/conf --console-mode
   7451    7350   0  19 Ssl   0.7  0.0  9256    01:37:06 redis-server    redis-server *:6379
  73538    2293   0  19 Ssl   0.7  0.1 49936       21:24 gnome-terminal- /usr/libexec/gnome-terminal-server
  10129    9422   0  19 Ssl   0.6  0.0 14712    01:37:06 mysqld          mysqld
   2256       1   0  19 Ssl   0.6  0.0 22496    01:37:31 mysqld          /usr/sbin/mysqld
 100436    3454   -   0 SNl   0.5  0.0 29820       00:07 tracker-extract /usr/libexec/tracker-extract-3 --socket-fd 3
  81995       2 -20  39 I<    0.4  0.0     0       10:08 kworker/u129:0- [kworker/u129:0-rtw89_tx_wq]
  95425       2 -20  39 I<    0.4  0.0     0       04:40 kworker/u129:2- [kworker/u129:2-rtw89_tx_wq]
  73712       2 -20  39 I<    0.4  0.0     0       21:05 kworker/u129:1- [kworker/u129:1-rtw89_tx_wq]
      1       0   0  19 Ss    0.4  0.0 15608    01:37:38 systemd         /sbin/init splash
  32706   32683   0  19 Ssl   0.3  0.0 29440    01:15:08 python3.10      python3.10 ms_jarvis_unified_gateway.py

===== DOCKER STATS SNAPSHOT =====
2026-05-22 20:02:09
NAME                                                    CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O         PIDS
jarvis-unified-gateway                                  0.16%     33.62MiB / 4GiB       0.82%     14MB / 1.5MB      95.5MB / 82.7MB   2
jarvis-brain-orchestrator                               0.11%     9.297MiB / 29.08GiB   0.03%     146kB / 653B      10.4MB / 26MB     5
jarvis-ollama                                           0.00%     8.549GiB / 28GiB      30.53%    524kB / 249kB     53.2GB / 764MB    17
jarvis-69dgm-bridge                                     0.18%     15.56MiB / 29.08GiB   0.05%     0B / 0B           1.98MB / 21.8MB   1
jarvis-main-brain                                       0.12%     60.52MiB / 29.08GiB   0.20%     5.64MB / 3.63MB   113MB / 93.8MB    36
jarvis-20llm-production                                 0.11%     20.64MiB / 29.08GiB   0.07%     287kB / 65.7kB    28MB / 41.2MB     5
llm21-proxy                                             0.13%     18.2MiB / 29.08GiB    0.06%     281kB / 15.3kB    21.6MB / 25.6MB   2
llm22-proxy                                             0.16%     15.57MiB / 29.08GiB   0.05%     273kB / 16.7kB    20.8MB / 26.7MB   2
jarvis-wv-entangled-gateway                             0.12%     16.7MiB / 29.08GiB    0.06%     261kB / 126B      22.8MB / 23.9MB   5
jarvis-psychology-services                              0.11%     16.64MiB / 29.08GiB   0.06%     264kB / 1.19kB    18.3MB / 19.1MB   6
jarvis-toroidal                                         0.13%     13.18MiB / 29.08GiB   0.04%     256kB / 709B      15.2MB / 19.7MB   1
jarvis-autonomous-learner                               0.00%     0B / 0B               0.00%     0B / 0B           0B / 0B           0
jarvis-rag-server                                       0.11%     24.86MiB / 29.08GiB   0.08%     269kB / 6.38kB    63.2MB / 51.3MB   36
jarvis-aaacpe-rag                                       0.12%     22.15MiB / 29.08GiB   0.07%     147kB / 643B      76MB / 54.5MB     102
jarvis-gis-rag                                          0.15%     16.56MiB / 29.08GiB   0.06%     147kB / 126B      17.9MB / 13.7MB   1
jarvis-spiritual-rag                                    0.15%     17.61MiB / 29.08GiB   0.06%     148kB / 1.92kB    12.1MB / 14.8MB   1
jarvis-hippocampus                                      0.13%     18.63MiB / 29.08GiB   0.06%     148kB / 2.49kB    61.9MB / 53.1MB   36
jarvis-neurobiological-master                           0.10%     16.13MiB / 29.08GiB   0.05%     700kB / 397kB     19.7MB / 22.8MB   5
591cd058cd26_jarvis-consciousness-bridge                0.16%     15.04MiB / 29.08GiB   0.05%     262kB / 264B      9.23MB / 24MB     1
dd0340814f6d_jarvis-eeg-beta                            0.11%     34.52MiB / 29.08GiB   0.12%     1.17MB / 538kB    21.3MB / 63.3MB   6
a1f602068b45_jarvis-eeg-delta                           0.10%     34.03MiB / 29.08GiB   0.11%     580kB / 474kB     21.3MB / 61.2MB   6
llm7-proxy                                              0.15%     18.91MiB / 29.08GiB   0.06%     276kB / 16.6kB    21.1MB / 25.6MB   2
llm11-proxy                                             0.15%     15.36MiB / 29.08GiB   0.05%     273kB / 11.1kB    16.9MB / 22.1MB   1
llm17-proxy                                             0.18%     17.48MiB / 29.08GiB   0.06%     282kB / 15.8kB    21.9MB / 26.6MB   2
llm3-proxy                                              0.14%     17.1MiB / 29.08GiB    0.06%     281kB / 16.1kB    21.6MB / 26.3MB   2
12d6dc1b1e49_jarvis-chroma                              0.00%     29.3MiB / 29.08GiB    0.10%     1.06MB / 17.7MB   212MB / 126MB     68
llm19-proxy                                             0.15%     16.7MiB / 29.08GiB    0.06%     282kB / 15.1kB    22.2MB / 26.2MB   2
jarvis-local-resources                                  0.12%     16.61MiB / 29.08GiB   0.06%     360kB / 82.9kB    15.5MB / 11.4MB   1
jarvis-woah                                             0.13%     15.54MiB / 29.08GiB   0.05%     263kB / 694B      23.5MB / 22.9MB   5
11aba8ab78dd_jarvis-temporal-consciousness              0.11%     17.8MiB / 29.08GiB    0.06%     262kB / 662B      21.1MB / 18.2MB   5
llm15-proxy                                             0.14%     18.09MiB / 29.08GiB   0.06%     283kB / 16.2kB    26.6MB / 27.6MB   2
jarvis-blood-brain-barrier                              0.11%     23.54MiB / 29.08GiB   0.08%     481kB / 225kB     24.7MB / 22.9MB   2
msjarvis-rebuild-nbb_prefrontal_cortex-1                3.30%     51.5MiB / 29.08GiB    0.17%     300kB / 52kB      15.5MB / 1.3GB    34
jarvis-web-research                                     0.16%     15.01MiB / 29.08GiB   0.05%     332kB / 7.15kB    5.24MB / 22.4MB   1
msjarvis-rebuild-nbb_qualia_engine-1                    0.15%     17.28MiB / 29.08GiB   0.06%     389kB / 104kB     16.3MB / 16.6MB   2
jarvis-redis                                            0.57%     6.008MiB / 29.08GiB   0.02%     1.52MB / 606kB    11.9MB / 545kB    6
llm8-proxy                                              0.14%     17.77MiB / 29.08GiB   0.06%     275kB / 15.5kB    21.6MB / 25.4MB   2
llm2-proxy                                              0.15%     19.07MiB / 29.08GiB   0.06%     278kB / 16.6kB    20.1MB / 23.4MB   2
llm5-proxy                                              0.14%     16.54MiB / 29.08GiB   0.06%     280kB / 14.9kB    15.9MB / 20.8MB   2
msjarvis-rebuild-nbb_darwin_godel_machines-1            0.13%     16.1MiB / 29.08GiB    0.05%     257kB / 716B      13.8MB / 17MB     2
msjarvis-rebuild-nbb_mother_carrie_protocols-1          0.10%     15.74MiB / 29.08GiB   0.05%     265kB / 5.66kB    3.82MB / 35.9MB   5
llm20-proxy                                             0.13%     18.98MiB / 29.08GiB   0.06%     278kB / 16.3kB    19.7MB / 23.3MB   2
llm10-proxy                                             0.15%     17.54MiB / 29.08GiB   0.06%     278kB / 16kB      21MB / 25MB       2
llm1-proxy                                              0.12%     17.54MiB / 29.08GiB   0.06%     274kB / 14.7kB    18.1MB / 23.3MB   2
llm9-proxy                                              0.14%     17.55MiB / 29.08GiB   0.06%     282kB / 16.1kB    21.8MB / 26.7MB   2
llm4-proxy                                              0.12%     19.14MiB / 29.08GiB   0.06%     279kB / 16.5kB    21.6MB / 24.5MB   2
jarvis-fractal-consciousness                            0.13%     5.668MiB / 29.08GiB   0.02%     263kB / 264B      34.1MB / 30.3MB   1
llm13-proxy                                             0.12%     15.61MiB / 29.08GiB   0.05%     279kB / 14.5kB    18.3MB / 24.3MB   2
jarvis-semaphore                                        0.13%     21.03MiB / 29.08GiB   0.07%     267kB / 9.26kB    22.2MB / 21.2MB   2
jarvis-agents-service                                   0.14%     16.1MiB / 29.08GiB    0.05%     263kB / 646B      24.2MB / 21.7MB   5
llm14-proxy                                             0.13%     20.62MiB / 29.08GiB   0.07%     278kB / 16.7kB    23.5MB / 24.6MB   2
llm6-proxy                                              0.14%     17.06MiB / 29.08GiB   0.06%     282kB / 15.3kB    37.2MB / 31MB     2
llm12-proxy                                             0.14%     19.15MiB / 29.08GiB   0.06%     278kB / 16.3kB    20.2MB / 24.1MB   2
llm18-proxy                                             0.15%     17.37MiB / 29.08GiB   0.06%     280kB / 15.3kB    21.1MB / 25.4MB   2
llm16-proxy                                             0.13%     17.41MiB / 29.08GiB   0.06%     281kB / 16.4kB    22.4MB / 26.9MB   2
jarvis-judge-pipeline                                   0.12%     29.15MiB / 29.08GiB   0.10%     273kB / 25.9kB    15.4MB / 26.2MB   5
jarvis-judge-truth                                      0.15%     21.15MiB / 29.08GiB   0.07%     267kB / 1.54kB    6.01MB / 20.3MB   1
jarvis-judge-ethics                                     0.13%     20.93MiB / 29.08GiB   0.07%     267kB / 1.52kB    7.35MB / 21.9MB   1
jarvis-judge-consistency                                0.12%     20.02MiB / 29.08GiB   0.07%     266kB / 1.54kB    5.1MB / 20.6MB    1
jarvis-judge-alignment                                  0.14%     22.12MiB / 29.08GiB   0.07%     269kB / 1.54kB    22.7MB / 23.5MB   1
jarvis-lm-synthesizer                                   0.12%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
msjarvis-rebuild-nbb_pituitary_gland-1                  0.12%     28.59MiB / 29.08GiB   0.10%     1.13MB / 1.25MB   27.1MB / 58.8MB   7
jarvis-eeg-theta                                        0.10%     80MiB / 29.08GiB      0.27%     236MB / 1.01MB    127MB / 113MB     6
nbb-i-containers                                        0.11%     17.16MiB / 29.08GiB   0.06%     147kB / 667B      23.8MB / 24.5MB   5
jarvis-i-containers                                     0.18%     29.01MiB / 29.08GiB   0.10%     823kB / 224MB     55.8MB / 61.8MB   1
msjarvis-rebuild-nbb_spiritual_maternal_integration-1   0.11%     9.512MiB / 29.08GiB   0.03%     267kB / 6.83kB    39.8MB / 46.7MB   5
msjarvis-rebuild-nbb_heteroglobulin_transport-1         0.09%     16.49MiB / 29.08GiB   0.06%     265kB / 6.82kB    3.29MB / 34.8MB   5
msjarvis-rebuild-nbb_spiritual_root-1                   0.12%     15.48MiB / 29.08GiB   0.05%     261kB / 5.75kB    4.45MB / 33.8MB   5
msjarvis-rebuild-nbb_blood_brain_barrier-1              0.16%     15.66MiB / 29.08GiB   0.05%     418kB / 188kB     15.7MB / 22.6MB   2
msjarvis-rebuild-nbb_consciousness_containers-1         0.11%     16.72MiB / 29.08GiB   0.06%     426kB / 222kB     4.2MB / 33.7MB    5
jarvis-hilbert-state                                    0.11%     18.8MiB / 1GiB        1.84%     257kB / 126B      52.5MB / 39.8MB   6
jarvis-mother-protocols                                 0.12%     17.14MiB / 29.08GiB   0.06%     264kB / 656B      32MB / 24.3MB     5
jarvis-swarm-intelligence                               0.01%     11.41MiB / 29.08GiB   0.04%     262kB / 912B      28.3MB / 39.3MB   1
mysql                                                   0.51%     18.46MiB / 29.08GiB   0.06%     260kB / 126B      92.1MB / 185MB    37
neo4j                                                   0.61%     46.89MiB / 29.08GiB   0.16%     238kB / 290B      177MB / 451MB     88
ipfs                                                    0.47%     93.79MiB / 29.08GiB   0.31%     99.8MB / 88.7MB   312MB / 56.3MB    38
jarvis-session-sidecar                                  0.14%     14.31MiB / 29.08GiB   0.05%     261kB / 126B      17.5MB / 24MB     1
jarvis-constitutional-guardian                          0.16%     17.48MiB / 29.08GiB   0.06%     484kB / 180kB     13.2MB / 12.8MB   1
msjarvis-rebuild-nbb_woah_algorithms-1                  0.13%     16.72MiB / 29.08GiB   0.06%     263kB / 4.69kB    20.5MB / 30.9MB   1
jarvis-qualia-engine                                    0.14%     17.43MiB / 29.08GiB   0.06%     479kB / 177kB     27.6MB / 18.1MB   1
jarvis-fifth-dgm                                        0.17%     16.82MiB / 29.08GiB   0.06%     260kB / 1.41kB    41.2MB / 35.5MB   1
msjarvis-rebuild-nbb_subconscious-1                     0.09%     15.08MiB / 29.08GiB   0.05%     377kB / 108kB     4.43MB / 34.1MB   5
psychological_rag_domain                                0.11%     18.55MiB / 29.08GiB   0.06%     263kB / 1.67kB    59.6MB / 57.5MB   36
jarvis-local-resources-db                               0.00%     11.93MiB / 29.08GiB   0.04%     261kB / 6.12kB    66.9MB / 12.3MB   6
jarvis-gbim-temporal-indexer                            0.13%     11.58MiB / 29.08GiB   0.04%     262kB / 126B      23.3MB / 24.7MB   5
jarvis-jaeger                                           0.03%     8.305MiB / 29.08GiB   0.03%     124kB / 126B      40.6MB / 1.56MB   15

----
2026-05-22 20:02:12
NAME                                                    CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O         PIDS
jarvis-unified-gateway                                  7.81%     35.79MiB / 4GiB       0.87%     14MB / 1.51MB     95.5MB / 82.7MB   2
jarvis-brain-orchestrator                               0.13%     9.297MiB / 29.08GiB   0.03%     146kB / 653B      10.4MB / 26MB     5
jarvis-ollama                                           0.00%     8.549GiB / 28GiB      30.53%    524kB / 249kB     53.2GB / 764MB    17
jarvis-69dgm-bridge                                     0.14%     15.56MiB / 29.08GiB   0.05%     0B / 0B           1.98MB / 21.8MB   1
jarvis-main-brain                                       0.22%     60.76MiB / 29.08GiB   0.20%     5.64MB / 3.63MB   113MB / 93.8MB    36
jarvis-20llm-production                                 0.15%     20.64MiB / 29.08GiB   0.07%     287kB / 65.7kB    28MB / 41.2MB     5
llm21-proxy                                             0.19%     18.2MiB / 29.08GiB    0.06%     281kB / 15.3kB    21.6MB / 25.6MB   2
llm22-proxy                                             0.20%     15.57MiB / 29.08GiB   0.05%     273kB / 16.7kB    20.8MB / 26.7MB   2
jarvis-wv-entangled-gateway                             0.14%     16.7MiB / 29.08GiB    0.06%     261kB / 126B      22.8MB / 23.9MB   5
jarvis-psychology-services                              0.13%     16.64MiB / 29.08GiB   0.06%     264kB / 1.19kB    18.3MB / 19.1MB   6
jarvis-toroidal                                         0.19%     13.18MiB / 29.08GiB   0.04%     256kB / 709B      15.2MB / 19.7MB   1
jarvis-autonomous-learner                               0.00%     0B / 0B               0.00%     0B / 0B           0B / 0B           0
jarvis-rag-server                                       0.13%     24.86MiB / 29.08GiB   0.08%     269kB / 6.38kB    63.2MB / 51.3MB   36
jarvis-aaacpe-rag                                       0.14%     22.15MiB / 29.08GiB   0.07%     147kB / 643B      76MB / 54.5MB     102
jarvis-gis-rag                                          0.18%     16.56MiB / 29.08GiB   0.06%     147kB / 126B      17.9MB / 13.7MB   1
jarvis-spiritual-rag                                    0.20%     17.61MiB / 29.08GiB   0.06%     148kB / 1.92kB    12.1MB / 14.8MB   1
jarvis-hippocampus                                      0.14%     18.63MiB / 29.08GiB   0.06%     148kB / 2.49kB    61.9MB / 53.1MB   36
jarvis-neurobiological-master                           0.20%     16.38MiB / 29.08GiB   0.06%     701kB / 398kB     19.7MB / 22.8MB   5
591cd058cd26_jarvis-consciousness-bridge                0.18%     15.04MiB / 29.08GiB   0.05%     262kB / 264B      9.23MB / 24MB     1
dd0340814f6d_jarvis-eeg-beta                            0.14%     34.52MiB / 29.08GiB   0.12%     1.17MB / 538kB    21.3MB / 63.3MB   6
a1f602068b45_jarvis-eeg-delta                           0.17%     34.03MiB / 29.08GiB   0.11%     580kB / 474kB     21.3MB / 61.2MB   6
llm7-proxy                                              0.18%     18.91MiB / 29.08GiB   0.06%     276kB / 16.6kB    21.1MB / 25.6MB   2
llm11-proxy                                             0.19%     15.36MiB / 29.08GiB   0.05%     273kB / 11.1kB    16.9MB / 22.1MB   1
llm17-proxy                                             0.18%     17.48MiB / 29.08GiB   0.06%     282kB / 15.8kB    21.9MB / 26.6MB   2
llm3-proxy                                              0.19%     17.1MiB / 29.08GiB    0.06%     281kB / 16.1kB    21.6MB / 26.3MB   2
12d6dc1b1e49_jarvis-chroma                              0.00%     29.3MiB / 29.08GiB    0.10%     1.06MB / 17.7MB   212MB / 126MB     68
llm19-proxy                                             0.19%     16.7MiB / 29.08GiB    0.06%     282kB / 15.1kB    22.2MB / 26.2MB   2
jarvis-local-resources                                  0.18%     16.61MiB / 29.08GiB   0.06%     360kB / 82.9kB    15.5MB / 11.4MB   1
jarvis-woah                                             0.15%     15.54MiB / 29.08GiB   0.05%     263kB / 694B      23.5MB / 22.9MB   5
11aba8ab78dd_jarvis-temporal-consciousness              0.13%     17.8MiB / 29.08GiB    0.06%     262kB / 662B      21.1MB / 18.2MB   5
llm15-proxy                                             0.19%     18.09MiB / 29.08GiB   0.06%     283kB / 16.2kB    26.6MB / 27.6MB   2
jarvis-blood-brain-barrier                              0.29%     23.79MiB / 29.08GiB   0.08%     482kB / 225kB     24.7MB / 22.9MB   2
msjarvis-rebuild-nbb_prefrontal_cortex-1                4.32%     51.5MiB / 29.08GiB    0.17%     300kB / 52kB      15.5MB / 1.3GB    34
jarvis-web-research                                     0.17%     15.01MiB / 29.08GiB   0.05%     332kB / 7.15kB    5.24MB / 22.4MB   1
msjarvis-rebuild-nbb_qualia_engine-1                    0.18%     17.28MiB / 29.08GiB   0.06%     389kB / 104kB     16.3MB / 16.6MB   2
jarvis-redis                                            0.89%     6.258MiB / 29.08GiB   0.02%     1.52MB / 607kB    11.9MB / 545kB    6
llm8-proxy                                              0.17%     17.77MiB / 29.08GiB   0.06%     275kB / 15.5kB    21.6MB / 25.4MB   2
llm2-proxy                                              0.20%     19.07MiB / 29.08GiB   0.06%     278kB / 16.6kB    20.1MB / 23.4MB   2
llm5-proxy                                              0.19%     16.54MiB / 29.08GiB   0.06%     280kB / 14.9kB    15.9MB / 20.8MB   2
msjarvis-rebuild-nbb_darwin_godel_machines-1            0.20%     16.1MiB / 29.08GiB    0.05%     257kB / 716B      13.8MB / 17MB     2
msjarvis-rebuild-nbb_mother_carrie_protocols-1          0.15%     15.74MiB / 29.08GiB   0.05%     265kB / 5.66kB    3.82MB / 35.9MB   5
llm20-proxy                                             0.17%     18.98MiB / 29.08GiB   0.06%     278kB / 16.3kB    19.7MB / 23.3MB   2
llm10-proxy                                             0.18%     17.54MiB / 29.08GiB   0.06%     278kB / 16kB      21MB / 25MB       2
llm1-proxy                                              0.18%     17.54MiB / 29.08GiB   0.06%     274kB / 14.7kB    18.1MB / 23.3MB   2
llm9-proxy                                              0.19%     17.55MiB / 29.08GiB   0.06%     282kB / 16.1kB    21.8MB / 26.7MB   2
llm4-proxy                                              0.18%     19.14MiB / 29.08GiB   0.06%     279kB / 16.5kB    21.6MB / 24.5MB   2
jarvis-fractal-consciousness                            0.16%     5.668MiB / 29.08GiB   0.02%     263kB / 264B      34.1MB / 30.3MB   1
llm13-proxy                                             0.20%     15.61MiB / 29.08GiB   0.05%     279kB / 14.5kB    18.3MB / 24.3MB   2
jarvis-semaphore                                        0.19%     21.03MiB / 29.08GiB   0.07%     267kB / 9.26kB    22.2MB / 21.2MB   2
jarvis-agents-service                                   0.17%     16.1MiB / 29.08GiB    0.05%     263kB / 646B      24.2MB / 21.7MB   5
llm14-proxy                                             0.18%     20.62MiB / 29.08GiB   0.07%     278kB / 16.7kB    23.5MB / 24.6MB   2
llm6-proxy                                              0.20%     17.06MiB / 29.08GiB   0.06%     282kB / 15.3kB    37.2MB / 31MB     2
llm12-proxy                                             0.20%     19.15MiB / 29.08GiB   0.06%     278kB / 16.3kB    20.2MB / 24.1MB   2
llm18-proxy                                             0.18%     17.37MiB / 29.08GiB   0.06%     280kB / 15.3kB    21.1MB / 25.4MB   2
llm16-proxy                                             0.21%     17.41MiB / 29.08GiB   0.06%     281kB / 16.4kB    22.4MB / 26.9MB   2
jarvis-judge-pipeline                                   0.19%     29.15MiB / 29.08GiB   0.10%     273kB / 25.9kB    15.4MB / 26.2MB   5
jarvis-judge-truth                                      0.18%     21.15MiB / 29.08GiB   0.07%     267kB / 1.54kB    6.01MB / 20.3MB   1
jarvis-judge-ethics                                     0.17%     20.93MiB / 29.08GiB   0.07%     267kB / 1.52kB    7.35MB / 21.9MB   1
jarvis-judge-consistency                                0.18%     20.02MiB / 29.08GiB   0.07%     266kB / 1.54kB    5.1MB / 20.6MB    1
jarvis-judge-alignment                                  0.18%     22.12MiB / 29.08GiB   0.07%     269kB / 1.54kB    22.7MB / 23.5MB   1
jarvis-lm-synthesizer                                   0.13%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
msjarvis-rebuild-nbb_pituitary_gland-1                  0.17%     28.59MiB / 29.08GiB   0.10%     1.13MB / 1.25MB   27.1MB / 58.8MB   7
jarvis-eeg-theta                                        0.15%     80MiB / 29.08GiB      0.27%     236MB / 1.01MB    127MB / 113MB     6
nbb-i-containers                                        0.13%     17.16MiB / 29.08GiB   0.06%     147kB / 667B      23.8MB / 24.5MB   5
jarvis-i-containers                                     0.27%     29.01MiB / 29.08GiB   0.10%     823kB / 224MB     55.8MB / 61.8MB   1
msjarvis-rebuild-nbb_spiritual_maternal_integration-1   0.14%     9.512MiB / 29.08GiB   0.03%     267kB / 6.83kB    39.8MB / 46.7MB   5
msjarvis-rebuild-nbb_heteroglobulin_transport-1         0.12%     16.49MiB / 29.08GiB   0.06%     265kB / 6.82kB    3.29MB / 34.8MB   5
msjarvis-rebuild-nbb_spiritual_root-1                   0.13%     15.48MiB / 29.08GiB   0.05%     261kB / 5.75kB    4.45MB / 33.8MB   5
msjarvis-rebuild-nbb_blood_brain_barrier-1              0.17%     15.66MiB / 29.08GiB   0.05%     418kB / 188kB     15.7MB / 22.6MB   2
msjarvis-rebuild-nbb_consciousness_containers-1         0.13%     16.72MiB / 29.08GiB   0.06%     426kB / 222kB     4.2MB / 33.7MB    5
jarvis-hilbert-state                                    0.15%     18.8MiB / 1GiB        1.84%     257kB / 126B      52.5MB / 39.8MB   6
jarvis-mother-protocols                                 0.17%     17.14MiB / 29.08GiB   0.06%     264kB / 656B      32MB / 24.3MB     5
jarvis-swarm-intelligence                               0.01%     11.41MiB / 29.08GiB   0.04%     262kB / 912B      28.3MB / 39.3MB   1
mysql                                                   0.69%     18.46MiB / 29.08GiB   0.06%     260kB / 126B      92.1MB / 185MB    37
neo4j                                                   0.63%     47.47MiB / 29.08GiB   0.16%     238kB / 290B      177MB / 451MB     88
ipfs                                                    0.31%     94.1MiB / 29.08GiB    0.32%     99.8MB / 88.7MB   312MB / 56.3MB    38
jarvis-session-sidecar                                  0.20%     14.31MiB / 29.08GiB   0.05%     261kB / 126B      17.5MB / 24MB     1
jarvis-constitutional-guardian                          0.34%     17.73MiB / 29.08GiB   0.06%     485kB / 180kB     13.2MB / 12.8MB   1
msjarvis-rebuild-nbb_woah_algorithms-1                  0.17%     16.72MiB / 29.08GiB   0.06%     263kB / 4.69kB    20.5MB / 30.9MB   1
jarvis-qualia-engine                                    0.31%     17.67MiB / 29.08GiB   0.06%     479kB / 178kB     27.6MB / 18.1MB   1
jarvis-fifth-dgm                                        0.17%     16.82MiB / 29.08GiB   0.06%     260kB / 1.41kB    41.2MB / 35.5MB   1
msjarvis-rebuild-nbb_subconscious-1                     0.15%     15.08MiB / 29.08GiB   0.05%     377kB / 108kB     4.43MB / 34.1MB   5
psychological_rag_domain                                0.13%     18.55MiB / 29.08GiB   0.06%     263kB / 1.67kB    59.6MB / 57.5MB   36
jarvis-local-resources-db                               0.00%     11.93MiB / 29.08GiB   0.04%     261kB / 6.12kB    66.9MB / 12.3MB   6
jarvis-gbim-temporal-indexer                            0.13%     11.58MiB / 29.08GiB   0.04%     262kB / 126B      23.3MB / 24.7MB   5
jarvis-jaeger                                           0.02%     8.305MiB / 29.08GiB   0.03%     124kB / 126B      40.6MB / 1.56MB   15

----
2026-05-22 20:02:15
NAME                                                    CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O         PIDS
jarvis-unified-gateway                                  0.23%     34.93MiB / 4GiB       0.85%     14MB / 1.51MB     95.5MB / 82.7MB   2
jarvis-brain-orchestrator                               0.14%     9.297MiB / 29.08GiB   0.03%     146kB / 653B      10.4MB / 26MB     5
jarvis-ollama                                           0.00%     8.549GiB / 28GiB      30.53%    524kB / 249kB     53.2GB / 764MB    17
jarvis-69dgm-bridge                                     0.21%     15.56MiB / 29.08GiB   0.05%     0B / 0B           1.98MB / 21.8MB   1
jarvis-main-brain                                       0.16%     60.76MiB / 29.08GiB   0.20%     5.64MB / 3.63MB   113MB / 93.8MB    36
jarvis-20llm-production                                 0.16%     20.64MiB / 29.08GiB   0.07%     287kB / 65.7kB    28MB / 41.2MB     5
llm21-proxy                                             0.20%     18.2MiB / 29.08GiB    0.06%     281kB / 15.3kB    21.6MB / 25.6MB   2
llm22-proxy                                             0.21%     15.57MiB / 29.08GiB   0.05%     273kB / 16.7kB    20.8MB / 26.7MB   2
jarvis-wv-entangled-gateway                             0.16%     16.7MiB / 29.08GiB    0.06%     261kB / 126B      22.8MB / 23.9MB   5
jarvis-psychology-services                              0.15%     16.64MiB / 29.08GiB   0.06%     264kB / 1.19kB    18.3MB / 19.1MB   6
jarvis-toroidal                                         0.18%     13.18MiB / 29.08GiB   0.04%     256kB / 709B      15.2MB / 19.7MB   1
jarvis-autonomous-learner                               0.00%     0B / 0B               0.00%     0B / 0B           0B / 0B           0
jarvis-rag-server                                       0.16%     24.86MiB / 29.08GiB   0.08%     269kB / 6.38kB    63.2MB / 51.3MB   36
jarvis-aaacpe-rag                                       0.14%     22.15MiB / 29.08GiB   0.07%     147kB / 643B      76MB / 54.5MB     102
jarvis-gis-rag                                          0.18%     16.56MiB / 29.08GiB   0.06%     147kB / 126B      17.9MB / 13.7MB   1
jarvis-spiritual-rag                                    0.21%     17.61MiB / 29.08GiB   0.06%     148kB / 1.92kB    12.1MB / 14.8MB   1
jarvis-hippocampus                                      0.14%     18.63MiB / 29.08GiB   0.06%     148kB / 2.49kB    61.9MB / 53.1MB   36
jarvis-neurobiological-master                           0.18%     16.38MiB / 29.08GiB   0.05%     702kB / 399kB     19.7MB / 22.8MB   5
591cd058cd26_jarvis-consciousness-bridge                0.20%     15.04MiB / 29.08GiB   0.05%     262kB / 264B      9.23MB / 24MB     1
dd0340814f6d_jarvis-eeg-beta                            0.14%     34.52MiB / 29.08GiB   0.12%     1.17MB / 538kB    21.3MB / 63.3MB   6
a1f602068b45_jarvis-eeg-delta                           0.19%     34.79MiB / 29.08GiB   0.12%     583kB / 477kB     21.3MB / 61.2MB   6
llm7-proxy                                              0.19%     18.91MiB / 29.08GiB   0.06%     276kB / 16.6kB    21.1MB / 25.6MB   2
llm11-proxy                                             0.18%     15.36MiB / 29.08GiB   0.05%     273kB / 11.1kB    16.9MB / 22.1MB   1
llm17-proxy                                             0.21%     17.48MiB / 29.08GiB   0.06%     282kB / 15.8kB    21.9MB / 26.6MB   2
llm3-proxy                                              0.21%     17.1MiB / 29.08GiB    0.06%     281kB / 16.1kB    21.6MB / 26.3MB   2
12d6dc1b1e49_jarvis-chroma                              0.00%     29.31MiB / 29.08GiB   0.10%     1.06MB / 17.7MB   212MB / 126MB     68
llm19-proxy                                             0.21%     16.7MiB / 29.08GiB    0.06%     282kB / 15.1kB    22.2MB / 26.2MB   2
jarvis-local-resources                                  0.18%     16.86MiB / 29.08GiB   0.06%     361kB / 83.4kB    15.5MB / 11.4MB   1
jarvis-woah                                             0.15%     15.54MiB / 29.08GiB   0.05%     263kB / 694B      23.5MB / 22.9MB   5
11aba8ab78dd_jarvis-temporal-consciousness              0.15%     17.8MiB / 29.08GiB    0.06%     262kB / 662B      21.1MB / 18.2MB   5
llm15-proxy                                             0.26%     18.09MiB / 29.08GiB   0.06%     283kB / 16.2kB    26.6MB / 27.6MB   2
jarvis-blood-brain-barrier                              0.19%     23.79MiB / 29.08GiB   0.08%     483kB / 226kB     24.7MB / 22.9MB   2
msjarvis-rebuild-nbb_prefrontal_cortex-1                4.49%     51.5MiB / 29.08GiB    0.17%     300kB / 52kB      15.5MB / 1.3GB    34
jarvis-web-research                                     0.19%     15.01MiB / 29.08GiB   0.05%     332kB / 7.15kB    5.24MB / 22.4MB   1
msjarvis-rebuild-nbb_qualia_engine-1                    0.19%     17.28MiB / 29.08GiB   0.06%     389kB / 104kB     16.3MB / 16.6MB   2
jarvis-redis                                            0.99%     5.758MiB / 29.08GiB   0.02%     1.52MB / 607kB    11.9MB / 545kB    6
llm8-proxy                                              0.19%     17.77MiB / 29.08GiB   0.06%     275kB / 15.5kB    21.6MB / 25.4MB   2
llm2-proxy                                              0.20%     19.07MiB / 29.08GiB   0.06%     278kB / 16.6kB    20.1MB / 23.4MB   2

===== IOSTAT SNAPSHOT =====
2026-05-22 20:02:09
Linux 6.17.0-29-generic (cakidd-Legion-5-16IRX9) 	05/22/2026 	_x86_64_(32 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.40    0.00    0.89    0.09    0.00   95.61

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util
loop0            0.01      0.19     0.00   0.00    0.08    17.98    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop1            0.00      0.00     0.00   0.00    0.00     1.21    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop10           0.01      0.18     0.00   0.00    0.12    18.86    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop11           0.01      0.06     0.00   0.00    0.05     8.09    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop12           0.50      1.55     0.00   0.00    0.02     3.08    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop13           0.01      0.18     0.00   0.00    0.09    19.96    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop14           0.01      0.19     0.00   0.00    0.05    18.58    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop15           0.00      0.01     0.00   0.00    0.04     3.17    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop16           0.01      0.19     0.00   0.00    0.07    19.32    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop17           1.42     86.06     0.00   0.00    0.13    60.75    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.02
loop18           0.01      0.19     0.00   0.00    0.08    18.54    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop19           0.01      0.06     0.00   0.00    0.05     8.09    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop2            0.01      0.06     0.00   0.00    0.05     8.05    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop20           0.01      0.06     0.00   0.00    0.07     8.12    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop21           0.01      0.06     0.00   0.00    0.08     7.52    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop22           0.14      3.48     0.00   0.00    0.10    25.64    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop23           0.56     16.85     0.00   0.00    0.10    30.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.01
loop24           0.25     11.48     0.00   0.00    0.10    46.54    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop25           0.01      0.18     0.00   0.00    0.11    20.02    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop26           0.01      0.18     0.00   0.00    0.07    19.64    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop27           0.01      0.06     0.00   0.00    0.08     7.92    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop28           0.00      0.01     0.00   0.00    0.05     2.81    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop29           0.25     10.86     0.00   0.00    0.17    43.51    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop3            0.01      0.06     0.00   0.00    0.08     7.48    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop30           0.01      0.06     0.00   0.00    0.03     9.31    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop31           0.01      0.20     0.00   0.00    0.11    15.41    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop32           0.01      0.06     0.00   0.00    0.04     7.78    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop33           0.00      0.00     0.00   0.00    0.00     1.27    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop4            0.01      0.06     0.00   0.00    0.04     7.78    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop5            0.01      0.06     0.00   0.00    0.06     7.22    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop6            0.01      0.07     0.00   0.00    0.06     8.17    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop7            0.01      0.19     0.00   0.00    0.09    19.71    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop8            0.01      0.06     0.00   0.00    0.07     7.93    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop9            0.01      0.19     0.00   0.00    0.14    19.11    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
nvme0n1        185.98  10095.41    30.78  14.20    0.10    54.28   57.32   2164.65   329.30  85.17    5.00    37.76    0.00      0.00     0.00   0.00    0.00     0.00    2.60    1.32    0.31   2.21
nvme1n1         24.31    687.41     7.53  23.65    0.33    28.27   22.85   1772.64    11.75  33.96    4.96    77.56    0.00      0.00     0.00   0.00    0.00     0.00    2.45    0.48    0.12   0.61
sda              0.04      0.83     0.01  21.84    2.90    21.19    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.01


avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           4.75    0.00    2.88    0.09    0.00   92.28

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util
nvme0n1        312.00   2932.00    55.00  14.99    0.07     9.40    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.02   1.50
nvme1n1        364.00   5224.00    46.00  11.22    0.23    14.35    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.08   2.80



----
2026-05-22 20:02:11
Linux 6.17.0-29-generic (cakidd-Legion-5-16IRX9) 	05/22/2026 	_x86_64_(32 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.40    0.00    0.89    0.09    0.00   95.61

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util
loop0            0.01      0.19     0.00   0.00    0.08    17.98    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop1            0.00      0.00     0.00   0.00    0.00     1.21    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop10           0.01      0.18     0.00   0.00    0.12    18.86    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop11           0.01      0.06     0.00   0.00    0.05     8.09    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop12           0.50      1.55     0.00   0.00    0.02     3.08    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop13           0.01      0.18     0.00   0.00    0.09    19.96    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop14           0.01      0.19     0.00   0.00    0.05    18.58    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop15           0.00      0.01     0.00   0.00    0.04     3.17    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop16           0.01      0.19     0.00   0.00    0.07    19.32    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop17           1.42     86.03     0.00   0.00    0.13    60.75    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.02
loop18           0.01      0.19     0.00   0.00    0.08    18.54    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop19           0.01      0.06     0.00   0.00    0.05     8.09    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop2            0.01      0.06     0.00   0.00    0.05     8.05    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop20           0.01      0.06     0.00   0.00    0.07     8.12    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop21           0.01      0.06     0.00   0.00    0.08     7.52    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop22           0.14      3.48     0.00   0.00    0.10    25.64    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop23           0.56     16.84     0.00   0.00    0.10    30.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.01
loop24           0.25     11.47     0.00   0.00    0.10    46.54    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop25           0.01      0.18     0.00   0.00    0.11    20.02    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop26           0.01      0.18     0.00   0.00    0.07    19.64    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop27           0.01      0.06     0.00   0.00    0.08     7.92    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop28           0.00      0.01     0.00   0.00    0.05     2.81    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop29           0.25     10.85     0.00   0.00    0.17    43.51    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop3            0.01      0.06     0.00   0.00    0.08     7.48    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop30           0.01      0.06     0.00   0.00    0.03     9.31    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop31           0.01      0.20     0.00   0.00    0.11    15.41    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop32           0.01      0.06     0.00   0.00    0.04     7.78    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop33           0.00      0.00     0.00   0.00    0.00     1.27    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop4            0.01      0.06     0.00   0.00    0.04     7.78    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop5            0.01      0.06     0.00   0.00    0.06     7.22    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop6            0.01      0.07     0.00   0.00    0.06     8.17    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop7            0.01      0.19     0.00   0.00    0.09    19.71    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop8            0.01      0.06     0.00   0.00    0.07     7.93    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop9            0.01      0.19     0.00   0.00    0.14    19.11    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
nvme0n1        186.33  10094.01    30.81  14.19    0.10    54.17   57.30   2163.91   329.19  85.17    5.00    37.76    0.00      0.00     0.00   0.00    0.00     0.00    2.60    1.32    0.31   2.22
nvme1n1         24.45    689.21     7.54  23.58    0.33    28.19   22.85   1772.03    11.75  33.96    4.96    77.56    0.00      0.00     0.00   0.00    0.00     0.00    2.45    0.48    0.12   0.61
sda              0.04      0.83     0.01  21.84    2.90    21.19    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.01


avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           7.38    0.00    3.39    0.13    0.00   89.11

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util
nvme0n1        340.00   1792.00    21.00   5.82    0.11     5.27   16.00   1628.00     0.00   0.00    0.12   101.75    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.04   3.90
nvme1n1        358.00  26640.00   120.00  25.10    0.28    74.41    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.10   4.60



----
2026-05-22 20:02:13
Linux 6.17.0-29-generic (cakidd-Legion-5-16IRX9) 	05/22/2026 	_x86_64_(32 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.41    0.00    0.89    0.09    0.00   95.61

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util
loop0            0.01      0.19     0.00   0.00    0.08    17.98    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop1            0.00      0.00     0.00   0.00    0.00     1.21    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop10           0.01      0.18     0.00   0.00    0.12    18.86    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop11           0.01      0.06     0.00   0.00    0.05     8.09    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop12           0.50      1.55     0.00   0.00    0.02     3.08    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop13           0.01      0.18     0.00   0.00    0.09    19.96    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop14           0.01      0.19     0.00   0.00    0.05    18.58    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop15           0.00      0.01     0.00   0.00    0.04     3.17    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop16           0.01      0.19     0.00   0.00    0.07    19.32    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop17           1.42     86.00     0.00   0.00    0.13    60.75    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.02
loop18           0.01      0.19     0.00   0.00    0.08    18.54    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop19           0.01      0.06     0.00   0.00    0.05     8.09    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop2            0.01      0.06     0.00   0.00    0.05     8.05    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop20           0.01      0.06     0.00   0.00    0.07     8.12    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop21           0.01      0.06     0.00   0.00    0.08     7.52    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop22           0.14      3.48     0.00   0.00    0.10    25.64    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop23           0.56     16.84     0.00   0.00    0.10    30.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.01
loop24           0.25     11.47     0.00   0.00    0.10    46.54    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop25           0.01      0.18     0.00   0.00    0.11    20.02    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop26           0.01      0.18     0.00   0.00    0.07    19.64    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop27           0.01      0.06     0.00   0.00    0.08     7.92    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop28           0.00      0.01     0.00   0.00    0.05     2.81    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop29           0.25     10.85     0.00   0.00    0.17    43.51    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop3            0.01      0.06     0.00   0.00    0.08     7.48    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop30           0.01      0.06     0.00   0.00    0.03     9.31    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop31           0.01      0.20     0.00   0.00    0.11    15.41    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop32           0.01      0.06     0.00   0.00    0.04     7.78    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop33           0.00      0.00     0.00   0.00    0.00     1.27    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop4            0.01      0.06     0.00   0.00    0.04     7.78    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop5            0.01      0.06     0.00   0.00    0.06     7.22    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop6            0.01      0.07     0.00   0.00    0.06     8.17    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop7            0.01      0.19     0.00   0.00    0.09    19.71    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop8            0.01      0.06     0.00   0.00    0.07     7.93    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop9            0.01      0.19     0.00   0.00    0.14    19.11    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
nvme0n1        186.35  10091.02    30.82  14.19    0.10    54.15   57.29   2163.44   329.07  85.17    5.00    37.77    0.00      0.00     0.00   0.00    0.00     0.00    2.60    1.32    0.31   2.22
nvme1n1         24.63    707.99     7.57  23.51    0.33    28.74   22.84   1771.46    11.75  33.97    4.96    77.56    0.00      0.00     0.00   0.00    0.00     0.00    2.45    0.48    0.12   0.62
sda              0.04      0.83     0.01  21.84    2.90    21.19    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.01


avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           8.10    0.00    2.32    0.13    0.00   89.46

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util
nvme0n1        290.00   1412.00    24.00   7.64    0.13     4.87    5.00    428.00   102.00  95.33    1.40    85.60    0.00      0.00     0.00   0.00    0.00     0.00    1.00    2.00    0.05   3.40
nvme1n1        987.00 122884.00    97.00   8.95    0.25   124.50    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.25  13.60



----
2026-05-22 20:02:15
Linux 6.17.0-29-generic (cakidd-Legion-5-16IRX9) 	05/22/2026 	_x86_64_(32 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.41    0.00    0.89    0.09    0.00   95.61

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util
loop0            0.01      0.19     0.00   0.00    0.08    17.98    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop1            0.00      0.00     0.00   0.00    0.00     1.21    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop10           0.01      0.18     0.00   0.00    0.12    18.86    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop11           0.01      0.06     0.00   0.00    0.05     8.09    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop12           0.50      1.55     0.00   0.00    0.02     3.08    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop13           0.01      0.18     0.00   0.00    0.09    19.96    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop14           0.01      0.19     0.00   0.00    0.05    18.58    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop15           0.00      0.01     0.00   0.00    0.04     3.17    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop16           0.01      0.19     0.00   0.00    0.07    19.32    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop17           1.42     85.97     0.00   0.00    0.13    60.75    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.02
loop18           0.01      0.19     0.00   0.00    0.08    18.54    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop19           0.01      0.06     0.00   0.00    0.05     8.09    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop2            0.01      0.06     0.00   0.00    0.05     8.05    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop20           0.01      0.06     0.00   0.00    0.07     8.12    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop21           0.01      0.06     0.00   0.00    0.08     7.52    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop22           0.14      3.48     0.00   0.00    0.10    25.64    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop23           0.56     16.83     0.00   0.00    0.10    30.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.01
loop24           0.25     11.47     0.00   0.00    0.10    46.54    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop25           0.01      0.18     0.00   0.00    0.11    20.02    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop26           0.01      0.18     0.00   0.00    0.07    19.64    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop27           0.01      0.06     0.00   0.00    0.08     7.92    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop28           0.00      0.01     0.00   0.00    0.05     2.81    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop29           0.25     10.85     0.00   0.00    0.17    43.51    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop3            0.01      0.06     0.00   0.00    0.08     7.48    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop30           0.01      0.06     0.00   0.00    0.03     9.31    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop31           0.01      0.20     0.00   0.00    0.11    15.41    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop32           0.01      0.06     0.00   0.00    0.04     7.78    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop33           0.00      0.00     0.00   0.00    0.00     1.27    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop4            0.01      0.06     0.00   0.00    0.04     7.78    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop5            0.01      0.06     0.00   0.00    0.06     7.22    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop6            0.01      0.07     0.00   0.00    0.06     8.17    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop7            0.01      0.19     0.00   0.00    0.09    19.71    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop8            0.01      0.06     0.00   0.00    0.07     7.93    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop9            0.01      0.19     0.00   0.00    0.14    19.11    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
nvme0n1        186.37  10087.95    30.81  14.19    0.10    54.13   57.27   2162.77   328.98  85.17    5.00    37.77    0.00      0.00     0.00   0.00    0.00     0.00    2.60    1.32    0.31   2.22
nvme1n1         24.79    728.73     7.59  23.43    0.33    29.40   22.83   1770.84    11.75  33.97    4.96    77.56    0.00      0.00     0.00   0.00    0.00     0.00    2.45    0.48    0.12   0.62
sda              0.04      0.83     0.01  21.84    2.90    21.19    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.01


avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.22    0.00    0.88    0.06    0.00   95.84

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util
nvme0n1         32.00    176.00    12.00  27.27    0.66     5.50    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.02   2.00

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msallis-diag-20260522-200208$ cd /home/cakidd/msallis-diag-20260522-200208
bash docker-update-recommendations.sh
jarvis-unified-gateway
jarvis-brain-orchestrator
jarvis-ollama
jarvis-69dgm-bridge
jarvis-main-brain
jarvis-20llm-production
llm21-proxy
llm22-proxy
jarvis-wv-entangled-gateway
jarvis-psychology-services
jarvis-toroidal
jarvis-autonomous-learner
jarvis-rag-server
jarvis-aaacpe-rag
jarvis-gis-rag
jarvis-spiritual-rag
jarvis-hippocampus
jarvis-neurobiological-master
591cd058cd26_jarvis-consciousness-bridge
dd0340814f6d_jarvis-eeg-beta
a1f602068b45_jarvis-eeg-delta
llm7-proxy
llm11-proxy
llm17-proxy
llm3-proxy
12d6dc1b1e49_jarvis-chroma
llm19-proxy
jarvis-local-resources
jarvis-woah
11aba8ab78dd_jarvis-temporal-consciousness
llm15-proxy
jarvis-blood-brain-barrier
msjarvis-rebuild-nbb_prefrontal_cortex-1
jarvis-web-research
msjarvis-rebuild-nbb_qualia_engine-1
jarvis-redis
llm8-proxy
llm2-proxy
llm5-proxy
msjarvis-rebuild-nbb_darwin_godel_machines-1
msjarvis-rebuild-nbb_mother_carrie_protocols-1
llm20-proxy
llm10-proxy
llm1-proxy
llm9-proxy
llm4-proxy
jarvis-fractal-consciousness
llm13-proxy
jarvis-semaphore
jarvis-agents-service
llm14-proxy
llm6-proxy
llm12-proxy
llm18-proxy
llm16-proxy
jarvis-judge-pipeline
jarvis-judge-truth
jarvis-judge-ethics
jarvis-judge-consistency
jarvis-judge-alignment
jarvis-lm-synthesizer
msjarvis-rebuild-nbb_pituitary_gland-1
jarvis-eeg-theta
nbb-i-containers
jarvis-i-containers
msjarvis-rebuild-nbb_spiritual_maternal_integration-1
msjarvis-rebuild-nbb_heteroglobulin_transport-1
msjarvis-rebuild-nbb_spiritual_root-1
msjarvis-rebuild-nbb_blood_brain_barrier-1
msjarvis-rebuild-nbb_consciousness_containers-1
jarvis-hilbert-state
jarvis-mother-protocols
jarvis-swarm-intelligence
mysql
neo4j
ipfs
jarvis-session-sidecar
jarvis-constitutional-guardian
msjarvis-rebuild-nbb_woah_algorithms-1
jarvis-qualia-engine
jarvis-fifth-dgm
msjarvis-rebuild-nbb_subconscious-1
psychological_rag_domain
jarvis-local-resources-db
jarvis-gbim-temporal-indexer
jarvis-jaeger
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msallis-diag-20260522-200208$ grep -RniE 'finaliz|synthes|memory consolidation|capture every status|embedding|save_|persist|ledger|broadcast|poll' . | sed -n '1,300p'
./jarvis-lm-synthesizer.end.log:1:2026-05-19T03:57:54.791666574Z INFO:lm_synthesizer:Starting LM Synthesizer on 0.0.0.0:8001
./jarvis-lm-synthesizer.end.log:76:2026-05-22T22:25:11.815499916Z INFO:lm_synthesizer:Starting LM Synthesizer on 0.0.0.0:8001
./12d6dc1b1e49_jarvis-chroma.log:3:2026-05-19T03:59:34.041061144Z persist_path: "/data"
./12d6dc1b1e49_jarvis-chroma.log:31:2026-05-22T22:25:11.072470362Z persist_path: "/data"
./NEXT-STEPS.txt:7:7) Compare timestamps around Phase 4 / Finalizing answer against container CPU, memory, and Block I/O spikes.
./jarvis-web-research.end.log:321:2026-05-22T01:40:31.067292655Z INFO:primp:response: https://www.bing.com/search?q=capture+every+status+response+to+debug+polling 200
./jarvis-web-research.end.log:322:2026-05-22T01:40:31.182196406Z INFO:__main__:🔍 Search: 'capture every status response to debug polling' → 5 results
./jarvis-web-research.end.log:327:2026-05-22T03:16:43.216931338Z INFO:primp:response: https://www.bing.com/search?q=capture+every+status+response+to+debug+polling 200
./jarvis-web-research.end.log:328:2026-05-22T03:16:43.608909548Z INFO:__main__:🔍 Search: 'capture every status response to debug polling' → 0 results
./jarvis-web-research.end.log:334:2026-05-22T03:36:18.995834946Z INFO:primp:response: https://www.bing.com/search?q=fast+poll+test 200
./jarvis-web-research.end.log:335:2026-05-22T03:36:19.049901472Z INFO:__main__:🔍 Search: 'fast poll test' → 5 results
./jarvis-web-research.end.log:340:2026-05-22T12:25:08.048205087Z INFO:primp:response: https://www.bing.com/search?q=patch+verification+-+does+assistant+response+persist+now 200
./jarvis-web-research.end.log:341:2026-05-22T12:25:08.101936984Z INFO:__main__:🔍 Search: 'patch verification - does assistant response persist now' → 0 results
./jarvis-web-research.end.log:346:2026-05-22T12:34:07.828926436Z INFO:primp:response: https://www.bing.com/search?q=patch+verification+-+does+assistant+response+persist+now 200
./jarvis-web-research.end.log:347:2026-05-22T12:34:07.974057233Z INFO:__main__:🔍 Search: 'patch verification - does assistant response persist now' → 5 results
./jarvis-web-research.end.log:372:2026-05-22T19:20:09.784029541Z INFO:primp:response: https://www.bing.com/search?q=ping+after+persist+move 200
./jarvis-web-research.end.log:373:2026-05-22T19:20:09.929174574Z INFO:__main__:🔍 Search: 'ping after persist move' → 0 results
./jarvis-web-research.end.log:402:2026-05-22T21:14:23.641553467Z INFO:primp:response: https://www.bing.com/search?q=assistant+persistence+final+proof 200
./jarvis-web-research.end.log:403:2026-05-22T21:14:23.743586499Z INFO:__main__:🔍 Search: 'assistant persistence final proof' → 0 results
./docker-ps.txt:62:jarvis-lm-synthesizer                                   msjarvis-rebuild-jarvis-lm-synthesizer                Up 2 hours                      8001/tcp
./jarvis-local-resources-db.log:111166:2026-05-17T01:34:13.254961649Z 	  ('wvgistc_air_nonattainment_wvdep_200802_utm83',      'WVDEP',            '2008-02-01', 'POLYGON', 4326, (SELECT COUNT(*) FROM wvgistc_air_nonattainment_wvdep_200802_utm83),      'WV air pollution non-attainment areas, WVDEP 2008, UTM17N→WGS84', NOW()),
./jarvis-local-resources-db.log:112808:2026-05-17T01:45:19.261039704Z 	"user_poll_" varchar(100),
./jarvis-local-resources-db.log:112809:2026-05-17T01:45:19.261040654Z 	"user_poll1" varchar(20),
./jarvis-local-resources-db.log:114264:2026-05-20T00:44:08.720324522Z 	      UPDATE mountainshares_ledger SET amount = <YOUR_AMOUNT> WHERE ueid = 'fc238378-14f5-4a10-9865-ae241ea2ef74' AND transaction_type = 'founding_grant';
./jarvis-local-resources-db.log:114296:2026-05-20T01:57:06.018920829Z 2026-05-20 01:57:06.018 UTC [37691] ERROR:  relation "ledger_entries" does not exist at character 15
./jarvis-local-resources-db.log:114297:2026-05-20T01:57:06.018951677Z 2026-05-20 01:57:06.018 UTC [37691] STATEMENT:  SELECT * FROM ledger_entries ORDER BY created_at LIMIT 5;
./jarvis-local-resources-db.log:114341:2026-05-22T14:24:50.404642486Z 	      WHERE session_id='persist-verify'
./jarvis-local-resources-db.log:114353:2026-05-22T15:19:10.487046126Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
./jarvis-local-resources-db.log:114361:2026-05-22T15:24:51.796790724Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
./jarvis-local-resources-db.log:114368:2026-05-22T15:27:26.338476293Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
./jarvis-lm-synthesizer.inspect.json:7:            "lm_synthesizer.py"
./jarvis-lm-synthesizer.inspect.json:27:        "Name": "/jarvis-lm-synthesizer",
./jarvis-lm-synthesizer.inspect.json:200:                "lm_synthesizer.py"
./jarvis-lm-synthesizer.inspect.json:202:            "Image": "msjarvis-rebuild-jarvis-lm-synthesizer",
./jarvis-lm-synthesizer.inspect.json:215:                "com.docker.compose.replace": "jarvis-lm-synthesizer",
./jarvis-lm-synthesizer.inspect.json:216:                "com.docker.compose.service": "jarvis-lm-synthesizer",
./jarvis-lm-synthesizer.inspect.json:231:                        "jarvis-lm-synthesizer",
./jarvis-lm-synthesizer.inspect.json:232:                        "jarvis-lm-synthesizer"
./jarvis-lm-synthesizer.inspect.json:246:                        "jarvis-lm-synthesizer",
./jarvis-main-brain.end.log:32:2026-05-22T20:27:56.253064826Z 2026-05-22 20:27:56,252 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./jarvis-main-brain.end.log:57:2026-05-22T20:32:26.411693339Z 2026-05-22 20:32:26,411 INFO jarvis-main-brain - assistant-response-persisted
./jarvis-main-brain.end.log:97:2026-05-22T21:09:25.409053119Z 2026-05-22 21:09:25,408 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./jarvis-main-brain.end.log:142:2026-05-22T21:13:39.564261633Z 2026-05-22 21:13:39,563 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./jarvis-main-brain.end.log:167:2026-05-22T21:14:34.798964227Z 2026-05-22 21:14:34,798 INFO jarvis-main-brain - assistant-response-persisted
./jarvis-main-brain.end.log:182:2026-05-22T21:22:24.096716186Z 2026-05-22 21:22:24,096 INFO jarvis-main-brain - assistant-response-persisted
./jarvis-main-brain.end.log:219:2026-05-22T23:52:47.381962344Z 2026-05-22 23:52:47,381 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./jarvis-main-brain.end.log:247:2026-05-22T23:57:53.208903422Z 2026-05-22 23:57:53,208 INFO jarvis-main-brain - assistant-response-persisted
./jarvis-main-brain.end.log:285:2026-05-23T00:02:47.665388807Z 2026-05-23 00:02:47,665 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./docker-update-recommendations.sh:62:docker update --cpus 2 --memory 6g --memory-swap 6g jarvis-lm-synthesizer
./jarvis-main-brain.inspect.json:253:                "ISPERSISTENT=TRUE",
./jarvis-main-brain.inspect.json:271:                "PERSIST_DIRECTORY=/data",
./jarvis-main-brain.inspect.json:357:                "ESCALATION_POLL_INTERVAL=60",
./jarvis-main-brain.log:32:2026-05-22T20:27:56.253064826Z 2026-05-22 20:27:56,252 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./jarvis-main-brain.log:57:2026-05-22T20:32:26.411693339Z 2026-05-22 20:32:26,411 INFO jarvis-main-brain - assistant-response-persisted
./jarvis-main-brain.log:97:2026-05-22T21:09:25.409053119Z 2026-05-22 21:09:25,408 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./jarvis-main-brain.log:142:2026-05-22T21:13:39.564261633Z 2026-05-22 21:13:39,563 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./jarvis-main-brain.log:167:2026-05-22T21:14:34.798964227Z 2026-05-22 21:14:34,798 INFO jarvis-main-brain - assistant-response-persisted
./jarvis-main-brain.log:182:2026-05-22T21:22:24.096716186Z 2026-05-22 21:22:24,096 INFO jarvis-main-brain - assistant-response-persisted
./jarvis-main-brain.log:219:2026-05-22T23:52:47.381962344Z 2026-05-22 23:52:47,381 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./jarvis-main-brain.log:247:2026-05-22T23:57:53.208903422Z 2026-05-22 23:57:53,208 INFO jarvis-main-brain - assistant-response-persisted
./docker-compose-ps.txt:27:jarvis-lm-synthesizer                                   msjarvis-rebuild-jarvis-lm-synthesizer                "python lm_synthesiz…"   jarvis-lm-synthesizer                3 days ago          Up 2 hours                      8001/tcp
./jarvis-20llm-production.end.log:3:2026-05-19T18:04:02.798508625Z INFO:__main__:   • Gemma -> model=gemma:2b endpoint=http://llm2-proxy:8202/generate weight=0.8 specialty=Synthesis active=True
./jarvis-20llm-production.end.log:2512:2026-05-22T22:25:10.718572044Z INFO:__main__:   • Gemma -> model=gemma:2b endpoint=http://llm2-proxy:8202/generate weight=0.8 specialty=Synthesis active=True
./12d6dc1b1e49_jarvis-chroma.inspect.json:246:                "ISPERSISTENT=TRUE",
./12d6dc1b1e49_jarvis-chroma.inspect.json:249:                "PERSIST_DIRECTORY=/data",
./jarvis-local-resources-db.end.log:111166:2026-05-17T01:34:13.254961649Z 	  ('wvgistc_air_nonattainment_wvdep_200802_utm83',      'WVDEP',            '2008-02-01', 'POLYGON', 4326, (SELECT COUNT(*) FROM wvgistc_air_nonattainment_wvdep_200802_utm83),      'WV air pollution non-attainment areas, WVDEP 2008, UTM17N→WGS84', NOW()),
./jarvis-local-resources-db.end.log:112808:2026-05-17T01:45:19.261039704Z 	"user_poll_" varchar(100),
./jarvis-local-resources-db.end.log:112809:2026-05-17T01:45:19.261040654Z 	"user_poll1" varchar(20),
./jarvis-local-resources-db.end.log:114264:2026-05-20T00:44:08.720324522Z 	      UPDATE mountainshares_ledger SET amount = <YOUR_AMOUNT> WHERE ueid = 'fc238378-14f5-4a10-9865-ae241ea2ef74' AND transaction_type = 'founding_grant';
./jarvis-local-resources-db.end.log:114296:2026-05-20T01:57:06.018920829Z 2026-05-20 01:57:06.018 UTC [37691] ERROR:  relation "ledger_entries" does not exist at character 15
./jarvis-local-resources-db.end.log:114297:2026-05-20T01:57:06.018951677Z 2026-05-20 01:57:06.018 UTC [37691] STATEMENT:  SELECT * FROM ledger_entries ORDER BY created_at LIMIT 5;
./jarvis-local-resources-db.end.log:114341:2026-05-22T14:24:50.404642486Z 	      WHERE session_id='persist-verify'
./jarvis-local-resources-db.end.log:114353:2026-05-22T15:19:10.487046126Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
./jarvis-local-resources-db.end.log:114361:2026-05-22T15:24:51.796790724Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
./jarvis-local-resources-db.end.log:114368:2026-05-22T15:27:26.338476293Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
./jarvis-unified-gateway.inspect.json:306:                "com.docker.compose.depends_on": "psychological_rag_domain:service_started:false,nbb_spiritual_maternal_integration:service_started:false,nbb_woah_algorithms:service_started:false,nbb-i-containers:service_started:false,nbb_subconscious:service_started:false,jarvis-toroidal:service_started:false,jarvis-fifth-dgm:service_started:false,jarvis-lm-synthesizer:service_started:false,nbb_spiritual_root:service_started:false,jarvis-ollama:service_started:false,jarvis-constitutional-guardian:service_started:false,jarvis-woah:service_started:false,jarvis-brain-orchestrator:service_started:false,jarvis-chroma:service_started:false,jarvis-qualia-engine:service_started:false,jarvis-neurobiological-master:service_started:false,nbb_prefrontal_cortex:service_started:false,jarvis-psychology-services:service_started:false,jarvis-fractal-consciousness:service_started:false,nbb_consciousness_containers:service_started:false,jarvis-consciousness-bridge:service_started:false,jarvis-20llm-production:service_started:false,nbb_mother_carrie_protocols:service_started:false,jarvis-blood-brain-barrier:service_started:false,nbb_heteroglobulin_transport:service_started:false,jarvis-redis:service_started:false,jarvis-i-containers:service_started:false,nbb_pituitary_gland:service_started:false",
./jarvis-20llm-production.log:3:2026-05-19T18:04:02.798508625Z INFO:__main__:   • Gemma -> model=gemma:2b endpoint=http://llm2-proxy:8202/generate weight=0.8 specialty=Synthesis active=True
./jarvis-20llm-production.log:2512:2026-05-22T22:25:10.718572044Z INFO:__main__:   • Gemma -> model=gemma:2b endpoint=http://llm2-proxy:8202/generate weight=0.8 specialty=Synthesis active=True
./12d6dc1b1e49_jarvis-chroma.end.log:3:2026-05-19T03:59:34.041061144Z persist_path: "/data"
./12d6dc1b1e49_jarvis-chroma.end.log:31:2026-05-22T22:25:11.072470362Z persist_path: "/data"
./slow-path-grep.txt:1:/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.end.log:1:2026-05-19T03:57:54.791666574Z INFO:lm_synthesizer:Starting LM Synthesizer on 0.0.0.0:8001
./slow-path-grep.txt:2:/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.end.log:76:2026-05-22T22:25:11.815499916Z INFO:lm_synthesizer:Starting LM Synthesizer on 0.0.0.0:8001
./slow-path-grep.txt:3:/home/cakidd/msallis-diag-20260522-200208/12d6dc1b1e49_jarvis-chroma.log:3:2026-05-19T03:59:34.041061144Z persist_path: "/data"
./slow-path-grep.txt:4:/home/cakidd/msallis-diag-20260522-200208/12d6dc1b1e49_jarvis-chroma.log:31:2026-05-22T22:25:11.072470362Z persist_path: "/data"
./slow-path-grep.txt:5:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:321:2026-05-22T01:40:31.067292655Z INFO:primp:response: https://www.bing.com/search?q=capture+every+status+response+to+debug+polling 200
./slow-path-grep.txt:6:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:322:2026-05-22T01:40:31.182196406Z INFO:__main__:🔍 Search: 'capture every status response to debug polling' → 5 results
./slow-path-grep.txt:7:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:327:2026-05-22T03:16:43.216931338Z INFO:primp:response: https://www.bing.com/search?q=capture+every+status+response+to+debug+polling 200
./slow-path-grep.txt:8:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:328:2026-05-22T03:16:43.608909548Z INFO:__main__:🔍 Search: 'capture every status response to debug polling' → 0 results
./slow-path-grep.txt:9:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:334:2026-05-22T03:36:18.995834946Z INFO:primp:response: https://www.bing.com/search?q=fast+poll+test 200
./slow-path-grep.txt:10:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:335:2026-05-22T03:36:19.049901472Z INFO:__main__:🔍 Search: 'fast poll test' → 5 results
./slow-path-grep.txt:11:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:340:2026-05-22T12:25:08.048205087Z INFO:primp:response: https://www.bing.com/search?q=patch+verification+-+does+assistant+response+persist+now 200
./slow-path-grep.txt:12:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:341:2026-05-22T12:25:08.101936984Z INFO:__main__:🔍 Search: 'patch verification - does assistant response persist now' → 0 results
./slow-path-grep.txt:13:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:346:2026-05-22T12:34:07.828926436Z INFO:primp:response: https://www.bing.com/search?q=patch+verification+-+does+assistant+response+persist+now 200
./slow-path-grep.txt:14:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:347:2026-05-22T12:34:07.974057233Z INFO:__main__:🔍 Search: 'patch verification - does assistant response persist now' → 5 results
./slow-path-grep.txt:15:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:372:2026-05-22T19:20:09.784029541Z INFO:primp:response: https://www.bing.com/search?q=ping+after+persist+move 200
./slow-path-grep.txt:16:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:373:2026-05-22T19:20:09.929174574Z INFO:__main__:🔍 Search: 'ping after persist move' → 0 results
./slow-path-grep.txt:17:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:402:2026-05-22T21:14:23.641553467Z INFO:primp:response: https://www.bing.com/search?q=assistant+persistence+final+proof 200
./slow-path-grep.txt:18:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.end.log:403:2026-05-22T21:14:23.743586499Z INFO:__main__:🔍 Search: 'assistant persistence final proof' → 0 results
./slow-path-grep.txt:19:/home/cakidd/msallis-diag-20260522-200208/docker-ps.txt:62:jarvis-lm-synthesizer                                   msjarvis-rebuild-jarvis-lm-synthesizer                Up 2 hours                      8001/tcp
./slow-path-grep.txt:20:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:111166:2026-05-17T01:34:13.254961649Z 	  ('wvgistc_air_nonattainment_wvdep_200802_utm83',      'WVDEP',            '2008-02-01', 'POLYGON', 4326, (SELECT COUNT(*) FROM wvgistc_air_nonattainment_wvdep_200802_utm83),      'WV air pollution non-attainment areas, WVDEP 2008, UTM17N→WGS84', NOW()),
./slow-path-grep.txt:21:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:112808:2026-05-17T01:45:19.261039704Z 	"user_poll_" varchar(100),
./slow-path-grep.txt:22:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:112809:2026-05-17T01:45:19.261040654Z 	"user_poll1" varchar(20),
./slow-path-grep.txt:23:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:114264:2026-05-20T00:44:08.720324522Z 	      UPDATE mountainshares_ledger SET amount = <YOUR_AMOUNT> WHERE ueid = 'fc238378-14f5-4a10-9865-ae241ea2ef74' AND transaction_type = 'founding_grant';
./slow-path-grep.txt:24:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:114296:2026-05-20T01:57:06.018920829Z 2026-05-20 01:57:06.018 UTC [37691] ERROR:  relation "ledger_entries" does not exist at character 15
./slow-path-grep.txt:25:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:114297:2026-05-20T01:57:06.018951677Z 2026-05-20 01:57:06.018 UTC [37691] STATEMENT:  SELECT * FROM ledger_entries ORDER BY created_at LIMIT 5;
./slow-path-grep.txt:26:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:114341:2026-05-22T14:24:50.404642486Z 	      WHERE session_id='persist-verify'
./slow-path-grep.txt:27:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:114353:2026-05-22T15:19:10.487046126Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
./slow-path-grep.txt:28:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:114361:2026-05-22T15:24:51.796790724Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
./slow-path-grep.txt:29:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.log:114368:2026-05-22T15:27:26.338476293Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
./slow-path-grep.txt:30:/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:7:            "lm_synthesizer.py"
./slow-path-grep.txt:31:/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:27:        "Name": "/jarvis-lm-synthesizer",
./slow-path-grep.txt:32:/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:200:                "lm_synthesizer.py"
./slow-path-grep.txt:33:/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:202:            "Image": "msjarvis-rebuild-jarvis-lm-synthesizer",
./slow-path-grep.txt:34:/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:215:                "com.docker.compose.replace": "jarvis-lm-synthesizer",
./slow-path-grep.txt:35:/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:216:                "com.docker.compose.service": "jarvis-lm-synthesizer",
./slow-path-grep.txt:36:/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:231:                        "jarvis-lm-synthesizer",
./slow-path-grep.txt:37:/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:232:                        "jarvis-lm-synthesizer"
./slow-path-grep.txt:38:/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.inspect.json:246:                        "jarvis-lm-synthesizer",
./slow-path-grep.txt:39:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:32:2026-05-22T20:27:56.253064826Z 2026-05-22 20:27:56,252 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./slow-path-grep.txt:40:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:57:2026-05-22T20:32:26.411693339Z 2026-05-22 20:32:26,411 INFO jarvis-main-brain - assistant-response-persisted
./slow-path-grep.txt:41:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:97:2026-05-22T21:09:25.409053119Z 2026-05-22 21:09:25,408 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./slow-path-grep.txt:42:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:142:2026-05-22T21:13:39.564261633Z 2026-05-22 21:13:39,563 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./slow-path-grep.txt:43:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:167:2026-05-22T21:14:34.798964227Z 2026-05-22 21:14:34,798 INFO jarvis-main-brain - assistant-response-persisted
./slow-path-grep.txt:44:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:182:2026-05-22T21:22:24.096716186Z 2026-05-22 21:22:24,096 INFO jarvis-main-brain - assistant-response-persisted
./slow-path-grep.txt:45:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:219:2026-05-22T23:52:47.381962344Z 2026-05-22 23:52:47,381 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./slow-path-grep.txt:46:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:247:2026-05-22T23:57:53.208903422Z 2026-05-22 23:57:53,208 INFO jarvis-main-brain - assistant-response-persisted
./slow-path-grep.txt:47:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.end.log:285:2026-05-23T00:02:47.665388807Z 2026-05-23 00:02:47,665 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./slow-path-grep.txt:48:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.inspect.json:253:                "ISPERSISTENT=TRUE",
./slow-path-grep.txt:49:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.inspect.json:271:                "PERSIST_DIRECTORY=/data",
./slow-path-grep.txt:50:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.inspect.json:357:                "ESCALATION_POLL_INTERVAL=60",
./slow-path-grep.txt:51:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:32:2026-05-22T20:27:56.253064826Z 2026-05-22 20:27:56,252 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./slow-path-grep.txt:52:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:57:2026-05-22T20:32:26.411693339Z 2026-05-22 20:32:26,411 INFO jarvis-main-brain - assistant-response-persisted
./slow-path-grep.txt:53:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:97:2026-05-22T21:09:25.409053119Z 2026-05-22 21:09:25,408 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./slow-path-grep.txt:54:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:142:2026-05-22T21:13:39.564261633Z 2026-05-22 21:13:39,563 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./slow-path-grep.txt:55:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:167:2026-05-22T21:14:34.798964227Z 2026-05-22 21:14:34,798 INFO jarvis-main-brain - assistant-response-persisted
./slow-path-grep.txt:56:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:182:2026-05-22T21:22:24.096716186Z 2026-05-22 21:22:24,096 INFO jarvis-main-brain - assistant-response-persisted
./slow-path-grep.txt:57:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:219:2026-05-22T23:52:47.381962344Z 2026-05-22 23:52:47,381 INFO httpx - HTTP Request: GET http://jarvis-lm-synthesizer:8001/health "HTTP/1.1 200 OK"
./slow-path-grep.txt:58:/home/cakidd/msallis-diag-20260522-200208/jarvis-main-brain.log:247:2026-05-22T23:57:53.208903422Z 2026-05-22 23:57:53,208 INFO jarvis-main-brain - assistant-response-persisted
./slow-path-grep.txt:59:/home/cakidd/msallis-diag-20260522-200208/docker-compose-ps.txt:27:jarvis-lm-synthesizer                                   msjarvis-rebuild-jarvis-lm-synthesizer                "python lm_synthesiz…"   jarvis-lm-synthesizer                3 days ago          Up 2 hours                      8001/tcp
./slow-path-grep.txt:60:/home/cakidd/msallis-diag-20260522-200208/jarvis-20llm-production.end.log:3:2026-05-19T18:04:02.798508625Z INFO:__main__:   • Gemma -> model=gemma:2b endpoint=http://llm2-proxy:8202/generate weight=0.8 specialty=Synthesis active=True
./slow-path-grep.txt:61:/home/cakidd/msallis-diag-20260522-200208/jarvis-20llm-production.end.log:2512:2026-05-22T22:25:10.718572044Z INFO:__main__:   • Gemma -> model=gemma:2b endpoint=http://llm2-proxy:8202/generate weight=0.8 specialty=Synthesis active=True
./slow-path-grep.txt:62:/home/cakidd/msallis-diag-20260522-200208/12d6dc1b1e49_jarvis-chroma.inspect.json:246:                "ISPERSISTENT=TRUE",
./slow-path-grep.txt:63:/home/cakidd/msallis-diag-20260522-200208/12d6dc1b1e49_jarvis-chroma.inspect.json:249:                "PERSIST_DIRECTORY=/data",
./slow-path-grep.txt:64:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:111166:2026-05-17T01:34:13.254961649Z 	  ('wvgistc_air_nonattainment_wvdep_200802_utm83',      'WVDEP',            '2008-02-01', 'POLYGON', 4326, (SELECT COUNT(*) FROM wvgistc_air_nonattainment_wvdep_200802_utm83),      'WV air pollution non-attainment areas, WVDEP 2008, UTM17N→WGS84', NOW()),
./slow-path-grep.txt:65:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:112808:2026-05-17T01:45:19.261039704Z 	"user_poll_" varchar(100),
./slow-path-grep.txt:66:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:112809:2026-05-17T01:45:19.261040654Z 	"user_poll1" varchar(20),
./slow-path-grep.txt:67:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:114264:2026-05-20T00:44:08.720324522Z 	      UPDATE mountainshares_ledger SET amount = <YOUR_AMOUNT> WHERE ueid = 'fc238378-14f5-4a10-9865-ae241ea2ef74' AND transaction_type = 'founding_grant';
./slow-path-grep.txt:68:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:114296:2026-05-20T01:57:06.018920829Z 2026-05-20 01:57:06.018 UTC [37691] ERROR:  relation "ledger_entries" does not exist at character 15
./slow-path-grep.txt:69:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:114297:2026-05-20T01:57:06.018951677Z 2026-05-20 01:57:06.018 UTC [37691] STATEMENT:  SELECT * FROM ledger_entries ORDER BY created_at LIMIT 5;
./slow-path-grep.txt:70:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:114341:2026-05-22T14:24:50.404642486Z 	      WHERE session_id='persist-verify'
./slow-path-grep.txt:71:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:114353:2026-05-22T15:19:10.487046126Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
./slow-path-grep.txt:72:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:114361:2026-05-22T15:24:51.796790724Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
./slow-path-grep.txt:73:/home/cakidd/msallis-diag-20260522-200208/jarvis-local-resources-db.end.log:114368:2026-05-22T15:27:26.338476293Z 	WHERE session_id IN ('persist-verify-direct', 'persist-verify')
./slow-path-grep.txt:74:/home/cakidd/msallis-diag-20260522-200208/jarvis-unified-gateway.inspect.json:306:                "com.docker.compose.depends_on": "psychological_rag_domain:service_started:false,nbb_spiritual_maternal_integration:service_started:false,nbb_woah_algorithms:service_started:false,nbb-i-containers:service_started:false,nbb_subconscious:service_started:false,jarvis-toroidal:service_started:false,jarvis-fifth-dgm:service_started:false,jarvis-lm-synthesizer:service_started:false,nbb_spiritual_root:service_started:false,jarvis-ollama:service_started:false,jarvis-constitutional-guardian:service_started:false,jarvis-woah:service_started:false,jarvis-brain-orchestrator:service_started:false,jarvis-chroma:service_started:false,jarvis-qualia-engine:service_started:false,jarvis-neurobiological-master:service_started:false,nbb_prefrontal_cortex:service_started:false,jarvis-psychology-services:service_started:false,jarvis-fractal-consciousness:service_started:false,nbb_consciousness_containers:service_started:false,jarvis-consciousness-bridge:service_started:false,jarvis-20llm-production:service_started:false,nbb_mother_carrie_protocols:service_started:false,jarvis-blood-brain-barrier:service_started:false,nbb_heteroglobulin_transport:service_started:false,jarvis-redis:service_started:false,jarvis-i-containers:service_started:false,nbb_pituitary_gland:service_started:false",
./slow-path-grep.txt:75:/home/cakidd/msallis-diag-20260522-200208/jarvis-20llm-production.log:3:2026-05-19T18:04:02.798508625Z INFO:__main__:   • Gemma -> model=gemma:2b endpoint=http://llm2-proxy:8202/generate weight=0.8 specialty=Synthesis active=True
./slow-path-grep.txt:76:/home/cakidd/msallis-diag-20260522-200208/jarvis-20llm-production.log:2512:2026-05-22T22:25:10.718572044Z INFO:__main__:   • Gemma -> model=gemma:2b endpoint=http://llm2-proxy:8202/generate weight=0.8 specialty=Synthesis active=True
./slow-path-grep.txt:77:/home/cakidd/msallis-diag-20260522-200208/12d6dc1b1e49_jarvis-chroma.end.log:3:2026-05-19T03:59:34.041061144Z persist_path: "/data"
./slow-path-grep.txt:78:/home/cakidd/msallis-diag-20260522-200208/12d6dc1b1e49_jarvis-chroma.end.log:31:2026-05-22T22:25:11.072470362Z persist_path: "/data"
./slow-path-grep.txt:80:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:168:2026-05-22T23:52:52.686012145Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 3200
./slow-path-grep.txt:81:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:249:2026-05-22T23:52:53.236862897Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 3200
./slow-path-grep.txt:82:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:361:2026-05-22T23:53:13.149684929Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
./slow-path-grep.txt:83:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:445:2026-05-22T23:53:17.557183580Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
./slow-path-grep.txt:84:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:562:2026-05-22T23:53:37.241514389Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:85:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:666:2026-05-22T23:53:47.330645735Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:86:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1195:2026-05-22T23:54:15.806807252Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:87:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1276:2026-05-22T23:54:18.978274494Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:88:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1388:2026-05-22T23:54:29.660032960Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:89:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1492:2026-05-22T23:54:41.631149448Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:90:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1609:2026-05-22T23:54:51.781936135Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:91:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1694:2026-05-22T23:54:53.397496085Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:92:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1811:2026-05-22T23:54:56.256453904Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:93:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:1912:2026-05-22T23:55:10.347849077Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:94:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2025:2026-05-22T23:55:14.009307673Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:95:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2132:2026-05-22T23:55:21.236845252Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:96:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2251:2026-05-22T23:55:31.996226417Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:97:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2354:2026-05-22T23:55:48.851239652Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:98:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2468:2026-05-22T23:55:51.719707737Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
./slow-path-grep.txt:99:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2584:2026-05-22T23:56:04.845748307Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
./slow-path-grep.txt:100:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2715:2026-05-22T23:56:06.198228820Z llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:101:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2802:2026-05-22T23:56:08.299697925Z llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:102:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:2929:2026-05-22T23:56:11.142780529Z llama_model_loader: - kv  12:                      phi3.embedding_length u32              = 3072
./slow-path-grep.txt:103:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3049:2026-05-22T23:56:27.687706746Z llama_model_loader: - kv  12:                      phi3.embedding_length u32              = 3072
./slow-path-grep.txt:104:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3174:2026-05-22T23:56:42.864626949Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:105:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3260:2026-05-22T23:56:49.300142341Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:106:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3377:2026-05-22T23:56:52.158691523Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:107:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3477:2026-05-22T23:57:04.289921868Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:108:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3589:2026-05-22T23:57:11.748896533Z llama_model_loader: - kv   4:                starcoder2.embedding_length u32              = 3072
./slow-path-grep.txt:109:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3694:2026-05-22T23:57:24.742290551Z llama_model_loader: - kv   4:                starcoder2.embedding_length u32              = 3072
./slow-path-grep.txt:110:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3811:2026-05-22T23:57:26.095016910Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:111:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:3913:2026-05-22T23:57:32.620899339Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:112:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:4029:2026-05-22T23:57:40.859081243Z llama_model_loader: - kv   3:                      phi2.embedding_length u32              = 2560
./slow-path-grep.txt:113:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:4142:2026-05-23T00:02:50.741324046Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:114:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:4220:2026-05-23T00:02:50.903360061Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:115:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:4750:2026-05-23T00:02:54.256367952Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:116:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:4837:2026-05-23T00:03:00.142655315Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:117:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:4958:2026-05-23T00:03:11.203997380Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:118:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5058:2026-05-23T00:03:31.984325844Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:119:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5170:2026-05-23T00:03:39.650279766Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:120:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5269:2026-05-23T00:04:05.242015099Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:121:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5381:2026-05-23T00:04:11.641280899Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
./slow-path-grep.txt:122:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5497:2026-05-23T00:04:28.142344533Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
./slow-path-grep.txt:123:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5636:2026-05-23T00:04:29.495405178Z llama_model_loader: - kv  12:                      phi3.embedding_length u32              = 3072
./slow-path-grep.txt:124:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5736:2026-05-23T00:04:31.527847575Z llama_model_loader: - kv  12:                      phi3.embedding_length u32              = 3072
./slow-path-grep.txt:125:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5861:2026-05-23T00:04:35.648445887Z llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:126:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:5950:2026-05-23T00:04:47.301717370Z llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:127:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:6068:2026-05-23T00:04:50.154647811Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:128:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:6169:2026-05-23T00:05:06.840391051Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:129:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:6282:2026-05-23T00:05:10.615082950Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:130:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:6387:2026-05-23T00:05:18.103365438Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:131:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.end.log:6504:2026-05-23T00:05:21.506464796Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:132:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:39:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:133:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:138:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:134:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:169:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:135:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:207:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:136:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:251:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:137:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:290:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:138:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:291:      PERSIST_DIRECTORY: /data
./slow-path-grep.txt:139:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:322:        source: /home/ms-jarvis/msjarvis-rebuild/persistent/chroma
./slow-path-grep.txt:140:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:339:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:141:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:388:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:142:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:420:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:143:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:511:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:144:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:703:  jarvis-lm-synthesizer:
./slow-path-grep.txt:145:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:706:      dockerfile: Dockerfile.lm_synthesizer
./slow-path-grep.txt:146:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:709:      - lm_synthesizer.py
./slow-path-grep.txt:147:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:710:    container_name: jarvis-lm-synthesizer
./slow-path-grep.txt:148:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:716:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:149:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:814:      jarvis-lm-synthesizer:
./slow-path-grep.txt:150:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:880:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:151:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1010:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:152:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1038:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:153:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1079:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:154:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1232:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:155:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1287:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:156:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1321:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:157:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1350:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:158:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1768:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:159:/home/cakidd/msallis-diag-20260522-200208/docker-compose-config.txt:1987:      IS_PERSISTENT: "TRUE"
./slow-path-grep.txt:160:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:321:2026-05-22T01:40:31.067292655Z INFO:primp:response: https://www.bing.com/search?q=capture+every+status+response+to+debug+polling 200
./slow-path-grep.txt:161:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:322:2026-05-22T01:40:31.182196406Z INFO:__main__:🔍 Search: 'capture every status response to debug polling' → 5 results
./slow-path-grep.txt:162:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:327:2026-05-22T03:16:43.216931338Z INFO:primp:response: https://www.bing.com/search?q=capture+every+status+response+to+debug+polling 200
./slow-path-grep.txt:163:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:328:2026-05-22T03:16:43.608909548Z INFO:__main__:🔍 Search: 'capture every status response to debug polling' → 0 results
./slow-path-grep.txt:164:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:334:2026-05-22T03:36:18.995834946Z INFO:primp:response: https://www.bing.com/search?q=fast+poll+test 200
./slow-path-grep.txt:165:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:335:2026-05-22T03:36:19.049901472Z INFO:__main__:🔍 Search: 'fast poll test' → 5 results
./slow-path-grep.txt:166:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:340:2026-05-22T12:25:08.048205087Z INFO:primp:response: https://www.bing.com/search?q=patch+verification+-+does+assistant+response+persist+now 200
./slow-path-grep.txt:167:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:341:2026-05-22T12:25:08.101936984Z INFO:__main__:🔍 Search: 'patch verification - does assistant response persist now' → 0 results
./slow-path-grep.txt:168:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:346:2026-05-22T12:34:07.828926436Z INFO:primp:response: https://www.bing.com/search?q=patch+verification+-+does+assistant+response+persist+now 200
./slow-path-grep.txt:169:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:347:2026-05-22T12:34:07.974057233Z INFO:__main__:🔍 Search: 'patch verification - does assistant response persist now' → 5 results
./slow-path-grep.txt:170:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:372:2026-05-22T19:20:09.784029541Z INFO:primp:response: https://www.bing.com/search?q=ping+after+persist+move 200
./slow-path-grep.txt:171:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:373:2026-05-22T19:20:09.929174574Z INFO:__main__:🔍 Search: 'ping after persist move' → 0 results
./slow-path-grep.txt:172:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:402:2026-05-22T21:14:23.641553467Z INFO:primp:response: https://www.bing.com/search?q=assistant+persistence+final+proof 200
./slow-path-grep.txt:173:/home/cakidd/msallis-diag-20260522-200208/jarvis-web-research.log:403:2026-05-22T21:14:23.743586499Z INFO:__main__:🔍 Search: 'assistant persistence final proof' → 0 results
./slow-path-grep.txt:174:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:168:2026-05-22T23:52:52.686012145Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 3200
./slow-path-grep.txt:175:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:249:2026-05-22T23:52:53.236862897Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 3200
./slow-path-grep.txt:176:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:361:2026-05-22T23:53:13.149684929Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
./slow-path-grep.txt:177:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:445:2026-05-22T23:53:17.557183580Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
./slow-path-grep.txt:178:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:562:2026-05-22T23:53:37.241514389Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:179:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:666:2026-05-22T23:53:47.330645735Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:180:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1195:2026-05-22T23:54:15.806807252Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:181:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1276:2026-05-22T23:54:18.978274494Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:182:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1388:2026-05-22T23:54:29.660032960Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:183:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1492:2026-05-22T23:54:41.631149448Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:184:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1609:2026-05-22T23:54:51.781936135Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:185:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1694:2026-05-22T23:54:53.397496085Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:186:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1811:2026-05-22T23:54:56.256453904Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:187:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:1912:2026-05-22T23:55:10.347849077Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:188:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2025:2026-05-22T23:55:14.009307673Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:189:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2132:2026-05-22T23:55:21.236845252Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:190:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2251:2026-05-22T23:55:31.996226417Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:191:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2354:2026-05-22T23:55:48.851239652Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:192:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2468:2026-05-22T23:55:51.719707737Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
./slow-path-grep.txt:193:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2584:2026-05-22T23:56:04.845748307Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 2048
./slow-path-grep.txt:194:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2715:2026-05-22T23:56:06.198228820Z llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:195:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2802:2026-05-22T23:56:08.299697925Z llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:196:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:2929:2026-05-22T23:56:11.142780529Z llama_model_loader: - kv  12:                      phi3.embedding_length u32              = 3072
./slow-path-grep.txt:197:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3049:2026-05-22T23:56:27.687706746Z llama_model_loader: - kv  12:                      phi3.embedding_length u32              = 3072
./slow-path-grep.txt:198:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3174:2026-05-22T23:56:42.864626949Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:199:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3260:2026-05-22T23:56:49.300142341Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:200:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3377:2026-05-22T23:56:52.158691523Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:201:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3477:2026-05-22T23:57:04.289921868Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:202:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3589:2026-05-22T23:57:11.748896533Z llama_model_loader: - kv   4:                starcoder2.embedding_length u32              = 3072
./slow-path-grep.txt:203:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3694:2026-05-22T23:57:24.742290551Z llama_model_loader: - kv   4:                starcoder2.embedding_length u32              = 3072
./slow-path-grep.txt:204:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3811:2026-05-22T23:57:26.095016910Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:205:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:3913:2026-05-22T23:57:32.620899339Z llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
./slow-path-grep.txt:206:/home/cakidd/msallis-diag-20260522-200208/jarvis-ollama.log:4029:2026-05-22T23:57:40.859081243Z llama_model_loader: - kv   3:                      phi2.embedding_length u32              = 2560
./slow-path-grep.txt:207:/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.log:1:2026-05-19T03:57:54.791666574Z INFO:lm_synthesizer:Starting LM Synthesizer on 0.0.0.0:8001
./slow-path-grep.txt:208:/home/cakidd/msallis-diag-20260522-200208/jarvis-lm-synthesizer.log:76:2026-05-22T22:25:11.815499916Z INFO:lm_synthesizer:Starting LM Synthesizer on 0.0.0.0:8001
./slow-path-grep.txt:209:/home/cakidd/msallis-diag-20260522-200208/jarvis-judge-pipeline.inspect.json:214:                "LM_SYNTHESIZER_URL=http://jarvis-lm-synthesizer:8001",
./slow-path-grep.txt:210:/home/cakidd/msallis-diag-20260522-200208/jarvis-judge-pipeline.inspect.json:237:                "com.docker.compose.depends_on": "jarvis-judge-ethics:service_started:false,jarvis-lm-synthesizer:service_started:false,jarvis-judge-truth:service_started:false,jarvis-judge-consistency:service_started:false,jarvis-judge-alignment:service_started:false",
./slow-path-grep.txt:211:/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:63:jarvis-lm-synthesizer                                   0.12%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
./slow-path-grep.txt:212:/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:153:jarvis-lm-synthesizer                                   0.13%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
./slow-path-grep.txt:213:/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:243:jarvis-lm-synthesizer                                   0.16%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
./slow-path-grep.txt:214:/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:333:jarvis-lm-synthesizer                                   0.15%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
./slow-path-grep.txt:215:/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:423:jarvis-lm-synthesizer                                   0.11%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
./slow-path-grep.txt:216:/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:513:jarvis-lm-synthesizer                                   0.15%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
./slow-path-grep.txt:217:/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:603:jarvis-lm-synthesizer                                   0.14%     17.8MiB / 29.08GiB    0.06%     262kB / 910B      26.1MB / 26.1MB   5
./slow-path-grep.txt:218:/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:693:jarvis-lm-synthesizer                                   0.16%     17.8MiB / 29.08GiB    0.06%     263kB / 910B      26.1MB / 26.1MB   5
./slow-path-grep.txt:219:/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:783:jarvis-lm-synthesizer                                   0.14%     17.8MiB / 29.08GiB    0.06%     263kB / 910B      26.1MB / 26.1MB   5
./slow-path-grep.txt:220:/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:873:jarvis-lm-synthesizer                                   0.16%     17.8MiB / 29.08GiB    0.06%     263kB / 910B      26.1MB / 26.1MB   5
./slow-path-grep.txt:221:/home/cakidd/msallis-diag-20260522-200208/docker-stats-sample.txt:963:jarvis-lm-synthesizer                                   0.14%     17.8MiB / 29.08GiB    0.06%     263kB / 910B      26.1MB / 26.1MB   5
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msallis-diag-20260522-200208$ 

