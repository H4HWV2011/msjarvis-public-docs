(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # Find the actual query endpoint
grep -n "^@app\.\(post\|get\|api_route\)" \
  /opt/msjarvis-rebuild/msjarvis-rebuild/ms_jarvis_unified_gateway.py | head -30
604:@app.api_route("/constitutional/{path:path}", methods=["GET","POST","PUT","DELETE","PATCH"])
685:@app.api_route("/memory/{path:path}", methods=["GET","POST","DELETE"])
713:@app.post("/feedback")
732:@app.get("/feedback/summary")
815:@app.api_route("/brain/{path:path}",            methods=["GET","POST","PUT","DELETE","PATCH"])
819:@app.api_route("/steward/{path:path}",          methods=["GET","POST","PUT","DELETE","PATCH"])
822:@app.api_route("/dao/mountainshares/{path:path}",methods=["GET","POST","PUT","DELETE","PATCH"])
825:@app.api_route("/dao/governance/{path:path}",   methods=["GET","POST","PUT","DELETE","PATCH"])
828:@app.api_route("/dao/commons/{path:path}",      methods=["GET","POST","PUT","DELETE","PATCH"])
831:@app.api_route("/dao/stakes/{path:path}",       methods=["GET","POST","PUT","DELETE","PATCH"])
834:@app.api_route("/dao/tokens/{path:path}",       methods=["GET","POST","PUT","DELETE","PATCH"])
837:@app.api_route("/gbim/{path:path}",             methods=["GET","POST","PUT","DELETE","PATCH"])
841:@app.api_route("/gis/rag/{path:path}",            methods=["GET","POST","PUT","DELETE","PATCH"])
843:@app.api_route("/gis/{path:path}",              methods=["GET","POST","PUT","DELETE","PATCH"])
847:@app.api_route("/neuro/eeg/delta/{path:path}",    methods=["GET","POST","PUT","DELETE","PATCH"])
850:@app.api_route("/neuro/eeg/theta/{path:path}",    methods=["GET","POST","PUT","DELETE","PATCH"])
853:@app.api_route("/neuro/eeg/beta/{path:path}",     methods=["GET","POST","PUT","DELETE","PATCH"])
857:@app.api_route("/hippocampus/{path:path}",        methods=["GET","POST","PUT","DELETE","PATCH"])
860:@app.api_route("/llm/consensus/{path:path}",      methods=["GET","POST","PUT","DELETE","PATCH"])
863:@app.api_route("/judge/pipeline/{path:path}",     methods=["GET","POST","PUT","DELETE","PATCH"])
866:@app.api_route("/local/{path:path}",              methods=["GET","POST","PUT","DELETE","PATCH"])
869:@app.api_route("/brain/orchestrator/{path:path}", methods=["GET","POST","PUT","DELETE","PATCH"])
872:@app.api_route("/psych/rag/{path:path}",          methods=["GET","POST","PUT","DELETE","PATCH"])
875:@app.api_route("/research/{path:path}",         methods=["GET","POST","PUT","DELETE","PATCH"])
879:@app.api_route("/policy/crypto/{path:path}",    methods=["GET","POST","PUT","DELETE","PATCH"])
912:@app.api_route("/llm/production/{path:path}", methods=["GET","POST","PUT","DELETE","PATCH"])
916:@app.api_route("/llm/synthesizer/{path:path}", methods=["GET","POST","PUT","DELETE","PATCH"])
920:@app.api_route("/llm/intake/{path:path}", methods=["GET","POST","PUT","DELETE","PATCH"])
924:@app.api_route("/consciousness/bridge/{path:path}", methods=["GET","POST","PUT","DELETE","PATCH"])
928:@app.api_route("/consciousness/fractal/{path:path}", methods=["GET","POST","PUT","DELETE","PATCH"])
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ curl -sf http://127.0.0.1:8001/chat \
  -X POST -H "Content-Type: application/json" \
  -d '{"query": "ADHD resources in Fayette County", "user_id": "carrie_kidd"}' \ 
  | python3 -m json.tool | head -40
Expecting value: line 1 column 1 (char 0)
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # See exactly what's around lines 218-235
sed -n '210,245p' \
  /opt/msjarvis-rebuild/msjarvis-rebuild/ms_jarvis_unified_gateway.py
    async def process_unified(self, message: str, user_id: str = "anonymous", role: str = "guest") -> Dict[str, Any]:
        """Process through complete system"""
        self.total_queries += 1
        start_time = datetime.now()
        
        async with httpx.AsyncClient(timeout=None) as client:
            pipeline = {"query": message, "user_id": user_id}
            
            # Try Blood-Brain Barrier
            try:
                bbb_resp = await client.post(
                    f"{self.services['blood_brain_barrier']}/filter",
                    json={"content": message},
                    timeout=10.0
                )
                pipeline["bbb"] = bbb_resp.json()
                
                if not pipeline["bbb"].get("content_approved", True):
                    return {"status": "blocked", "reason": "Ethical filter", "details": pipeline["bbb"]}
                    
                logger.info("✅ BBB: Approved")
            except:
                logger.warning("⚠️  BBB bypassed")
                pipeline["bbb"] = {"status": "bypassed"}
            
            # M-18: Constitutional audit endpoint — March 29 2026
            try:
                _cg_url = os.environ.get("CONSTITUTIONAL_GUARDIAN_URL",
                                         "http://jarvis-constitutional-guardian:8091")
                _ca = await client.post(
                    f"{_cg_url}/constitutional/check",
                    json={
                        "content":    message,
                        "user_id":    user_id,
                        "actor_role": role,
                        "action_type": "chat",
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # See the full Caddyfile
cat /etc/caddy/Caddyfile

# What port is Next.js actually on?
ss -tlnp | grep -E "3000|3001|8090"

# Can we hit Next.js directly?
curl -sf http://127.0.0.1:3001/ | head -5 || \
curl -sf http://127.0.0.1:3000/ | head -5
{
	http_port 80
	https_port 8443
	auto_https off
}

:80, :8443 {
	header {
		Access-Control-Allow-Origin "*"
		Access-Control-Allow-Methods "GET, POST, OPTIONS, DELETE, PUT"
		Access-Control-Allow-Headers "Authorization, Content-Type, X-API-Key"
		Access-Control-Max-Age "3600"
	}

	@chat_rate path /chat*
	rate_limit @chat_rate {
		zone chat_zone {
			key {remote_host}
			events 60
			window 1m
		}
	}

	handle /api/chat* {
		reverse_proxy 127.0.0.1:3001
	}

	handle /chat* {
		reverse_proxy 127.0.0.1:8001 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-Api-Key}
			transport http {
				read_buffer 16384
				response_header_timeout 300s
				dial_timeout 10s
			}
		}
	}

	handle /constitutional* {
		reverse_proxy 127.0.0.1:18018 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}

	handle /bbb-audit* {
		reverse_proxy 127.0.0.1:18018 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
		}
	}

	# Admin + registration endpoints → auth_router on :8095
	handle /auth/register {
		reverse_proxy 127.0.0.1:8095
	}
	handle /auth/applications/* {
		reverse_proxy 127.0.0.1:8095
	}
	handle /auth/applications {
		reverse_proxy 127.0.0.1:8095
	}
	handle /auth/approve/* {
		reverse_proxy 127.0.0.1:8095
	}
	handle /auth/deny/* {
		reverse_proxy 127.0.0.1:8095
	}
	handle /auth/first-login {
		reverse_proxy 127.0.0.1:8095
	}
	handle /auth/me {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up Cookie {http.request.header.Cookie}
		}
	}
	handle /auth/logout {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up Cookie {http.request.header.Cookie}
		}
	}
	handle /auth/token* {
		reverse_proxy 127.0.0.1:8095
	}

	handle /auth/portal/* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up Cookie {http.request.header.Cookie}
		}
	}

	handle /auth* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-API-Key}
			header_up Cookie {http.request.header.Cookie}
		}
	}

	handle /health* {
		reverse_proxy 127.0.0.1:8001
	}

	handle /systems* {
		reverse_proxy 127.0.0.1:18018
	}

	handle {
		reverse_proxy 127.0.0.1:3001
	}

	encode gzip

	log {
		output file /var/log/caddy/caddy_access.log
		format json
	}
}

:8090 {
	bind 127.0.0.1
	root * /opt/msjarvis-rebuild/ui
	file_server
	encode gzip
	log {
		output file /var/log/caddy/caddy_dashboard.log
		format json
	}
}

egeria.mountainshares.us {
	header {
		Access-Control-Allow-Origin "*"
		Access-Control-Allow-Methods "GET, POST, OPTIONS, DELETE, PUT"
		Access-Control-Allow-Headers "Authorization, Content-Type, X-API-Key"
		Access-Control-Max-Age "3600"
	}

	handle /api/chat* {
		reverse_proxy 127.0.0.1:3001
	}

	handle /chat_wv {
		reverse_proxy 127.0.0.1:8010 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-User-Id {http.request.header.X-User-Id}
			transport http {
				read_buffer 16384
				response_header_timeout 600s
				dial_timeout 10s
			}
		}
	}

	handle /chat* {
		reverse_proxy 127.0.0.1:8001 {
			header_up Authorization {http.request.header.Authorization}
			header_up X-API-Key {http.request.header.X-Api-Key}
			transport http {
				read_buffer 16384
				response_header_timeout 600s
				dial_timeout 10s
			}
		}
	}

	# Admin + registration endpoints → auth_router on :8095
	handle /auth/register {
		reverse_proxy 127.0.0.1:8095
	}
	handle /auth/applications/* {
		reverse_proxy 127.0.0.1:8095
	}
	handle /auth/applications {
		reverse_proxy 127.0.0.1:8095
	}
	handle /auth/approve/* {
		reverse_proxy 127.0.0.1:8095
	}
	handle /auth/deny/* {
		reverse_proxy 127.0.0.1:8095
	}
	handle /auth/first-login {
		reverse_proxy 127.0.0.1:8095
	}
	handle /auth/portal/* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up Cookie {http.request.header.Cookie}
		}
	}
	handle /auth/me {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up Cookie {http.request.header.Cookie}
		}
	}
	handle /auth/logout {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up Cookie {http.request.header.Cookie}
		}
	}

	handle /auth* {
		reverse_proxy 127.0.0.1:8095 {
			header_up Authorization {http.request.header.Authorization}
			header_up Cookie {http.request.header.Cookie}
		}
	}

	handle {
		reverse_proxy 127.0.0.1:3001
	}

	encode gzip
	log {
		output file /var/log/caddy/caddy_allis.log
		format json
	}
}
LISTEN 0      4096       127.0.0.1:8090       0.0.0.0:*                                                 
LISTEN 0      511                *:3001             *:*    users:(("next-server (v1",pid=3761274,fd=18))
<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/><link rel="preload" as="image" imageSrcSet="/_next/image?url=%2Fms-allis.jpg&amp;w=16&amp;q=75 16w, /_next/image?url=%2Fms-allis.jpg&amp;w=32&amp;q=75 32w, /_next/image?url=%2Fms-allis.jpg&amp;w=48&amp;q=75 48w, /_next/image?url=%2Fms-allis.jpg&amp;w=64&amp;q=75 64w, /_next/image?url=%2Fms-allis.jpg&amp;w=96&amp;q=75 96w, /_next/image?url=%2Fms-allis.jpg&amp;w=128&amp;q=75 128w, /_next/image?url=%2Fms-allis.jpg&amp;w=256&amp;q=75 256w, /_next/image?url=%2Fms-allis.jpg&amp;w=384&amp;q=75 384w, /_next/image?url=%2Fms-allis.jpg&amp;w=640&amp;q=75 640w, /_next/image?url=%2Fms-allis.jpg&amp;w=750&amp;q=75 750w, /_next/image?url=%2Fms-allis.jpg&amp;w=828&amp;q=75 828w, /_next/image?url=%2Fms-allis.jpg&amp;w=1080&amp;q=75 1080w, /_next/image?url=%2Fms-allis.jpg&amp;w=1200&amp;q=75 1200w, /_next/image?url=%2Fms-allis.jpg&amp;w=1920&amp;q=75 1920w, /_next/image?url=%2Fms-allis.jpg&amp;w=2048&amp;q=75 2048w, /_next/image?url=%2Fms-allis.jpg&amp;w=3840&amp;q=75 3840w" imageSizes="(max-width: 768px) 320px, (max-width: 1024px) 420px, 480px" fetchPriority="high"/><link rel="stylesheet" href="/_next/static/css/29f1d71aa19ee44c.css" data-precedence="next"/><link rel="preload" as="script" fetchPriority="low" href="/_next/static/chunks/webpack-1ea540f0e26c2248.js"/><script src="/_next/static/chunks/fd9d1056-b3e22152f23ae9ca.js" async=""></script><script src="/_next/static/chunks/117-506865e2681b6c3b.js" async=""></script><script src="/_next/static/chunks/main-app-10b1772d4e9542a6.js" async=""></script><script src="/_next/static/chunks/609-09c674f61ad8c961.js" async=""></script><script src="/_next/static/chunks/app/page-f5b3c5a76f31235e.js" async=""></script><title>Ms. Allis — MountainShares Artificial Learning &amp; Location Intelligence System</title><meta name="description" content="An Appalachian-rooted AI assistant, built and stewarded in Mount Hope, West Virginia, by Harmony for Hope, Inc."/><meta property="og:title" content="Ms. Allis"/><meta property="og:description" content="Appalachian community AI from Mount Hope, West Virginia."/><meta property="og:image" content="https://msallis.h4h.org/ms-allis.jpg"/><meta name="twitter:card" content="summary_large_image"/><meta name="twitter:title" content="Ms. Allis"/><meta name="twitter:description" content="Appalachian community AI from Mount Hope, West Virginia."/><meta name="twitter:image" content="https://msallis.h4h.org/ms-allis.jpg"/><script src="/_next/static/chunks/polyfills-42372ed130431b0a.js" noModule=""></script></head><body><main class="min-h-screen flex flex-col"><section class="relative pt-12 pb-20 md:pt-20 md:pb-32 overflow-hidden"><div aria-hidden="true" class="absolute inset-0 bg-halo opacity-100 pointer-events-none"></div><div class="relative max-w-6xl mx-auto px-6 md:px-10"><div class="animate-fade-in mb-12 md:mb-16"><div class="flex items-center justify-center gap-3 text-terracotta"><svg viewBox="0 0 24 24" class="w-3 h-3 opacity-40" aria-hidden="true" fill="currentColor" stroke="currentColor" stroke-width="0" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z"></path><path d="M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z" fill="rgba(0,0,0,0.18)"></path></svg><svg viewBox="0 0 24 24" class="w-4 h-4 opacity-60" aria-hidden="true" fill="currentColor" stroke="currentColor" stroke-width="0" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z"></path><path d="M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z" fill="rgba(0,0,0,0.18)"></path></svg><svg viewBox="0 0 24 24" class="w-5 h-5 opacity-100" aria-hidden="true" fill="currentColor" stroke="currentColor" stroke-width="0" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z"></path><path d="M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z" fill="rgba(0,0,0,0.18)"></path></svg><svg viewBox="0 0 24 24" class="w-4 h-4 opacity-60" aria-hidden="true" fill="currentColor" stroke="currentColor" stroke-width="0" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z"></path><path d="M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z" fill="rgba(0,0,0,0.18)"></path></svg><svg viewBox="0 0 24 24" class="w-3 h-3 opacity-40" aria-hidden="true" fill="currentColor" stroke="currentColor" stroke-width="0" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z"></path><path d="M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z" fill="rgba(0,0,0,0.18)"></path></svg></div></div><div class="grid md:grid-cols-12 gap-10 md:gap-16 items-center"><div class="md:col-span-5 flex justify-center md:justify-start animate-fade-in-up"><div class="relative inline-block max-w-full " style="max-width:640px"><div class="relative bg-terracotta-deep p-2 shadow-warm-lg"><div class="bg-cream-light p-1.5"><img alt="Ms. Allis — folk-art portrait" fetchPriority="high" width="640" height="640" decoding="async" data-nimg="1" class="block w-full h-auto object-cover" style="color:transparent" sizes="(max-width: 768px) 320px, (max-width: 1024px) 420px, 480px" srcSet="/_next/image?url=%2Fms-allis.jpg&amp;w=16&amp;q=75 16w, /_next/image?url=%2Fms-allis.jpg&amp;w=32&amp;q=75 32w, /_next/image?url=%2Fms-allis.jpg&amp;w=48&amp;q=75 48w, /_next/image?url=%2Fms-allis.jpg&amp;w=64&amp;q=75 64w, /_next/image?url=%2Fms-allis.jpg&amp;w=96&amp;q=75 96w, /_next/image?url=%2Fms-allis.jpg&amp;w=128&amp;q=75 128w, /_next/image?url=%2Fms-allis.jpg&amp;w=256&amp;q=75 256w, /_next/image?url=%2Fms-allis.jpg&amp;w=384&amp;q=75 384w, /_next/image?url=%2Fms-allis.jpg&amp;w=640&amp;q=75 640w, /_next/image?url=%2Fms-allis.jpg&amp;w=750&amp;q=75 750w, /_next/image?url=%2Fms-allis.jpg&amp;w=828&amp;q=75 828w, /_next/image?url=%2Fms-allis.jpg&amp;w=1080&amp;q=75 1080w, /_next/image?url=%2Fms-allis.jpg&amp;w=1200&amp;q=75 1200w, /_next/image?url=%2Fms-allis.jpg&amp;w=1920&amp;q=75 1920w, /_next/image?url=%2Fms-allis.jpg&amp;w=2048&amp;q=75 2048w, /_next/image?url=%2Fms-allis.jpg&amp;w=3840&amp;q=75 3840w" src="/_next/image?url=%2Fms-allis.jpg&amp;w=3840&amp;q=75"/></div></div></div></div><div class="md:col-span-7 animate-fade-in-up" style="animation-delay:0.15s"><div class="inline-flex items-center gap-3 mb-6 text-terracotta"><span class="h-px w-8 bg-terracotta"></span><span class="font-display italic text-sm tracking-widest uppercase">Mount Hope · West Virginia</span></div><h1 class="font-display text-hero text-teal-deep mb-8"><span class="block italic font-light text-gold-deep">meet</span>Ms. Allis<span class="text-terracotta">.</span></h1><p class="font-body text-xl md:text-2xl leading-relaxed text-ink-soft mb-3 max-w-xl">The MountainShares Artificial Learning &amp; Location Intelligence System.</p><p class="font-body text-base md:text-lg leading-relaxed text-ink-soft mb-10 max-w-xl">An AI rooted in Appalachia. Built and stewarded by<!-- --> <a href="https://www.harmonyforhopewv.org" class="text-terracotta underline decoration-terracotta/40 underline-offset-4 hover:decoration-terracotta transition-colors" target="_blank" rel="noopener noreferrer">Harmony for Hope, Inc.</a>, a 501(c)(3) nonprofit in Mount Hope, West Virginia. Currently in Phase 0 invite-only beta with<!-- --> <span class="text-teal-deep font-medium">Community Champions</span> <!-- -->from across all 55 counties.</p><div class="flex flex-wrap items-center gap-4"><a class="btn-primary group" href="/apply"><svg viewBox="0 0 24 24" class="w-4 h-4 group-hover:scale-110 transition-transform" aria-hidden="true" fill="currentColor" stroke="currentColor" stroke-width="0" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z"></path><path d="M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z" fill="rgba(0,0,0,0.18)"></path></svg>Apply to be a Champion</a><a class="font-body text-base text-ink-soft hover:text-teal underline decoration-cream-deep underline-offset-4 hover:decoration-teal transition-colors" href="/portal">Already a Champion? Sign in</a></div></div></div></div></section><div class="flex justify-center py-8"><svg viewBox="0 0 80 24" class="w-32 text-gold" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><path d="M5 12 Q15 12 20 6 Q25 0 35 6 Q40 9 40 12"></path><path d="M75 12 Q65 12 60 6 Q55 0 45 6 Q40 9 40 12"></path><circle cx="40" cy="12" r="2" fill="currentColor"></circle><path d="M20 6 Q19 4 17 4"></path><path d="M60 6 Q61 4 63 4"></path></g></svg></div><section class="py-20 md:py-28 bg-cream-light/40"><div class="max-w-4xl mx-auto px-6 md:px-10"><div class="text-center mb-16"><h2 class="font-display italic text-display text-teal-deep mb-4">Who is Ms. Allis?</h2><div class="divider-hearts max-w-md mx-auto"><svg viewBox="0 0 24 24" class="w-3 h-3" aria-hidden="true" fill="currentColor" stroke="currentColor" stroke-width="0" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z"></path><path d="M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z" fill="rgba(0,0,0,0.18)"></path></svg></div></div><div class="grid md:grid-cols-2 gap-12 md:gap-16"><div><div class="inline-block px-3 py-1 mb-4 font-display italic text-xs uppercase tracking-widest text-terracotta border border-terracotta/30">Place-bound</div><p class="font-body text-lg leading-relaxed text-ink-soft">Ms. Allis is grounded in West Virginia — every belief she holds is anchored to a place, a time, a source. She knows the difference between Fayette County and Fayetteville. She knows which fire station serves your hollow. She knows the parcels, the EMS response zones, the historic markers, the food pantries.</p></div><div><div class="inline-block px-3 py-1 mb-4 font-display italic text-xs uppercase tracking-widest text-forest-deep border border-forest/30">Stewarded</div><p class="font-body text-lg leading-relaxed text-ink-soft">She is not a product. She is community infrastructure — built by a Quaker-rooted nonprofit with a 346-year heritage of stewardship, governed transparently, and accountable to the people she serves. Her conversations belong to you. Her code is yours to inspect.</p></div><div><div class="inline-block px-3 py-1 mb-4 font-display italic text-xs uppercase tracking-widest text-gold-deep border border-gold/40">Verified</div><p class="font-body text-lg leading-relaxed text-ink-soft">Twenty-one language models reach consensus on every answer. Five judges check for accuracy and harm. Truth-filter validators check for hallucination. The pipeline is transparent and the audit log is permanent.</p></div><div><div class="inline-block px-3 py-1 mb-4 font-display italic text-xs uppercase tracking-widest text-teal-mid border border-teal/30">Yours</div><p class="font-body text-lg leading-relaxed text-ink-soft">Champions receive a unique ecosystem identifier (UEID), a custodial Arbitrum wallet, and the ability to earn MountainShares through community contribution. Phase 0 is small and careful by design — we&#x27;d rather grow slowly and well.</p></div></div></div></section><section class="py-20 md:py-28"><div class="max-w-3xl mx-auto px-6 md:px-10 text-center"><div class="flex items-center justify-center gap-3 text-terracotta mb-8"><svg viewBox="0 0 24 24" class="w-3 h-3 opacity-40" aria-hidden="true" fill="currentColor" stroke="currentColor" stroke-width="0" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z"></path><path d="M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z" fill="rgba(0,0,0,0.18)"></path></svg><svg viewBox="0 0 24 24" class="w-4 h-4 opacity-60" aria-hidden="true" fill="currentColor" stroke="currentColor" stroke-width="0" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z"></path><path d="M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z" fill="rgba(0,0,0,0.18)"></path></svg><svg viewBox="0 0 24 24" class="w-5 h-5 opacity-100" aria-hidden="true" fill="currentColor" stroke="currentColor" stroke-width="0" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z"></path><path d="M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z" fill="rgba(0,0,0,0.18)"></path></svg><svg viewBox="0 0 24 24" class="w-4 h-4 opacity-60" aria-hidden="true" fill="currentColor" stroke="currentColor" stroke-width="0" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z"></path><path d="M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z" fill="rgba(0,0,0,0.18)"></path></svg><svg viewBox="0 0 24 24" class="w-3 h-3 opacity-40" aria-hidden="true" fill="currentColor" stroke="currentColor" stroke-width="0" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z"></path><path d="M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z" fill="rgba(0,0,0,0.18)"></path></svg></div><h2 class="font-display italic text-display text-teal-deep mb-6">Want to help?</h2><p class="font-body text-lg md:text-xl leading-relaxed text-ink-soft mb-10 max-w-2xl mx-auto">Phase 0 Champions test the system, find what&#x27;s broken, and shape what it becomes. Application takes about ten minutes. We read every one personally.</p><a class="btn-terracotta" href="/apply">Apply to be a Champion</a></div></section><footer class="mt-auto relative"><svg viewBox="0 0 1200 200" class="w-full h-32 md:h-40 text-forest" preserveAspectRatio="none" aria-hidden="true"><path d="M0,200 L0,140 L80,90 L160,120 L240,75 L340,110 L440,60 L540,95 L640,55 L740,100 L840,70 L940,105 L1040,65 L1140,95 L1200,80 L1200,200 Z" fill="currentColor" opacity="0.35"></path><path d="M0,200 L0,170 L100,130 L200,150 L320,115 L420,140 L520,110 L640,135 L760,105 L880,138 L1000,108 L1100,130 L1200,118 L1200,200 Z" fill="currentColor" opacity="0.65"></path><g fill="currentColor" opacity="0.85"><path d="M60,200 L60,165 L50,170 L60,150 L52,155 L60,135 L68,155 L60,150 L70,170 L60,165 L60,200 Z"></path><path d="M180,200 L180,158 L168,164 L180,140 L170,146 L180,122 L190,146 L180,140 L192,164 L180,158 L180,200 Z"></path><path d="M340,200 L340,170 L332,174 L340,158 L334,162 L340,146 L346,162 L340,158 L348,174 L340,170 L340,200 Z"></path><path d="M520,200 L520,162 L510,168 L520,148 L512,154 L520,132 L528,154 L520,148 L530,168 L520,162 L520,200 Z"></path><path d="M720,200 L720,168 L711,172 L720,154 L713,158 L720,140 L727,158 L720,154 L729,172 L720,168 L720,200 Z"></path><path d="M900,200 L900,160 L890,166 L900,144 L892,150 L900,128 L908,150 L900,144 L910,166 L900,160 L900,200 Z"></path><path d="M1080,200 L1080,164 L1070,170 L1080,150 L1072,156 L1080,134 L1088,156 L1080,150 L1090,170 L1080,164 L1080,200 Z"></path></g></svg><div class="bg-forest-deep text-cream-light py-8"><div class="max-w-4xl mx-auto px-6 md:px-10 text-center font-body text-sm"><p class="mb-2">Ms. Allis is a project of<!-- --> <a href="https://www.harmonyforhopewv.org" class="underline decoration-cream-light/40 underline-offset-4 hover:decoration-cream-light" target="_blank" rel="noopener noreferrer">Harmony for Hope, Inc.</a>, a West Virginia 501(c)(3) nonprofit (EIN 81-1907024).</p><p class="opacity-70 italic">704 Main Street, Mount Hope, West Virginia · Phase 0 invite-only beta</p></div></div></footer></main><script src="/_next/static/chunks/webpack-1ea540f0e26c2248.js" async=""></script><script>(self.__next_f=self.__next_f||[]).push([0]);self.__next_f.push([2,null])</script><script>self.__next_f.push([1,"1:HL[\"/_next/static/css/29f1d71aa19ee44c.css\",\"style\"]\n"])</script><script>self.__next_f.push([1,"2:I[2846,[],\"\"]\n4:I[5878,[\"609\",\"static/chunks/609-09c674f61ad8c961.js\",\"931\",\"static/chunks/app/page-f5b3c5a76f31235e.js\"],\"Image\"]\n5:I[2972,[\"609\",\"static/chunks/609-09c674f61ad8c961.js\",\"931\",\"static/chunks/app/page-f5b3c5a76f31235e.js\"],\"\"]\n6:I[4707,[],\"\"]\n7:I[6423,[],\"\"]\n9:I[1060,[],\"\"]\na:[]\n"])</script><script>self.__next_f.push([1,"0:[\"$\",\"$L2\",null,{\"buildId\":\"2GauRFh05CCnYxic4MiwT\",\"assetPrefix\":\"\",\"urlParts\":[\"\",\"\"],\"initialTree\":[\"\",{\"children\":[\"__PAGE__\",{}]},\"$undefined\",\"$undefined\",true],\"initialSeedData\":[\"\",{\"children\":[\"__PAGE__\",{},[[\"$L3\",[\"$\",\"main\",null,{\"className\":\"min-h-screen flex flex-col\",\"children\":[[\"$\",\"section\",null,{\"className\":\"relative pt-12 pb-20 md:pt-20 md:pb-32 overflow-hidden\",\"children\":[[\"$\",\"div\",null,{\"aria-hidden\":\"true\",\"className\":\"absolute inset-0 bg-halo opacity-100 pointer-events-none\"}],[\"$\",\"div\",null,{\"className\":\"relative max-w-6xl mx-auto px-6 md:px-10\",\"children\":[[\"$\",\"div\",null,{\"className\":\"animate-fade-in mb-12 md:mb-16\",\"children\":[\"$\",\"div\",null,{\"className\":\"flex items-center justify-center gap-3 text-terracotta\",\"children\":[[\"$\",\"svg\",null,{\"viewBox\":\"0 0 24 24\",\"className\":\"w-3 h-3 opacity-40\",\"aria-hidden\":\"true\",\"fill\":\"currentColor\",\"stroke\":\"currentColor\",\"strokeWidth\":0,\"strokeLinecap\":\"round\",\"strokeLinejoin\":\"round\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z\"}],[\"$\",\"path\",null,{\"d\":\"M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z\",\"fill\":\"rgba(0,0,0,0.18)\"}]]}],[\"$\",\"svg\",null,{\"viewBox\":\"0 0 24 24\",\"className\":\"w-4 h-4 opacity-60\",\"aria-hidden\":\"true\",\"fill\":\"currentColor\",\"stroke\":\"currentColor\",\"strokeWidth\":0,\"strokeLinecap\":\"round\",\"strokeLinejoin\":\"round\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z\"}],[\"$\",\"path\",null,{\"d\":\"M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z\",\"fill\":\"rgba(0,0,0,0.18)\"}]]}],[\"$\",\"svg\",null,{\"viewBox\":\"0 0 24 24\",\"className\":\"w-5 h-5 opacity-100\",\"aria-hidden\":\"true\",\"fill\":\"currentColor\",\"stroke\":\"currentColor\",\"strokeWidth\":0,\"strokeLinecap\":\"round\",\"strokeLinejoin\":\"round\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z\"}],[\"$\",\"path\",null,{\"d\":\"M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z\",\"fill\":\"rgba(0,0,0,0.18)\"}]]}],[\"$\",\"svg\",null,{\"viewBox\":\"0 0 24 24\",\"className\":\"w-4 h-4 opacity-60\",\"aria-hidden\":\"true\",\"fill\":\"currentColor\",\"stroke\":\"currentColor\",\"strokeWidth\":0,\"strokeLinecap\":\"round\",\"strokeLinejoin\":\"round\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z\"}],[\"$\",\"path\",null,{\"d\":\"M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z\",\"fill\":\"rgba(0,0,0,0.18)\"}]]}],[\"$\",\"svg\",null,{\"viewBox\":\"0 0 24 24\",\"className\":\"w-3 h-3 opacity-40\",\"aria-hidden\":\"true\",\"fill\":\"currentColor\",\"stroke\":\"currentColor\",\"strokeWidth\":0,\"strokeLinecap\":\"round\",\"strokeLinejoin\":\"round\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z\"}],[\"$\",\"path\",null,{\"d\":\"M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z\",\"fill\":\"rgba(0,0,0,0.18)\"}]]}]]}]}],[\"$\",\"div\",null,{\"className\":\"grid md:grid-cols-12 gap-10 md:gap-16 items-center\",\"children\":[[\"$\",\"div\",null,{\"className\":\"md:col-span-5 flex justify-center md:justify-start animate-fade-in-up\",\"children\":[\"$\",\"div\",null,{\"className\":\"relative inline-block max-w-full \",\"style\":{\"maxWidth\":\"640px\"},\"children\":[\"$\",\"div\",null,{\"className\":\"relative bg-terracotta-deep p-2 shadow-warm-lg\",\"children\":[\"$\",\"div\",null,{\"className\":\"bg-cream-light p-1.5\",\"children\":[\"$\",\"$L4\",null,{\"src\":\"/ms-allis.jpg\",\"alt\":\"Ms. Allis — folk-art portrait\",\"width\":640,\"height\":640,\"sizes\":\"(max-width: 768px) 320px, (max-width: 1024px) 420px, 480px\",\"priority\":true,\"className\":\"block w-full h-auto object-cover\"}]}]}]}]}],[\"$\",\"div\",null,{\"className\":\"md:col-span-7 animate-fade-in-up\",\"style\":{\"animationDelay\":\"0.15s\"},\"children\":[[\"$\",\"div\",null,{\"className\":\"inline-flex items-center gap-3 mb-6 text-terracotta\",\"children\":[[\"$\",\"span\",null,{\"className\":\"h-px w-8 bg-terracotta\"}],[\"$\",\"span\",null,{\"className\":\"font-display italic text-sm tracking-widest uppercase\",\"children\":\"Mount Hope · West Virginia\"}]]}],[\"$\",\"h1\",null,{\"className\":\"font-display text-hero text-teal-deep mb-8\",\"children\":[[\"$\",\"span\",null,{\"className\":\"block italic font-light text-gold-deep\",\"children\":\"meet\"}],\"Ms. Allis\",[\"$\",\"span\",null,{\"className\":\"text-terracotta\",\"children\":\".\"}]]}],[\"$\",\"p\",null,{\"className\":\"font-body text-xl md:text-2xl leading-relaxed text-ink-soft mb-3 max-w-xl\",\"children\":\"The MountainShares Artificial Learning \u0026 Location Intelligence System.\"}],[\"$\",\"p\",null,{\"className\":\"font-body text-base md:text-lg leading-relaxed text-ink-soft mb-10 max-w-xl\",\"children\":[\"An AI rooted in Appalachia. Built and stewarded by\",\" \",[\"$\",\"a\",null,{\"href\":\"https://www.harmonyforhopewv.org\",\"className\":\"text-terracotta underline decoration-terracotta/40 underline-offset-4 hover:decoration-terracotta transition-colors\",\"target\":\"_blank\",\"rel\":\"noopener noreferrer\",\"children\":\"Harmony for Hope, Inc.\"}],\", a 501(c)(3) nonprofit in Mount Hope, West Virginia. Currently in Phase 0 invite-only beta with\",\" \",[\"$\",\"span\",null,{\"className\":\"text-teal-deep font-medium\",\"children\":\"Community Champions\"}],\" \",\"from across all 55 counties.\"]}],[\"$\",\"div\",null,{\"className\":\"flex flex-wrap items-center gap-4\",\"children\":[[\"$\",\"$L5\",null,{\"href\":\"/apply\",\"className\":\"btn-primary group\",\"children\":[[\"$\",\"svg\",null,{\"viewBox\":\"0 0 24 24\",\"className\":\"w-4 h-4 group-hover:scale-110 transition-transform\",\"aria-hidden\":\"true\",\"fill\":\"currentColor\",\"stroke\":\"currentColor\",\"strokeWidth\":0,\"strokeLinecap\":\"round\",\"strokeLinejoin\":\"round\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z\"}],[\"$\",\"path\",null,{\"d\":\"M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z\",\"fill\":\"rgba(0,0,0,0.18)\"}]]}],\"Apply to be a Champion\"]}],[\"$\",\"$L5\",null,{\"href\":\"/portal\",\"className\":\"font-body text-base text-ink-soft hover:text-teal underline decoration-cream-deep underline-offset-4 hover:decoration-teal transition-colors\",\"children\":\"Already a Champion? Sign in\"}]]}]]}]]}]]}]]}],[\"$\",\"div\",null,{\"className\":\"flex justify-center py-8\",\"children\":[\"$\",\"svg\",null,{\"viewBox\":\"0 0 80 24\",\"className\":\"w-32 text-gold\",\"aria-hidden\":\"true\",\"children\":[\"$\",\"g\",null,{\"fill\":\"none\",\"stroke\":\"currentColor\",\"strokeWidth\":\"1.5\",\"strokeLinecap\":\"round\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M5 12 Q15 12 20 6 Q25 0 35 6 Q40 9 40 12\"}],[\"$\",\"path\",null,{\"d\":\"M75 12 Q65 12 60 6 Q55 0 45 6 Q40 9 40 12\"}],[\"$\",\"circle\",null,{\"cx\":\"40\",\"cy\":\"12\",\"r\":\"2\",\"fill\":\"currentColor\"}],[\"$\",\"path\",null,{\"d\":\"M20 6 Q19 4 17 4\"}],[\"$\",\"path\",null,{\"d\":\"M60 6 Q61 4 63 4\"}]]}]}]}],[\"$\",\"section\",null,{\"className\":\"py-20 md:py-28 bg-cream-light/40\",\"children\":[\"$\",\"div\",null,{\"className\":\"max-w-4xl mx-auto px-6 md:px-10\",\"children\":[[\"$\",\"div\",null,{\"className\":\"text-center mb-16\",\"children\":[[\"$\",\"h2\",null,{\"className\":\"font-display italic text-display text-teal-deep mb-4\",\"children\":\"Who is Ms. Allis?\"}],[\"$\",\"div\",null,{\"className\":\"divider-hearts max-w-md mx-auto\",\"children\":[\"$\",\"svg\",null,{\"viewBox\":\"0 0 24 24\",\"className\":\"w-3 h-3\",\"aria-hidden\":\"true\",\"fill\":\"currentColor\",\"stroke\":\"currentColor\",\"strokeWidth\":0,\"strokeLinecap\":\"round\",\"strokeLinejoin\":\"round\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z\"}],[\"$\",\"path\",null,{\"d\":\"M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z\",\"fill\":\"rgba(0,0,0,0.18)\"}]]}]}]]}],[\"$\",\"div\",null,{\"className\":\"grid md:grid-cols-2 gap-12 md:gap-16\",\"children\":[[\"$\",\"div\",null,{\"children\":[[\"$\",\"div\",null,{\"className\":\"inline-block px-3 py-1 mb-4 font-display italic text-xs uppercase tracking-widest text-terracotta border border-terracotta/30\",\"children\":\"Place-bound\"}],[\"$\",\"p\",null,{\"className\":\"font-body text-lg leading-relaxed text-ink-soft\",\"children\":\"Ms. Allis is grounded in West Virginia — every belief she holds is anchored to a place, a time, a source. She knows the difference between Fayette County and Fayetteville. She knows which fire station serves your hollow. She knows the parcels, the EMS response zones, the historic markers, the food pantries.\"}]]}],[\"$\",\"div\",null,{\"children\":[[\"$\",\"div\",null,{\"className\":\"inline-block px-3 py-1 mb-4 font-display italic text-xs uppercase tracking-widest text-forest-deep border border-forest/30\",\"children\":\"Stewarded\"}],[\"$\",\"p\",null,{\"className\":\"font-body text-lg leading-relaxed text-ink-soft\",\"children\":\"She is not a product. She is community infrastructure — built by a Quaker-rooted nonprofit with a 346-year heritage of stewardship, governed transparently, and accountable to the people she serves. Her conversations belong to you. Her code is yours to inspect.\"}]]}],[\"$\",\"div\",null,{\"children\":[[\"$\",\"div\",null,{\"className\":\"inline-block px-3 py-1 mb-4 font-display italic text-xs uppercase tracking-widest text-gold-deep border border-gold/40\",\"children\":\"Verified\"}],[\"$\",\"p\",null,{\"className\":\"font-body text-lg leading-relaxed text-ink-soft\",\"children\":\"Twenty-one language models reach consensus on every answer. Five judges check for accuracy and harm. Truth-filter validators check for hallucination. The pipeline is transparent and the audit log is permanent.\"}]]}],[\"$\",\"div\",null,{\"children\":[[\"$\",\"div\",null,{\"className\":\"inline-block px-3 py-1 mb-4 font-display italic text-xs uppercase tracking-widest text-teal-mid border border-teal/30\",\"children\":\"Yours\"}],[\"$\",\"p\",null,{\"className\":\"font-body text-lg leading-relaxed text-ink-soft\",\"children\":\"Champions receive a unique ecosystem identifier (UEID), a custodial Arbitrum wallet, and the ability to earn MountainShares through community contribution. Phase 0 is small and careful by design — we'd rather grow slowly and well.\"}]]}]]}]]}]}],[\"$\",\"section\",null,{\"className\":\"py-20 md:py-28\",\"children\":[\"$\",\"div\",null,{\"className\":\"max-w-3xl mx-auto px-6 md:px-10 text-center\",\"children\":[[\"$\",\"div\",null,{\"className\":\"flex items-center justify-center gap-3 text-terracotta mb-8\",\"children\":[[\"$\",\"svg\",null,{\"viewBox\":\"0 0 24 24\",\"className\":\"w-3 h-3 opacity-40\",\"aria-hidden\":\"true\",\"fill\":\"currentColor\",\"stroke\":\"currentColor\",\"strokeWidth\":0,\"strokeLinecap\":\"round\",\"strokeLinejoin\":\"round\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z\"}],[\"$\",\"path\",null,{\"d\":\"M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z\",\"fill\":\"rgba(0,0,0,0.18)\"}]]}],[\"$\",\"svg\",null,{\"viewBox\":\"0 0 24 24\",\"className\":\"w-4 h-4 opacity-60\",\"aria-hidden\":\"true\",\"fill\":\"currentColor\",\"stroke\":\"currentColor\",\"strokeWidth\":0,\"strokeLinecap\":\"round\",\"strokeLinejoin\":\"round\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z\"}],[\"$\",\"path\",null,{\"d\":\"M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z\",\"fill\":\"rgba(0,0,0,0.18)\"}]]}],[\"$\",\"svg\",null,{\"viewBox\":\"0 0 24 24\",\"className\":\"w-5 h-5 opacity-100\",\"aria-hidden\":\"true\",\"fill\":\"currentColor\",\"stroke\":\"currentColor\",\"strokeWidth\":0,\"strokeLinecap\":\"round\",\"strokeLinejoin\":\"round\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z\"}],[\"$\",\"path\",null,{\"d\":\"M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z\",\"fill\":\"rgba(0,0,0,0.18)\"}]]}],[\"$\",\"svg\",null,{\"viewBox\":\"0 0 24 24\",\"className\":\"w-4 h-4 opacity-60\",\"aria-hidden\":\"true\",\"fill\":\"currentColor\",\"stroke\":\"currentColor\",\"strokeWidth\":0,\"strokeLinecap\":\"round\",\"strokeLinejoin\":\"round\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z\"}],[\"$\",\"path\",null,{\"d\":\"M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z\",\"fill\":\"rgba(0,0,0,0.18)\"}]]}],[\"$\",\"svg\",null,{\"viewBox\":\"0 0 24 24\",\"className\":\"w-3 h-3 opacity-40\",\"aria-hidden\":\"true\",\"fill\":\"currentColor\",\"stroke\":\"currentColor\",\"strokeWidth\":0,\"strokeLinecap\":\"round\",\"strokeLinejoin\":\"round\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M12 21.5c-.4 0-.8-.15-1.1-.45L3.5 13.6C1.4 11.5 1.4 8.1 3.5 6c1-1 2.4-1.55 3.85-1.55s2.85.55 3.85 1.55l.8.8.8-.8c1-1 2.4-1.55 3.85-1.55S19.5 5 20.5 6c2.1 2.1 2.1 5.5 0 7.6l-7.4 7.45c-.3.3-.7.45-1.1.45z\"}],[\"$\",\"path\",null,{\"d\":\"M12 18.4c-.2 0-.4-.08-.55-.23L5.7 12.4c-1.05-1.05-1.05-2.75 0-3.8.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78l1.7 1.7c.4.4 1.1.4 1.5 0l1.7-1.7c.5-.5 1.2-.78 1.93-.78s1.43.28 1.93.78c1.05 1.05 1.05 2.75 0 3.8l-5.75 5.77c-.15.15-.35.23-.55.23z\",\"fill\":\"rgba(0,0,0,0.18)\"}]]}]]}],[\"$\",\"h2\",null,{\"className\":\"font-display italic text-display text-teal-deep mb-6\",\"children\":\"Want to help?\"}],[\"$\",\"p\",null,{\"className\":\"font-body text-lg md:text-xl leading-relaxed text-ink-soft mb-10 max-w-2xl mx-auto\",\"children\":\"Phase 0 Champions test the system, find what's broken, and shape what it becomes. Application takes about ten minutes. We read every one personally.\"}],[\"$\",\"$L5\",null,{\"href\":\"/apply\",\"className\":\"btn-terracotta\",\"children\":\"Apply to be a Champion\"}]]}]}],[\"$\",\"footer\",null,{\"className\":\"mt-auto relative\",\"children\":[[\"$\",\"svg\",null,{\"viewBox\":\"0 0 1200 200\",\"className\":\"w-full h-32 md:h-40 text-forest\",\"preserveAspectRatio\":\"none\",\"aria-hidden\":\"true\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M0,200 L0,140 L80,90 L160,120 L240,75 L340,110 L440,60 L540,95 L640,55 L740,100 L840,70 L940,105 L1040,65 L1140,95 L1200,80 L1200,200 Z\",\"fill\":\"currentColor\",\"opacity\":\"0.35\"}],[\"$\",\"path\",null,{\"d\":\"M0,200 L0,170 L100,130 L200,150 L320,115 L420,140 L520,110 L640,135 L760,105 L880,138 L1000,108 L1100,130 L1200,118 L1200,200 Z\",\"fill\":\"currentColor\",\"opacity\":\"0.65\"}],[\"$\",\"g\",null,{\"fill\":\"currentColor\",\"opacity\":\"0.85\",\"children\":[[\"$\",\"path\",null,{\"d\":\"M60,200 L60,165 L50,170 L60,150 L52,155 L60,135 L68,155 L60,150 L70,170 L60,165 L60,200 Z\"}],[\"$\",\"path\",null,{\"d\":\"M180,200 L180,158 L168,164 L180,140 L170,146 L180,122 L190,146 L180,140 L192,164 L180,158 L180,200 Z\"}],[\"$\",\"path\",null,{\"d\":\"M340,200 L340,170 L332,174 L340,158 L334,162 L340,146 L346,162 L340,158 L348,174 L340,170 L340,200 Z\"}],[\"$\",\"path\",null,{\"d\":\"M520,200 L520,162 L510,168 L520,148 L512,154 L520,132 L528,154 L520,148 L530,168 L520,162 L520,200 Z\"}],[\"$\",\"path\",null,{\"d\":\"M720,200 L720,168 L711,172 L720,154 L713,158 L720,140 L727,158 L720,154 L729,172 L720,168 L720,200 Z\"}],[\"$\",\"path\",null,{\"d\":\"M900,200 L900,160 L890,166 L900,144 L892,150 L900,128 L908,150 L900,144 L910,166 L900,160 L900,200 Z\"}],[\"$\",\"path\",null,{\"d\":\"M1080,200 L1080,164 L1070,170 L1080,150 L1072,156 L1080,134 L1088,156 L1080,150 L1090,170 L1080,164 L1080,200 Z\"}]]}]]}],[\"$\",\"div\",null,{\"className\":\"bg-forest-deep text-cream-light py-8\",\"children\":[\"$\",\"div\",null,{\"className\":\"max-w-4xl mx-auto px-6 md:px-10 text-center font-body text-sm\",\"children\":[[\"$\",\"p\",null,{\"className\":\"mb-2\",\"children\":[\"Ms. Allis is a project of\",\" \",[\"$\",\"a\",null,{\"href\":\"https://www.harmonyforhopewv.org\",\"className\":\"underline decoration-cream-light/40 underline-offset-4 hover:decoration-cream-light\",\"target\":\"_blank\",\"rel\":\"noopener noreferrer\",\"children\":\"Harmony for Hope, Inc.\"}],\", a West Virginia 501(c)(3) nonprofit (EIN 81-1907024).\"]}],[\"$\",\"p\",null,{\"className\":\"opacity-70 italic\",\"children\":\"704 Main Street, Mount Hope, West Virginia · Phase 0 invite-only beta\"}]]}]}]]}]]}],null],null],null]},[[[[\"$\",\"link\",\"0\",{\"rel\":\"stylesheet\",\"href\":\"/_next/static/css/29f1d71aa19ee44c.css\",\"precedence\":\"next\",\"crossOrigin\":\"$undefined\"}]],[\"$\",\"html\",null,{\"lang\":\"en\",\"children\":[\"$\",\"body\",null,{\"children\":[\"$\",\"$L6\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\"],\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$L7\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":[[\"$\",\"title\",null,{\"children\":\"404: This page could not be found.\"}],[\"$\",\"div\",null,{\"style\":{\"fontFamily\":\"system-ui,\\\"Segoe UI\\\",Roboto,Helvetica,Arial,sans-serif,\\\"Apple Color Emoji\\\",\\\"Segoe UI Emoji\\\"\",\"height\":\"100vh\",\"textAlign\":\"center\",\"display\":\"flex\",\"flexDirection\":\"column\",\"alignItems\":\"center\",\"justifyContent\":\"center\"},\"children\":[\"$\",\"div\",null,{\"children\":[[\"$\",\"style\",null,{\"dangerouslySetInnerHTML\":{\"__html\":\"body{color:#000;background:#fff;margin:0}.next-error-h1{border-right:1px solid rgba(0,0,0,.3)}@media (prefers-color-scheme:dark){body{color:#fff;background:#000}.next-error-h1{border-right:1px solid rgba(255,255,255,.3)}}\"}}],[\"$\",\"h1\",null,{\"className\":\"next-error-h1\",\"style\":{\"display\":\"inline-block\",\"margin\":\"0 20px 0 0\",\"padding\":\"0 23px 0 0\",\"fontSize\":24,\"fontWeight\":500,\"verticalAlign\":\"top\",\"lineHeight\":\"49px\"},\"children\":\"404\"}],[\"$\",\"div\",null,{\"style\":{\"display\":\"inline-block\"},\"children\":[\"$\",\"h2\",null,{\"style\":{\"fontSize\":14,\"fontWeight\":400,\"lineHeight\":\"49px\",\"margin\":0},\"children\":\"This page could not be found.\"}]}]]}]}]],\"notFoundStyles\":[]}]}]}]],null],null],\"couldBeIntercepted\":false,\"initialHead\":[null,\"$L8\"],\"globalErrorComponent\":\"$9\",\"missingSlots\":\"$Wa\"}]\n"])</script><script>self.__next_f.push([1,"8:[[\"$\",\"meta\",\"0\",{\"name\":\"viewport\",\"content\":\"width=device-width, initial-scale=1\"}],[\"$\",\"meta\",\"1\",{\"charSet\":\"utf-8\"}],[\"$\",\"title\",\"2\",{\"children\":\"Ms. Allis — MountainShares Artificial Learning \u0026 Location Intelligence System\"}],[\"$\",\"meta\",\"3\",{\"name\":\"description\",\"content\":\"An Appalachian-rooted AI assistant, built and stewarded in Mount Hope, West Virginia, by Harmony for Hope, Inc.\"}],[\"$\",\"meta\",\"4\",{\"property\":\"og:title\",\"content\":\"Ms. Allis\"}],[\"$\",\"meta\",\"5\",{\"property\":\"og:description\",\"content\":\"Appalachian community AI from Mount Hope, West Virginia.\"}],[\"$\",\"meta\",\"6\",{\"property\":\"og:image\",\"content\":\"https://msallis.h4h.org/ms-allis.jpg\"}],[\"$\",\"meta\",\"7\",{\"name\":\"twitter:card\",\"content\":\"summary_large_image\"}],[\"$\",\"meta\",\"8\",{\"name\":\"twitter:title\",\"content\":\"Ms. Allis\"}],[\"$\",\"meta\",\"9\",{\"name\":\"twitter:description\",\"content\":\"Appalachian community AI from Mount Hope, West Virginia.\"}],[\"$\",\"meta\",\"10\",{\"name\":\"twitter:image\",\"content\":\"https://msallis.h4h.org/ms-allis.jpg\"}]]\n3:null\n"])</script></body></html>(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ # ── FIX 1: Make BBB a hard gate (fail-close# ── FIX 1: Make BBB a hard gate (fail-closed) ──────────────────────────────
cp /opt/msjarvis-rebuild/msjarvis-rebuild/ms_jarvis_unified_gateway.py \
   /opt/msjarvis-rebuild/msjarvis-rebuild/ms_jarvis_unified_gateway.py.bak.$(date +%Y%m%dT%H%M%S)

sed -i \
  's/pipeline\["bbb"\].get("content_approved", True)/pipeline["bbb"].get("content_approved", False)/' \
  /opt/msjarvis-rebuild/msjarvis-rebuild/ms_jarvis_unified_gateway.py

# Verify the change landed
grep -n "content_approved" \
  /opt/msjarvis-rebuild/msjarvis-rebuild/ms_jarvis_unified_gateway.py
227:                if not pipeline["bbb"].get("content_approved", False):
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

