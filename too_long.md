<pre>(crypto-venv) <font color="#26A269"><b>cakidd@cakidd-Legion-5-16IRX9</b></font>:<font color="#12488B"><b>/mnt/spiritual_drive/msjarvis-rebuild</b></font>$ ps -fp 2441755
pstree -sap 2441755
systemctl list-units --type=service --all | rg &apos;auth|8095|jarvis|uvicorn|gunicorn&apos;
systemctl list-unit-files | rg &apos;auth|8095|jarvis|uvicorn|gunicorn&apos;
sudo journalctl --since &quot;10 minutes ago&quot; --no-pager | rg &apos;2441755|uvicorn auth_api:app|gunicorn auth_api:app|8095&apos;
pgrep -af &apos;uvicorn auth_api:app|gunicorn auth_api:app|run_auth_uvicorn.py&apos;
crontab -l || true
sudo crontab -l || true
systemctl --user list-units --type=service --all | rg &apos;auth|8095|jarvis|uvicorn|gunicorn&apos; || true
systemctl --user list-unit-files | rg &apos;auth|8095|jarvis|uvicorn|gunicorn&apos; || true
UID          PID    PPID  C STIME TTY          TIME CMD
cakidd   2441755       1  2 16:00 ?        00:00:00 /mnt/spiritual_drive/msjarvi
systemd,1 splash
  └─python,2441755 -m uvicornauth_api
      ├─{python},2441775
      ├─{python},2441776
      ├─{python},2441777
      ├─{python},2441778
      └─{python},2441779
  <font color="#C01C28"><b>jarvis</b></font>-<font color="#C01C28"><b>auth</b></font>.service                                                                       loaded    active     running      Ms. Jarvis Auth + Status Service
  <font color="#C01C28"><b>jarvis</b></font>-chat-metrics.service                                                               loaded    inactive   dead         Build Jarvis chat metrics JSON
  <font color="#C01C28"><b>jarvis</b></font>-consciousness-4021.service                                                         loaded    active     running      Ms. Jarvis Consciousness Enhancement 4021
  <font color="#C01C28"><b>jarvis</b></font>-interaction-logger.service                                                         loaded    active     running      Jarvis Interaction Logger
  ms-allis-<font color="#C01C28"><b>auth</b></font>-router.service                                                              loaded    active     running      Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>)
  ms-allis-<font color="#C01C28"><b>auth8095</b></font>.service                                                                 loaded    active     running      MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run)
  ms<font color="#C01C28"><b>jarvis</b></font>-69dgm-9000.service                                                               loaded    inactive   dead         MsJarvis Port 9000 → 69-DGM Bridge
  ms<font color="#C01C28"><b>jarvis</b></font>-69dgm-9002-chat.service                                                          loaded    active     running      MsJarvis Port 9002 → 69-DGM Chat Wrapper
  ms<font color="#C01C28"><b>jarvis</b></font>-69dgm-orchestrator.service                                                       loaded    inactive   dead         MsJarvis 69-DGM Orchestrator (port 8300)
  ms<font color="#C01C28"><b>jarvis</b></font>-chat.service                                                                     loaded    active     running      Ms. Jarvis Production Chat Service (port 8018)
  ms<font color="#C01C28"><b>jarvis</b></font>-interaction-logger.service                                                       loaded    activating auto-restart MS Jarvis Interaction Logger
  ms<font color="#C01C28"><b>jarvis</b></font>-production-chat.service                                                          loaded    active     running      Ms. Allis Production Chat Pipeline (port 8018)
  ms<font color="#C01C28"><b>jarvis</b></font>.service                                                                          loaded    activating auto-restart Ms. Jarvis Rebuild Stack
  postgresql@16-ms<font color="#C01C28"><b>jarvis</b></font>.service                                                            loaded    inactive   dead         PostgreSQL Cluster 16-ms<font color="#C01C28"><b>jarvis</b></font>
<font color="#C01C28"><b>auth</b></font>-router.service                                                           disabled        enabled
<font color="#C01C28"><b>jarvis</b></font>-<font color="#C01C28"><b>auth</b></font>.service                                                           enabled         enabled
<font color="#C01C28"><b>jarvis</b></font>-chat-metrics.service                                                   static          -
<font color="#C01C28"><b>jarvis</b></font>-chat.service                                                           disabled        enabled
<font color="#C01C28"><b>jarvis</b></font>-consciousness-4021.service                                             enabled         enabled
<font color="#C01C28"><b>jarvis</b></font>-interaction-logger.service                                             enabled         enabled
ms-allis-<font color="#C01C28"><b>auth</b></font>-router.service                                                  enabled         enabled
ms-allis-<font color="#C01C28"><b>auth</b></font>.service                                                         disabled        enabled
ms-allis-<font color="#C01C28"><b>auth8095</b></font>.service                                                     enabled         enabled
ms<font color="#C01C28"><b>jarvis</b></font>-69dgm-9000.service                                                   disabled        enabled
ms<font color="#C01C28"><b>jarvis</b></font>-69dgm-9002-chat.service                                              enabled         enabled
ms<font color="#C01C28"><b>jarvis</b></font>-69dgm-orchestrator.service                                           enabled         enabled
ms<font color="#C01C28"><b>jarvis</b></font>-chat.service                                                         enabled         enabled
ms<font color="#C01C28"><b>jarvis</b></font>-frontend.service                                                     disabled        enabled
ms<font color="#C01C28"><b>jarvis</b></font>-interaction-logger.service                                           enabled         enabled
ms<font color="#C01C28"><b>jarvis</b></font>-production-chat.service                                              enabled         enabled
ms<font color="#C01C28"><b>jarvis</b></font>.service                                                              enabled         enabled
systemd-pcrlock-secureboot-<font color="#C01C28"><b>auth</b></font>ority.service                                  disabled        enabled
<font color="#C01C28"><b>jarvis</b></font>-chat-metrics.timer                                                     enabled         enabled
Jul 03 15:51:07 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 16.
Jul 03 15:51:07 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:51:08 cakidd-Legion-5-16IRX9 python[2428849]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:51:08 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:51:08 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:51:13 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 17.
Jul 03 15:51:13 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:51:14 cakidd-Legion-5-16IRX9 python[2428884]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:51:14 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:51:14 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:51:19 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 18.
Jul 03 15:51:19 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:51:20 cakidd-Legion-5-16IRX9 python[2428893]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:51:20 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:51:20 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:51:25 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 19.
Jul 03 15:51:25 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:51:26 cakidd-Legion-5-16IRX9 python[2428991]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:51:26 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:51:26 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:51:26 cakidd-Legion-5-16IRX9 sudo[2429000]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/sed -n 1,200p /etc/systemd/system/ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:51:26 cakidd-Legion-5-16IRX9 sudo[2429173]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl reset-failed ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:51:26 cakidd-Legion-5-16IRX9 sudo[2429177]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl stop ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:51:26 cakidd-Legion-5-16IRX9 systemd[1]: Stopped ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:51:26 cakidd-Legion-5-16IRX9 sudo[2429181]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/fuser -k <font color="#C01C28"><b>8095</b></font>/tcp
Jul 03 15:51:28 cakidd-Legion-5-16IRX9 sudo[2429205]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl start ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:51:28 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:51:29 cakidd-Legion-5-16IRX9 python[2429209]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:51:32 cakidd-Legion-5-16IRX9 systemd[1]: Starting ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>)...
Jul 03 15:51:32 cakidd-Legion-5-16IRX9 bash[2429240]: <font color="#C01C28"><b>8095</b></font>/tcp:            2429209
Jul 03 15:51:32 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>).
Jul 03 15:51:32 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=killed, status=9/KILL
Jul 03 15:51:32 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;signal&apos;.
Jul 03 15:51:32 cakidd-Legion-5-16IRX9 sudo[2429246]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/lsof -iTCP:<font color="#C01C28"><b>8095</b></font> -sTCP:LISTEN -nP
Jul 03 15:51:32 cakidd-Legion-5-16IRX9 python[2429241]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:51:37 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 1.
Jul 03 15:51:37 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:51:37 cakidd-Legion-5-16IRX9 python[2429451]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:51:38 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:51:38 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:51:43 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 2.
Jul 03 15:51:43 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:51:43 cakidd-Legion-5-16IRX9 python[2429519]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:51:44 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:51:44 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:51:49 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 3.
Jul 03 15:51:49 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:51:49 cakidd-Legion-5-16IRX9 python[2429539]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:51:50 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:51:50 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:51:55 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 4.
Jul 03 15:51:55 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:51:55 cakidd-Legion-5-16IRX9 python[2429636]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:51:56 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:51:56 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:52:01 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 5.
Jul 03 15:52:01 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:52:01 cakidd-Legion-5-16IRX9 python[2429694]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:52:02 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:52:02 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:52:07 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 6.
Jul 03 15:52:07 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:52:07 cakidd-Legion-5-16IRX9 python[2429728]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:52:08 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:52:08 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:52:13 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 7.
Jul 03 15:52:13 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:52:13 cakidd-Legion-5-16IRX9 python[2429795]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:52:14 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:52:14 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:52:18 cakidd-Legion-5-16IRX9 sudo[2429875]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/sed -n 1,200p /etc/systemd/system/ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:52:19 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 8.
Jul 03 15:52:19 cakidd-Legion-5-16IRX9 sudo[2430045]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl reset-failed ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:52:19 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:52:19 cakidd-Legion-5-16IRX9 sudo[2430049]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl stop ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:52:19 cakidd-Legion-5-16IRX9 systemd[1]: Stopping ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run)...
Jul 03 15:52:19 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Deactivated successfully.
Jul 03 15:52:19 cakidd-Legion-5-16IRX9 systemd[1]: Stopped ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:52:19 cakidd-Legion-5-16IRX9 sudo[2430054]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/fuser -k <font color="#C01C28"><b>8095</b></font>/tcp
Jul 03 15:52:21 cakidd-Legion-5-16IRX9 sudo[2430080]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl start ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:52:21 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:52:22 cakidd-Legion-5-16IRX9 python[2430084]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:52:24 cakidd-Legion-5-16IRX9 systemd[1]: Starting ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>)...
Jul 03 15:52:24 cakidd-Legion-5-16IRX9 bash[2430095]: <font color="#C01C28"><b>8095</b></font>/tcp:            2430084
Jul 03 15:52:24 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>).
Jul 03 15:52:24 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=killed, status=9/KILL
Jul 03 15:52:24 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;signal&apos;.
Jul 03 15:52:25 cakidd-Legion-5-16IRX9 python[2430097]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:52:25 cakidd-Legion-5-16IRX9 sudo[2430105]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/lsof -iTCP:<font color="#C01C28"><b>8095</b></font> -sTCP:LISTEN -nP
Jul 03 15:52:29 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 1.
Jul 03 15:52:29 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:52:30 cakidd-Legion-5-16IRX9 python[2430139]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:52:30 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:52:30 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:52:35 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 2.
Jul 03 15:52:35 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:52:36 cakidd-Legion-5-16IRX9 python[2430210]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:52:36 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:52:36 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:52:36 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Consumed 1.079s CPU time.
Jul 03 15:52:41 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 3.
Jul 03 15:52:41 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:52:42 cakidd-Legion-5-16IRX9 python[2430515]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:52:42 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:52:42 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:52:47 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 4.
Jul 03 15:52:47 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:52:48 cakidd-Legion-5-16IRX9 python[2430588]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:52:48 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:52:48 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:52:53 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 5.
Jul 03 15:52:53 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:52:54 cakidd-Legion-5-16IRX9 python[2430623]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:52:54 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:52:54 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:52:59 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 6.
Jul 03 15:52:59 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:53:00 cakidd-Legion-5-16IRX9 python[2430656]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:53:00 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:53:00 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:53:05 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 7.
Jul 03 15:53:05 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:53:06 cakidd-Legion-5-16IRX9 python[2430705]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:53:06 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:53:06 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:53:11 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 8.
Jul 03 15:53:11 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:53:12 cakidd-Legion-5-16IRX9 python[2430913]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:53:12 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:53:12 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:53:17 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 9.
Jul 03 15:53:17 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:53:18 cakidd-Legion-5-16IRX9 python[2430924]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:53:18 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:53:18 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:53:23 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 10.
Jul 03 15:53:23 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:53:24 cakidd-Legion-5-16IRX9 python[2430954]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:53:24 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:53:24 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:53:29 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 11.
Jul 03 15:53:29 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:53:29 cakidd-Legion-5-16IRX9 python[2430986]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:53:30 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:53:30 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:53:35 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 12.
Jul 03 15:53:35 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:53:35 cakidd-Legion-5-16IRX9 python[2431017]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:53:36 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:53:36 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:53:41 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 13.
Jul 03 15:53:41 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:53:41 cakidd-Legion-5-16IRX9 python[2431331]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:53:41 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:53:41 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:53:47 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 14.
Jul 03 15:53:47 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:53:47 cakidd-Legion-5-16IRX9 python[2431364]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:53:47 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:53:47 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:53:53 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 15.
Jul 03 15:53:53 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:53:53 cakidd-Legion-5-16IRX9 python[2431394]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:53:53 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:53:53 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:53:59 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 16.
Jul 03 15:53:59 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:53:59 cakidd-Legion-5-16IRX9 python[2431490]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:53:59 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:53:59 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:54:05 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 17.
Jul 03 15:54:05 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:54:05 cakidd-Legion-5-16IRX9 python[2431524]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:54:05 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:54:05 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:54:11 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 18.
Jul 03 15:54:11 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:54:11 cakidd-Legion-5-16IRX9 python[2431573]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:54:11 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:54:11 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:54:13 cakidd-Legion-5-16IRX9 sudo[2431625]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/sed -n 1,200p /etc/systemd/system/ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:54:13 cakidd-Legion-5-16IRX9 sudo[2431796]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl reset-failed ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:54:13 cakidd-Legion-5-16IRX9 sudo[2431799]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl stop ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:54:14 cakidd-Legion-5-16IRX9 systemd[1]: Stopped ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:54:14 cakidd-Legion-5-16IRX9 sudo[2431803]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/fuser -k <font color="#C01C28"><b>8095</b></font>/tcp
Jul 03 15:54:16 cakidd-Legion-5-16IRX9 sudo[2431812]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl start ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:54:16 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:54:16 cakidd-Legion-5-16IRX9 uvicorn[2431816]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:54:19 cakidd-Legion-5-16IRX9 systemd[1]: Starting ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>)...
Jul 03 15:54:19 cakidd-Legion-5-16IRX9 bash[2431829]: <font color="#C01C28"><b>8095</b></font>/tcp:            2431816
Jul 03 15:54:19 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>).
Jul 03 15:54:19 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=killed, status=9/KILL
Jul 03 15:54:19 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;signal&apos;.
Jul 03 15:54:20 cakidd-Legion-5-16IRX9 python[2431830]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:54:24 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 1.
Jul 03 15:54:24 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:54:25 cakidd-Legion-5-16IRX9 uvicorn[2431863]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:54:25 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:54:25 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:54:26 cakidd-Legion-5-16IRX9 sudo[2431872]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/lsof -iTCP:<font color="#C01C28"><b>8095</b></font> -sTCP:LISTEN -nP
Jul 03 15:54:30 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 2.
Jul 03 15:54:30 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:54:31 cakidd-Legion-5-16IRX9 uvicorn[2431973]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:54:31 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:54:31 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:54:36 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 3.
Jul 03 15:54:36 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:54:37 cakidd-Legion-5-16IRX9 uvicorn[2432025]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:54:37 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:54:37 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:54:42 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 4.
Jul 03 15:54:42 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:54:43 cakidd-Legion-5-16IRX9 uvicorn[2432208]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:54:43 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:54:43 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:54:43 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Consumed 1.068s CPU time.
Jul 03 15:54:48 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 5.
Jul 03 15:54:48 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:54:49 cakidd-Legion-5-16IRX9 uvicorn[2432323]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:54:49 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:54:49 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:54:54 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 6.
Jul 03 15:54:54 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:54:55 cakidd-Legion-5-16IRX9 uvicorn[2432426]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:54:55 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:54:55 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:55:00 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 7.
Jul 03 15:55:00 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:55:01 cakidd-Legion-5-16IRX9 uvicorn[2432455]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:55:01 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:55:01 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:55:06 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 8.
Jul 03 15:55:06 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:55:07 cakidd-Legion-5-16IRX9 uvicorn[2433830]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:55:07 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:55:07 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:55:08 cakidd-Legion-5-16IRX9 sudo[2434056]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/sed -n 1,200p /etc/systemd/system/ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:55:08 cakidd-Legion-5-16IRX9 sudo[2434319]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl reset-failed ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:55:08 cakidd-Legion-5-16IRX9 sudo[2434323]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl stop ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:55:08 cakidd-Legion-5-16IRX9 systemd[1]: Stopped ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:55:08 cakidd-Legion-5-16IRX9 sudo[2434327]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/fuser -k <font color="#C01C28"><b>8095</b></font>/tcp
Jul 03 15:55:10 cakidd-Legion-5-16IRX9 sudo[2434533]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl start ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:55:10 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:55:11 cakidd-Legion-5-16IRX9 python[2434543]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:55:14 cakidd-Legion-5-16IRX9 systemd[1]: Starting ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>)...
Jul 03 15:55:14 cakidd-Legion-5-16IRX9 bash[2434612]: <font color="#C01C28"><b>8095</b></font>/tcp:            2434543
Jul 03 15:55:14 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>).
Jul 03 15:55:14 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=killed, status=9/KILL
Jul 03 15:55:14 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;signal&apos;.
Jul 03 15:55:14 cakidd-Legion-5-16IRX9 python[2434613]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:55:17 cakidd-Legion-5-16IRX9 sudo[2434642]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/lsof -iTCP:<font color="#C01C28"><b>8095</b></font> -sTCP:LISTEN -nP
Jul 03 15:55:19 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 1.
Jul 03 15:55:19 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:55:19 cakidd-Legion-5-16IRX9 python[2434650]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:55:20 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:55:20 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:55:25 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 2.
Jul 03 15:55:25 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:55:25 cakidd-Legion-5-16IRX9 python[2434747]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:55:26 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:55:26 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:55:31 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 3.
Jul 03 15:55:31 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:55:31 cakidd-Legion-5-16IRX9 python[2434779]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:55:31 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:55:31 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:55:37 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 4.
Jul 03 15:55:37 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:55:37 cakidd-Legion-5-16IRX9 python[2434832]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:55:37 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:55:37 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:55:42 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 5.
Jul 03 15:55:42 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:55:43 cakidd-Legion-5-16IRX9 python[2434954]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:55:43 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:55:43 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:55:48 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 6.
Jul 03 15:55:48 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:55:49 cakidd-Legion-5-16IRX9 python[2435248]: ERROR:    [Errno 98] error while attempting to bind on address (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>): address already in use
Jul 03 15:55:49 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:55:49 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:55:52 cakidd-Legion-5-16IRX9 sudo[2435261]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/sed -n 1,200p /etc/systemd/system/ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:55:52 cakidd-Legion-5-16IRX9 sudo[2435451]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl reset-failed ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:55:52 cakidd-Legion-5-16IRX9 sudo[2435454]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl stop ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:55:52 cakidd-Legion-5-16IRX9 systemd[1]: Stopped ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:55:52 cakidd-Legion-5-16IRX9 sudo[2435458]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/fuser -k <font color="#C01C28"><b>8095</b></font>/tcp
Jul 03 15:55:54 cakidd-Legion-5-16IRX9 sudo[2435463]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl start ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:55:54 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:55:55 cakidd-Legion-5-16IRX9 python[2435467]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:55:58 cakidd-Legion-5-16IRX9 systemd[1]: Starting ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>)...
Jul 03 15:55:58 cakidd-Legion-5-16IRX9 bash[2435478]: <font color="#C01C28"><b>8095</b></font>/tcp:            2435467
Jul 03 15:55:58 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>).
Jul 03 15:55:58 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=killed, status=9/KILL
Jul 03 15:55:58 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;signal&apos;.
Jul 03 15:55:58 cakidd-Legion-5-16IRX9 python[2435479]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:55:59 cakidd-Legion-5-16IRX9 sudo[2435506]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/lsof -iTCP:<font color="#C01C28"><b>8095</b></font> -sTCP:LISTEN -nP
Jul 03 15:56:38 cakidd-Legion-5-16IRX9 sudo[2435940]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/sed -n 1,200p /etc/systemd/system/ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:56:38 cakidd-Legion-5-16IRX9 sudo[2436110]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl reset-failed ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:56:38 cakidd-Legion-5-16IRX9 sudo[2436113]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl stop ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:56:38 cakidd-Legion-5-16IRX9 sudo[2436117]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/fuser -k <font color="#C01C28"><b>8095</b></font>/tcp
Jul 03 15:56:40 cakidd-Legion-5-16IRX9 sudo[2436125]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl start ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:56:40 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:56:41 cakidd-Legion-5-16IRX9 python[2436129]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:56:44 cakidd-Legion-5-16IRX9 systemd[1]: Starting ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>)...
Jul 03 15:56:44 cakidd-Legion-5-16IRX9 bash[2436158]: <font color="#C01C28"><b>8095</b></font>/tcp:            2436129
Jul 03 15:56:44 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>).
Jul 03 15:56:44 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Deactivated successfully.
Jul 03 15:56:44 cakidd-Legion-5-16IRX9 python[2436159]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:56:48 cakidd-Legion-5-16IRX9 sudo[2436292]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/lsof -iTCP:<font color="#C01C28"><b>8095</b></font> -sTCP:LISTEN -nP
Jul 03 15:58:14 cakidd-Legion-5-16IRX9 sudo[2437376]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/tee /etc/systemd/system/ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:58:14 cakidd-Legion-5-16IRX9 sudo[2437546]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl reset-failed ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:58:14 cakidd-Legion-5-16IRX9 sudo[2437549]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl stop ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:58:14 cakidd-Legion-5-16IRX9 sudo[2437553]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/fuser -k <font color="#C01C28"><b>8095</b></font>/tcp
Jul 03 15:58:16 cakidd-Legion-5-16IRX9 sudo[2437558]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl start ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:58:16 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:58:16 cakidd-Legion-5-16IRX9 uvicorn[2437562]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:58:19 cakidd-Legion-5-16IRX9 systemd[1]: Starting ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>)...
Jul 03 15:58:19 cakidd-Legion-5-16IRX9 bash[2437578]: <font color="#C01C28"><b>8095</b></font>/tcp:            2437562 2437565 2437566
Jul 03 15:58:19 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>).
Jul 03 15:58:19 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=killed, status=9/KILL
Jul 03 15:58:19 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;signal&apos;.
Jul 03 15:58:19 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Consumed 1.434s CPU time.
Jul 03 15:58:20 cakidd-Legion-5-16IRX9 python[2437579]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:58:25 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 1.
Jul 03 15:58:25 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:58:25 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:58:25 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:58:26 cakidd-Legion-5-16IRX9 sudo[2437632]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/lsof -iTCP:<font color="#C01C28"><b>8095</b></font> -sTCP:LISTEN -nP
Jul 03 15:58:30 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 2.
Jul 03 15:58:30 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:58:30 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:58:30 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:58:35 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 3.
Jul 03 15:58:35 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:58:35 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:58:35 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:58:40 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 4.
Jul 03 15:58:40 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:58:40 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:58:40 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:58:46 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 5.
Jul 03 15:58:46 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:58:46 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:58:46 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:58:51 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 6.
Jul 03 15:58:51 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:58:51 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:58:51 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:58:56 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 7.
Jul 03 15:58:56 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:58:56 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:58:56 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:59:01 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 8.
Jul 03 15:59:01 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:59:01 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:59:01 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:59:07 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 9.
Jul 03 15:59:07 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:59:07 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:59:07 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:59:09 cakidd-Legion-5-16IRX9 sudo[2438449]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl reset-failed ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:59:09 cakidd-Legion-5-16IRX9 sudo[2438453]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl stop ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:59:09 cakidd-Legion-5-16IRX9 systemd[1]: Stopped ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:59:09 cakidd-Legion-5-16IRX9 sudo[2438457]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/pkill -9 -f &apos;/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python -m <font color="#C01C28"><b>uvicorn auth_api:app</b></font> --host 127.0.0.1 --port <font color="#C01C28"><b>8095</b></font>&apos;
Jul 03 15:59:09 cakidd-Legion-5-16IRX9 sudo[2438465]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/pkill -9 -f &apos;/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/<font color="#C01C28"><b>uvicorn auth_api:app</b></font> --host 127.0.0.1 --port <font color="#C01C28"><b>8095</b></font>&apos;
Jul 03 15:59:09 cakidd-Legion-5-16IRX9 sudo[2438468]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/fuser -k <font color="#C01C28"><b>8095</b></font>/tcp
Jul 03 15:59:11 cakidd-Legion-5-16IRX9 sudo[2438473]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/lsof -iTCP:<font color="#C01C28"><b>8095</b></font> -sTCP:LISTEN -nP
Jul 03 15:59:11 cakidd-Legion-5-16IRX9 sudo[2438481]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl start ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 15:59:11 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:59:11 cakidd-Legion-5-16IRX9 uvicorn[2438485]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:59:14 cakidd-Legion-5-16IRX9 systemd[1]: Starting ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>)...
Jul 03 15:59:14 cakidd-Legion-5-16IRX9 bash[2438514]: <font color="#C01C28"><b>8095</b></font>/tcp:            2438485 2438488 2438489
Jul 03 15:59:14 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>).
Jul 03 15:59:14 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=killed, status=9/KILL
Jul 03 15:59:14 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;signal&apos;.
Jul 03 15:59:14 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Consumed 1.436s CPU time.
Jul 03 15:59:14 cakidd-Legion-5-16IRX9 sudo[2438519]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/lsof -iTCP:<font color="#C01C28"><b>8095</b></font> -sTCP:LISTEN -nP
Jul 03 15:59:15 cakidd-Legion-5-16IRX9 python[2438516]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 15:59:19 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 1.
Jul 03 15:59:19 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:59:19 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:59:19 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:59:24 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 2.
Jul 03 15:59:24 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:59:24 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:59:24 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:59:30 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 3.
Jul 03 15:59:30 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:59:30 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:59:30 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:59:35 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 4.
Jul 03 15:59:35 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:59:35 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:59:35 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:59:40 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 5.
Jul 03 15:59:40 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:59:40 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:59:40 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:59:45 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 6.
Jul 03 15:59:45 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:59:45 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:59:45 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:59:51 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 7.
Jul 03 15:59:51 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:59:51 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:59:51 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 15:59:56 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 8.
Jul 03 15:59:56 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 15:59:56 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 15:59:56 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 16:00:01 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 9.
Jul 03 16:00:01 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 16:00:02 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 16:00:02 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 16:00:07 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 10.
Jul 03 16:00:07 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 16:00:08 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 16:00:08 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 16:00:13 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 11.
Jul 03 16:00:13 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 16:00:14 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 16:00:14 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 16:00:17 cakidd-Legion-5-16IRX9 sudo[2441474]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/tee /etc/systemd/system/ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 16:00:19 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 12.
Jul 03 16:00:19 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 16:00:20 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 16:00:20 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 16:00:25 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 13.
Jul 03 16:00:25 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 16:00:26 cakidd-Legion-5-16IRX9 sudo[2441675]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl reset-failed ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 16:00:26 cakidd-Legion-5-16IRX9 sudo[2441678]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl stop ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 16:00:26 cakidd-Legion-5-16IRX9 systemd[1]: Stopping ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run)...
Jul 03 16:00:26 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Deactivated successfully.
Jul 03 16:00:26 cakidd-Legion-5-16IRX9 systemd[1]: Stopped ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 16:00:26 cakidd-Legion-5-16IRX9 sudo[2441683]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/pkill -9 -f &apos;/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python -m <font color="#C01C28"><b>uvicorn auth_api:app</b></font> --host 127.0.0.1 --port <font color="#C01C28"><b>8095</b></font>&apos;
Jul 03 16:00:26 cakidd-Legion-5-16IRX9 sudo[2441690]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/pkill -9 -f &apos;/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/<font color="#C01C28"><b>uvicorn auth_api:app</b></font> --host 127.0.0.1 --port <font color="#C01C28"><b>8095</b></font>&apos;
Jul 03 16:00:26 cakidd-Legion-5-16IRX9 sudo[2441693]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/pkill -9 -f &apos;/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/<font color="#C01C28"><b>gunicorn auth_api:app</b></font>&apos;
Jul 03 16:00:26 cakidd-Legion-5-16IRX9 sudo[2441696]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/fuser -k <font color="#C01C28"><b>8095</b></font>/tcp
Jul 03 16:00:28 cakidd-Legion-5-16IRX9 sudo[2441701]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/lsof -iTCP:<font color="#C01C28"><b>8095</b></font> -sTCP:LISTEN -nP
Jul 03 16:00:28 cakidd-Legion-5-16IRX9 sudo[2441705]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/systemctl start ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service
Jul 03 16:00:28 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 16:00:28 cakidd-Legion-5-16IRX9 gunicorn[2441709]: [2026-07-03 16:00:28 -0400] [2441709] [INFO] Listening at: http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (2441709)
Jul 03 16:00:31 cakidd-Legion-5-16IRX9 systemd[1]: Starting ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>)...
Jul 03 16:00:31 cakidd-Legion-5-16IRX9 bash[2441754]: <font color="#C01C28"><b>8095</b></font>/tcp:            2441709 2441711 2441712
Jul 03 16:00:31 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth-router.service - Ms Allis Auth Router (port <font color="#C01C28"><b>8095</b></font>).
Jul 03 16:00:31 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=killed, status=9/KILL
Jul 03 16:00:31 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;signal&apos;.
Jul 03 16:00:31 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Consumed 1.259s CPU time.
Jul 03 16:00:31 cakidd-Legion-5-16IRX9 sudo[2441759]:   cakidd : TTY=pts/0 ; PWD=/mnt/spiritual_drive/msjarvis-rebuild ; USER=root ; COMMAND=/usr/bin/lsof -iTCP:<font color="#C01C28"><b>8095</b></font> -sTCP:LISTEN -nP
Jul 03 16:00:32 cakidd-Legion-5-16IRX9 python[<font color="#C01C28"><b>2441755</b></font>]: INFO:     Started server process [<font color="#C01C28"><b>2441755</b></font>]
Jul 03 16:00:32 cakidd-Legion-5-16IRX9 python[<font color="#C01C28"><b>2441755</b></font>]: INFO:     Waiting for application startup.
Jul 03 16:00:32 cakidd-Legion-5-16IRX9 python[<font color="#C01C28"><b>2441755</b></font>]: INFO:     Application startup complete.
Jul 03 16:00:32 cakidd-Legion-5-16IRX9 python[<font color="#C01C28"><b>2441755</b></font>]: INFO:     Uvicorn running on http://127.0.0.1:<font color="#C01C28"><b>8095</b></font> (Press CTRL+C to quit)
Jul 03 16:00:36 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 1.
Jul 03 16:00:36 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 16:00:36 cakidd-Legion-5-16IRX9 gunicorn[2441803]: [2026-07-03 16:00:36 -0400] [2441803] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:36 cakidd-Legion-5-16IRX9 gunicorn[2441803]: [2026-07-03 16:00:36 -0400] [2441803] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:00:37 cakidd-Legion-5-16IRX9 gunicorn[2441803]: [2026-07-03 16:00:37 -0400] [2441803] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:37 cakidd-Legion-5-16IRX9 gunicorn[2441803]: [2026-07-03 16:00:37 -0400] [2441803] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:00:38 cakidd-Legion-5-16IRX9 gunicorn[2441803]: [2026-07-03 16:00:38 -0400] [2441803] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:38 cakidd-Legion-5-16IRX9 gunicorn[2441803]: [2026-07-03 16:00:38 -0400] [2441803] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:00:39 cakidd-Legion-5-16IRX9 gunicorn[2441803]: [2026-07-03 16:00:39 -0400] [2441803] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:39 cakidd-Legion-5-16IRX9 gunicorn[2441803]: [2026-07-03 16:00:39 -0400] [2441803] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:00:40 cakidd-Legion-5-16IRX9 gunicorn[2441803]: [2026-07-03 16:00:40 -0400] [2441803] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:40 cakidd-Legion-5-16IRX9 gunicorn[2441803]: [2026-07-03 16:00:40 -0400] [2441803] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:00:41 cakidd-Legion-5-16IRX9 gunicorn[2441803]: [2026-07-03 16:00:41 -0400] [2441803] [ERROR] Can&apos;t connect to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:41 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 16:00:41 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 16:00:46 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 2.
Jul 03 16:00:46 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 16:00:46 cakidd-Legion-5-16IRX9 gunicorn[2441937]: [2026-07-03 16:00:46 -0400] [2441937] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:46 cakidd-Legion-5-16IRX9 gunicorn[2441937]: [2026-07-03 16:00:46 -0400] [2441937] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:00:47 cakidd-Legion-5-16IRX9 gunicorn[2441937]: [2026-07-03 16:00:47 -0400] [2441937] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:47 cakidd-Legion-5-16IRX9 gunicorn[2441937]: [2026-07-03 16:00:47 -0400] [2441937] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:00:48 cakidd-Legion-5-16IRX9 gunicorn[2441937]: [2026-07-03 16:00:48 -0400] [2441937] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:48 cakidd-Legion-5-16IRX9 gunicorn[2441937]: [2026-07-03 16:00:48 -0400] [2441937] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:00:49 cakidd-Legion-5-16IRX9 gunicorn[2441937]: [2026-07-03 16:00:49 -0400] [2441937] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:49 cakidd-Legion-5-16IRX9 gunicorn[2441937]: [2026-07-03 16:00:49 -0400] [2441937] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:00:50 cakidd-Legion-5-16IRX9 gunicorn[2441937]: [2026-07-03 16:00:50 -0400] [2441937] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:50 cakidd-Legion-5-16IRX9 gunicorn[2441937]: [2026-07-03 16:00:50 -0400] [2441937] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:00:51 cakidd-Legion-5-16IRX9 gunicorn[2441937]: [2026-07-03 16:00:51 -0400] [2441937] [ERROR] Can&apos;t connect to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:51 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 16:00:51 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
Jul 03 16:00:57 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Scheduled restart job, restart counter is at 3.
Jul 03 16:00:57 cakidd-Legion-5-16IRX9 systemd[1]: Started ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service - MS Allis Auth <font color="#C01C28"><b>8095</b></font> (host-run).
Jul 03 16:00:57 cakidd-Legion-5-16IRX9 gunicorn[2442114]: [2026-07-03 16:00:57 -0400] [2442114] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:57 cakidd-Legion-5-16IRX9 gunicorn[2442114]: [2026-07-03 16:00:57 -0400] [2442114] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:00:58 cakidd-Legion-5-16IRX9 gunicorn[2442114]: [2026-07-03 16:00:58 -0400] [2442114] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:58 cakidd-Legion-5-16IRX9 gunicorn[2442114]: [2026-07-03 16:00:58 -0400] [2442114] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:00:59 cakidd-Legion-5-16IRX9 gunicorn[2442114]: [2026-07-03 16:00:59 -0400] [2442114] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:00:59 cakidd-Legion-5-16IRX9 gunicorn[2442114]: [2026-07-03 16:00:59 -0400] [2442114] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:01:00 cakidd-Legion-5-16IRX9 gunicorn[2442114]: [2026-07-03 16:01:00 -0400] [2442114] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:01:00 cakidd-Legion-5-16IRX9 gunicorn[2442114]: [2026-07-03 16:01:00 -0400] [2442114] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:01:01 cakidd-Legion-5-16IRX9 gunicorn[2442114]: [2026-07-03 16:01:01 -0400] [2442114] [ERROR] Connection in use: (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:01:01 cakidd-Legion-5-16IRX9 gunicorn[2442114]: [2026-07-03 16:01:01 -0400] [2442114] [ERROR] connection to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>) failed: [Errno 98] Address already in use
Jul 03 16:01:02 cakidd-Legion-5-16IRX9 gunicorn[2442114]: [2026-07-03 16:01:02 -0400] [2442114] [ERROR] Can&apos;t connect to (&apos;127.0.0.1&apos;, <font color="#C01C28"><b>8095</b></font>)
Jul 03 16:01:02 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Main process exited, code=exited, status=1/FAILURE
Jul 03 16:01:02 cakidd-Legion-5-16IRX9 systemd[1]: ms-allis-auth<font color="#C01C28"><b>8095</b></font>.service: Failed with result &apos;exit-code&apos;.
2441755 /mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/python -m uvicorn auth_api:app --host 127.0.0.1 --port 8095
# Ms. Jarvis Master Crontab

*/5 * * * * /usr/local/bin/jarvis_bbb_watchdog.sh
*/15 * * * * cd /mnt/spiritual_drive/msjarvis-rebuild &amp;&amp; ./scripts/watchdog-containers.sh
*/15 * * * * /home/cakidd/msjarvis-monitoring/monitor_services.sh
*/30 * * * * /home/cakidd/msjarvis-monitoring/monitor_databases.sh
0 * * * * /home/cakidd/msjarvis-monitoring/monitor_disk.sh
0 */6 * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/run_aaacpe_scraper.sh
0 2 * * * docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c &quot;REFRESH MATERIALIZED VIEW CONCURRENTLY county_tax_building_summary&quot; &gt;&gt; /var/log/jarvis_mv_refresh.log 2&gt;&amp;1
0 2 * * * /mnt/spiritual_drive/msjarvis-rebuild/backup_postgresql.sh &gt;&gt; /home/cakidd/logs/backup_postgresql.log 2&gt;&amp;1
0 2 * * * cd /mnt/spiritual_drive/msjarvis-rebuild &amp;&amp; bash scripts/refresh_gbim_spatial.sh &gt;&gt; logs/gbim_refresh.log 2&gt;&amp;1
# DISABLED - copies 0-byte sqlite3, useless: 0 2 * * * cp /home/ms-jarvis/msjarvis-rebuild/persistent/chroma/chroma.sqlite3 &quot;/mnt/nvme1/msjarvis-backups/chromadb/chroma-$(date +%Y%m%d-%H%M%S).sqlite3&quot;
0 3 * * 0 docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c &quot;REFRESH MATERIALIZED VIEW CONCURRENTLY building_parcel_county_tax_mv&quot; &gt;&gt; /var/log/jarvis_mv_refresh.log 2&gt;&amp;1
# DISABLED - 77GB rsync too large, chroma-live is the live mount, postgresql backups confirmed current: 0 3 * * * rsync -a /home/ms-jarvis/msjarvis-rebuild/persistent/chroma/ /mnt/nvme1/msjarvis-backups/chromadb/chroma-latest/ &gt;&gt; /tmp/chroma_backup.log 2&gt;&amp;1
0 3 * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/refresh_mvw.sh &gt;&gt; /var/log/mvw_refresh.log 2&gt;&amp;1
0 3 * * * python3 /mnt/spiritual_drive/msjarvis-rebuild/services/identity_promotion.py &gt;&gt; /var/log/jarvis/identity_promotion.log 2&gt;&amp;1
0 4 * * * /mnt/spiritual_drive/msjarvis-rebuild/backup_configs.sh &gt;&gt; /home/cakidd/logs/backup_configs.log 2&gt;&amp;1
0 8 * * 1 cd /mnt/spiritual_drive/msjarvis-rebuild &amp;&amp; bash scripts/pia/run_pia_audit.sh &gt;&gt; /var/log/msjarvis-pia.log 2&gt;&amp;1
# NEEDS_PARAMS: 0 1 * * * curl -sf -X POST http://localhost:8099/policy/set -H &quot;Content-Type: application/json&quot; -d &quot;{}&quot; &gt;&gt; /var/log/jarvis/policy_update.log 2&gt;&amp;1
0 2 * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/gbim_decay_tick.sh &gt;&gt; /var/log/gbim_decay.log 2&gt;&amp;1
# RETENTION - Keep only last 2 ChromaDB main tarballs (~6.6G cap)
30 4 * * * find /mnt/nvme1/msjarvis-backups/chromadb -name &quot;chroma_main_*.tar.gz&quot; -mtime +2 -delete
# MAINTENANCE - Weekly Docker build cache prune, keep 10GB headroom
0 3 * * 0 /usr/bin/docker builder prune -f --keep-storage 10GB &gt;&gt; /tmp/docker_prune.log 2&gt;&amp;1
0 2 * * 0 cd /mnt/spiritual_drive/msjarvis-rebuild &amp;&amp; .venv/bin/python3 scripts/audit_happiness_v2.py &gt;&gt; logs/manipulation_proximity_audit.log 2&gt;&amp;1
0 */6 * * * /home/cakidd/scripts/local_resources_gap_report.sh &gt;&gt; /home/cakidd/allis-reports/coverage-gaps/gap-report.log 2&gt;&amp;1
*/5 * * * * /mnt/spiritual_drive/msjarvis-rebuild/scripts/check_proxies.sh &gt;&gt; /home/cakidd/logs/msjarvis-proxy-health.log 2&gt;&amp;1
#PAUSED */30 * * * * tail -1 /mnt/spiritual_drive/msjarvis-rebuild/migration.log &gt;&gt; /mnt/spiritual_drive/msjarvis-rebuild/progress_history.log
17 2 * * * /home/cakidd/.local/bin/purge-kyc-location-strip.sh

# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use &apos;*&apos; in these fields (for &apos;any&apos;).
# 
# Notice that tasks will be started based on the cron&apos;s system
# daemon&apos;s notion of time and timezones.
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
0 2 * * * docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c &quot;REFRESH MATERIALIZED VIEW CONCURRENTLY county_tax_building_summary&quot; &gt;&gt; /var/log/jarvis_mv_refresh.log 2&gt;&amp;1
  <font color="#C01C28"><b>auth</b></font>-8055-forward.service                                        loaded    active   running Forward 127.0.0.1:8055 to 127.0.0.1:<font color="#C01C28"><b>8095</b></font>
● <font color="#C01C28"><b>jarvis</b></font>-preflight.service                                         loaded    failed   failed  Ms. Jarvis Pre-Flight Gate
● <font color="#C01C28"><b>jarvis</b></font>-verify.service                                            loaded    failed   failed  Ms. Jarvis Full Regression Verify
<font color="#C01C28"><b>auth</b></font>-8055-forward.service                                         enabled   enabled
flatpak-oci-<font color="#C01C28"><b>auth</b></font>enticator.service                                 static    -
<font color="#C01C28"><b>jarvis</b></font>-preflight.service                                          static    -
<font color="#C01C28"><b>jarvis</b></font>-verify.service                                             static    -
ms<font color="#C01C28"><b>jarvis</b></font>-<font color="#C01C28"><b>auth</b></font>-8055.service                                        disabled  enabled
<font color="#C01C28"><b>jarvis</b></font>-preflight.timer                                            enabled   enabled
<font color="#C01C28"><b>jarvis</b></font>-verify.timer                                               enabled   enabled
(crypto-venv) <font color="#26A269"><b>cakidd@cakidd-Legion-5-16IRX9</b></font>:<font color="#12488B"><b>/mnt/spiritual_drive/msjarvis-rebuild</b></font>$ 

</pre>
