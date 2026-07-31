(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiri(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild
{ echo '--- get_current_user ---'
  echo '--- get_current_user ---'--include='*.py' | head -n 50
  grep -Rni 'get_current_user' . --include='*.py' | head -n 50
  echo '--- current_user ---'
  echo '--- current_user ---'--include='*.py' | head -n 50
  grep -Rni 'current_user' . --include='*.py' | head -n 50
  echo '--- Authorization ---'
  echo '--- Authorization ---'--include='*.py' | head -n 50
  grep -Rni 'Authorization' . --include='*.py' | head -n 50
  echo '--- Bearer ---'
  echo '--- Bearer ---'--include='*.py' | head -n 50
  grep -Rni 'Bearer' . --include='*.py' | head -n 50
  echo '--- oauth2 ---'
  echo '--- oauth2 ---'--include='*.py' | head -n 50
  grep -Rni 'oauth2' . --include='*.py' | head -n 50
  echo '--- jwt ---'
  echo '--- jwt ---'--include='*.py' | head -n 50
  grep -Rni 'jwt' . --include='*.py' | head -n 50
  echo '--- Depends( ---'
  echo '--- Depends( ---'--include='*.py' | head -n 100
  grep -Rni 'Depends(' . --include='*.py' | head -n 100
} > auth_search_results.txt_results.txt
sed -n '1,220p' auth_search_results.txt
grep: ./msjarvis-rebuild: warning: recursive directory loop
grep: ./production_closeout_20260728/asbuilt_snapshot_20260728/repo/msjarvis-rebuild: warning: recursive directory loop
grep: ./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/msjarvis-rebuild: warning: recursive directory loop
grep: ./msjarvis-rebuild: warning: recursive directory loop
grep: ./production_closeout_20260728/asbuilt_snapshot_20260728/repo/msjarvis-rebuild: warning: recursive directory loop
grep: ./msjarvis-rebuild: warning: recursive directory loop
grep: ./production_closeout_20260728/asbuilt_snapshot_20260728/repo/msjarvis-rebuild: warning: recursive directory loop
grep: ./msjarvis-rebuild: warning: recursive directory loop
grep: ./production_closeout_20260728/asbuilt_snapshot_20260728/repo/msjarvis-rebuild: warning: recursive directory loop
grep: ./msjarvis-rebuild: warning: recursive directory loop
grep: ./production_closeout_20260728/asbuilt_snapshot_20260728/repo/msjarvis-rebuild: warning: recursive directory loop
grep: ./msjarvis-rebuild: warning: recursive directory loop
grep: ./production_closeout_20260728/asbuilt_snapshot_20260728/repo/msjarvis-rebuild: warning: recursive directory loop
grep: ./msjarvis-rebuild: warning: recursive directory loop
grep: ./production_closeout_20260728/asbuilt_snapshot_20260728/repo/msjarvis-rebuild: warning: recursive directory loop
--- get_current_user ---
./auth_api.patched.py:127:def _get_current_user(session_token: str | None) -> dict | None:
./auth_api.patched.py:209:    user = _get_current_user(msallis_session)
./auth_api.patched.py:236:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:127:def _get_current_user(session_token: str | None) -> dict | None:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:209:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:236:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api_no_full_router.py:125:def _get_current_user(session_token: str | None) -> dict | None:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api_no_full_router.py:224:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api_no_full_router.py:254:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/pygments/lexers/_php_builtins.py:1870:                      'get_current_user',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/tornado/web.py:1479:        * A subclass may override `get_current_user()`, which will be called
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/tornado/web.py:1481:          `get_current_user()` will only be called once per request,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/tornado/web.py:1484:              def get_current_user(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/tornado/web.py:1499:        Note that `prepare()` may be a coroutine while `get_current_user()`
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/tornado/web.py:1506:            self._current_user = self.get_current_user()
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/tornado/web.py:1513:    def get_current_user(self) -> Any:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/tornado/test/web_test.py:2141:        def get_current_user(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/tornado/test/web_test.py:2149:        # that want to forgo the lazy get_current_user property
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/tornado/test/web_test.py:2189:            def get_current_user(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/tornado/test/web_test.py:2206:                # get_current_user is evaluated. Until #820 is fixed, this
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/tornado/test/web_test.py:2228:    def test_get_current_user_is_lazy(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/tornado/test/web_test.py:2233:    def test_get_current_user_works(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/tornado/test/web_test.py:2237:    def test_get_current_user_from_ui_module_is_lazy(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/tornado/test/web_test.py:2241:    def test_get_current_user_from_ui_module_works(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py:1870:                      'get_current_user',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/tornado/web.py:1479:        * A subclass may override `get_current_user()`, which will be called
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/tornado/web.py:1481:          `get_current_user()` will only be called once per request,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/tornado/web.py:1484:              def get_current_user(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/tornado/web.py:1499:        Note that `prepare()` may be a coroutine while `get_current_user()`
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/tornado/web.py:1506:            self._current_user = self.get_current_user()
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/tornado/web.py:1513:    def get_current_user(self) -> Any:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/tornado/test/web_test.py:2141:        def get_current_user(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/tornado/test/web_test.py:2149:        # that want to forgo the lazy get_current_user property
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/tornado/test/web_test.py:2189:            def get_current_user(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/tornado/test/web_test.py:2206:                # get_current_user is evaluated. Until #820 is fixed, this
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/tornado/test/web_test.py:2228:    def test_get_current_user_is_lazy(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/tornado/test/web_test.py:2233:    def test_get_current_user_works(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/tornado/test/web_test.py:2237:    def test_get_current_user_from_ui_module_is_lazy(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/tornado/test/web_test.py:2241:    def test_get_current_user_from_ui_module_works(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.py:126:def _get_current_user(session_token: str | None) -> dict | None:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.py:225:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.py:255:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.check_venv/lib64/python3.12/site-packages/pygments/lexers/_php_builtins.py:1870:                      'get_current_user',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.check_venv/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py:1870:                      'get_current_user',
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_api.patched.py:127:def _get_current_user(session_token: str | None) -> dict | None:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_api.patched.py:209:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_api.patched.py:236:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_api_no_full_router.py:125:def _get_current_user(session_token: str | None) -> dict | None:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_api_no_full_router.py:224:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_api_no_full_router.py:254:    user = _get_current_user(msallis_session)

--- current_user ---
./auth_api.patched.py:127:def _get_current_user(session_token: str | None) -> dict | None:
./auth_api.patched.py:209:    user = _get_current_user(msallis_session)
./auth_api.patched.py:236:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:127:def _get_current_user(session_token: str | None) -> dict | None:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:209:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:236:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api_no_full_router.py:125:def _get_current_user(session_token: str | None) -> dict | None:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api_no_full_router.py:224:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api_no_full_router.py:254:    user = _get_current_user(msallis_session)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/debugpy/_vendored/pydevd/pydevd_attach_to_process/winappdbg/registry.py:393:        "HKCU": win32.HKEY_CURRENT_USER,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/debugpy/_vendored/pydevd/pydevd_attach_to_process/winappdbg/registry.py:400:        "HKEY_CURRENT_USER": win32.HKEY_CURRENT_USER,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/debugpy/_vendored/pydevd/pydevd_attach_to_process/winappdbg/registry.py:409:        win32.HKEY_CURRENT_USER: "HKEY_CURRENT_USER",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/debugpy/_vendored/pydevd/pydevd_attach_to_process/winappdbg/registry.py:444:             - L{win32.HKEY_CURRENT_USER}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/debugpy/_vendored/pydevd/pydevd_attach_to_process/winappdbg/registry.py:485:             - L{win32.HKEY_CURRENT_USER}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/debugpy/_vendored/pydevd/pydevd_attach_to_process/winappdbg/win32/advapi32.py:124:HKEY_CURRENT_USER = 0x80000001
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/debugpy/_vendored/pydevd/pydevd_attach_to_process/winappdbg/win32/advapi32.py:2264:    if value in (HKEY_CLASSES_ROOT, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, HKEY_USERS, HKEY_PERFORMANCE_DATA, HKEY_CURRENT_CONFIG):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/appdirs.py:472:        _winreg.HKEY_CURRENT_USER,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/fastapi/security/http.py:125:    def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/fastapi/security/http.py:245:    def read_current_user(
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/fastapi/security/http.py:349:    def read_current_user(
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/fastapi/param_functions.py:2355:        current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])]
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/fastapi/param_functions.py:2357:        return [{"item_id": "Foo", "owner": current_user.username}]
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/torch/_appdirs.py:514:        _winreg.HKEY_CURRENT_USER,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/requests/utils.py:107:                winreg.HKEY_CURRENT_USER,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/fakeredis/_basefakesocket.py:126:    def current_user(self) -> bytes:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/IPython/utils/path.py:185:                wreg.HKEY_CURRENT_USER,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/jedi/api/environment.py:414:        for root_key in [winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE]:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/dialects/postgresql/base.py:1721:    "current_user",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/dialects/postgresql/provision.py:69:                    "where usename=current_user and pid != pg_backend_pid() "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/dialects/postgresql/provision.py:125:        "usename=current_user "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/dialects/mysql/reserved_words.py:51:    "current_user",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/dialects/mysql/reserved_words.py:330:    "current_user",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/dialects/mssql/base.py:1089:    "current_user",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/sql/functions.py:1111:        def current_user(self) -> Type[_current_user_func]: ...
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/sql/functions.py:1858:class current_user(AnsiFunction[str]):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/sql/functions.py:1859:    """The CURRENT_USER() SQL function."""
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/sql/functions.py:2177:_current_user_func: TypeAlias = current_user
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/sql/compiler.py:175:    "current_user",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/sql/compiler.py:324:    functions.current_user: "CURRENT_USER",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/platformdirs/windows.py:256:    # Use HKEY_LOCAL_MACHINE for system-wide folders, HKEY_CURRENT_USER for user-specific folders
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/platformdirs/windows.py:257:    hkey = winreg.HKEY_LOCAL_MACHINE if csidl_name in machine_names else winreg.HKEY_CURRENT_USER
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/matplotlib/font_manager.py:206:      \\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders\Fonts
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/matplotlib/font_manager.py:212:        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, MSFolders) as user:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/matplotlib/font_manager.py:225:            (winreg.HKEY_CURRENT_USER, MSUserFontDirectories),  # User.
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/setuptools/msvc.py:37:        HKEY_CURRENT_USER = None
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/setuptools/msvc.py:177:        winreg.HKEY_CURRENT_USER,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/setuptools/_vendor/platformdirs/windows.py:208:    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/pygments/formatters/img.py:174:        keynames = [ (_winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows NT\CurrentVersion\Fonts'),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/pygments/formatters/img.py:175:                     (_winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Fonts'),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/pygments/lexers/_postgres_builtins.py:104:    'CURRENT_USER',

--- Authorization ---
./thesis_chapter_gates/probes/overview_docs_probe.py:67:      "Corpus retrieval equals direct action or self-authorization",
./thesis_chapter_gates/probes/ch17_probe_v2.py:24:      "autonomous self-authorization",
./thesis_chapter_gates/probes/ch32_probe.py:24:      "DGM self-authorization into production",
./thesis_chapter_gates/probes/ch27_probe.py:27:      "DGM self-authorization of findings",
./thesis_chapter_gates/probes/ch17_probe.py:24:      "autonomous self-authorization",
./auth_api.patched.py:260:            headers["Authorization"] = f"Bearer {JARVIS_TOKEN}"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/overview_docs_probe.py:67:      "Corpus retrieval equals direct action or self-authorization",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch17_probe_v2.py:24:      "autonomous self-authorization",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch32_probe.py:24:      "DGM self-authorization into production",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch27_probe.py:27:      "DGM self-authorization of findings",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/thesis_chapter_gates/probes/ch17_probe.py:24:      "autonomous self-authorization",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:260:            headers["Authorization"] = f"Bearer {JARVIS_TOKEN}"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_email_service.py:54:    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_email_service.py:107:    headers = {"Authorization": f"Bearer {token}"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_microsoft_integration_FIXED.py:111:            "Authorization": f"Bearer {self.access_token}",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/oauth2_handler.py:26:                "grant_type": "authorization_code"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/oauth2_handler.py:46:            headers = {"Authorization": f"Bearer {access_token}"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_expiration_monitor.py:112:    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarviscryptopolicy.py:115:def evaluate(req: PolicyRequest, authorization: Optional[str] = Header(None)):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarviscryptopolicy.py:120:        token = (authorization or "").replace("Bearer ", "")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarviscryptopolicy.py:153:def verify_token(authorization: str = Header(...)):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarviscryptopolicy.py:155:    token = authorization.replace("Bearer ", "")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarviscryptopolicy.py:176:               authorization: str = Header(...)):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarviscryptopolicy.py:178:    token = authorization.replace("Bearer ", "")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_egeria_facebook_autopost.py:9:Maintaining community engagement during app authorization
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_egeria_facebook_autopost.py:180:                    logger.info("   📋 Post logged (Facebook API pending authorization)")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_exclusive_training_layer.py:17:    if not check_authorization(user):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/registration_biometric_production_final.py:69:        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:702:async def verify_token(authorization: Optional[str] = Header(None)):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:703:    """Verify JWT token from Authorization header"""
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:704:    if not authorization:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:705:        raise HTTPException(status_code=401, detail="Missing authorization header")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:708:        scheme, token = authorization.split()
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:722:        raise HTTPException(status_code=401, detail="Invalid authorization format")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/stage2_biometric.py:60:            "Authorization": f"Bearer {MICROSOFT_GRAPH_TOKEN}",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/oauth2_callback.py:27:            raise HTTPException(status_code=400, detail="Invalid authorization code")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_web_deployer_old.py:43:            "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/registration_service_clean.backup_1762220206.py:107:            headers = {"Authorization": f"Bearer {token['access_token']}", "Content-Type": "application/json"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_unified_swagger_gateway.py:24:    swagger_ui_parameters={"persistAuthorization": True}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_web_deployer.py:49:            "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_web_deployer.py:171:        headers = {"Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}", "Content-Type": "application/json"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_microsoft_integration.py:113:            "Authorization": f"Bearer {self.access_token}",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/registration_service_clean.py:107:            headers = {"Authorization": f"Bearer {token['access_token']}", "Content-Type": "application/json"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api_no_full_router.py:278:            headers["Authorization"] = f"Bearer {JARVIS_TOKEN}"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/eth/vm/forks/london/transactions.py:37:    SetCodeAuthorizationAPI,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/eth/vm/forks/london/transactions.py:213:    def authorization_list(self) -> Sequence[SetCodeAuthorizationAPI]:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/eth/vm/forks/london/transactions.py:214:        raise NotImplementedError("authorization_list is not implemented until Prague.")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/eth/vm/forks/prague/state.py:63:            authorizations_refund = self.vm_state.process_set_code_authorizations(
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/eth/vm/forks/prague/state.py:66:            message_refund += authorizations_refund
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/eth/vm/forks/prague/state.py:121:    def process_set_code_authorizations(self, transaction: SignedTransactionAPI) -> int:

--- Bearer ---
./token_service.py:161:            "token_type": "bearer",
./token_service.py:170:        Validate a bearer token.  Returns payload dict or None if invalid/expired.
./token_service.py:198:            "token_type": "bearer",
./auth_api.patched.py:260:            headers["Authorization"] = f"Bearer {JARVIS_TOKEN}"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:161:            "token_type": "bearer",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:170:        Validate a bearer token.  Returns payload dict or None if invalid/expired.
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/token_service.py:198:            "token_type": "bearer",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api.patched.py:260:            headers["Authorization"] = f"Bearer {JARVIS_TOKEN}"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_email_service.py:54:    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_email_service.py:107:    headers = {"Authorization": f"Bearer {token}"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_microsoft_integration_FIXED.py:111:            "Authorization": f"Bearer {self.access_token}",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/oauth2_handler.py:46:            headers = {"Authorization": f"Bearer {access_token}"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_expiration_monitor.py:112:    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarviscryptopolicy.py:120:        token = (authorization or "").replace("Bearer ", "")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarviscryptopolicy.py:154:    """Verify a bearer token."""
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarviscryptopolicy.py:155:    token = authorization.replace("Bearer ", "")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarviscryptopolicy.py:178:    token = authorization.replace("Bearer ", "")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/registration_biometric_production_final.py:69:        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:709:        if scheme.lower() != "bearer":
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:746:        "token_type": "bearer",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/stage2_biometric.py:60:            "Authorization": f"Bearer {MICROSOFT_GRAPH_TOKEN}",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_web_deployer_old.py:43:            "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/registration_service_clean.backup_1762220206.py:107:            headers = {"Authorization": f"Bearer {token['access_token']}", "Content-Type": "application/json"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_web_deployer.py:49:            "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_web_deployer.py:171:        headers = {"Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}", "Content-Type": "application/json"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_microsoft_integration.py:113:            "Authorization": f"Bearer {self.access_token}",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/registration_service_clean.py:107:            headers = {"Authorization": f"Bearer {token['access_token']}", "Content-Type": "application/json"}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_api_no_full_router.py:278:            headers["Authorization"] = f"Bearer {JARVIS_TOKEN}"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/models/auto/processing_auto.py:191:                The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/models/auto/tokenization_auto.py:642:            The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/models/auto/image_processing_auto.py:236:            The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/models/auto/image_processing_auto.py:357:                The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/models/auto/feature_extraction_auto.py:179:            The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/models/auto/feature_extraction_auto.py:293:                The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/models/wav2vec2/modeling_wav2vec2.py:1473:                The token to use as HTTP bearer authorization for remote files. If `True`, or not specified, will use
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/pipelines/__init__.py:691:            The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/modeling_utils.py:2731:                The token to use as HTTP bearer authorization for remote files. If `True`, or not specified, will use
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/modeling_utils.py:3278:                The token to use as HTTP bearer authorization for remote files. If `True`, or not specified, will use
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/agents/tools.py:379:                The token to use as HTTP bearer authorization for remote files. If unset, will use the token generated
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/agents/tools.py:523:            The token to use as HTTP bearer authorization for remote files. If unset, will use the token generated when
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/modeling_flax_utils.py:603:                The token to use as HTTP bearer authorization for remote files. If `True`, or not specified, will use
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/modeling_flax_utils.py:1122:                The token to use as HTTP bearer authorization for remote files. If `True`, or not specified, will use
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/utils/peft_utils.py:61:            The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/utils/hub.py:313:            The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/utils/hub.py:516:            The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/utils/hub.py:858:                The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/dynamic_module_utils.py:296:            The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/dynamic_module_utils.py:485:            The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/configuration_utils.py:488:                The token to use as HTTP bearer authorization for remote files. If `True`, or not specified, will use
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/transformers/feature_extraction_utils.py:314:                The token to use as HTTP bearer authorization for remote files. If `True`, or not specified, will use

--- oauth2 ---
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_email_service.py:31:    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:436:        url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_unified_swagger_gateway_BACKUP.py:476:        url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_unified_swagger_gateway_FIXED.py:455:        url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_main_gateway.backup_error.py:408:        url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/oauth2_handler.py:9:class OAuth2Handler:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/oauth2_handler.py:10:    """Universal OAuth2 handler for GitHub, LinkedIn, Facebook"""
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/oauth2_handler.py:12:    def __init__(self, config_file="oauth2_config.json"):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_main_gateway.backup_1762220815.py:476:        url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/registration_biometric_production_final.py:48:        url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/oauth2_callback.py:11:from oauth2_handler import OAuth2Handler
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 
