PUBLIC_AUTH_ROUTING_DISCOVERY_VALID
config_file=/etc/caddy/Caddyfile
match_count=131
match_file=/etc/caddy/Caddyfile match_line=2 match_text=	@egeria host egeria.mountainshares.us
match_file=/etc/caddy/Caddyfile match_line=7 match_text=		hostnames egeria.mountainshares.us
match_file=/etc/caddy/Caddyfile match_line=8 match_text=		output file /var/log/caddy/caddy_egeria.log
match_file=/etc/caddy/Caddyfile match_line=12 match_text=		hostnames dashboard.mountainshares.us
match_file=/etc/caddy/Caddyfile match_line=17 match_text=		hostnames msallis.mountainshares.us
match_file=/etc/caddy/Caddyfile match_line=22 match_text=	handle @egeria {
match_file=/etc/caddy/Caddyfile match_line=23 match_text=		handle /auth/login* {
match_file=/etc/caddy/Caddyfile match_line=24 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=25 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=26 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=29 match_text=		handle /auth/me* {
match_file=/etc/caddy/Caddyfile match_line=30 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=31 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=32 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=35 match_text=		handle /auth/logout* {
match_file=/etc/caddy/Caddyfile match_line=36 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=37 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=38 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=41 match_text=		handle /auth/register* {
match_file=/etc/caddy/Caddyfile match_line=42 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=43 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=44 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=47 match_text=		handle /auth* {
match_file=/etc/caddy/Caddyfile match_line=48 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=49 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=50 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=53 match_text=		handle /api/me* {
match_file=/etc/caddy/Caddyfile match_line=55 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=56 match_text=			header_up Cookie {http.request.header.Cookie}
match_file=/etc/caddy/Caddyfile match_line=57 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=60 match_text=		handle /api/apply* {
match_file=/etc/caddy/Caddyfile match_line=62 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=63 match_text=			header_up Cookie {http.request.header.Cookie}
match_file=/etc/caddy/Caddyfile match_line=66 match_text=		handle /chat_wv* {
match_file=/etc/caddy/Caddyfile match_line=67 match_text=      reverse_proxy 127.0.0.1:8010 {
match_file=/etc/caddy/Caddyfile match_line=68 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=69 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=72 match_text=			response_header_timeout 300s
match_file=/etc/caddy/Caddyfile match_line=77 match_text=		handle {
match_file=/etc/caddy/Caddyfile match_line=78 match_text=			reverse_proxy 127.0.0.1:3002 {
match_file=/etc/caddy/Caddyfile match_line=79 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=84 match_text=	handle @dashboard {
match_file=/etc/caddy/Caddyfile match_line=85 match_text=		reverse_proxy 127.0.0.1:3002 {
match_file=/etc/caddy/Caddyfile match_line=86 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=90 match_text=	handle @msallis {
match_file=/etc/caddy/Caddyfile match_line=92 match_text=			not: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=94 match_text=		handle /auth/portal/me* {
match_file=/etc/caddy/Caddyfile match_line=95 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=96 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=97 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=98 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=101 match_text=		route /portal* {
match_file=/etc/caddy/Caddyfile match_line=102 match_text=			handle: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=103 match_text=			respond `{"detail":"Not authenticated"}` 401
match_file=/etc/caddy/Caddyfile match_line=105 match_text=			reverse_proxy 127.0.0.1:3002 {
match_file=/etc/caddy/Caddyfile match_line=106 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=109 match_text=		route /admin* {
match_file=/etc/caddy/Caddyfile match_line=110 match_text=			handle: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=111 match_text=			respond `{"detail":"Not authenticated"}` 401
match_file=/etc/caddy/Caddyfile match_line=113 match_text=			reverse_proxy 127.0.0.1:3002 {
match_file=/etc/caddy/Caddyfile match_line=114 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=117 match_text=		handle /api/ui-config {
match_file=/etc/caddy/Caddyfile match_line=119 match_text=			reverse_proxy 127.0.0.1:8001 {
match_file=/etc/caddy/Caddyfile match_line=120 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=123 match_text=		handle /api/me* {
match_file=/etc/caddy/Caddyfile match_line=125 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=126 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=127 match_text=			header_up Cookie {http.request.header.Cookie}
match_file=/etc/caddy/Caddyfile match_line=130 match_text=		handle /api/chat/async {
match_file=/etc/caddy/Caddyfile match_line=131 match_text=			handle: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=132 match_text=			respond `{"detail":"Not authenticated"}` 401
match_file=/etc/caddy/Caddyfile match_line=134 match_text=			reverse_proxy 127.0.0.1:3002 {
match_file=/etc/caddy/Caddyfile match_line=135 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=138 match_text=		handle /chat_wv* {
match_file=/etc/caddy/Caddyfile match_line=139 match_text=			handle: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=140 match_text=			respond `{"detail":"Not authenticated"}` 401
match_file=/etc/caddy/Caddyfile match_line=142 match_text=			reverse_proxy 127.0.0.1:8010 {
match_file=/etc/caddy/Caddyfile match_line=143 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=144 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=147 match_text=			response_header_timeout 300s
match_file=/etc/caddy/Caddyfile match_line=152 match_text=		handle /health {
match_file=/etc/caddy/Caddyfile match_line=153 match_text=			reverse_proxy 127.0.0.1:8095
match_file=/etc/caddy/Caddyfile match_line=155 match_text=		handle /auth/apply* {
match_file=/etc/caddy/Caddyfile match_line=156 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=157 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=158 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=161 match_text=		handle /auth/approve* {
match_file=/etc/caddy/Caddyfile match_line=162 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=163 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=164 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=167 match_text=		handle /auth/deny* {
match_file=/etc/caddy/Caddyfile match_line=168 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=169 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=170 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=173 match_text=		handle /auth/first-login* {
match_file=/etc/caddy/Caddyfile match_line=174 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=175 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=176 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=179 match_text=		handle /auth/login* {
match_file=/etc/caddy/Caddyfile match_line=180 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=181 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=182 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=185 match_text=		handle /auth/logout* {
match_file=/etc/caddy/Caddyfile match_line=186 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=187 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=188 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=191 match_text=		handle /auth/me* {
match_file=/etc/caddy/Caddyfile match_line=192 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=193 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=194 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=197 match_text=		handle /auth/portal* {
match_file=/etc/caddy/Caddyfile match_line=198 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=199 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=200 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=203 match_text=		handle /auth/register* {
match_file=/etc/caddy/Caddyfile match_line=204 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=205 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=206 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=209 match_text=		handle /auth/applications* {
match_file=/etc/caddy/Caddyfile match_line=210 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=211 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=212 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=215 match_text=		handle /auth/chat* {
match_file=/etc/caddy/Caddyfile match_line=216 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=217 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=218 match_text=			header_up X-API-Key {http.request.header.X-API-Key}
match_file=/etc/caddy/Caddyfile match_line=221 match_text=		handle /auth* {
match_file=/etc/caddy/Caddyfile match_line=222 match_text=			reverse_proxy 127.0.0.1:8095 {
match_file=/etc/caddy/Caddyfile match_line=223 match_text=			header_up: [REDACTED]
match_file=/etc/caddy/Caddyfile match_line=226 match_text=		handle {
match_file=/etc/caddy/Caddyfile match_line=227 match_text=			reverse_proxy 127.0.0.1:3002
config_file=/etc/cloudflared/config.yml
match_count=8
match_file=/etc/cloudflared/config.yml match_line=5 match_text=ingress:
match_file=/etc/cloudflared/config.yml match_line=6 match_text=  - hostname: egeria.mountainshares.us
match_file=/etc/cloudflared/config.yml match_line=7 match_text=    service: http://localhost:80
match_file=/etc/cloudflared/config.yml match_line=8 match_text=  - hostname: dashboard.mountainshares.us
match_file=/etc/cloudflared/config.yml match_line=9 match_text=    service: http://localhost:80
match_file=/etc/cloudflared/config.yml match_line=10 match_text=  - hostname: msallis.mountainshares.us
match_file=/etc/cloudflared/config.yml match_line=11 match_text=    service: http://localhost:80
match_file=/etc/cloudflared/config.yml match_line=12 match_text=  - service: http_status:404
config_file=/etc/nginx/conf.d/msjarvis-rate-limit.conf
match_count=8
match_file=/etc/nginx/conf.d/msjarvis-rate-limit.conf match_line=1 match_text=limit_req_zone $binary_remote_addr zone=msjarvis_api_per_ip:10m rate=20r/s;
match_file=/etc/nginx/conf.d/msjarvis-rate-limit.conf match_line=8 match_text=        limit_req zone=msjarvis_api_per_ip burst=40 nodelay;
match_file=/etc/nginx/conf.d/msjarvis-rate-limit.conf match_line=10 match_text=        proxy_set_header Host $host;
match_file=/etc/nginx/conf.d/msjarvis-rate-limit.conf match_line=11 match_text=        proxy_set_header X-Real-IP $remote_addr;
match_file=/etc/nginx/conf.d/msjarvis-rate-limit.conf match_line=12 match_text=        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
match_file=/etc/nginx/conf.d/msjarvis-rate-limit.conf match_line=17 match_text=        proxy_set_header Host $host;
match_file=/etc/nginx/conf.d/msjarvis-rate-limit.conf match_line=18 match_text=        proxy_set_header X-Real-IP $remote_addr;
match_file=/etc/nginx/conf.d/msjarvis-rate-limit.conf match_line=19 match_text=        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
config_file=/etc/nginx/fastcgi.conf
match_count=0
config_file=/etc/nginx/nginx.conf
match_count=1
match_file=/etc/nginx/nginx.conf match_line=66 match_text=#	# http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
config_file=/etc/nginx/snippets/fastcgi-php.conf
match_count=0
config_file=/etc/nginx/snippets/snakeoil.conf
match_count=0
report_sha256=sha256:8d903f74954db924f06c9549c035e744521764536a4fce56404cc4d4171bdab1
report_path=/home/cakidd/msjarvis-pilot-build-evidence-20260810/public-auth-routing-discovery-20260811.json
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ python3 - <<'PY'
import json
import re
import subprocess
from pathlib import Path

print("=== PORT_8095_LISTENER ===")
result = subprocess.run(
    ["ss", "-ltnp", "sport", "=", ":8095"],
    text=True,
    capture_output=True,
)
print(result.stdout.strip() or "NO_LISTENER_ON_8095")

print()
print("=== DOCKER_PORT_8095 ===")
result = subprocess.run(
    [
        "docker", "ps", "--no-trunc",
        "--format",
        "container_id={{.ID}} name={{.Names}} image={{.Image}} "
        "status={{.Status}} ports={{.Ports}} command={{.Command}}",
    ],
PY      breakria and brace_depth <= 0 and number > 22:if matcher_text else "")
=== PORT_8095_LISTENER ===
State  Recv-Q Send-Q Local Address:Port Peer Address:PortProcess
LISTEN 0      2048       127.0.0.1:8095      0.0.0.0:*    users:(("gunicorn",pid=676829,fd=3),("gunicorn",pid=676822,fd=3),("gunicorn",pid=676804,fd=3))

=== DOCKER_PORT_8095 ===
NO_DOCKER_CONTAINER_PUBLISHES_8095

=== CADDY_EGERIA_AUTH_STRUCTURE ===
line=22 directive=handle structure=handle @egeria {
line=23 directive=handle structure=handle /auth/login* {
line=24 directive=reverse_proxy structure=reverse_proxy 127.0.0.1:8095 {
line=25 directive=header_up structure=header_up [REDACTED]
line=26 directive=header_up structure=header_up X-API-Key {http.request.header.X-API-Key}
line=29 directive=handle structure=handle /auth/me* {
line=30 directive=reverse_proxy structure=reverse_proxy 127.0.0.1:8095 {
line=31 directive=header_up structure=header_up [REDACTED]
line=32 directive=header_up structure=header_up X-API-Key {http.request.header.X-API-Key}
line=35 directive=handle structure=handle /auth/logout* {
line=36 directive=reverse_proxy structure=reverse_proxy 127.0.0.1:8095 {
line=37 directive=header_up structure=header_up [REDACTED]
line=38 directive=header_up structure=header_up X-API-Key {http.request.header.X-API-Key}
line=41 directive=handle structure=handle /auth/register* {
line=42 directive=reverse_proxy structure=reverse_proxy 127.0.0.1:8095 {
line=43 directive=header_up structure=header_up [REDACTED]
line=44 directive=header_up structure=header_up X-API-Key {http.request.header.X-API-Key}
line=47 directive=handle structure=handle /auth* {
line=48 directive=reverse_proxy structure=reverse_proxy 127.0.0.1:8095 {
line=49 directive=header_up structure=header_up [REDACTED]
line=50 directive=header_up structure=header_up X-API-Key {http.request.header.X-API-Key}
line=53 directive=handle structure=handle /api/me* {
line=54 directive=rewrite structure=rewrite * /auth/me
line=55 directive=reverse_proxy structure=reverse_proxy 127.0.0.1:8095 {
line=56 directive=header_up structure=header_up Cookie {http.request.header.Cookie}
line=57 directive=header_up structure=header_up [REDACTED]
line=60 directive=handle structure=handle /api/apply* {
line=61 directive=rewrite structure=rewrite * /auth/apply
line=62 directive=reverse_proxy structure=reverse_proxy 127.0.0.1:8095 {
line=63 directive=header_up structure=header_up Cookie {http.request.header.Cookie}
line=66 directive=handle structure=handle /chat_wv* {
line=67 directive=reverse_proxy structure=reverse_proxy 127.0.0.1:8010 {
line=68 directive=header_up structure=header_up [REDACTED]
line=69 directive=header_up structure=header_up [REDACTED]
line=72 directive=response_header_timeout structure=response_header_timeout 300s
line=77 directive=handle structure=handle {
line=78 directive=reverse_proxy structure=reverse_proxy 127.0.0.1:3002 {
line=79 directive=header_up structure=header_up [REDACTED]
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ python3 - <<'PY'
import ast
import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

evidence_dir = Path("/home/cakidd/msjarvis-pilot-build-evidence-20260810")
evidence_dir.mkdir(parents=True, exist_ok=True)
report_path = evidence_dir / "host-gunicorn-auth-discovery-20260811.json"

ss = subprocess.run(
    ["ss", "-ltnp", "sport", "=", ":8095"],
    text=True,
    capture_output=True,
    check=True,
).stdout

pids = sorted(set(re.findall(r'pid=(\d+)', ss)))
if not pids:
PYint("report_path=" + str(report_path))sha256(report_bytes).hexdigest())))():
HOST_GUNICORN_AUTH_DISCOVERY_VALID
port_8095_pid_count=3
gunicorn_pid=676804
gunicorn_cwd=/mnt/spiritual_drive/msjarvis-rebuild
gunicorn_command=/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/gunicorn auth_api:app -k uvicorn_worker.UvicornWorker -w 2 --bind 127.0.0.1:8095
gunicorn_cgroup=0::/system.slice/ms-allis-auth8095.service
gunicorn_pid=676822
gunicorn_cwd=/mnt/spiritual_drive/msjarvis-rebuild
gunicorn_command=/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/gunicorn auth_api:app -k uvicorn_worker.UvicornWorker -w 2 --bind 127.0.0.1:8095
gunicorn_cgroup=0::/system.slice/ms-allis-auth8095.service
gunicorn_pid=676829
gunicorn_cwd=/mnt/spiritual_drive/msjarvis-rebuild
gunicorn_command=/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/gunicorn auth_api:app -k uvicorn_worker.UvicornWorker -w 2 --bind 127.0.0.1:8095
gunicorn_cgroup=0::/system.slice/ms-allis-auth8095.service
auth_source_file_count=172
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_route_line=151 auth_route_decorator=auth_router.post auth_route_paths=/register auth_route_function=register
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_route_line=237 auth_route_decorator=auth_router.post auth_route_paths=/logout auth_route_function=logout
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_route_line=244 auth_route_decorator=auth_router.post auth_route_paths=/login auth_route_function=login
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_route_line=260 auth_route_decorator=auth_router.get auth_route_paths=/me auth_route_function=me
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_route_line=290 auth_route_decorator=auth_router.get auth_route_paths=/admin/chat-metrics auth_route_function=admin_chat_metrics
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_route_line=310 auth_route_decorator=auth_router.get auth_route_paths=/applications/pending auth_route_function=list_pending
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_route_line=359 auth_route_decorator=auth_router.post auth_route_paths=/approve/{application_id} auth_route_function=approve_application
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_route_line=503 auth_route_decorator=auth_router.post auth_route_paths=/deny/{application_id} auth_route_function=deny_application
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_route_line=555 auth_route_decorator=auth_router.post auth_route_paths=/first-login auth_route_function=first_login
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_route_line=605 auth_route_decorator=auth_router.get auth_route_paths=/portal/me/balances auth_route_function=get_my_balances
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_route_line=652 auth_route_decorator=auth_router.get auth_route_paths=/portal/me/ledger auth_route_function=get_my_ledger
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_route_line=773 auth_route_decorator=auth_router.get auth_route_paths=/portal/me/timesheet auth_route_function=get_my_timesheet
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_function_line=98 auth_function_name=_current_user
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_function_line=151 auth_function_name=register
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_function_line=237 auth_function_name=logout
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_function_line=244 auth_function_name=login
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_function_line=555 auth_function_name=first_login
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=32 auth_string_value=auth_router
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=150 auth_string_value=/register
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=238 auth_string_value=Invalidate the bearer token server-side.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=236 auth_string_value=/logout
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=245 auth_string_value=Login accepts either email OR proposed_userid as the username field.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=243 auth_string_value=/login
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=554 auth_string_value=/first-login
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=661 auth_string_value=Return paginated ledger history for the authenticated user.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=72 auth_string_value=/auth
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=95 auth_string_value=/auth/login
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=192 auth_string_value=approved_pending_login
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=192 auth_string_value=pending_first_login
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=646 auth_string_value=founder_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=769 auth_string_value=founder_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=72 auth_string_value=auth
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=225 auth_string_value=[AUTH] Registered 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=535 auth_string_value=[AUTH] Application 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=569 auth_string_value=approved_pending_login
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=569 auth_string_value=pending_first_login
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=593 auth_string_value=first-login
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=594 auth_string_value=[AUTH] First login complete for 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=636 auth_string_value=SELECT serial_number, minted_at, cohort, allocation_type FROM founder_tokens WHERE ueid = %s
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=638 auth_string_value=SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s AND ueid IN (%s, %s)
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=713 auth_string_value=token_class
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=799 auth_string_value=
            SELECT COALESCE(SUM(ems_earned), 0), COUNT(*), COALESCE(SUM(duration_sec), 0)
            FROM equity_timesheet
            WHERE user_id = %s
              AND ueid IN (%s, %s)
              AND status IN ('complete', 'completed')
        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=811 auth_string_value=total_sessions
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=104 auth_string_value=Invalid or expired token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=255 auth_string_value=access_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=325 auth_string_value=SELECT ueid FROM founder_tokens WHERE cohort = 'phase_0'
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=408 auth_string_value=approved_pending_login
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=423 auth_string_value=SELECT COALESCE(MAX(serial_number), 0) FROM founder_tokens
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=587 auth_string_value=first_login_at
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=609 auth_string_value=Invalid token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=105 auth_string_value=WWW-Authenticate
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=220 auth_string_value=[AUTH] First user bootstrap: 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=252 auth_string_value=WWW-Authenticate
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=391 auth_string_value=approved_pending_login
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=428 auth_string_value=INSERT INTO founder_tokens (serial_number, ueid, minted_by, cohort, allocation_type) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=478 auth_string_value=[AUTH] Approval email sent to 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=481 auth_string_value=[AUTH] Approval email not confirmed for 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=484 auth_string_value=[AUTH] Approval email failed: 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=570 auth_string_value=Account not eligible for first login (status=
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=693 auth_string_value=SELECT id, transaction_type, amount, token_class, reason, reference_id, created_at, created_by FROM mountainshares_ledger 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=62 auth_string_value=subject_ref
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=222 auth_string_value=[AUTH] First-user auto-approve failed: 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=432 auth_string_value=[FOUNDER] Minted token #
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=453 auth_string_value=[FOUNDER] Phase 0 cap (60) reached — no token minted for 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=438 auth_string_value=INSERT INTO mountainshares_ledger (ueid, transaction_type, amount, token_class, reason, reference_id, created_by) VALUES (%s, %s, %s, %s, %s, %s, %s)
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/debug_files_20260630/auth_router.debug.py auth_string_line=730 auth_string_value=token_class
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/gis_rag_service.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/gis_rag_service.py auth_route_line=52 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/gis_rag_service.py auth_route_line=133 auth_route_decorator=app.post auth_route_paths=/gis_rag auth_route_function=gis_rag
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/gis_rag_service.py auth_route_line=209 auth_route_decorator=app.post auth_route_paths=/search auth_route_function=search_endpoint
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_route_line=312 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=healthcheck
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_route_line=316 auth_route_decorator=app.post auth_route_paths=/chat/async auth_route_function=create_chat_job
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_route_line=336 auth_route_decorator=app.get auth_route_paths=/chat/status/{job_id} auth_route_function=get_job_status
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_route_line=361 auth_route_decorator=app.delete auth_route_paths=/chat/cancel/all auth_route_function=cancel_all_jobs
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_route_line=381 auth_route_decorator=app.delete auth_route_paths=/chat/cancel/{job_id} auth_route_function=cancel_job
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_route_line=715 auth_route_decorator=app.post auth_route_paths=/ultimate_chat auth_route_function=ultimate_chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_route_line=715 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=ultimate_chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_route_line=1692 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_route_line=1710 auth_route_decorator=governance_router.get auth_route_paths=/query auth_route_function=unified_governance_query
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_string_line=325 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_string_line=626 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_string_line=630 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_string_line=644 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_string_line=1295 auth_string_value=  ✅ I-Containers: Identity processing complete
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_string_line=452 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_string_line=763 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_string_line=1008 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_string_line=1273 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_string_line=1201 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_string_line=1240 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_string_line=1257 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/main_brain_patch.py auth_string_line=1365 auth_string_value=user_id
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_route_line=312 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=healthcheck
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_route_line=316 auth_route_decorator=app.post auth_route_paths=/chat/async auth_route_function=create_chat_job
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_route_line=336 auth_route_decorator=app.get auth_route_paths=/chat/status/{job_id} auth_route_function=get_job_status
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_route_line=361 auth_route_decorator=app.delete auth_route_paths=/chat/cancel/all auth_route_function=cancel_all_jobs
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_route_line=381 auth_route_decorator=app.delete auth_route_paths=/chat/cancel/{job_id} auth_route_function=cancel_job
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_route_line=715 auth_route_decorator=app.post auth_route_paths=/ultimate_chat auth_route_function=ultimate_chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_route_line=715 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=ultimate_chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_route_line=1699 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_route_line=1717 auth_route_decorator=governance_router.get auth_route_paths=/query auth_route_function=unified_governance_query
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_string_line=325 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_string_line=626 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_string_line=630 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_string_line=644 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_string_line=1302 auth_string_value=  ✅ I-Containers: Identity processing complete
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_string_line=452 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_string_line=770 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_string_line=1015 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_string_line=1280 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_string_line=1208 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_string_line=1247 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_string_line=1264 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_bbb_fix.py auth_string_line=1372 auth_string_value=user_id
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_route_line=312 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=healthcheck
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_route_line=316 auth_route_decorator=app.post auth_route_paths=/chat/async auth_route_function=create_chat_job
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_route_line=336 auth_route_decorator=app.get auth_route_paths=/chat/status/{job_id} auth_route_function=get_job_status
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_route_line=361 auth_route_decorator=app.delete auth_route_paths=/chat/cancel/all auth_route_function=cancel_all_jobs
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_route_line=381 auth_route_decorator=app.delete auth_route_paths=/chat/cancel/{job_id} auth_route_function=cancel_job
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_route_line=715 auth_route_decorator=app.post auth_route_paths=/ultimate_chat auth_route_function=ultimate_chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_route_line=715 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=ultimate_chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_route_line=1699 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_route_line=1717 auth_route_decorator=governance_router.get auth_route_paths=/query auth_route_function=unified_governance_query
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_string_line=325 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_string_line=626 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_string_line=630 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_string_line=644 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_string_line=1302 auth_string_value=  ✅ I-Containers: Identity processing complete
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_string_line=452 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_string_line=770 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_string_line=1015 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_string_line=1280 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_string_line=1208 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_string_line=1247 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_string_line=1264 auth_string_value=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/mb_clean_fix.py auth_string_line=1372 auth_string_value=user_id
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/dgm_adoption_worker.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/dgm_adoption_worker.py auth_route_line=113 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/dgm_adoption_worker.py auth_route_line=126 auth_route_decorator=app.post auth_route_paths=/adopt_patches auth_route_function=adopt_patches
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/dgm_adoption_worker.py auth_route_line=187 auth_route_decorator=app.get auth_route_paths=/adoption_log auth_route_function=get_adoption_log
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-69dgm-bridge_jarvis-fractal-consciousness_baseline.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-69dgm-bridge_jarvis-fractal-consciousness_baseline.py auth_route_line=12 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=chat
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-aaacpe-rag_aaacpe_rag_service.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-aaacpe-rag_aaacpe_rag_service.py auth_route_line=26 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-aaacpe-rag_aaacpe_rag_service.py auth_route_line=34 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-aaacpe-rag_aaacpe_rag_service.py auth_route_line=38 auth_route_decorator=app.post auth_route_paths=/search auth_route_function=search
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-aaacpe-rag_aaacpe_rag_service.py auth_route_line=52 auth_route_decorator=app.post auth_route_paths=/ingest auth_route_function=ingest_cultural_intelligence
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-adoption-worker_dgm_adoption_worker.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-adoption-worker_dgm_adoption_worker.py auth_route_line=113 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-adoption-worker_dgm_adoption_worker.py auth_route_line=126 auth_route_decorator=app.post auth_route_paths=/adopt_patches auth_route_function=adopt_patches
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-adoption-worker_dgm_adoption_worker.py auth_route_line=187 auth_route_decorator=app.get auth_route_paths=/adoption_log auth_route_function=get_adoption_log
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-agents-service_ms_jarvis_consciousness_unified_bridge.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-agents-service_ms_jarvis_consciousness_unified_bridge.py auth_route_line=65 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-agents-service_ms_jarvis_consciousness_unified_bridge.py auth_route_line=84 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-agents-service_ms_jarvis_consciousness_unified_bridge.py auth_route_line=94 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=unified_chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-agents-service_ms_jarvis_consciousness_unified_bridge.py auth_route_line=181 auth_route_decorator=app.post auth_route_paths=/experience auth_route_function=experience_endpoint
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-agents-service_ms_jarvis_consciousness_unified_bridge.py auth_route_line=186 auth_route_decorator=app.post auth_route_paths=/filter_consciousness auth_route_function=filter_consciousness_endpoint
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-agents-service_ms_jarvis_consciousness_unified_bridge.py auth_route_line=191 auth_route_decorator=app.get auth_route_paths=/status auth_route_function=status
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py auth_route_line=65 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py auth_route_line=84 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py auth_route_line=94 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=unified_chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py auth_route_line=181 auth_route_decorator=app.post auth_route_paths=/experience auth_route_function=experience_endpoint
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py auth_route_line=186 auth_route_decorator=app.post auth_route_paths=/filter_consciousness auth_route_function=filter_consciousness_endpoint
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-consciousness-bridge_ms_jarvis_consciousness_unified_bridge.py auth_route_line=191 auth_route_decorator=app.get auth_route_paths=/status auth_route_function=status
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py auth_route_line=119 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py auth_route_line=128 auth_route_decorator=app.get auth_route_paths=/constitutional/status auth_route_function=constitutional_status
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py auth_route_line=142 auth_route_decorator=app.get auth_route_paths=/constitutional/principles auth_route_function=constitutional_principles
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py auth_route_line=147 auth_route_decorator=app.post auth_route_paths=/constitutional/check auth_route_function=constitutional_check
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py auth_route_line=240 auth_route_decorator=app.get auth_route_paths=/constitutional/audit auth_route_function=constitutional_audit
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py auth_route_line=263 auth_route_decorator=app.get auth_route_paths=/constitutional/audit/stats auth_route_function=constitutional_audit_stats
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py auth_route_line=298 auth_route_decorator=app.get auth_route_paths=/constitutional/versions auth_route_function=constitutional_versions
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py auth_route_line=333 auth_route_decorator=app.get auth_route_paths=/constitutional/changes/{version} auth_route_function=constitutional_changes
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py auth_route_line=368 auth_route_decorator=app.get auth_route_paths=/constitutional/transparency auth_route_function=constitutional_transparency
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py auth_string_line=136 auth_string_value=authority
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py auth_string_line=357 auth_string_value=Ground Ms. Jarvis in established U.S. Constitutional law for legitimate legal authority
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-constitutional-guardian_constitutional_api.py auth_string_line=171 auth_string_value=unauthorized access
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-fifth-dgm_service_discovery.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-fifth-dgm_service_discovery.py auth_string_line=125 auth_string_value=Get all registered services
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-gis-rag_gis_rag_service.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-gis-rag_gis_rag_service.py auth_route_line=52 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-gis-rag_gis_rag_service.py auth_route_line=133 auth_route_decorator=app.post auth_route_paths=/gis_rag auth_route_function=gis_rag
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-gis-rag_gis_rag_service.py auth_route_line=209 auth_route_decorator=app.post auth_route_paths=/search auth_route_function=search_endpoint
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-hippocampus_hippocampus_service.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-hippocampus_hippocampus_service.py auth_route_line=51 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-hippocampus_hippocampus_service.py auth_route_line=75 auth_route_decorator=app.get auth_route_paths=/status auth_route_function=status
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-hippocampus_hippocampus_service.py auth_route_line=117 auth_route_decorator=app.get auth_route_paths=/retrieve auth_route_function=retrieve
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-hippocampus_hippocampus_service.py auth_route_line=151 auth_route_decorator=app.get auth_route_paths=/consolidation/preview auth_route_function=consolidation_preview
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-i-containers_icontainers_fastapi.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-i-containers_icontainers_fastapi.py auth_route_line=36 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-i-containers_icontainers_fastapi.py auth_route_line=134 auth_route_decorator=app.post auth_route_paths=/process auth_route_function=process
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-i-containers_icontainers_fastapi.py auth_function_line=78 auth_function_name=build_identity_layers
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-i-containers_icontainers_fastapi.py auth_string_line=83 auth_string_value=
    Build a simple identity_layers list from the NBB payload.
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-i-containers_icontainers_fastapi.py auth_string_line=135 auth_string_value=
    Thin adapter:
    - Calls NBB i-containers
    - Projects its dual-awareness payload into:
      ego_boundaries, experiential_processing, observer_processing, icontainers_state, identity_layers
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-i-containers_icontainers_fastapi.py auth_string_line=89 auth_string_value=identity_core
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-i-containers_icontainers_fastapi.py auth_string_line=97 auth_string_value=identity-core
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-i-containers_icontainers_fastapi.py auth_string_line=98 auth_string_value=identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-i-containers_icontainers_fastapi.py auth_string_line=104 auth_string_value=identity_core
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-alignment_lm_synthesizer.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-alignment_lm_synthesizer.py auth_route_line=39 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-alignment_lm_synthesizer.py auth_route_line=59 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-alignment_lm_synthesizer.py auth_route_line=102 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-alignment_lm_synthesizer.py auth_string_line=60 auth_string_value=
    Canonical synthesizer endpoint for main_brain:
    POST /chat {message, user_id, context?}
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-alignment_lm_synthesizer.py auth_string_line=66 auth_string_value=user_id
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-consistency_lm_synthesizer.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-consistency_lm_synthesizer.py auth_route_line=39 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-consistency_lm_synthesizer.py auth_route_line=59 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-consistency_lm_synthesizer.py auth_route_line=102 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-consistency_lm_synthesizer.py auth_string_line=60 auth_string_value=
    Canonical synthesizer endpoint for main_brain:
    POST /chat {message, user_id, context?}
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-consistency_lm_synthesizer.py auth_string_line=66 auth_string_value=user_id
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-ethics_lm_synthesizer.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-ethics_lm_synthesizer.py auth_route_line=39 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-ethics_lm_synthesizer.py auth_route_line=59 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-ethics_lm_synthesizer.py auth_route_line=102 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-ethics_lm_synthesizer.py auth_string_line=60 auth_string_value=
    Canonical synthesizer endpoint for main_brain:
    POST /chat {message, user_id, context?}
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-ethics_lm_synthesizer.py auth_string_line=66 auth_string_value=user_id
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-pipeline_judge_pipeline.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-pipeline_judge_pipeline.py auth_route_line=77 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-pipeline_judge_pipeline.py auth_route_line=135 auth_route_decorator=app.post auth_route_paths=/evaluate auth_route_function=evaluate_pipeline
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-pipeline_judge_pipeline.py auth_string_line=216 auth_string_value=

Please synthesize the expert responses and judge feedback into a refined, accurate answer that addresses all issues while maintaining Ms. Egeria Jarvis's identity.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-pipeline_judge_pipeline.py auth_string_line=226 auth_string_value=user_id
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-truth_lm_synthesizer.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-truth_lm_synthesizer.py auth_route_line=39 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-truth_lm_synthesizer.py auth_route_line=59 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-truth_lm_synthesizer.py auth_route_line=102 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-truth_lm_synthesizer.py auth_string_line=60 auth_string_value=
    Canonical synthesizer endpoint for main_brain:
    POST /chat {message, user_id, context?}
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-judge-truth_lm_synthesizer.py auth_string_line=66 auth_string_value=user_id
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-lm-synthesizer_lm_synthesizer.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-lm-synthesizer_lm_synthesizer.py auth_route_line=39 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-lm-synthesizer_lm_synthesizer.py auth_route_line=59 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-lm-synthesizer_lm_synthesizer.py auth_route_line=102 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-lm-synthesizer_lm_synthesizer.py auth_string_line=60 auth_string_value=
    Canonical synthesizer endpoint for main_brain:
    POST /chat {message, user_id, context?}
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-lm-synthesizer_lm_synthesizer.py auth_string_line=66 auth_string_value=user_id
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-local-resources_local_resources_resolver.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-local-resources_local_resources_resolver.py auth_route_line=42 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-local-resources_local_resources_resolver.py auth_route_line=47 auth_route_decorator=app.post auth_route_paths=/resolve auth_route_function=resolve_resources
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-mother-protocols_mother_protocols.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-mother-protocols_mother_protocols.py auth_route_line=14 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-mother-protocols_mother_protocols.py auth_route_line=18 auth_route_decorator=app.post auth_route_paths=/guidance auth_route_function=guidance
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-neurobiological-master_ms_jarvis_consciousness_unified_bridge.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-neurobiological-master_ms_jarvis_consciousness_unified_bridge.py auth_route_line=65 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-neurobiological-master_ms_jarvis_consciousness_unified_bridge.py auth_route_line=84 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-neurobiological-master_ms_jarvis_consciousness_unified_bridge.py auth_route_line=94 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=unified_chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-neurobiological-master_ms_jarvis_consciousness_unified_bridge.py auth_route_line=181 auth_route_decorator=app.post auth_route_paths=/experience auth_route_function=experience_endpoint
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-neurobiological-master_ms_jarvis_consciousness_unified_bridge.py auth_route_line=186 auth_route_decorator=app.post auth_route_paths=/filter_consciousness auth_route_function=filter_consciousness_endpoint
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-neurobiological-master_ms_jarvis_consciousness_unified_bridge.py auth_route_line=191 auth_route_decorator=app.get auth_route_paths=/status auth_route_function=status
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-psychology-services_psychology_integration_adapter.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-psychology-services_psychology_integration_adapter.py auth_string_line=159 auth_string_value=
                INSERT INTO identity_access_log 
                (ueid, action, service, endpoint, success, error_message, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-psychology-services_psychology_integration_adapter.py auth_string_line=48 auth_string_value=user_id
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-qualia-engine_ms_jarvis_qualia_engine.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-qualia-engine_ms_jarvis_qualia_engine.py auth_route_line=28 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-qualia-engine_ms_jarvis_qualia_engine.py auth_route_line=37 auth_route_decorator=app.post auth_route_paths=/communicate auth_route_function=communicate
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py auth_route_line=65 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py auth_route_line=84 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py auth_route_line=94 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=unified_chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py auth_route_line=181 auth_route_decorator=app.post auth_route_paths=/experience auth_route_function=experience_endpoint
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py auth_route_line=186 auth_route_decorator=app.post auth_route_paths=/filter_consciousness auth_route_function=filter_consciousness_endpoint
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-rag-server_ms_jarvis_consciousness_unified_bridge.py auth_route_line=191 auth_route_decorator=app.get auth_route_paths=/status auth_route_function=status
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-semaphore_msjarvis_semaphore.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-semaphore_msjarvis_semaphore.py auth_route_line=21 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-semaphore_msjarvis_semaphore.py auth_route_line=31 auth_route_decorator=app.post auth_route_paths=/proxy auth_route_function=proxy_request
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-spiritual-rag_spiritual_rag_domain.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-spiritual-rag_spiritual_rag_domain.py auth_route_line=51 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-spiritual-rag_spiritual_rag_domain.py auth_route_line=62 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-spiritual-rag_spiritual_rag_domain.py auth_route_line=73 auth_route_decorator=app.post auth_route_paths=/search auth_route_function=search
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-spiritual-rag_spiritual_rag_domain.py auth_route_line=115 auth_route_decorator=app.post auth_route_paths=/add_document auth_route_function=add_document
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-spiritual-rag_spiritual_rag_domain.py auth_string_line=43 auth_string_value=Let your life speak - authentic action rooted in faith is more powerful than words alone.
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-swarm-intelligence_ms_jarvis_consciousness_unified_bridge.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-swarm-intelligence_ms_jarvis_consciousness_unified_bridge.py auth_route_line=65 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-swarm-intelligence_ms_jarvis_consciousness_unified_bridge.py auth_route_line=84 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-swarm-intelligence_ms_jarvis_consciousness_unified_bridge.py auth_route_line=94 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=unified_chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-swarm-intelligence_ms_jarvis_consciousness_unified_bridge.py auth_route_line=181 auth_route_decorator=app.post auth_route_paths=/experience auth_route_function=experience_endpoint
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-swarm-intelligence_ms_jarvis_consciousness_unified_bridge.py auth_route_line=186 auth_route_decorator=app.post auth_route_paths=/filter_consciousness auth_route_function=filter_consciousness_endpoint
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-swarm-intelligence_ms_jarvis_consciousness_unified_bridge.py auth_route_line=191 auth_route_decorator=app.get auth_route_paths=/status auth_route_function=status
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-temporal-consciousness_temporal_consciousness.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-temporal-consciousness_temporal_consciousness.py auth_route_line=14 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-temporal-consciousness_temporal_consciousness.py auth_route_line=18 auth_route_decorator=app.post auth_route_paths=/temporalanalysis auth_route_function=temporalanalysis
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-toroidal_toroidal_service.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-toroidal_toroidal_service.py auth_route_line=40 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-toroidal_toroidal_service.py auth_route_line=48 auth_route_decorator=app.get auth_route_paths=/selftest auth_route_function=selftest
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-toroidal_toroidal_service.py auth_route_line=74 auth_route_decorator=app.post auth_route_paths=/process auth_route_function=process
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py auth_route_line=104 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py auth_route_line=123 auth_route_decorator=app.post auth_route_paths=/chat_wv auth_route_function=chat_wv
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/jarvis-wv-entangled-gateway_msjarvis_wv_entangled_gateway.py auth_string_line=133 auth_string_value=user_id
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm1-proxy_llm1_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm1-proxy_llm1_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm1-proxy_llm1_health_proxy.py auth_route_line=56 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm10-proxy_llm10_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm10-proxy_llm10_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm10-proxy_llm10_health_proxy.py auth_route_line=64 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm11-proxy_llm11_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm11-proxy_llm11_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm11-proxy_llm11_health_proxy.py auth_route_line=56 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm12-proxy_llm12_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm12-proxy_llm12_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm12-proxy_llm12_health_proxy.py auth_route_line=56 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm13-proxy_llm13_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm13-proxy_llm13_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm13-proxy_llm13_health_proxy.py auth_route_line=64 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm14-proxy_llm14_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm14-proxy_llm14_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm14-proxy_llm14_health_proxy.py auth_route_line=64 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm15-proxy_llm15_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm15-proxy_llm15_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm15-proxy_llm15_health_proxy.py auth_route_line=64 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm16-proxy_llm16_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm16-proxy_llm16_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm16-proxy_llm16_health_proxy.py auth_route_line=56 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm17-proxy_llm17_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm17-proxy_llm17_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm17-proxy_llm17_health_proxy.py auth_route_line=56 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm18-proxy_llm18_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm18-proxy_llm18_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm18-proxy_llm18_health_proxy.py auth_route_line=64 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm19-proxy_llm19_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm19-proxy_llm19_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm19-proxy_llm19_health_proxy.py auth_route_line=64 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm2-proxy_llm2_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm2-proxy_llm2_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm2-proxy_llm2_health_proxy.py auth_route_line=56 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm20-proxy_llm20_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm20-proxy_llm20_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm20-proxy_llm20_health_proxy.py auth_route_line=56 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm21-proxy_llm21_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm21-proxy_llm21_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm21-proxy_llm21_health_proxy.py auth_route_line=64 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm22-proxy_llm22_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm22-proxy_llm22_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm22-proxy_llm22_health_proxy.py auth_route_line=57 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm3-proxy_llm3_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm3-proxy_llm3_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm3-proxy_llm3_health_proxy.py auth_route_line=64 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm4-proxy_llm4_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm4-proxy_llm4_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm4-proxy_llm4_health_proxy.py auth_route_line=56 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm5-proxy_llm5_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm5-proxy_llm5_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm5-proxy_llm5_health_proxy.py auth_route_line=64 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm6-proxy_llm6_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm6-proxy_llm6_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm6-proxy_llm6_health_proxy.py auth_route_line=56 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm7-proxy_llm7_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm7-proxy_llm7_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm7-proxy_llm7_health_proxy.py auth_route_line=56 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm8-proxy_llm8_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm8-proxy_llm8_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm8-proxy_llm8_health_proxy.py auth_route_line=56 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm9-proxy_llm9_health_proxy.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm9-proxy_llm9_health_proxy.py auth_route_line=23 auth_route_decorator=app.post auth_route_paths=/generate auth_route_function=generate
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/llm9-proxy_llm9_health_proxy.py auth_route_line=56 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/ms_jarvis_qualia_engine.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/ms_jarvis_qualia_engine.py auth_route_line=28 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/ms_jarvis_qualia_engine.py auth_route_line=37 auth_route_decorator=app.post auth_route_paths=/communicate auth_route_function=communicate
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_blood_brain_barrier-1_ms_jarvis_consciousness_bridge.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_blood_brain_barrier-1_ms_jarvis_consciousness_bridge.py auth_route_line=6 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_blood_brain_barrier-1_ms_jarvis_consciousness_bridge.py auth_route_line=10 auth_route_decorator=app.post auth_route_paths=/process auth_route_function=process
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_consciousness_containers-1_main.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_consciousness_containers-1_main.py auth_route_line=11 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=read_root
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_heteroglobulin_transport-1_main.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_heteroglobulin_transport-1_main.py auth_route_line=11 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=read_root
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py auth_route_line=65 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py auth_route_line=84 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py auth_route_line=94 auth_route_decorator=app.post auth_route_paths=/chat auth_route_function=unified_chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py auth_route_line=181 auth_route_decorator=app.post auth_route_paths=/experience auth_route_function=experience_endpoint
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py auth_route_line=186 auth_route_decorator=app.post auth_route_paths=/filter_consciousness auth_route_function=filter_consciousness_endpoint
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_i_containers-1_ms_jarvis_consciousness_unified_bridge.py auth_route_line=191 auth_route_decorator=app.get auth_route_paths=/status auth_route_function=status
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_mother_carrie_protocols-1_main.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_mother_carrie_protocols-1_main.py auth_route_line=11 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=read_root
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_pituitary_gland-1_main.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_pituitary_gland-1_main.py auth_route_line=11 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=read_root
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_prefrontal_cortex-1_main.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_prefrontal_cortex-1_main.py auth_route_line=11 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=read_root
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_qualia_engine-1_ms_jarvis_consciousness_bridge.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_qualia_engine-1_ms_jarvis_consciousness_bridge.py auth_route_line=6 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_qualia_engine-1_ms_jarvis_consciousness_bridge.py auth_route_line=10 auth_route_decorator=app.post auth_route_paths=/process auth_route_function=process
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_spiritual_maternal_integration-1_main.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_spiritual_maternal_integration-1_main.py auth_route_line=11 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=read_root
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_spiritual_root-1_main.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_spiritual_root-1_main.py auth_route_line=11 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=read_root
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_subconscious-1_main.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_subconscious-1_main.py auth_route_line=11 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=read_root
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_woah_algorithms-1_service_discovery.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/msjarvis-rebuild-nbb_woah_algorithms-1_service_discovery.py auth_string_line=120 auth_string_value=Get all registered services
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/nbb_darwin_godel_machines.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/nbb_darwin_godel_machines.py auth_route_line=128 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/nbb_darwin_godel_machines.py auth_route_line=144 auth_route_decorator=app.get auth_route_paths=/list_targets auth_route_function=list_targets
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/nbb_darwin_godel_machines.py auth_route_line=156 auth_route_decorator=app.post auth_route_paths=/propose_patches auth_route_function=propose_patches
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/nbb_darwin_godel_machines.py auth_route_line=236 auth_route_decorator=app.post auth_route_paths=/enqueue_patches auth_route_function=enqueue_patches
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/nbb_darwin_godel_machines.py auth_route_line=302 auth_route_decorator=app.post auth_route_paths=/commit_patch auth_route_function=commit_patch
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/nbb_darwin_godel_machines_msjarvis-rebuild-nbb_spiritual_root-1_main.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/nbb_darwin_godel_machines_msjarvis-rebuild-nbb_spiritual_root-1_main.py auth_route_line=11 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=read_root
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/port_9000_69dgm_bridge.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/port_9000_69dgm_bridge.py auth_route_line=65 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/port_9000_69dgm_bridge.py auth_route_line=117 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/port_9000_69dgm_bridge.py auth_route_line=132 auth_route_decorator=app.post auth_route_paths=/consciousnesschat auth_route_function=consciousness_chat
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/port_9000_69dgm_bridge.py auth_route_line=261 auth_route_decorator=app.post auth_route_paths=/assess auth_route_function=assess_legacy
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/port_9000_69dgm_bridge.py auth_route_line=266 auth_route_decorator=app.get auth_route_paths=/metrics auth_route_function=metrics
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/port_9000_69dgm_bridge.py auth_route_line=300 auth_route_decorator=app.get auth_route_paths=/status auth_route_function=status
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/port_9000_69dgm_bridge.py auth_string_line=102 auth_string_value=user_id
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/psychological_rag_domain_psychological_rag_domain.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/psychological_rag_domain_psychological_rag_domain.py auth_route_line=72 auth_route_decorator=app.get auth_route_paths=/ auth_route_function=root
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/psychological_rag_domain_psychological_rag_domain.py auth_route_line=85 auth_route_decorator=app.get auth_route_paths=/health auth_route_function=health
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/psychological_rag_domain_psychological_rag_domain.py auth_route_line=119 auth_route_decorator=app.post auth_route_paths=/search auth_route_function=search
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/psychological_rag_domain_psychological_rag_domain.py auth_route_line=171 auth_route_decorator=app.post auth_route_paths=/query auth_route_function=query_rag
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.archive/services.backup_20260308_111532/psychological_rag_domain_psychological_rag_domain.py auth_route_line=198 auth_route_decorator=app.post auth_route_paths=/add_document auth_route_function=add_document
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/_yaml/__init__.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/_yaml/__init__.py auth_string_line=19 auth_string_value=The _yaml extension module is now located at yaml._yaml and its location is subject to change.  To use the LibYAML-based parser and emitter, import from `yaml`: `from yaml import CLoader as Loader, CDumper as Dumper`.
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py auth_function_line=1973 auth_function_name=total_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py auth_function_line=1977 auth_function_name=total_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py auth_function_line=1994 auth_function_name=borrowed_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py auth_function_line=1998 auth_function_name=available_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py auth_function_line=2345 auth_function_name=current_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py auth_string_line=1979 auth_string_value=total_tokens must be an int or math.inf
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py auth_string_line=1982 auth_string_value=total_tokens must be >= 0
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py auth_string_line=2013 auth_string_value=this borrower is already holding one of this CapacityLimiter's tokens
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py auth_string_line=2056 auth_string_value=this borrower isn't holding any of this CapacityLimiter's tokens
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_trio.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_trio.py auth_function_line=771 auth_function_name=total_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_trio.py auth_function_line=775 auth_function_name=total_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_trio.py auth_function_line=779 auth_function_name=borrowed_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_trio.py auth_function_line=783 auth_function_name=available_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_trio.py auth_function_line=971 auth_function_name=current_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_trio.py auth_string_line=1064 auth_string_value=trio.lowlevel.TrioToken | None
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_backends/_trio.py auth_string_line=1077 auth_string_value=trio.lowlevel.TrioToken | None
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_asyncio_selector_thread.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_asyncio_selector_thread.py auth_string_line=59 auth_string_value=selector still has registered file descriptors after shutdown
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_asyncio_selector_thread.py auth_string_line=77 auth_string_value=this file descriptor is already registered for reading
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_asyncio_selector_thread.py auth_string_line=94 auth_string_value=this file descriptor is already registered for writing
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_exceptions.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_exceptions.py auth_string_line=148 auth_string_value=
    Raised by :func:`.from_thread.run` and :func:`.from_thread.run_sync` if the event
    loop associated with the explicitly passed token has already finished.
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_exceptions.py auth_string_line=155 auth_string_value=The event loop associated with the given token has already finished
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_function_line=531 auth_function_name=total_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_function_line=548 auth_function_name=total_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_function_line=552 auth_function_name=borrowed_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_function_line=557 auth_function_name=available_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_function_line=658 auth_function_name=total_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_function_line=665 auth_function_name=total_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_function_line=678 auth_function_name=borrowed_tokens
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_function_line=685 auth_function_name=available_tokens
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_string_line=553 auth_string_value=The number of tokens that have currently been borrowed.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_string_line=558 auth_string_value=The number of tokens currently available to be borrowed
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_string_line=562 auth_string_value=
        Acquire a token for the current task without waiting for one to become
        available.

        :raises ~anyio.WouldBlock: if there are no tokens available for borrowing

        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_string_line=572 auth_string_value=
        Acquire a token without waiting for one to become available.

        :param borrower: the entity borrowing a token
        :raises ~anyio.WouldBlock: if there are no tokens available for borrowing

        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_string_line=582 auth_string_value=
        Acquire a token for the current task, waiting if necessary for one to become
        available.

        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_string_line=590 auth_string_value=
        Acquire a token, waiting if necessary for one to become available.

        :param borrower: the entity borrowing a token

        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_string_line=599 auth_string_value=
        Release the token held by the current task.

        :raises RuntimeError: if the current task has not borrowed a token from this
            limiter.

        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_string_line=609 auth_string_value=
        Release the token held by the given borrower.

        :raises RuntimeError: if the borrower has not borrowed a token from this
            limiter.

        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_string_line=667 auth_string_value=total_tokens must be an int or math.inf
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/_core/_synchronization.py auth_string_line=669 auth_string_value=total_tokens must be >= 1
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/abc/_eventloop.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/abc/_eventloop.py auth_function_line=80 auth_function_name=current_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/abc/_eventloop.py auth_string_line=81 auth_string_value=
        Return an object that allows other threads to run code inside the event loop.

        :return: a token object, specific to the event loop running in the current
            thread
        
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/from_thread.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/from_thread.py auth_function_line=54 auth_function_name=_token_or_error
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/from_thread.py auth_string_line=62 auth_string_value=Not running inside an AnyIO worker thread, and no event loop token was provided
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/lowlevel.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/lowlevel.py auth_function_line=81 auth_function_name=current_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/lowlevel.py auth_string_line=4 auth_string_value=EventLoopToken
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/lowlevel.py auth_string_line=5 auth_string_value=RunvarToken
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/lowlevel.py auth_string_line=10 auth_string_value=current_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/lowlevel.py auth_string_line=82 auth_string_value=
    Return a token object that can be used to call code in the current event loop from
    another thread.

    :raises NoEventLoopError: if no supported asynchronous event loop is running in the
        current thread

    .. versionadded:: 4.11.0

    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/lowlevel.py auth_string_line=180 auth_string_value=This token does not belong to this RunVar
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/lowlevel.py auth_string_line=183 auth_string_value=This token has already been used
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/pytest_plugin.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/pytest_plugin.py auth_string_line=285 auth_string_value=session
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/pytest_plugin.py auth_string_line=290 auth_string_value=session
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/streams/tls.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/anyio/streams/tls.py auth_string_line=260 auth_string_value=send_eof() requires at least TLSv1.3; current session uses 
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/attr/_make.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/attr/_make.py auth_string_line=771 auth_string_value=
        Evaluate any registered snippets in one go.
        
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/attrs/__init__.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/attrs/__init__.py auth_string_line=39 auth_string_value=__author__
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/__init__.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/__init__.py auth_string_line=81 auth_string_value=TokenTransportHeader
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/__init__.py auth_string_line=435 auth_string_value=chromadb.auth.token_authn.TokenAuthClientProvider
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/__init__.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/__init__.py auth_function_line=381 auth_function_name=get_user_identity
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/async_api.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/async_api.py auth_function_line=333 auth_function_name=get_user_identity
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/async_client.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/async_client.py auth_function_line=120 auth_function_name=get_user_identity
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/async_fastapi.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/async_fastapi.py auth_function_line=264 auth_function_name=get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/async_fastapi.py auth_string_line=262 auth_string_value=AsyncFastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/async_fastapi.py auth_string_line=265 auth_string_value=/auth/identity
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/client.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/client.py auth_function_line=132 auth_function_name=get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/client.py auth_string_line=91 auth_string_value=Could not determine a tenant from the current authentication method. Please provide a tenant.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/client.py auth_string_line=95 auth_string_value=Could not determine a database name from the current authentication method. Please provide a database name.
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/collection_configuration.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/collection_configuration.py auth_string_line=96 auth_string_value= not found. Add @register_embedding_function decorator to the class definition.
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/fastapi.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/fastapi.py auth_function_line=225 auth_function_name=get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/fastapi.py auth_string_line=223 auth_string_value=FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/fastapi.py auth_string_line=226 auth_string_value=/auth/identity
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/rust.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/rust.py auth_function_line=669 auth_function_name=get_user_identity
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/segment.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/segment.py auth_function_line=204 auth_function_name=get_user_identity
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/shared_system_client.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/shared_system_client.py auth_string_line=174 auth_string_value=x-chroma-token
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/types.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/api/types.py auth_function_line=974 auth_function_name=max_tokens
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/__init__.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/__init__.py auth_function_line=44 auth_function_name=authenticate
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/__init__.py auth_function_line=90 auth_function_name=authenticate_or_raise
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/__init__.py auth_function_line=211 auth_function_name=authorize_or_raise
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/__init__.py auth_string_line=34 auth_string_value=
    ClientAuthProvider is responsible for providing authentication headers for
    client requests. Client implementations (in our case, just the FastAPI
    client) must inject these headers into their requests.
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/__init__.py auth_string_line=158 auth_string_value=
    The set of actions that can be authorized by the authorization provider.
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/__init__.py auth_string_line=187 auth_string_value=
    The resource being accessed in an authorization request.
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/__init__.py auth_string_line=113 auth_string_value=No credentials file or credentials found in [chroma_server_authn_credentials].
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/__init__.py auth_string_line=220 auth_string_value=chroma_server_authz_config_file
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/__init__.py auth_string_line=225 auth_string_value=No authz configuration file or authz configuration found.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/__init__.py auth_string_line=229 auth_string_value=Both authz configuration file and authz configuration found.Please provide only one.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/__init__.py auth_string_line=107 auth_string_value=chroma_server_authn_credentials_file
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/__init__.py auth_string_line=110 auth_string_value=chroma_server_authn_credentials
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/__init__.py auth_string_line=222 auth_string_value=chroma_server_authz_config
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py auth_function_line=51 auth_function_name=authenticate
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py auth_function_line=105 auth_function_name=authenticate_or_raise
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py auth_string_line=35 auth_string_value=Authorization
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py auth_string_line=33 auth_string_value=BasicAuthenticationServerProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py auth_string_line=33 auth_string_value=BasicAuthClientProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py auth_string_line=39 auth_string_value=
    Client auth provider for basic auth. The credentials are passed as a
    base64-encoded string in the Authorization header prepended with "Basic ".
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py auth_string_line=102 auth_string_value=BasicAuthenticationServerProvider.authenticate
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py auth_string_line=47 auth_string_value=chroma_client_auth_credentials
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py auth_string_line=95 auth_string_value=Duplicate username found in [chroma_server_authn_credentials]. Usernames must be unique.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py auth_string_line=115 auth_string_value=Invalid Authorization header format
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py auth_string_line=131 auth_string_value=BasicAuthenticationServerProvider.authenticate failed: 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/basic_authn/__init__.py auth_string_line=140 auth_string_value=BasicAuthenticationServerProvider.authenticate failed: Failed to authenticate 
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/simple_rbac_authz/__init__.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/simple_rbac_authz/__init__.py auth_function_line=58 auth_function_name=authorize_or_raise
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/simple_rbac_authz/__init__.py auth_string_line=54 auth_string_value=SimpleRBACAuthorizationProvider.authorize
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/simple_rbac_authz/__init__.py auth_string_line=50 auth_string_value=Authorization Provider SimpleRBACAuthorizationProvider initialized
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/simple_rbac_authz/__init__.py auth_string_line=69 auth_string_value=Authorization decision: Access 
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_function_line=56 auth_function_name=_check_token
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_function_line=70 auth_function_name=_check_allowed_token_headers
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_function_line=105 auth_function_name=authenticate
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_function_line=194 auth_function_name=authenticate_or_raise
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=34 auth_string_value=TokenAuthenticationServerProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=35 auth_string_value=TokenAuthClientProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=36 auth_string_value=TokenTransportHeader
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=41 auth_string_value=
    Accceptable token transport headers.
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=49 auth_string_value=Authorization
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=50 auth_string_value=X-Chroma-Token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=79 auth_string_value=
    Client auth provider for token-based auth. Header key will be either
    "Authorization" or "X-Chroma-Token" depending on
    `chroma_auth_token_transport_header`. If the header is "Authorization",
    the token is passed as a bearer token.
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=115 auth_string_value=
    A simple User class for use in this module only. If you need a generic
    way to represent a User, please use UserIdentity as this class keeps
    track of sensitive tokens.
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=191 auth_string_value=TokenAuthenticationServerProvider.authenticate
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=60 auth_string_value=Invalid token. Must contain only ASCII letters, digits, and punctuation.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=90 auth_string_value=chroma_client_auth_credentials
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=73 auth_string_value=Invalid token transport header: 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=171 auth_string_value=tokens
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=177 auth_string_value=tokens
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=172 auth_string_value=User missing tokens
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=210 auth_string_value=Invalid credentials: Token not found}
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=198 auth_string_value=Authorization header '
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=203 auth_string_value=Bearer not found in Authorization header
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=220 auth_string_value=TokenAuthenticationServerProvider.authenticate failed: 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=229 auth_string_value=TokenAuthenticationServerProvider.authenticate failed: Failed to authenticate 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py auth_string_line=184 auth_string_value=Token 
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/base_types.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/base_types.py auth_string_line=87 auth_string_value=Serialize to transport format with type tag.

        Note: Uses 'tokens' as the wire format key name for compatibility
        with the protobuf schema, even though the Python attribute is 'labels'.
        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/base_types.py auth_string_line=103 auth_string_value=Deserialize from transport format (strict - requires #type field).

        Note: Reads from 'tokens' key in the wire format for compatibility
        with the protobuf schema, mapping it to the 'labels' attribute.
        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/base_types.py auth_string_line=98 auth_string_value=tokens
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/base_types.py auth_string_line=115 auth_string_value=tokens
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/config.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/config.py auth_string_line=67 auth_string_value=chromadb.auth.ClientAuthProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/config.py auth_string_line=68 auth_string_value=chromadb.auth.ServerAuthenticationProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/config.py auth_string_line=69 auth_string_value=chromadb.auth.ServerAuthorizationProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/config.py auth_string_line=67 auth_string_value=chroma_client_auth_provider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/config.py auth_string_line=68 auth_string_value=chroma_server_authn_provider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/config.py auth_string_line=69 auth_string_value=chroma_server_authz_provider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/config.py auth_string_line=337 auth_string_value=Get a Component instance of the given type, and register as a dependency of
        that instance.
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/errors.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/errors.py auth_string_line=183 auth_string_value=AuthorizationError
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/errors.py auth_string_line=188 auth_string_value=AuthError
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/errors.py auth_string_line=49 auth_string_value=AuthError
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/errors.py auth_string_line=96 auth_string_value=AuthorizationError
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/execution/expression/operator.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/execution/expression/operator.py auth_string_line=1279 auth_string_value=Create Select from dictionary.

        Examples:
        - {"keys": ["#document", "#score"]} -> Select(keys={Key.DOCUMENT, Key.SCORE})
        - {"keys": ["title", "author"]} -> Select(keys={"title", "author"})
        
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/ingest/__init__.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/ingest/__init__.py auth_string_line=109 auth_string_value=Unregister a subscription. The consume function will no longer be invoked,
        and resources associated with the subscription will be released.
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/segment/distributed/__init__.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/segment/distributed/__init__.py auth_function_line=21 auth_function_name=register_updated_segment_callback
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/segment/distributed/__init__.py auth_function_line=64 auth_function_name=register_updated_memberlist_callback
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/segment/distributed/__init__.py auth_function_line=72 auth_function_name=unregister_updated_memberlist_callback
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/segment/distributed/__init__.py auth_string_line=24 auth_string_value=Register a callback that will be called when a segment is updated
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/segment/distributed/__init__.py auth_string_line=67 auth_string_value=Registers a callback that will be called when the memberlist changes. May be called many times
        with the same memberlist, so callers should be idempotent. May be called from a different thread.
        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/segment/distributed/__init__.py auth_string_line=75 auth_string_value=Unregisters a callback that was previously registered. Returns True if the callback was
        successfully unregistered, False if it was not ever registered.
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/segment/impl/distributed/segment_directory.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/segment/impl/distributed/segment_directory.py auth_function_line=315 auth_function_name=register_updated_segment_callback
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/segment/impl/distributed/segment_directory.py auth_string_line=52 auth_string_value=Updates the memberlist and calls all registered callbacks. This mocks an update from a k8s CR
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py auth_function_line=485 auth_function_name=auth_request
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py auth_function_line=503 auth_function_name=sync_auth_request
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py auth_function_line=548 auth_function_name=get_user_identity
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py auth_function_line=1549 auth_function_name=auth_and_get_tenant_and_database_for_request
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py auth_function_line=1582 auth_function_name=sync_auth_and_get_tenant_and_database_for_request
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py auth_string_line=481 auth_string_value=auth_request
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py auth_string_line=511 auth_string_value=
        Authenticates and authorizes the request based on the given headers
        and other parameters. If the request cannot be authenticated or cannot
        be authorized (with the configured providers), raises an HTTP 401.
        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py auth_string_line=500 auth_string_value=FastAPI.sync_auth_request
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py auth_string_line=547 auth_string_value=FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py auth_string_line=1545 auth_string_value=auth_and_get_tenant_and_database_for_request_v1
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/server/fastapi/__init__.py auth_string_line=288 auth_string_value=/api/v2/auth/identity
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/telemetry/product/__init__.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/telemetry/product/__init__.py auth_function_line=79 auth_function_name=user_id
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/telemetry/product/__init__.py auth_string_line=51 auth_string_value=telemetry_user_id
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_schema_e2e.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_schema_e2e.py auth_string_line=274 auth_string_value=Sparse embedding function that emits predictable token/value pairs.
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py auth_function_line=30 auth_function_name=register_mock_system
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py auth_string_line=31 auth_string_value=Register a mock system with the given ID and server API.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py auth_string_line=41 auth_string_value=X-Chroma-Token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py auth_string_line=53 auth_string_value=x-chroma-token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py auth_string_line=65 auth_string_value=X-Chroma-Token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py auth_string_line=77 auth_string_value=X-Chroma-Token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py auth_string_line=89 auth_string_value=X-Chroma-Token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py auth_string_line=113 auth_string_value=X-Chroma-Token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py auth_string_line=117 auth_string_value=X-Chroma-Token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py auth_string_line=156 auth_string_value=X-CHROMA-TOKEN
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py auth_string_line=169 auth_string_value=X-Chroma-Token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/api/test_shared_system_client.py auth_string_line=173 auth_string_value=X-Chroma-Token
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/auth/test_auth_utils.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/auth/test_auth_utils.py auth_function_line=10 auth_function_name=user_identity
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/auth/test_auth_utils.py auth_function_line=18 auth_function_name=test_doesnt_overrite_from_auth
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/auth/test_auth_utils.py auth_function_line=54 auth_function_name=test_errors_when_provided_tenant_and_database_dont_match_from_auth
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/auth/test_auth_utils.py auth_function_line=66 auth_function_name=test_doesnt_overrite_from_auth_when_ambiguous
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/auth/test_auth_utils.py auth_string_line=12 auth_string_value=test_user_id
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/create_http_client_with_basic_auth.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/create_http_client_with_basic_auth.py auth_string_line=17 auth_string_value=chromadb.auth.basic_authn.BasicAuthClientProvider
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=12 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=36 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=39 auth_string_value=chromadb.auth.token_authn.TokenAuthClientProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=47 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=49 auth_string_value=Authentication failed
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=58 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=82 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=104 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=126 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=150 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=165 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=180 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=191 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=210 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=236 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=261 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=279 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=294 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=309 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=324 auth_string_value=chromadb.api.fastapi.FastAPI.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=29 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=73 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=96 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=118 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=141 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=227 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=52 auth_string_value=invalid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=160 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=175 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=204 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=256 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=271 auth_string_value=Could not determine a database name from the current authentication method. Please provide a database name.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=273 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=287 auth_string_value=Could not determine a tenant from the current authentication method. Please provide a tenant.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=289 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=302 auth_string_value=Could not determine a database name from the current authentication method. Please provide a database name.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=304 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=317 auth_string_value=Could not determine a database name from the current authentication method. Please provide a database name.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=319 auth_string_value=valid_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=332 auth_string_value=Could not determine a tenant from the current authentication method. Please provide a tenant.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_cloud_client.py auth_string_line=334 auth_string_value=valid_token
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_create_http_client.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_create_http_client.py auth_string_line=4 auth_string_value=chromadb.test.client.create_http_client_with_basic_auth
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_database_tenant_auth.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_database_tenant_auth.py auth_function_line=18 auth_function_name=authenticate_or_raise
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_database_tenant_auth.py auth_function_line=33 auth_function_name=authorize_or_raise
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_database_tenant_auth.py auth_string_line=15 auth_string_value=In practice the tenant would likely be resolved from some other opaque value (e.g. key/token). Here, it's just passed directly as a header for simplicity.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_database_tenant_auth.py auth_string_line=26 auth_string_value=A simple authz provider that asserts the user's tenant matches the resource's tenant.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/client/test_database_tenant_auth.py auth_string_line=43 auth_string_value=Unauthorized
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_function_line=433 auth_function_name=fastapi_server_basic_auth_valid_cred_single_user
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_function_line=452 auth_function_name=fastapi_server_basic_auth_valid_cred_multiple_users
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_function_line=475 auth_function_name=fastapi_server_basic_auth_invalid_cred
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_function_line=490 auth_function_name=fastapi_server_basic_authn_rbac_authz
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_function_line=772 auth_function_name=system_fixtures_auth
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_function_line=780 auth_function_name=system_fixtures_authn_rbac_authz
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_function_line=794 auth_function_name=system_fixtures_wrong_auth
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_function_line=805 auth_function_name=system_wrong_auth
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_function_line=812 auth_function_name=system_authn_rbac_authz
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_function_line=836 auth_function_name=system_auth
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_function_line=1064 auth_function_name=api_with_authn_rbac_authz
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_function_line=1073 auth_function_name=api_with_server_auth
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=1137 auth_string_value=Register custom markers
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=575 auth_string_value=
users:
  - id: admin
    tokens:
      - admin-token
  - id: singleton_user
    tenant: singleton_tenant
    databases:
      - singleton_database
    tokens:
      - singleton-token

auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=444 auth_string_value=chromadb.auth.basic_authn.BasicAuthenticationServerProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=446 auth_string_value=chromadb.auth.basic_authn.BasicAuthClientProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=467 auth_string_value=chromadb.auth.basic_authn.BasicAuthenticationServerProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=469 auth_string_value=chromadb.auth.basic_authn.BasicAuthClientProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=482 auth_string_value=chromadb.auth.basic_authn.BasicAuthenticationServerProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=484 auth_string_value=chromadb.auth.basic_authn.BasicAuthClientProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=560 auth_string_value=chromadb.auth.token_authn.TokenAuthClientProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=561 auth_string_value=admin-token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=573 auth_string_value=.authn
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=593 auth_string_value=chromadb.auth.token_authn.TokenAuthClientProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=594 auth_string_value=admin-token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=595 auth_string_value=chromadb.auth.token_authn.TokenAuthenticationServerProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=500 auth_string_value=.authz
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=537 auth_string_value=chromadb.auth.basic_authn.BasicAuthClientProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=539 auth_string_value=chromadb.auth.basic_authn.BasicAuthenticationServerProvider
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/conftest.py auth_string_line=541 auth_string_value=chromadb.auth.simple_rbac_authz.SimpleRBACAuthorizationProvider
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py auth_function_line=17 auth_function_name=test_comprehensive_tokenization_matches_reference
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py auth_string_line=108 auth_string_value=token_max_length
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py auth_string_line=121 auth_string_value=token_max_length
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_chroma_bm25_embedding_function.py auth_string_line=121 auth_string_value=token_max_length
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_onnx_mini_lm_l6_v2.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_onnx_mini_lm_l6_v2.py auth_route_line=104 auth_route_decorator=patch auth_route_paths=httpx.stream auth_route_function=test_download_functionality
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_onnx_mini_lm_l6_v2.py auth_function_line=98 auth_function_name=test_max_tokens
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/ef/test_onnx_mini_lm_l6_v2.py auth_string_line=99 auth_string_value=Test the max_tokens method.
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/property/test_base64_conversion.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/property/test_base64_conversion.py auth_function_line=11 auth_function_name=test_base64_conversion_is_identity_i8
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/property/test_base64_conversion.py auth_function_line=21 auth_function_name=test_base64_conversion_is_identity_f16
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/property/test_base64_conversion.py auth_function_line=31 auth_function_name=test_base64_conversion_is_identity_f32
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/property/test_base64_conversion.py auth_function_line=41 auth_function_name=test_base64_conversion_is_identity_f64
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/property/test_base64_conversion.py auth_function_line=67 auth_function_name=test_base64_conversion_numpy_is_identity_f32
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/property/test_collections_with_database_tenant_overwrite.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/property/test_collections_with_database_tenant_overwrite.py auth_string_line=187 auth_string_value=singleton-token
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/property/test_cross_version_persist.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/property/test_cross_version_persist.py auth_string_line=41 auth_string_value=tokenizers
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/test_api.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/test_api.py auth_string_line=3800 auth_string_value=author
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/test_api.py auth_string_line=3798 auth_string_value=author
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/test_chroma.py
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/test_chroma.py auth_route_line=13 auth_route_decorator=patch auth_route_paths=chromadb.db.impl.sqlite.SqliteDB auth_route_function=test_default_db
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/test_chroma.py auth_route_line=21 auth_route_decorator=patch auth_route_paths=chromadb.db.impl.sqlite.SqliteDB auth_route_function=test_sqlite_sysdb
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/test_chroma.py auth_route_line=32 auth_route_decorator=patch auth_route_paths=chromadb.db.impl.sqlite.SqliteDB auth_route_function=test_sqlite_queue
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/test_chroma.py auth_route_line=51 auth_route_decorator=patch auth_route_paths=chromadb.api.segment.SegmentAPI auth_route_function=test_local
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/test_chroma.py auth_route_line=60 auth_route_decorator=patch auth_route_paths=chromadb.db.impl.sqlite.SqliteDB auth_route_function=test_local_db
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/test_chroma.py auth_route_line=67 auth_route_decorator=patch auth_route_paths=chromadb.api.fastapi.FastAPI auth_route_function=test_fastapi
auth_route_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/test_chroma.py auth_route_line=81 auth_route_decorator=patch auth_route_paths=chromadb.api.fastapi.FastAPI auth_route_function=test_settings_pass_to_fastapi
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/test_client.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/test_client.py auth_string_line=43 auth_string_value=chromadb.api.client.Client.get_user_identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/test/test_client.py auth_string_line=47 auth_string_value=chromadb.api.async_client.AsyncClient.get_user_identity
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/__init__.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/__init__.py auth_function_line=185 auth_function_name=register_embedding_function
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/__init__.py auth_function_line=217 auth_function_name=register_sparse_embedding_function
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/__init__.py auth_function_line=201 auth_function_name=_register
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/__init__.py auth_function_line=227 auth_function_name=_register
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/__init__.py auth_string_line=218 auth_string_value=Register a custom sparse embedding function.

    Can be used as a decorator:
        @register_sparse_embedding_function
        class MySparseEmbeddingFunction(SparseEmbeddingFunction):
            @classmethod
            def name(cls): return "my_sparse_embedding"
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/__init__.py auth_string_line=304 auth_string_value=register_embedding_function
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/__init__.py auth_string_line=206 auth_string_value=Failed to register embedding function: 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/__init__.py auth_string_line=232 auth_string_value=Failed to register sparse embedding function: 
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/amazon_bedrock_embedding_function.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/amazon_bedrock_embedding_function.py auth_string_line=98 auth_string_value=session_args
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/amazon_bedrock_embedding_function.py auth_string_line=115 auth_string_value=session_args
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/bm25_embedding_function.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/bm25_embedding_function.py auth_string_line=84 auth_string_value=token_max_length
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/bm25_embedding_function.py auth_string_line=182 auth_string_value=token_max_length
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/bm25_embedding_function.py auth_string_line=210 auth_string_value=token_max_length
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_bm25_embedding_function.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_bm25_embedding_function.py auth_string_line=41 auth_string_value=_HashedToken
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_bm25_embedding_function.py auth_string_line=152 auth_string_value=token_max_length
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_bm25_embedding_function.py auth_string_line=153 auth_string_value=include_tokens
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_bm25_embedding_function.py auth_string_line=168 auth_string_value=token_max_length
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_bm25_embedding_function.py auth_string_line=170 auth_string_value=include_tokens
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_bm25_embedding_function.py auth_string_line=142 auth_string_value=token_max_length
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_bm25_embedding_function.py auth_string_line=144 auth_string_value=include_tokens
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_qwen_embedding_function.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_qwen_embedding_function.py auth_string_line=81 auth_string_value=x-chroma-token
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_splade_embedding_function.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_splade_embedding_function.py auth_string_line=65 auth_string_value=
        Cleanup the HTTP client session when the object is destroyed.
        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_splade_embedding_function.py auth_string_line=72 auth_string_value=
        Explicitly close the HTTP client session.
        Call this method when you're done using the embedding function.
        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_splade_embedding_function.py auth_string_line=68 auth_string_value=_session
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_splade_embedding_function.py auth_string_line=76 auth_string_value=_session
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_splade_embedding_function.py auth_string_line=93 auth_string_value=fetch_tokens
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_splade_embedding_function.py auth_string_line=166 auth_string_value=include_tokens
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_splade_embedding_function.py auth_string_line=172 auth_string_value=include_tokens
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_splade_embedding_function.py auth_string_line=59 auth_string_value=x-chroma-token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/chroma_cloud_splade_embedding_function.py auth_string_line=159 auth_string_value=include_tokens
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/cloudflare_workers_ai_embedding_function.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/cloudflare_workers_ai_embedding_function.py auth_string_line=77 auth_string_value=Authorization
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/cloudflare_workers_ai_embedding_function.py auth_string_line=77 auth_string_value=identity
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/huggingface_embedding_function.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/huggingface_embedding_function.py auth_string_line=58 auth_string_value=Authorization
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/huggingface_embedding_function.py auth_string_line=181 auth_string_value=Authorization
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/jina_embedding_function.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/jina_embedding_function.py auth_string_line=109 auth_string_value=Authorization
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/jina_embedding_function.py auth_string_line=109 auth_string_value=identity
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/onnx_mini_lm_l6_v2.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/onnx_mini_lm_l6_v2.py auth_function_line=199 auth_function_name=tokenizer
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/onnx_mini_lm_l6_v2.py auth_function_line=334 auth_function_name=max_tokens
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/onnx_mini_lm_l6_v2.py auth_string_line=200 auth_string_value=
        Get the tokenizer for the model.

        Returns:
            The tokenizer for the model.
        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/onnx_mini_lm_l6_v2.py auth_string_line=288 auth_string_value=special_tokens_map.json
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/onnx_mini_lm_l6_v2.py auth_string_line=289 auth_string_value=tokenizer_config.json
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/onnx_mini_lm_l6_v2.py auth_string_line=290 auth_string_value=tokenizer.json
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/onnx_mini_lm_l6_v2.py auth_string_line=176 auth_string_value=token_type_ids
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/onnx_mini_lm_l6_v2.py auth_string_line=208 auth_string_value=tokenizer.json
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/onnx_mini_lm_l6_v2.py auth_string_line=77 auth_string_value=tokenizers
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/onnx_mini_lm_l6_v2.py auth_string_line=80 auth_string_value=The tokenizers python package is not installed. Please install it with `pip install tokenizers`
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/onnx_mini_lm_l6_v2.py auth_string_line=167 auth_string_value= is greater than the max tokens 
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/schemas/bm25_tokenizer.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/schemas/bm25_tokenizer.py auth_function_line=238 auth_function_name=_simple_tokenize
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/schemas/bm25_tokenizer.py auth_function_line=241 auth_function_name=tokenize
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/schemas/bm25_tokenizer.py auth_string_line=221 auth_string_value=Tokenizer with stopword filtering and stemming used by BM25 embeddings.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/schemas/bm25_tokenizer.py auth_string_line=276 auth_string_value=Bm25Tokenizer
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/together_ai_embedding_function.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/chromadb/utils/embedding_functions/together_ai_embedding_function.py auth_string_line=66 auth_string_value=Authorization
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/click/core.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/click/core.py auth_string_line=617 auth_string_value=Invoke all close callbacks registered with
        :meth:`call_on_close`, and exit all context managers entered
        with :meth:`with_resource`.
        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/click/core.py auth_string_line=629 auth_string_value=Unwind the exit stack by calling its :meth:`__exit__` providing the exception
        information to allow for exception handling by the various resources registered
        using :meth;`with_resource`

        :return: Whatever ``exit_stack.__exit__()`` returns.
        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/click/core.py auth_string_line=731 auth_string_value=Exits the application with a given exit code.

        .. versionchanged:: 8.2
            Callbacks and context managers registered with :meth:`call_on_close`
            and :meth:`with_resource` are closed before exiting.
        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/click/core.py auth_string_line=1623 auth_string_value=Registers another :class:`Command` with this group.  If the name
        is not provided, the name of the command is used.
        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/click/core.py auth_string_line=448 auth_string_value='protected_args' is deprecated and will be removed in Click 9.0. 'args' will contain remaining unparsed tokens.
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/click/shell_completion.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/click/shell_completion.py auth_string_line=214 auth_string_value=Name to register the shell as with :func:`add_completion_class`.
    This is used in completion instructions (``{name}_source`` and
    ``{name}_complete``).
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/click/shell_completion.py auth_string_line=457 auth_string_value=Look up a registered :class:`ShellComplete` subclass by the name
    provided by the completion instruction environment variable. If the
    name isn't registered, returns ``None``.

    :param shell: Name the class is registered under.
    
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/dotenv/ipython.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/dotenv/ipython.py auth_string_line=49 auth_string_value=Register the %dotenv magic.
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/applications.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/applications.py auth_string_line=461 auth_string_value=/docs/oauth2-redirect
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/applications.py auth_string_line=452 auth_string_value=
                The OAuth2 redirect endpoint for the Swagger UI.

                By default it is `/docs/oauth2-redirect`.

                This is only used if you use OAuth2 (with the "Authorize" button)
                with Swagger UI.
                
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/applications.py auth_string_line=465 auth_string_value=
                OAuth2 configuration for the Swagger UI, by default shown at `/docs`.

                Read more about the available configuration options in the
                [Swagger UI docs](https://swagger.io/docs/open-source-tools/swagger-ui/usage/oauth2/).
                
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/dependencies/models.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/dependencies/models.py auth_function_line=54 auth_function_name=oauth_scopes
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/dependencies/utils.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/dependencies/utils.py auth_string_line=570 auth_string_value=non-body parameters must be in path, query, header or cookie: 
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/openapi/docs.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/openapi/docs.py auth_function_line=301 auth_function_name=get_swagger_ui_oauth2_redirect_html
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/openapi/docs.py auth_string_line=302 auth_string_value=
    Generate the HTML response with the OAuth2 redirection for Swagger UI.

    You normally don't need to use or change this.
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/openapi/docs.py auth_string_line=175 auth_string_value=oauth2RedirectUrl: window.location.origin + '
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/openapi/docs.py auth_string_line=185 auth_string_value=
        ui.initOAuth(
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/openapi/docs.py auth_string_line=104 auth_string_value=
            The OAuth2 redirect URL, it is normally automatically handled by FastAPI.

            Read more about it in the
            [FastAPI docs for Custom Docs UI Static Assets](https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/)
            
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/openapi/docs.py auth_string_line=115 auth_string_value=
            A dictionary with Swagger UI OAuth2 initialization configurations.

            Read more about the available configuration options in the
            [Swagger UI docs](https://swagger.io/docs/open-source-tools/swagger-ui/usage/oauth2/).
            
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/openapi/models.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/openapi/models.py auth_string_line=225 auth_string_value=cookie
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/openapi/models.py auth_string_line=324 auth_string_value=oauth2
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/openapi/models.py auth_string_line=336 auth_string_value=cookie
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/param_functions.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/param_functions.py auth_function_line=1019 auth_function_name=Cookie
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/params.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/params.py auth_string_line=24 auth_string_value=cookie
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/routing.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/routing.py auth_function_line=137 auth_function_name=websocket_session
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/routing.py auth_string_line=140 auth_string_value=
    Takes a coroutine `func(session)`, and returns an ASGI application.
    
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/api_key.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/api_key.py auth_function_line=29 auth_function_name=make_not_authenticated_error
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/api_key.py auth_string_line=41 auth_string_value=Not authenticated
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/api_key.py auth_string_line=42 auth_string_value=WWW-Authenticate
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/api_key.py auth_string_line=268 auth_string_value=Cookie name.
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_function_line=84 auth_function_name=make_authenticate_headers
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_function_line=87 auth_function_name=make_not_authenticated_error
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_function_line=197 auth_function_name=make_authenticate_headers
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_string_line=17 auth_string_value=
    The HTTP Basic credentials given as the result of using `HTTPBasic` in a
    dependency.

    Read more about it in the
    [FastAPI docs for HTTP Basic Auth](https://fastapi.tiangolo.com/advanced/security/http-basic-auth/).
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_string_line=85 auth_string_value=WWW-Authenticate
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_string_line=95 auth_string_value=Authorization
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_string_line=200 auth_string_value=WWW-Authenticate
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_string_line=205 auth_string_value=Authorization
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_string_line=304 auth_string_value=Authorization
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_string_line=405 auth_string_value=Authorization
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_string_line=54 auth_string_value=
            The HTTP authorization scheme extracted from the header value.
            
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_string_line=62 auth_string_value=
            The HTTP authorization credentials extracted from the header value.
            
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_string_line=90 auth_string_value=Not authenticated
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_string_line=199 auth_string_value=WWW-Authenticate
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_string_line=156 auth_string_value=
                HTTP Basic authentication realm.
                
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/http.py auth_string_line=257 auth_string_value=Bearer token format.
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_function_line=401 auth_function_name=make_not_authenticated_error
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=434 auth_string_value=
    OAuth2 flow for authentication using a bearer token obtained with a password.
    An instance of it would be used as a dependency.

    Read more about it in the
    [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=548 auth_string_value=
    OAuth2 flow for authentication using a bearer token obtained with an OAuth2 code
    flow. An instance of it would be used as a dependency.
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=424 auth_string_value=Authorization
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=537 auth_string_value=Authorization
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=643 auth_string_value=Authorization
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=419 auth_string_value=Not authenticated
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=420 auth_string_value=WWW-Authenticate
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=688 auth_string_value=
                All the scopes required by all the dependencies in a single string
                separated by spaces, as defined in the OAuth2 specification.
                
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=134 auth_string_value=
                If there's a `client_id`, it can be sent as part of the form fields.
                But the OAuth2 specification recommends sending the `client_id` and
                `client_secret` (if any) using HTTP Basic auth.
                
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=145 auth_string_value=
                If there's a `client_password` (and a `client_id`), they can be sent
                as part of the form fields. But the OAuth2 specification recommends
                sending the `client_id` and `client_secret` (if any) using HTTP Basic
                auth.
                
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=300 auth_string_value=
                If there's a `client_id`, it can be sent as part of the form fields.
                But the OAuth2 specification recommends sending the `client_id` and
                `client_secret` (if any) using HTTP Basic auth.
                
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=311 auth_string_value=
                If there's a `client_password` (and a `client_id`), they can be sent
                as part of the form fields. But the OAuth2 specification recommends
                sending the `client_id` and `client_secret` (if any) using HTTP Basic
                auth.
                
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=349 auth_string_value=
                The dictionary of OAuth2 flows.
                
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=511 auth_string_value=
                The URL to refresh the token and obtain a new one.
                
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=523 auth_string_value=tokenUrl
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=559 auth_string_value=
                The URL to obtain the OAuth2 token.
                
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=567 auth_string_value=
                The URL to refresh the token and obtain a new one.
                
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=585 auth_string_value=
                The OAuth2 scopes that would be required by the *path operations* that
                use this dependency.
                
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=628 auth_string_value=authorizationUrl
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/oauth2.py auth_string_line=629 auth_string_value=tokenUrl
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/open_id_connect_url.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/open_id_connect_url.py auth_function_line=80 auth_function_name=make_not_authenticated_error
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/open_id_connect_url.py auth_string_line=88 auth_string_value=Authorization
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/open_id_connect_url.py auth_string_line=83 auth_string_value=Not authenticated
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/open_id_connect_url.py auth_string_line=84 auth_string_value=WWW-Authenticate
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/utils.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fastapi/security/utils.py auth_function_line=1 auth_function_name=get_authorization_scheme_param
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/__init__.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/__init__.py auth_string_line=22 auth_string_value=register_implementation
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/__init__.py auth_string_line=24 auth_string_value=get_fs_token_paths
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/asyn.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/asyn.py auth_string_line=148 auth_string_value=register_at_fork
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/caching.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/caching.py auth_function_line=974 auth_function_name=register_cache
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/caching.py auth_string_line=975 auth_string_value='Register' cache implementation.

    Parameters
    ----------
    clobber: bool, optional
        If set to True (default is False) - allow to overwrite existing
        entry.

    Raises
    ------
    ValueError
    
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/compression.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/compression.py auth_function_line=19 auth_function_name=register_compression
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/core.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/core.py auth_function_line=632 auth_function_name=get_fs_token_paths
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/gui.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/gui.py auth_function_line=49 auth_function_name=_register
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/gui.py auth_string_line=45 auth_string_value=Create GUI elements and register signals
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/dbfs.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/dbfs.py auth_string_line=58 auth_string_value=Authorization
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/dirfs.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/dirfs.py auth_function_line=85 auth_function_name=set_session
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/gist.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/gist.py auth_string_line=67 auth_string_value=Auth parameters passed to 'requests' if we have username/token.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/gist.py auth_string_line=143 auth_string_value=
        Parse 'gist://' style URLs into GistFileSystem constructor kwargs.
        For example:
          gist://:TOKEN@<gist_id>/file.txt
          gist://username:TOKEN@<gist_id>/file.txt
        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/gist.py auth_string_line=55 auth_string_value=User auth requires a token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/gist.py auth_string_line=76 auth_string_value=auth
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/gist.py auth_string_line=154 auth_string_value=token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/gist.py auth_string_line=78 auth_string_value=Authorization
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/github.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/github.py auth_string_line=51 auth_string_value=Auth required both username and token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/github.py auth_string_line=77 auth_string_value=auth
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/github.py auth_string_line=291 auth_string_value=Authentication required
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/http.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/http.py auth_function_line=122 auth_function_name=close_session
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/http.py auth_function_line=134 auth_function_name=set_session
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/http.py auth_string_line=840 auth_string_value=Call HEAD on the server to get details about the file (size/checksum etc.)

    Default operation is to explicitly allow redirects and use encoding
    'identity' (no compression) to get the true size of the target.
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/http.py auth_string_line=849 auth_string_value=identity
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/http.py auth_string_line=866 auth_string_value=identity
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/http_sync.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/http_sync.py auth_function_line=923 auth_function_name=register
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/http_sync.py auth_function_line=933 auth_function_name=unregister
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/http_sync.py auth_string_line=880 auth_string_value=Call HEAD on the server to get details about the file (size/checksum etc.)

    Default operation is to explicitly allow redirects and use encoding
    'identity' (no compression) to get the true size of the target.
    
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/http_sync.py auth_string_line=252 auth_string_value=Starting JS session
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/http_sync.py auth_string_line=258 auth_string_value=Starting cpython session because of: %s
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/jupyter.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/jupyter.py auth_string_line=37 auth_string_value=Authorization
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/jupyter.py auth_string_line=37 auth_string_value=token 
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/jupyter.py auth_string_line=30 auth_string_value=token=([a-z0-9]+)
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/jupyter.py auth_string_line=32 auth_string_value=Could not determine token
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/smb.py
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/smb.py auth_string_line=140 auth_string_value=register_session_retry_wait must be a non-negative integer
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/smb.py auth_string_line=145 auth_string_value=register_session_retry_factor must be a positive integer equal to or greater than 1
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_function_line=322 auth_function_name=get_delegation_token
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_function_line=339 auth_function_name=renew_delegation_token
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_function_line=344 auth_function_name=cancel_delegation_token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_string_line=323 auth_string_value=Retrieve token which can give the same authority to other uses

        Parameters
        ----------
        renewer: str or None
            User who may use this token; if None, will be current user
        
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_string_line=340 auth_string_value=Make token live longer. Returns new expiry time
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_string_line=345 auth_string_value=Stop the token from being useful
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_string_line=334 auth_string_value=Token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_string_line=341 auth_string_value=RENEWDELEGATIONTOKEN
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_string_line=346 auth_string_value=CANCELDELEGATIONTOKEN
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_string_line=136 auth_string_value=If using Kerberos auth, do not specify the user, this is handled by kinit.
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_string_line=331 auth_string_value=GETDELEGATIONTOKEN
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_string_line=333 auth_string_value=GETDELEGATIONTOKEN
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_string_line=336 auth_string_value=No token available for this user/security context
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_string_line=114 auth_string_value=If passing a delegation token, must not set user or proxy_to, as these are encoded in the token
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/implementations/webhdfs.py auth_string_line=125 auth_string_value=If passing a password, the user must also beset in order to set up the basic-auth
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/registry.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/registry.py auth_function_line=17 auth_function_name=register_implementation
auth_source_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/spec.py
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/spec.py auth_function_line=177 auth_function_name=_fs_token
auth_function_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/spec.py auth_function_line=180 auth_function_name=__dask_tokenize__
auth_string_file=/mnt/spiritual_drive/msjarvis-rebuild/.check_venv/lib/python3.12/site-packages/fsspec/spec.py auth_string_line=171 auth_string_value=Persistent filesystem id that can be used to compare filesystems
        across sessions.
        
report_sha256=sha256:764a5db44c7cfce314e62ecddf1a2f7607f0f8604a2e49d94efce0b67d550624
report_path=/home/cakidd/msjarvis-pilot-build-evidence-20260810/host-gunicorn-auth-discovery-20260811.json
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-guardian-deploy-candidate-e8827b2$ 

