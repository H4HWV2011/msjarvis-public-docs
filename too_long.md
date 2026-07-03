crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ # 1) Show the rogue listener and its parent tree

echo "== rogue listener =="
pgrep -af 'uvicorn auth_api:app|gunicorn auth_api:app'

echo
echo "== ps -fp on rogue PIDs =="
ps -fp $(pgrep -f 'uvicorn auth_api:app|gunicorn auth_api:app' || echo "")

echo
echo "== pstree for rogue PIDs =="
for p in $(pgrep -f 'uvicorn auth_api:app|gunicorn auth_api:app' || echo ""); do 
  echo "--- pstree for PID $p ---"
  pstree -sap "$p"
done


# 2) Find any systemd units (system + user) that mention uvicorn/gunicorn/auth/jarvis/8095

echo
echo "== system services that may spawn auth =="
1:8095/auth/me/me -> "; curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.
== rogue listener ==
2441755 /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python -m uvicorn auth_api:app --host 127.0.0.1 --port 8095
2443953 /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/gunicorn auth_api:app -k uvicorn_worker.UvicornWorker -w 2 --bind 127.0.0.1:8095

== ps -fp on rogue PIDs ==
UID          PID    PPID  C STIME TTY      STAT   TIME CMD
cakidd   2441755       1  0 16:00 ?        Ssl    0:00 /mnt/spiritual_drive/msja
cakidd   2443953       1 26 16:03 ?        Ss     0:00 /mnt/spiritual_drive/msja

== pstree for rogue PIDs ==
--- pstree for PID 2441755 ---
systemd,1 splash
  └─python,2441755 -m uvicornauth_api
      ├─{python},2441775
      ├─{python},2441776
      ├─{python},2441777
      ├─{python},2441778
      └─{python},2441779
--- pstree for PID 2443953 ---
systemd,1 splash
  └─gunicorn,2443953/mnt/spiritual_driv

== system services that may spawn auth ==
  jarvis-auth.service                                                                       loaded    active     running            Ms. Jarvis Auth + Status Service
  jarvis-chat-metrics.service                                                               loaded    inactive   dead               Build Jarvis chat metrics JSON
  jarvis-consciousness-4021.service                                                         loaded    active     running            Ms. Jarvis Consciousness Enhancement 4021
  jarvis-interaction-logger.service                                                         loaded    active     running            Jarvis Interaction Logger
  ms-allis-auth-router.service                                                              loaded    active     running            Ms Allis Auth Router (port 8095)
  ms-allis-auth8095.service                                                                 loaded    active     running            MS Allis Auth 8095 (host-run)
  msjarvis-69dgm-9000.service                                                               loaded    inactive   dead               MsJarvis Port 9000 → 69-DGM Bridge
  msjarvis-69dgm-9002-chat.service                                                          loaded    active     running            MsJarvis Port 9002 → 69-DGM Chat Wrapper
  msjarvis-69dgm-orchestrator.service                                                       loaded    inactive   dead               MsJarvis 69-DGM Orchestrator (port 8300)
  msjarvis-chat.service                                                                     loaded    active     running            Ms. Jarvis Production Chat Service (port 8018)
  msjarvis-interaction-logger.service                                                       loaded    activating auto-restart       MS Jarvis Interaction Logger
  msjarvis-production-chat.service                                                          loaded    active     running            Ms. Allis Production Chat Pipeline (port 8018)
  msjarvis.service                                                                          loaded    activating start-pre    start Ms. Jarvis Rebuild Stack
  polkit.service                                                                            loaded    active     running            Authorization Manager
  postgresql@16-msjarvis.service                                                            loaded    inactive   dead               PostgreSQL Cluster 16-msjarvis

== system unit files that may spawn auth ==
auth-router.service                                                           disabled        enabled
jarvis-auth.service                                                           enabled         enabled
jarvis-chat-metrics.service                                                   static          -
jarvis-chat.service                                                           disabled        enabled
jarvis-consciousness-4021.service                                             enabled         enabled
jarvis-interaction-logger.service                                             enabled         enabled
ms-allis-auth-router.service                                                  enabled         enabled
ms-allis-auth.service                                                         disabled        enabled
ms-allis-auth8095.service                                                     enabled         enabled
msjarvis-69dgm-9000.service                                                   disabled        enabled
msjarvis-69dgm-9002-chat.service                                              enabled         enabled
msjarvis-69dgm-orchestrator.service                                           enabled         enabled
msjarvis-chat.service                                                         enabled         enabled
msjarvis-frontend.service                                                     disabled        enabled
msjarvis-interaction-logger.service                                           enabled         enabled
msjarvis-production-chat.service                                              enabled         enabled
msjarvis.service                                                              enabled         enabled
systemd-pcrlock-secureboot-authority.service                                  disabled        enabled
jarvis-chat-metrics.timer                                                     enabled         enabled

== user services that may spawn auth ==
  auth-8055-forward.service                                        loaded    active   running Forward 127.0.0.1:8055 to 127.0.0.1:8095
● jarvis-preflight.service                                         loaded    failed   failed  Ms. Jarvis Pre-Flight Gate
● jarvis-verify.service                                            loaded    failed   failed  Ms. Jarvis Full Regression Verify

== user unit files that may spawn auth ==
auth-8055-forward.service                                         enabled   enabled
flatpak-oci-authenticator.service                                 static    -
jarvis-preflight.service                                          static    -
jarvis-verify.service                                             static    -
msjarvis-auth-8055.service                                        disabled  enabled
jarvis-preflight.timer                                            enabled   enabled
jarvis-verify.timer                                               enabled   enabled

== user crontab ==
# Ms. Jarvis Master Crontab

*/5 * * * * /usr/local/bin/jarvis_bbb_watchdog.sh
*/15 * * * * cd /mnt/spiritual_drive/msjarvis-rebuild && ./scripts/watchdog-containers.sh
*/15 * * * * /home/cakidd/msjarvis-monitoring/monitor_services.sh
*/30 * * * * /home/cakidd/msjarvis-monitoring/monitor_databases.sh
0 * * * * /home/cakidd/msjarvis-monitoring/monitor_disk.sh
0 */6 * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/run_aaacpe_scraper.sh
0 2 * * * docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c "REFRESH MATERIALIZED VIEW CONCURRENTLY county_tax_building_summary" >> /var/log/jarvis_mv_refresh.log 2>&1
0 2 * * * /mnt/spiritual_drive/msjarvis-rebuild/backup_postgresql.sh >> /home/cakidd/logs/backup_postgresql.log 2>&1
0 2 * * * cd /mnt/spiritual_drive/msjarvis-rebuild && bash scripts/refresh_gbim_spatial.sh >> logs/gbim_refresh.log 2>&1
# DISABLED - copies 0-byte sqlite3, useless: 0 2 * * * cp /home/ms-jarvis/msjarvis-rebuild/persistent/chroma/chroma.sqlite3 "/mnt/nvme1/msjarvis-backups/chromadb/chroma-$(date +%Y%m%d-%H%M%S).sqlite3"
0 3 * * 0 docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c "REFRESH MATERIALIZED VIEW CONCURRENTLY building_parcel_county_tax_mv" >> /var/log/jarvis_mv_refresh.log 2>&1
# DISABLED - 77GB rsync too large, chroma-live is the live mount, postgresql backups confirmed current: 0 3 * * * rsync -a /home/ms-jarvis/msjarvis-rebuild/persistent/chroma/ /mnt/nvme1/msjarvis-backups/chromadb/chroma-latest/ >> /tmp/chroma_backup.log 2>&1
0 3 * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/refresh_mvw.sh >> /var/log/mvw_refresh.log 2>&1
0 3 * * * python3 /mnt/spiritual_drive/msjarvis-rebuild/services/identity_promotion.py >> /var/log/jarvis/identity_promotion.log 2>&1
0 4 * * * /mnt/spiritual_drive/msjarvis-rebuild/backup_configs.sh >> /home/cakidd/logs/backup_configs.log 2>&1
0 8 * * 1 cd /mnt/spiritual_drive/msjarvis-rebuild && bash scripts/pia/run_pia_audit.sh >> /var/log/msjarvis-pia.log 2>&1
# NEEDS_PARAMS: 0 1 * * * curl -sf -X POST http://localhost:8099/policy/set -H "Content-Type: application/json" -d "{}" >> /var/log/jarvis/policy_update.log 2>&1
0 2 * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/gbim_decay_tick.sh >> /var/log/gbim_decay.log 2>&1
# RETENTION - Keep only last 2 ChromaDB main tarballs (~6.6G cap)
30 4 * * * find /mnt/nvme1/msjarvis-backups/chromadb -name "chroma_main_*.tar.gz" -mtime +2 -delete
# MAINTENANCE - Weekly Docker build cache prune, keep 10GB headroom
0 3 * * 0 /usr/bin/docker builder prune -f --keep-storage 10GB >> /tmp/docker_prune.log 2>&1
0 2 * * 0 cd /mnt/spiritual_drive/msjarvis-rebuild && .venv/bin/python3 scripts/audit_happiness_v2.py >> logs/manipulation_proximity_audit.log 2>&1
0 */6 * * * /home/cakidd/scripts/local_resources_gap_report.sh >> /home/cakidd/allis-reports/coverage-gaps/gap-report.log 2>&1
*/5 * * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/check_proxies.sh >> /home/cakidd/logs/msjarvis-proxy-health.log 2>&1
#PAUSED */30 * * * * tail -1 /mnt/spiritual_drive/msjarvis-rebuild/migration.log >> /mnt/spiritual_drive/msjarvis-rebuild/progress_history.log
17 2 * * * /home/cakidd/.local/bin/purge-kyc-location-strip.sh


== root crontab ==
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
0 2 * * * docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c "REFRESH MATERIALIZED VIEW CONCURRENTLY county_tax_building_summary" >> /var/log/jarvis_mv_refresh.log 2>&1

== stop/disable any obvious legacy units (safe to run even if absent) ==

== killing all uvicorn/gunicorn auth processes and freeing 8095 ==
Killed
Killed
Killed

== lsof / pgrep after cleanup (should be empty) ==
(no listeners on 8095)
(no uvicorn/gunicorn auth processes)

== starting ms-allis-auth8095.service under gunicorn+uvicorn-worker ==

== final status / listeners / PIDs / HTTP checks ==
● ms-allis-auth8095.service - MS Allis Auth 8095 (host-run)
     Loaded: loaded (/etc/systemd/system/ms-allis-auth8095.service; enabled; preset: enabled)
     Active: active (running) since Fri 2026-07-03 16:03:28 EDT; 3s ago
   Main PID: 2444658 (gunicorn)
      Tasks: 6 (limit: 35466)
     Memory: 143.2M (peak: 144.1M)
        CPU: 1.257s
     CGroup: /system.slice/ms-allis-auth8095.service
             ├─2444658 /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/gunicorn auth_api:app -k uvicorn_worker.UvicornWorker -w 2 --bind 127.0.0.1:8095
             ├─2444663 /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/gunicorn auth_api:app -k uvicorn_worker.UvicornWorker -w 2 --bind 127.0.0.1:8095
             └─2444664 /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/gunicorn auth_api:app -k uvicorn_worker.UvicornWorker -w 2 --bind 127.0.0.1:8095

Jul 03 16:03:28 cakidd-Legion-5-16IRX9 gunicorn[2444658]: [2026-07-03 16:03:28 -0400] [2444658] [INFO] Using worker: uvicorn_worker.UvicornWorker
Jul 03 16:03:28 cakidd-Legion-5-16IRX9 gunicorn[2444663]: [2026-07-03 16:03:28 -0400] [2444663] [INFO] Booting worker with pid: 2444663
Jul 03 16:03:28 cakidd-Legion-5-16IRX9 gunicorn[2444664]: [2026-07-03 16:03:28 -0400] [2444664] [INFO] Booting worker with pid: 2444664
Jul 03 16:03:29 cakidd-Legion-5-16IRX9 gunicorn[2444658]: [2026-07-03 16:03:29 -0400] [2444658] [INFO] Control socket listening at /home/cakidd/.gunicorn/gunicorn.ctl
Jul 03 16:03:29 cakidd-Legion-5-16IRX9 gunicorn[2444663]: [2026-07-03 16:03:29 -0400] [2444663] [INFO] Started server process [2444663]
Jul 03 16:03:29 cakidd-Legion-5-16IRX9 gunicorn[2444663]: [2026-07-03 16:03:29 -0400] [2444663] [INFO] Waiting for application startup.
Jul 03 16:03:29 cakidd-Legion-5-16IRX9 gunicorn[2444663]: [2026-07-03 16:03:29 -0400] [2444663] [INFO] Application startup complete.
Jul 03 16:03:29 cakidd-Legion-5-16IRX9 gunicorn[2444664]: [2026-07-03 16:03:29 -0400] [2444664] [INFO] Started server process [2444664]
Jul 03 16:03:29 cakidd-Legion-5-16IRX9 gunicorn[2444664]: [2026-07-03 16:03:29 -0400] [2444664] [INFO] Waiting for application startup.
Jul 03 16:03:29 cakidd-Legion-5-16IRX9 gunicorn[2444664]: [2026-07-03 16:03:29 -0400] [2444664] [INFO] Application startup complete.
COMMAND      PID   USER   FD   TYPE    DEVICE SIZE/OFF NODE NAME
gunicorn 2444658 cakidd    3u  IPv4 103524126      0t0  TCP 127.0.0.1:8095 (LISTEN)
gunicorn 2444663 cakidd    3u  IPv4 103524126      0t0  TCP 127.0.0.1:8095 (LISTEN)
gunicorn 2444664 cakidd    3u  IPv4 103524126      0t0  TCP 127.0.0.1:8095 (LISTEN)
2444658
2444658 /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/gunicorn auth_api:app -k uvicorn_worker.UvicornWorker -w 2 --bind 127.0.0.1:8095
2444663 /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/gunicorn auth_api:app -k uvicorn_worker.UvicornWorker -w 2 --bind 127.0.0.1:8095
2444664 /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/gunicorn auth_api:app -k uvicorn_worker.UvicornWorker -w 2 --bind 127.0.0.1:8095
/health -> 200
/auth/me -> 401
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

