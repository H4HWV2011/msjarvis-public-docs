cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ docker logs jarvis-consciousness-bridge -f 2>&1 | grep -E "422|200|embed|stored|memory" &

curl -s -X POST "http://localhost:8050/chat" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: super-secret-key" \
  -d '{"message":"memory is now working test","user_id":"test_memory_01"}' \ 
  > /tmp/mem4.json &

echo "Waiting for response..."
wait %2
echo "Done — checking count"

curl -s "http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/count"

Also — 187s is great progress but let's keep pushing toward 110s:

bash
#
[1] 456913
[2] 456914
Waiting for response...
INFO:     172.18.0.56:42562 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.56:55908 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.56:38520 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.56:45714 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:42882 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:50882 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:37192 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:49794 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:38596 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:50914 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:52092 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:45800 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:37958 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:59440 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:49320 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:43530 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:53316 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:39522 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:33052 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:42010 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:41180 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:43914 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:57592 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:44064 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:56380 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:47258 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:37754 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:55240 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:38964 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.51:38966 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.51:34894 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.51:34906 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:50588 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:50600 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:55700 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:55706 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:55716 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:34010 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:38060 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:57142 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:57158 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:57162 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:57172 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:57178 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:45566 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:45568 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:33592 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:60274 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:38472 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:44756 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:47446 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:51678 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.51:51682 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.51:50164 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:56682 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:56684 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:56690 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:56692 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:56704 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:33924 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:59916 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:33666 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:43208 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:35376 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:40998 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:55286 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:34406 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:42858 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:52792 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:52800 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:40866 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:40872 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:35580 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:35590 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:56324 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:56334 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:58246 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:49028 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:41314 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:41320 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:33488 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:51766 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:51842 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:51858 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:47814 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:55446 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:46232 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:46448 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:44186 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:44198 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:50146 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:43998 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:42932 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:38884 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:50564 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:49866 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:52342 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:52358 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:46352 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:50678 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:57496 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:56550 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:37744 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:49896 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:50142 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:34426 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:34294 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:54740 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:53928 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:44434 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:51400 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:53212 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:56100 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:37186 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:34730 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:42822 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:52850 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:38754 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:34114 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:45878 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:39982 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:48130 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:48014 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:38704 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:45688 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:32826 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:53464 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:41700 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:55698 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:43878 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:58290 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:58300 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:39716 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:41728 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:54890 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:32898 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:37526 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:49192 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.51:49448 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:42970 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:57356 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:45002 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:59756 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:39954 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:35570 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:47188 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:44042 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:47290 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:46622 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:56592 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:46944 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:59986 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:57870 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:51958 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:54734 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:52582 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:45144 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:44520 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:34628 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:56522 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:53200 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:43010 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:53564 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:46858 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:49320 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.51:40472 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:47688 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:37854 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:50810 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:47630 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:41362 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:57430 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:44614 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:45784 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:42796 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:46470 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:42392 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:50992 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:34170 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:45976 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:34680 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:48236 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:37600 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:47866 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:43468 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:36528 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:43522 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:43528 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:40066 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:34124 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:50930 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:36730 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:48958 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:34044 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:58160 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:33420 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:42138 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:42150 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:53302 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:44052 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:38332 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:39272 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:33326 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:33328 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:59288 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:59300 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:55512 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:57332 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:36900 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.24:38578 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.24:38768 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.3:37680 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:35314 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.3:35324 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.3:60924 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.1:59216 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.1:51492 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.3:55718 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.3:48810 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.1:34034 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.90:59712 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:38176 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.90:40432 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.90:48404 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:46832 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.90:49374 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.90:40690 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:50312 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.90:39644 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.90:46066 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:34852 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.90:55296 - "POST /chat HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.3:49360 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.90:52644 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:53052 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.90:47228 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.90:51522 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:45384 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:     172.18.0.90:60580 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.90:52652 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:46614 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn 58d4cd99 for default_user
INFO:     172.18.0.90:33342 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.90:33354 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:49470 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn 5888b1c3 for default_user
INFO:     172.18.0.90:32860 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:49724 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:54250 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn 516fcf3e for default_user
INFO:     172.18.0.51:44356 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:44358 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:47846 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn 50d40329 for default_user
INFO:     172.18.0.51:49222 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:39080 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:59150 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn cd309521 for default_user
INFO:     172.18.0.51:39742 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:39750 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:53636 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn f5ceec26 for default_user
INFO:     172.18.0.51:54186 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:51276 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:37304 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn 9cdc78ac for default_user
INFO:     172.18.0.51:39654 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:50910 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:59966 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn 4a319e7f for default_user
INFO:     172.18.0.51:38488 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:32940 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:60266 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn b6aa72c0 for default_user
INFO:     172.18.0.51:40568 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:48110 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:57558 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn 5d9916a8 for default_user
INFO:     172.18.0.51:46186 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:42016 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:49222 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn a17da910 for default_user
INFO:     172.18.0.51:40310 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:44618 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:32882 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn ed750d97 for default_user
INFO:     172.18.0.51:37508 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:35108 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:60374 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn a1bf4abb for carrie_admin
INFO:     172.18.0.51:46158 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:60216 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:42212 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn aee40dcf for carrie_admin
INFO:     172.18.0.51:49734 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:34068 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:55444 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn 7fcc68a7 for carrie_admin
INFO:     172.18.0.51:33930 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:53490 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:49098 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn 1fb7e9c7 for hayden_test
INFO:     172.18.0.51:46030 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.51:56494 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:48944 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn 21a5b48f for carrie_admin
INFO:     172.18.0.51:33124 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.3:47556 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:40430 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.51:45734 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.3:56360 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn 1f28910b for carrie_admin
INFO:     172.18.0.51:40416 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.35:40408 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.73:39520 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn 90191d41 for carrie_admin
INFO:     172.18.0.35:53648 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.73:34338 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.35:60670 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.73:39300 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn a2acab33 for carrie_admin
INFO:     172.18.0.35:43226 - "POST /chat HTTP/1.1" 200 OK
INFO:     172.18.0.35:56326 - "GET /health HTTP/1.1" 200 OK
INFO:     172.18.0.73:58568 - "GET /health HTTP/1.1" 200 OK
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/get "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-hilbert-gateway:8010/wv_summary "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-woah:7012/process "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://jarvis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/8b101b8d-8d18-44b3-884e-a7112569a09e/add "HTTP/1.1 422 Unprocessable Entity"
INFO:__main__:memory: stored turn 7498d2dd for carrie_admin
INFO:     172.18.0.35:41970 - "POST /chat HTTP/1.1" 200 OK
[2]+  Done                    curl -s -X POST "http://localhost:8050/chat" -H "Content-Type: application/json" -H "X-API-Key: super-secret-key" -d '{"message":"memory is now working test","user_id":"test_memory_01"}' > /tmp/mem4.json
Done — checking count
0> 

