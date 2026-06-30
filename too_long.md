(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ # Assertion counts — run as separate statement
docker exec -i msjarvisgis-db psql -U postgres -d hilbert_people -c "
SELECT claim_type, context, count(*)
FROM hp.appearance_assertion
GROUP BY claim_type, context
ORDER BY count DESC LIMIT 10;
"
        claim_type        |        context         | count 
--------------------------+------------------------+-------
 verified_county_resident | gbimrouterenrichment   |     2
 verified_state_resident  | gbimrouterenrichment   |     2
 verified_county_resident | gbim_router_enrichment |     1
 verified_adult           | gbim_router_enrichment |     1
 verified_state_resident  | admin_grant            |     1
 verified_state_resident  | gbim_router_enrichment |     1
(6 rows)

(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ # Write minimization.py
cat > /mnt/spiritual_drive/msjarvis-rebuild/services/jarvis-assertion-gateway/app/minimization.py << 'EOF'
"""
Assertion minimization policy.

Suppresses persisting assertions when fewer than K_ANONYMITY_THRESHOLD
subjects share the same (claim_type, context) tuple in
hp.appearance_assertion — preventing tier-3 re-identification by auxiliary
correlation even without access to identity_binding.

Defends against the statistical re-identification failure mode
(Netflix Prize, NYC taxi) where a rich tier-3 record alone reconstructs
tier-1 correlations that were never explicitly stored.

County is intentionally excluded from the tuple — including it would 
allow a sparse-county population to suppress every assertion trivially
and leak county membership via timing side-channel.
echo "✅ minimization.py written"count, K_ANONYMITY_THRESHOLD,jects 
✅ minimization.py written
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ WARNING:  WatchFiles detected changes in 'services/jarvis-assertion-gateway/app/minimization.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2140972]
INFO:     Started server process [2143231]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'services/jarvis-assertion-gateway/app/main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2143231]
INFO:     Started server process [2143264]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:52988 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52992 - "GET /openapi.json HTTP/1.1" 200 OK
WARNING:  WatchFiles detected changes in 'services/jarvis-assertion-gateway/app/main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2143264]
INFO:     Started server process [2145985]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'services/jarvis-assertion-gateway/app/main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2145985]
INFO:     Started server process [2147133]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'auth_router.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2147133]
INFO:     Started server process [2148133]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'auth_router.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2148133]
INFO:     Started server process [2148152]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:48600 - "GET /health HTTP/1.1" 200 OK
[PIPELINE] No DL image provided — skipping OCR
[KYC] Failed to write three-tier identity: new row for relation "appearance" violates check constraint "appearance_disclosure_status_check"
DETAIL:  Failing row contains (949bb5e1-25c9-4bd2-bb2f-ad9bc4e02a2d, self_registration, Community Member, person, community_member, null, null, null, self_declared, self, active, 4ae579dd034179eaeb1867d05c9a349f168a09e25076fb40d574416f86e32522, 2026-06-30 19:53:06.803008+00, 2026-06-30 19:53:06.803008+00).

INFO:     127.0.0.1:45222 - "POST /auth/register HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 411, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 69, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/applications.py", line 123, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/cors.py", line 85, in __call__
    await self.app(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 65, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 756, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 776, in app
    await route.handle(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 297, in handle
    await self.app(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 77, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 72, in app
    response = await func(request)
               ^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/routing.py", line 278, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/auth_router.py", line 277, in register
    _write_kyc_vault(public_uuid, body.name, ueid)
  File "/mnt/spiritual_drive/msjarvis-rebuild/auth_router.py", line 75, in _write_kyc_vault
    cur.execute(
psycopg2.errors.CheckViolation: new row for relation "appearance" violates check constraint "appearance_disclosure_status_check"
DETAIL:  Failing row contains (949bb5e1-25c9-4bd2-bb2f-ad9bc4e02a2d, self_registration, Community Member, person, community_member, null, null, null, self_declared, self, active, 4ae579dd034179eaeb1867d05c9a349f168a09e25076fb40d574416f86e32522, 2026-06-30 19:53:06.803008+00, 2026-06-30 19:53:06.803008+00).

INFO:     127.0.0.1:36794 - "POST /auth/register HTTP/1.1" 422 Unprocessable Entity
[PIPELINE] No DL image provided — skipping OCR
[KYC] Failed to write three-tier identity: new row for relation "appearance" violates check constraint "appearance_disclosure_status_check"
DETAIL:  Failing row contains (30ae43ca-8994-43de-95f7-e455be82690f, self_registration, Community Member, person, community_member, null, null, null, self_declared, self, active, 8d2c76e067f827076e4f3718d50ac48c86ce4076a078e3e19eecc9cabc482dc6, 2026-06-30 19:54:48.002324+00, 2026-06-30 19:54:48.002324+00).

INFO:     127.0.0.1:33808 - "POST /auth/register HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 411, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 69, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/applications.py", line 123, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/cors.py", line 85, in __call__
    await self.app(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 65, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 756, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 776, in app
    await route.handle(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 297, in handle
    await self.app(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 77, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 72, in app
    response = await func(request)
               ^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/routing.py", line 278, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/auth_router.py", line 277, in register
    _write_kyc_vault(public_uuid, body.name, ueid)
  File "/mnt/spiritual_drive/msjarvis-rebuild/auth_router.py", line 75, in _write_kyc_vault
    cur.execute(
psycopg2.errors.CheckViolation: new row for relation "appearance" violates check constraint "appearance_disclosure_status_check"
DETAIL:  Failing row contains (30ae43ca-8994-43de-95f7-e455be82690f, self_registration, Community Member, person, community_member, null, null, null, self_declared, self, active, 8d2c76e067f827076e4f3718d50ac48c86ce4076a078e3e19eecc9cabc482dc6, 2026-06-30 19:54:48.002324+00, 2026-06-30 19:54:48.002324+00).

[PIPELINE] No DL image provided — skipping OCR
[KYC] Failed to write three-tier identity: new row for relation "appearance" violates check constraint "appearance_disclosure_status_check"
DETAIL:  Failing row contains (d47f9f1e-102a-4b26-926c-16a76bcc8d4a, self_registration, Community Member, person, community_member, null, null, null, self_declared, self, active, f4a2b3060d520d59b9049787ac647ce534f590217e7990e0695d1ebef1ba9ced, 2026-06-30 19:54:57.464183+00, 2026-06-30 19:54:57.464183+00).

INFO:     127.0.0.1:54312 - "POST /auth/register HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 411, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 69, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/applications.py", line 123, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/cors.py", line 85, in __call__
    await self.app(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 65, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 756, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 776, in app
    await route.handle(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 297, in handle
    await self.app(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 77, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 72, in app
    response = await func(request)
               ^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/routing.py", line 278, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/auth_router.py", line 277, in register
    _write_kyc_vault(public_uuid, body.name, ueid)
  File "/mnt/spiritual_drive/msjarvis-rebuild/auth_router.py", line 75, in _write_kyc_vault
    cur.execute(
psycopg2.errors.CheckViolation: new row for relation "appearance" violates check constraint "appearance_disclosure_status_check"
DETAIL:  Failing row contains (d47f9f1e-102a-4b26-926c-16a76bcc8d4a, self_registration, Community Member, person, community_member, null, null, null, self_declared, self, active, f4a2b3060d520d59b9049787ac647ce534f590217e7990e0695d1ebef1ba9ced, 2026-06-30 19:54:57.464183+00, 2026-06-30 19:54:57.464183+00).

WARNING:  WatchFiles detected changes in 'auth_router.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2148152]
INFO:     Started server process [2151548]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'auth_router.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2151548]
INFO:     Started server process [2151570]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:39130 - "GET /health HTTP/1.1" 200 OK
[PIPELINE] No DL image provided — skipping OCR
[KYC] Failed to write three-tier identity: new row for relation "appearance" violates check constraint "appearance_disclosure_status_check"
DETAIL:  Failing row contains (2765630f-968b-498f-b08b-aa63ac9a5c77, self_registration, Community Member, person, community_member, null, null, null, self_declared, self, active, 1b6d4a0e9bb384a156c986e81dafdac1e472c882a6cf4554d1f06462a2f804f6, 2026-06-30 20:02:15.482063+00, 2026-06-30 20:02:15.482063+00).

INFO:     127.0.0.1:39132 - "POST /auth/register HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 411, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 69, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/applications.py", line 123, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/cors.py", line 85, in __call__
    await self.app(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 65, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 756, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 776, in app
    await route.handle(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 297, in handle
    await self.app(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 77, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 72, in app
    response = await func(request)
               ^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/routing.py", line 278, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/auth_router.py", line 277, in register
    _write_kyc_vault(public_uuid, body.name, ueid)
  File "/mnt/spiritual_drive/msjarvis-rebuild/auth_router.py", line 75, in _write_kyc_vault
    cur.execute(
psycopg2.errors.CheckViolation: new row for relation "appearance" violates check constraint "appearance_disclosure_status_check"
DETAIL:  Failing row contains (2765630f-968b-498f-b08b-aa63ac9a5c77, self_registration, Community Member, person, community_member, null, null, null, self_declared, self, active, 1b6d4a0e9bb384a156c986e81dafdac1e472c882a6cf4554d1f06462a2f804f6, 2026-06-30 20:02:15.482063+00, 2026-06-30 20:02:15.482063+00).

[PIPELINE] No DL image provided — skipping OCR
[KYC] Failed to write three-tier identity: new row for relation "appearance" violates check constraint "appearance_disclosure_status_check"
DETAIL:  Failing row contains (038bfb18-416f-4eb4-a335-6e7709989b93, self_registration, Community Member, person, community_member, null, null, null, self_declared, self, active, e0295d6764755a432300d407c1ced46be51934feb38c9f08a3e7ce17f65bde11, 2026-06-30 20:02:24.454408+00, 2026-06-30 20:02:24.454408+00).

INFO:     127.0.0.1:51132 - "POST /auth/register HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 411, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 69, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/applications.py", line 123, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/cors.py", line 85, in __call__
    await self.app(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 65, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 756, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 776, in app
    await route.handle(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 297, in handle
    await self.app(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 77, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 72, in app
    response = await func(request)
               ^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/routing.py", line 278, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/auth_router.py", line 277, in register
    _write_kyc_vault(public_uuid, body.name, ueid)
  File "/mnt/spiritual_drive/msjarvis-rebuild/auth_router.py", line 75, in _write_kyc_vault
    cur.execute(
psycopg2.errors.CheckViolation: new row for relation "appearance" violates check constraint "appearance_disclosure_status_check"
DETAIL:  Failing row contains (038bfb18-416f-4eb4-a335-6e7709989b93, self_registration, Community Member, person, community_member, null, null, null, self_declared, self, active, e0295d6764755a432300d407c1ced46be51934feb38c9f08a3e7ce17f65bde11, 2026-06-30 20:02:24.454408+00, 2026-06-30 20:02:24.454408+00).

[PIPELINE] No DL image provided — skipping OCR
[KYC] Failed to write three-tier identity: new row for relation "appearance" violates check constraint "appearance_disclosure_status_check"
DETAIL:  Failing row contains (c5caac9e-7694-4817-8ce3-eedb76c210a2, self_registration, Community Member, person, community_member, null, null, null, self_declared, self, active, 1b8f06d349410d36d5c831e371bd98537094dcf9267185c270387337ccc9fb66, 2026-06-30 20:03:08.919776+00, 2026-06-30 20:03:08.919776+00).

INFO:     127.0.0.1:38738 - "POST /auth/register HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 411, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 69, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/applications.py", line 123, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/cors.py", line 85, in __call__
    await self.app(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 65, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 756, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 776, in app
    await route.handle(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 297, in handle
    await self.app(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 77, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app
    raise exc
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/starlette/routing.py", line 72, in app
    response = await func(request)
               ^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/routing.py", line 278, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/lib/python3.12/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/spiritual_drive/msjarvis-rebuild/auth_router.py", line 277, in register
    _write_kyc_vault(public_uuid, body.name, ueid)
  File "/mnt/spiritual_drive/msjarvis-rebuild/auth_router.py", line 75, in _write_kyc_vault
    cur.execute(
psycopg2.errors.CheckViolation: new row for relation "appearance" violates check constraint "appearance_disclosure_status_check"
DETAIL:  Failing row contains (c5caac9e-7694-4817-8ce3-eedb76c210a2, self_registration, Community Member, person, community_member, null, null, null, self_declared, self, active, 1b8f06d349410d36d5c831e371bd98537094dcf9267185c270387337ccc9fb66, 2026-06-30 20:03:08.919776+00, 2026-06-30 20:03:08.919776+00).

WARNING:  WatchFiles detected changes in 'auth_router.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2151570]
INFO:     Started server process [2152146]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'auth_router.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2152146]
INFO:     Started server process [2152282]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
[PIPELINE] No DL image provided — skipping OCR
INFO:     127.0.0.1:51370 - "POST /auth/register HTTP/1.1" 201 Created
INFO:     127.0.0.1:38704 - "POST /auth/register HTTP/1.1" 409 Conflict
[PIPELINE] No DL image provided — skipping OCR
INFO:     127.0.0.1:54726 - "POST /auth/register HTTP/1.1" 201 Created
[PIPELINE] No DL image provided — skipping OCR
INFO:     127.0.0.1:60108 - "POST /auth/register HTTP/1.1" 201 Created
WARNING:  WatchFiles detected changes in 'merkle_identity.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2152282]
INFO:     Started server process [2157985]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'auth_router.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2157985]
INFO:     Started server process [2158069]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'auth_router.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2158069]
INFO:     Started server process [2158150]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:48518 - "GET /health HTTP/1.1" 200 OK
[PIPELINE] No DL image provided — skipping OCR
INFO:     127.0.0.1:34478 - "POST /auth/register HTTP/1.1" 201 Created
[PIPELINE] No DL image provided — skipping OCR
INFO:     127.0.0.1:49908 - "POST /auth/register HTTP/1.1" 201 Created
[PIPELINE] No DL image provided — skipping OCR
INFO:     127.0.0.1:49914 - "POST /auth/register HTTP/1.1" 201 Created
[PIPELINE] No DL image provided — skipping OCR
INFO:     127.0.0.1:49918 - "POST /auth/register HTTP/1.1" 201 Created
[PIPELINE] No DL image provided — skipping OCR
INFO:     127.0.0.1:60642 - "POST /auth/register HTTP/1.1" 201 Created
INFO:     127.0.0.1:48552 - "POST /auth/register HTTP/1.1" 422 Unprocessable Entity
WARNING:  WatchFiles detected changes in 'auth_router.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2158150]
INFO:     Started server process [2162359]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'auth_router.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2162359]
INFO:     Started server process [2162394]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:45712 - "POST /auth/register HTTP/1.1" 422 Unprocessable Entity
[PIPELINE] No DL image provided — skipping OCR
INFO:     127.0.0.1:57970 - "POST /auth/register HTTP/1.1" 201 Created
WARNING:  WatchFiles detected changes in 'auth_router.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2162394]
INFO:     Started server process [2164799]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:44246 - "GET /health HTTP/1.1" 200 OK
[PIPELINE] No DL image provided — skipping OCR
INFO:     127.0.0.1:52580 - "POST /auth/register HTTP/1.1" 201 Created
WARNING:  WatchFiles detected changes in 'auth_router.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2164799]
INFO:     Started server process [2165346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'auth_router.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2165346]
INFO:     Started server process [2165360]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
[PIPELINE] No DL image provided — skipping OCR
INFO:     127.0.0.1:45590 - "POST /auth/register HTTP/1.1" 201 Created
WARNING:  WatchFiles detected changes in 'services/jarvis-assertion-gateway/app/main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2165360]
INFO:     Started server process [2166868]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'services/jarvis-assertion-gateway/app/main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2166868]
INFO:     Started server process [2166990]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'services/jarvis-assertion-gateway/app/main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2166990]
INFO:     Started server process [2169445]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'services/jarvis-assertion-gateway/app/main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2169445]
INFO:     Started server process [2169572]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'crypto-venv/lib/python3.12/site-packages/deprecated/classic.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/storage/memcached/emcache.py', 'crypto-venv/lib/python3.12/site-packages/limits/storage/__init__.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/storage/redis/valkey.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/storage/redis/bridge.py', 'crypto-venv/lib/python3.12/site-packages/limits/strategies.py', 'crypto-venv/lib/python3.12/site-packages/limits/storage/base.py', 'crypto-venv/lib/python3.12/site-packages/slowapi/util.py', 'crypto-venv/lib/python3.12/site-packages/limits/_storage_scheme.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/storage/mongodb.py', 'crypto-venv/lib/python3.12/site-packages/slowapi/wrappers.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/storage/redis/redispy.py', 'crypto-venv/lib/python3.12/site-packages/limits/storage/redis_cluster.py', 'crypto-venv/lib/python3.12/site-packages/deprecated/params.py', 'crypto-venv/lib/python3.12/site-packages/limits/limits.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/strategies.py', 'crypto-venv/lib/python3.12/site-packages/deprecated/__init__.py', 'crypto-venv/lib/python3.12/site-packages/limits/_version.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/__init__.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/storage/memory.py', 'crypto-venv/lib/python3.12/site-packages/limits/storage/redis_sentinel.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/storage/redis/__init__.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/storage/memcached/memcachio.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/storage/__init__.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/storage/base.py', 'crypto-venv/lib/python3.12/site-packages/limits/storage/redis.py', 'crypto-venv/lib/python3.12/site-packages/slowapi/errors.py', 'crypto-venv/lib/python3.12/site-packages/limits/storage/mongodb.py', 'crypto-venv/lib/python3.12/site-packages/limits/errors.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/storage/redis/coredis.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/storage/memcached/__init__.py', 'crypto-venv/lib/python3.12/site-packages/slowapi/middleware.py', 'crypto-venv/lib/python3.12/site-packages/limits/storage/memcached.py', 'crypto-venv/lib/python3.12/site-packages/limits/typing.py', 'crypto-venv/lib/python3.12/site-packages/limits/storage/memory.py', 'crypto-venv/lib/python3.12/site-packages/slowapi/extension.py', 'crypto-venv/lib/python3.12/site-packages/limits/aio/storage/memcached/bridge.py', 'crypto-venv/lib/python3.12/site-packages/deprecated/sphinx.py', 'crypto-venv/lib/python3.12/site-packages/limits/util.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2169572]
INFO:     Started server process [2174301]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'services/jarvis-assertion-gateway/app/main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2174301]
INFO:     Started server process [2174381]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'services/jarvis-assertion-gateway/app/main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2174381]
INFO:     Started server process [2175560]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

