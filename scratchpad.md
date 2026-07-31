(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ docker inspect jarvis-assertion-gateway --format '{{range .Config.Env}}{{println .}}{{end}}' | sort | grep -E 'KYC_DATABASE_URL|REDIS|PORT|POSTGRES|DATABASE'
DATABASE_URL=postgresql://msjarvis:postgres@hp-local-db:5432/hilbert_people
HP_DATABASE_URL=postgresql://postgres@hp-local-db:5432/hilbert_people_test
SERVICE_PORT=8047
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild && \
grep -RIn --include='*.sql' --include='*.py' --include='*.yml' --include='*.yaml' \
  -E 'mountainshares_ledger|mountainshares_balances|equity_timesheet|founder_tokens' .
grep: ./msjarvis-rebuild: warning: recursive directory loop
grep: ./production_closeout_20260728/asbuilt_snapshot_20260728/repo/msjarvis-rebuild: warning: recursive directory loop
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:49:                    "SELECT ems_balance FROM mountainshares_balances WHERE ueid = %s",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:58:                    "FROM mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:82:                    "UPDATE mountainshares_balances "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:93:                    "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:190:                    "UPDATE mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:226:                        "UPDATE mountainshares_balances "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:232:                        "UPDATE mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/chain_listener.py:68:                "UPDATE mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:450:            _cur.execute("SELECT ueid FROM founder_tokens WHERE cohort = 'phase_0'")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:524:                        _cx.execute("SELECT 1 FROM founder_tokens WHERE ueid = %s", (_ueid_check,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:527:                logger.warning(f"[APPROVE-IDEMPOTENCY] founder_tokens check failed: {_e}")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:600:            _cur.execute("INSERT INTO mountainshares_balances (ueid) VALUES (%s) ON CONFLICT DO NOTHING", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:601:            _cur.execute("SELECT serial_number FROM founder_tokens WHERE ueid = %s", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:607:                _cur.execute("SELECT COALESCE(MAX(serial_number), 0) FROM founder_tokens")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:612:                    "INSERT INTO founder_tokens (serial_number, ueid, cohort, allocation_type) "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:619:                    _cur.execute("SELECT COUNT(*) FROM mountainshares_ledger WHERE ueid = %s AND transaction_type = 'founding_grant'", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:622:                            "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:631:                        "UPDATE mountainshares_balances SET ems_balance = ems_balance + 100.0000, "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:871:        cur.execute("SELECT ems_balance, rank, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:873:        cur.execute("SELECT serial_number, created_at, cohort, allocation_type FROM founder_tokens WHERE ueid = %s", (ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:875:        cur.execute("SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s AND ueid IN (%s, %s)", (sub, sub, f"UEID-{sub.upper()}-ADMIN"))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:932:            "FROM mountainshares_ledger " + where +
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:938:            "SELECT COUNT(*) FROM mountainshares_ledger " + where,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:1029:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:1038:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/002_founder_tokens.sql:1:CREATE TABLE IF NOT EXISTS founder_tokens (
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/002_founder_tokens.sql:10:CREATE INDEX IF NOT EXISTS idx_founder_tokens_ueid   ON founder_tokens(ueid);
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/002_founder_tokens.sql:11:CREATE INDEX IF NOT EXISTS idx_founder_tokens_cohort ON founder_tokens(cohort);
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/003_ledger_columns.sql:1:ALTER TABLE mountainshares_ledger
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/003_ledger_columns.sql:8:CREATE OR REPLACE VIEW mountainshares_ledger_v AS
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/003_ledger_columns.sql:9:    SELECT *, ems_amount AS amount FROM mountainshares_ledger;
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/004_ledger_event_types.sql:2:ALTER TABLE mountainshares_ledger
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/004_ledger_event_types.sql:3:    DROP CONSTRAINT mountainshares_ledger_event_type_check;
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/004_ledger_event_types.sql:5:ALTER TABLE mountainshares_ledger
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/004_ledger_event_types.sql:6:    ADD CONSTRAINT mountainshares_ledger_event_type_check
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:325:            _cur.execute("SELECT ueid FROM founder_tokens WHERE cohort = 'phase_0'")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:422:            _cur.execute("INSERT INTO mountainshares_balances (ueid) VALUES (%s) ON CONFLICT DO NOTHING", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:423:            _cur.execute("SELECT COALESCE(MAX(serial_number), 0) FROM founder_tokens")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:428:                    "INSERT INTO founder_tokens (serial_number, ueid, minted_by, cohort, allocation_type) "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:435:                    _cur.execute("SELECT COUNT(*) FROM mountainshares_ledger WHERE ueid = %s AND transaction_type = 'founding_grant'", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:438:                        "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:447:                        "UPDATE mountainshares_balances SET ems_balance = ems_balance + 100.0000, "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:634:        cur.execute("SELECT ems_balance, rank, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:636:        cur.execute("SELECT serial_number, minted_at, cohort, allocation_type FROM founder_tokens WHERE ueid = %s", (ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:638:        cur.execute("SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s AND ueid IN (%s, %s)", (sub, sub, f"UEID-{sub.upper()}-ADMIN"))
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:695:            "FROM mountainshares_ledger " + where +
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:701:            "SELECT COUNT(*) FROM mountainshares_ledger " + where,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:792:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:801:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/scripts/materialize_tensor_bridge.py:17:    'geo_equity_timesheet',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/scripts/materialize_tensor_bridge.py:18:    'geo_equity_timesheet_ctx_backup',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/scripts/materialize_tensor_bridge.py:19:    'geo_founder_tokens',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/scripts/materialize_tensor_bridge.py:20:    'founder_tokens',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/scripts/materialize_tensor_bridge.py:26:    'equity_timesheet',
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:49:                    "SELECT ems_balance FROM mountainshares_balances WHERE ueid = %s",
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:58:                    "FROM mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:82:                    "UPDATE mountainshares_balances "
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:93:                    "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:190:                    "UPDATE mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:226:                        "UPDATE mountainshares_balances "
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:232:                        "UPDATE mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/chain_listener.py:68:                "UPDATE mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:49:                    "SELECT ems_balance FROM mountainshares_balances WHERE ueid = %s",
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:58:                    "FROM mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:82:                    "UPDATE mountainshares_balances "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:93:                    "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:190:                    "UPDATE mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:226:                        "UPDATE mountainshares_balances "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:232:                        "UPDATE mountainshares_ledger "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/chain_listener.py:68:                "UPDATE mountainshares_ledger "
grep: ./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/msjarvis-rebuild: warning: recursive directory loop
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:49:                    "SELECT ems_balance FROM mountainshares_balances WHERE ueid = %s",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:58:                    "FROM mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:82:                    "UPDATE mountainshares_balances "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:93:                    "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:190:                    "UPDATE mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:226:                        "UPDATE mountainshares_balances "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:232:                        "UPDATE mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/chain_listener.py:68:                "UPDATE mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:450:            _cur.execute("SELECT ueid FROM founder_tokens WHERE cohort = 'phase_0'")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:524:                        _cx.execute("SELECT 1 FROM founder_tokens WHERE ueid = %s", (_ueid_check,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:527:                logger.warning(f"[APPROVE-IDEMPOTENCY] founder_tokens check failed: {_e}")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:600:            _cur.execute("INSERT INTO mountainshares_balances (ueid) VALUES (%s) ON CONFLICT DO NOTHING", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:601:            _cur.execute("SELECT serial_number FROM founder_tokens WHERE ueid = %s", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:607:                _cur.execute("SELECT COALESCE(MAX(serial_number), 0) FROM founder_tokens")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:612:                    "INSERT INTO founder_tokens (serial_number, ueid, cohort, allocation_type) "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:619:                    _cur.execute("SELECT COUNT(*) FROM mountainshares_ledger WHERE ueid = %s AND transaction_type = 'founding_grant'", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:622:                            "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:631:                        "UPDATE mountainshares_balances SET ems_balance = ems_balance + 100.0000, "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:871:        cur.execute("SELECT ems_balance, rank, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:873:        cur.execute("SELECT serial_number, created_at, cohort, allocation_type FROM founder_tokens WHERE ueid = %s", (ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:875:        cur.execute("SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s AND ueid IN (%s, %s)", (sub, sub, f"UEID-{sub.upper()}-ADMIN"))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:932:            "FROM mountainshares_ledger " + where +
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:938:            "SELECT COUNT(*) FROM mountainshares_ledger " + where,
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:1029:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:1038:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/002_founder_tokens.sql:1:CREATE TABLE IF NOT EXISTS founder_tokens (
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/002_founder_tokens.sql:10:CREATE INDEX IF NOT EXISTS idx_founder_tokens_ueid   ON founder_tokens(ueid);
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/002_founder_tokens.sql:11:CREATE INDEX IF NOT EXISTS idx_founder_tokens_cohort ON founder_tokens(cohort);
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/003_ledger_columns.sql:1:ALTER TABLE mountainshares_ledger
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/003_ledger_columns.sql:8:CREATE OR REPLACE VIEW mountainshares_ledger_v AS
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/003_ledger_columns.sql:9:    SELECT *, ems_amount AS amount FROM mountainshares_ledger;
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/004_ledger_event_types.sql:2:ALTER TABLE mountainshares_ledger
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/004_ledger_event_types.sql:3:    DROP CONSTRAINT mountainshares_ledger_event_type_check;
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/004_ledger_event_types.sql:5:ALTER TABLE mountainshares_ledger
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/004_ledger_event_types.sql:6:    ADD CONSTRAINT mountainshares_ledger_event_type_check
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:325:            _cur.execute("SELECT ueid FROM founder_tokens WHERE cohort = 'phase_0'")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:422:            _cur.execute("INSERT INTO mountainshares_balances (ueid) VALUES (%s) ON CONFLICT DO NOTHING", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:423:            _cur.execute("SELECT COALESCE(MAX(serial_number), 0) FROM founder_tokens")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:428:                    "INSERT INTO founder_tokens (serial_number, ueid, minted_by, cohort, allocation_type) "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:435:                    _cur.execute("SELECT COUNT(*) FROM mountainshares_ledger WHERE ueid = %s AND transaction_type = 'founding_grant'", (_ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:438:                        "INSERT INTO mountainshares_ledger "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:447:                        "UPDATE mountainshares_balances SET ems_balance = ems_balance + 100.0000, "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:634:        cur.execute("SELECT ems_balance, rank, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:636:        cur.execute("SELECT serial_number, minted_at, cohort, allocation_type FROM founder_tokens WHERE ueid = %s", (ueid,))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:638:        cur.execute("SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s AND ueid IN (%s, %s)", (sub, sub, f"UEID-{sub.upper()}-ADMIN"))
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:695:            "FROM mountainshares_ledger " + where +
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:701:            "SELECT COUNT(*) FROM mountainshares_ledger " + where,
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:792:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:801:            FROM equity_timesheet
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/scripts/materialize_tensor_bridge.py:17:    'geo_equity_timesheet',
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/scripts/materialize_tensor_bridge.py:18:    'geo_equity_timesheet_ctx_backup',
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/scripts/materialize_tensor_bridge.py:19:    'geo_founder_tokens',
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/scripts/materialize_tensor_bridge.py:20:    'founder_tokens',
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/scripts/materialize_tensor_bridge.py:26:    'equity_timesheet',
grep: ./services/ms_jarvis_mother_carrie_protocols.py: Permission denied
./services/conversion_service.py:49:                    "SELECT ems_balance FROM mountainshares_balances WHERE ueid = %s",
./services/conversion_service.py:58:                    "FROM mountainshares_ledger "
./services/conversion_service.py:82:                    "UPDATE mountainshares_balances "
./services/conversion_service.py:93:                    "INSERT INTO mountainshares_ledger "
./services/conversion_service.py:190:                    "UPDATE mountainshares_ledger "
./services/conversion_service.py:226:                        "UPDATE mountainshares_balances "
./services/conversion_service.py:232:                        "UPDATE mountainshares_ledger "
./services/chain_listener.py:68:                "UPDATE mountainshares_ledger "
./auth_router.py:450:            _cur.execute("SELECT ueid FROM founder_tokens WHERE cohort = 'phase_0'")
./auth_router.py:524:                        _cx.execute("SELECT 1 FROM founder_tokens WHERE ueid = %s", (_ueid_check,))
./auth_router.py:527:                logger.warning(f"[APPROVE-IDEMPOTENCY] founder_tokens check failed: {_e}")
./auth_router.py:600:            _cur.execute("INSERT INTO mountainshares_balances (ueid) VALUES (%s) ON CONFLICT DO NOTHING", (_ueid,))
./auth_router.py:601:            _cur.execute("SELECT serial_number FROM founder_tokens WHERE ueid = %s", (_ueid,))
./auth_router.py:607:                _cur.execute("SELECT COALESCE(MAX(serial_number), 0) FROM founder_tokens")
./auth_router.py:612:                    "INSERT INTO founder_tokens (serial_number, ueid, cohort, allocation_type) "
./auth_router.py:619:                    _cur.execute("SELECT COUNT(*) FROM mountainshares_ledger WHERE ueid = %s AND transaction_type = 'founding_grant'", (_ueid,))
./auth_router.py:622:                            "INSERT INTO mountainshares_ledger "
./auth_router.py:631:                        "UPDATE mountainshares_balances SET ems_balance = ems_balance + 100.0000, "
./auth_router.py:871:        cur.execute("SELECT ems_balance, rank, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
./auth_router.py:873:        cur.execute("SELECT serial_number, created_at, cohort, allocation_type FROM founder_tokens WHERE ueid = %s", (ueid,))
./auth_router.py:875:        cur.execute("SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s AND ueid IN (%s, %s)", (sub, sub, f"UEID-{sub.upper()}-ADMIN"))
./auth_router.py:932:            "FROM mountainshares_ledger " + where +
./auth_router.py:938:            "SELECT COUNT(*) FROM mountainshares_ledger " + where,
./auth_router.py:1029:            FROM equity_timesheet
./auth_router.py:1038:            FROM equity_timesheet
./migrations/002_founder_tokens.sql:1:CREATE TABLE IF NOT EXISTS founder_tokens (
./migrations/002_founder_tokens.sql:10:CREATE INDEX IF NOT EXISTS idx_founder_tokens_ueid   ON founder_tokens(ueid);
./migrations/002_founder_tokens.sql:11:CREATE INDEX IF NOT EXISTS idx_founder_tokens_cohort ON founder_tokens(cohort);
./migrations/003_ledger_columns.sql:1:ALTER TABLE mountainshares_ledger
./migrations/003_ledger_columns.sql:8:CREATE OR REPLACE VIEW mountainshares_ledger_v AS
./migrations/003_ledger_columns.sql:9:    SELECT *, ems_amount AS amount FROM mountainshares_ledger;
./migrations/004_ledger_event_types.sql:2:ALTER TABLE mountainshares_ledger
./migrations/004_ledger_event_types.sql:3:    DROP CONSTRAINT mountainshares_ledger_event_type_check;
./migrations/004_ledger_event_types.sql:5:ALTER TABLE mountainshares_ledger
./migrations/004_ledger_event_types.sql:6:    ADD CONSTRAINT mountainshares_ledger_event_type_check
grep: ./data/local_resources: Permission denied
grep: ./data/mysql/sys: Permission denied
grep: ./data/mysql/#innodb_temp: Permission denied
grep: ./data/mysql/quantum_ai: Permission denied
grep: ./data/mysql/mysql: Permission denied
grep: ./data/mysql/performance_schema: Permission denied
grep: ./data/mysql/#innodb_redo: Permission denied
./.archive/debug_files_20260630/auth_router.debug.py:325:            _cur.execute("SELECT ueid FROM founder_tokens WHERE cohort = 'phase_0'")
./.archive/debug_files_20260630/auth_router.debug.py:422:            _cur.execute("INSERT INTO mountainshares_balances (ueid) VALUES (%s) ON CONFLICT DO NOTHING", (_ueid,))
./.archive/debug_files_20260630/auth_router.debug.py:423:            _cur.execute("SELECT COALESCE(MAX(serial_number), 0) FROM founder_tokens")
./.archive/debug_files_20260630/auth_router.debug.py:428:                    "INSERT INTO founder_tokens (serial_number, ueid, minted_by, cohort, allocation_type) "
./.archive/debug_files_20260630/auth_router.debug.py:435:                    _cur.execute("SELECT COUNT(*) FROM mountainshares_ledger WHERE ueid = %s AND transaction_type = 'founding_grant'", (_ueid,))
./.archive/debug_files_20260630/auth_router.debug.py:438:                        "INSERT INTO mountainshares_ledger "
./.archive/debug_files_20260630/auth_router.debug.py:447:                        "UPDATE mountainshares_balances SET ems_balance = ems_balance + 100.0000, "
./.archive/debug_files_20260630/auth_router.debug.py:634:        cur.execute("SELECT ems_balance, rank, last_updated FROM mountainshares_balances WHERE ueid = %s", (ueid,))
./.archive/debug_files_20260630/auth_router.debug.py:636:        cur.execute("SELECT serial_number, minted_at, cohort, allocation_type FROM founder_tokens WHERE ueid = %s", (ueid,))
./.archive/debug_files_20260630/auth_router.debug.py:638:        cur.execute("SELECT COALESCE(SUM(ems_earned), 0) FROM equity_timesheet WHERE user_id = %s AND ueid IN (%s, %s)", (sub, sub, f"UEID-{sub.upper()}-ADMIN"))
./.archive/debug_files_20260630/auth_router.debug.py:695:            "FROM mountainshares_ledger " + where +
./.archive/debug_files_20260630/auth_router.debug.py:701:            "SELECT COUNT(*) FROM mountainshares_ledger " + where,
./.archive/debug_files_20260630/auth_router.debug.py:792:            FROM equity_timesheet
./.archive/debug_files_20260630/auth_router.debug.py:801:            FROM equity_timesheet
./scripts/materialize_tensor_bridge.py:17:    'geo_equity_timesheet',
./scripts/materialize_tensor_bridge.py:18:    'geo_equity_timesheet_ctx_backup',
./scripts/materialize_tensor_bridge.py:19:    'geo_founder_tokens',
./scripts/materialize_tensor_bridge.py:20:    'founder_tokens',
./scripts/materialize_tensor_bridge.py:26:    'equity_timesheet',
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ docker inspect jarvis-msjarvis-db --format '{{.Name}} {{index .Config.Env}}' | tr ' ' '\n' | grep -E 'POSTGRES_DB|POSTGRES_USER|POSTGRES_PASSWORD|DATABASE_URL' || true

docker inspect hp-local-db --format '{{.Name}} {{index .Config.Env}}' | tr ' ' '\n' | grep -E 'POSTGRES_DB|POSTGRES_USER|POSTGRES_PASSWORD|DATABASE_URL' || true
[POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=msjarvisgis_v2
[POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ python3 - <<'PY'
import psycopg2

targets = [
    ("hp-local-db-msjarvisgis", "postgresql://postgres:postgres@127.0.0.1:5435/msjarvisgis"),
    ("hp-local-db-postgres",    "postgresql://postgres:postgres@127.0.0.1:5435/postgres"),
    ("relay-5433-msjarvisgis",  "postgresql://postgres:postgres@127.0.0.1:5433/msjarvisgis"),
]

tables = ["mountainshares_ledger", "mountainshares_balances", "equity_timesheet", "founder_tokens"]

for name, dsn in targets:
    print(f"\n=== {name} ===")
    try:
        conn = psycopg2.connect(dsn)
        cur = conn.cursor()
        cur.execute("select current_database(), current_user")
        print("db,user =", cur.fetchone())
        for t in tables:
            cur.execute("""
                select table_schema, table_name
                from information_schema.tables
PY      print("ERROR", type(e).__name__, e)SING")

=== hp-local-db-msjarvisgis ===
db,user = ('msjarvisgis', 'postgres')
mountainshares_ledger MISSING
mountainshares_balances MISSING
equity_timesheet MISSING
founder_tokens MISSING

=== hp-local-db-postgres ===
db,user = ('postgres', 'postgres')
mountainshares_ledger MISSING
mountainshares_balances MISSING
equity_timesheet MISSING
founder_tokens MISSING

=== relay-5433-msjarvisgis ===
db,user = ('msjarvisgis', 'postgres')
mountainshares_ledger MISSING
mountainshares_balances MISSING
equity_timesheet MISSING
founder_tokens MISSING
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ export DATABASE_URL='postgresql://postgres:postgres@127.0.0.1:5435/msjarvisgis'
export POSTGRES_DSN='postgresql://postgres:postgres@127.0.0.1:5435/msjarvisgis'
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ pkill -f 'uvicorn auth_api:app --host 127.0.0.1 --port 8097' 2>/dev/null || true && \
export APP_ENCRYPT_KEY='8lA8zHCqaczOeYjQ_iKWsbyrlB6ErzwhV9bBo-cGQWo=' && \
export REDIS_URL='redis://127.0.0.1:6379' && \
export JARVIS_URL='http://127.0.0.1:8050' && \
export JARVIS_TOKEN='internal' && \
export PORTAL_URL='http://localhost:3000' && \
export ADMIN_EMAIL='h4hwv2011@gmail.com' && \
export SERVICE_PORT='8091' && \
export ASSERTION_GATEWAY_URL='http://127.0.0.1:8047' && \
cd /mnt/spiritual_drive/msjarvis-rebuild && \
nohup python3 -m uvicorn auth_api:app --host 127.0.0.1 --port 8097 > /tmp/auth_api_8097.log 2>&1 & \
sleep 3 && \
tail -n 80 /tmp/auth_api_8097.log
[9] 1635854
Terminated
[8]-  Exit 143                pkill -f 'uvicorn auth_api:app --host 127.0.0.1 --port 8097' 2> /dev/null || true && export APP_ENCRYPT_KEY='8lA8zHCqaczOeYjQ_iKWsbyrlB6ErzwhV9bBo-cGQWo=' && export DATABASE_URL='postgresql://postgres:postgres@127.0.0.1:5433/msjarvisgis' && export POSTGRES_DSN='postgresql://postgres:postgres@127.0.0.1:5433/msjarvisgis' && export REDIS_URL='redis://127.0.0.1:6379' && export JARVIS_URL='http://127.0.0.1:8050' && export JARVIS_TOKEN='internal' && export PORTAL_URL='http://localhost:3000' && export ADMIN_EMAIL='h4hwv2011@gmail.com' && export SERVICE_PORT='8091' && export ASSERTION_GATEWAY_URL='http://127.0.0.1:8047' && cd /mnt/spiritual_drive/msjarvis-rebuild && nohup python3 -m uvicorn auth_api:app --host 127.0.0.1 --port 8097 > /tmp/auth_api_8097.log 2>&1
nohup: ignoring input
INFO:     Started server process [1635857]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8097 (Press CTRL+C to quit)
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [1627632]
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ curl -sS -X POST "http://127.0.0.1:8097/auth/login" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode "username=cakidd" \
  --data-urlencode "password=CHOOSE_A_NEW_PASSWORD_HERE" \
  | tee /tmp/login_8097_portal.json && \
export MSALLIS_TOKEN=$(python3 - <<'PY'
import json
print(json.load(open('/tmp/login_8097_portal.json'))['access_token'])
PY
)

curl -sS "http://127.0.0.1:8097/auth/portal/me/ledger?limit=10" \
  -H "Authorization: Bearer $MSALLIS_TOKEN" | jq .

curl -sS "http://127.0.0.1:8097/auth/portal/me/timesheet" \
  -H "Authorization: Bearer $MSALLIS_TOKEN" | jq .
{"access_token":"rt_254cc82ff8e5133ad1f13b15","token_type":"bearer","expires_in":7776000}{
  "detail": "DB error: relation \"mountainshares_ledger\" does not exist\nLINE 1: ...reason, reference_id, created_at, created_by FROM mountainsh...\n                                                             ^\n"
}
{
  "detail": "Timesheet query failed: relation \"equity_timesheet\" does not exist\nLINE 4:             FROM equity_timesheet\n                         ^\n"
}
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild && \
grep -RIn --include='*.py' --include='*.yml' --include='*.yaml' \
  -E 'KYC_DATABASE_URL|kyc_database_url|KYC DB|ASSERTION_GATEWAY_URL|/assert' \
  services/jarvis-assertion-gateway docker-compose.yml .
services/jarvis-assertion-gateway/app/kyc_reader.py:10:KYC_DATABASE_URL = os.environ.get("KYC_DATABASE_URL")
services/jarvis-assertion-gateway/app/kyc_reader.py:13:    if not KYC_DATABASE_URL:
services/jarvis-assertion-gateway/app/kyc_reader.py:14:        raise RuntimeError("KYC_DATABASE_URL is not set.")
services/jarvis-assertion-gateway/app/kyc_reader.py:15:    return await asyncpg.connect(KYC_DATABASE_URL)
services/jarvis-assertion-gateway/app/main.py:80:@app.post("/assert", response_model=ClaimResponse)
grep: ./msjarvis-rebuild: warning: recursive directory loop
grep: ./production_closeout_20260728/asbuilt_snapshot_20260728/repo/msjarvis-rebuild: warning: recursive directory loop
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/output/47_general_noun_space_patch_v3.py:134:if '@app.post("/noun/assert")' not in src:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/output/47_general_noun_space_patch_v3.py:135:    anchor = '@app.post("/assert")'
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/output/47_general_noun_space_patch_v3.py:138:        raise SystemExit('/assert route anchor not found')
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/output/47_general_noun_space_patch_v3.py:141:@app.post("/noun/assert")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/gbim_query_router.py:231:@app.post("/assert")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/gbim_query_router.py:257:            session_id, "/assert", actor_id,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/gbim_query_router.py:279:        session_id, "/assert", actor_id,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:10:KYC_DATABASE_URL = os.environ.get("KYC_DATABASE_URL")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:13:    if not KYC_DATABASE_URL:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:14:        raise RuntimeError("KYC_DATABASE_URL is not set.")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:15:    return await asyncpg.connect(KYC_DATABASE_URL)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarvis-assertion-gateway/app/main.py:80:@app.post("/assert", response_model=ClaimResponse)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/gbim-router/app/assertion_client.py:4:ASSERTION_GATEWAY_URL = os.environ.get("ASSERTION_GATEWAY_URL", "http://127.0.0.1:8009")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/gbim-router/app/assertion_client.py:17:        resp = await client.post(f"{ASSERTION_GATEWAY_URL}/assert", json=payload)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/playwright/async_api/_generated.py:12201:          is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/playwright/async_api/_generated.py:12202:          handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/playwright/async_api/_generated.py:12206:        - The execution time of the handler counts towards the timeout of the action/assertion that executed the handler.
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/playwright/async_api/_generated.py:12285:            Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/playwright/sync_api/_generated.py:12269:          is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/playwright/sync_api/_generated.py:12270:          handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/playwright/sync_api/_generated.py:12274:        - The execution time of the handler counts towards the timeout of the action/assertion that executed the handler.
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/playwright/sync_api/_generated.py:12353:            Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/packageurl/contrib/url2purl.py:342:# https://packagist.org/packages/webmozart/assert#1.9.1
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/torch/testing/_internal/common_utils.py:3123:# This implements a variant of assertRaises/assertRaisesRegex where we first test
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/_pytest/python.py:174:                "See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information."
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/jedi/inference/context.py:93:        # Add isinstance and other if/assert knowledge.
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/testing/assertions.py:1:# testing/assertions.py
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/testing/assertsql.py:1:# testing/assertsql.py
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/narwhals/testing/asserts/frame.py:152:    # Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/py-polars/src/polars/testing/asserts/frame.py#L15-L17
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/narwhals/testing/asserts/frame.py:180:    # Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/crates/polars-testing/src/asserts/utils.rs#L829
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/narwhals/testing/asserts/frame.py:239:    Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/crates/polars-testing/src/asserts/utils.rs#L667-L698
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib64/python3.12/site-packages/pypdf/_codecs/adobe_glyphs.py:2157:    "/assertion": "\u22A6",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/playwright/async_api/_generated.py:12201:          is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/playwright/async_api/_generated.py:12202:          handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/playwright/async_api/_generated.py:12206:        - The execution time of the handler counts towards the timeout of the action/assertion that executed the handler.
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/playwright/async_api/_generated.py:12285:            Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/playwright/sync_api/_generated.py:12269:          is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/playwright/sync_api/_generated.py:12270:          handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/playwright/sync_api/_generated.py:12274:        - The execution time of the handler counts towards the timeout of the action/assertion that executed the handler.
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/playwright/sync_api/_generated.py:12353:            Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/packageurl/contrib/url2purl.py:342:# https://packagist.org/packages/webmozart/assert#1.9.1
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/torch/testing/_internal/common_utils.py:3123:# This implements a variant of assertRaises/assertRaisesRegex where we first test
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/_pytest/python.py:174:                "See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information."
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/jedi/inference/context.py:93:        # Add isinstance and other if/assert knowledge.
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/sqlalchemy/testing/assertions.py:1:# testing/assertions.py
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/sqlalchemy/testing/assertsql.py:1:# testing/assertsql.py
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/narwhals/testing/asserts/frame.py:152:    # Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/py-polars/src/polars/testing/asserts/frame.py#L15-L17
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/narwhals/testing/asserts/frame.py:180:    # Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/crates/polars-testing/src/asserts/utils.rs#L829
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/narwhals/testing/asserts/frame.py:239:    Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/crates/polars-testing/src/asserts/utils.rs#L667-L698
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/crypto-venv/lib/python3.12/site-packages/pypdf/_codecs/adobe_glyphs.py:2157:    "/assertion": "\u22A6",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:149:    base = os.getenv("ASSERTION_GATEWAY_URL", "http://127.0.0.1:8009").rstrip("/")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:152:            f"{base}/assert",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/tools/load_noun_assertions.py:22:            "curl", "-s", "-X", "POST", "http://127.0.0.1:7205/noun/assert",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/tools/hp_promote_inference_candidates.py:67:        "curl", "-s", "-X", "POST", "http://127.0.0.1:7205/assert",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:56:    base = os.getenv("ASSERTION_GATEWAY_URL", "http://127.0.0.1:8009").rstrip("/")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:59:            f"{base}/assert",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.check_venv/lib64/python3.12/site-packages/chromadb/test/property/test_schema.py:266:    some assumptions/assertions:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.check_venv/lib/python3.12/site-packages/chromadb/test/property/test_schema.py:266:    some assumptions/assertions:
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/gbim_query_router.py:231:@app.post("/assert")
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/gbim_query_router.py:257:            session_id, "/assert", actor_id,
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/gbim_query_router.py:279:        session_id, "/assert", actor_id,
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/jarvis-assertion-gateway/app/kyc_reader.py:10:KYC_DATABASE_URL = os.environ.get("KYC_DATABASE_URL")
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/jarvis-assertion-gateway/app/kyc_reader.py:13:    if not KYC_DATABASE_URL:
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/jarvis-assertion-gateway/app/kyc_reader.py:14:        raise RuntimeError("KYC_DATABASE_URL is not set.")
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/jarvis-assertion-gateway/app/kyc_reader.py:15:    return await asyncpg.connect(KYC_DATABASE_URL)
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/jarvis-assertion-gateway/app/main.py:80:@app.post("/assert", response_model=ClaimResponse)
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/gbim-router/app/assertion_client.py:4:ASSERTION_GATEWAY_URL = os.environ.get("ASSERTION_GATEWAY_URL", "http://127.0.0.1:8009")
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/gbim-router/app/assertion_client.py:17:        resp = await client.post(f"{ASSERTION_GATEWAY_URL}/assert", json=payload)
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/gbim_query_router.py:231:@app.post("/assert")
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/gbim_query_router.py:257:            session_id, "/assert", actor_id,
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/gbim_query_router.py:279:        session_id, "/assert", actor_id,
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/jarvis-assertion-gateway/app/kyc_reader.py:10:KYC_DATABASE_URL = os.environ.get("KYC_DATABASE_URL")
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/jarvis-assertion-gateway/app/kyc_reader.py:13:    if not KYC_DATABASE_URL:
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/jarvis-assertion-gateway/app/kyc_reader.py:14:        raise RuntimeError("KYC_DATABASE_URL is not set.")
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/jarvis-assertion-gateway/app/kyc_reader.py:15:    return await asyncpg.connect(KYC_DATABASE_URL)
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/jarvis-assertion-gateway/app/main.py:80:@app.post("/assert", response_model=ClaimResponse)
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/gbim-router/app/assertion_client.py:4:ASSERTION_GATEWAY_URL = os.environ.get("ASSERTION_GATEWAY_URL", "http://127.0.0.1:8009")
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/gbim-router/app/assertion_client.py:17:        resp = await client.post(f"{ASSERTION_GATEWAY_URL}/assert", json=payload)
grep: ./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/msjarvis-rebuild: warning: recursive directory loop
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/output/47_general_noun_space_patch_v3.py:134:if '@app.post("/noun/assert")' not in src:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/output/47_general_noun_space_patch_v3.py:135:    anchor = '@app.post("/assert")'
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/output/47_general_noun_space_patch_v3.py:138:        raise SystemExit('/assert route anchor not found')
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/output/47_general_noun_space_patch_v3.py:141:@app.post("/noun/assert")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/gbim_query_router.py:231:@app.post("/assert")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/gbim_query_router.py:257:            session_id, "/assert", actor_id,
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/gbim_query_router.py:279:        session_id, "/assert", actor_id,
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:10:KYC_DATABASE_URL = os.environ.get("KYC_DATABASE_URL")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:13:    if not KYC_DATABASE_URL:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:14:        raise RuntimeError("KYC_DATABASE_URL is not set.")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:15:    return await asyncpg.connect(KYC_DATABASE_URL)
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/jarvis-assertion-gateway/app/main.py:80:@app.post("/assert", response_model=ClaimResponse)
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/gbim-router/app/assertion_client.py:4:ASSERTION_GATEWAY_URL = os.environ.get("ASSERTION_GATEWAY_URL", "http://127.0.0.1:8009")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/gbim-router/app/assertion_client.py:17:        resp = await client.post(f"{ASSERTION_GATEWAY_URL}/assert", json=payload)
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/playwright/async_api/_generated.py:12201:          is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/playwright/async_api/_generated.py:12202:          handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/playwright/async_api/_generated.py:12206:        - The execution time of the handler counts towards the timeout of the action/assertion that executed the handler.
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/playwright/async_api/_generated.py:12285:            Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/playwright/sync_api/_generated.py:12269:          is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/playwright/sync_api/_generated.py:12270:          handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/playwright/sync_api/_generated.py:12274:        - The execution time of the handler counts towards the timeout of the action/assertion that executed the handler.
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/playwright/sync_api/_generated.py:12353:            Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/packageurl/contrib/url2purl.py:342:# https://packagist.org/packages/webmozart/assert#1.9.1
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/torch/testing/_internal/common_utils.py:3123:# This implements a variant of assertRaises/assertRaisesRegex where we first test
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/_pytest/python.py:174:                "See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information."
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/jedi/inference/context.py:93:        # Add isinstance and other if/assert knowledge.
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/testing/assertions.py:1:# testing/assertions.py
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/sqlalchemy/testing/assertsql.py:1:# testing/assertsql.py
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/narwhals/testing/asserts/frame.py:152:    # Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/py-polars/src/polars/testing/asserts/frame.py#L15-L17
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/narwhals/testing/asserts/frame.py:180:    # Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/crates/polars-testing/src/asserts/utils.rs#L829
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/narwhals/testing/asserts/frame.py:239:    Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/crates/polars-testing/src/asserts/utils.rs#L667-L698
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib64/python3.12/site-packages/pypdf/_codecs/adobe_glyphs.py:2157:    "/assertion": "\u22A6",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/playwright/async_api/_generated.py:12201:          is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/playwright/async_api/_generated.py:12202:          handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/playwright/async_api/_generated.py:12206:        - The execution time of the handler counts towards the timeout of the action/assertion that executed the handler.
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/playwright/async_api/_generated.py:12285:            Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/playwright/sync_api/_generated.py:12269:          is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/playwright/sync_api/_generated.py:12270:          handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/playwright/sync_api/_generated.py:12274:        - The execution time of the handler counts towards the timeout of the action/assertion that executed the handler.
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/playwright/sync_api/_generated.py:12353:            Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/packageurl/contrib/url2purl.py:342:# https://packagist.org/packages/webmozart/assert#1.9.1
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/torch/testing/_internal/common_utils.py:3123:# This implements a variant of assertRaises/assertRaisesRegex where we first test
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/_pytest/python.py:174:                "See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information."
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/jedi/inference/context.py:93:        # Add isinstance and other if/assert knowledge.
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/sqlalchemy/testing/assertions.py:1:# testing/assertions.py
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/sqlalchemy/testing/assertsql.py:1:# testing/assertsql.py
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/narwhals/testing/asserts/frame.py:152:    # Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/py-polars/src/polars/testing/asserts/frame.py#L15-L17
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/narwhals/testing/asserts/frame.py:180:    # Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/crates/polars-testing/src/asserts/utils.rs#L829
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/narwhals/testing/asserts/frame.py:239:    Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/crates/polars-testing/src/asserts/utils.rs#L667-L698
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/crypto-venv/lib/python3.12/site-packages/pypdf/_codecs/adobe_glyphs.py:2157:    "/assertion": "\u22A6",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:149:    base = os.getenv("ASSERTION_GATEWAY_URL", "http://127.0.0.1:8009").rstrip("/")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:152:            f"{base}/assert",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/tools/load_noun_assertions.py:22:            "curl", "-s", "-X", "POST", "http://127.0.0.1:7205/noun/assert",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/tools/hp_promote_inference_candidates.py:67:        "curl", "-s", "-X", "POST", "http://127.0.0.1:7205/assert",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:56:    base = os.getenv("ASSERTION_GATEWAY_URL", "http://127.0.0.1:8009").rstrip("/")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:59:            f"{base}/assert",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.check_venv/lib64/python3.12/site-packages/chromadb/test/property/test_schema.py:266:    some assumptions/assertions:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.check_venv/lib/python3.12/site-packages/chromadb/test/property/test_schema.py:266:    some assumptions/assertions:
./output/47_general_noun_space_patch_v3.py:134:if '@app.post("/noun/assert")' not in src:
./output/47_general_noun_space_patch_v3.py:135:    anchor = '@app.post("/assert")'
./output/47_general_noun_space_patch_v3.py:138:        raise SystemExit('/assert route anchor not found')
./output/47_general_noun_space_patch_v3.py:141:@app.post("/noun/assert")
./services/gbim_query_router.py:231:@app.post("/assert")
./services/gbim_query_router.py:257:            session_id, "/assert", actor_id,
./services/gbim_query_router.py:279:        session_id, "/assert", actor_id,
grep: ./services/ms_jarvis_mother_carrie_protocols.py: Permission denied
./services/jarvis-assertion-gateway/app/kyc_reader.py:10:KYC_DATABASE_URL = os.environ.get("KYC_DATABASE_URL")
./services/jarvis-assertion-gateway/app/kyc_reader.py:13:    if not KYC_DATABASE_URL:
./services/jarvis-assertion-gateway/app/kyc_reader.py:14:        raise RuntimeError("KYC_DATABASE_URL is not set.")
./services/jarvis-assertion-gateway/app/kyc_reader.py:15:    return await asyncpg.connect(KYC_DATABASE_URL)
./services/jarvis-assertion-gateway/app/main.py:80:@app.post("/assert", response_model=ClaimResponse)
./services/gbim-router/app/assertion_client.py:4:ASSERTION_GATEWAY_URL = os.environ.get("ASSERTION_GATEWAY_URL", "http://127.0.0.1:8009")
./services/gbim-router/app/assertion_client.py:17:        resp = await client.post(f"{ASSERTION_GATEWAY_URL}/assert", json=payload)
./crypto-venv/lib64/python3.12/site-packages/playwright/async_api/_generated.py:12201:          is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the
./crypto-venv/lib64/python3.12/site-packages/playwright/async_api/_generated.py:12202:          handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't
./crypto-venv/lib64/python3.12/site-packages/playwright/async_api/_generated.py:12206:        - The execution time of the handler counts towards the timeout of the action/assertion that executed the handler.
./crypto-venv/lib64/python3.12/site-packages/playwright/async_api/_generated.py:12285:            Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of
./crypto-venv/lib64/python3.12/site-packages/playwright/sync_api/_generated.py:12269:          is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the
./crypto-venv/lib64/python3.12/site-packages/playwright/sync_api/_generated.py:12270:          handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't
./crypto-venv/lib64/python3.12/site-packages/playwright/sync_api/_generated.py:12274:        - The execution time of the handler counts towards the timeout of the action/assertion that executed the handler.
./crypto-venv/lib64/python3.12/site-packages/playwright/sync_api/_generated.py:12353:            Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of
./crypto-venv/lib64/python3.12/site-packages/packageurl/contrib/url2purl.py:342:# https://packagist.org/packages/webmozart/assert#1.9.1
./crypto-venv/lib64/python3.12/site-packages/torch/testing/_internal/common_utils.py:3123:# This implements a variant of assertRaises/assertRaisesRegex where we first test
./crypto-venv/lib64/python3.12/site-packages/_pytest/python.py:174:                "See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information."
./crypto-venv/lib64/python3.12/site-packages/jedi/inference/context.py:93:        # Add isinstance and other if/assert knowledge.
./crypto-venv/lib64/python3.12/site-packages/sqlalchemy/testing/assertions.py:1:# testing/assertions.py
./crypto-venv/lib64/python3.12/site-packages/sqlalchemy/testing/assertsql.py:1:# testing/assertsql.py
./crypto-venv/lib64/python3.12/site-packages/narwhals/testing/asserts/frame.py:152:    # Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/py-polars/src/polars/testing/asserts/frame.py#L15-L17
./crypto-venv/lib64/python3.12/site-packages/narwhals/testing/asserts/frame.py:180:    # Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/crates/polars-testing/src/asserts/utils.rs#L829
./crypto-venv/lib64/python3.12/site-packages/narwhals/testing/asserts/frame.py:239:    Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/crates/polars-testing/src/asserts/utils.rs#L667-L698
./crypto-venv/lib64/python3.12/site-packages/pypdf/_codecs/adobe_glyphs.py:2157:    "/assertion": "\u22A6",
./crypto-venv/lib/python3.12/site-packages/playwright/async_api/_generated.py:12201:          is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the
./crypto-venv/lib/python3.12/site-packages/playwright/async_api/_generated.py:12202:          handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't
./crypto-venv/lib/python3.12/site-packages/playwright/async_api/_generated.py:12206:        - The execution time of the handler counts towards the timeout of the action/assertion that executed the handler.
./crypto-venv/lib/python3.12/site-packages/playwright/async_api/_generated.py:12285:            Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of
./crypto-venv/lib/python3.12/site-packages/playwright/sync_api/_generated.py:12269:          is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the
./crypto-venv/lib/python3.12/site-packages/playwright/sync_api/_generated.py:12270:          handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't
./crypto-venv/lib/python3.12/site-packages/playwright/sync_api/_generated.py:12274:        - The execution time of the handler counts towards the timeout of the action/assertion that executed the handler.
./crypto-venv/lib/python3.12/site-packages/playwright/sync_api/_generated.py:12353:            Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of
./crypto-venv/lib/python3.12/site-packages/packageurl/contrib/url2purl.py:342:# https://packagist.org/packages/webmozart/assert#1.9.1
./crypto-venv/lib/python3.12/site-packages/torch/testing/_internal/common_utils.py:3123:# This implements a variant of assertRaises/assertRaisesRegex where we first test
./crypto-venv/lib/python3.12/site-packages/_pytest/python.py:174:                "See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information."
./crypto-venv/lib/python3.12/site-packages/jedi/inference/context.py:93:        # Add isinstance and other if/assert knowledge.
./crypto-venv/lib/python3.12/site-packages/sqlalchemy/testing/assertions.py:1:# testing/assertions.py
./crypto-venv/lib/python3.12/site-packages/sqlalchemy/testing/assertsql.py:1:# testing/assertsql.py
./crypto-venv/lib/python3.12/site-packages/narwhals/testing/asserts/frame.py:152:    # Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/py-polars/src/polars/testing/asserts/frame.py#L15-L17
./crypto-venv/lib/python3.12/site-packages/narwhals/testing/asserts/frame.py:180:    # Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/crates/polars-testing/src/asserts/utils.rs#L829
./crypto-venv/lib/python3.12/site-packages/narwhals/testing/asserts/frame.py:239:    Adapted from https://github.com/pola-rs/polars/blob/afdbf3056d1228cf493901e45f536b0905cec8ea/crates/polars-testing/src/asserts/utils.rs#L667-L698
./crypto-venv/lib/python3.12/site-packages/pypdf/_codecs/adobe_glyphs.py:2157:    "/assertion": "\u22A6",
./auth_router.py:149:    base = os.getenv("ASSERTION_GATEWAY_URL", "http://127.0.0.1:8009").rstrip("/")
./auth_router.py:152:            f"{base}/assert",
./tools/load_noun_assertions.py:22:            "curl", "-s", "-X", "POST", "http://127.0.0.1:7205/noun/assert",
./tools/hp_promote_inference_candidates.py:67:        "curl", "-s", "-X", "POST", "http://127.0.0.1:7205/assert",
grep: ./data/local_resources: Permission denied
grep: ./data/mysql/sys: Permission denied
grep: ./data/mysql/#innodb_temp: Permission denied
grep: ./data/mysql/quantum_ai: Permission denied
grep: ./data/mysql/mysql: Permission denied
grep: ./data/mysql/performance_schema: Permission denied
grep: ./data/mysql/#innodb_redo: Permission denied
./.archive/debug_files_20260630/auth_router.debug.py:56:    base = os.getenv("ASSERTION_GATEWAY_URL", "http://127.0.0.1:8009").rstrip("/")
./.archive/debug_files_20260630/auth_router.debug.py:59:            f"{base}/assert",
./.check_venv/lib64/python3.12/site-packages/chromadb/test/property/test_schema.py:266:    some assumptions/assertions:
./.check_venv/lib/python3.12/site-packages/chromadb/test/property/test_schema.py:266:    some assumptions/assertions:
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ docker inspect jarvis-assertion-gateway --format '{{range .Config.Env}}{{println .}}{{end}}' | sort | \
grep -E 'KYC_DATABASE_URL|DATABASE_URL|POSTGRES|REDIS|PORT'
DATABASE_URL=postgresql://msjarvis:postgres@hp-local-db:5432/hilbert_people
HP_DATABASE_URL=postgresql://postgres@hp-local-db:5432/hilbert_people_test
SERVICE_PORT=8047
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild && \
grep -RIn --include='*.sql' --include='*.py' \
  -E 'kyc_' services/jarvis-assertion-gateway data sql migrations .
services/jarvis-assertion-gateway/app/kyc_reader.py:29:                FROM public.kyc_vault
services/jarvis-assertion-gateway/app/kyc_reader.py:45:                FROM public.kyc_vault
services/jarvis-assertion-gateway/app/kyc_reader.py:60:                FROM public.kyc_location_strip
services/jarvis-assertion-gateway/app/kyc_reader.py:74:                FROM public.kyc_location_strip
services/jarvis-assertion-gateway/app/kyc_reader.py:88:                FROM public.kyc_vault
services/jarvis-assertion-gateway/app/kyc_reader.py:109:                FROM public.kyc_vault
services/jarvis-assertion-gateway/app/claims.py:21:    "beliefid", "worldviewid", "kyc_provider_ref", "ip_address",
services/jarvis-assertion-gateway/app/main.py:22:from .kyc_reader import evaluate_claim
grep: data/local_resources: Permission denied
grep: data/mysql/sys: Permission denied
grep: data/mysql/#innodb_temp: Permission denied
grep: data/mysql/quantum_ai: Permission denied
grep: data/mysql/mysql: Permission denied
grep: data/mysql/performance_schema: Permission denied
grep: data/mysql/#innodb_redo: Permission denied
grep: sql: No such file or directory
migrations/001_kyc_vault.sql:1:CREATE TABLE IF NOT EXISTS kyc_vault (
migrations/001_kyc_vault.sql:5:    kyc_provider    TEXT        DEFAULT 'self_attestation',
migrations/001_kyc_vault.sql:6:    kyc_status      TEXT        DEFAULT 'pending',
migrations/001_kyc_vault.sql:7:    kyc_reference   TEXT,
migrations/001_kyc_vault.sql:20:CREATE INDEX IF NOT EXISTS idx_kyc_vault_secret_uuid ON kyc_vault(secret_uuid);
migrations/001_kyc_vault.sql:21:CREATE INDEX IF NOT EXISTS idx_kyc_vault_ueid        ON kyc_vault(ueid);
migrations/005_three_tier_identity.sql:4:    secret_uuid    UUID NOT NULL REFERENCES public.kyc_vault(secret_uuid) ON DELETE CASCADE,
migrations/004_ledger_event_types.sql:9:        'kyc_location_verified',
./db/schema/mountainshares_tables.sql:61:    kyc_tier        SMALLINT DEFAULT 0 CHECK (kyc_tier IN (0,1,2,3)),
grep: ./msjarvis-rebuild: warning: recursive directory loop
./hp_antisurveillance_guardian_client.py:17:    "public.kyc_vault",
./hp_antisurveillance_guardian_client.py:18:    "public.kyc_location_strip",
./hp_antisurveillance_guardian_client.py:19:    "public.kyc_vault_access_log",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/db/schema/mountainshares_tables.sql:61:    kyc_tier        SMALLINT DEFAULT 0 CHECK (kyc_tier IN (0,1,2,3)),
grep: ./production_closeout_20260728/asbuilt_snapshot_20260728/repo/msjarvis-rebuild: warning: recursive directory loop
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:17:    "public.kyc_vault",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:18:    "public.kyc_location_strip",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/hp_antisurveillance_guardian_client.py:19:    "public.kyc_vault_access_log",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:688:            if metadata.get("target_store") != "kyc_vault":
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:689:                reasons.append("target_store_not_kyc_vault")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:29:                FROM public.kyc_vault
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:45:                FROM public.kyc_vault
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:60:                FROM public.kyc_location_strip
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:74:                FROM public.kyc_location_strip
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:88:                FROM public.kyc_vault
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:109:                FROM public.kyc_vault
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarvis-assertion-gateway/app/claims.py:21:    "beliefid", "worldviewid", "kyc_provider_ref", "ip_address",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarvis-assertion-gateway/app/main.py:22:from .kyc_reader import evaluate_claim
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/hp_antisurveillance_guardian_client.py:17:    "public.kyc_vault",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/hp_antisurveillance_guardian_client.py:18:    "public.kyc_location_strip",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/hp_antisurveillance_guardian_client.py:19:    "public.kyc_vault_access_log",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/jarvis-constitutional-guardian_constitutional_api.py:9:            "tables": ["public.gbim_entities","public.kyc_vault","public.user_documents"],
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/hilbert/write_pipeline.py:30:    "vulnerability_score","ideology","kyc_provider_ref",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/hilbert/identity_registration_promotion.py:28:    target_store: str = "kyc_vault"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/hilbert/identity_registration_promotion.py:63:    if candidate.target_store != "kyc_vault":
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/hilbert/identity_registration_promotion.py:64:        return IdentityRegistrationDecision("SUPPRESS", "target_store_not_kyc_vault", None, None, None, False)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/hilbert/ch36_identity_registration_probe.py:13:    "auth_router.py": ["consent_gated_registration", "kyc_vault"],
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/hilbert/ch36_identity_registration_probe.py:148:        "context": "Ch36 identity registration consent-gated PII write to kyc_vault",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/hilbert/ch36_identity_registration_probe.py:154:            "target_store": "kyc_vault",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/hilbert/ch36_identity_registration_probe.py:166:            "target_store": "kyc_vault",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/hilbert/chroma_policy.py:66:    "vulnerability_score", "ideology", "kyc_provider_ref",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:36:                    "SELECT pms_blocked, bsa_hard_cap, kyc_tier "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/services/conversion_service.py:45:                if (profile["kyc_tier"] or 0) < 1:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:6:        context="User registration — consent-gated PII write to kyc_vault",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:8:        content="Registration path writes user-provided PII to kyc_vault under explicit consent. No H_p entity linkage, no face data, no unified profile formation.",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:10:            "tables": ["public.kyc_vault"],
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:30:import psycopg2 as _kyc_pg
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:31:from security.hp_kyc_topology import (
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:32:    get_primary_kyc_dsn,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:40:_KYC_DSN = get_primary_kyc_dsn()
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:42:def _write_kyc_vault(public_uuid: str, name: str, ueid: str) -> dict:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:54:        conn = _kyc_pg.connect(_KYC_DSN)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:58:            "INSERT INTO kyc_vault "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:59:            "(secret_uuid, verified_name, kyc_provider, kyc_reference, privacy_tier, is_active) "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:316:    # Write PII name to kyc_vault (secret tier) — not Redis
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:318:        _kyc_result = _write_kyc_vault(public_uuid, body.name, ueid) or {}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:321:        _kyc_result = {}
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:338:        "appearance_id": _kyc_result.get("appearance_id", ""),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:347:        commitment_salt=_kyc_result.get("commitment_salt"),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/auth_router.py:348:        appearance_id=_kyc_result.get("appearance_id"),
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/scratch_edits/chroma_policy_edit.py:63:    "vulnerability_score", "ideology", "kyc_provider_ref",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/tests/policy/test_constitutional_guard.py:41:    def test_kyc_suppresses(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/tests/policy/test_constitutional_guard.py:80:    def test_kyc_collection_rejected(self):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/tests/policy/test_constitutional_guard.py:82:            assert_collection_allowed("kyc_mirror")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/tests/test_ch36_identity_registration_promotion.py:22:def test_permits_consented_kyc_registration():
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/tests/test_ch36_identity_registration_promotion.py:25:    assert decision.target_store == "kyc_vault"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/tests/test_antisurveillance_guard.py:30:        content="Assemble unified person profile from gbim_entities, kyc_vault, faces.",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/tests/test_antisurveillance_guard.py:32:            "tables": ["public.gbim_beliefs","public.kyc_vault","public.user_documents"],
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/tests/test_antisurveillance_guard.py:45:        content="Link identity across kyc_vault and gbim_beliefs.",
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/001_kyc_vault.sql:1:CREATE TABLE IF NOT EXISTS kyc_vault (
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/001_kyc_vault.sql:5:    kyc_provider    TEXT        DEFAULT 'self_attestation',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/001_kyc_vault.sql:6:    kyc_status      TEXT        DEFAULT 'pending',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/001_kyc_vault.sql:7:    kyc_reference   TEXT,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/001_kyc_vault.sql:20:CREATE INDEX IF NOT EXISTS idx_kyc_vault_secret_uuid ON kyc_vault(secret_uuid);
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/001_kyc_vault.sql:21:CREATE INDEX IF NOT EXISTS idx_kyc_vault_ueid        ON kyc_vault(ueid);
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/005_three_tier_identity.sql:4:    secret_uuid    UUID NOT NULL REFERENCES public.kyc_vault(secret_uuid) ON DELETE CASCADE,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/migrations/004_ledger_event_types.sql:9:        'kyc_location_verified',
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/security/hp_kyc_topology.py:10:DEFAULT_TOPOLOGY_PATH = Path.home() / "jarvis_audit" / "policy" / "hp_kyc_mapping.yaml"
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/security/hp_kyc_topology.py:70:def get_primary_kyc_dsn() -> str:
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:10:            "tables": ["public.gbim_entities","public.kyc_vault","public.user_documents"],
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:30:import psycopg2 as _kyc_pg
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:36:def _write_kyc_vault(public_uuid: str, name: str, ueid: str):
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:37:    """Write verified name to kyc_vault secret tier. Never stored in Redis."""
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:39:        conn = _kyc_pg.connect(_KYC_DSN)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:42:            "INSERT INTO kyc_vault "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:43:            "(secret_uuid, verified_name, kyc_provider, kyc_reference, privacy_tier, is_active) "
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:210:    # Write PII name to kyc_vault (secret tier) — not Redis
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/.archive/debug_files_20260630/auth_router.debug.py:211:    _write_kyc_vault(public_uuid, body.name, ueid)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:21:    kyc_provider: Optional[str] = None
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:22:    kyc_reference: Optional[str] = None
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:47:            CREATE TABLE IF NOT EXISTS kyc_vault (
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:53:                kyc_provider TEXT,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:54:                kyc_reference TEXT,
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:62:            CREATE TABLE IF NOT EXISTS kyc_location_strip (
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:87:        await conn.execute("ALTER TABLE kyc_location_strip ALTER COLUMN lat DROP NOT NULL;")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:88:        await conn.execute("ALTER TABLE kyc_location_strip ALTER COLUMN lon DROP NOT NULL;")
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:90:            CREATE TABLE IF NOT EXISTS kyc_consent_registry (
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:107:                    WHERE conname = 'kyc_location_strip_encryption_guard'
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:109:                    ALTER TABLE kyc_location_strip
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:110:                    ADD CONSTRAINT kyc_location_strip_encryption_guard
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:120:            ALTER TABLE kyc_location_strip
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:121:            VALIDATE CONSTRAINT kyc_location_strip_encryption_guard;
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:137:                INSERT INTO kyc_vault
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:138:                    (verified_name, verified_dob, verified_at, kyc_provider, kyc_reference, privacy_tier, is_active)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:142:            """, req.verified_name, req.verified_dob, req.kyc_provider, req.kyc_reference, req.privacy_tier)
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:155:                INSERT INTO kyc_location_strip
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:237:            INSERT INTO kyc_consent_registry
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:255:                UPDATE kyc_consent_registry
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:263:                UPDATE kyc_consent_registry
./production_closeout_20260728/asbuilt_snapshot_20260728/repo/kyc-vault/app.py:276:            FROM kyc_consent_registry
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:688:            if metadata.get("target_store") != "kyc_vault":
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:689:                reasons.append("target_store_not_kyc_vault")
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/jarvis-assertion-gateway/app/kyc_reader.py:29:                FROM public.kyc_vault
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/jarvis-assertion-gateway/app/kyc_reader.py:45:                FROM public.kyc_vault
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/jarvis-assertion-gateway/app/kyc_reader.py:60:                FROM public.kyc_location_strip
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/jarvis-assertion-gateway/app/kyc_reader.py:74:                FROM public.kyc_location_strip
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/jarvis-assertion-gateway/app/kyc_reader.py:88:                FROM public.kyc_vault
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/jarvis-assertion-gateway/app/kyc_reader.py:109:                FROM public.kyc_vault
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/jarvis-assertion-gateway/app/claims.py:21:    "beliefid", "worldviewid", "kyc_provider_ref", "ip_address",
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/jarvis-assertion-gateway/app/main.py:22:from .kyc_reader import evaluate_claim
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/hp_antisurveillance_guardian_client.py:17:    "public.kyc_vault",
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/hp_antisurveillance_guardian_client.py:18:    "public.kyc_location_strip",
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/hp_antisurveillance_guardian_client.py:19:    "public.kyc_vault_access_log",
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/jarvis-constitutional-guardian_constitutional_api.py:9:            "tables": ["public.gbim_entities","public.kyc_vault","public.user_documents"],
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/hilbert/write_pipeline.py:30:    "vulnerability_score","ideology","kyc_provider_ref",
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/hilbert/identity_registration_promotion.py:28:    target_store: str = "kyc_vault"
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/hilbert/identity_registration_promotion.py:63:    if candidate.target_store != "kyc_vault":
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/hilbert/identity_registration_promotion.py:64:        return IdentityRegistrationDecision("SUPPRESS", "target_store_not_kyc_vault", None, None, None, False)
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/hilbert/ch36_identity_registration_probe.py:13:    "auth_router.py": ["consent_gated_registration", "kyc_vault"],
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/hilbert/ch36_identity_registration_probe.py:148:        "context": "Ch36 identity registration consent-gated PII write to kyc_vault",
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/hilbert/ch36_identity_registration_probe.py:154:            "target_store": "kyc_vault",
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/hilbert/ch36_identity_registration_probe.py:166:            "target_store": "kyc_vault",
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/hilbert/chroma_policy.py:66:    "vulnerability_score", "ideology", "kyc_provider_ref",
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:36:                    "SELECT pms_blocked, bsa_hard_cap, kyc_tier "
./production_closeout_20260728/snapshot_deploy/bbb-asbuilt-build-context.UentYg/services/conversion_service.py:45:                if (profile["kyc_tier"] or 0) < 1:
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:688:            if metadata.get("target_store") != "kyc_vault":
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:689:                reasons.append("target_store_not_kyc_vault")
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/jarvis-assertion-gateway/app/kyc_reader.py:29:                FROM public.kyc_vault
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/jarvis-assertion-gateway/app/kyc_reader.py:45:                FROM public.kyc_vault
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/jarvis-assertion-gateway/app/kyc_reader.py:60:                FROM public.kyc_location_strip
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/jarvis-assertion-gateway/app/kyc_reader.py:74:                FROM public.kyc_location_strip
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/jarvis-assertion-gateway/app/kyc_reader.py:88:                FROM public.kyc_vault
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/jarvis-assertion-gateway/app/kyc_reader.py:109:                FROM public.kyc_vault
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/jarvis-assertion-gateway/app/claims.py:21:    "beliefid", "worldviewid", "kyc_provider_ref", "ip_address",
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/jarvis-assertion-gateway/app/main.py:22:from .kyc_reader import evaluate_claim
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/hp_antisurveillance_guardian_client.py:17:    "public.kyc_vault",
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/hp_antisurveillance_guardian_client.py:18:    "public.kyc_location_strip",
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/hp_antisurveillance_guardian_client.py:19:    "public.kyc_vault_access_log",
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/jarvis-constitutional-guardian_constitutional_api.py:9:            "tables": ["public.gbim_entities","public.kyc_vault","public.user_documents"],
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/hilbert/write_pipeline.py:30:    "vulnerability_score","ideology","kyc_provider_ref",
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/hilbert/identity_registration_promotion.py:28:    target_store: str = "kyc_vault"
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/hilbert/identity_registration_promotion.py:63:    if candidate.target_store != "kyc_vault":
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/hilbert/identity_registration_promotion.py:64:        return IdentityRegistrationDecision("SUPPRESS", "target_store_not_kyc_vault", None, None, None, False)
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/hilbert/ch36_identity_registration_probe.py:13:    "auth_router.py": ["consent_gated_registration", "kyc_vault"],
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/hilbert/ch36_identity_registration_probe.py:148:        "context": "Ch36 identity registration consent-gated PII write to kyc_vault",
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/hilbert/ch36_identity_registration_probe.py:154:            "target_store": "kyc_vault",
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/hilbert/ch36_identity_registration_probe.py:166:            "target_store": "kyc_vault",
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/hilbert/chroma_policy.py:66:    "vulnerability_score", "ideology", "kyc_provider_ref",
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:36:                    "SELECT pms_blocked, bsa_hard_cap, kyc_tier "
./production_closeout_20260728/snapshot_deploy/nbb-i-containers-build-context.IWcKqD/services/conversion_service.py:45:                if (profile["kyc_tier"] or 0) < 1:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/db/schema/mountainshares_tables.sql:61:    kyc_tier        SMALLINT DEFAULT 0 CHECK (kyc_tier IN (0,1,2,3)),
grep: ./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/msjarvis-rebuild: warning: recursive directory loop
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/hp_antisurveillance_guardian_client.py:17:    "public.kyc_vault",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/hp_antisurveillance_guardian_client.py:18:    "public.kyc_location_strip",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/hp_antisurveillance_guardian_client.py:19:    "public.kyc_vault_access_log",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:688:            if metadata.get("target_store") != "kyc_vault":
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:689:                reasons.append("target_store_not_kyc_vault")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:29:                FROM public.kyc_vault
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:45:                FROM public.kyc_vault
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:60:                FROM public.kyc_location_strip
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:74:                FROM public.kyc_location_strip
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:88:                FROM public.kyc_vault
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/jarvis-assertion-gateway/app/kyc_reader.py:109:                FROM public.kyc_vault
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/jarvis-assertion-gateway/app/claims.py:21:    "beliefid", "worldviewid", "kyc_provider_ref", "ip_address",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/jarvis-assertion-gateway/app/main.py:22:from .kyc_reader import evaluate_claim
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/hp_antisurveillance_guardian_client.py:17:    "public.kyc_vault",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/hp_antisurveillance_guardian_client.py:18:    "public.kyc_location_strip",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/hp_antisurveillance_guardian_client.py:19:    "public.kyc_vault_access_log",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/jarvis-constitutional-guardian_constitutional_api.py:9:            "tables": ["public.gbim_entities","public.kyc_vault","public.user_documents"],
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/hilbert/write_pipeline.py:30:    "vulnerability_score","ideology","kyc_provider_ref",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/hilbert/identity_registration_promotion.py:28:    target_store: str = "kyc_vault"
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/hilbert/identity_registration_promotion.py:63:    if candidate.target_store != "kyc_vault":
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/hilbert/identity_registration_promotion.py:64:        return IdentityRegistrationDecision("SUPPRESS", "target_store_not_kyc_vault", None, None, None, False)
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/hilbert/ch36_identity_registration_probe.py:13:    "auth_router.py": ["consent_gated_registration", "kyc_vault"],
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/hilbert/ch36_identity_registration_probe.py:148:        "context": "Ch36 identity registration consent-gated PII write to kyc_vault",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/hilbert/ch36_identity_registration_probe.py:154:            "target_store": "kyc_vault",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/hilbert/ch36_identity_registration_probe.py:166:            "target_store": "kyc_vault",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/hilbert/chroma_policy.py:66:    "vulnerability_score", "ideology", "kyc_provider_ref",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:36:                    "SELECT pms_blocked, bsa_hard_cap, kyc_tier "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/services/conversion_service.py:45:                if (profile["kyc_tier"] or 0) < 1:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:6:        context="User registration — consent-gated PII write to kyc_vault",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:8:        content="Registration path writes user-provided PII to kyc_vault under explicit consent. No H_p entity linkage, no face data, no unified profile formation.",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:10:            "tables": ["public.kyc_vault"],
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:30:import psycopg2 as _kyc_pg
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:31:from security.hp_kyc_topology import (
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:32:    get_primary_kyc_dsn,
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:40:_KYC_DSN = get_primary_kyc_dsn()
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:42:def _write_kyc_vault(public_uuid: str, name: str, ueid: str) -> dict:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:54:        conn = _kyc_pg.connect(_KYC_DSN)
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:58:            "INSERT INTO kyc_vault "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:59:            "(secret_uuid, verified_name, kyc_provider, kyc_reference, privacy_tier, is_active) "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:316:    # Write PII name to kyc_vault (secret tier) — not Redis
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:318:        _kyc_result = _write_kyc_vault(public_uuid, body.name, ueid) or {}
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:321:        _kyc_result = {}
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:338:        "appearance_id": _kyc_result.get("appearance_id", ""),
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:347:        commitment_salt=_kyc_result.get("commitment_salt"),
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/auth_router.py:348:        appearance_id=_kyc_result.get("appearance_id"),
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/scratch_edits/chroma_policy_edit.py:63:    "vulnerability_score", "ideology", "kyc_provider_ref",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/tests/policy/test_constitutional_guard.py:41:    def test_kyc_suppresses(self):
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/tests/policy/test_constitutional_guard.py:80:    def test_kyc_collection_rejected(self):
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/tests/policy/test_constitutional_guard.py:82:            assert_collection_allowed("kyc_mirror")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/tests/test_ch36_identity_registration_promotion.py:22:def test_permits_consented_kyc_registration():
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/tests/test_ch36_identity_registration_promotion.py:25:    assert decision.target_store == "kyc_vault"
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/tests/test_antisurveillance_guard.py:30:        content="Assemble unified person profile from gbim_entities, kyc_vault, faces.",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/tests/test_antisurveillance_guard.py:32:            "tables": ["public.gbim_beliefs","public.kyc_vault","public.user_documents"],
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/tests/test_antisurveillance_guard.py:45:        content="Link identity across kyc_vault and gbim_beliefs.",
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/001_kyc_vault.sql:1:CREATE TABLE IF NOT EXISTS kyc_vault (
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/001_kyc_vault.sql:5:    kyc_provider    TEXT        DEFAULT 'self_attestation',
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/001_kyc_vault.sql:6:    kyc_status      TEXT        DEFAULT 'pending',
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/001_kyc_vault.sql:7:    kyc_reference   TEXT,
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/001_kyc_vault.sql:20:CREATE INDEX IF NOT EXISTS idx_kyc_vault_secret_uuid ON kyc_vault(secret_uuid);
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/001_kyc_vault.sql:21:CREATE INDEX IF NOT EXISTS idx_kyc_vault_ueid        ON kyc_vault(ueid);
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/005_three_tier_identity.sql:4:    secret_uuid    UUID NOT NULL REFERENCES public.kyc_vault(secret_uuid) ON DELETE CASCADE,
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/migrations/004_ledger_event_types.sql:9:        'kyc_location_verified',
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/security/hp_kyc_topology.py:10:DEFAULT_TOPOLOGY_PATH = Path.home() / "jarvis_audit" / "policy" / "hp_kyc_mapping.yaml"
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/security/hp_kyc_topology.py:70:def get_primary_kyc_dsn() -> str:
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:10:            "tables": ["public.gbim_entities","public.kyc_vault","public.user_documents"],
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:30:import psycopg2 as _kyc_pg
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:36:def _write_kyc_vault(public_uuid: str, name: str, ueid: str):
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:37:    """Write verified name to kyc_vault secret tier. Never stored in Redis."""
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:39:        conn = _kyc_pg.connect(_KYC_DSN)
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:42:            "INSERT INTO kyc_vault "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:43:            "(secret_uuid, verified_name, kyc_provider, kyc_reference, privacy_tier, is_active) "
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:210:    # Write PII name to kyc_vault (secret tier) — not Redis
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/.archive/debug_files_20260630/auth_router.debug.py:211:    _write_kyc_vault(public_uuid, body.name, ueid)
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:21:    kyc_provider: Optional[str] = None
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:22:    kyc_reference: Optional[str] = None
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:47:            CREATE TABLE IF NOT EXISTS kyc_vault (
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:53:                kyc_provider TEXT,
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:54:                kyc_reference TEXT,
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:62:            CREATE TABLE IF NOT EXISTS kyc_location_strip (
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:87:        await conn.execute("ALTER TABLE kyc_location_strip ALTER COLUMN lat DROP NOT NULL;")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:88:        await conn.execute("ALTER TABLE kyc_location_strip ALTER COLUMN lon DROP NOT NULL;")
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:90:            CREATE TABLE IF NOT EXISTS kyc_consent_registry (
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:107:                    WHERE conname = 'kyc_location_strip_encryption_guard'
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:109:                    ALTER TABLE kyc_location_strip
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:110:                    ADD CONSTRAINT kyc_location_strip_encryption_guard
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:120:            ALTER TABLE kyc_location_strip
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:121:            VALIDATE CONSTRAINT kyc_location_strip_encryption_guard;
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:137:                INSERT INTO kyc_vault
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:138:                    (verified_name, verified_dob, verified_at, kyc_provider, kyc_reference, privacy_tier, is_active)
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:142:            """, req.verified_name, req.verified_dob, req.kyc_provider, req.kyc_reference, req.privacy_tier)
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:155:                INSERT INTO kyc_location_strip
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:237:            INSERT INTO kyc_consent_registry
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:255:                UPDATE kyc_consent_registry
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:263:                UPDATE kyc_consent_registry
./production_closeout_20260728/asbuilt_snapshot_20260728_complete/repo/kyc-vault/app.py:276:            FROM kyc_consent_registry
./production_closeout_20260728/backups/wv_gis_schema_20260728_001859.sql:234:CREATE FUNCTION private.get_hilbert_person_governed(p_requester_role text, p_requester_subject text, p_request_purpose text, p_legal_basis text, p_case_id text, p_subject_lookup text) RETURNS TABLE(person_id text, full_name text, date_of_birth date, kyc_status text)
./production_closeout_20260728/backups/wv_gis_schema_20260728_001859.sql:349:        hp.kyc_status::text
./production_closeout_20260728/backups/wv_gis_schema_20260728_001859.sql:2475:    kyc_status text,
./services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:688:            if metadata.get("target_store") != "kyc_vault":
./services/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:689:                reasons.append("target_store_not_kyc_vault")
grep: ./services/ms_jarvis_mother_carrie_protocols.py: Permission denied
./services/jarvis-assertion-gateway/app/kyc_reader.py:29:                FROM public.kyc_vault
./services/jarvis-assertion-gateway/app/kyc_reader.py:45:                FROM public.kyc_vault
./services/jarvis-assertion-gateway/app/kyc_reader.py:60:                FROM public.kyc_location_strip
./services/jarvis-assertion-gateway/app/kyc_reader.py:74:                FROM public.kyc_location_strip
./services/jarvis-assertion-gateway/app/kyc_reader.py:88:                FROM public.kyc_vault
./services/jarvis-assertion-gateway/app/kyc_reader.py:109:                FROM public.kyc_vault
./services/jarvis-assertion-gateway/app/claims.py:21:    "beliefid", "worldviewid", "kyc_provider_ref", "ip_address",
./services/jarvis-assertion-gateway/app/main.py:22:from .kyc_reader import evaluate_claim
./services/hp_antisurveillance_guardian_client.py:17:    "public.kyc_vault",
./services/hp_antisurveillance_guardian_client.py:18:    "public.kyc_location_strip",
./services/hp_antisurveillance_guardian_client.py:19:    "public.kyc_vault_access_log",
./services/jarvis-constitutional-guardian_constitutional_api.py:9:            "tables": ["public.gbim_entities","public.kyc_vault","public.user_documents"],
./services/hilbert/write_pipeline.py:30:    "vulnerability_score","ideology","kyc_provider_ref",
./services/hilbert/identity_registration_promotion.py:28:    target_store: str = "kyc_vault"
./services/hilbert/identity_registration_promotion.py:63:    if candidate.target_store != "kyc_vault":
./services/hilbert/identity_registration_promotion.py:64:        return IdentityRegistrationDecision("SUPPRESS", "target_store_not_kyc_vault", None, None, None, False)
./services/hilbert/ch36_identity_registration_probe.py:13:    "auth_router.py": ["consent_gated_registration", "kyc_vault"],
./services/hilbert/ch36_identity_registration_probe.py:148:        "context": "Ch36 identity registration consent-gated PII write to kyc_vault",
./services/hilbert/ch36_identity_registration_probe.py:154:            "target_store": "kyc_vault",
./services/hilbert/ch36_identity_registration_probe.py:166:            "target_store": "kyc_vault",
./services/hilbert/chroma_policy.py:66:    "vulnerability_score", "ideology", "kyc_provider_ref",
./services/conversion_service.py:36:                    "SELECT pms_blocked, bsa_hard_cap, kyc_tier "
./services/conversion_service.py:45:                if (profile["kyc_tier"] or 0) < 1:
./auth_router.py:6:        context="User registration — consent-gated PII write to kyc_vault",
./auth_router.py:8:        content="Registration path writes user-provided PII to kyc_vault under explicit consent. No H_p entity linkage, no face data, no unified profile formation.",
./auth_router.py:10:            "tables": ["public.kyc_vault"],
./auth_router.py:30:import psycopg2 as _kyc_pg
./auth_router.py:31:from security.hp_kyc_topology import (
./auth_router.py:32:    get_primary_kyc_dsn,
./auth_router.py:40:_KYC_DSN = get_primary_kyc_dsn()
./auth_router.py:42:def _write_kyc_vault(public_uuid: str, name: str, ueid: str) -> dict:
./auth_router.py:54:        conn = _kyc_pg.connect(_KYC_DSN)
./auth_router.py:58:            "INSERT INTO kyc_vault "
./auth_router.py:59:            "(secret_uuid, verified_name, kyc_provider, kyc_reference, privacy_tier, is_active) "
./auth_router.py:316:    # Write PII name to kyc_vault (secret tier) — not Redis
./auth_router.py:318:        _kyc_result = _write_kyc_vault(public_uuid, body.name, ueid) or {}
./auth_router.py:321:        _kyc_result = {}
./auth_router.py:338:        "appearance_id": _kyc_result.get("appearance_id", ""),
./auth_router.py:347:        commitment_salt=_kyc_result.get("commitment_salt"),
./auth_router.py:348:        appearance_id=_kyc_result.get("appearance_id"),
./scratch_edits/chroma_policy_edit.py:63:    "vulnerability_score", "ideology", "kyc_provider_ref",
./tests/policy/test_constitutional_guard.py:41:    def test_kyc_suppresses(self):
./tests/policy/test_constitutional_guard.py:80:    def test_kyc_collection_rejected(self):
./tests/policy/test_constitutional_guard.py:82:            assert_collection_allowed("kyc_mirror")
./tests/test_ch36_identity_registration_promotion.py:22:def test_permits_consented_kyc_registration():
./tests/test_ch36_identity_registration_promotion.py:25:    assert decision.target_store == "kyc_vault"
./tests/test_antisurveillance_guard.py:30:        content="Assemble unified person profile from gbim_entities, kyc_vault, faces.",
./tests/test_antisurveillance_guard.py:32:            "tables": ["public.gbim_beliefs","public.kyc_vault","public.user_documents"],
./tests/test_antisurveillance_guard.py:45:        content="Link identity across kyc_vault and gbim_beliefs.",
./migrations/001_kyc_vault.sql:1:CREATE TABLE IF NOT EXISTS kyc_vault (
./migrations/001_kyc_vault.sql:5:    kyc_provider    TEXT        DEFAULT 'self_attestation',
./migrations/001_kyc_vault.sql:6:    kyc_status      TEXT        DEFAULT 'pending',
./migrations/001_kyc_vault.sql:7:    kyc_reference   TEXT,
./migrations/001_kyc_vault.sql:20:CREATE INDEX IF NOT EXISTS idx_kyc_vault_secret_uuid ON kyc_vault(secret_uuid);
./migrations/001_kyc_vault.sql:21:CREATE INDEX IF NOT EXISTS idx_kyc_vault_ueid        ON kyc_vault(ueid);
./migrations/005_three_tier_identity.sql:4:    secret_uuid    UUID NOT NULL REFERENCES public.kyc_vault(secret_uuid) ON DELETE CASCADE,
./migrations/004_ledger_event_types.sql:9:        'kyc_location_verified',
./security/hp_kyc_topology.py:10:DEFAULT_TOPOLOGY_PATH = Path.home() / "jarvis_audit" / "policy" / "hp_kyc_mapping.yaml"
./security/hp_kyc_topology.py:70:def get_primary_kyc_dsn() -> str:
grep: ./data/local_resources: Permission denied
grep: ./data/mysql/sys: Permission denied
grep: ./data/mysql/#innodb_temp: Permission denied
grep: ./data/mysql/quantum_ai: Permission denied
grep: ./data/mysql/mysql: Permission denied
grep: ./data/mysql/performance_schema: Permission denied
grep: ./data/mysql/#innodb_redo: Permission denied
./.archive/debug_files_20260630/auth_router.debug.py:10:            "tables": ["public.gbim_entities","public.kyc_vault","public.user_documents"],
./.archive/debug_files_20260630/auth_router.debug.py:30:import psycopg2 as _kyc_pg
./.archive/debug_files_20260630/auth_router.debug.py:36:def _write_kyc_vault(public_uuid: str, name: str, ueid: str):
./.archive/debug_files_20260630/auth_router.debug.py:37:    """Write verified name to kyc_vault secret tier. Never stored in Redis."""
./.archive/debug_files_20260630/auth_router.debug.py:39:        conn = _kyc_pg.connect(_KYC_DSN)
./.archive/debug_files_20260630/auth_router.debug.py:42:            "INSERT INTO kyc_vault "
./.archive/debug_files_20260630/auth_router.debug.py:43:            "(secret_uuid, verified_name, kyc_provider, kyc_reference, privacy_tier, is_active) "
./.archive/debug_files_20260630/auth_router.debug.py:210:    # Write PII name to kyc_vault (secret tier) — not Redis
./.archive/debug_files_20260630/auth_router.debug.py:211:    _write_kyc_vault(public_uuid, body.name, ueid)
./kyc-vault/app.py:21:    kyc_provider: Optional[str] = None
./kyc-vault/app.py:22:    kyc_reference: Optional[str] = None
./kyc-vault/app.py:47:            CREATE TABLE IF NOT EXISTS kyc_vault (
./kyc-vault/app.py:53:                kyc_provider TEXT,
./kyc-vault/app.py:54:                kyc_reference TEXT,
./kyc-vault/app.py:62:            CREATE TABLE IF NOT EXISTS kyc_location_strip (
./kyc-vault/app.py:87:        await conn.execute("ALTER TABLE kyc_location_strip ALTER COLUMN lat DROP NOT NULL;")
./kyc-vault/app.py:88:        await conn.execute("ALTER TABLE kyc_location_strip ALTER COLUMN lon DROP NOT NULL;")
./kyc-vault/app.py:90:            CREATE TABLE IF NOT EXISTS kyc_consent_registry (
./kyc-vault/app.py:107:                    WHERE conname = 'kyc_location_strip_encryption_guard'
./kyc-vault/app.py:109:                    ALTER TABLE kyc_location_strip
./kyc-vault/app.py:110:                    ADD CONSTRAINT kyc_location_strip_encryption_guard
./kyc-vault/app.py:120:            ALTER TABLE kyc_location_strip
./kyc-vault/app.py:121:            VALIDATE CONSTRAINT kyc_location_strip_encryption_guard;
./kyc-vault/app.py:137:                INSERT INTO kyc_vault
./kyc-vault/app.py:138:                    (verified_name, verified_dob, verified_at, kyc_provider, kyc_reference, privacy_tier, is_active)
./kyc-vault/app.py:142:            """, req.verified_name, req.verified_dob, req.kyc_provider, req.kyc_reference, req.privacy_tier)
./kyc-vault/app.py:155:                INSERT INTO kyc_location_strip
./kyc-vault/app.py:237:            INSERT INTO kyc_consent_registry
./kyc-vault/app.py:255:                UPDATE kyc_consent_registry
./kyc-vault/app.py:263:                UPDATE kyc_consent_registry
./kyc-vault/app.py:276:            FROM kyc_consent_registry
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

