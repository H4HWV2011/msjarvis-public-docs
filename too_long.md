(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild

# 1) Look for env variables that define DB host, name, user
grep -RInE 'DATABASE_URL|DB_HOST|DB_PORT|DB_USER|DB_NAME|SUPABASE_URL|SUPABASE' . 2>/dev/null

# 2) Inspect docker-compose for a Postgres service and its DB name
grep -RInE 'postgres' docker-compose*.yml 2>/dev/null || echo "no docker-compose postgres section found"

# 3) Look for Prisma / ORM / migration files that define the schema
find . -maxdepth 5 \( -name 'schema.prisma' -o -name 'migrations.sql' -o -name '*migration*.sql' -o -name '*schema*.sql' \) 2>/dev/null

# 4) Look for a separate auth or app DB in configs
grep -RInE 'msjarvisgis|gisdb|gbim|auth' .env* config* 2>/dev/null
./docker-compose.yml.bak.20260501:13:    - DATABASE_URL=postgresql://postgres:pgtemp123@msjarvis-db:5432/msjarvisgis
./docker-compose.yml.bak.20260501:43:    - DATABASE_URL=postgresql://postgres:pgtemp123@msjarvis-db:5432/msjarvisgis
./docker-compose.yml.bak.20260501:1270:    - DATABASE_URL=postgresql://postgres:pgtemp123@msjarvis-db:5432/msjarvisgis
./docker-compose.yml.bak.20260501:1373:    - DATABASE_URL=postgresql://postgres:pgtemp123@msjarvis-db:5432/msjarvisgis
./docker-compose.yml.bak.20260501:1545:      DATABASE_URL: postgresql://msjarvis:msjarvis@jarvis-local-resources-db:5432/msjarvisgis
./gis_service/router.py:13:    "GIS_DATABASE_URL",
./docker-compose.yml.bak.20260422-204722:1471:      DATABASE_URL: postgresql://msjarvis:${DB_PASSWORD}@msjarvis-db:5432/msjarvis
./.env:19:DATABASE_URL=postgresql://postgres:postgres@127.0.0.1:5435/local_resources
./.env:153:LOCALDB_HOST_PORT=5435
./docker-compose.yml.bak.20260422-204609:1471:      DATABASE_URL: postgresql://msjarvis:${DB_PASSWORD}@msjarvis-db:5432/msjarvis
./docker-compose.yml.bak_hilbert_depsfix_20260415-142340:92:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.bak_hilbert_depsfix_20260415-142340:93:      DB_PORT: '5432'
./docker-compose.yml.bak_hilbert_depsfix_20260415-142340:94:      DB_NAME: local_resources
./docker-compose.yml.bak_hilbert_depsfix_20260415-142340:95:      DB_USER: postgres
./docker-compose.yml.bak_hilbert_depsfix_20260415-142340:97:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./docker-compose.yml.pre-secrets-fix:1471:      DATABASE_URL: postgresql://msjarvis:${DB_PASSWORD}@msjarvis-db:5432/msjarvis
./docker-compose.yml.bak.20260517-162627:1234:      - GIS_DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
./docker-compose.yml.bak_20260415-111235:90:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.bak_20260415-111235:91:      DB_PORT: '5432'
./docker-compose.yml.bak_20260415-111235:92:      DB_NAME: local_resources
./docker-compose.yml.bak_20260415-111235:93:      DB_USER: postgres
./docker-compose.yml.bak_20260415-111235:95:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./docker-compose.yml.backup_20260318_110223:22:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_110223:23:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_110223:24:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110223:25:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_110223:451:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_110223:452:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_110223:453:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110223:454:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_110223:776:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_110223:777:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_110223:778:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110223:779:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_110223:1066:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_110223:1067:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_110223:1068:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110223:1069:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_110223:1192:      - DB_HOST=172.17.0.1
./docker-compose.yml.backup_20260318_110223:1193:      - DB_PORT=5432
./docker-compose.yml.backup_20260318_110223:1194:      - DB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110223:1195:      - DB_USER=msjarvis
./docker-compose.yml.bak.20260407-221457:1219:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.bak.20260407-221457:1220:    - GISDB_PORT=5432
./docker-compose.yml.bak.20260407-221457:1221:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.bak.20260407-221457:1222:    - GISDB_USER=msjarvis
./docker-compose.yml.bak.20260407-221457:1248:    - DB_HOST=172.17.0.1
./docker-compose.yml.bak.20260407-221457:1249:    - DB_PORT=5432
./docker-compose.yml.bak.20260407-221457:1250:    - DB_NAME=msjarvisgis
./docker-compose.yml.bak.20260407-221457:1251:    - DB_USER=msjarvis
./docker-compose.yml:1283:      - GIS_DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
./docker-compose.yml.bak_hilbert_depsfix_20260415-142332:92:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.bak_hilbert_depsfix_20260415-142332:93:      DB_PORT: '5432'
./docker-compose.yml.bak_hilbert_depsfix_20260415-142332:94:      DB_NAME: local_resources
./docker-compose.yml.bak_hilbert_depsfix_20260415-142332:95:      DB_USER: postgres
./docker-compose.yml.bak_hilbert_depsfix_20260415-142332:97:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./.env.backup-20260505:21:DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./.env.backup-20260505:22:DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
./_archive/service_baks_20260430/docker-compose.yml.backup-corrupted-1763229905:134:      CHROMADB_HOST: chroma
./_archive/service_baks_20260430/docker-compose.yml.backup-corrupted-1763229905:135:      CHROMADB_PORT: 8010
./_archive/service_baks_20260430/docker-compose.yml.backup-1763229864:134:      CHROMADB_HOST: chroma
./_archive/service_baks_20260430/docker-compose.yml.backup-1763229864:135:      CHROMADB_PORT: 8010
./_archive/service_baks_20260430/auth_router.py.bak:233:    _dsn = _os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL")
./_archive/service_baks_20260430/auth_router.py.bak:319:        _dsn = _os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL")
./_archive/service_baks_20260430/auth_router.py.bak:506:    pg_dsn = _os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL")
./_archive/service_baks_20260430/auth_router.py.bak:562:    _dsn = (_os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL", ""))
./docker-compose.yml.bak.20260416_145312:1229:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.bak.20260416_145312:1230:    - GISDB_PORT=5432
./docker-compose.yml.bak.20260416_145312:1231:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416_145312:1232:    - GISDB_USER=msjarvis
./docker-compose.yml.bak.20260416_145312:1258:    - DB_HOST=172.17.0.1
./docker-compose.yml.bak.20260416_145312:1259:    - DB_PORT=5432
./docker-compose.yml.bak.20260416_145312:1260:    - DB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416_145312:1261:    - DB_USER=msjarvis
./.env.complete:21:DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./.env.complete:22:DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
./.env.bak:19:DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1495:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1496:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1497:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1498:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1524:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1525:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1526:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1527:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1501:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1502:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1503:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1504:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1530:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1531:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1532:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1533:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1506:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1507:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1508:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1509:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1535:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1536:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1537:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1538:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1495:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1496:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1497:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1498:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1524:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1525:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1526:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1527:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1495:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1496:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1497:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1498:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1524:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1525:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1526:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1527:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1504:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1505:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1506:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1507:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1533:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1534:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1535:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1536:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml:1530:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml:1531:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml:1532:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml:1533:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml:1559:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml:1560:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml:1561:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml:1562:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1506:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1507:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1508:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1509:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1535:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1536:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1537:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1538:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1502:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1503:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1504:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1505:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1531:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1532:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1533:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1534:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1509:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1510:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1511:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1512:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1538:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1539:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1540:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1541:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1501:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1502:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1503:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1504:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1530:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1531:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1532:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1533:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1512:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1513:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1514:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1515:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1541:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1542:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1543:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1544:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1508:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1509:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1510:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1511:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1537:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1538:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1539:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1540:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1512:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1513:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1514:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1515:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1541:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1542:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1543:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1544:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1495:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1496:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1497:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1498:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1524:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1525:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1526:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1527:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1504:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1505:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1506:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1507:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1533:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1534:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1535:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1536:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1498:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1499:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1500:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1501:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1527:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1528:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1529:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1530:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1509:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1510:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1511:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1512:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1538:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1539:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1540:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1541:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1498:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1499:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1500:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1501:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1527:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1528:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1529:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1530:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1502:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1503:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1504:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1505:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1531:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1532:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1533:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1534:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1495:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1496:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1497:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1498:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1524:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1525:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1526:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1527:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak:1479:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak:1480:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak:1481:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak:1482:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak:1508:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak:1509:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak:1510:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak:1511:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1509:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1510:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1511:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1512:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1538:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1539:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1540:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1541:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1498:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1499:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1500:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1501:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1527:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1528:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1529:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1530:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1495:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1496:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1497:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1498:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1524:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1525:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1526:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1527:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1495:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1496:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1497:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1498:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1524:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1525:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1526:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1527:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1498:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1499:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1500:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1501:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1527:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1528:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1529:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1530:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1502:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1503:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1504:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1505:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1531:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1532:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1533:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1534:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1495:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1496:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1497:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1498:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1524:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1525:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1526:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1527:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1495:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1496:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1497:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1498:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1524:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1525:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1526:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1527:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1495:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1496:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1497:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1498:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1524:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1525:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1526:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1527:    - DB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1512:    - GISDB_HOST=172.18.0.1
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1513:    - GISDB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1514:    - GISDB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1515:    - GISDB_USER=msjarvis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1541:    - DB_HOST=172.17.0.1
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1542:    - DB_PORT=5432
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1543:    - DB_NAME=msjarvisgis
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1544:    - DB_USER=msjarvis
./docker-compose.yml.bak.20260423_095331:1471:      DATABASE_URL: postgresql://msjarvis:${DB_PASSWORD}@msjarvis-db:5432/msjarvis
./docker-compose.yml.bak.20260430-115408:13:    - DATABASE_URL=postgresql://postgres:pgtemp123@msjarvis-db:5432/msjarvisgis
./docker-compose.yml.bak.20260430-115408:42:    - DATABASE_URL=postgresql://postgres:pgtemp123@msjarvis-db:5432/msjarvisgis
./docker-compose.yml.bak.20260430-115408:1249:    - DATABASE_URL=postgresql://postgres:pgtemp123@msjarvis-db:5432/msjarvisgis
./docker-compose.yml.corrupt.20260415-1601:77:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.corrupt.20260415-1601:78:      DB_PORT: '5432'
./docker-compose.yml.corrupt.20260415-1601:79:      DB_NAME: local_resources
./docker-compose.yml.corrupt.20260415-1601:80:      DB_USER: postgres
./docker-compose.yml.corrupt.20260415-1601:82:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./docker-compose.yml.backup_20260318_103245:22:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_103245:23:    - GISDB_PORT=5433
./docker-compose.yml.backup_20260318_103245:24:    - GISDB_NAME=gisdb
./docker-compose.yml.backup_20260318_103245:25:    - GISDB_USER=postgres
./docker-compose.yml.backup_20260318_103245:451:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_103245:452:    - GISDB_PORT=5433
./docker-compose.yml.backup_20260318_103245:453:    - GISDB_NAME=gisdb
./docker-compose.yml.backup_20260318_103245:454:    - GISDB_USER=postgres
./docker-compose.yml.backup_20260318_103245:776:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_103245:777:    - GISDB_PORT=5433
./docker-compose.yml.backup_20260318_103245:778:    - GISDB_NAME=gisdb
./docker-compose.yml.backup_20260318_103245:779:    - GISDB_USER=postgres
./docker-compose.yml.backup_20260318_103245:1048:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_103245:1049:    - GISDB_PORT=5433
./docker-compose.yml.backup_20260318_103245:1050:    - GISDB_NAME=gisdb
./docker-compose.yml.backup_20260318_103245:1051:    - GISDB_USER=postgres
./docker-compose.yml.backup_20260318_103245:1068:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_103245:1069:    - GISDB_PORT=5433
./docker-compose.yml.backup_20260318_103245:1070:    - GISDB_NAME=gisdb
./docker-compose.yml.backup_20260318_103245:1071:    - GISDB_USER=postgres
./docker-compose.yml.bak.20260414-211038:88:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.bak.20260414-211038:89:      DB_PORT: '5432'
./docker-compose.yml.bak.20260414-211038:90:      DB_NAME: local_resources
./docker-compose.yml.bak.20260414-211038:91:      DB_USER: postgres
./docker-compose.yml.bak.20260414-211038:93:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./docker-compose.yml.pre-hilbert-fix-1768013541:134:      CHROMADB_HOST: chroma
./docker-compose.yml.pre-hilbert-fix-1768013541:135:      CHROMADB_PORT: 8010
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:1471:      DATABASE_URL: postgresql://msjarvis:${DB_PASSWORD}@msjarvis-db:5432/msjarvis
./.scratch/patch_longterm_memory.py:22:MEMORY_DSN  = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
./docker-compose.yml.hilbert-experiment.20260415-163850:96:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.hilbert-experiment.20260415-163850:97:      DB_PORT: '5432'
./docker-compose.yml.hilbert-experiment.20260415-163850:98:      DB_NAME: local_resources
./docker-compose.yml.hilbert-experiment.20260415-163850:99:      DB_USER: postgres
./docker-compose.yml.hilbert-experiment.20260415-163850:101:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./.venv/lib64/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:406:    DB_USER = "db.user"
./.venv/lib64/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:416:    DB_NAME = "db.name"
./.venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:174:DB_NAME: Final = "db.name"
./.venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:179:DB_NAMESPACE: Final = "db.namespace"
./.venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:181:Deprecated in favor of stable :py:const:`opentelemetry.semconv.attributes.db_attributes.DB_NAMESPACE`.
./.venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:282:DB_USER: Final = "db.user"
./.venv/lib64/python3.12/site-packages/opentelemetry/semconv/attributes/db_attributes.py:32:DB_NAMESPACE: Final = "db.namespace"
./.venv/lib64/python3.12/site-packages/sentry_sdk/consts.py:435:    DB_NAME = "db.name"
./.venv/lib64/python3.12/site-packages/sentry_sdk/consts.py:455:    DB_USER = "db.user"
./.venv/lib64/python3.12/site-packages/sentry_sdk/integrations/asyncpg.py:179:            span.set_data(SPANDATA.DB_NAME, database)
./.venv/lib64/python3.12/site-packages/sentry_sdk/integrations/asyncpg.py:180:            span.set_data(SPANDATA.DB_USER, user)
./.venv/lib64/python3.12/site-packages/sentry_sdk/integrations/asyncpg.py:206:        span.set_data(SPANDATA.DB_NAME, database)
./.venv/lib64/python3.12/site-packages/sentry_sdk/integrations/asyncpg.py:210:        span.set_data(SPANDATA.DB_USER, user)
./.venv/lib64/python3.12/site-packages/sentry_sdk/integrations/clickhouse_driver.py:170:    span.set_data(SPANDATA.DB_NAME, connection.database)
./.venv/lib64/python3.12/site-packages/sentry_sdk/integrations/clickhouse_driver.py:171:    span.set_data(SPANDATA.DB_USER, connection.user)
./.venv/lib64/python3.12/site-packages/sentry_sdk/integrations/django/__init__.py:763:        span.set_data(SPANDATA.DB_NAME, db_name)
./.venv/lib64/python3.12/site-packages/sentry_sdk/integrations/pymongo.py:94:        data[SPANDATA.DB_NAME] = db_name
./.venv/lib64/python3.12/site-packages/sentry_sdk/integrations/redis/modules/queries.py:50:        span.set_data(SPANDATA.DB_NAME, str(db))
./.venv/lib64/python3.12/site-packages/sentry_sdk/integrations/sqlalchemy.py:145:        span.set_data(SPANDATA.DB_NAME, db_name)
./.venv/lib64/python3.12/site-packages/mysql/connector/opentelemetry/instrumentation.py:220:            SpanAttributes.DB_USER: cnx._user,
./.venv/lib64/python3.12/site-packages/mysql/connector/opentelemetry/instrumentation.py:252:            SpanAttributes.DB_USER: connection._user,
./.venv/lib64/python3.12/site-packages/mysql/connector/errorcode.py:140:ER_WRONG_DB_NAME = 1102
./.venv/lib/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:406:    DB_USER = "db.user"
./.venv/lib/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:416:    DB_NAME = "db.name"
./.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:174:DB_NAME: Final = "db.name"
./.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:179:DB_NAMESPACE: Final = "db.namespace"
./.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:181:Deprecated in favor of stable :py:const:`opentelemetry.semconv.attributes.db_attributes.DB_NAMESPACE`.
./.venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:282:DB_USER: Final = "db.user"
./.venv/lib/python3.12/site-packages/opentelemetry/semconv/attributes/db_attributes.py:32:DB_NAMESPACE: Final = "db.namespace"
./.venv/lib/python3.12/site-packages/sentry_sdk/consts.py:435:    DB_NAME = "db.name"
./.venv/lib/python3.12/site-packages/sentry_sdk/consts.py:455:    DB_USER = "db.user"
./.venv/lib/python3.12/site-packages/sentry_sdk/integrations/asyncpg.py:179:            span.set_data(SPANDATA.DB_NAME, database)
./.venv/lib/python3.12/site-packages/sentry_sdk/integrations/asyncpg.py:180:            span.set_data(SPANDATA.DB_USER, user)
./.venv/lib/python3.12/site-packages/sentry_sdk/integrations/asyncpg.py:206:        span.set_data(SPANDATA.DB_NAME, database)
./.venv/lib/python3.12/site-packages/sentry_sdk/integrations/asyncpg.py:210:        span.set_data(SPANDATA.DB_USER, user)
./.venv/lib/python3.12/site-packages/sentry_sdk/integrations/clickhouse_driver.py:170:    span.set_data(SPANDATA.DB_NAME, connection.database)
./.venv/lib/python3.12/site-packages/sentry_sdk/integrations/clickhouse_driver.py:171:    span.set_data(SPANDATA.DB_USER, connection.user)
./.venv/lib/python3.12/site-packages/sentry_sdk/integrations/django/__init__.py:763:        span.set_data(SPANDATA.DB_NAME, db_name)
./.venv/lib/python3.12/site-packages/sentry_sdk/integrations/pymongo.py:94:        data[SPANDATA.DB_NAME] = db_name
./.venv/lib/python3.12/site-packages/sentry_sdk/integrations/redis/modules/queries.py:50:        span.set_data(SPANDATA.DB_NAME, str(db))
./.venv/lib/python3.12/site-packages/sentry_sdk/integrations/sqlalchemy.py:145:        span.set_data(SPANDATA.DB_NAME, db_name)
./.venv/lib/python3.12/site-packages/mysql/connector/opentelemetry/instrumentation.py:220:            SpanAttributes.DB_USER: cnx._user,
./.venv/lib/python3.12/site-packages/mysql/connector/opentelemetry/instrumentation.py:252:            SpanAttributes.DB_USER: connection._user,
./.venv/lib/python3.12/site-packages/mysql/connector/errorcode.py:140:ER_WRONG_DB_NAME = 1102
./services/restored_documents.json.bak-msallis:3382:      "content": "ies\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118\npip install transformers sentence-transformers\npip install ollama\n\nWeb framework and API\npip install fastapi uvicorn flask\n\nDatabase and storage\npip install redis chromadb\n\nUtilities and processing\npip install psutil pyyaml python-dotenv\npip install asyncio aiofiles\npip install requests numpy pandas\n\ntext\n\n#### Step 3: Configure Services\nSet up environment variables\ncat > .env << 'ENVEOF'\nOLLAMA_URL=http://localhost:11434\nREDIS_URL=redis://localhost:6379\nPOSTGRES_URL=postgresql://user:password@localhost:5432/ms_jarvis\nJARVIS_PORT=8010\nVECTOR_DB_PORT=8001\nENVEOF\n\nMake scripts executable\nchmod +x *.py\n\nSet up logging directory\nmkdir -p logs\nmkdir -p data/vector_db\nmkdir -p backups\n\ntext\n\n#### Step 4: Database Setup\nStart Redis (should already be running)\nsudo systemctl status redis-server\n\nCreate PostgreSQL database\nsudo -u postgres createdb ms_jarvis\nsudo -u postgres psql -c \"CREATE USER jarvis WITH PASSWORD 'your_password_here';\"\nsudo -u postgres psql -c \"GRANT ALL PRIVILEGES ON DATABASE ms_jarvis TO jarvis;\"\n\ntext\n\n#### Step 5: Start Core Services (In Order)\nTerminal 1: Start AI Server (core brain)\nsource venv/bin/activate\npython ai_server.py\n\nTerminal 2: Start Service Factory\nsource venv/bin/activate\npython ms_jarvis_service_factory.py\n\nTerminal 3: Start Brain Orchestrator\nsource venv/bin/activate\npython dynamic_app.py\n\nTerminal 4: Start Service Discovery\nsource venv/bin/activate",
./services/restored_documents.json.bak-msallis:13470:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://${USERNAME}@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://username@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://$(whoami)@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
./services/restored_documents.json.bak-msallis:13478:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
./services/restored_documents.json.bak-msallis:37038:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://${USERNAME}@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://username@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://$(whoami)@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
./services/restored_documents.json.bak-msallis:37046:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
./services/restored_documents.json.bak-msallis:48382:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://${USERNAME}@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://username@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://$(whoami)@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
./services/restored_documents.json.bak-msallis:48390:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
./services/restored_documents.json.bak-msallis:58142:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://${USERNAME}@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://username@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://$(whoami)@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
./services/restored_documents.json.bak-msallis:58150:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
./services/restored_documents.json.bak-msallis:63734:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://${USERNAME}@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://username@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://$(whoami)@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
./services/restored_documents.json.bak-msallis:63742:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
./services/restored_documents.json.bak-msallis:78374:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://${USERNAME}@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://username@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://$(whoami)@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
./services/restored_documents.json.bak-msallis:78382:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
./services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:406:    DB_USER = "db.user"
./services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:416:    DB_NAME = "db.name"
./services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:174:DB_NAME: Final = "db.name"
./services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:179:DB_NAMESPACE: Final = "db.namespace"
./services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:181:Deprecated in favor of stable :py:const:`opentelemetry.semconv.attributes.db_attributes.DB_NAMESPACE`.
./services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:282:DB_USER: Final = "db.user"
./services/chroma_inspect_venv/lib64/python3.12/site-packages/opentelemetry/semconv/attributes/db_attributes.py:32:DB_NAMESPACE: Final = "db.namespace"
./services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:406:    DB_USER = "db.user"
./services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:416:    DB_NAME = "db.name"
./services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:174:DB_NAME: Final = "db.name"
./services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:179:DB_NAMESPACE: Final = "db.namespace"
./services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:181:Deprecated in favor of stable :py:const:`opentelemetry.semconv.attributes.db_attributes.DB_NAMESPACE`.
./services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:282:DB_USER: Final = "db.user"
./services/chroma_inspect_venv/lib/python3.12/site-packages/opentelemetry/semconv/attributes/db_attributes.py:32:DB_NAMESPACE: Final = "db.namespace"
./services/gbim_verification_loop.py:12:DATABASE_URL    = os.environ.get("DATABASE_URL",     "postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
./services/gbim_verification_loop.py:93:    log.info(f"  DB:     {DATABASE_URL}")
./services/gbim_verification_loop.py:99:            pool = await asyncpg.create_pool(DATABASE_URL, min_size=1, max_size=3)
./services/docker-compose.yml.backup-corrupted-1763229905:134:      CHROMADB_HOST: chroma
./services/docker-compose.yml.backup-corrupted-1763229905:135:      CHROMADB_PORT: 8010
./services/jarvis_rag_search/retrieval_tuning.py:28:    "GBIM_DATABASE_URL",
./services/docker-compose.yml.backup-1763229864:134:      CHROMADB_HOST: chroma
./services/docker-compose.yml.backup-1763229864:135:      CHROMADB_PORT: 8010
./services/jarvis_decay_escalation_consumer.py:33:DB_HOST = os.getenv("MSJARVISGIS_HOST", "localhost")
./services/jarvis_decay_escalation_consumer.py:34:DB_PORT = int(os.getenv("MSJARVISGIS_PORT", "5432"))
./services/jarvis_decay_escalation_consumer.py:35:DB_NAME = "msjarvisgis"
./services/jarvis_decay_escalation_consumer.py:36:DB_USER = os.getenv("POSTGRES_USER", "postgres")
./services/jarvis_decay_escalation_consumer.py:42:        host=DB_HOST, port=DB_PORT,
./services/jarvis_decay_escalation_consumer.py:43:        database=DB_NAME, user=DB_USER, password=DB_PASS,
./services/jarvis_decay_escalation_consumer.py:107:        f"db={DB_HOST}:{DB_PORT}/{DB_NAME}"
./services/restored_documents.json:3382:      "content": "ies\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118\npip install transformers sentence-transformers\npip install ollama\n\nWeb framework and API\npip install fastapi uvicorn flask\n\nDatabase and storage\npip install redis chromadb\n\nUtilities and processing\npip install psutil pyyaml python-dotenv\npip install asyncio aiofiles\npip install requests numpy pandas\n\ntext\n\n#### Step 3: Configure Services\nSet up environment variables\ncat > .env << 'ENVEOF'\nOLLAMA_URL=http://localhost:11434\nREDIS_URL=redis://localhost:6379\nPOSTGRES_URL=postgresql://user:password@localhost:5432/ms_jarvis\nJARVIS_PORT=8010\nVECTOR_DB_PORT=8001\nENVEOF\n\nMake scripts executable\nchmod +x *.py\n\nSet up logging directory\nmkdir -p logs\nmkdir -p data/vector_db\nmkdir -p backups\n\ntext\n\n#### Step 4: Database Setup\nStart Redis (should already be running)\nsudo systemctl status redis-server\n\nCreate PostgreSQL database\nsudo -u postgres createdb ms_jarvis\nsudo -u postgres psql -c \"CREATE USER jarvis WITH PASSWORD 'your_password_here';\"\nsudo -u postgres psql -c \"GRANT ALL PRIVILEGES ON DATABASE ms_jarvis TO jarvis;\"\n\ntext\n\n#### Step 5: Start Core Services (In Order)\nTerminal 1: Start AI Server (core brain)\nsource venv/bin/activate\npython ai_server.py\n\nTerminal 2: Start Service Factory\nsource venv/bin/activate\npython ms_jarvis_service_factory.py\n\nTerminal 3: Start Brain Orchestrator\nsource venv/bin/activate\npython dynamic_app.py\n\nTerminal 4: Start Service Discovery\nsource venv/bin/activate",
./services/restored_documents.json:13470:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://${USERNAME}@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://username@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://$(whoami)@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
./services/restored_documents.json:13478:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
./services/restored_documents.json:37038:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://${USERNAME}@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://username@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://$(whoami)@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
./services/restored_documents.json:37046:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
./services/restored_documents.json:48382:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://${USERNAME}@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://username@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://$(whoami)@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
./services/restored_documents.json:48390:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
./services/restored_documents.json:58142:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://${USERNAME}@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://username@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://$(whoami)@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
./services/restored_documents.json:58150:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
./services/restored_documents.json:63734:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://${USERNAME}@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://username@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://$(whoami)@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
./services/restored_documents.json:63742:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
./services/restored_documents.json:78374:      "content": "r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true\n```\n\nAdditionally, you can use environment variables to set configuration options. Command line arguments will precede these.\n\n```bash\n$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js\n```\n\n```bash\n$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env\n```\n\n### Variable Expansion\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use variable expansion.\n\nReference and expand variables already on your machine for use in your .env file.\n\n```ini\n# .env\nUSERNAME=\"username\"\nDATABASE_URL=\"postgres://${USERNAME}@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (2) from .env\nDATABASE_URL postgres://username@localhost/my_database\n```\n\n### Command Substitution\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to use command substitution.\n\nAdd the output of a command to one of your variables in your .env file.\n\n```ini\n# .env\nDATABASE_URL=\"postgres://$(whoami)@localhost/my_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync betw",
./services/restored_documents.json:78382:      "content": "_database\"\n```\n```js\n// index.js\nconsole.log('DATABASE_URL', process.env.DATABASE_URL)\n```\n```sh\n$ dotenvx run --debug -- node index.js\n[dotenvx@0.14.1] injecting env (1) from .env\nDATABASE_URL postgres://yourusername@localhost/my_database\n```\n\n### Syncing\n\nYou need to keep `.env` files in sync between machines, environments, or team members? Use [dotenvx](https://github.com/dotenvx/dotenvx) to encrypt your `.env` files and safely include them in source control. This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.\n\n### Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx) to generate `.env.ci`, `.env.production` files, and more.\n\n### Deploying\n\nYou need to deploy your secrets in a cloud-agnostic manner? Use [dotenvx](https://github.com/dotenvx/dotenvx) to generate a private decryption key that is set on your production server.\n\n## \ud83c\udf34 Manage Multiple Environments\n\nUse [dotenvx](https://github.com/dotenvx/dotenvx)\n\nRun any environment locally. Create a `.env.ENVIRONMENT` file and use `--env-file` to load it. It's straightforward, yet flexible.\n\n```bash\n$ echo \"HELLO=production\" > .env.production\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx run --env-file=.env.production -- node index.js\nHello production\n> ^^\n```\n\nor with multiple .env files\n\n```bash\n$ echo \"HELLO=local\" > .env.local\n$ echo \"HELLO=World\" > .env\n$ echo \"console.log('Hello ' + process.env.HELLO)\" > index.js\n\n$ dotenvx ",
./services/auth_router.py:241:    _dsn = _os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL")
./services/auth_router.py:339:        _dsn = _os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL")
./services/auth_router.py:538:    pg_dsn = _os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL")
./services/auth_router.py:582:    _dsn = (_os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL", ""))
./services/auth_router.py:687:    pg_dsn = _os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL")
./services/ms_mountainshares_indexer.py:22:        "DATABASE_URL",
./services/ms_jarvis_memory.py:20:MEMORY_DSN  = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
./services/main_brain.py:990:                _dsn = _os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL")
./services/ingest_postgis_to_chroma.py:17:    "host": os.getenv("GIS_DB_HOST", "localhost"),
./services/ingest_postgis_to_chroma.py:18:    "port": int(os.getenv("GIS_DB_PORT", "5435")),
./services/ingest_postgis_to_chroma.py:19:    "dbname": os.getenv("GIS_DB_NAME", "msjarvisgis"),
./services/ingest_postgis_to_chroma.py:20:    "user": os.getenv("GIS_DB_USER", "postgres"),
./services/lm_synthesizer.py:18:GIS_DATABASE_URL = os.getenv("GIS_DATABASE_URL", "")
./services/lm_synthesizer.py:28:    if not GIS_DATABASE_URL:
./services/lm_synthesizer.py:32:        conn = psycopg2.connect(GIS_DATABASE_URL, connect_timeout=2)
./services/gis_rag_service.py:33:    "GIS_DATABASE_URL",
./services/ms_mountainshares_indexer.py.bak-msallis:22:        "DATABASE_URL",
./services/main_brain.py.bak_persona_1779997582:966:                _dsn = _os.environ.get("POSTGRES_DSN") or _os.environ.get("DATABASE_URL")
./services/ms_jarvis_memory.py.bak-msallis:18:MEMORY_DSN  = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis")
./docker-compose.yml.safe-1768040125:134:      CHROMADB_HOST: chroma
./docker-compose.yml.safe-1768040125:135:      CHROMADB_PORT: 8010
./docker-compose.yml.bak.20260501-200948:13:    - DATABASE_URL=postgresql://postgres:pgtemp123@msjarvis-db:5432/msjarvisgis
./docker-compose.yml.bak.20260501-200948:43:    - DATABASE_URL=postgresql://postgres:pgtemp123@msjarvis-db:5432/msjarvisgis
./docker-compose.yml.bak.20260501-200948:1270:    - DATABASE_URL=postgresql://postgres:pgtemp123@msjarvis-db:5432/msjarvisgis
./docker-compose.yml.bak.20260501-200948:1373:    - DATABASE_URL=postgresql://postgres:pgtemp123@msjarvis-db:5432/msjarvisgis
./docker-compose.yml.bak.20260501-200948:1545:      DATABASE_URL: postgresql://postgres:postgres@msjarvisgis-recovery:5432/msjarvisgis
./docker-compose.yml.bak.20260416-141203:1223:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.bak.20260416-141203:1224:    - GISDB_PORT=5432
./docker-compose.yml.bak.20260416-141203:1225:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416-141203:1226:    - GISDB_USER=msjarvis
./docker-compose.yml.bak.20260416-141203:1252:    - DB_HOST=172.17.0.1
./docker-compose.yml.bak.20260416-141203:1253:    - DB_PORT=5432
./docker-compose.yml.bak.20260416-141203:1254:    - DB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416-141203:1255:    - DB_USER=msjarvis
./docker-compose.yml.bak.20260518-215027:1238:      - GIS_DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
./.env.example:36:DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./.env.example:38:DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./docker-compose.yml.bak.20260416_144451:1229:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.bak.20260416_144451:1230:    - GISDB_PORT=5432
./docker-compose.yml.bak.20260416_144451:1231:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416_144451:1232:    - GISDB_USER=msjarvis
./docker-compose.yml.bak.20260416_144451:1258:    - DB_HOST=172.17.0.1
./docker-compose.yml.bak.20260416_144451:1259:    - DB_PORT=5432
./docker-compose.yml.bak.20260416_144451:1260:    - DB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416_144451:1261:    - DB_USER=msjarvis
./crypto-venv/lib64/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:406:    DB_USER = "db.user"
./crypto-venv/lib64/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:416:    DB_NAME = "db.name"
./crypto-venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:174:DB_NAME: Final = "db.name"
./crypto-venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:179:DB_NAMESPACE: Final = "db.namespace"
./crypto-venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:181:Deprecated in favor of stable :py:const:`opentelemetry.semconv.attributes.db_attributes.DB_NAMESPACE`.
./crypto-venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:282:DB_USER: Final = "db.user"
./crypto-venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/oracle_attributes.py:35:ORACLE_DB_NAME: Final = "oracle.db.name"
./crypto-venv/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/oracle_attributes.py:38:Note: This attribute SHOULD be set to the value of the parameter `DB_NAME` exposed in `v$parameter`.
./crypto-venv/lib64/python3.12/site-packages/opentelemetry/semconv/attributes/db_attributes.py:32:DB_NAMESPACE: Final = "db.namespace"
./crypto-venv/lib64/python3.12/site-packages/redis/observability/attributes.py:23:DB_NAMESPACE = "db.namespace"
./crypto-venv/lib64/python3.12/site-packages/redis/observability/attributes.py:126:            attrs[DB_NAMESPACE] = str(db_namespace)
./crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:406:    DB_USER = "db.user"
./crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:416:    DB_NAME = "db.name"
./crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:174:DB_NAME: Final = "db.name"
./crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:179:DB_NAMESPACE: Final = "db.namespace"
./crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:181:Deprecated in favor of stable :py:const:`opentelemetry.semconv.attributes.db_attributes.DB_NAMESPACE`.
./crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:282:DB_USER: Final = "db.user"
./crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/oracle_attributes.py:35:ORACLE_DB_NAME: Final = "oracle.db.name"
./crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/oracle_attributes.py:38:Note: This attribute SHOULD be set to the value of the parameter `DB_NAME` exposed in `v$parameter`.
./crypto-venv/lib/python3.12/site-packages/opentelemetry/semconv/attributes/db_attributes.py:32:DB_NAMESPACE: Final = "db.namespace"
./crypto-venv/lib/python3.12/site-packages/redis/observability/attributes.py:23:DB_NAMESPACE = "db.namespace"
./crypto-venv/lib/python3.12/site-packages/redis/observability/attributes.py:126:            attrs[DB_NAMESPACE] = str(db_namespace)
./docker-compose.yml.bak.20260414-211257:88:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.bak.20260414-211257:89:      DB_PORT: '5432'
./docker-compose.yml.bak.20260414-211257:90:      DB_NAME: local_resources
./docker-compose.yml.bak.20260414-211257:91:      DB_USER: postgres
./docker-compose.yml.bak.20260414-211257:93:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./docker-compose.yml.bak.20260416-141709:1229:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.bak.20260416-141709:1230:    - GISDB_PORT=5432
./docker-compose.yml.bak.20260416-141709:1231:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416-141709:1232:    - GISDB_USER=msjarvis
./docker-compose.yml.bak.20260416-141709:1258:    - DB_HOST=172.17.0.1
./docker-compose.yml.bak.20260416-141709:1259:    - DB_PORT=5432
./docker-compose.yml.bak.20260416-141709:1260:    - DB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416-141709:1261:    - DB_USER=msjarvis
./docker-compose.yml.bak-20260417-144354:1233:  # DISABLED (path missing):     - GISDB_HOST=172.18.0.1
./docker-compose.yml.bak-20260417-144354:1234:  # DISABLED (path missing):     - GISDB_PORT=5432
./docker-compose.yml.bak-20260417-144354:1235:  # DISABLED (path missing):     - GISDB_NAME=msjarvisgis
./docker-compose.yml.bak-20260417-144354:1236:  # DISABLED (path missing):     - GISDB_USER=msjarvis
./docker-compose.yml.bak-20260417-144354:1262:  # DISABLED (path missing):     - DB_HOST=172.17.0.1
./docker-compose.yml.bak-20260417-144354:1263:  # DISABLED (path missing):     - DB_PORT=5432
./docker-compose.yml.bak-20260417-144354:1264:  # DISABLED (path missing):     - DB_NAME=msjarvisgis
./docker-compose.yml.bak-20260417-144354:1265:  # DISABLED (path missing):     - DB_USER=msjarvis
./docker-compose.yml.pre-hilbert-portfix.20260415-162529:98:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.pre-hilbert-portfix.20260415-162529:99:      DB_PORT: '5432'
./docker-compose.yml.pre-hilbert-portfix.20260415-162529:100:      DB_NAME: local_resources
./docker-compose.yml.pre-hilbert-portfix.20260415-162529:101:      DB_USER: postgres
./docker-compose.yml.pre-hilbert-portfix.20260415-162529:103:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./docker-compose.yml.bak.20260414-210743:88:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.bak.20260414-210743:89:      DB_PORT: '5432'
./docker-compose.yml.bak.20260414-210743:90:      DB_NAME: local_resources
./docker-compose.yml.bak.20260414-210743:91:      DB_USER: postgres
./docker-compose.yml.bak.20260414-210743:93:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./ms-allis-frontend/node_modules/pg-pool/README.md:59:const params = url.parse(process.env.DATABASE_URL)
./docker-compose.yml.bak.20260414-210516:88:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.bak.20260414-210516:89:      DB_PORT: '5432'
./docker-compose.yml.bak.20260414-210516:90:      DB_NAME: local_resources
./docker-compose.yml.bak.20260414-210516:91:      DB_USER: postgres
./docker-compose.yml.bak.20260414-210516:93:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./docker-compose.yml.bak_hilbert_cmdfix_20260415-142151:90:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.bak_hilbert_cmdfix_20260415-142151:91:      DB_PORT: '5432'
./docker-compose.yml.bak_hilbert_cmdfix_20260415-142151:92:      DB_NAME: local_resources
./docker-compose.yml.bak_hilbert_cmdfix_20260415-142151:93:      DB_USER: postgres
./docker-compose.yml.bak_hilbert_cmdfix_20260415-142151:95:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./tiger_downloads/load_resume.sh:6:DB_USER=postgres
./tiger_downloads/load_resume.sh:7:DB_NAME=msjarvisgis
./tiger_downloads/load_resume.sh:44:      | docker exec -i "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" \
./tiger_downloads/load_resume.sh:49:      | docker exec -i "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" \
./tiger_downloads/load_resume.sh:53:  docker exec "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" -c \
./tiger_downloads/load_resume.sh:58:  docker exec "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" -c \
./tiger_downloads/load_resume.sh:213:docker exec "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" -c \
./tiger_downloads/load_all_wv_layers.sh:4:export DB_USER=postgres
./tiger_downloads/load_all_wv_layers.sh:5:export DB_NAME=msjarvisgis
./tiger_downloads/load_all_wv_layers.sh:9:DB_USER=postgres
./tiger_downloads/load_all_wv_layers.sh:10:DB_NAME=msjarvisgis
./tiger_downloads/load_all_wv_layers.sh:47:      | docker exec -i "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" \
./tiger_downloads/load_all_wv_layers.sh:52:      | docker exec -i "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" \
./tiger_downloads/load_all_wv_layers.sh:56:  docker exec "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" -c \
./tiger_downloads/load_all_wv_layers.sh:61:  docker exec "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" -c \
./tiger_downloads/load_all_wv_layers.sh:242:docker exec "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" -c \
./tiger_downloads/load_remaining.sh:153:docker exec "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" -c \
./tiger_downloads/load_resume2.sh:4:export DB_USER=postgres
./tiger_downloads/load_resume2.sh:5:export DB_NAME=msjarvisgis
./tiger_downloads/load_resume2.sh:20:  docker exec "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" -c \
./tiger_downloads/load_resume2.sh:23:    | docker exec -i "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" \
./tiger_downloads/load_resume2.sh:26:    | docker exec -i "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" \
./tiger_downloads/load_resume2.sh:28:  docker exec "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" -c \
./tiger_downloads/load_resume2.sh:31:  docker exec "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" -c \
./tiger_downloads/load_resume2.sh:42:docker exec "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" -c \
./tiger_downloads/load_resume2.sh:199:docker exec "$DB_CONTAINER" psql -U "$DB_USER" -d "$DB_NAME" -c \
./docker-compose.yml.bak.20260416-141224:1223:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.bak.20260416-141224:1224:    - GISDB_PORT=5432
./docker-compose.yml.bak.20260416-141224:1225:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416-141224:1226:    - GISDB_USER=msjarvis
./docker-compose.yml.bak.20260416-141224:1252:    - DB_HOST=172.17.0.1
./docker-compose.yml.bak.20260416-141224:1253:    - DB_PORT=5432
./docker-compose.yml.bak.20260416-141224:1254:    - DB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416-141224:1255:    - DB_USER=msjarvis
./docker-compose.yml.bak.20260414-210440:87:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.bak.20260414-210440:88:      DB_PORT: '5432'
./docker-compose.yml.bak.20260414-210440:89:      DB_NAME: local_resources
./docker-compose.yml.bak.20260414-210440:90:      DB_USER: postgres
./docker-compose.yml.bak.20260414-210440:92:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./docker-compose.yml.backup_20260318_110053:22:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_110053:23:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_110053:24:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110053:25:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_110053:451:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_110053:452:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_110053:453:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110053:454:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_110053:776:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_110053:777:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_110053:778:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110053:779:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_110053:1048:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_110053:1049:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_110053:1050:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110053:1051:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_110053:1068:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_110053:1069:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_110053:1070:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110053:1071:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_110053:1194:      - DB_HOST=172.17.0.1
./docker-compose.yml.backup_20260318_110053:1195:      - DB_PORT=5432
./docker-compose.yml.backup_20260318_110053:1196:      - DB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110053:1197:      - DB_USER=msjarvis
./docker-compose.yml.bak.20260517-163017:1234:      - GIS_DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
./docker-compose.restored.yml.safe-1768040125:132:      CHROMADB_HOST: chroma
./docker-compose.restored.yml.safe-1768040125:133:      CHROMADB_PORT: 8010
./docker-compose.yml.bak.20260522_204447:1244:      - GIS_DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
./docker-compose.yml.bak.20260416-141425:1223:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.bak.20260416-141425:1224:    - GISDB_PORT=5432
./docker-compose.yml.bak.20260416-141425:1225:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416-141425:1226:    - GISDB_USER=msjarvis
./docker-compose.yml.bak.20260416-141425:1252:    - DB_HOST=172.17.0.1
./docker-compose.yml.bak.20260416-141425:1253:    - DB_PORT=5432
./docker-compose.yml.bak.20260416-141425:1254:    - DB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416-141425:1255:    - DB_USER=msjarvis
./docker-compose.yml.bak.20260416_144808:1229:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.bak.20260416_144808:1230:    - GISDB_PORT=5432
./docker-compose.yml.bak.20260416_144808:1231:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416_144808:1232:    - GISDB_USER=msjarvis
./docker-compose.yml.bak.20260416_144808:1258:    - DB_HOST=172.17.0.1
./docker-compose.yml.bak.20260416_144808:1259:    - DB_PORT=5432
./docker-compose.yml.bak.20260416_144808:1260:    - DB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416_144808:1261:    - DB_USER=msjarvis
./docker-compose.yml.bak.20260416-141603:1230:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.bak.20260416-141603:1231:    - GISDB_PORT=5432
./docker-compose.yml.bak.20260416-141603:1232:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416-141603:1233:    - GISDB_USER=msjarvis
./docker-compose.yml.bak.20260416-141603:1259:    - DB_HOST=172.17.0.1
./docker-compose.yml.bak.20260416-141603:1260:    - DB_PORT=5432
./docker-compose.yml.bak.20260416-141603:1261:    - DB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416-141603:1262:    - DB_USER=msjarvis
./docker-compose.yml.bak.20260522T193400Z:1244:      - GIS_DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
./docker-compose.yml.bak.20260430-202630:13:    - DATABASE_URL=postgresql://postgres:pgtemp123@msjarvis-db:5432/msjarvisgis
./docker-compose.yml.bak.20260430-202630:43:    - DATABASE_URL=postgresql://postgres:pgtemp123@msjarvis-db:5432/msjarvisgis
./docker-compose.yml.bak.20260430-202630:1268:    - DATABASE_URL=postgresql://postgres:pgtemp123@msjarvis-db:5432/msjarvisgis
./docker-compose.yml.pre-hilbert-noports.20260415-162654:98:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.pre-hilbert-noports.20260415-162654:99:      DB_PORT: '5432'
./docker-compose.yml.pre-hilbert-noports.20260415-162654:100:      DB_NAME: local_resources
./docker-compose.yml.pre-hilbert-noports.20260415-162654:101:      DB_USER: postgres
./docker-compose.yml.pre-hilbert-noports.20260415-162654:103:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./docker-compose.yml.backup_20260406_newservices:1232:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260406_newservices:1233:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260406_newservices:1234:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260406_newservices:1235:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260406_newservices:1261:    - DB_HOST=172.17.0.1
./docker-compose.yml.backup_20260406_newservices:1262:    - DB_PORT=5432
./docker-compose.yml.backup_20260406_newservices:1263:    - DB_NAME=msjarvisgis
./docker-compose.yml.backup_20260406_newservices:1264:    - DB_USER=msjarvis
./gis_rag_service.py:33:    "GIS_DATABASE_URL",
./docker-compose.restored.yml.pre-hilbert-fix-1768013541:134:      CHROMADB_HOST: chroma
./docker-compose.restored.yml.pre-hilbert-fix-1768013541:135:      CHROMADB_PORT: 8010
./docker-compose.yml.pre-hilbert-image-20260415-161150:92:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.pre-hilbert-image-20260415-161150:93:      DB_PORT: '5432'
./docker-compose.yml.pre-hilbert-image-20260415-161150:94:      DB_NAME: local_resources
./docker-compose.yml.pre-hilbert-image-20260415-161150:95:      DB_USER: postgres
./docker-compose.yml.pre-hilbert-image-20260415-161150:97:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./.venv-chroma/lib64/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:406:    DB_USER = "db.user"
./.venv-chroma/lib64/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:416:    DB_NAME = "db.name"
./.venv-chroma/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:174:DB_NAME: Final = "db.name"
./.venv-chroma/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:179:DB_NAMESPACE: Final = "db.namespace"
./.venv-chroma/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:181:Deprecated in favor of stable :py:const:`opentelemetry.semconv.attributes.db_attributes.DB_NAMESPACE`.
./.venv-chroma/lib64/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:282:DB_USER: Final = "db.user"
./.venv-chroma/lib64/python3.12/site-packages/opentelemetry/semconv/attributes/db_attributes.py:32:DB_NAMESPACE: Final = "db.namespace"
./.venv-chroma/lib/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:406:    DB_USER = "db.user"
./.venv-chroma/lib/python3.12/site-packages/opentelemetry/semconv/trace/__init__.py:416:    DB_NAME = "db.name"
./.venv-chroma/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:174:DB_NAME: Final = "db.name"
./.venv-chroma/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:179:DB_NAMESPACE: Final = "db.namespace"
./.venv-chroma/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:181:Deprecated in favor of stable :py:const:`opentelemetry.semconv.attributes.db_attributes.DB_NAMESPACE`.
./.venv-chroma/lib/python3.12/site-packages/opentelemetry/semconv/_incubating/attributes/db_attributes.py:282:DB_USER: Final = "db.user"
./.venv-chroma/lib/python3.12/site-packages/opentelemetry/semconv/attributes/db_attributes.py:32:DB_NAMESPACE: Final = "db.namespace"
./scripts/load_one_attrs.sh:4:DB_HOST=${DEST_HOST:-localhost}
./scripts/load_one_attrs.sh:5:DB_PORT=${DEST_PORT:-5432}
./scripts/load_one_attrs.sh:6:DB_USER=${DEST_USER:-postgres}
./scripts/load_one_attrs.sh:7:DB_NAME=${DEST_DB:-msjarvisgis}
./scripts/load_one_attrs.sh:12:psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$DB_NAME" <<EOF
./docker-compose.yml.backup_20260323_205752:22:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260323_205752:23:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260323_205752:24:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260323_205752:25:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260323_205752:473:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260323_205752:474:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260323_205752:475:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260323_205752:476:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260323_205752:798:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260323_205752:799:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260323_205752:800:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260323_205752:801:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260323_205752:1090:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260323_205752:1091:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260323_205752:1092:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260323_205752:1093:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260323_205752:1254:    - DB_HOST=172.17.0.1
./docker-compose.yml.backup_20260323_205752:1255:    - DB_PORT=5432
./docker-compose.yml.backup_20260323_205752:1256:    - DB_NAME=msjarvisgis
./docker-compose.yml.backup_20260323_205752:1257:    - DB_USER=msjarvis
./docker-compose.yml.backup_20260318_102158:22:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_102158:23:    - GISDB_PORT=5433
./docker-compose.yml.backup_20260318_102158:24:    - GISDB_NAME=gisdb
./docker-compose.yml.backup_20260318_102158:25:    - GISDB_USER=postgres
./docker-compose.yml.backup_20260318_102158:451:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_102158:452:    - GISDB_PORT=5433
./docker-compose.yml.backup_20260318_102158:453:    - GISDB_NAME=gisdb
./docker-compose.yml.backup_20260318_102158:454:    - GISDB_USER=postgres
./docker-compose.yml.backup_20260318_102158:776:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_102158:777:    - GISDB_PORT=5433
./docker-compose.yml.backup_20260318_102158:778:    - GISDB_NAME=gisdb
./docker-compose.yml.backup_20260318_102158:779:    - GISDB_USER=postgres
./docker-compose.yml.backup_20260318_102158:1048:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_102158:1049:    - GISDB_PORT=5433
./docker-compose.yml.backup_20260318_102158:1050:    - GISDB_NAME=gisdb
./docker-compose.yml.backup_20260318_102158:1051:    - GISDB_USER=postgres
./docker-compose.yml.backup_20260318_102158:1068:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_102158:1069:    - GISDB_PORT=5433
./docker-compose.yml.backup_20260318_102158:1070:    - GISDB_NAME=gisdb
./docker-compose.yml.backup_20260318_102158:1071:    - GISDB_USER=postgres
./docker-compose.yml.bak.20260422_220748:1471:      DATABASE_URL: postgresql://msjarvis:${DB_PASSWORD}@msjarvis-db:5432/msjarvis
./docker-compose.yml.bak.20260416-141309:1223:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.bak.20260416-141309:1224:    - GISDB_PORT=5432
./docker-compose.yml.bak.20260416-141309:1225:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416-141309:1226:    - GISDB_USER=msjarvis
./docker-compose.yml.bak.20260416-141309:1252:    - DB_HOST=172.17.0.1
./docker-compose.yml.bak.20260416-141309:1253:    - DB_PORT=5432
./docker-compose.yml.bak.20260416-141309:1254:    - DB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416-141309:1255:    - DB_USER=msjarvis
./docker-compose.yml.bak_20260415-111118:88:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.bak_20260415-111118:89:      DB_PORT: '5432'
./docker-compose.yml.bak_20260415-111118:90:      DB_NAME: local_resources
./docker-compose.yml.bak_20260415-111118:91:      DB_USER: postgres
./docker-compose.yml.bak_20260415-111118:93:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./docker-compose.yml.backup_20260323_211407:22:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260323_211407:23:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260323_211407:24:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260323_211407:25:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260323_211407:473:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260323_211407:474:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260323_211407:475:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260323_211407:476:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260323_211407:798:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260323_211407:799:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260323_211407:800:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260323_211407:801:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260323_211407:1090:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260323_211407:1091:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260323_211407:1092:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260323_211407:1093:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260323_211407:1254:    - DB_HOST=172.17.0.1
./docker-compose.yml.backup_20260323_211407:1255:    - DB_PORT=5432
./docker-compose.yml.backup_20260323_211407:1256:    - DB_NAME=msjarvisgis
./docker-compose.yml.backup_20260323_211407:1257:    - DB_USER=msjarvis
./docker-compose.yml.bak.20260416-141316:1223:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.bak.20260416-141316:1224:    - GISDB_PORT=5432
./docker-compose.yml.bak.20260416-141316:1225:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416-141316:1226:    - GISDB_USER=msjarvis
./docker-compose.yml.bak.20260416-141316:1252:    - DB_HOST=172.17.0.1
./docker-compose.yml.bak.20260416-141316:1253:    - DB_PORT=5432
./docker-compose.yml.bak.20260416-141316:1254:    - DB_NAME=msjarvisgis
./docker-compose.yml.bak.20260416-141316:1255:    - DB_USER=msjarvis
./docker-compose.yml.bak_hilbert_depsfix_20260415-142323:96:      DB_HOST: jarvis-local-resources-db
./docker-compose.yml.bak_hilbert_depsfix_20260415-142323:97:      DB_PORT: '5432'
./docker-compose.yml.bak_hilbert_depsfix_20260415-142323:98:      DB_NAME: local_resources
./docker-compose.yml.bak_hilbert_depsfix_20260415-142323:99:      DB_USER: postgres
./docker-compose.yml.bak_hilbert_depsfix_20260415-142323:101:      DATABASE_URL: postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
./docker-compose.yml.backup_20260318_110927:22:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_110927:23:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_110927:24:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110927:25:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_110927:451:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_110927:452:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_110927:453:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110927:454:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_110927:776:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_110927:777:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_110927:778:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110927:779:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_110927:1067:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_110927:1068:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_110927:1069:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110927:1070:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_110927:1193:      - DB_HOST=172.17.0.1
./docker-compose.yml.backup_20260318_110927:1194:      - DB_PORT=5432
./docker-compose.yml.backup_20260318_110927:1195:      - DB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_110927:1196:      - DB_USER=msjarvis
./docker-compose.yml.pre_dsn_fix:1188:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.pre_dsn_fix:1189:    - GISDB_PORT=5432
./docker-compose.yml.pre_dsn_fix:1190:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.pre_dsn_fix:1191:    - GISDB_USER=msjarvis
./docker-compose.yml.pre_dsn_fix:1217:    - DB_HOST=172.17.0.1
./docker-compose.yml.pre_dsn_fix:1218:    - DB_PORT=5432
./docker-compose.yml.pre_dsn_fix:1219:    - DB_NAME=msjarvisgis
./docker-compose.yml.pre_dsn_fix:1220:    - DB_USER=msjarvis
./docker-compose.yml.backup_20260318_103829:22:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_103829:23:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_103829:24:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_103829:25:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_103829:451:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_103829:452:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_103829:453:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_103829:454:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_103829:776:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_103829:777:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_103829:778:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_103829:779:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_103829:1048:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_103829:1049:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_103829:1050:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_103829:1051:    - GISDB_USER=msjarvis
./docker-compose.yml.backup_20260318_103829:1068:    - GISDB_HOST=172.18.0.1
./docker-compose.yml.backup_20260318_103829:1069:    - GISDB_PORT=5432
./docker-compose.yml.backup_20260318_103829:1070:    - GISDB_NAME=msjarvisgis
./docker-compose.yml.backup_20260318_103829:1071:    - GISDB_USER=msjarvis
docker-compose.gbim.yml:14:      - gbim_data:/var/lib/postgresql/data
docker-compose.override.yml:15:      - POSTGRES_DSN=postgresql://postgres@jarvis-local-resources-db:5432/msjarvisgis
docker-compose.rag.yml:14:      - EPISODIC_DSN=dbname=postgres user=postgres password=postgres host=jarvis-local-resources-db
docker-compose.yml:513:      - GBIM_DSN=postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources
docker-compose.yml:1249:      - LOCAL_RESOURCES_DSN=postgresql://msjarvis:Nathaniel1@jarvis-gis-db:5432/msjarvisgis
docker-compose.yml:1262:      - POSTGRES_USER=postgres
docker-compose.yml:1263:      - POSTGRES_PASSWORD=postgres
docker-compose.yml:1267:      - msjarvis-rebuild_jarvis-local-resources-db-data:/var/lib/postgresql/data
docker-compose.yml:1283:      - GIS_DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
docker-compose.yml:2034:      - POSTGRES_DSN=postgresql://postgres@jarvis-local-resources-db:5432/msjarvisgis
./db/gbim_confidence_decay_schema.sql
./db/gbim_schema_patch.sql
./db/mountainshares_tokenomics_schema.sql
./docs/mysql_schema_quantum_ai.sql
./docs/mysql_schema_all.sql
./docs/mysql_schema_20260328.sql
./docs/mysql_schema_dump_20260402.sql
./docs/database/mysql_schema_dump_2026-03-24.sql
./docs/mysql_schema.sql
./docs/schema/mysql-schema-dump.sql
./00_provenance_migration.sql
./scripts/create_trail_schema.sql
.env:20:DB_DSN=postgresql://postgres:postgres@127.0.0.1:5435/msjarvisgis
.env:22:DB_URL=postgresql://postgres:postgres@127.0.0.1:5435/msjarvisgis
.env:32:GBIM_ROUTER_URL=http://jarvis-gbim-query-router:7205
.env:33:GBIM_URL=http://jarvis-gbim-query-router:7205
.env:34:GEODB_DSN=postgresql://postgres:postgres@127.0.0.1:5435/msjarvisgis
.env:63:LOCAL_RESOURCES_DSN=postgresql://msjarvis:MsJarvis2026Secure@jarvis-local-resources-db:5432/msjarvisgis
.env:75:MSJARVIS_GIS_URL=postgresql://msjarvis:MsJarvis2026Secure@jarvis-local-resources-db:5432/msjarvisgis
.env:113:POSTGRES_DB=msjarvisgis
.env.backup-20260505:22:DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.backup-20260505:23:DB_DSN=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.backup-20260505:24:DB_DSN=postgresql://postgres:postgres@msjarvisgis-recovery:5432/msjarvisgis
.env.backup-20260505:26:DB_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.backup-20260505:37:GBIM_ROUTER_URL=http://jarvis-gbim-query-router:7205
.env.backup-20260505:38:GBIM_URL=http://jarvis-gbim-query-router:7205
.env.backup-20260505:39:GEODB_DSN=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.backup-20260505:69:LOCAL_RESOURCES_DSN=postgresql://msjarvis:MsJarvis2026Secure@jarvis-local-resources-db:5432/msjarvisgis
.env.backup-20260505:70:LOCAL_RESOURCES_DSN=postgresql://msjarvis:Nathaniel1@jarvis-gis-db:5432/msjarvisgis
.env.backup-20260505:72:LOCAL_RESOURCES_DSN=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.backup-20260505:84:MSJARVIS_GIS_URL=postgresql://msjarvis:MsJarvis2026Secure@jarvis-local-resources-db:5432/msjarvisgis
.env.backup-20260505:85:MSJARVIS_GIS_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.backup-20260505:125:POSTGRES_DB=msjarvisgis
.env.backup-20260505:129:POSTGRES_HOST=msjarvisgis-recovery
.env.backup-20260505:133:POSTGRES_USER=gbim
.env.backup-20260505:187:TRAILS_DSN=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.bak:20:DB_DSN=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.bak:22:DB_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.bak:32:GBIM_ROUTER_URL=http://jarvis-gbim-query-router:7205
.env.bak:33:GBIM_URL=http://jarvis-gbim-query-router:7205
.env.bak:34:GEODB_DSN=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.bak:63:LOCAL_RESOURCES_DSN=postgresql://msjarvis:MsJarvis2026Secure@jarvis-local-resources-db:5432/msjarvisgis
.env.bak:75:MSJARVIS_GIS_URL=postgresql://msjarvis:MsJarvis2026Secure@jarvis-local-resources-db:5432/msjarvisgis
.env.bak:113:POSTGRES_DB=msjarvisgis
.env.complete:22:DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.complete:23:DB_DSN=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.complete:24:DB_DSN=postgresql://postgres:postgres@msjarvisgis-recovery:5432/msjarvisgis
.env.complete:26:DB_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.complete:37:GBIM_ROUTER_URL=http://jarvis-gbim-query-router:7205
.env.complete:38:GBIM_URL=http://jarvis-gbim-query-router:7205
.env.complete:39:GEODB_DSN=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.complete:69:LOCAL_RESOURCES_DSN=postgresql://msjarvis:MsJarvis2026Secure@jarvis-local-resources-db:5432/msjarvisgis
.env.complete:70:LOCAL_RESOURCES_DSN=postgresql://msjarvis:Nathaniel1@jarvis-gis-db:5432/msjarvisgis
.env.complete:72:LOCAL_RESOURCES_DSN=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.complete:84:MSJARVIS_GIS_URL=postgresql://msjarvis:MsJarvis2026Secure@jarvis-local-resources-db:5432/msjarvisgis
.env.complete:85:MSJARVIS_GIS_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.complete:125:POSTGRES_DB=msjarvisgis
.env.complete:129:POSTGRES_HOST=msjarvisgis-recovery
.env.complete:133:POSTGRES_USER=gbim
.env.complete:187:TRAILS_DSN=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
.env.example:2:GBIM_URL=http://jarvis-gbim-query-router:7205
config/Caddyfile:45:	handle /auth/portal/me* {
config/Caddyfile:55:			respond `{"detail":"Not authenticated"}` 401
config/Caddyfile:64:			respond `{"detail":"Not authenticated"}` 401
config/Caddyfile:73:			respond `{"detail":"Not authenticated"}` 401
config/Caddyfile:83:			respond `{"detail":"Not authenticated"}` 401
config/Caddyfile:93:			respond `{"detail":"Not authenticated"}` 401
config/Caddyfile:105:			respond `{"detail":"Not authenticated"}` 401
config/Caddyfile:121:			respond `{"detail":"Not authenticated"}` 401
config/Caddyfile:138:			respond `{"detail":"Not authenticated"}` 401
config/Caddyfile:152:	handle /auth/apply* {
config/Caddyfile:159:	handle /auth/approve* {
config/Caddyfile:166:	handle /auth/deny* {
config/Caddyfile:173:	handle /auth/portal* {
config/Caddyfile:180:	handle /auth/applications* {
config/Caddyfile:187:	handle /auth/first-login* {
config/Caddyfile:194:	handle /auth/register* {
config/Caddyfile:201:	handle /auth/login* {
config/Caddyfile:208:	handle /auth/logout* {
config/Caddyfile:215:	handle /auth/me* {
config/Caddyfile:222:	handle /auth* {
config/Caddyfile.bak.1779823184:58:    handle /auth/token* {
config/Caddyfile.bak.1779823184:62:    handle /auth* {
config/Caddyfile.bak.1779823184:110:    forward_auth @protected {
config/Caddyfile.bak.1779823184:111:        uri http://127.0.0.1:8092/auth/me
config/Caddyfile.bak.1779823184:127:    handle /auth* {
config/Caddyfile.bak.20260502-173808:45:    handle /auth/token* {
config/Caddyfile.bak.20260502-173808:49:    handle /auth* {
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

