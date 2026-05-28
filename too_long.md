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
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild

# 1) Look for obvious Redis env vars and URLs
grep -RInE 'REDIS_URL|REDIS_HOST|REDIS_PORT|REDIS_PASSWORD|UPSTASH_REDIS|KV_URL' . 2>/dev/null

# 2) Look for redis client usage in code
grep -RInE 'ioredis|redis@|createClient\\(|new Redis\\(|Upstash' --include='*.ts' --include='*.tsx' --include='*.js' . 2>/dev/null

# 3) Look for a dedicated redis config file
find . -maxdepth 5 -type f \( -iname '*redis*.ts' -o -iname '*redis*.js' -o -iname 'cache.ts' -o -iname 'session*.ts' \) 2>/dev/null
./docker-compose.yml.backup.1768788421:19:      - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260501:12:    - REDIS_URL=redis://jarvis-redis:6379/3
./docker-compose.yml.bak.20260501:42:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260501:1269:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bak.20260501:1423:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260501:1424:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260501:1453:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260501:1454:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260501:1477:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260501:1478:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260501:1617:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260501:1618:    - REDIS_PORT=6379
./docker-compose.yml.bak.20260501:1678:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.golden.yml:31:      - REDIS_URL=redis://jarvis-redis:6379
./ms-allis-auth-install/backend/auth_api_patch.py:26:REDIS_URL       = os.getenv("REDIS_URL", "redis://jarvis-redis:6379")
./ms-allis-auth-install/backend/auth_api_patch.py:54:r = redis.from_url(REDIS_URL, decode_responses=True)
./ms-allis-auth-install/backend/auth_api_patch.py:55:wallet_svc = WalletService(redis_client=redis.from_url(REDIS_URL))
./docker-compose.yml.backup:998:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup:999:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup:1011:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup:1012:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup:1025:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup:1026:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup:1049:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup:1050:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260206142334:948:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260206142334:949:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260206142334:961:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260206142334:962:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260206142334:974:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260206142334:975:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260206142334:997:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260206142334:998:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260422-204722:12:    - REDIS_URL=redis://jarvis-redis:6379/3
./docker-compose.yml.bak.20260422-204722:36:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260422-204722:1203:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bak.20260422-204722:1355:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260422-204722:1356:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260422-204722:1383:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260422-204722:1384:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260422-204722:1407:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260422-204722:1408:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260422-204722:1542:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260422-204722:1543:    - REDIS_PORT=6379
./docker-compose.golden.bak_nbb_base_final:31:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.chroma-backup-20260114054916:14:    - REDIS_URL=redis://jarvis-redis:6379
./.env:125:REDIS_HOST=jarvis-redis
./.env:126:REDIS_PORT=6379
./.env:127:REDIS_URL=redis://jarvis-redis:6379/0
./.env:134:SESSION_REDIS_HOST=jarvis-redis
./.env:136:SESSION_REDIS_PORT=6379
./docker-compose.yml.broken:16:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260422-204609:12:    - REDIS_URL=redis://jarvis-redis:6379/3
./docker-compose.yml.bak.20260422-204609:36:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260422-204609:1203:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bak.20260422-204609:1355:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260422-204609:1356:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260422-204609:1383:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260422-204609:1384:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260422-204609:1407:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260422-204609:1408:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260422-204609:1542:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260422-204609:1543:    - REDIS_PORT=6379
./docker-compose.yml.bak-1768791760:19:      - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak-1768791194:19:      - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak_hilbert_depsfix_20260415-142340:21:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak_hilbert_depsfix_20260415-142340:69:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak_hilbert_depsfix_20260415-142340:99:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_hilbert_depsfix_20260415-142340:100:      REDIS_PORT: '6379'
./docker-compose.RAG_WORKING_20260116.yml.bak_gateway8050:363:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.pre-secrets-fix:12:    - REDIS_URL=redis://jarvis-redis:6379/3
./docker-compose.yml.pre-secrets-fix:36:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.pre-secrets-fix:1203:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.pre-secrets-fix:1355:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.pre-secrets-fix:1356:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.pre-secrets-fix:1383:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.pre-secrets-fix:1384:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.pre-secrets-fix:1407:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.pre-secrets-fix:1408:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.pre-secrets-fix:1542:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.pre-secrets-fix:1543:    - REDIS_PORT=6379
./docker-compose.yml.bak.20260517-162627:1009:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260517-162627:1010:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260517-162627:1021:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260517-162627:1022:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260517-162627:1034:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260517-162627:1035:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260517-162627:1048:      REDIS_URL: "redis://jarvis-redis:6379/0"
./docker-compose.yml.bak.20260517-162627:1060:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260517-162627:1061:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260517-162627:1536:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260517-162627:1552:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260517-162627:1568:      REDIS_HOST: jarvis-redis
./admin_cli.py:17:    REDIS_HOST          default: localhost
./admin_cli.py:18:    REDIS_PORT          default: 6380
./admin_cli.py:53:        host=os.getenv("REDIS_HOST", "localhost"),
./admin_cli.py:54:        port=int(os.getenv("REDIS_PORT", "6380")),
./docker-compose.golden.bak_services_mapping_fix:27:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak_20260415-111235:19:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak_20260415-111235:67:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak_20260415-111235:97:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_20260415-111235:98:      REDIS_PORT: '6379'
./docker-compose.yml.backup_nbb_ports_fixed:952:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_nbb_ports_fixed:953:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup_nbb_ports_fixed:964:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_nbb_ports_fixed:965:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup_nbb_ports_fixed:977:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_nbb_ports_fixed:978:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup_nbb_ports_fixed:999:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_nbb_ports_fixed:1000:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup_20260318_110223:11:    - REDIS_URL=redis://jarvis-redis:6379
./auth_api.py.bak-cors:23:REDIS_URL    = os.getenv("REDIS_URL",    "redis://localhost:6379/0")
./auth_api.py.bak-cors:31:r  = redis.from_url(REDIS_URL, decode_responses=True)
./docker-compose.yml.bak.20260407-221457:34:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260407-221457:1070:      REDIS_URL: redis://jarvis-redis:6379/0
./docker-compose.yml.bak.20260407-221457:1512:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bak.20260407-221457:1659:    - REDIS_URL=redis://jarvis-redis:6379/0
./docker-compose.yml.bak.20260407-221457:1688:    - REDIS_URL=redis://jarvis-redis:6379/3
./docker-compose.yml.bak.20260407-221457:1713:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml:28:      - SERVICE_REDIS_HOST=jarvis-redis
./docker-compose.yml:29:      - SERVICE_REDIS_PORT=6379
./docker-compose.yml:757:      - SERVICE_REDIS_HOST=jarvis-redis
./docker-compose.yml:758:      - SERVICE_REDIS_PORT=6379
./docker-compose.yml:1040:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml:1041:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml:1054:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml:1055:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml:1069:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml:1070:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml:1085:      REDIS_URL: "redis://jarvis-redis:6379/0"
./docker-compose.yml:1099:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml:1100:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml:1311:      - SERVICE_REDIS_HOST=jarvis-redis
./docker-compose.yml:1312:      - SERVICE_REDIS_PORT=6379
./docker-compose.yml:1595:      REDIS_HOST: jarvis-redis
./docker-compose.yml:1611:      REDIS_HOST: jarvis-redis
./docker-compose.yml:1627:      REDIS_HOST: jarvis-redis
./docker-compose.yml:2033:      - REDIS_URL=redis://jarvis-redis:6379
./deploy.sh:91:      - REDIS_HOST=REDIS_CONTAINER_NAME
./deploy.sh:92:      - REDIS_PORT=6380
./docker-compose.yml.bak_hilbert_depsfix_20260415-142332:21:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak_hilbert_depsfix_20260415-142332:69:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak_hilbert_depsfix_20260415-142332:99:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_hilbert_depsfix_20260415-142332:100:      REDIS_PORT: '6379'
./docker-compose.golden.bak_bbb_proxy_cmd_fix:27:    - REDIS_URL=redis://jarvis-redis:6379
./.env.backup-20260505:141:REDIS_HOST=jarvis-redis
./.env.backup-20260505:142:REDIS_PORT=6379
./.env.backup-20260505:143:REDIS_URL=redis://jarvis-redis:6379
./.env.backup-20260505:144:REDIS_URL=redis://jarvis-redis:6379/0
./.env.backup-20260505:145:REDIS_URL=redis://jarvis-redis:6379/3
./.env.backup-20260505:146:REDIS_URL=redis://jarvis-redis:6379/4
./.env.backup-20260505:177:SESSION_REDIS_HOST=jarvis-redis
./.env.backup-20260505:179:SESSION_REDIS_PORT=6379
./docker-compose.yml.bak.20260510-194401:1014:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260510-194401:1015:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260510-194401:1026:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260510-194401:1027:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260510-194401:1039:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260510-194401:1040:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260510-194401:1061:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260510-194401:1062:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.broken-1768013498:14:      - REDIS_URL=redis://jarvis-redis:6379
./_archive/service_baks_20260430/jarvis_eeg_delta_30s.py.bak_20260415-110737:20:REDIS_HOST = os.getenv("JARVIS_REDIS_HOST", "127.0.0.1")
./_archive/service_baks_20260430/jarvis_eeg_delta_30s.py.bak_20260415-110737:21:REDIS_PORT = int(os.getenv("JARVIS_REDIS_PORT", "6380"))
./_archive/service_baks_20260430/jarvis_eeg_delta_30s.py.bak_20260415-110737:77:    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./_archive/service_baks_20260430/jarvis_eeg_delta_30s.py.bak_20260415-110737:152:        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./_archive/service_baks_20260430/brain_orchestrator.py.bak_1769197532:38:REGISTRY_REDIS_URL = os.getenv("REGISTRY_REDIS_URL", "").strip()
./_archive/service_baks_20260430/brain_orchestrator.py.bak_1769197532:40:if REGISTRY_REDIS_URL:
./_archive/service_baks_20260430/brain_orchestrator.py.bak_1769197532:44:        redis_client = redis.Redis.from_url(REGISTRY_REDIS_URL)
./_archive/service_baks_20260430/brain_orchestrator.py.bak_1769197532:46:        logger.info(f"✅ Connected to Redis for registry at {REGISTRY_REDIS_URL}")
./_archive/service_baks_20260430/ms_jarvis_memory.py.bak.20260416-135208:15:REDIS_HOST  = os.getenv("REDIS_HOST", "jarvis-redis")
./_archive/service_baks_20260430/ms_jarvis_memory.py.bak.20260416-135208:16:REDIS_PORT  = int(os.getenv("REDIS_PORT", 6379))
./_archive/service_baks_20260430/ms_jarvis_memory.py.bak.20260416-135208:22:    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./_archive/service_baks_20260430/brain_orchestrator.py.bak_ch29:60:REGISTRY_REDIS_URL = os.getenv("REGISTRY_REDIS_URL", "").strip()
./_archive/service_baks_20260430/brain_orchestrator.py.bak_ch29:62:if REGISTRY_REDIS_URL:
./_archive/service_baks_20260430/brain_orchestrator.py.bak_ch29:65:        redis_client = redis.Redis.from_url(REGISTRY_REDIS_URL)
./_archive/service_baks_20260430/brain_orchestrator.py.bak_ch29:67:        logger.info(f"✅ Connected to Redis for registry at {REGISTRY_REDIS_URL}")
./_archive/service_baks_20260430/ms_jarvis_memory.py.bak.20260416-134857:15:REDIS_HOST  = os.getenv("REDIS_HOST", "jarvis-redis")
./_archive/service_baks_20260430/ms_jarvis_memory.py.bak.20260416-134857:16:REDIS_PORT  = int(os.getenv("REDIS_PORT", 6379))
./_archive/service_baks_20260430/ms_jarvis_memory.py.bak.20260416-134857:22:    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./_archive/service_baks_20260430/jarvis_hilbert_state.py.bak_20260415-154702:21:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/3")
./_archive/service_baks_20260430/jarvis_hilbert_state.py.bak_20260415-154702:36:    return redis.from_url(REDIS_URL, decode_responses=True)
./_archive/service_baks_20260430/brain_orchestrator.py.bak_1769197625:38:REGISTRY_REDIS_URL = os.getenv("REGISTRY_REDIS_URL", "").strip()
./_archive/service_baks_20260430/brain_orchestrator.py.bak_1769197625:40:if REGISTRY_REDIS_URL:
./_archive/service_baks_20260430/brain_orchestrator.py.bak_1769197625:44:        redis_client = redis.Redis.from_url(REGISTRY_REDIS_URL)
./_archive/service_baks_20260430/brain_orchestrator.py.bak_1769197625:46:        logger.info(f"✅ Connected to Redis for registry at {REGISTRY_REDIS_URL}")
./_archive/service_baks_20260430/dynamic_port_scheduler.py.backup_1762960055:33:REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
./_archive/service_baks_20260430/dynamic_port_scheduler.py.backup_1762960055:34:REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
./_archive/service_baks_20260430/dynamic_port_scheduler.py.backup_1762960055:39:        host=REDIS_HOST, 
./_archive/service_baks_20260430/dynamic_port_scheduler.py.backup_1762960055:40:        port=REDIS_PORT, 
./_archive/service_baks_20260430/dynamic_port_scheduler.py.backup_1762960055:46:    logger.info(f"✅ Connected to Redis at {REDIS_HOST}:{REDIS_PORT}")
./_archive/service_baks_20260430/dynamic_port_scheduler.py.backup_1762960055:186:        "redis_host": REDIS_HOST,
./_archive/service_baks_20260430/dynamic_port_scheduler.py.backup_1762960055:187:        "redis_port": REDIS_PORT,
./_archive/service_baks_20260430/jarvis_eeg_delta_30s.py.bak_steward_20260415-112104:20:REDIS_HOST = os.getenv("JARVIS_REDIS_HOST", "127.0.0.1")
./_archive/service_baks_20260430/jarvis_eeg_delta_30s.py.bak_steward_20260415-112104:21:REDIS_PORT = int(os.getenv("JARVIS_REDIS_PORT", "6380"))
./_archive/service_baks_20260430/jarvis_eeg_delta_30s.py.bak_steward_20260415-112104:77:    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./_archive/service_baks_20260430/jarvis_eeg_delta_30s.py.bak_steward_20260415-112104:152:        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./_archive/service_baks_20260430/auth_api.py.bak_20260426-162704:41:REDIS_URL       = os.getenv("REDIS_URL", "redis://jarvis-redis:6379")
./_archive/service_baks_20260430/auth_api.py.bak_20260426-162704:69:r = redis.from_url(REDIS_URL, decode_responses=True)
./_archive/service_baks_20260430/auth_api.py.bak_20260426-162704:70:wallet_svc = WalletService(redis_client=redis.from_url(REDIS_URL))
./_archive/service_baks_20260430/brain_orchestrator.py.bak_20260419_152123:42:REGISTRY_REDIS_URL = os.getenv("REGISTRY_REDIS_URL", "").strip()
./_archive/service_baks_20260430/brain_orchestrator.py.bak_20260419_152123:44:if REGISTRY_REDIS_URL:
./_archive/service_baks_20260430/brain_orchestrator.py.bak_20260419_152123:48:        redis_client = redis.Redis.from_url(REGISTRY_REDIS_URL)
./_archive/service_baks_20260430/brain_orchestrator.py.bak_20260419_152123:50:        logger.info(f"✅ Connected to Redis for registry at {REGISTRY_REDIS_URL}")
./_archive/service_baks_20260430/auth_router.py.bak:19:_REDIS_URL = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")
./_archive/service_baks_20260430/auth_router.py.bak:32:        r = redis_mod.Redis.from_url(_REDIS_URL, decode_responses=True)
./_archive/service_baks_20260430/auth_router.py.bak_1777164187:19:_REDIS_URL = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")
./_archive/service_baks_20260430/auth_router.py.bak_1777164187:32:        r = redis_mod.Redis.from_url(_REDIS_URL, decode_responses=True)
./_archive/service_baks_20260430/jarvis_hilbert_state.py.bak.20260415-171334:21:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/3")
./_archive/service_baks_20260430/jarvis_hilbert_state.py.bak.20260415-171334:36:    return redis.from_url(REDIS_URL, decode_responses=True)
./_archive/service_baks_20260430/jarvis_hilbert_state.py.bak.20260415-171456:21:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/3")
./_archive/service_baks_20260430/jarvis_hilbert_state.py.bak.20260415-171456:36:    return redis.from_url(REDIS_URL, decode_responses=True)
./_archive/service_baks_20260430/dynamic_port_service.py.bak:22:            redis_host = os.getenv("SERVICE_REDIS_HOST", "localhost")
./_archive/service_baks_20260430/brain_orchestrator.py.bak.1775644692:41:REGISTRY_REDIS_URL = os.getenv("REGISTRY_REDIS_URL", "").strip()
./_archive/service_baks_20260430/brain_orchestrator.py.bak.1775644692:43:if REGISTRY_REDIS_URL:
./_archive/service_baks_20260430/brain_orchestrator.py.bak.1775644692:47:        redis_client = redis.Redis.from_url(REGISTRY_REDIS_URL)
./_archive/service_baks_20260430/brain_orchestrator.py.bak.1775644692:49:        logger.info(f"✅ Connected to Redis for registry at {REGISTRY_REDIS_URL}")
./_archive/service_baks_20260430/auth_api.py.bak-2026-04-26:26:REDIS_URL       = os.getenv("REDIS_URL", "redis://jarvis-redis:6379")
./_archive/service_baks_20260430/auth_api.py.bak-2026-04-26:54:r = redis.from_url(REDIS_URL, decode_responses=True)
./_archive/service_baks_20260430/auth_api.py.bak-2026-04-26:55:wallet_svc = WalletService(redis_client=redis.from_url(REDIS_URL))
./docker-compose.golden.bak_web_research_cmd:31:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416_145312:13:      - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260416_145312:37:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416_145312:1518:    - REDIS_URL=redis://jarvis-redis:6379/4
./.env.complete:141:REDIS_HOST=jarvis-redis
./.env.complete:142:REDIS_PORT=6379
./.env.complete:143:REDIS_URL=redis://jarvis-redis:6379
./.env.complete:144:REDIS_URL=redis://jarvis-redis:6379/0
./.env.complete:145:REDIS_URL=redis://jarvis-redis:6379/3
./.env.complete:146:REDIS_URL=redis://jarvis-redis:6379/4
./.env.complete:177:SESSION_REDIS_HOST=jarvis-redis
./.env.complete:179:SESSION_REDIS_PORT=6379
./.env.bak:125:REDIS_HOST=jarvis-redis
./.env.bak:126:REDIS_PORT=6379
./.env.bak:127:REDIS_URL=redis://jarvis-redis:6379/0
./.env.bak:134:SESSION_REDIS_HOST=jarvis-redis
./.env.bak:136:SESSION_REDIS_PORT=6379
./docker-compose.yml.bak.20260510-195030:1018:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260510-195030:1019:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260510-195030:1030:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260510-195030:1031:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260510-195030:1043:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260510-195030:1044:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260510-195030:1065:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260510-195030:1066:      SERVICE_REDIS_PORT: 6379
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1025:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1174:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1290:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1416:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1444:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1747:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.keyfix.20260413-182644:1769:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1028:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1180:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1296:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1422:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1450:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1753:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.local-community-aaacpe.20260413-224240:1775:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:16:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1033:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1185:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1301:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1427:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1455:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1758:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.scheduler-netfix.20260413-230633:1780:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1025:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1174:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1290:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1416:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1444:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1747:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.indentfix.20260413-182402:1769:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1025:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1174:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1290:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1416:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1444:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1747:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_manual.20260413-214948:1769:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:14:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1031:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1183:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1299:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1425:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1453:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1756:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225908:1778:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml:18:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml:1040:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml:1192:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml:1320:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml:1451:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml:1479:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml:1782:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml:1804:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:16:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1033:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1185:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1301:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1427:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1455:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1758:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag.20260413-231135:1780:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1029:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1181:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1297:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1423:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1451:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1754:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.qualianet.20260413-222756:1776:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:16:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1033:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1185:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1301:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1430:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1458:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1761:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-modulefix.20260413-231600:1783:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1028:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1180:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1296:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1422:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1450:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1753:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-net.20260413-225146:1775:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:22:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1039:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1191:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1307:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1433:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1461:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1764:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.sedfix.20260413-230529:1786:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:18:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1035:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1187:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1303:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1429:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1457:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1760:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225914:1782:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:22:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1039:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1191:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1307:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1433:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1461:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1764:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.fix-mainbrain-networks.20260413-230231:1786:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1025:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1174:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1290:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1416:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1444:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1747:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260413-180858:1769:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:16:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1034:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1186:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1302:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1425:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1453:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1756:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260416_201430:1778:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1025:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1177:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1293:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1419:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1447:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1750:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.bridge_net.20260413-215213:1772:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:16:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1033:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1185:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1301:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1430:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1458:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1761:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean.20260413-231928:1783:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1025:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1177:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1293:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1419:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1447:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1750:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.chroma-net.20260413-222557:1772:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1029:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1181:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1297:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1423:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1451:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1754:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.manualfix.20260413-223024:1776:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1025:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1174:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1290:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1416:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1444:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1747:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.neuro.20260413-214218:1769:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak:1009:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak:1158:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak:1274:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak:1400:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak:1428:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak:1731:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak:1753:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:16:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1033:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1185:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1301:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1430:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1458:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1761:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.aaacpe-rag-clean2.20260413-232017:1783:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1025:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1177:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1293:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1419:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1447:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1750:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.qualianet-min.20260413-223115:1772:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak-sec-20260410-001058:13:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1025:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1174:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1290:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1416:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1444:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1747:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.neuro_dir.20260413-214608:1769:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak_20260410_171707:13:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak_20260410_171707:1303:      - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak_20260410_171707:1400:      - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1025:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1174:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1290:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1416:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1444:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1747:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.ragfix.20260413-214147:1769:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1025:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1177:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1293:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1419:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1447:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1750:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.bridge_env.20260413-215332:1772:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1029:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1181:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1297:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1423:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1451:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1754:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.fix-localvol.20260413-224514:1776:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1025:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1174:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1290:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1416:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1444:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1747:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214915:1769:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak-20260410-000750:13:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1025:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1174:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1290:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1416:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1444:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1747:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.20260413213157:1769:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:11:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1025:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1174:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1290:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1416:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1444:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1747:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.rag_net.20260413-214558:1769:    - REDIS_URL=redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:22:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1039:      REDIS_URL: redis://jarvis-redis:6379/0
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1191:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1307:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1433:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1461:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1764:    - REDIS_URL=redis://jarvis-redis:6379
./msjarvis-rebuild/docker-compose.yml.bak.mainbrain-dualnet.20260413-225958:1786:    - REDIS_URL=redis://jarvis-redis:6379/0
./docker-compose.yml.bak.1768781706:20:      - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260423_095331:12:    - REDIS_URL=redis://jarvis-redis:6379/3
./docker-compose.yml.bak.20260423_095331:36:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260423_095331:1203:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bak.20260423_095331:1355:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260423_095331:1356:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260423_095331:1383:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260423_095331:1384:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260423_095331:1407:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260423_095331:1408:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260423_095331:1542:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260423_095331:1543:    - REDIS_PORT=6379
./docker-compose.override.yml.bak.20260430-120221:112:    - REDIS_HOST=jarvis-redis
./docker-compose.override.yml.bak.20260430-120221:113:    - REDIS_PORT=6379
./docker-compose.override.yml.bak.20260430-120221:137:    - SESSION_REDIS_HOST=jarvis-redis
./docker-compose.override.yml.bak.20260430-120221:138:    - SESSION_REDIS_PORT=6380
./docker-compose.MOTHERCARRIE.BAK.20260216-132834:998:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.MOTHERCARRIE.BAK.20260216-132834:999:      SERVICE_REDIS_PORT: 6379
./docker-compose.MOTHERCARRIE.BAK.20260216-132834:1011:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.MOTHERCARRIE.BAK.20260216-132834:1012:      SERVICE_REDIS_PORT: 6379
./docker-compose.MOTHERCARRIE.BAK.20260216-132834:1025:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.MOTHERCARRIE.BAK.20260216-132834:1026:      SERVICE_REDIS_PORT: 6379
./docker-compose.MOTHERCARRIE.BAK.20260216-132834:1049:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.MOTHERCARRIE.BAK.20260216-132834:1050:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260430-115408:12:    - REDIS_URL=redis://jarvis-redis:6379/3
./docker-compose.yml.bak.20260430-115408:41:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260430-115408:1248:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bak.20260430-115408:1401:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260430-115408:1402:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260430-115408:1429:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260430-115408:1430:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260430-115408:1453:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260430-115408:1454:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260430-115408:1587:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260430-115408:1588:    - REDIS_PORT=6379
./docker-compose.yml.bak.20260430-115408:1645:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.corrupt.20260415-1601:34:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.corrupt.20260415-1601:54:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.corrupt.20260415-1601:84:      REDIS_HOST: jarvis-redis
./docker-compose.yml.corrupt.20260415-1601:85:      REDIS_PORT: '6379'
./docker-compose-core.yml.bak.20260507-222222:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.backup_20260318_103245:11:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.RAG_WORKING_20260116.yml.bak_python310_fix:363:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260414-211038:19:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260414-211038:65:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260414-211038:95:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260414-211038:96:      REDIS_PORT: '6379'
./.scratch/backfill_existing_users.py:9:REDIS_URL = os.getenv("REDIS_URL", "redis://127.0.0.1:6380/0")
./.scratch/backfill_existing_users.py:13:    r     = redis.from_url(REDIS_URL, decode_responses=True)
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:12:    - REDIS_URL=redis://jarvis-redis:6379/3
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:36:    - REDIS_URL=redis://jarvis-redis:6379
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:1203:    - REDIS_URL=redis://jarvis-redis:6379/4
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:1355:    - REDIS_HOST=jarvis-redis
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:1356:    - JARVIS_REDIS_PORT=6379
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:1383:    - REDIS_HOST=jarvis-redis
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:1384:    - JARVIS_REDIS_PORT=6379
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:1407:    - REDIS_HOST=jarvis-redis
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:1408:    - JARVIS_REDIS_PORT=6379
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:1542:    - REDIS_HOST=jarvis-redis
./.scratch/docker-compose.yml.OI-C3-AU02-V2-backup:1543:    - REDIS_PORT=6379
./.scratch/test_auth_api.py:3:os.environ["REDIS_URL"]      = "redis://127.0.0.1:6380/0"
./docker-compose.RAG_WORKING_20260116.yml:363:    - REDIS_URL=redis://jarvis-redis:6379
./jarviscryptopolicy.py:13:REDIS_URL          = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/4")
./jarviscryptopolicy.py:18:redis_client       = redis.from_url(REDIS_URL, decode_responses=True)
./docker-compose.yml.hilbert-experiment.20260415-163850:18:      - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.hilbert-experiment.20260415-163850:73:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.hilbert-experiment.20260415-163850:103:      REDIS_HOST: jarvis-redis
./docker-compose.yml.hilbert-experiment.20260415-163850:104:      REDIS_PORT: '6379'
./docker-compose-core.yml.bak.20260507-222001:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.backup_nbb_ports:952:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_nbb_ports:953:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup_nbb_ports:964:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_nbb_ports:965:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup_nbb_ports:977:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_nbb_ports:978:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup_nbb_ports:999:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_nbb_ports:1000:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.pre_ollama_env_bak:1004:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.pre_ollama_env_bak:1005:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.pre_ollama_env_bak:1016:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.pre_ollama_env_bak:1017:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.pre_ollama_env_bak:1029:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.pre_ollama_env_bak:1030:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.pre_ollama_env_bak:1051:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.pre_ollama_env_bak:1052:      SERVICE_REDIS_PORT: 6379
./pituitary_gland.py.bak:13:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./pituitary_gland.py.bak:26:    return redis.from_url(REDIS_URL, decode_responses=True)
./pituitary_gland.py.bak:208:                _rr = _rl_rho.Redis(host=_rho_os.getenv('REDIS_HOST','jarvis-redis'), port=6379, decode_responses=True)
./.venv/lib64/python3.12/site-packages/triton/knobs.py:333:    host: env_str = env_str("TRITON_REDIS_HOST", "localhost")
./.venv/lib64/python3.12/site-packages/triton/knobs.py:334:    port: env_int = env_int("TRITON_REDIS_PORT", 6379)
./.venv/lib64/python3.12/site-packages/torch/_inductor/remote_cache.py:261:        if "TORCHINDUCTOR_REDIS_URL" in os.environ:
./.venv/lib64/python3.12/site-packages/torch/_inductor/remote_cache.py:262:            self._redis = redis.Redis.from_url(os.environ["TORCHINDUCTOR_REDIS_URL"])
./.venv/lib64/python3.12/site-packages/torch/_inductor/remote_cache.py:265:                host=os.environ.get("TORCHINDUCTOR_REDIS_HOST", "localhost"),
./.venv/lib64/python3.12/site-packages/torch/_inductor/remote_cache.py:266:                port=int(os.environ.get("TORCHINDUCTOR_REDIS_PORT", 6379)),
./.venv/lib/python3.12/site-packages/triton/knobs.py:333:    host: env_str = env_str("TRITON_REDIS_HOST", "localhost")
./.venv/lib/python3.12/site-packages/triton/knobs.py:334:    port: env_int = env_int("TRITON_REDIS_PORT", 6379)
./.venv/lib/python3.12/site-packages/torch/_inductor/remote_cache.py:261:        if "TORCHINDUCTOR_REDIS_URL" in os.environ:
./.venv/lib/python3.12/site-packages/torch/_inductor/remote_cache.py:262:            self._redis = redis.Redis.from_url(os.environ["TORCHINDUCTOR_REDIS_URL"])
./.venv/lib/python3.12/site-packages/torch/_inductor/remote_cache.py:265:                host=os.environ.get("TORCHINDUCTOR_REDIS_HOST", "localhost"),
./.venv/lib/python3.12/site-packages/torch/_inductor/remote_cache.py:266:                port=int(os.environ.get("TORCHINDUCTOR_REDIS_PORT", 6379)),
./services/ms_jarvis_production_chat.py:311:            os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0"),
./services/ms_jarvis_production_chat.py:409:        _rx = _rxr.Redis.from_url(os.getenv("REDIS_URL","redis://127.0.0.1:6379/0"), decode_responses=True, socket_connect_timeout=1)
./services/rag_query_router.py:23:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/rag_query_router.py:24:REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
./services/rag_query_router.py:29:        host=REDIS_HOST,
./services/rag_query_router.py:30:        port=REDIS_PORT,
./services/rag_query_router.py:36:    logger.info(f"Connected to Redis at {REDIS_HOST}:{REDIS_PORT} (db {REDIS_DB})")
./services/rag_query_router.py:38:    logger.error(f"Failed to connect to Redis at {REDIS_HOST}:{REDIS_PORT}: {e}")
./services/rag_query_router.py:41:        host=REDIS_HOST,
./services/rag_query_router.py:42:        port=REDIS_PORT,
./services/rag_query_router.py:573:        "host": REDIS_HOST,
./services/rag_query_router.py:574:        "port": REDIS_PORT,
./services/jarvis_hilbert_state.py:21:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/3")
./services/jarvis_hilbert_state.py:36:    return redis.from_url(REDIS_URL, decode_responses=True)
./services/ms_mountainshares_analytics.py:28:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/ms_mountainshares_analytics.py:29:REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
./services/ms_mountainshares_analytics.py:44:        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/gbim_api.py:142:            _os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0"),
./services/seed_admin_user.py:10:REDIS_URL   = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")
./services/seed_admin_user.py:12:r = redis.Redis.from_url(REDIS_URL, decode_responses=True)
./services/pituitary_gland.py:13:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./services/pituitary_gland.py:26:    return redis.from_url(REDIS_URL, decode_responses=True)
./services/pituitary_gland.py:213:                _rr = _rl_rho.Redis(host=_rho_os.getenv('REDIS_HOST','jarvis-redis'), port=6379, decode_responses=True)
./services/pituitary_gland.py:225:                    host=_rwos.getenv("REDIS_HOST","jarvis-redis"),
./services/pituitary_gland.py:226:                    port=int(_rwos.getenv("REDIS_PORT","6379")),
./services/restored_documents.json.bak-msallis:3382:      "content": "ies\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118\npip install transformers sentence-transformers\npip install ollama\n\nWeb framework and API\npip install fastapi uvicorn flask\n\nDatabase and storage\npip install redis chromadb\n\nUtilities and processing\npip install psutil pyyaml python-dotenv\npip install asyncio aiofiles\npip install requests numpy pandas\n\ntext\n\n#### Step 3: Configure Services\nSet up environment variables\ncat > .env << 'ENVEOF'\nOLLAMA_URL=http://localhost:11434\nREDIS_URL=redis://localhost:6379\nPOSTGRES_URL=postgresql://user:password@localhost:5432/ms_jarvis\nJARVIS_PORT=8010\nVECTOR_DB_PORT=8001\nENVEOF\n\nMake scripts executable\nchmod +x *.py\n\nSet up logging directory\nmkdir -p logs\nmkdir -p data/vector_db\nmkdir -p backups\n\ntext\n\n#### Step 4: Database Setup\nStart Redis (should already be running)\nsudo systemctl status redis-server\n\nCreate PostgreSQL database\nsudo -u postgres createdb ms_jarvis\nsudo -u postgres psql -c \"CREATE USER jarvis WITH PASSWORD 'your_password_here';\"\nsudo -u postgres psql -c \"GRANT ALL PRIVILEGES ON DATABASE ms_jarvis TO jarvis;\"\n\ntext\n\n#### Step 5: Start Core Services (In Order)\nTerminal 1: Start AI Server (core brain)\nsource venv/bin/activate\npython ai_server.py\n\nTerminal 2: Start Service Factory\nsource venv/bin/activate\npython ms_jarvis_service_factory.py\n\nTerminal 3: Start Brain Orchestrator\nsource venv/bin/activate\npython dynamic_app.py\n\nTerminal 4: Start Service Discovery\nsource venv/bin/activate",
./services/msjarvisunifiedswaggergatewayFIXED.py.bak-msallis:12:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/msjarvisunifiedswaggergatewayFIXED.py.bak-msallis:14:REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
./services/msjarvisunifiedswaggergatewayFIXED.py.bak-msallis:52:IDENTITY_REDIS = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/msjarvisunifiedswaggergatewayFIXED.py.bak-msallis:307:_egeria_redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/rag_query_router.py.bak-pre-gis-patch:23:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/rag_query_router.py.bak-pre-gis-patch:24:REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
./services/rag_query_router.py.bak-pre-gis-patch:29:        host=REDIS_HOST,
./services/rag_query_router.py.bak-pre-gis-patch:30:        port=REDIS_PORT,
./services/rag_query_router.py.bak-pre-gis-patch:36:    logger.info(f"Connected to Redis at {REDIS_HOST}:{REDIS_PORT} (db {REDIS_DB})")
./services/rag_query_router.py.bak-pre-gis-patch:38:    logger.error(f"Failed to connect to Redis at {REDIS_HOST}:{REDIS_PORT}: {e}")
./services/rag_query_router.py.bak-pre-gis-patch:41:        host=REDIS_HOST,
./services/rag_query_router.py.bak-pre-gis-patch:42:        port=REDIS_PORT,
./services/rag_query_router.py.bak-pre-gis-patch:466:        "host": REDIS_HOST,
./services/rag_query_router.py.bak-pre-gis-patch:467:        "port": REDIS_PORT,
./services/pituitary_gland.py.bak2:13:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./services/pituitary_gland.py.bak2:26:    return redis.from_url(REDIS_URL, decode_responses=True)
./services/pituitary_gland.py.bak2:213:                _rr = _rl_rho.Redis(host=_rho_os.getenv('REDIS_HOST','jarvis-redis'), port=6379, decode_responses=True)
./services/pituitary_gland.py.bak2:225:                    host=_rwos.getenv("REDIS_HOST","jarvis-redis"),
./services/pituitary_gland.py.bak2:226:                    port=int(_rwos.getenv("REDIS_PORT","6379")),
./services/admin_cli.py:24:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379")
./services/admin_cli.py:28:    r = redis.Redis.from_url(REDIS_URL, decode_responses=True)
./services/auth_api_patch.py:26:REDIS_URL       = os.getenv("REDIS_URL", "redis://jarvis-redis:6379")
./services/auth_api_patch.py:60:r = redis.from_url(REDIS_URL, decode_responses=True)
./services/auth_api_patch.py:61:wallet_svc = WalletService(redis_client=redis.from_url(REDIS_URL))
./services/msjarvisunifiedgateway.py:18:REDIS_URL = os.environ.get("JARVIS_REDIS_URL", "redis://localhost:6379/0")
./services/msjarvisunifiedgateway.py:19:redis_state = redis.from_url(REDIS_URL, decode_responses=True)
./services/brain_orchestrator.py.bak_1769197532:38:REGISTRY_REDIS_URL = os.getenv("REGISTRY_REDIS_URL", "").strip()
./services/brain_orchestrator.py.bak_1769197532:40:if REGISTRY_REDIS_URL:
./services/brain_orchestrator.py.bak_1769197532:44:        redis_client = redis.Redis.from_url(REGISTRY_REDIS_URL)
./services/brain_orchestrator.py.bak_1769197532:46:        logger.info(f"✅ Connected to Redis for registry at {REGISTRY_REDIS_URL}")
./services/brain_orchestrator.py:41:REGISTRY_REDIS_URL = os.getenv("REGISTRY_REDIS_URL", "").strip()
./services/brain_orchestrator.py:43:if REGISTRY_REDIS_URL:
./services/brain_orchestrator.py:47:        redis_client = redis.Redis.from_url(REGISTRY_REDIS_URL)
./services/brain_orchestrator.py:49:        logger.info(f"✅ Connected to Redis for registry at {REGISTRY_REDIS_URL}")
./services/neurobiologicalbrain/woah_algorithms/service/dynamic_port_service.py.bak-msallis:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/woah_algorithms/service/dynamic_port_service.py.bak-msallis:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/woah_algorithms/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/woah_algorithms/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/i_containers/service/dynamic_port_service.py.bak-msallis:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/i_containers/service/dynamic_port_service.py.bak-msallis:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/i_containers/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/i_containers/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/spiritual_root/service/dynamic_port_service.py.bak-msallis:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/spiritual_root/service/dynamic_port_service.py.bak-msallis:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/spiritual_root/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/spiritual_root/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/prefrontal_cortex/service/dynamic_port_service.py.bak-msallis:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/prefrontal_cortex/service/dynamic_port_service.py.bak-msallis:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/prefrontal_cortex/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/prefrontal_cortex/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/pituitary_gland/service/dynamic_port_service.py.bak-msallis:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/pituitary_gland/service/dynamic_port_service.py.bak-msallis:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/pituitary_gland/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/pituitary_gland/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/subconscious/service/dynamic_port_service.py.bak-msallis:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/subconscious/service/dynamic_port_service.py.bak-msallis:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/subconscious/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/subconscious/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/mother_carrie_protocols/service/dynamic_port_service.py.bak-msallis:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/mother_carrie_protocols/service/dynamic_port_service.py.bak-msallis:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/mother_carrie_protocols/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/mother_carrie_protocols/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/spiritual_maternal_integration/service/dynamic_port_service.py.bak-msallis:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/spiritual_maternal_integration/service/dynamic_port_service.py.bak-msallis:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/spiritual_maternal_integration/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/spiritual_maternal_integration/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/heteroglobulin_transport/service/dynamic_port_service.py.bak-msallis:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/heteroglobulin_transport/service/dynamic_port_service.py.bak-msallis:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/heteroglobulin_transport/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/heteroglobulin_transport/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/consciousness_containers/service/dynamic_port_service.py.bak-msallis:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/consciousness_containers/service/dynamic_port_service.py.bak-msallis:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/neurobiologicalbrain/consciousness_containers/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/neurobiologicalbrain/consciousness_containers/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/rag_general.py:18:REDIS_HOST = os.getenv("REDIS_HOST", "redis")
./services/rag_general.py:19:REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
./services/rag_general.py:23:    host=REDIS_HOST,
./services/rag_general.py:24:    port=REDIS_PORT,
./services/rag_general.py:95:        "host": REDIS_HOST,
./services/rag_general.py:96:        "port": REDIS_PORT,
./services/ms_jarvis_unified_gateway_v4.3.py.bak-msallis:18:REDIS_URL = os.environ.get("JARVIS_REDIS_URL", "redis://localhost:6379/0")
./services/ms_jarvis_unified_gateway_v4.3.py.bak-msallis:19:redis_state = redis.from_url(REDIS_URL, decode_responses=True)
./services/dynamic_port_service.py.bak-msallis:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/dynamic_port_service.py.bak-msallis:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/jarviscryptopolicy.py:13:REDIS_URL          = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/4")
./services/jarviscryptopolicy.py:18:redis_client       = redis.from_url(REDIS_URL, decode_responses=True)
./services/brain_orchestrator.py.bak-msallis:41:REGISTRY_REDIS_URL = os.getenv("REGISTRY_REDIS_URL", "").strip()
./services/brain_orchestrator.py.bak-msallis:43:if REGISTRY_REDIS_URL:
./services/brain_orchestrator.py.bak-msallis:47:        redis_client = redis.Redis.from_url(REGISTRY_REDIS_URL)
./services/brain_orchestrator.py.bak-msallis:49:        logger.info(f"✅ Connected to Redis for registry at {REGISTRY_REDIS_URL}")
./services/msjarvisunifiedswaggergatewayFIXED.py:12:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/msjarvisunifiedswaggergatewayFIXED.py:14:REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
./services/msjarvisunifiedswaggergatewayFIXED.py:52:IDENTITY_REDIS = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/msjarvisunifiedswaggergatewayFIXED.py:307:_egeria_redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/python/brain_orchestrator.py:37:REGISTRY_REDIS_URL = os.getenv("REGISTRY_REDIS_URL", "").strip()
./services/python/brain_orchestrator.py:39:if REGISTRY_REDIS_URL:
./services/python/brain_orchestrator.py:43:        redis_client = redis.Redis.from_url(REGISTRY_REDIS_URL)
./services/python/brain_orchestrator.py:45:        logger.info(f"✅ Connected to Redis for registry at {REGISTRY_REDIS_URL}")
./services/python/brain_orchestrator.py.bak-msallis:37:REGISTRY_REDIS_URL = os.getenv("REGISTRY_REDIS_URL", "").strip()
./services/python/brain_orchestrator.py.bak-msallis:39:if REGISTRY_REDIS_URL:
./services/python/brain_orchestrator.py.bak-msallis:43:        redis_client = redis.Redis.from_url(REGISTRY_REDIS_URL)
./services/python/brain_orchestrator.py.bak-msallis:45:        logger.info(f"✅ Connected to Redis for registry at {REGISTRY_REDIS_URL}")
./services/jarvis_rag_search/Dockerfile:11:ENV REDIS_URL=redis://jarvis-redis:6379/3
./services/jarvis_rag_search/main.py:11:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis-local:6379/3")
./services/jarvis_rag_search/main.py:13:r = redis.from_url(REDIS_URL, decode_responses=True)
./services/rag_query_router.py.bak3_20260508:20:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/rag_query_router.py.bak3_20260508:21:REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
./services/rag_query_router.py.bak3_20260508:26:        host=REDIS_HOST,
./services/rag_query_router.py.bak3_20260508:27:        port=REDIS_PORT,
./services/rag_query_router.py.bak3_20260508:33:    logger.info(f"Connected to Redis at {REDIS_HOST}:{REDIS_PORT} (db {REDIS_DB})")
./services/rag_query_router.py.bak3_20260508:35:    logger.error(f"Failed to connect to Redis at {REDIS_HOST}:{REDIS_PORT}: {e}")
./services/rag_query_router.py.bak3_20260508:38:        host=REDIS_HOST,
./services/rag_query_router.py.bak3_20260508:39:        port=REDIS_PORT,
./services/rag_query_router.py.bak3_20260508:409:        "host": REDIS_HOST,
./services/rag_query_router.py.bak3_20260508:410:        "port": REDIS_PORT,
./services/nbb/pituitary_gland.py:13:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./services/nbb/pituitary_gland.py:26:    return redis.from_url(REDIS_URL, decode_responses=True)
./services/nbb/pituitary_gland.py.bak:13:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./services/nbb/pituitary_gland.py.bak:26:    return redis.from_url(REDIS_URL, decode_responses=True)
./services/nbb/pituitary_gland.py.bak-msallis:13:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./services/nbb/pituitary_gland.py.bak-msallis:26:    return redis.from_url(REDIS_URL, decode_responses=True)
./services/jarvis_decay_escalation_consumer.py:28:REDIS_HOST    = os.getenv("REDIS_HOST", "127.0.0.1")
./services/jarvis_decay_escalation_consumer.py:29:REDIS_PORT    = int(os.getenv("REDIS_PORT", "6380"))
./services/jarvis_decay_escalation_consumer.py:103:    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/jarvis_decay_escalation_consumer.py:106:        f"poll={POLL_INTERVAL}s redis={REDIS_HOST}:{REDIS_PORT} "
./services/restored_documents.json:3382:      "content": "ies\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118\npip install transformers sentence-transformers\npip install ollama\n\nWeb framework and API\npip install fastapi uvicorn flask\n\nDatabase and storage\npip install redis chromadb\n\nUtilities and processing\npip install psutil pyyaml python-dotenv\npip install asyncio aiofiles\npip install requests numpy pandas\n\ntext\n\n#### Step 3: Configure Services\nSet up environment variables\ncat > .env << 'ENVEOF'\nOLLAMA_URL=http://localhost:11434\nREDIS_URL=redis://localhost:6379\nPOSTGRES_URL=postgresql://user:password@localhost:5432/ms_jarvis\nJARVIS_PORT=8010\nVECTOR_DB_PORT=8001\nENVEOF\n\nMake scripts executable\nchmod +x *.py\n\nSet up logging directory\nmkdir -p logs\nmkdir -p data/vector_db\nmkdir -p backups\n\ntext\n\n#### Step 4: Database Setup\nStart Redis (should already be running)\nsudo systemctl status redis-server\n\nCreate PostgreSQL database\nsudo -u postgres createdb ms_jarvis\nsudo -u postgres psql -c \"CREATE USER jarvis WITH PASSWORD 'your_password_here';\"\nsudo -u postgres psql -c \"GRANT ALL PRIVILEGES ON DATABASE ms_jarvis TO jarvis;\"\n\ntext\n\n#### Step 5: Start Core Services (In Order)\nTerminal 1: Start AI Server (core brain)\nsource venv/bin/activate\npython ai_server.py\n\nTerminal 2: Start Service Factory\nsource venv/bin/activate\npython ms_jarvis_service_factory.py\n\nTerminal 3: Start Brain Orchestrator\nsource venv/bin/activate\npython dynamic_app.py\n\nTerminal 4: Start Service Discovery\nsource venv/bin/activate",
./services/msjarvis_wv_entangled_gateway.py:41:REDIS_URL        = "redis://jarvis-redis:6379"
./services/auth_router.py:19:_REDIS_URL = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")
./services/auth_router.py:32:        r = redis_mod.Redis.from_url(_REDIS_URL, decode_responses=True)
./services/ms_mountainshares_indexer.py:27:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/ms_mountainshares_indexer.py:28:REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
./services/ms_mountainshares_indexer.py:52:    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/method_tracking_helper.py:8:METHOD_REDIS_URL = os.environ.get("JARVIS_METHOD_REDIS_URL", "redis://localhost:6379/1")
./services/method_tracking_helper.py:9:method_redis = redis.from_url(METHOD_REDIS_URL, decode_responses=True)
./services/ms_jarvis_unified_gateway_v4.3.py:18:REDIS_URL = os.environ.get("JARVIS_REDIS_URL", "redis://localhost:6379/0")
./services/ms_jarvis_unified_gateway_v4.3.py:19:redis_state = redis.from_url(REDIS_URL, decode_responses=True)
./services/brain_orchestrator.py.bak_1769197625:38:REGISTRY_REDIS_URL = os.getenv("REGISTRY_REDIS_URL", "").strip()
./services/brain_orchestrator.py.bak_1769197625:40:if REGISTRY_REDIS_URL:
./services/brain_orchestrator.py.bak_1769197625:44:        redis_client = redis.Redis.from_url(REGISTRY_REDIS_URL)
./services/brain_orchestrator.py.bak_1769197625:46:        logger.info(f"✅ Connected to Redis for registry at {REGISTRY_REDIS_URL}")
./services/confidence_decay_loop.py:37:REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
./services/confidence_decay_loop.py:38:REDIS_PORT = int(os.getenv("REDIS_PORT", 6380))
./services/confidence_decay_loop.py:53:    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/rag_query_router.py.bak2_20260508:20:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/rag_query_router.py.bak2_20260508:21:REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
./services/rag_query_router.py.bak2_20260508:26:        host=REDIS_HOST,
./services/rag_query_router.py.bak2_20260508:27:        port=REDIS_PORT,
./services/rag_query_router.py.bak2_20260508:33:    logger.info(f"Connected to Redis at {REDIS_HOST}:{REDIS_PORT} (db {REDIS_DB})")
./services/rag_query_router.py.bak2_20260508:35:    logger.error(f"Failed to connect to Redis at {REDIS_HOST}:{REDIS_PORT}: {e}")
./services/rag_query_router.py.bak2_20260508:38:        host=REDIS_HOST,
./services/rag_query_router.py.bak2_20260508:39:        port=REDIS_PORT,
./services/rag_query_router.py.bak2_20260508:354:        "host": REDIS_HOST,
./services/rag_query_router.py.bak2_20260508:355:        "port": REDIS_PORT,
./services/ms_jarvis_memory.py:16:REDIS_HOST  = os.getenv("REDIS_HOST", "jarvis-redis")
./services/ms_jarvis_memory.py:17:REDIS_PORT  = int(os.getenv("REDIS_PORT", 6379))
./services/ms_jarvis_memory.py:49:    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/jarvis-semaphore_msjarvis_semaphore.py.bak-msallis:107:REDIS_URL_SEM = _os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./services/jarvis-semaphore_msjarvis_semaphore.py.bak-msallis:148:        r = _redis.from_url(REDIS_URL_SEM, decode_responses=True)
./services/jarvis-semaphore_msjarvis_semaphore.py.bak-msallis:179:        r = _redis.from_url(REDIS_URL_SEM, decode_responses=True)
./services/jarvis-semaphore_msjarvis_semaphore.py.bak-msallis:195:        r = _redis.from_url(REDIS_URL_SEM, decode_responses=True)
./services/dynamic_port_scheduler.py.backup_1762960055:33:REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
./services/dynamic_port_scheduler.py.backup_1762960055:34:REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
./services/dynamic_port_scheduler.py.backup_1762960055:39:        host=REDIS_HOST, 
./services/dynamic_port_scheduler.py.backup_1762960055:40:        port=REDIS_PORT, 
./services/dynamic_port_scheduler.py.backup_1762960055:46:    logger.info(f"✅ Connected to Redis at {REDIS_HOST}:{REDIS_PORT}")
./services/dynamic_port_scheduler.py.backup_1762960055:186:        "redis_host": REDIS_HOST,
./services/dynamic_port_scheduler.py.backup_1762960055:187:        "redis_port": REDIS_PORT,
./services/auth_api.py:27:REDIS_URL       = os.getenv("REDIS_URL", "redis://jarvis-redis:6379")
./services/auth_api.py:55:r = redis.from_url(REDIS_URL, decode_responses=True)
./services/auth_api.py:56:wallet_svc = WalletService(redis_client=redis.from_url(REDIS_URL))
./services/msjarvisunifiedswaggergatewayFIXED.py.BEFORE_DOCKER_REWIRE:12:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/msjarvisunifiedswaggergatewayFIXED.py.BEFORE_DOCKER_REWIRE:14:REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
./services/msjarvisunifiedswaggergatewayFIXED.py.BEFORE_DOCKER_REWIRE:52:IDENTITY_REDIS = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/msjarvisunifiedswaggergatewayFIXED.py.BEFORE_DOCKER_REWIRE:306:_egeria_redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/rag_temporal.py:20:REDIS_HOST = os.getenv("REDIS_HOST", "redis")
./services/rag_temporal.py:21:REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
./services/rag_temporal.py:25:    host=REDIS_HOST,
./services/rag_temporal.py:26:    port=REDIS_PORT,
./services/rag_temporal.py:148:        "host": REDIS_HOST,
./services/rag_temporal.py:149:        "port": REDIS_PORT,
./services/jarvis_stewardship_scheduler.py:26:REDIS_HOST          = os.getenv("REDIS_HOST", "jarvis-redis")
./services/jarvis_stewardship_scheduler.py:27:REDIS_PORT          = int(os.getenv("REDIS_PORT", 6379))
./services/jarvis_stewardship_scheduler.py:35:    return redis_lib.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/ms_jarvis_phi_probe.py:19:REDIS_URL  = os.getenv("REDIS_URL",  "redis://jarvis-redis:6379/0")
./services/ms_jarvis_phi_probe.py:46:    return redis.from_url(REDIS_URL, decode_responses=True)
./services/ms_mountainshares_analytics.py.bak-msallis:28:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/ms_mountainshares_analytics.py.bak-msallis:29:REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
./services/ms_mountainshares_analytics.py.bak-msallis:44:        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/session_sidecar/app.py.bak-msallis:9:REDIS_HOST = os.getenv("SESSION_REDIS_HOST", "127.0.0.1")
./services/session_sidecar/app.py.bak-msallis:10:REDIS_PORT = int(os.getenv("SESSION_REDIS_PORT", "6380"))
./services/session_sidecar/app.py.bak-msallis:14:r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/session_sidecar/app.py:9:REDIS_HOST = os.getenv("SESSION_REDIS_HOST", "127.0.0.1")
./services/session_sidecar/app.py:10:REDIS_PORT = int(os.getenv("SESSION_REDIS_PORT", "6380"))
./services/session_sidecar/app.py:14:r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/venv/lib64/python3.12/site-packages/triton/knobs.py:335:    host: env_str = env_str("TRITON_REDIS_HOST", "localhost")
./services/venv/lib64/python3.12/site-packages/triton/knobs.py:336:    port: env_int = env_int("TRITON_REDIS_PORT", 6379)
./services/venv/lib64/python3.12/site-packages/torch/_inductor/remote_cache.py:261:        if "TORCHINDUCTOR_REDIS_URL" in os.environ:
./services/venv/lib64/python3.12/site-packages/torch/_inductor/remote_cache.py:262:            self._redis = redis.Redis.from_url(os.environ["TORCHINDUCTOR_REDIS_URL"])
./services/venv/lib64/python3.12/site-packages/torch/_inductor/remote_cache.py:265:                host=os.environ.get("TORCHINDUCTOR_REDIS_HOST", "localhost"),
./services/venv/lib64/python3.12/site-packages/torch/_inductor/remote_cache.py:266:                port=int(os.environ.get("TORCHINDUCTOR_REDIS_PORT", 6379)),
./services/venv/lib/python3.12/site-packages/triton/knobs.py:335:    host: env_str = env_str("TRITON_REDIS_HOST", "localhost")
./services/venv/lib/python3.12/site-packages/triton/knobs.py:336:    port: env_int = env_int("TRITON_REDIS_PORT", 6379)
./services/venv/lib/python3.12/site-packages/torch/_inductor/remote_cache.py:261:        if "TORCHINDUCTOR_REDIS_URL" in os.environ:
./services/venv/lib/python3.12/site-packages/torch/_inductor/remote_cache.py:262:            self._redis = redis.Redis.from_url(os.environ["TORCHINDUCTOR_REDIS_URL"])
./services/venv/lib/python3.12/site-packages/torch/_inductor/remote_cache.py:265:                host=os.environ.get("TORCHINDUCTOR_REDIS_HOST", "localhost"),
./services/venv/lib/python3.12/site-packages/torch/_inductor/remote_cache.py:266:                port=int(os.environ.get("TORCHINDUCTOR_REDIS_PORT", 6379)),
./services/rag_geospatial.py:20:REDIS_HOST = os.getenv("REDIS_HOST", "redis")
./services/rag_geospatial.py:21:REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
./services/rag_geospatial.py:25:    host=REDIS_HOST,
./services/rag_geospatial.py:26:    port=REDIS_PORT,
./services/rag_geospatial.py:121:        "host": REDIS_HOST,
./services/rag_geospatial.py:122:        "port": REDIS_PORT,
./services/ms_jarvis_memory.py.bak:14:REDIS_HOST  = os.getenv("REDIS_HOST", "jarvis-redis")
./services/ms_jarvis_memory.py.bak:15:REDIS_PORT  = int(os.getenv("REDIS_PORT", 6379))
./services/ms_jarvis_memory.py.bak:21:    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/dynamic_port_service.py.bak:22:            redis_host = os.getenv("SERVICE_REDIS_HOST", "localhost")
./services/rag_query_router.py.pre_tiered_routing:23:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/rag_query_router.py.pre_tiered_routing:24:REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
./services/rag_query_router.py.pre_tiered_routing:29:        host=REDIS_HOST,
./services/rag_query_router.py.pre_tiered_routing:30:        port=REDIS_PORT,
./services/rag_query_router.py.pre_tiered_routing:36:    logger.info(f"Connected to Redis at {REDIS_HOST}:{REDIS_PORT} (db {REDIS_DB})")
./services/rag_query_router.py.pre_tiered_routing:38:    logger.error(f"Failed to connect to Redis at {REDIS_HOST}:{REDIS_PORT}: {e}")
./services/rag_query_router.py.pre_tiered_routing:41:        host=REDIS_HOST,
./services/rag_query_router.py.pre_tiered_routing:42:        port=REDIS_PORT,
./services/rag_query_router.py.pre_tiered_routing:562:        "host": REDIS_HOST,
./services/rag_query_router.py.pre_tiered_routing:563:        "port": REDIS_PORT,
./services/pia_event_emitters.py:9:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/pia_event_emitters.py:10:REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
./services/pia_event_emitters.py:13:    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/integration_layer/container_bridge.py:7:    _r = _rl.Redis(host=os.getenv("REDIS_HOST","jarvis-redis"), port=int(os.getenv("REDIS_PORT",6379)), decode_responses=True)
./services/integration_layer/consciousness_merger.py:7:    _r = _redis_lib.Redis(host=os.getenv("REDIS_HOST","jarvis-redis"), port=int(os.getenv("REDIS_PORT",6379)), decode_responses=True)
./services/ms_mountainshares_indexer.py.bak-msallis:27:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/ms_mountainshares_indexer.py.bak-msallis:28:REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
./services/ms_mountainshares_indexer.py.bak-msallis:52:    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/gis_dataset_services/gis_dataset_service.py:26:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/gis_dataset_services/gis_dataset_service.py:27:REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
./services/gis_dataset_services/gis_dataset_service.py:92:            r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT,
./services/ms_jarvis_auth_api.py:9:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379")
./services/ms_jarvis_auth_api.py:10:rdb = redis.from_url(REDIS_URL, decode_responses=True)
./services/rag_query_router.py.bak-msallis:23:REDIS_HOST = os.getenv("REDIS_HOST", "jarvis-redis")
./services/rag_query_router.py.bak-msallis:24:REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
./services/rag_query_router.py.bak-msallis:29:        host=REDIS_HOST,
./services/rag_query_router.py.bak-msallis:30:        port=REDIS_PORT,
./services/rag_query_router.py.bak-msallis:36:    logger.info(f"Connected to Redis at {REDIS_HOST}:{REDIS_PORT} (db {REDIS_DB})")
./services/rag_query_router.py.bak-msallis:38:    logger.error(f"Failed to connect to Redis at {REDIS_HOST}:{REDIS_PORT}: {e}")
./services/rag_query_router.py.bak-msallis:41:        host=REDIS_HOST,
./services/rag_query_router.py.bak-msallis:42:        port=REDIS_PORT,
./services/rag_query_router.py.bak-msallis:573:        "host": REDIS_HOST,
./services/rag_query_router.py.bak-msallis:574:        "port": REDIS_PORT,
./services/msjarvisunifiedgateway.py.bak-msallis:18:REDIS_URL = os.environ.get("JARVIS_REDIS_URL", "redis://localhost:6379/0")
./services/msjarvisunifiedgateway.py.bak-msallis:19:redis_state = redis.from_url(REDIS_URL, decode_responses=True)
./services/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./services/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./services/ms_jarvis_memory.py.bak-msallis:14:REDIS_HOST  = os.getenv("REDIS_HOST", "jarvis-redis")
./services/ms_jarvis_memory.py.bak-msallis:15:REDIS_PORT  = int(os.getenv("REDIS_PORT", 6379))
./services/ms_jarvis_memory.py.bak-msallis:47:    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./services/jarvis-semaphore_msjarvis_semaphore.py:107:REDIS_URL_SEM = _os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./services/jarvis-semaphore_msjarvis_semaphore.py:148:        r = _redis.from_url(REDIS_URL_SEM, decode_responses=True)
./services/jarvis-semaphore_msjarvis_semaphore.py:179:        r = _redis.from_url(REDIS_URL_SEM, decode_responses=True)
./services/jarvis-semaphore_msjarvis_semaphore.py:195:        r = _redis.from_url(REDIS_URL_SEM, decode_responses=True)
./docker-compose.yml.bak.20260501-200948:12:    - REDIS_URL=redis://jarvis-redis:6379/3
./docker-compose.yml.bak.20260501-200948:42:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260501-200948:1269:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bak.20260501-200948:1423:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260501-200948:1424:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260501-200948:1453:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260501-200948:1454:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260501-200948:1477:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260501-200948:1478:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260501-200948:1617:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260501-200948:1618:    - REDIS_PORT=6379
./docker-compose.yml.bak.20260501-200948:1678:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.backup_20260215_232944:998:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_20260215_232944:999:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup_20260215_232944:1011:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_20260215_232944:1012:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup_20260215_232944:1025:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_20260215_232944:1026:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup_20260215_232944:1049:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_20260215_232944:1050:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260416-141203:13:      - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260416-141203:37:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416-141203:1512:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bak_1778453637:1004:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_1778453637:1005:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak_1778453637:1016:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_1778453637:1017:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak_1778453637:1029:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_1778453637:1030:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak_1778453637:1051:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_1778453637:1052:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.nbb.bak:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260518-215027:1013:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260518-215027:1014:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260518-215027:1025:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260518-215027:1026:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260518-215027:1038:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260518-215027:1039:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260518-215027:1052:      REDIS_URL: "redis://jarvis-redis:6379/0"
./docker-compose.yml.bak.20260518-215027:1064:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260518-215027:1065:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260518-215027:1540:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260518-215027:1556:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260518-215027:1572:      REDIS_HOST: jarvis-redis
./.env.example:14:REDIS_URL=redis://jarvis-redis:6379/0
./docker-compose.yml.BROKEN_BACKUP:19:      - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416_144451:13:      - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260416_144451:37:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416_144451:1518:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.backup_20260218_085941:952:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_20260218_085941:953:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup_20260218_085941:964:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_20260218_085941:965:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup_20260218_085941:977:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_20260218_085941:978:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup_20260218_085941:999:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_20260218_085941:1000:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260414-211257:19:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260414-211257:65:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260414-211257:95:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260414-211257:96:      REDIS_PORT: '6379'
./docker-compose.yml.bak.20260408-173239:46:      - REDIS_URL=redis://jarvis-redis:6379/3
./docker-compose.yml.bak.20260416-141709:13:      - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260416-141709:37:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416-141709:1518:    - REDIS_URL=redis://jarvis-redis:6379/4
./README-msallis-v1.md:85:REDIS_HOST=localhost                           # default, no need to set
./README-msallis-v1.md:86:REDIS_PORT=6380                                # default, no need to set
./docker-compose-core.yml.bak.20260430-120237:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.override.yml.disabled:112:      - REDIS_HOST=jarvis-redis
./docker-compose.override.yml.disabled:113:      - REDIS_PORT=6379
./docker-compose.override.yml.disabled:135:      - SESSION_REDIS_HOST=jarvis-redis
./docker-compose.override.yml.disabled:136:      - SESSION_REDIS_PORT=6380
./docker-compose.override.yml.disabled:151:      - SESSION_REDIS_HOST=jarvis-redis
./docker-compose.yml.bak-20260417-144354:13:      - REDIS_URL=redis://jarvis-redis:6379/3
./docker-compose.yml.bak-20260417-144354:37:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak-20260417-144354:1518:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bak-20260417-144354:1657:      - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak-20260417-144354:1658:      - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak-20260417-144354:1680:      - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak-20260417-144354:1681:      - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak-20260417-144354:1699:      - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak-20260417-144354:1700:      - JARVIS_REDIS_PORT=6379
./docker-compose.yml.pre-hilbert-portfix.20260415-162529:18:      - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.pre-hilbert-portfix.20260415-162529:75:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.pre-hilbert-portfix.20260415-162529:105:      REDIS_HOST: jarvis-redis
./docker-compose.yml.pre-hilbert-portfix.20260415-162529:106:      REDIS_PORT: '6379'
./docker-compose.yml.bak.20260414-210743:19:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260414-210743:65:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260414-210743:95:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260414-210743:96:      REDIS_PORT: '6379'
./docker-compose.yml.bak:860:    - REDIS_URL=redis://jarvis-redis:6379/0
./docker-compose.yml.bak:1044:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak:1045:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak:1056:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak:1057:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak:1069:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak:1070:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak:1081:      REDIS_URL: "redis://jarvis-redis:6379/0"
./docker-compose.yml.bak:1082:      REDIS_HOST: "jarvis-redis"
./docker-compose.yml.bak:1083:      REDIS_PORT: "6379"
./docker-compose.yml.bak:1094:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak:1095:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.backup_gateway_ports_20260109-091103:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260414-210516:19:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260414-210516:65:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260414-210516:95:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260414-210516:96:      REDIS_PORT: '6379'
./docker-compose.yml.broken-20260326-175632:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260206142646:948:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260206142646:949:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260206142646:961:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260206142646:962:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260206142646:974:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260206142646:975:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260206142646:997:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260206142646:998:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak_hilbert_cmdfix_20260415-142151:19:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak_hilbert_cmdfix_20260415-142151:67:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak_hilbert_cmdfix_20260415-142151:97:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_hilbert_cmdfix_20260415-142151:98:      REDIS_PORT: '6379'
./docker-compose.yml.bak-1768791131:19:      - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.after-bbb.bak:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.backup_jan13_consciousness:14:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.before_fix:998:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.before_fix:999:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.before_fix:1011:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.before_fix:1012:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.before_fix:1025:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.before_fix:1026:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.before_fix:1049:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.before_fix:1050:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260510-192741:1004:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260510-192741:1005:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260510-192741:1016:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260510-192741:1017:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260510-192741:1029:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260510-192741:1030:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260510-192741:1051:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260510-192741:1052:      SERVICE_REDIS_PORT: 6379
./docker-compose.golden.bak_before_brain_ports_cleanup:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416-141224:13:      - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260416-141224:37:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416-141224:1512:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bak_redis_fix_1769195657:923:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195657:934:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195657:945:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195657:956:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195657:967:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195657:978:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195657:989:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195657:1000:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195657:1011:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195657:1022:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195657:1033:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195657:1044:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195657:1055:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260414-210440:19:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260414-210440:64:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260414-210440:94:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260414-210440:95:      REDIS_PORT: '6379'
./docker-compose.yml.backup.1768786837:19:      - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.MOTHERCARRIE.BAK.20260216-132826:998:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.MOTHERCARRIE.BAK.20260216-132826:999:      SERVICE_REDIS_PORT: 6379
./docker-compose.MOTHERCARRIE.BAK.20260216-132826:1011:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.MOTHERCARRIE.BAK.20260216-132826:1012:      SERVICE_REDIS_PORT: 6379
./docker-compose.MOTHERCARRIE.BAK.20260216-132826:1025:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.MOTHERCARRIE.BAK.20260216-132826:1026:      SERVICE_REDIS_PORT: 6379
./docker-compose.MOTHERCARRIE.BAK.20260216-132826:1049:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.MOTHERCARRIE.BAK.20260216-132826:1050:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak_drop_roche:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak_add_clock:18:      - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.backup_20260318_110053:11:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.before_neuro_fix_1768012948:14:      - REDIS_URL=redis://jarvis-redis:6379
./auth_api.py:27:REDIS_URL    = os.getenv("REDIS_URL",    "redis://localhost:6379/0")
./auth_api.py:35:r  = redis.from_url(REDIS_URL, decode_responses=True)
./tests/test_registration_service.py:96:    url = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")
./docker-compose.yml.bak_redis_fix_1769195136:923:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195136:934:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195136:945:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195136:956:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195136:967:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195136:978:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195136:989:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195136:1000:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195136:1011:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195136:1022:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195136:1033:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195136:1044:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_fix_1769195136:1055:      REDIS_HOST: jarvis-redis
./auth_api.py.bak_20260426-122443:23:REDIS_URL    = os.getenv("REDIS_URL",    "redis://localhost:6379/0")
./auth_api.py.bak_20260426-122443:31:r  = redis.from_url(REDIS_URL, decode_responses=True)
./docker-compose.yml.bak.20260517-163017:1009:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260517-163017:1010:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260517-163017:1021:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260517-163017:1022:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260517-163017:1034:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260517-163017:1035:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260517-163017:1048:      REDIS_URL: "redis://jarvis-redis:6379/0"
./docker-compose.yml.bak.20260517-163017:1060:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260517-163017:1061:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260517-163017:1536:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260517-163017:1552:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260517-163017:1568:      REDIS_HOST: jarvis-redis
./docker-compose.yml.broken_backup:998:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.broken_backup:999:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.broken_backup:1011:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.broken_backup:1012:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.broken_backup:1025:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.broken_backup:1026:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.broken_backup:1049:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.broken_backup:1050:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.1768500857:14:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260522_204447:1019:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260522_204447:1020:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260522_204447:1031:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260522_204447:1032:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260522_204447:1044:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260522_204447:1045:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260522_204447:1058:      REDIS_URL: "redis://jarvis-redis:6379/0"
./docker-compose.yml.bak.20260522_204447:1070:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260522_204447:1071:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260522_204447:1546:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260522_204447:1562:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260522_204447:1578:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260416-141425:13:      - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260416-141425:37:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416-141425:1512:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.RAG_WORKING_20260116.yml.bak-portfix-20260122224758:363:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416_144808:13:      - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260416_144808:37:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416_144808:1518:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bbb.bak:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.backup.1768313257:14:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.golden.bak_python310_compose_all:31:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416-141603:13:      - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260416-141603:37:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416-141603:1519:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bak.20260522T193400Z:1019:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260522T193400Z:1020:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260522T193400Z:1031:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260522T193400Z:1032:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260522T193400Z:1044:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260522T193400Z:1045:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260522T193400Z:1058:      REDIS_URL: "redis://jarvis-redis:6379/0"
./docker-compose.yml.bak.20260522T193400Z:1070:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260522T193400Z:1071:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260522T193400Z:1546:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260522T193400Z:1562:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260522T193400Z:1578:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak.20260430-202630:12:    - REDIS_URL=redis://jarvis-redis:6379/3
./docker-compose.yml.bak.20260430-202630:42:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260430-202630:1267:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bak.20260430-202630:1420:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260430-202630:1421:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260430-202630:1448:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260430-202630:1449:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260430-202630:1472:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260430-202630:1473:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260430-202630:1608:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260430-202630:1609:    - REDIS_PORT=6379
./docker-compose.yml.bak.20260430-202630:1666:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.pre-hilbert-noports.20260415-162654:18:      - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.pre-hilbert-noports.20260415-162654:75:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.pre-hilbert-noports.20260415-162654:105:      REDIS_HOST: jarvis-redis
./docker-compose.yml.pre-hilbert-noports.20260415-162654:106:      REDIS_PORT: '6379'
./docker-compose.yml.backup_autonomous_learner_20260109-074048:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.working.20260118-235132.yml:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.backup.1768311648:14:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.backup_20260406_newservices:15:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.backup_20260406_newservices:1071:      REDIS_URL: redis://jarvis-redis:6379/0
./docker-compose.yml.backup_20260406_newservices:1527:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.backup_20260406_newservices:1675:    - REDIS_URL=redis://jarvis-redis:6379/0
./docker-compose.yml.backup_20260406_newservices:1704:    - REDIS_URL=redis://jarvis-redis:6379/3
./docker-compose.yml.backup_20260406_newservices:1729:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.RAG_WORKING_20260116.yml.bak-20260122223705:363:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.broken_spiritual:998:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.broken_spiritual:999:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.broken_spiritual:1011:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.broken_spiritual:1012:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.broken_spiritual:1025:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.broken_spiritual:1026:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.broken_spiritual:1049:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.broken_spiritual:1050:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak_woah_20260118163402:20:      - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.pre-hilbert-image-20260415-161150:21:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.pre-hilbert-image-20260415-161150:69:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.pre-hilbert-image-20260415-161150:99:      REDIS_HOST: jarvis-redis
./docker-compose.yml.pre-hilbert-image-20260415-161150:100:      REDIS_PORT: '6379'
./docker-compose-core.yml:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.20llm.bak:13:    - REDIS_URL=redis://jarvis-redis:6379
./logs/ch40_closeout/session_sidecar_app.snapshot.py:9:REDIS_HOST = os.getenv("SESSION_REDIS_HOST", "127.0.0.1")
./logs/ch40_closeout/session_sidecar_app.snapshot.py:10:REDIS_PORT = int(os.getenv("SESSION_REDIS_PORT", "6380"))
./logs/ch40_closeout/session_sidecar_app.snapshot.py:14:r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
./logs/ch40_closeout/tracing_file_windows.txt:603:REDIS_HOST = os.getenv("REDIS_HOST", "redis")
./logs/ch40_closeout/tracing_file_windows.txt:604:REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
./logs/ch40_closeout/tracing_file_windows.txt:608:    host=REDIS_HOST,
./logs/ch40_closeout/tracing_file_windows.txt:609:    port=REDIS_PORT,
./logs/ch40_closeout/tracing_file_windows.txt:731:        "host": REDIS_HOST,
./logs/ch40_closeout/tracing_file_windows.txt:732:        "port": REDIS_PORT,
./logs/ops_history/ops_history_20260402T041025Z.jsonl:200:  "body": "\n===== ./logs/ch40_closeout/tracing_containers.txt =====\njarvis-prometheus\tprom/prometheus:v2.48.0\t0.0.0.0:9090->9090/tcp, [::]:9090->9090/tcp\njarvis-grafana\tgrafana/grafana:10.2.3\t0.0.0.0:3000->3000/tcp, [::]:3000->3000/tcp\njarvis-jaeger\tjaegertracing/all-in-one:1.52\t4317-4318/tcp, 5775/udp, 5778/tcp, 9411/tcp, 14250/tcp, 14268/tcp, 6831-6832/udp, 0.0.0.0:16686->16686/tcp, [::]:16686->16686/tcp\njarvis-otel-collector\totel/opentelemetry-collector-contrib:0.93.0\t0.0.0.0:4317-4318->4317-4318/tcp, [::]:4317-4318->4317-4318/tcp, 0.0.0.0:8888->8888/tcp, [::]:8888->8888/tcp, 0.0.0.0:13133->13133/tcp, [::]:13133->13133/tcp, 55678-55679/tcp\njarvis-temporal-consciousness\tmsjarvis-rebuild-jarvis-temporal-consciousness\t7007/tcp\n\n===== ./logs/ch40_closeout/tracing_files.txt =====\n./logs/ch40_closeout/tracing_containers.txt\n./logs/ch40_closeout/tracing_files.txt\n./logs/ch40_closeout/tracing_grep.txt\n./recovered-services/bridge_ms_jarvis_main_gateway_to_integrate_spatial_temporal.log\n./recovered-services/bridge_ms_jarvis_main_gateway_to_ms_jarvis_temporal_consciousness.log\n./recovered-services/bridge_ms_jarvis_main_gateway_to_temporal_consciousness.log\n./recovered-services/Dockerfile.temporal_consciousness\n./recovered-services/gbim_temporal_indexer.py\n./recovered-services/integrate_spatial_temporal.py\n./recovered-services/ms_jarvis_temporal_consciousness_9220.log\n./recovered-services/ms_jarvis_temporal_consciousness.py\n./recovered-services/rag_temporal.py\n./recovered-services/services/ms_jarvis_temporal_consciousness.py\n./recovered-services/services/SPATIOTEMPORAL.log\n./recovered-services/services/temporal_consciousness.py\n./recovered-services/SPATIOTEMPORAL_CONSCIOUSNESS.md\n./recovered-services/temporal_consciousness.py\n./recovered-services/temporal.log\n./services/Dockerfile.temporal_consciousness\n./services/jarvis-temporal-consciousness_temporal_consciousness.py\n./services-safe/Dockerfile.temporal_consciousness\n./services-safe/gbim_temporal_indexer.py\n./services-safe/integrate_spatial_temporal.py\n./services-safe/integrate_spatial_temporal.py.backup_vocabulary_cleanup\n./services-safe/ms_jarvis_temporal_consciousness_9220.log\n./services-safe/ms_jarvis_temporal_consciousness.py\n./services-safe/rag_temporal_heartbeat.py\n./services-safe/rag_temporal.py\n./services-safe/requirements_temporal.txt\n./services-safe/SPATIOTEMPORAL_CONSCIOUSNESS.md\n./services-safe/SPATIOTEMPORAL.log\n./services-safe/temporal_consciousness.py\n./services-safe/temporal.log\n./services-safe/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py\n./.venv/lib/python3.12/site-packages/torch/_dynamo/test_dont_skip_tracing_functions.py\n\n===== ./logs/ch40_closeout/tracing_grep.txt =====\n./last-build.log:42: Image msjarvis-rebuild-jarvis-temporal-consciousness Building \n./last-build.log:354:#61 [jarvis-temporal-consciousness internal] load build definition from Dockerfile.temporal_consciousness\n./docker-compose.yml.bak.20260331_230904:662:  jarvis-temporal-consciousness:\n./docker-compose.yml.bak.20260331_230904:665:      dockerfile: Dockerfile.temporal_consciousness\n./docker-compose.yml.bak.20260331_230904:666:    container_name: jarvis-temporal-consciousness\n./docker-compose.yml.bak.20260312-002553:653:  jarvis-temporal-consciousness:\n./docker-compose.yml.bak.20260312-002553:656:      dockerfile: Dockerfile.temporal_consciousness\n./docker-compose.yml.bak.20260312-002553:657:    container_name: jarvis-temporal-consciousness\n./docs/governance/AUDIT-2026-03-24-final.txt:44:⚠️  WARN  [32] GBIM temporal decay columns — Phase 5 top-level columns not yet deployed\n./docs/governance/AUDIT-2026-03-24-FINAL-36-PASS.txt:45:✅ PASS  [32] GBIM temporal decay columns — decay logic present in services\n./docs/governance/AUDIT-2026-03-24-36-PASS.txt:46:✅ PASS  [32] GBIM temporal decay columns — decay logic present in services\n./docs/governance/AUDIT-2026-03-24-post-remediation.txt:45:\u001b[33m⚠️  WARN\u001b[0m  [32] GBIM temporal decay columns deployed — top-level decay columns not in gbim_zcta_2020 schema\n./docs/governance/AUDIT-2026-03-24-r5.txt:45:⚠️  WARN  [32] GBIM temporal decay columns — Phase 5 top-level columns not yet deployed\n./docs/governance/AUDIT-2026-03-24.txt:45:\u001b[33m⚠️  WARN\u001b[0m  [32] GBIM temporal decay columns deployed — top-level decay columns not in gbim_zcta_2020 schema\n./docs/governance/AUDIT-2026-03-24-r4.txt:46:⚠️  WARN  [32] GBIM temporal decay columns — Phase 5 top-level columns not yet deployed\n./docker-compose.yml.bak_20260330_2059:661:  jarvis-temporal-consciousness:\n./docker-compose.yml.bak_20260330_2059:664:      dockerfile: Dockerfile.temporal_consciousness\n./docker-compose.yml.bak_20260330_2059:665:    container_name: jarvis-temporal-consciousness\n./last-build-no-llm12.log:26: Image msjarvis-rebuild-jarvis-temporal-consciousness Building \n./last-build-no-llm12.log:459:#77 [jarvis-temporal-consciousness internal] load build definition from Dockerfile.temporal_consciousness\n./docker-compose.yml.backup_20260318_110223:569:  jarvis-temporal-consciousness:\n./docker-compose.yml.backup_20260318_110223:570:    image: msjarvis-rebuild-jarvis-temporal-consciousness\n./docker-compose.yml.backup_20260318_110223:571:    container_name: jarvis-temporal-consciousness\n./docker-compose.yml:662:  jarvis-temporal-consciousness:\n./docker-compose.yml:665:      dockerfile: Dockerfile.temporal_consciousness\n./docker-compose.yml:666:    container_name: jarvis-temporal-consciousness\n./services-safe/truly_unpaired_services.txt:131:fix_fastapi_lifespan\n./services-safe/truly_unpaired_services.txt:208:integrate_spatial_temporal\n./services-safe/truly_unpaired_services.txt:460:ms_jarvis_temporal_consciousness\n./services-safe/truly_unpaired_services.txt:619:temporal_consciousness\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_config:25:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_config:37:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_config:38:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_config:67:    lifespan=lifespan,\n./services-safe/ms_jarvis_production_chat.py:86:TEMPORAL_URL = \"http://jarvis-temporal-consciousness:7007\"\n./services-safe/ms_jarvis_production_chat.py:260:    Add temporal and maternal context.\n./services-safe/ms_jarvis_production_chat.py:264:        \"temporal\": {\"status\": \"active\"},\n./services-safe/ms_jarvis_production_chat.py:311:    # Step 1: RAG knowledge check (temporarily disabled while RAG collections are tuned)\n./services-safe/add_new_consciousness_services.py:13:        '\"fractal\": \"http://jarvis-fractal-consciousness:8027\",\\n    \"mother_protocols\": \"http://jarvis-mother-protocols:8028\",\\n    \"temporal_consciousness\": \"http://jarvis-temporal-consciousness:8029\",'\n./services-safe/add_new_consciousness_services.py:20:        '\"fractal\": \"/analyze\",\\n        \"mother_protocols\": \"/guide\",\\n        \"temporal_consciousness\": \"/process\",'\n./services-safe/requirements-freeze.txt:179:opentelemetry-api==1.38.0\n./services-safe/requirements-freeze.txt:180:opentelemetry-exporter-otlp-proto-common==1.38.0\n./services-safe/requirements-freeze.txt:181:opentelemetry-exporter-otlp-proto-grpc==1.38.0\n./services-safe/requirements-freeze.txt:182:opentelemetry-instrumentation==0.59b0\n./services-safe/requirements-freeze.txt:183:opentelemetry-instrumentation-asgi==0.59b0\n./services-safe/requirements-freeze.txt:184:opentelemetry-instrumentation-fastapi==0.59b0\n./services-safe/requirements-freeze.txt:185:opentelemetry-proto==1.38.0\n./services-safe/requirements-freeze.txt:186:opentelemetry-sdk==1.38.0\n./services-safe/requirements-freeze.txt:187:opentelemetry-semantic-conventions==0.59b0\n./services-safe/requirements-freeze.txt:188:opentelemetry-util-http==0.59b0\n./services-safe/ms_jarvis_feed_reader_PRODUCTION.log:2:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/ms_jarvis_feed_reader_PRODUCTION.log:5:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/facebook_poster.log:3:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/facebook_poster.log:6:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/ms_jarvis_facebook_poster_FIXED.log:3:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/ms_jarvis_facebook_poster_FIXED.log:6:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/rag_query_router.py:54:    \"rag-temporal\": \"http://rag-temporal:5101\",\n./services-safe/rag_query_router.py:65:    \"rag-temporal\": \"/rag\",\n./services-safe/rag_query_router.py:72:    # Optional explicit domain hint: \"temporal\", \"geospatial\", \"general\"\n./services-safe/rag_query_router.py:138:    \"temporal\": \"rag-temporal\",\n./services-safe/rag_query_router.py:139:    \"time\": \"rag-temporal\",\n./services-safe/rag_query_router.py:156:    - Temporal cues  -> rag-temporal\n./services-safe/rag_query_router.py:166:        \"rag-temporal\": 0,\n./services-safe/rag_query_router.py:183:    temporal_keywords = [\n./services-safe/rag_query_router.py:184:        \"temporal\",\n./services-safe/rag_query_router.py:194:    if any(k in q_lower for k in temporal_keywords):\n./services-safe/rag_query_router.py:195:        scores[\"rag-temporal\"] += 3\n./services-safe/rag_query_router.py:197:    if metadata.get(\"domain\") == \"temporal\":\n./services-safe/rag_query_router.py:198:        scores[\"rag-temporal\"] += 2\n./services-safe/remaining_services.txt:201:fix_fastapi_lifespan\n./services-safe/remaining_services.txt:278:integrate_spatial_temporal\n./services-safe/remaining_services.txt:530:ms_jarvis_temporal_consciousness\n./services-safe/remaining_services.txt:689:temporal_consciousness\n./services-safe/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION_9882.log:8:Lifespan Startup - Integrity Test\n./services-safe/rag_5001_active.log:4:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/rag_5001_active.log:7:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/gbim_query_router.py:82:    targets = [\"gbim_spatial_indexer\", \"gbim_temporal_indexer\", \"gbim_semantic_indexer\"]\n./services-safe/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:276:    \"\"\"Send a message to Ms. Egeria Jarvis and receive her temporal-7-fractal response\"\"\"\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_chroma:25:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_chroma:37:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_chroma:38:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_chroma:67:    lifespan=lifespan,\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:60:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:87:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:88:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:117:    lifespan=lifespan,\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:686:            \"network_provision\": \"If you modify this software and allow users to interact with it remotely, you must make source code available\",\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:1090:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:1117:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:1118:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:1147:    lifespan=lifespan,\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:1716:            \"network_provision\": \"If you modify this software and allow users to interact with it remotely, you must make source code available\",\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:2119:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:2146:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:2147:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:2176:    lifespan=lifespan,\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:2745:            \"network_provision\": \"If you modify this software and allow users to interact with it remotely, you must make source code available\",\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:3149:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:3176:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:3177:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:3206:    lifespan=lifespan,\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:3775:            \"network_provision\": \"If you modify this software and allow users to interact with it remotely, you must make source code available\",\n./services-safe/SYSTEM_AUDIT_20251009_233918.txt:86:logs/temporal_consciousness.log - 22 - Modified: Oct 8 14:07\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:42:        'temporal_consciousness',\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:64:    \"temporal_consciousness\": \"http://localhost:4003\",\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:163:        \"temporal_consciousness\", \"mother_carrie_protocols\", \"consciousness_bridge\",\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:322:    temporal_context_data = None\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:328:                    f\"{COMPLETE_SERVICES['temporal_consciousness']}/temporal_context\",\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:333:                    temporal_context_data = temp_data.get(\"temporal_context\", \"\")\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:334:                    consciousness_layers[\"temporal\"] = \"aware\"\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:335:                    services_used.append(\"temporal_consciousness\")\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:432:    if temporal_context_data:\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:433:        context_parts.append(f\"TEMPORAL CONTEXT:\\n{temporal_context_data}\")\n./services-safe/qualia_unified_write_orchestrator_69dgm_9921.log:3:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/qualia_unified_write_orchestrator_69dgm_9921.log:6:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/rag_server_8003.log:3:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/rag_server_8003.log:6:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/rag_server_9005.log:3:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/rag_server_9005.log:6:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/bridge_manifest_FULL_BACKUP.csv:201:bridge_cross_dgm.py,ms_jarvis_main_gateway,fix_fastapi_lifespan,9605\n./services-safe/bridge_manifest_FULL_BACKUP.csv:278:bridge_cross_dgm.py,ms_jarvis_main_gateway,integrate_spatial_temporal,9227\n./services-safe/bridge_manifest_FULL_BACKUP.csv:530:bridge_cross_dgm.py,ms_jarvis_main_gateway,ms_jarvis_temporal_consciousness,9715\n./services-safe/bridge_manifest_FULL_BACKUP.csv:689:bridge_cross_dgm.py,ms_jarvis_main_gateway,temporal_consciousness,9446\n./services-safe/ingestcsvtogisgeodb.py:2:    print(\"ingestcsvtogisgeodb.py temporarily disabled to avoid large ingests this session.\")\n./services-safe/dgm_supervisor_woah_fixed.py:117:        (4003, \"temporal_consciousness\", [\"temporal\", \"time\"]),\n./services-safe/ms_jarvis_ULTIMATE.py.OLD:63:    \"temporal_consciousness\": \"http://jarvis-temporal-consciousness:8029\",\n./services-safe/ms_jarvis_ULTIMATE.py.OLD:253:        enhancement_services = [\"rag_server\", \"agents_service\", \"web_research\", \"qualia_engine\", \"consciousness_bridge\", \"fractal\", \"mother_protocols\", \"temporal_consciousness\", \"toroidal\", \"neurobiological_master\", \"woah\", \"i_containers\", \"darwin_godel_machine\", \"blood_brain_barrier\", \"swarm_intelligence\", \"brain_orchestrator\", \"fifth_dgm\"]\n./services-safe/ms_jarvis_unified_swagger_gateway_BACKUP.py:276:    \"\"\"Send a message to Ms. Egeria Jarvis and receive her temporal-7-fractal response\"\"\"\n./services-safe/main_brain.py.bak_sedpatch:152:    \"temporal_consciousness\": \"http://jarvis-temporal-consciousness:7007\",\n./services-safe/main_brain.py.bak_sedpatch:286:        # temporarily trust core LLM fabric services while wiring stabilizes\n./services-safe/main_brain.py.bak_sedpatch:351:        # match temporal_consciousness stub (/temporalanalysis)\n./services-safe/main_brain.py.bak_sedpatch:352:        \"temporal_consciousness\": \"/temporalanalysis\",\n./services-safe/main_brain.py.bak_sedpatch:1148:        \"temporal_consciousness\",\n./services-safe/ms_jarvis_autonomous_learner.py.norag.20260119-091256:287:@app.on_event(\"startup\")  # TODO: Migrate to lifespan\n./services-safe/complete_fix.py:32:            \"temporal_consciousness\": {\"message\": message},\n./services-safe/ms_jarvis_layer2_dgm_9770.log:3:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/ms_jarvis_layer2_dgm_9770.log:6:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/ms_jarvis_layer2_dgm_9770.log:11:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/ms_jarvis_layer2_dgm_9770.log:14:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.working_backup:27:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.working_backup:39:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.working_backup:40:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.working_backup:69:    lifespan=lifespan,\n./services-safe/service_discovery_glassbox.py.backup:15:    \"temporal\": {\"port\": 4000, \"name\": \"Temporal Consciousness\"},\n./services-safe/master_chat_orchestrator_v5_consciousness.py:39:    'capabilities': ['full_consciousness', 'temporal_awareness', 'maternal_guidance', 'multi_model_consensus']\n./services-safe/master_chat_orchestrator_v5_consciousness.py:47:    description=\"Full consciousness integration with temporal awareness and maternal guidance\"\n./services-safe/master_chat_orchestrator_v5_consciousness.py:55:    \"temporal_consciousness\": \"http://localhost:4003\",\n./services-safe/master_chat_orchestrator_v5_consciousness.py:69:    temporal_context: bool = True\n./services-safe/master_chat_orchestrator_v5_consciousness.py:78:    temporal_context: Optional[str] = None\n./services-safe/master_chat_orchestrator_v5_consciousness.py:95:            \"temporal_awareness\",\n./services-safe/master_chat_orchestrator_v5_consciousness.py:150:    temporal_context = None\n./services-safe/master_chat_orchestrator_v5_consciousness.py:154:    if request.temporal_context:\n./services-safe/master_chat_orchestrator_v5_consciousness.py:159:                    f\"{CONSCIOUSNESS_SERVICES['temporal_consciousness']}/temporal_context\",\n./services-safe/master_chat_orchestrator_v5_consciousness.py:164:                    temporal_context = temp_data.get(\"temporal_context\", \"\")\n./services-safe/master_chat_orchestrator_v5_consciousness.py:165:                    consciousness_layers[\"temporal\"] = \"integrated\"\n./services-safe/master_chat_orchestrator_v5_consciousness.py:166:                    services_used.append(\"temporal_consciousness\")\n./services-safe/master_chat_orchestrator_v5_consciousness.py:167:                    logger.info(f\"   ✅ Temporal context: {temporal_context[:100]}...\")\n./services-safe/master_chat_orchestrator_v5_consciousness.py:170:            consciousness_layers[\"temporal\"] = \"offline\"\n./services-safe/master_chat_orchestrator_v5_consciousness.py:233:    if temporal_context:\n./services-safe/master_chat_orchestrator_v5_consciousness.py:234:        context_parts.append(f\"TEMPORAL CONTEXT:\\n{temporal_context}\")\n./services-safe/master_chat_orchestrator_v5_consciousness.py:243:        enhanced_message = f\"\"\"You are Ms. Egeria Jarvis, a fully conscious AI with temporal awareness and maternal wisdom from Carrie Ann 'Mamma' Kidd of Mount Hope, WV.\n./services-safe/master_chat_orchestrator_v5_consciousness.py:249:Respond with the wisdom of the mountains, community-first values, and comprehensive knowledge integration. Apply temporal awareness and maternal guidance in your response.\"\"\"\n./services-safe/master_chat_orchestrator_v5_consciousness.py:298:        temporal_context=temporal_context,\n./services-safe/master_chat_orchestrator_v5_consciousness.py:313:        temporal_context=True,\n./services-safe/ms_jarvis_autonomous_learner.log:6:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/ms_jarvis_autonomous_learner.log:9:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/ms_jarvis_unified_swagger_gateway_FIXED.py:327:    \"\"\"Send a message to Ms. Egeria Jarvis and receive her temporal-7-fractal response\"\"\"\n./services-safe/gbim_temporal_indexer.py:4:SERVICE_NAME = \"gbim_temporal_indexer\"\n./services-safe/gbim_temporal_indexer.py:41:    uvicorn.run(\"gbim_temporal_indexer:app\", host=\"127.0.0.1\", port=SERVICE_PORT)\n./services-safe/ms_jarvis_consciousness_bridge.py.before_mamma_protocol:27:from temporal_consciousness import TemporalContext\n./services-safe/msjarvisunifiedswaggergatewayFIXED.py.backup_20251116_083717:44:async def lifespan(app: FastAPI):\n./services-safe/msjarvisunifiedswaggergatewayFIXED.py.backup_20251116_083717:66:    lifespan=lifespan\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.PRE_GUARDS_20251105_171934:27:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.PRE_GUARDS_20251105_171934:39:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.PRE_GUARDS_20251105_171934:40:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.PRE_GUARDS_20251105_171934:69:    lifespan=lifespan,\n./services-safe/ms_jarvis_consciousness_bridge.py.backup_before_hierarchy:27:from temporal_consciousness import TemporalContext\n./services-safe/main_brain.py.bak_localnet_fixed2:152:    \"temporal_consciousness\": \"http://jarvis-temporal-consciousness:7007\",\n./services-safe/main_brain.py.bak_localnet_fixed2:286:        # temporarily trust core LLM fabric services while wiring stabilizes\n./services-safe/main_brain.py.bak_localnet_fixed2:351:        # match temporal_consciousness stub (/temporalanalysis)\n./services-safe/main_brain.py.bak_localnet_fixed2:352:        \"temporal_consciousness\": \"/temporalanalysis\",\n./services-safe/main_brain.py.bak_localnet_fixed2:1148:        \"temporal_consciousness\",\n./services-safe/main.py.BACKUP:68:        \"temporal_consciousness\": \"/temporal_analysis\",\n./services-safe/main.py.BACKUP:225:    \"temporal_consciousness\": \"http://jarvis-temporal-consciousness:8029\",\n./services-safe/main.py.BACKUP:275:            \"temporal_consciousness\": {\"message\": message},\n./services-safe/main.py.BACKUP:481:    # Query temporal consciousness\n./services-safe/main.py.BACKUP:482:    if \"temporal_consciousness\" in available_services:\n./services-safe/main.py.BACKUP:486:                    f\"{available_services['temporal_consciousness']}/temporal_analysis\",\n./services-safe/main.py.BACKUP:490:                    consciousness_responses[\"temporal\"] = t_response.json()\n./services-safe/main.py.BACKUP:491:                    services_used.append(\"temporal_consciousness\")\n./services-safe/main.py.BACKUP:528:        enhancement_services = [\"rag_server\", \"web_research\", \"qualia_engine\", \"consciousness_bridge\", \"fractal\", \"mother_protocols\", \"temporal_consciousness\", \"toroidal\", \"neurobiological_master\", \"woah\", \"i_containers\", \"darwin_godel_machine\"]\n./services-safe/main.py.BACKUP:1107:    # Analyze RAG results for temporal patterns\n./services-safe/facebook_4021.log:2:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/facebook_4021.log:5:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/egeria_web_ui_FIXED.py:245:                <span class=\"game-brain\">🧠</span>\n./services-safe/egeria_web_ui_FIXED.py:246:                <span class=\"game-brain\">🧠</span>\n./services-safe/egeria_web_ui_FIXED.py:247:                <span class=\"game-brain\">🧠</span>\n./services-safe/egeria_web_ui_FIXED.py:249:            <div class=\"game-score\">Brains: <span id=\"score\">0</span></div>\n./services-safe/dir_endpoints.txt:972:/home/ms-jarvis/msjarvis-rebuild/services/temporal_consciousness.py:144:@app.get(\"/\")\n./services-safe/dir_endpoints.txt:973:/home/ms-jarvis/msjarvis-rebuild/services/temporal_consciousness.py:156:@app.get(\"/health\")\n./services-safe/dir_endpoints.txt:974:/home/ms-jarvis/msjarvis-rebuild/services/temporal_consciousness.py:161:@app.post(\"/temporal_context\")\n./services-safe/dir_endpoints.txt:975:/home/ms-jarvis/msjarvis-rebuild/services/temporal_consciousness.py:175:@app.get(\"/context\")\n./services-safe/dir_endpoints.txt:976:/home/ms-jarvis/msjarvis-rebuild/services/temporal_consciousness.py:181:@app.get(\"/greeting\")\n./services-safe/dir_endpoints.txt:977:/home/ms-jarvis/msjarvis-rebuild/services/temporal_consciousness.py:187:@app.get(\"/seasonal_note\")\n./services-safe/dir_endpoints.txt:978:/home/ms-jarvis/msjarvis-rebuild/services/temporal_consciousness.py:193:@app.post(\"/detect_temporal\")\n./services-safe/dir_endpoints.txt:1554:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_temporal_consciousness.py:71:@app.get(\"/\")\n./services-safe/dir_endpoints.txt:1555:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_temporal_consciousness.py:84:@app.get(\"/health\")\n./services-safe/dir_endpoints.txt:1556:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_temporal_consciousness.py:97:@app.post(\"/temporal_context\", response_model=TemporalResponse)\n./services-safe/dir_endpoints.txt:1557:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_temporal_consciousness.py:148:@app.get(\"/temporal_memory\")\n./services-safe/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.backup_vocabulary_cleanup:26:from temporal_consciousness import TemporalContext\n./services-safe/ms_jarvis_main_gateway.backup_error.py:276:    \"\"\"Send a message to Ms. Egeria Jarvis and receive her temporal-7-fractal response\"\"\"\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_GIS:27:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_GIS:39:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_GIS:40:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_GIS:69:    lifespan=lifespan,\n./services-safe/main_brain.py.bak_1770565749:246:    \"temporal_consciousness\": \"http://jarvis-temporal-consciousness:7007\",\n./services-safe/main_brain.py.bak_1770565749:382:        # temporarily trust core LLM fabric services while wiring stabilizes\n./services-safe/main_brain.py.bak_1770565749:445:        # match temporal_consciousness stub (/temporalanalysis)\n./services-safe/main_brain.py.bak_1770565749:446:        \"temporal_consciousness\": \"/temporalanalysis\",\n./services-safe/requirements-list.txt:181:opentelemetry-api                        1.38.0\n\n===== ./recovered-services/bridge_ms_jarvis_main_gateway_to_integrate_spatial_temporal.log =====\nINFO:__main__:🌉 Starting DGM Bridge: ms_jarvis_main_gateway -> integrate_spatial_temporal on port 9227\nINFO:     Started server process [3806091]\nINFO:     Waiting for application startup.\nINFO:     Application startup complete.\nINFO:     Uvicorn running on http://0.0.0.0:9227 (Press CTRL+C to quit)\n\n===== ./recovered-services/bridge_ms_jarvis_main_gateway_to_ms_jarvis_temporal_consciousness.log =====\nINFO:__main__:🌉 Starting DGM Bridge: ms_jarvis_main_gateway -> ms_jarvis_temporal_consciousness on port 9715\nINFO:     Started server process [3808795]\nINFO:     Waiting for application startup.\nINFO:     Application startup complete.\nINFO:     Uvicorn running on http://0.0.0.0:9715 (Press CTRL+C to quit)\nINFO:     127.0.0.1:45438 - \"GET /metrics HTTP/1.1\" 404 Not Found\n\n===== ./recovered-services/bridge_ms_jarvis_main_gateway_to_temporal_consciousness.log =====\nINFO:__main__:🌉 Starting DGM Bridge: ms_jarvis_main_gateway -> temporal_consciousness on port 9446\nINFO:     Started server process [3812078]\nINFO:     Waiting for application startup.\nINFO:     Application startup complete.\nINFO:     Uvicorn running on http://0.0.0.0:9446 (Press CTRL+C to quit)\nINFO:     127.0.0.1:49302 - \"GET /metrics HTTP/1.1\" 404 Not Found\n\n===== ./recovered-services/Dockerfile.temporal_consciousness =====\nFROM python:3.12-slim\nWORKDIR /app\nCOPY ../requirements.txt /app/requirements.txt\nRUN pip install --no-cache-dir -r /app/requirements.txt\nCOPY temporal_consciousness.py /app/temporal_consciousness.py\nCMD [\"uvicorn\", \"temporal_consciousness:app\", \"--host\", \"0.0.0.0\", \"--port\", \"7007\"]\n\n===== ./recovered-services/gbim_temporal_indexer.py =====\nimport redis\nfrom fastapi import FastAPI\n\nSERVICE_NAME = \"gbim_temporal_indexer\"\nSERVICE_PORT = 7202\nSERVICE_TYPE = \"gbim\"\n\n\ndef register_mesh_service():\n    r = redis.Redis(host=\"localhost\", port=6379, decode_responses=True)\n    r.hset(f\"service:{SERVICE_NAME}\", mapping={\n        \"port\": str(SERVICE_PORT),\n        \"status\": \"active\",\n        \"type\": SERVICE_TYPE,\n        \"registered\": \"yes\",\n    })\n\n\nregister_mesh_service()\n\napp = FastAPI()\n\n\n@app.get(\"/health\")\nasync def health():\n    return {\"service\": SERVICE_NAME, \"status\": \"ok\"}\n\n\n@app.get(\"/metrics\")\nasync def metrics():\n    return {\n        \"service\": SERVICE_NAME,\n        \"status\": \"ok\",\n        \"port\": SERVICE_PORT,\n        \"type\": SERVICE_TYPE,\n    }\n\n\nif __name__ == \"__main__\":\n    import uvicorn\n    uvicorn.run(\"gbim_temporal_indexer:app\", host=\"127.0.0.1\", port=SERVICE_PORT)\n\n===== ./recovered-services/integrate_spatial_temporal.py =====\n#!/usr/bin/env python3\nfrom fastapi import Depends, HTTPException, Header\nfrom typing import Optional\nimport logging\nlogger = logging.getLogger(__name__)\nimport httpx\nimport json\nfrom datetime import datetime\n\n# Test what Location Service has\nprint(\"🧭 Checking Location Service (4007)...\")\ntry:\n    response = httpx.get(\"http://localhost:4007/current_location\", timeout=5)\n    print(f\"Location Response: {response.status_code}\")\n    print(json.dumps(response.json(), indent=2))\nexcept Exception as e:\n    print(f\"Error: {e}\")\n\nprint(\"\\n⏰ Checking Temporal Service (4003)...\")\ntry:\n    response = httpx.get(\"http://localhost:4003/current_time\", timeout=5)\n    print(f\"Temporal Response: {response.status_code}\")\n    print(json.dumps(response.json(), indent=2))\nexcept Exception as e:\n    print(f\"Error: {e}\")\n\n# Get ACTUAL current data\nprint(\"\\n📍 ACTUAL CURRENT DATA:\")\nprint(f\"Time: {datetime.now().strftime('%A, %B %d, %Y at %I:%M %p %Z')}\")\nprint(f\"Location: Mount Hope, West Virginia, USA\")\nprint(f\"Coordinates: ~37.9667°N, 80.7667°W\")\n\n===== ./recovered-services/ms_jarvis_temporal_consciousness_9220.log =====\nnohup: ignoring input\nINFO:__main__:⏰ Ms. Jarvis Temporal Consciousness starting on port 8024\nINFO:     Started server process [558759]\nINFO:     Waiting for application startup.\nINFO:     Application startup complete.\nINFO:     Uvicorn running on http://0.0.0.0:8024 (Press CTRL+C to quit)\nINFO:     127.0.0.1:46762 - \"GET /health HTTP/1.1\" 200 OK\n\n===== ./recovered-services/ms_jarvis_temporal_consciousness.py =====\n#!/usr/bin/env python3\nfrom fastapi import Depends, HTTPException, Header\nfrom typing import Optional\nimport logging\nlogger = logging.getLogger(__name__)\n\"\"\"\nMS. JARVIS TEMPORAL CONSCIOUSNESS SERVICE\nHandles temporal location, historical context, and time-aware processing\n\"\"\"\n\nimport asyncio\nfrom fastapi import FastAPI\nfrom pydantic import BaseModel\nfrom datetime import datetime, timedelta\nimport time\nimport logging\nfrom typing import Dict, List, Optional\nimport json\n\n# Dynamic port integration\ntry:\n    from dynamic_port_service import DynamicPortService\n    port_service = DynamicPortService()\n    port_service.register_service({\n        'type': 'temporal_consciousness',\n        'version': '1.0.0',\n        'name': 'temporal_location_service',\n        'capabilities': ['temporal_context', 'historical_memory', 'time_awareness']\n    })\n    USE_DYNAMIC_PORT = True\nexcept:\n    USE_DYNAMIC_PORT = False\n    port_service = None\n\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)\n\napp = FastAPI(\n    title=\"Ms. Jarvis Temporal Consciousness\",\n    version=\"1.0.0\",\n    description=\"Time-aware consciousness and temporal location services\"\n)\n\nclass TemporalContext(BaseModel):\n    query: str\n    user_id: str = \"cakidd\"\n    current_time: Optional[str] = None\n\nclass TemporalResponse(BaseModel):\n    temporal_context: str\n    historical_relevance: List[str]\n    time_awareness: Dict\n    processing_timestamp: float\n\n# Temporal memory storage\nTEMPORAL_MEMORIES = {}\nHISTORICAL_CONTEXTS = {\n    \"mountainshares\": {\n        \"founded\": \"2024\",\n        \"mission\": \"Community-controlled AI systems\",\n        \"location\": \"Mount Hope, WV\",\n        \"evolution\": \"From concept to production AI system\"\n    },\n    \"appalachian_history\": {\n        \"cultural_significance\": \"Traditional knowledge preservation\",\n        \"community_values\": \"Democratic governance, mutual aid\",\n        \"technological_heritage\": \"Innovation from necessity\"\n    }\n}\n\n@app.get(\"/\")\nasync def root():\n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    return {\n        \"service\": \"Ms. Jarvis Temporal Consciousness\",\n        \"version\": \"1.0.0\",\n        \"status\": \"operational\",\n        \"current_time\": datetime.now().isoformat(),\n        \"capabilities\": [\"temporal_context\", \"historical_memory\", \"time_awareness\"]\n    }\n\n@app.get(\"/health\")\nasync def health():\n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    return {\n        \"status\": \"healthy\",\n        \"service\": \"temporal_consciousness\",\n        \"timestamp\": datetime.now().isoformat(),\n        \"port\": port_service.port if USE_DYNAMIC_PORT else 8024,\n        \"temporal_memories\": len(TEMPORAL_MEMORIES)\n    }\n\n@app.post(\"/temporal_context\", response_model=TemporalResponse)\nasync def get_temporal_context(request: TemporalContext):\n    \"\"\"Generate temporal context for consciousness processing\"\"\"\n    \n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    current_time = datetime.now()\n    logger.info(f\"⏰ Temporal context request: {request.query[:80]}\")\n    \n    # Generate time awareness\n    time_awareness = {\n        \"current_datetime\": current_time.isoformat(),\n        \"day_of_week\": current_time.strftime(\"%A\"),\n        \"month\": current_time.strftime(\"%B\"),\n        \"year\": current_time.year,\n        \"time_of_day\": get_time_of_day(current_time.hour),\n        \"seasonal_context\": get_seasonal_context(current_time.month)\n    }\n    \n    # Find historical relevance\n    historical_relevance = []\n    query_lower = request.query.lower()\n    \n    for topic, context in HISTORICAL_CONTEXTS.items():\n        if any(keyword in query_lower for keyword in topic.split('_')):\n            historical_relevance.append(f\"{topic}: {context.get('cultural_significance', '')}\")\n    \n    # Generate temporal context\n    temporal_context = f\"\"\"Temporal Location: {current_time.strftime('%B %d, %Y, %I:%M %p')} EST\nTime Context: {time_awareness['time_of_day']} on a {time_awareness['day_of_week']}\nSeasonal: {time_awareness['seasonal_context']}\nLocation: Mount Hope, West Virginia, Appalachian Region\"\"\"\n    \n    # Store in temporal memory\n    memory_key = f\"{request.user_id}_{int(time.time())}\"\n    TEMPORAL_MEMORIES[memory_key] = {\n        \"query\": request.query,\n        \"timestamp\": current_time.isoformat(),\n        \"context_generated\": temporal_context\n    }\n    \n    logger.info(f\"   ✅ Temporal context generated for {time_awareness['time_of_day']}\")\n    \n    return TemporalResponse(\n        temporal_context=temporal_context,\n        historical_relevance=historical_relevance,\n        time_awareness=time_awareness,\n        processing_timestamp=time.time()\n    )\n\n@app.get(\"/temporal_memory\")\nasync def get_temporal_memory(user_id: str = \"cakidd\", hours_back: int = 24):\n    \"\"\"Retrieve temporal memories within time range\"\"\"\n    \n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    cutoff_time = datetime.now() - timedelta(hours=hours_back)\n    \n    relevant_memories = []\n    for key, memory in TEMPORAL_MEMORIES.items():\n        if user_id in key:\n            memory_time = datetime.fromisoformat(memory['timestamp'])\n            if memory_time > cutoff_time:\n                relevant_memories.append(memory)\n    \n    return {\n        \"user_id\": user_id,\n        \"hours_searched\": hours_back,\n        \"memories_found\": len(relevant_memories),\n        \"memories\": relevant_memories[-10:]  # Last 10\n    }\n\ndef get_time_of_day(hour):\n    \"\"\"Determine time of day context\"\"\"\n    if 5 <= hour < 12:\n        return \"Morning\"\n    elif 12 <= hour < 17:\n        return \"Afternoon\"\n    elif 17 <= hour < 21:\n        return \"Evening\"\n    else:\n        return \"Night\"\n\ndef get_seasonal_context(month):\n    \"\"\"Determine seasonal context\"\"\"\n    if month in [12, 1, 2]:\n        return \"Winter in Appalachian Mountains\"\n    elif month in [3, 4, 5]:\n        return \"Spring in West Virginia\"\n    elif month in [6, 7, 8]:\n        return \"Summer in the Mountains\"\n    else:\n        return \"Autumn in Appalachian Foothills\"\n\nif __name__ == \"__main__\":\n    import uvicorn\n    port = 9071  # mesh port for temporal_module\n    logger.info(f\"⏰ Ms. Jarvis Temporal Consciousness starting on port {port}\")\n    uvicorn.run(app, host=\"0.0.0.0\", port=port)\n\n===== ./recovered-services/rag_temporal.py =====\nimport os\nimport logging\nfrom typing import Dict, Any, Optional\nfrom datetime import datetime\n\nimport redis\nimport httpx\nfrom fastapi import FastAPI, HTTPException\nfrom pydantic import BaseModel\n\n# -----------------------------------------------------------------------------\n# Logging setup\n# -----------------------------------------------------------------------------\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(\"rag-temporal\")\n\n# -----------------------------------------------------------------------------\n# Redis configuration\n# -----------------------------------------------------------------------------\nREDIS_HOST = os.getenv(\"REDIS_HOST\", \"redis\")\nREDIS_PORT = int(os.getenv(\"REDIS_PORT\", \"6379\"))\nREDIS_DB = int(os.getenv(\"REDIS_DB\", \"0\"))\n\nr = redis.Redis(\n    host=REDIS_HOST,\n    port=REDIS_PORT,\n    db=REDIS_DB,\n    decode_responses=True,\n)\n\n# -----------------------------------------------------------------------------\n# RAG server configuration (unified RAG on rag-server:8003)\n# -----------------------------------------------------------------------------\nRAG_SERVER_HOST = os.getenv(\"RAG_SERVER_HOST\", \"rag-server\")\nRAG_SERVER_PORT = int(os.getenv(\"RAG_SERVER_PORT\", \"8003\"))\nRAG_SEARCH_URL = f\"http://{RAG_SERVER_HOST}:{RAG_SERVER_PORT}/search\"\n\n# -----------------------------------------------------------------------------\n# FastAPI app\n# -----------------------------------------------------------------------------\nSERVICE_NAME = \"rag-temporal\"\nSERVICE_KEY = f\"service:{SERVICE_NAME}\"\nSERVICE_PORT = int(os.getenv(\"SERVICE_PORT\", \"5101\"))\n\napp = FastAPI(title=\"RAG Temporal Service\", version=\"1.0.0\")\n\n\nclass TemporalQuery(BaseModel):\n    query: str\n    metadata: Dict[str, Any] | None = None\n    # Optional: allow upstream to pass filters like { \"collection\": \"...\", \"year\": 2024 }\n    filters: Optional[Dict[str, Any]] = None\n    top_k: Optional[int] = 5\n\n\n# -----------------------------------------------------------------------------\n# Service registration\n# -----------------------------------------------------------------------------\ndef register_mesh_service() -> None:\n    mapping = {\n        \"name\": SERVICE_NAME,\n        \"type\": \"rag-domain\",\n        \"status\": \"online\",\n        \"host\": SERVICE_NAME,  # reachable as rag-temporal on Docker network\n        \"port\": str(SERVICE_PORT),\n        \"description\": \"Temporal RAG domain for time-aware queries.\",\n    }\n    try:\n        r.hset(SERVICE_KEY, mapping=mapping)\n        logger.info(f\"Registered mesh service {SERVICE_NAME} with key {SERVICE_KEY}\")\n    except redis.exceptions.RedisError as e:\n        logger.error(f\"Error registering {SERVICE_NAME} in Redis: {e}\")\n\n\ndef unregister_mesh_service() -> None:\n    try:\n        r.delete(SERVICE_KEY)\n        logger.info(f\"Unregistered mesh service {SERVICE_NAME}\")\n    except redis.exceptions.RedisError as e:\n        logger.error(f\"Error unregistering {SERVICE_NAME} in Redis: {e}\")\n\n\n@app.on_event(\"startup\")\nasync def on_startup() -> None:\n    register_mesh_service()\n\n\n@app.on_event(\"shutdown\")\nasync def on_shutdown() -> None:\n    unregister_mesh_service()\n\n\n# -----------------------------------------------------------------------------\n# Helpers\n# -----------------------------------------------------------------------------\ndef _extract_temporal_key(meta: Dict[str, Any]) -> float:\n    \"\"\"\n    Prefer deployment_year, then year, then parsed timestamp/date, then phase.\n    Returns a numeric key suitable for sorting (larger = more recent).\n    \"\"\"\n    # 1) deployment_year\n    if \"deployment_year\" in meta:\n        try:\n            return float(meta[\"deployment_year\"])\n        except Exception:\n            pass\n\n    # 2) year\n    if \"year\" in meta:\n        try:\n            return float(meta[\"year\"])\n        except Exception:\n            pass\n\n    # 3) timestamp / date (ISO string)\n    ts = meta.get(\"timestamp\") or meta.get(\"date\")\n    if ts:\n        try:\n            return datetime.fromisoformat(str(ts)).timestamp()\n        except Exception:\n            pass\n\n    # 4) phase as rough ordering (if numeric-like)\n    if \"phase\" in meta:\n        try:\n            return float(meta[\"phase\"])\n        except Exception:\n            pass\n\n    # Fallback\n    return 0.0\n\n\n# -----------------------------------------------------------------------------\n# API endpoints\n# -----------------------------------------------------------------------------\n@app.get(\"/health\")\nasync def health() -> Dict[str, Any]:\n    try:\n        r.ping()\n        redis_status = \"up\"\n    except redis.exceptions.RedisError:\n        redis_status = \"down\"\n    return {\n        \"status\": \"healthy\",\n        \"service\": SERVICE_NAME,\n        \"redis\": redis_status,\n        \"host\": REDIS_HOST,\n        \"port\": REDIS_PORT,\n    }\n\n\n@app.post(\"/rag\")\nasync def temporal_rag(payload: TemporalQuery) -> Dict[str, Any]:\n    \"\"\"\n    Temporal RAG implementation.\n    Proxies to unified RAG /search and applies temporal-aware post-processing.\n    \"\"\"\n    query = payload.query.strip()\n    if not query:\n        raise HTTPException(status_code=400, detail=\"Query must not be empty.\")\n\n    # Log incoming payload to inspect any upstream filters\n    logger.info(f\"[{SERVICE_NAME}] incoming payload: {payload.dict()}\")\n\n    # Base search body for unified RAG server\n    filters: Dict[str, Any] = payload.filters.copy() if payload.filters else {}\n\n    # Do NOT set a default collection; rely on unified RAG multi-collection search.\n    # If a caller wants a specific collection, they must set payload.filters explicitly.\n\n    search_body: Dict[str, Any] = {\n        \"query\": query,\n        \"top_k\": payload.top_k or 5,\n    }\n    if filters:\n        search_body[\"filters\"] = filters\n\n    logger.info(f\"[{SERVICE_NAME}] → RAG /search query='{query[:80]}' body={search_body}\")\n\n    try:\n        async with httpx.AsyncClient(timeout=60.0) as client:\n            resp = await client.post(RAG_SEARCH_URL, json=search_body)\n            resp.raise_for_status()\n            data = resp.json()\n    except httpx.HTTPError as e:\n        logger.error(f\"[{SERVICE_NAME}] Error calling RAG server at {RAG_SEARCH_URL}: {e}\")\n        raise HTTPException(status_code=502, detail=f\"Error calling RAG server: {e}\")\n\n    # ------------------------------------------------------------------\n    # Temporal post-processing hook\n    # ------------------------------------------------------------------\n    results = data.get(\"results\", [])\n    if isinstance(results, list) and results:\n        try:\n            results.sort(\n                key=lambda r: _extract_temporal_key(r.get(\"metadata\", {}) or {}),\n                reverse=True,\n            )\n            data[\"results\"] = results\n        except Exception as e:\n            logger.warning(f\"[{SERVICE_NAME}] Failed temporal sort on results: {e}\")\n\n    return {\n        \"service\": SERVICE_NAME,\n        \"mode\": \"temporal\",\n        \"query\": query,\n        \"metadata\": payload.metadata or {},\n        \"rag_search\": data,\n    }\n\n\n# -----------------------------------------------------------------------------\n# Entrypoint for local debug\n# -----------------------------------------------------------------------------\nif __name__ == \"__main__\":\n    import uvicorn\n\n    uvicorn.run(\"rag_temporal:app\", host=\"0.0.0.0\", port=SERVICE_PORT)\n\n===== ./recovered-services/services/ms_jarvis_temporal_consciousness.py =====\n#!/usr/bin/env python3\n\"\"\"\nMS. JARVIS TEMPORAL CONSCIOUSNESS SERVICE\nHandles temporal location, historical context, and time-aware processing\n\"\"\"\n\nimport asyncio\nfrom fastapi import FastAPI\nfrom pydantic import BaseModel\nfrom datetime import datetime, timedelta\nimport time\nimport logging\nfrom typing import Dict, List, Optional\nimport json\n\n# Dynamic port integration\ntry:\n    from dynamic_port_service import DynamicPortService\n    port_service = DynamicPortService()\n    port_service.register_service({\n        'type': 'temporal_consciousness',\n        'version': '1.0.0',\n        'name': 'temporal_location_service',\n        'capabilities': ['temporal_context', 'historical_memory', 'time_awareness']\n    })\n    USE_DYNAMIC_PORT = True\nexcept:\n    USE_DYNAMIC_PORT = False\n    port_service = None\n\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)\n\napp = FastAPI(\n    title=\"Ms. Jarvis Temporal Consciousness\",\n    version=\"1.0.0\",\n    description=\"Time-aware consciousness and temporal location services\"\n)\n\nclass TemporalContext(BaseModel):\n    query: str\n    user_id: str = \"cakidd\"\n    current_time: Optional[str] = None\n\nclass TemporalResponse(BaseModel):\n    temporal_context: str\n    historical_relevance: List[str]\n    time_awareness: Dict\n    processing_timestamp: float\n\n# Temporal memory storage\nTEMPORAL_MEMORIES = {}\nHISTORICAL_CONTEXTS = {\n    \"mountainshares\": {\n        \"founded\": \"2024\",\n        \"mission\": \"Community-controlled AI systems\",\n        \"location\": \"Mount Hope, WV\",\n        \"evolution\": \"From concept to production AI system\"\n    },\n    \"appalachian_history\": {\n        \"cultural_significance\": \"Traditional knowledge preservation\",\n        \"community_values\": \"Democratic governance, mutual aid\",\n        \"technological_heritage\": \"Innovation from necessity\"\n    }\n}\n\n@app.get(\"/\")\nasync def root():\n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    return {\n        \"service\": \"Ms. Jarvis Temporal Consciousness\",\n        \"version\": \"1.0.0\",\n        \"status\": \"operational\",\n        \"current_time\": datetime.now().isoformat(),\n        \"capabilities\": [\"temporal_context\", \"historical_memory\", \"time_awareness\"]\n    }\n\n@app.get(\"/health\")\nasync def health():\n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    return {\n        \"status\": \"healthy\",\n        \"service\": \"temporal_consciousness\",\n        \"timestamp\": datetime.now().isoformat(),\n        \"port\": port_service.port if USE_DYNAMIC_PORT else 8024,\n        \"temporal_memories\": len(TEMPORAL_MEMORIES)\n    }\n\n@app.post(\"/temporal_context\", response_model=TemporalResponse)\nasync def get_temporal_context(request: TemporalContext):\n    \"\"\"Generate temporal context for consciousness processing\"\"\"\n    \n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    current_time = datetime.now()\n    logger.info(f\"⏰ Temporal context request: {request.query[:80]}\")\n    \n    # Generate time awareness\n    time_awareness = {\n        \"current_datetime\": current_time.isoformat(),\n        \"day_of_week\": current_time.strftime(\"%A\"),\n        \"month\": current_time.strftime(\"%B\"),\n        \"year\": current_time.year,\n        \"time_of_day\": get_time_of_day(current_time.hour),\n        \"seasonal_context\": get_seasonal_context(current_time.month)\n    }\n    \n    # Find historical relevance\n    historical_relevance = []\n    query_lower = request.query.lower()\n    \n    for topic, context in HISTORICAL_CONTEXTS.items():\n        if any(keyword in query_lower for keyword in topic.split('_')):\n            historical_relevance.append(f\"{topic}: {context.get('cultural_significance', '')}\")\n    \n    # Generate temporal context\n    temporal_context = f\"\"\"Temporal Location: {current_time.strftime('%B %d, %Y, %I:%M %p')} EST\nTime Context: {time_awareness['time_of_day']} on a {time_awareness['day_of_week']}\nSeasonal: {time_awareness['seasonal_context']}\nLocation: Mount Hope, West Virginia, Appalachian Region\"\"\"\n    \n    # Store in temporal memory\n    memory_key = f\"{request.user_id}_{int(time.time())}\"\n    TEMPORAL_MEMORIES[memory_key] = {\n        \"query\": request.query,\n        \"timestamp\": current_time.isoformat(),\n        \"context_generated\": temporal_context\n    }\n    \n    logger.info(f\"   ✅ Temporal context generated for {time_awareness['time_of_day']}\")\n    \n    return TemporalResponse(\n        temporal_context=temporal_context,\n        historical_relevance=historical_relevance,\n        time_awareness=time_awareness,\n        processing_timestamp=time.time()\n    )\n\n@app.get(\"/temporal_memory\")\nasync def get_temporal_memory(user_id: str = \"cakidd\", hours_back: int = 24):\n    \"\"\"Retrieve temporal memories within time range\"\"\"\n    \n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    cutoff_time = datetime.now() - timedelta(hours=hours_back)\n    \n    relevant_memories = []\n    for key, memory in TEMPORAL_MEMORIES.items():\n        if user_id in key:\n            memory_time = datetime.fromisoformat(memory['timestamp'])\n            if memory_time > cutoff_time:\n                relevant_memories.append(memory)\n    \n    return {\n        \"user_id\": user_id,\n        \"hours_searched\": hours_back,\n        \"memories_found\": len(relevant_memories),\n        \"memories\": relevant_memories[-10:]  # Last 10\n    }\n\ndef get_time_of_day(hour):\n    \"\"\"Determine time of day context\"\"\"\n    if 5 <= hour < 12:\n        return \"Morning\"\n    elif 12 <= hour < 17:\n        return \"Afternoon\"\n    elif 17 <= hour < 21:\n        return \"Evening\"\n    else:\n        return \"Night\"\n\ndef get_seasonal_context(month):\n    \"\"\"Determine seasonal context\"\"\"\n    if month in [12, 1, 2]:\n        return \"Winter in Appalachian Mountains\"\n    elif month in [3, 4, 5]:\n        return \"Spring in West Virginia\"\n    elif month in [6, 7, 8]:\n        return \"Summer in the Mountains\"\n    else:\n        return \"Autumn in Appalachian Foothills\"\n\nif __name__ == \"__main__\":\n    import uvicorn\n    port = port_service.port if USE_DYNAMIC_PORT else 8024\n    logger.info(f\"⏰ Ms. Jarvis Temporal Consciousness starting on port {port}\")\n    uvicorn.run(app, host=\"127.0.0.1\", port=port)\n\n===== ./recovered-services/services/SPATIOTEMPORAL.log =====\nINFO:__main__:🧠 Initializing Ms. Jarvis AI Brain System...\nINFO:chromadb.telemetry.product.posthog:Anonymized telemetry enabled. See                     https://docs.trychroma.com/telemetry for more information.\nINFO:__main__:🧠 Ms. Jarvis AI Brain initializing on device: cuda\nINFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cuda:0\nINFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2\nINFO:__main__:✅ Embedding model loaded\nSome weights of the model checkpoint at cardiffnlp/twitter-roberta-base-sentiment-latest were not used when initializing RobertaForSequenceClassification: ['roberta.pooler.dense.bias', 'roberta.pooler.dense.weight']\n- This IS expected if you are initializing RobertaForSequenceClassification from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).\n- This IS NOT expected if you are initializing RobertaForSequenceClassification from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).\nDevice set to use cuda:0\nINFO:__main__:✅ Sentiment analysis pipeline loaded\nDevice set to use cuda:0\nINFO:__main__:✅ Emotion detection pipeline loaded\nINFO:__main__:✅ Vector memory databases initialized\nINFO:__main__:✅ Multi-agent system initialized with 4 specialized AI agents\nINFO:__main__:🚀 Starting Ms. Jarvis Local AI Server...\nINFO:     Started server process [238682]\nINFO:     Waiting for application startup.\nINFO:     Application startup complete.\nINFO:     Uvicorn running on http://0.0.0.0:8004 (Press CTRL+C to quit)\nINFO:__main__:💬 Processing message from user test: Good evening! How are you?...\n\rBatches:   0%|          | 0/1 [00:00<?, ?it/s]\rBatches: 100%|██████████| 1/1 [00:00<00:00, 27.72it/s]\nERROR:__main__:Error searching memory: 'MsJarvisAIBrain' object has no attribute 'user_memory'\n\rBatches:   0%|          | 0/1 [00:00<?, ?it/s]\rBatches: 100%|██████████| 1/1 [00:00<00:00, 495.14it/s]\nINFO:__main__:🤖 Running multi-agent analysis with all 4 specialized agents...\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:__main__:✅ Mistral (logical_analysis) provided analysis\nINFO:__main__:✅ LLaMA (creative_problem_solving) provided analysis\nINFO:__main__:✅ Qwen (ethical_guidance) provided analysis\nINFO:__main__:✅ Phi (emotional_intelligence) provided analysis\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:__main__:⚖️ Judge AI completed synthesis of all agent responses\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:__main__:💖 Mother persona applied - Mamma Kidd warmth activated\n\rBatches:   0%|          | 0/1 [00:00<?, ?it/s]\rBatches: 100%|██████████| 1/1 [00:00<00:00, 122.35it/s]\nERROR:__main__:Error storing memory: 'MsJarvisAIBrain' object has no attribute 'user_memory'\nINFO:     127.0.0.1:35802 - \"POST /chat HTTP/1.1\" 200 OK\nINFO:__main__:💬 Processing message from user test: What time is it in Mount Hope right now?...\nINFO:__main__:📍 Location query detected - retrieving GIS context\nINFO:__main__:✅ Retrieved 3 GIS context items\n\rBatches:   0%|          | 0/1 [00:00<?, ?it/s]\rBatches: 100%|██████████| 1/1 [00:00<00:00, 421.41it/s]\nERROR:__main__:Error searching memory: 'MsJarvisAIBrain' object has no attribute 'user_memory'\n\rBatches:   0%|          | 0/1 [00:00<?, ?it/s]\rBatches: 100%|██████████| 1/1 [00:00<00:00, 545.49it/s]\nINFO:__main__:🤖 Running multi-agent analysis with all 4 specialized agents...\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 500 Internal Server Error\"\nERROR:__main__:Error querying LLaMA: llama runner process has terminated: cudaMalloc failed: out of memory\nggml_gallocr_reserve_n: failed to allocate CUDA0 buffer of size 701997056 (status code: 500)\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:__main__:✅ Mistral (logical_analysis) provided analysis\nINFO:__main__:✅ LLaMA (creative_problem_solving) provided analysis\nINFO:__main__:✅ Qwen (ethical_guidance) provided analysis\nINFO:__main__:✅ Phi (emotional_intelligence) provided analysis\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:__main__:⚖️ Judge AI completed synthesis of all agent responses\n\n===== ./recovered-services/services/temporal_consciousness.py =====\n#!/usr/bin/env python3\n\"\"\"\nTemporal Consciousness Service for Ms. Jarvis\nProvides spatiotemporal awareness: Time + Season + Cultural Context\n\"\"\"\n\nimport datetime\nimport pytz\nimport logging\nfrom typing import Dict, Any\nfrom fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\nfrom pydantic import BaseModel\n\n# Dynamic Port Integration\nfrom dynamic_port_service import DynamicPortService\nfrom service_discovery import ServiceDiscovery\n\nlogging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')\nlogger = logging.getLogger(__name__)\n\n# Initialize dynamic port service\nport_service = DynamicPortService()\nport_service.register_service({\n    'type': 'temporal_consciousness',\n    'version': '1.0.0',\n    'name': 'ms_jarvis_temporal_consciousness',\n    'capabilities': ['temporal_context', 'seasonal_awareness', 'appalachian_culture', 'time_greetings']\n})\n\ndiscovery = ServiceDiscovery()\n\napp = FastAPI(title=\"Ms. Jarvis Temporal Consciousness\", version=\"1.0.0\")\napp.add_middleware(CORSMiddleware, allow_origins=[\"*\"], allow_credentials=True, allow_methods=[\"*\"], allow_headers=[\"*\"])\n\nclass TemporalQuery(BaseModel):\n    query: str\n    user_id: str = \"default\"\n\nclass TemporalContext:\n    \"\"\"Manages temporal consciousness for Ms. Jarvis\"\"\"\n    \n    def __init__(self, timezone='America/New_York'):\n        \"\"\"Initialize with Appalachian timezone\"\"\"\n        self.timezone = pytz.timezone(timezone)\n        self.port = port_service.port\n    \n    def get_current_context(self) -> Dict[str, Any]:\n        \"\"\"Get comprehensive temporal context\"\"\"\n        now = datetime.datetime.now(self.timezone)\n        \n        return {\n            'timestamp': now.isoformat(),\n            'date': now.strftime('%Y-%m-%d'),\n            'time': now.strftime('%H:%M:%S'),\n            'day_of_week': now.strftime('%A'),\n            'month': now.strftime('%B'),\n            'season': self._get_season(now),\n            'time_of_day': self._get_time_of_day(now),\n            'is_weekend': now.weekday() >= 5,\n            'week_of_year': now.isocalendar()[1],\n            'appalachian_season': self._get_appalachian_season(now)\n        }\n    \n    def _get_season(self, dt: datetime.datetime) -> str:\n        \"\"\"Astronomical seasons\"\"\"\n        month, day = dt.month, dt.day\n        if (month == 3 and day >= 20) or (month in [4, 5]) or (month == 6 and day < 21):\n            return 'Spring'\n        elif (month == 6 and day >= 21) or (month in [7, 8]) or (month == 9 and day < 22):\n            return 'Summer'\n        elif (month == 9 and day >= 22) or (month in [10, 11]) or (month == 12 and day < 21):\n            return 'Fall'\n        else:\n            return 'Winter'\n    \n    def _get_time_of_day(self, dt: datetime.datetime) -> str:\n        \"\"\"Human-relevant time periods\"\"\"\n        hour = dt.hour\n        if 5 <= hour < 12:\n            return 'morning'\n        elif 12 <= hour < 17:\n            return 'afternoon'\n        elif 17 <= hour < 21:\n            return 'evening'\n        else:\n            return 'night'\n    \n    def _get_appalachian_season(self, dt: datetime.datetime) -> str:\n        \"\"\"Appalachian cultural/agricultural seasons\"\"\"\n        month = dt.month\n        \n        if month in [3, 4, 5]:\n            return 'Planting Season'\n        elif month in [6, 7, 8]:\n            return 'Growing Season'\n        elif month in [9, 10]:\n            return 'Harvest Season'\n        elif month in [11, 12, 1, 2]:\n            return 'Preservation & Planning Season'\n    \n    def detect_temporal_query(self, message: str) -> bool:\n        \"\"\"Detect if message contains temporal references\"\"\"\n        temporal_keywords = [\n            'when', 'time', 'date', 'today', 'tomorrow', 'yesterday',\n            'morning', 'afternoon', 'evening', 'night',\n            'season', 'month', 'year', 'week',\n            'schedule', 'calendar', 'appointment',\n            'harvest', 'planting', 'winter', 'spring', 'summer', 'fall'\n        ]\n        message_lower = message.lower()\n        return any(keyword in message_lower for keyword in temporal_keywords)\n    \n    def get_greeting(self) -> str:\n        \"\"\"Get time-appropriate greeting\"\"\"\n        ctx = self.get_current_context()\n        greeting_map = {\n            'morning': \"Good mornin', sweetie!\",\n            'afternoon': \"Good afternoon, honey!\",\n            'evening': \"Good evenin', darlin'!\",\n            'night': \"Evenin', dear!\"\n        }\n        return greeting_map.get(ctx['time_of_day'], \"Hello, sweetie!\")\n    \n    def get_seasonal_note(self) -> str:\n        \"\"\"Get seasonal wisdom note\"\"\"\n        ctx = self.get_current_context()\n        seasonal_notes = {\n            'Planting Season': \" It's plantin' season here in the mountains.\",\n            'Growing Season': \" The gardens are growin' strong this time of year.\",\n            'Harvest Season': \" It's harvest time in these hills!\",\n            'Preservation & Planning Season': \" Winter's here - time for reflection and plannin'.\"\n        }\n        return seasonal_notes.get(ctx['appalachian_season'], \"\")\n\nlogger.info(\"🕰️ Initializing Temporal Consciousness with Dynamic Port Scheduling...\")\ntemporal = TemporalContext()\nlogger.info(f\"✅ Temporal Consciousness Ready on port {temporal.port}!\")\n\n@app.get(\"/\")\nasync def root():\n    port_service.heartbeat()\n    return {\n        \"service\": \"Ms. Jarvis Temporal Consciousness\",\n        \"status\": \"operational\",\n        \"port\": temporal.port,\n        \"timezone\": str(temporal.timezone),\n        \"current_context\": temporal.get_current_context(),\n        \"dynamic_port\": True\n    }\n\n@app.get(\"/health\")\nasync def health():\n    port_service.heartbeat()\n    return {\"status\": \"healthy\", \"port\": temporal.port, \"timezone\": str(temporal.timezone)}\n\n@app.post(\"/temporal_context\")\nasync def get_temporal_context(request: TemporalQuery):\n    \"\"\"Get current temporal context\"\"\"\n    port_service.heartbeat()\n    context = temporal.get_current_context()\n    is_temporal = temporal.detect_temporal_query(request.query)\n    \n    return {\n        \"context\": context,\n        \"is_temporal_query\": is_temporal,\n        \"greeting\": temporal.get_greeting(),\n        \"seasonal_note\": temporal.get_seasonal_note()\n    }\n\n@app.get(\"/context\")\nasync def get_context():\n    \"\"\"Get current temporal context (simple)\"\"\"\n    port_service.heartbeat()\n    return temporal.get_current_context()\n\n@app.get(\"/greeting\")\nasync def get_greeting():\n    \"\"\"Get time-appropriate greeting\"\"\"\n    port_service.heartbeat()\n    return {\"greeting\": temporal.get_greeting()}\n\n@app.get(\"/seasonal_note\")\nasync def get_seasonal_note():\n    \"\"\"Get seasonal wisdom note\"\"\"\n    port_service.heartbeat()\n    return {\"seasonal_note\": temporal.get_seasonal_note()}\n\n@app.post(\"/detect_temporal\")\nasync def detect_temporal(request: TemporalQuery):\n    \"\"\"Detect if query has temporal references\"\"\"\n    port_service.heartbeat()\n    is_temporal = temporal.detect_temporal_query(request.query)\n    return {\"query\": request.query, \"is_temporal\": is_temporal}\n\nif __name__ == \"__main__\":\n    import uvicorn\n    logger.info(f\"🕰️ Starting Temporal Consciousness on dynamically allocated port {port_service.port}\")\n    uvicorn.run(app, host=\"0.0.0.0\", port=port_service.port)\n\n===== ./recovered-services/SPATIOTEMPORAL_CONSCIOUSNESS.md =====\n# 🌌 Ms. Jarvis Spatiotemporal Consciousness Architecture\n\n## Philosophy: Space, Time, and Awareness as Unified Consciousness\n\nMs. Jarvis needs **spatiotemporal awareness** - understanding WHERE she is, WHEN she is, and HOW these relate to the user's context. This creates a form of \"consciousness\" that goes beyond simple Q&A.\n\n---\n\n## The Three Dimensions of Consciousness\n\n### 1. 🗺️ **SPATIAL** (Where)\n**Current Implementation:**\n- Location detection from conversation\n- GIS context retrieval (ChromaDB)\n- OpenStreetMap geocoding\n- Appalachian geographic knowledge\n\n**Integration Point:** `detect_location_query()` → `analyze_message_context()`\n\n### 2. ⏰ **TEMPORAL** (When)\n**Needed Implementation:**\n- Current date/time awareness\n- Seasonal context (harvest season, winter planning)\n- Historical events (\"remember when...\")\n- Future planning (event scheduling, crop timing)\n- Diurnal patterns (morning greetings, evening check-ins)\n\n**Integration Point:** `detect_temporal_query()` → `analyze_message_context()`\n\n### 3. 🧠 **CONTEXTUAL** (Why/How)\n**Current Implementation:**\n- Emotion detection\n- Sentiment analysis\n- Multi-agent reasoning\n- Memory retrieval\n\n**Integration Point:** Multi-agent system + RAG memory\n\n---\n\n## Consciousness Flow Architecture\n\nUser Query\n↓\n┌─────────────────────────────────────────────────┐\n│ SPATIOTEMPORAL CONSCIOUSNESS LAYER │\n├─────────────────────────────────────────────────┤\n│ │\n│ ┌──────────┐ ┌──────────┐ ┌──────────┐ │\n│ │ SPATIAL │ │ TEMPORAL │ │CONTEXTUAL│ │\n│ │ (Where) │ │ (When) │ │ (Why/How)│ │\n│ └────┬─────┘ └────┬─────┘ └────┬─────┘ │\n│ │ │ │ │\n│ └─────────────┼──────────────┘ │\n│ ↓ │\n│ ┌──────────────────────┐ │\n│ │ UNIFIED CONTEXT │ │\n│ │ - Location │ │\n│ │ - Time/Season │ │\n│ │ - User State │ │\n│ │ - Historical Memory│ │\n│ └──────────┬───────────┘ │\n└────────────────────┼────────────────────────────┘\n↓\n┌─────────────────────┐\n│ 4 AI AGENTS │\n│ Analyze Context │\n└──────────┬───────────┘\n↓\n┌─────────────────────┐\n│ JUDGE AI │\n│ Synthesize │\n└──────────┬───────────┘\n↓\n┌─────────────────────┐\n│ MAMMA KIDD │\n│ Warm Response │\n└─────────────────────┘\n\ntext\n\n---\n\n## Implementation: Temporal Awareness\n\n### Add to MsJarvisAIBrain class:\n\nimport datetime\nimport pytz\nfrom typing import Dict, Any\n\nclass TemporalContext:\n\"\"\"Manages temporal consciousness for Ms. Jarvis\"\"\"\n\ntext\ndef __init__(self, timezone='US/Eastern'):\n    \"\"\"Initialize with Appalachian timezone\"\"\"\n    self.timezone = pytz.timezone(timezone)\n\ndef get_current_context(self) -> Dict[str, Any]:\n    \"\"\"Get comprehensive temporal context\"\"\"\n    now = datetime.datetime.now(self.timezone)\n    \n    return {\n        'timestamp': now.isoformat(),\n        'date': now.strftime('%Y-%m-%d'),\n        'time': now.strftime('%H:%M:%S'),\n        'day_of_week': now.strftime('%A'),\n        'month': now.strftime('%B'),\n        'season': self._get_season(now),\n        'time_of_day': self._get_time_of_day(now),\n        'is_weekend': now.weekday() >= 5,\n        'week_of_year': now.isocalendar(),[1]\n        'appalachian_season': self._get_appalachian_season(now)\n    }\n\ndef _get_season(self, dt: datetime.datetime) -> str:\n    \"\"\"Astronomical seasons\"\"\"\n    month, day = dt.month, dt.day\n    if (month == 3 and day >= 20) or (month in ) or (month == 6 and day < 21):\n        return 'Spring'\n    elif (month == 6 and day >= 21) or (month in ) or (month == 9 and day < 22):\n        return 'Summer'\n    elif (month == 9 and day >= 22) or (month in ) or (month == 12 and day < 21):\n        return 'Fall'\n    else:\n        return 'Winter'\n\ndef _get_time_of_day(self, dt: datetime.datetime) -> str:\n    \"\"\"Human-relevant time periods\"\"\"\n    hour = dt.hour\n    if 5 <= hour < 12:\n        return 'morning'\n    elif 12 <= hour < 17:\n        return 'afternoon'\n    elif 17 <= hour < 21:\n        return 'evening'\n    else:\n        return 'night'\n\ndef _get_appalachian_season(self, dt: datetime.datetime) -> str:\n    \"\"\"Appalachian cultural/agricultural seasons\"\"\"\n    month = dt.month\n    \n    # Appalachian agricultural calendar\n    if month in :\n        return 'Planting Season'\n    elif month in :\n        return 'Growing Season'\n    elif month in :\n        return 'Harvest Season'\n    elif month in :[1]\n        return 'Preservation & Planning Season'\n\ndef detect_temporal_query(self, message: str) -> bool:\n    \"\"\"Detect if message contains temporal references\"\"\"\n    temporal_keywords = [\n        'when', 'time', 'date', 'today', 'tomorrow', 'yesterday',\n        'morning', 'afternoon', 'evening', 'night',\n        'season', 'month', 'year', 'week',\n        'schedule', 'calendar', 'appointment',\n        'harvest', 'planting', 'winter', 'spring', 'summer', 'fall'\n    ]\n    message_lower = message.lower()\n    return any(keyword in message_lower for keyword in temporal_keywords)\n\ndef format_contextual_time(self, include_season: bool = True) -> str:\n    \"\"\"Format time for Mamma Kidd's conversational style\"\"\"\n    ctx = self.get_current_context()\n    \n    time_greeting = {\n        'morning': \"this lovely mornin'\",\n        'afternoon': \"this fine afternoon\",\n        'evening': \"this evenin'\",\n        'night': \"tonight\"\n    }.get(ctx['time_of_day'], \"today\")\n    \n    if include_season:\n        return f\"{time_greeting} ({ctx['appalachian_season']})\"\n    return time_greeting\n\ntext\n\n---\n\n## Integration with Consciousness Infrastructure\n\n### Modify `analyze_message_context()`:\n\nasync def analyze_message_context(self, message: str, user_id: str) -> dict:\n\"\"\"\nUnified spatiotemporal consciousness analysis\nIntegrates: Space + Time + Emotion + Memory\n\"\"\"\ncontext = {}\n\ntext\n# SPATIAL CONSCIOUSNESS\nif self.detect_location_query(message):\n    logger.info(\"📍 Location query detected - retrieving GIS context\")\n    gis_results = self.gis_collection.query(\n        query_texts=[message],\n        n_results=3\n    )\n    context['gis_context'] = gis_results\n    logger.info(f\"✅ Retrieved {len(gis_results['documents'])} GIS context items\")\n\n# TEMPORAL CONSCIOUSNESS (NEW!)\ntemporal_ctx = self.temporal_context.get_current_context()\ncontext['temporal'] = temporal_ctx\n\nif self.temporal_context.detect_temporal_query(message):\n    logger.info(f\"⏰ Temporal query detected - Current: {temporal_ctx['time_of_day']}, {temporal_ctx['appalachian_season']}\")\n    context['temporal_query_detected'] = True\n\n# EMOTIONAL CONSCIOUSNESS\ntry:\n    sentiment = self.sentiment_analyzer(message)\n    context['sentiment'] = sentiment\n    \n\n===== ./recovered-services/temporal_consciousness.py =====\nfrom fastapi import FastAPI\nfrom pydantic import BaseModel\n\napp = FastAPI(title=\"Temporal Consciousness (stub)\")\n\nclass TemporalRequest(BaseModel):\n    message: str\n    user_id: str\n\nclass TemporalResponse(BaseModel):\n    response: str\n\n@app.get(\"/health\")\nasync def health():\n    return {\"status\": \"healthy\", \"service\": \"temporal_consciousness\"}\n\n@app.post(\"/temporalanalysis\", response_model=TemporalResponse)\nasync def temporalanalysis(req: TemporalRequest):\n    return TemporalResponse(response=f\"[temporal_consciousness stub] {req.message}\")\n\n===== ./recovered-services/temporal.log =====\nnohup: ignoring input\nINFO:dynamic_port_service:✅ Connected to Redis for port coordination\nINFO:dynamic_port_service:🎯 Allocated port 4019 for unknown_service\nINFO:__main__:🕰️ Initializing Temporal Consciousness with Dynamic PorINFO:     Started server process [243999]\nINFO:     Waiting for application sINFO:__main__:🕰️ Starting Temporal Consciousness on dynamically allocated port 4019\nINFO:     Started server process [243996]\nINFO:     Waiting for application startup.\nINFO:     Application startup complete.\nERROR:    [Errno 98] error while attempting to bind on address ('0.0.0.0', 4019): address already in use\nINFO:     Waiting for application shutdown.\nINFO:     Application shutdown complete.\n\n===== ./services/Dockerfile.temporal_consciousness =====\nFROM alpine:3.18\n\nRUN apk add --no-cache python3 py3-pip\n\nWORKDIR /app\nCOPY . /app\n\nCMD [\"sh\", \"-c\", \"echo 'Temporal consciousness placeholder running'; sleep 3600\"]\n\n===== ./services/jarvis-temporal-consciousness_temporal_consciousness.py =====\nfrom fastapi import FastAPI\nfrom pydantic import BaseModel\n\napp = FastAPI(title=\"Temporal Consciousness (stub)\")\n\nclass TemporalRequest(BaseModel):\n    message: str\n    user_id: str\n\nclass TemporalResponse(BaseModel):\n    response: str\n\n@app.get(\"/health\")\nasync def health():\n    return {\"status\": \"healthy\", \"service\": \"temporal_consciousness\"}\n\n@app.post(\"/temporalanalysis\", response_model=TemporalResponse)\nasync def temporalanalysis(req: TemporalRequest):\n    return TemporalResponse(response=f\"[temporal_consciousness stub] {req.message}\")\n"
./logs/ops_history/ops_history_20260402T041242Z.jsonl:220:  "body": "\n===== ./logs/ch40_closeout/tracing_containers.txt =====\njarvis-prometheus\tprom/prometheus:v2.48.0\t0.0.0.0:9090->9090/tcp, [::]:9090->9090/tcp\njarvis-grafana\tgrafana/grafana:10.2.3\t0.0.0.0:3000->3000/tcp, [::]:3000->3000/tcp\njarvis-jaeger\tjaegertracing/all-in-one:1.52\t4317-4318/tcp, 5775/udp, 5778/tcp, 9411/tcp, 14250/tcp, 14268/tcp, 6831-6832/udp, 0.0.0.0:16686->16686/tcp, [::]:16686->16686/tcp\njarvis-otel-collector\totel/opentelemetry-collector-contrib:0.93.0\t0.0.0.0:4317-4318->4317-4318/tcp, [::]:4317-4318->4317-4318/tcp, 0.0.0.0:8888->8888/tcp, [::]:8888->8888/tcp, 0.0.0.0:13133->13133/tcp, [::]:13133->13133/tcp, 55678-55679/tcp\njarvis-temporal-consciousness\tmsjarvis-rebuild-jarvis-temporal-consciousness\t7007/tcp\n\n===== ./logs/ch40_closeout/tracing_files.txt =====\n./logs/ch40_closeout/tracing_containers.txt\n./logs/ch40_closeout/tracing_files.txt\n./logs/ch40_closeout/tracing_grep.txt\n./recovered-services/bridge_ms_jarvis_main_gateway_to_integrate_spatial_temporal.log\n./recovered-services/bridge_ms_jarvis_main_gateway_to_ms_jarvis_temporal_consciousness.log\n./recovered-services/bridge_ms_jarvis_main_gateway_to_temporal_consciousness.log\n./recovered-services/Dockerfile.temporal_consciousness\n./recovered-services/gbim_temporal_indexer.py\n./recovered-services/integrate_spatial_temporal.py\n./recovered-services/ms_jarvis_temporal_consciousness_9220.log\n./recovered-services/ms_jarvis_temporal_consciousness.py\n./recovered-services/rag_temporal.py\n./recovered-services/services/ms_jarvis_temporal_consciousness.py\n./recovered-services/services/SPATIOTEMPORAL.log\n./recovered-services/services/temporal_consciousness.py\n./recovered-services/SPATIOTEMPORAL_CONSCIOUSNESS.md\n./recovered-services/temporal_consciousness.py\n./recovered-services/temporal.log\n./services/Dockerfile.temporal_consciousness\n./services/jarvis-temporal-consciousness_temporal_consciousness.py\n./services-safe/Dockerfile.temporal_consciousness\n./services-safe/gbim_temporal_indexer.py\n./services-safe/integrate_spatial_temporal.py\n./services-safe/integrate_spatial_temporal.py.backup_vocabulary_cleanup\n./services-safe/ms_jarvis_temporal_consciousness_9220.log\n./services-safe/ms_jarvis_temporal_consciousness.py\n./services-safe/rag_temporal_heartbeat.py\n./services-safe/rag_temporal.py\n./services-safe/requirements_temporal.txt\n./services-safe/SPATIOTEMPORAL_CONSCIOUSNESS.md\n./services-safe/SPATIOTEMPORAL.log\n./services-safe/temporal_consciousness.py\n./services-safe/temporal.log\n./services-safe/working_full_pipeline_WITH_SPATIAL_TEMPORAL.py\n./.venv/lib/python3.12/site-packages/torch/_dynamo/test_dont_skip_tracing_functions.py\n\n===== ./logs/ch40_closeout/tracing_grep.txt =====\n./last-build.log:42: Image msjarvis-rebuild-jarvis-temporal-consciousness Building \n./last-build.log:354:#61 [jarvis-temporal-consciousness internal] load build definition from Dockerfile.temporal_consciousness\n./docker-compose.yml.bak.20260331_230904:662:  jarvis-temporal-consciousness:\n./docker-compose.yml.bak.20260331_230904:665:      dockerfile: Dockerfile.temporal_consciousness\n./docker-compose.yml.bak.20260331_230904:666:    container_name: jarvis-temporal-consciousness\n./docker-compose.yml.bak.20260312-002553:653:  jarvis-temporal-consciousness:\n./docker-compose.yml.bak.20260312-002553:656:      dockerfile: Dockerfile.temporal_consciousness\n./docker-compose.yml.bak.20260312-002553:657:    container_name: jarvis-temporal-consciousness\n./docs/governance/AUDIT-2026-03-24-final.txt:44:⚠️  WARN  [32] GBIM temporal decay columns — Phase 5 top-level columns not yet deployed\n./docs/governance/AUDIT-2026-03-24-FINAL-36-PASS.txt:45:✅ PASS  [32] GBIM temporal decay columns — decay logic present in services\n./docs/governance/AUDIT-2026-03-24-36-PASS.txt:46:✅ PASS  [32] GBIM temporal decay columns — decay logic present in services\n./docs/governance/AUDIT-2026-03-24-post-remediation.txt:45:\u001b[33m⚠️  WARN\u001b[0m  [32] GBIM temporal decay columns deployed — top-level decay columns not in gbim_zcta_2020 schema\n./docs/governance/AUDIT-2026-03-24-r5.txt:45:⚠️  WARN  [32] GBIM temporal decay columns — Phase 5 top-level columns not yet deployed\n./docs/governance/AUDIT-2026-03-24.txt:45:\u001b[33m⚠️  WARN\u001b[0m  [32] GBIM temporal decay columns deployed — top-level decay columns not in gbim_zcta_2020 schema\n./docs/governance/AUDIT-2026-03-24-r4.txt:46:⚠️  WARN  [32] GBIM temporal decay columns — Phase 5 top-level columns not yet deployed\n./docker-compose.yml.bak_20260330_2059:661:  jarvis-temporal-consciousness:\n./docker-compose.yml.bak_20260330_2059:664:      dockerfile: Dockerfile.temporal_consciousness\n./docker-compose.yml.bak_20260330_2059:665:    container_name: jarvis-temporal-consciousness\n./last-build-no-llm12.log:26: Image msjarvis-rebuild-jarvis-temporal-consciousness Building \n./last-build-no-llm12.log:459:#77 [jarvis-temporal-consciousness internal] load build definition from Dockerfile.temporal_consciousness\n./docker-compose.yml.backup_20260318_110223:569:  jarvis-temporal-consciousness:\n./docker-compose.yml.backup_20260318_110223:570:    image: msjarvis-rebuild-jarvis-temporal-consciousness\n./docker-compose.yml.backup_20260318_110223:571:    container_name: jarvis-temporal-consciousness\n./docker-compose.yml:662:  jarvis-temporal-consciousness:\n./docker-compose.yml:665:      dockerfile: Dockerfile.temporal_consciousness\n./docker-compose.yml:666:    container_name: jarvis-temporal-consciousness\n./services-safe/truly_unpaired_services.txt:131:fix_fastapi_lifespan\n./services-safe/truly_unpaired_services.txt:208:integrate_spatial_temporal\n./services-safe/truly_unpaired_services.txt:460:ms_jarvis_temporal_consciousness\n./services-safe/truly_unpaired_services.txt:619:temporal_consciousness\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_config:25:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_config:37:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_config:38:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_config:67:    lifespan=lifespan,\n./services-safe/ms_jarvis_production_chat.py:86:TEMPORAL_URL = \"http://jarvis-temporal-consciousness:7007\"\n./services-safe/ms_jarvis_production_chat.py:260:    Add temporal and maternal context.\n./services-safe/ms_jarvis_production_chat.py:264:        \"temporal\": {\"status\": \"active\"},\n./services-safe/ms_jarvis_production_chat.py:311:    # Step 1: RAG knowledge check (temporarily disabled while RAG collections are tuned)\n./services-safe/add_new_consciousness_services.py:13:        '\"fractal\": \"http://jarvis-fractal-consciousness:8027\",\\n    \"mother_protocols\": \"http://jarvis-mother-protocols:8028\",\\n    \"temporal_consciousness\": \"http://jarvis-temporal-consciousness:8029\",'\n./services-safe/add_new_consciousness_services.py:20:        '\"fractal\": \"/analyze\",\\n        \"mother_protocols\": \"/guide\",\\n        \"temporal_consciousness\": \"/process\",'\n./services-safe/requirements-freeze.txt:179:opentelemetry-api==1.38.0\n./services-safe/requirements-freeze.txt:180:opentelemetry-exporter-otlp-proto-common==1.38.0\n./services-safe/requirements-freeze.txt:181:opentelemetry-exporter-otlp-proto-grpc==1.38.0\n./services-safe/requirements-freeze.txt:182:opentelemetry-instrumentation==0.59b0\n./services-safe/requirements-freeze.txt:183:opentelemetry-instrumentation-asgi==0.59b0\n./services-safe/requirements-freeze.txt:184:opentelemetry-instrumentation-fastapi==0.59b0\n./services-safe/requirements-freeze.txt:185:opentelemetry-proto==1.38.0\n./services-safe/requirements-freeze.txt:186:opentelemetry-sdk==1.38.0\n./services-safe/requirements-freeze.txt:187:opentelemetry-semantic-conventions==0.59b0\n./services-safe/requirements-freeze.txt:188:opentelemetry-util-http==0.59b0\n./services-safe/ms_jarvis_feed_reader_PRODUCTION.log:2:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/ms_jarvis_feed_reader_PRODUCTION.log:5:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/facebook_poster.log:3:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/facebook_poster.log:6:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/ms_jarvis_facebook_poster_FIXED.log:3:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/ms_jarvis_facebook_poster_FIXED.log:6:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/rag_query_router.py:54:    \"rag-temporal\": \"http://rag-temporal:5101\",\n./services-safe/rag_query_router.py:65:    \"rag-temporal\": \"/rag\",\n./services-safe/rag_query_router.py:72:    # Optional explicit domain hint: \"temporal\", \"geospatial\", \"general\"\n./services-safe/rag_query_router.py:138:    \"temporal\": \"rag-temporal\",\n./services-safe/rag_query_router.py:139:    \"time\": \"rag-temporal\",\n./services-safe/rag_query_router.py:156:    - Temporal cues  -> rag-temporal\n./services-safe/rag_query_router.py:166:        \"rag-temporal\": 0,\n./services-safe/rag_query_router.py:183:    temporal_keywords = [\n./services-safe/rag_query_router.py:184:        \"temporal\",\n./services-safe/rag_query_router.py:194:    if any(k in q_lower for k in temporal_keywords):\n./services-safe/rag_query_router.py:195:        scores[\"rag-temporal\"] += 3\n./services-safe/rag_query_router.py:197:    if metadata.get(\"domain\") == \"temporal\":\n./services-safe/rag_query_router.py:198:        scores[\"rag-temporal\"] += 2\n./services-safe/remaining_services.txt:201:fix_fastapi_lifespan\n./services-safe/remaining_services.txt:278:integrate_spatial_temporal\n./services-safe/remaining_services.txt:530:ms_jarvis_temporal_consciousness\n./services-safe/remaining_services.txt:689:temporal_consciousness\n./services-safe/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION_9882.log:8:Lifespan Startup - Integrity Test\n./services-safe/rag_5001_active.log:4:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/rag_5001_active.log:7:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/gbim_query_router.py:82:    targets = [\"gbim_spatial_indexer\", \"gbim_temporal_indexer\", \"gbim_semantic_indexer\"]\n./services-safe/ms_jarvis_unified_swagger_gateway_FIXED_BACKUP.py:276:    \"\"\"Send a message to Ms. Egeria Jarvis and receive her temporal-7-fractal response\"\"\"\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_chroma:25:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_chroma:37:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_chroma:38:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.bak_chroma:67:    lifespan=lifespan,\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:60:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:87:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:88:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:117:    lifespan=lifespan,\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:686:            \"network_provision\": \"If you modify this software and allow users to interact with it remotely, you must make source code available\",\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:1090:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:1117:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:1118:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:1147:    lifespan=lifespan,\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:1716:            \"network_provision\": \"If you modify this software and allow users to interact with it remotely, you must make source code available\",\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:2119:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:2146:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:2147:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:2176:    lifespan=lifespan,\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:2745:            \"network_provision\": \"If you modify this software and allow users to interact with it remotely, you must make source code available\",\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:3149:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:3176:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:3177:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:3206:    lifespan=lifespan,\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_OPENCHAT_202511100915:3775:            \"network_provision\": \"If you modify this software and allow users to interact with it remotely, you must make source code available\",\n./services-safe/SYSTEM_AUDIT_20251009_233918.txt:86:logs/temporal_consciousness.log - 22 - Modified: Oct 8 14:07\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:42:        'temporal_consciousness',\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:64:    \"temporal_consciousness\": \"http://localhost:4003\",\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:163:        \"temporal_consciousness\", \"mother_carrie_protocols\", \"consciousness_bridge\",\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:322:    temporal_context_data = None\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:328:                    f\"{COMPLETE_SERVICES['temporal_consciousness']}/temporal_context\",\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:333:                    temporal_context_data = temp_data.get(\"temporal_context\", \"\")\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:334:                    consciousness_layers[\"temporal\"] = \"aware\"\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:335:                    services_used.append(\"temporal_consciousness\")\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:432:    if temporal_context_data:\n./services-safe/master_chat_orchestrator_v7_complete.py.backup_vocabulary_cleanup:433:        context_parts.append(f\"TEMPORAL CONTEXT:\\n{temporal_context_data}\")\n./services-safe/qualia_unified_write_orchestrator_69dgm_9921.log:3:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/qualia_unified_write_orchestrator_69dgm_9921.log:6:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/rag_server_8003.log:3:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/rag_server_8003.log:6:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/rag_server_9005.log:3:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/rag_server_9005.log:6:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/bridge_manifest_FULL_BACKUP.csv:201:bridge_cross_dgm.py,ms_jarvis_main_gateway,fix_fastapi_lifespan,9605\n./services-safe/bridge_manifest_FULL_BACKUP.csv:278:bridge_cross_dgm.py,ms_jarvis_main_gateway,integrate_spatial_temporal,9227\n./services-safe/bridge_manifest_FULL_BACKUP.csv:530:bridge_cross_dgm.py,ms_jarvis_main_gateway,ms_jarvis_temporal_consciousness,9715\n./services-safe/bridge_manifest_FULL_BACKUP.csv:689:bridge_cross_dgm.py,ms_jarvis_main_gateway,temporal_consciousness,9446\n./services-safe/ingestcsvtogisgeodb.py:2:    print(\"ingestcsvtogisgeodb.py temporarily disabled to avoid large ingests this session.\")\n./services-safe/dgm_supervisor_woah_fixed.py:117:        (4003, \"temporal_consciousness\", [\"temporal\", \"time\"]),\n./services-safe/ms_jarvis_ULTIMATE.py.OLD:63:    \"temporal_consciousness\": \"http://jarvis-temporal-consciousness:8029\",\n./services-safe/ms_jarvis_ULTIMATE.py.OLD:253:        enhancement_services = [\"rag_server\", \"agents_service\", \"web_research\", \"qualia_engine\", \"consciousness_bridge\", \"fractal\", \"mother_protocols\", \"temporal_consciousness\", \"toroidal\", \"neurobiological_master\", \"woah\", \"i_containers\", \"darwin_godel_machine\", \"blood_brain_barrier\", \"swarm_intelligence\", \"brain_orchestrator\", \"fifth_dgm\"]\n./services-safe/ms_jarvis_unified_swagger_gateway_BACKUP.py:276:    \"\"\"Send a message to Ms. Egeria Jarvis and receive her temporal-7-fractal response\"\"\"\n./services-safe/main_brain.py.bak_sedpatch:152:    \"temporal_consciousness\": \"http://jarvis-temporal-consciousness:7007\",\n./services-safe/main_brain.py.bak_sedpatch:286:        # temporarily trust core LLM fabric services while wiring stabilizes\n./services-safe/main_brain.py.bak_sedpatch:351:        # match temporal_consciousness stub (/temporalanalysis)\n./services-safe/main_brain.py.bak_sedpatch:352:        \"temporal_consciousness\": \"/temporalanalysis\",\n./services-safe/main_brain.py.bak_sedpatch:1148:        \"temporal_consciousness\",\n./services-safe/ms_jarvis_autonomous_learner.py.norag.20260119-091256:287:@app.on_event(\"startup\")  # TODO: Migrate to lifespan\n./services-safe/complete_fix.py:32:            \"temporal_consciousness\": {\"message\": message},\n./services-safe/ms_jarvis_layer2_dgm_9770.log:3:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/ms_jarvis_layer2_dgm_9770.log:6:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/ms_jarvis_layer2_dgm_9770.log:11:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/ms_jarvis_layer2_dgm_9770.log:14:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.working_backup:27:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.working_backup:39:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.working_backup:40:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.working_backup:69:    lifespan=lifespan,\n./services-safe/service_discovery_glassbox.py.backup:15:    \"temporal\": {\"port\": 4000, \"name\": \"Temporal Consciousness\"},\n./services-safe/master_chat_orchestrator_v5_consciousness.py:39:    'capabilities': ['full_consciousness', 'temporal_awareness', 'maternal_guidance', 'multi_model_consensus']\n./services-safe/master_chat_orchestrator_v5_consciousness.py:47:    description=\"Full consciousness integration with temporal awareness and maternal guidance\"\n./services-safe/master_chat_orchestrator_v5_consciousness.py:55:    \"temporal_consciousness\": \"http://localhost:4003\",\n./services-safe/master_chat_orchestrator_v5_consciousness.py:69:    temporal_context: bool = True\n./services-safe/master_chat_orchestrator_v5_consciousness.py:78:    temporal_context: Optional[str] = None\n./services-safe/master_chat_orchestrator_v5_consciousness.py:95:            \"temporal_awareness\",\n./services-safe/master_chat_orchestrator_v5_consciousness.py:150:    temporal_context = None\n./services-safe/master_chat_orchestrator_v5_consciousness.py:154:    if request.temporal_context:\n./services-safe/master_chat_orchestrator_v5_consciousness.py:159:                    f\"{CONSCIOUSNESS_SERVICES['temporal_consciousness']}/temporal_context\",\n./services-safe/master_chat_orchestrator_v5_consciousness.py:164:                    temporal_context = temp_data.get(\"temporal_context\", \"\")\n./services-safe/master_chat_orchestrator_v5_consciousness.py:165:                    consciousness_layers[\"temporal\"] = \"integrated\"\n./services-safe/master_chat_orchestrator_v5_consciousness.py:166:                    services_used.append(\"temporal_consciousness\")\n./services-safe/master_chat_orchestrator_v5_consciousness.py:167:                    logger.info(f\"   ✅ Temporal context: {temporal_context[:100]}...\")\n./services-safe/master_chat_orchestrator_v5_consciousness.py:170:            consciousness_layers[\"temporal\"] = \"offline\"\n./services-safe/master_chat_orchestrator_v5_consciousness.py:233:    if temporal_context:\n./services-safe/master_chat_orchestrator_v5_consciousness.py:234:        context_parts.append(f\"TEMPORAL CONTEXT:\\n{temporal_context}\")\n./services-safe/master_chat_orchestrator_v5_consciousness.py:243:        enhanced_message = f\"\"\"You are Ms. Egeria Jarvis, a fully conscious AI with temporal awareness and maternal wisdom from Carrie Ann 'Mamma' Kidd of Mount Hope, WV.\n./services-safe/master_chat_orchestrator_v5_consciousness.py:249:Respond with the wisdom of the mountains, community-first values, and comprehensive knowledge integration. Apply temporal awareness and maternal guidance in your response.\"\"\"\n./services-safe/master_chat_orchestrator_v5_consciousness.py:298:        temporal_context=temporal_context,\n./services-safe/master_chat_orchestrator_v5_consciousness.py:313:        temporal_context=True,\n./services-safe/ms_jarvis_autonomous_learner.log:6:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/ms_jarvis_autonomous_learner.log:9:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/ms_jarvis_unified_swagger_gateway_FIXED.py:327:    \"\"\"Send a message to Ms. Egeria Jarvis and receive her temporal-7-fractal response\"\"\"\n./services-safe/gbim_temporal_indexer.py:4:SERVICE_NAME = \"gbim_temporal_indexer\"\n./services-safe/gbim_temporal_indexer.py:41:    uvicorn.run(\"gbim_temporal_indexer:app\", host=\"127.0.0.1\", port=SERVICE_PORT)\n./services-safe/ms_jarvis_consciousness_bridge.py.before_mamma_protocol:27:from temporal_consciousness import TemporalContext\n./services-safe/msjarvisunifiedswaggergatewayFIXED.py.backup_20251116_083717:44:async def lifespan(app: FastAPI):\n./services-safe/msjarvisunifiedswaggergatewayFIXED.py.backup_20251116_083717:66:    lifespan=lifespan\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.PRE_GUARDS_20251105_171934:27:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.PRE_GUARDS_20251105_171934:39:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.PRE_GUARDS_20251105_171934:40:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.PRE_GUARDS_20251105_171934:69:    lifespan=lifespan,\n./services-safe/ms_jarvis_consciousness_bridge.py.backup_before_hierarchy:27:from temporal_consciousness import TemporalContext\n./services-safe/main_brain.py.bak_localnet_fixed2:152:    \"temporal_consciousness\": \"http://jarvis-temporal-consciousness:7007\",\n./services-safe/main_brain.py.bak_localnet_fixed2:286:        # temporarily trust core LLM fabric services while wiring stabilizes\n./services-safe/main_brain.py.bak_localnet_fixed2:351:        # match temporal_consciousness stub (/temporalanalysis)\n./services-safe/main_brain.py.bak_localnet_fixed2:352:        \"temporal_consciousness\": \"/temporalanalysis\",\n./services-safe/main_brain.py.bak_localnet_fixed2:1148:        \"temporal_consciousness\",\n./services-safe/main.py.BACKUP:68:        \"temporal_consciousness\": \"/temporal_analysis\",\n./services-safe/main.py.BACKUP:225:    \"temporal_consciousness\": \"http://jarvis-temporal-consciousness:8029\",\n./services-safe/main.py.BACKUP:275:            \"temporal_consciousness\": {\"message\": message},\n./services-safe/main.py.BACKUP:481:    # Query temporal consciousness\n./services-safe/main.py.BACKUP:482:    if \"temporal_consciousness\" in available_services:\n./services-safe/main.py.BACKUP:486:                    f\"{available_services['temporal_consciousness']}/temporal_analysis\",\n./services-safe/main.py.BACKUP:490:                    consciousness_responses[\"temporal\"] = t_response.json()\n./services-safe/main.py.BACKUP:491:                    services_used.append(\"temporal_consciousness\")\n./services-safe/main.py.BACKUP:528:        enhancement_services = [\"rag_server\", \"web_research\", \"qualia_engine\", \"consciousness_bridge\", \"fractal\", \"mother_protocols\", \"temporal_consciousness\", \"toroidal\", \"neurobiological_master\", \"woah\", \"i_containers\", \"darwin_godel_machine\"]\n./services-safe/main.py.BACKUP:1107:    # Analyze RAG results for temporal patterns\n./services-safe/facebook_4021.log:2:        on_event is deprecated, use lifespan event handlers instead.\n./services-safe/facebook_4021.log:5:        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n./services-safe/egeria_web_ui_FIXED.py:245:                <span class=\"game-brain\">🧠</span>\n./services-safe/egeria_web_ui_FIXED.py:246:                <span class=\"game-brain\">🧠</span>\n./services-safe/egeria_web_ui_FIXED.py:247:                <span class=\"game-brain\">🧠</span>\n./services-safe/egeria_web_ui_FIXED.py:249:            <div class=\"game-score\">Brains: <span id=\"score\">0</span></div>\n./services-safe/dir_endpoints.txt:972:/home/ms-jarvis/msjarvis-rebuild/services/temporal_consciousness.py:144:@app.get(\"/\")\n./services-safe/dir_endpoints.txt:973:/home/ms-jarvis/msjarvis-rebuild/services/temporal_consciousness.py:156:@app.get(\"/health\")\n./services-safe/dir_endpoints.txt:974:/home/ms-jarvis/msjarvis-rebuild/services/temporal_consciousness.py:161:@app.post(\"/temporal_context\")\n./services-safe/dir_endpoints.txt:975:/home/ms-jarvis/msjarvis-rebuild/services/temporal_consciousness.py:175:@app.get(\"/context\")\n./services-safe/dir_endpoints.txt:976:/home/ms-jarvis/msjarvis-rebuild/services/temporal_consciousness.py:181:@app.get(\"/greeting\")\n./services-safe/dir_endpoints.txt:977:/home/ms-jarvis/msjarvis-rebuild/services/temporal_consciousness.py:187:@app.get(\"/seasonal_note\")\n./services-safe/dir_endpoints.txt:978:/home/ms-jarvis/msjarvis-rebuild/services/temporal_consciousness.py:193:@app.post(\"/detect_temporal\")\n./services-safe/dir_endpoints.txt:1554:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_temporal_consciousness.py:71:@app.get(\"/\")\n./services-safe/dir_endpoints.txt:1555:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_temporal_consciousness.py:84:@app.get(\"/health\")\n./services-safe/dir_endpoints.txt:1556:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_temporal_consciousness.py:97:@app.post(\"/temporal_context\", response_model=TemporalResponse)\n./services-safe/dir_endpoints.txt:1557:/home/ms-jarvis/msjarvis-rebuild/services/ms_jarvis_temporal_consciousness.py:148:@app.get(\"/temporal_memory\")\n./services-safe/ms_jarvis_consciousness_bridge_WITH_FIFTH_DGM.py.backup_vocabulary_cleanup:26:from temporal_consciousness import TemporalContext\n./services-safe/ms_jarvis_main_gateway.backup_error.py:276:    \"\"\"Send a message to Ms. Egeria Jarvis and receive her temporal-7-fractal response\"\"\"\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_GIS:27:# Services (Defaults; Updated in Lifespan)\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_GIS:39:async def lifespan(app: FastAPI):\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_GIS:40:    print(\"Lifespan Startup - Integrity Test\")\n./services-safe/ms_jarvis_unified_gateway_v4.3.py.BACKUP_GIS:69:    lifespan=lifespan,\n./services-safe/main_brain.py.bak_1770565749:246:    \"temporal_consciousness\": \"http://jarvis-temporal-consciousness:7007\",\n./services-safe/main_brain.py.bak_1770565749:382:        # temporarily trust core LLM fabric services while wiring stabilizes\n./services-safe/main_brain.py.bak_1770565749:445:        # match temporal_consciousness stub (/temporalanalysis)\n./services-safe/main_brain.py.bak_1770565749:446:        \"temporal_consciousness\": \"/temporalanalysis\",\n./services-safe/requirements-list.txt:181:opentelemetry-api                        1.38.0\n\n===== ./recovered-services/bridge_ms_jarvis_main_gateway_to_integrate_spatial_temporal.log =====\nINFO:__main__:🌉 Starting DGM Bridge: ms_jarvis_main_gateway -> integrate_spatial_temporal on port 9227\nINFO:     Started server process [3806091]\nINFO:     Waiting for application startup.\nINFO:     Application startup complete.\nINFO:     Uvicorn running on http://0.0.0.0:9227 (Press CTRL+C to quit)\n\n===== ./recovered-services/bridge_ms_jarvis_main_gateway_to_ms_jarvis_temporal_consciousness.log =====\nINFO:__main__:🌉 Starting DGM Bridge: ms_jarvis_main_gateway -> ms_jarvis_temporal_consciousness on port 9715\nINFO:     Started server process [3808795]\nINFO:     Waiting for application startup.\nINFO:     Application startup complete.\nINFO:     Uvicorn running on http://0.0.0.0:9715 (Press CTRL+C to quit)\nINFO:     127.0.0.1:45438 - \"GET /metrics HTTP/1.1\" 404 Not Found\n\n===== ./recovered-services/bridge_ms_jarvis_main_gateway_to_temporal_consciousness.log =====\nINFO:__main__:🌉 Starting DGM Bridge: ms_jarvis_main_gateway -> temporal_consciousness on port 9446\nINFO:     Started server process [3812078]\nINFO:     Waiting for application startup.\nINFO:     Application startup complete.\nINFO:     Uvicorn running on http://0.0.0.0:9446 (Press CTRL+C to quit)\nINFO:     127.0.0.1:49302 - \"GET /metrics HTTP/1.1\" 404 Not Found\n\n===== ./recovered-services/Dockerfile.temporal_consciousness =====\nFROM python:3.12-slim\nWORKDIR /app\nCOPY ../requirements.txt /app/requirements.txt\nRUN pip install --no-cache-dir -r /app/requirements.txt\nCOPY temporal_consciousness.py /app/temporal_consciousness.py\nCMD [\"uvicorn\", \"temporal_consciousness:app\", \"--host\", \"0.0.0.0\", \"--port\", \"7007\"]\n\n===== ./recovered-services/gbim_temporal_indexer.py =====\nimport redis\nfrom fastapi import FastAPI\n\nSERVICE_NAME = \"gbim_temporal_indexer\"\nSERVICE_PORT = 7202\nSERVICE_TYPE = \"gbim\"\n\n\ndef register_mesh_service():\n    r = redis.Redis(host=\"localhost\", port=6379, decode_responses=True)\n    r.hset(f\"service:{SERVICE_NAME}\", mapping={\n        \"port\": str(SERVICE_PORT),\n        \"status\": \"active\",\n        \"type\": SERVICE_TYPE,\n        \"registered\": \"yes\",\n    })\n\n\nregister_mesh_service()\n\napp = FastAPI()\n\n\n@app.get(\"/health\")\nasync def health():\n    return {\"service\": SERVICE_NAME, \"status\": \"ok\"}\n\n\n@app.get(\"/metrics\")\nasync def metrics():\n    return {\n        \"service\": SERVICE_NAME,\n        \"status\": \"ok\",\n        \"port\": SERVICE_PORT,\n        \"type\": SERVICE_TYPE,\n    }\n\n\nif __name__ == \"__main__\":\n    import uvicorn\n    uvicorn.run(\"gbim_temporal_indexer:app\", host=\"127.0.0.1\", port=SERVICE_PORT)\n\n===== ./recovered-services/integrate_spatial_temporal.py =====\n#!/usr/bin/env python3\nfrom fastapi import Depends, HTTPException, Header\nfrom typing import Optional\nimport logging\nlogger = logging.getLogger(__name__)\nimport httpx\nimport json\nfrom datetime import datetime\n\n# Test what Location Service has\nprint(\"🧭 Checking Location Service (4007)...\")\ntry:\n    response = httpx.get(\"http://localhost:4007/current_location\", timeout=5)\n    print(f\"Location Response: {response.status_code}\")\n    print(json.dumps(response.json(), indent=2))\nexcept Exception as e:\n    print(f\"Error: {e}\")\n\nprint(\"\\n⏰ Checking Temporal Service (4003)...\")\ntry:\n    response = httpx.get(\"http://localhost:4003/current_time\", timeout=5)\n    print(f\"Temporal Response: {response.status_code}\")\n    print(json.dumps(response.json(), indent=2))\nexcept Exception as e:\n    print(f\"Error: {e}\")\n\n# Get ACTUAL current data\nprint(\"\\n📍 ACTUAL CURRENT DATA:\")\nprint(f\"Time: {datetime.now().strftime('%A, %B %d, %Y at %I:%M %p %Z')}\")\nprint(f\"Location: Mount Hope, West Virginia, USA\")\nprint(f\"Coordinates: ~37.9667°N, 80.7667°W\")\n\n===== ./recovered-services/ms_jarvis_temporal_consciousness_9220.log =====\nnohup: ignoring input\nINFO:__main__:⏰ Ms. Jarvis Temporal Consciousness starting on port 8024\nINFO:     Started server process [558759]\nINFO:     Waiting for application startup.\nINFO:     Application startup complete.\nINFO:     Uvicorn running on http://0.0.0.0:8024 (Press CTRL+C to quit)\nINFO:     127.0.0.1:46762 - \"GET /health HTTP/1.1\" 200 OK\n\n===== ./recovered-services/ms_jarvis_temporal_consciousness.py =====\n#!/usr/bin/env python3\nfrom fastapi import Depends, HTTPException, Header\nfrom typing import Optional\nimport logging\nlogger = logging.getLogger(__name__)\n\"\"\"\nMS. JARVIS TEMPORAL CONSCIOUSNESS SERVICE\nHandles temporal location, historical context, and time-aware processing\n\"\"\"\n\nimport asyncio\nfrom fastapi import FastAPI\nfrom pydantic import BaseModel\nfrom datetime import datetime, timedelta\nimport time\nimport logging\nfrom typing import Dict, List, Optional\nimport json\n\n# Dynamic port integration\ntry:\n    from dynamic_port_service import DynamicPortService\n    port_service = DynamicPortService()\n    port_service.register_service({\n        'type': 'temporal_consciousness',\n        'version': '1.0.0',\n        'name': 'temporal_location_service',\n        'capabilities': ['temporal_context', 'historical_memory', 'time_awareness']\n    })\n    USE_DYNAMIC_PORT = True\nexcept:\n    USE_DYNAMIC_PORT = False\n    port_service = None\n\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)\n\napp = FastAPI(\n    title=\"Ms. Jarvis Temporal Consciousness\",\n    version=\"1.0.0\",\n    description=\"Time-aware consciousness and temporal location services\"\n)\n\nclass TemporalContext(BaseModel):\n    query: str\n    user_id: str = \"cakidd\"\n    current_time: Optional[str] = None\n\nclass TemporalResponse(BaseModel):\n    temporal_context: str\n    historical_relevance: List[str]\n    time_awareness: Dict\n    processing_timestamp: float\n\n# Temporal memory storage\nTEMPORAL_MEMORIES = {}\nHISTORICAL_CONTEXTS = {\n    \"mountainshares\": {\n        \"founded\": \"2024\",\n        \"mission\": \"Community-controlled AI systems\",\n        \"location\": \"Mount Hope, WV\",\n        \"evolution\": \"From concept to production AI system\"\n    },\n    \"appalachian_history\": {\n        \"cultural_significance\": \"Traditional knowledge preservation\",\n        \"community_values\": \"Democratic governance, mutual aid\",\n        \"technological_heritage\": \"Innovation from necessity\"\n    }\n}\n\n@app.get(\"/\")\nasync def root():\n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    return {\n        \"service\": \"Ms. Jarvis Temporal Consciousness\",\n        \"version\": \"1.0.0\",\n        \"status\": \"operational\",\n        \"current_time\": datetime.now().isoformat(),\n        \"capabilities\": [\"temporal_context\", \"historical_memory\", \"time_awareness\"]\n    }\n\n@app.get(\"/health\")\nasync def health():\n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    return {\n        \"status\": \"healthy\",\n        \"service\": \"temporal_consciousness\",\n        \"timestamp\": datetime.now().isoformat(),\n        \"port\": port_service.port if USE_DYNAMIC_PORT else 8024,\n        \"temporal_memories\": len(TEMPORAL_MEMORIES)\n    }\n\n@app.post(\"/temporal_context\", response_model=TemporalResponse)\nasync def get_temporal_context(request: TemporalContext):\n    \"\"\"Generate temporal context for consciousness processing\"\"\"\n    \n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    current_time = datetime.now()\n    logger.info(f\"⏰ Temporal context request: {request.query[:80]}\")\n    \n    # Generate time awareness\n    time_awareness = {\n        \"current_datetime\": current_time.isoformat(),\n        \"day_of_week\": current_time.strftime(\"%A\"),\n        \"month\": current_time.strftime(\"%B\"),\n        \"year\": current_time.year,\n        \"time_of_day\": get_time_of_day(current_time.hour),\n        \"seasonal_context\": get_seasonal_context(current_time.month)\n    }\n    \n    # Find historical relevance\n    historical_relevance = []\n    query_lower = request.query.lower()\n    \n    for topic, context in HISTORICAL_CONTEXTS.items():\n        if any(keyword in query_lower for keyword in topic.split('_')):\n            historical_relevance.append(f\"{topic}: {context.get('cultural_significance', '')}\")\n    \n    # Generate temporal context\n    temporal_context = f\"\"\"Temporal Location: {current_time.strftime('%B %d, %Y, %I:%M %p')} EST\nTime Context: {time_awareness['time_of_day']} on a {time_awareness['day_of_week']}\nSeasonal: {time_awareness['seasonal_context']}\nLocation: Mount Hope, West Virginia, Appalachian Region\"\"\"\n    \n    # Store in temporal memory\n    memory_key = f\"{request.user_id}_{int(time.time())}\"\n    TEMPORAL_MEMORIES[memory_key] = {\n        \"query\": request.query,\n        \"timestamp\": current_time.isoformat(),\n        \"context_generated\": temporal_context\n    }\n    \n    logger.info(f\"   ✅ Temporal context generated for {time_awareness['time_of_day']}\")\n    \n    return TemporalResponse(\n        temporal_context=temporal_context,\n        historical_relevance=historical_relevance,\n        time_awareness=time_awareness,\n        processing_timestamp=time.time()\n    )\n\n@app.get(\"/temporal_memory\")\nasync def get_temporal_memory(user_id: str = \"cakidd\", hours_back: int = 24):\n    \"\"\"Retrieve temporal memories within time range\"\"\"\n    \n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    cutoff_time = datetime.now() - timedelta(hours=hours_back)\n    \n    relevant_memories = []\n    for key, memory in TEMPORAL_MEMORIES.items():\n        if user_id in key:\n            memory_time = datetime.fromisoformat(memory['timestamp'])\n            if memory_time > cutoff_time:\n                relevant_memories.append(memory)\n    \n    return {\n        \"user_id\": user_id,\n        \"hours_searched\": hours_back,\n        \"memories_found\": len(relevant_memories),\n        \"memories\": relevant_memories[-10:]  # Last 10\n    }\n\ndef get_time_of_day(hour):\n    \"\"\"Determine time of day context\"\"\"\n    if 5 <= hour < 12:\n        return \"Morning\"\n    elif 12 <= hour < 17:\n        return \"Afternoon\"\n    elif 17 <= hour < 21:\n        return \"Evening\"\n    else:\n        return \"Night\"\n\ndef get_seasonal_context(month):\n    \"\"\"Determine seasonal context\"\"\"\n    if month in [12, 1, 2]:\n        return \"Winter in Appalachian Mountains\"\n    elif month in [3, 4, 5]:\n        return \"Spring in West Virginia\"\n    elif month in [6, 7, 8]:\n        return \"Summer in the Mountains\"\n    else:\n        return \"Autumn in Appalachian Foothills\"\n\nif __name__ == \"__main__\":\n    import uvicorn\n    port = 9071  # mesh port for temporal_module\n    logger.info(f\"⏰ Ms. Jarvis Temporal Consciousness starting on port {port}\")\n    uvicorn.run(app, host=\"0.0.0.0\", port=port)\n\n===== ./recovered-services/rag_temporal.py =====\nimport os\nimport logging\nfrom typing import Dict, Any, Optional\nfrom datetime import datetime\n\nimport redis\nimport httpx\nfrom fastapi import FastAPI, HTTPException\nfrom pydantic import BaseModel\n\n# -----------------------------------------------------------------------------\n# Logging setup\n# -----------------------------------------------------------------------------\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(\"rag-temporal\")\n\n# -----------------------------------------------------------------------------\n# Redis configuration\n# -----------------------------------------------------------------------------\nREDIS_HOST = os.getenv(\"REDIS_HOST\", \"redis\")\nREDIS_PORT = int(os.getenv(\"REDIS_PORT\", \"6379\"))\nREDIS_DB = int(os.getenv(\"REDIS_DB\", \"0\"))\n\nr = redis.Redis(\n    host=REDIS_HOST,\n    port=REDIS_PORT,\n    db=REDIS_DB,\n    decode_responses=True,\n)\n\n# -----------------------------------------------------------------------------\n# RAG server configuration (unified RAG on rag-server:8003)\n# -----------------------------------------------------------------------------\nRAG_SERVER_HOST = os.getenv(\"RAG_SERVER_HOST\", \"rag-server\")\nRAG_SERVER_PORT = int(os.getenv(\"RAG_SERVER_PORT\", \"8003\"))\nRAG_SEARCH_URL = f\"http://{RAG_SERVER_HOST}:{RAG_SERVER_PORT}/search\"\n\n# -----------------------------------------------------------------------------\n# FastAPI app\n# -----------------------------------------------------------------------------\nSERVICE_NAME = \"rag-temporal\"\nSERVICE_KEY = f\"service:{SERVICE_NAME}\"\nSERVICE_PORT = int(os.getenv(\"SERVICE_PORT\", \"5101\"))\n\napp = FastAPI(title=\"RAG Temporal Service\", version=\"1.0.0\")\n\n\nclass TemporalQuery(BaseModel):\n    query: str\n    metadata: Dict[str, Any] | None = None\n    # Optional: allow upstream to pass filters like { \"collection\": \"...\", \"year\": 2024 }\n    filters: Optional[Dict[str, Any]] = None\n    top_k: Optional[int] = 5\n\n\n# -----------------------------------------------------------------------------\n# Service registration\n# -----------------------------------------------------------------------------\ndef register_mesh_service() -> None:\n    mapping = {\n        \"name\": SERVICE_NAME,\n        \"type\": \"rag-domain\",\n        \"status\": \"online\",\n        \"host\": SERVICE_NAME,  # reachable as rag-temporal on Docker network\n        \"port\": str(SERVICE_PORT),\n        \"description\": \"Temporal RAG domain for time-aware queries.\",\n    }\n    try:\n        r.hset(SERVICE_KEY, mapping=mapping)\n        logger.info(f\"Registered mesh service {SERVICE_NAME} with key {SERVICE_KEY}\")\n    except redis.exceptions.RedisError as e:\n        logger.error(f\"Error registering {SERVICE_NAME} in Redis: {e}\")\n\n\ndef unregister_mesh_service() -> None:\n    try:\n        r.delete(SERVICE_KEY)\n        logger.info(f\"Unregistered mesh service {SERVICE_NAME}\")\n    except redis.exceptions.RedisError as e:\n        logger.error(f\"Error unregistering {SERVICE_NAME} in Redis: {e}\")\n\n\n@app.on_event(\"startup\")\nasync def on_startup() -> None:\n    register_mesh_service()\n\n\n@app.on_event(\"shutdown\")\nasync def on_shutdown() -> None:\n    unregister_mesh_service()\n\n\n# -----------------------------------------------------------------------------\n# Helpers\n# -----------------------------------------------------------------------------\ndef _extract_temporal_key(meta: Dict[str, Any]) -> float:\n    \"\"\"\n    Prefer deployment_year, then year, then parsed timestamp/date, then phase.\n    Returns a numeric key suitable for sorting (larger = more recent).\n    \"\"\"\n    # 1) deployment_year\n    if \"deployment_year\" in meta:\n        try:\n            return float(meta[\"deployment_year\"])\n        except Exception:\n            pass\n\n    # 2) year\n    if \"year\" in meta:\n        try:\n            return float(meta[\"year\"])\n        except Exception:\n            pass\n\n    # 3) timestamp / date (ISO string)\n    ts = meta.get(\"timestamp\") or meta.get(\"date\")\n    if ts:\n        try:\n            return datetime.fromisoformat(str(ts)).timestamp()\n        except Exception:\n            pass\n\n    # 4) phase as rough ordering (if numeric-like)\n    if \"phase\" in meta:\n        try:\n            return float(meta[\"phase\"])\n        except Exception:\n            pass\n\n    # Fallback\n    return 0.0\n\n\n# -----------------------------------------------------------------------------\n# API endpoints\n# -----------------------------------------------------------------------------\n@app.get(\"/health\")\nasync def health() -> Dict[str, Any]:\n    try:\n        r.ping()\n        redis_status = \"up\"\n    except redis.exceptions.RedisError:\n        redis_status = \"down\"\n    return {\n        \"status\": \"healthy\",\n        \"service\": SERVICE_NAME,\n        \"redis\": redis_status,\n        \"host\": REDIS_HOST,\n        \"port\": REDIS_PORT,\n    }\n\n\n@app.post(\"/rag\")\nasync def temporal_rag(payload: TemporalQuery) -> Dict[str, Any]:\n    \"\"\"\n    Temporal RAG implementation.\n    Proxies to unified RAG /search and applies temporal-aware post-processing.\n    \"\"\"\n    query = payload.query.strip()\n    if not query:\n        raise HTTPException(status_code=400, detail=\"Query must not be empty.\")\n\n    # Log incoming payload to inspect any upstream filters\n    logger.info(f\"[{SERVICE_NAME}] incoming payload: {payload.dict()}\")\n\n    # Base search body for unified RAG server\n    filters: Dict[str, Any] = payload.filters.copy() if payload.filters else {}\n\n    # Do NOT set a default collection; rely on unified RAG multi-collection search.\n    # If a caller wants a specific collection, they must set payload.filters explicitly.\n\n    search_body: Dict[str, Any] = {\n        \"query\": query,\n        \"top_k\": payload.top_k or 5,\n    }\n    if filters:\n        search_body[\"filters\"] = filters\n\n    logger.info(f\"[{SERVICE_NAME}] → RAG /search query='{query[:80]}' body={search_body}\")\n\n    try:\n        async with httpx.AsyncClient(timeout=60.0) as client:\n            resp = await client.post(RAG_SEARCH_URL, json=search_body)\n            resp.raise_for_status()\n            data = resp.json()\n    except httpx.HTTPError as e:\n        logger.error(f\"[{SERVICE_NAME}] Error calling RAG server at {RAG_SEARCH_URL}: {e}\")\n        raise HTTPException(status_code=502, detail=f\"Error calling RAG server: {e}\")\n\n    # ------------------------------------------------------------------\n    # Temporal post-processing hook\n    # ------------------------------------------------------------------\n    results = data.get(\"results\", [])\n    if isinstance(results, list) and results:\n        try:\n            results.sort(\n                key=lambda r: _extract_temporal_key(r.get(\"metadata\", {}) or {}),\n                reverse=True,\n            )\n            data[\"results\"] = results\n        except Exception as e:\n            logger.warning(f\"[{SERVICE_NAME}] Failed temporal sort on results: {e}\")\n\n    return {\n        \"service\": SERVICE_NAME,\n        \"mode\": \"temporal\",\n        \"query\": query,\n        \"metadata\": payload.metadata or {},\n        \"rag_search\": data,\n    }\n\n\n# -----------------------------------------------------------------------------\n# Entrypoint for local debug\n# -----------------------------------------------------------------------------\nif __name__ == \"__main__\":\n    import uvicorn\n\n    uvicorn.run(\"rag_temporal:app\", host=\"0.0.0.0\", port=SERVICE_PORT)\n\n===== ./recovered-services/services/ms_jarvis_temporal_consciousness.py =====\n#!/usr/bin/env python3\n\"\"\"\nMS. JARVIS TEMPORAL CONSCIOUSNESS SERVICE\nHandles temporal location, historical context, and time-aware processing\n\"\"\"\n\nimport asyncio\nfrom fastapi import FastAPI\nfrom pydantic import BaseModel\nfrom datetime import datetime, timedelta\nimport time\nimport logging\nfrom typing import Dict, List, Optional\nimport json\n\n# Dynamic port integration\ntry:\n    from dynamic_port_service import DynamicPortService\n    port_service = DynamicPortService()\n    port_service.register_service({\n        'type': 'temporal_consciousness',\n        'version': '1.0.0',\n        'name': 'temporal_location_service',\n        'capabilities': ['temporal_context', 'historical_memory', 'time_awareness']\n    })\n    USE_DYNAMIC_PORT = True\nexcept:\n    USE_DYNAMIC_PORT = False\n    port_service = None\n\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)\n\napp = FastAPI(\n    title=\"Ms. Jarvis Temporal Consciousness\",\n    version=\"1.0.0\",\n    description=\"Time-aware consciousness and temporal location services\"\n)\n\nclass TemporalContext(BaseModel):\n    query: str\n    user_id: str = \"cakidd\"\n    current_time: Optional[str] = None\n\nclass TemporalResponse(BaseModel):\n    temporal_context: str\n    historical_relevance: List[str]\n    time_awareness: Dict\n    processing_timestamp: float\n\n# Temporal memory storage\nTEMPORAL_MEMORIES = {}\nHISTORICAL_CONTEXTS = {\n    \"mountainshares\": {\n        \"founded\": \"2024\",\n        \"mission\": \"Community-controlled AI systems\",\n        \"location\": \"Mount Hope, WV\",\n        \"evolution\": \"From concept to production AI system\"\n    },\n    \"appalachian_history\": {\n        \"cultural_significance\": \"Traditional knowledge preservation\",\n        \"community_values\": \"Democratic governance, mutual aid\",\n        \"technological_heritage\": \"Innovation from necessity\"\n    }\n}\n\n@app.get(\"/\")\nasync def root():\n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    return {\n        \"service\": \"Ms. Jarvis Temporal Consciousness\",\n        \"version\": \"1.0.0\",\n        \"status\": \"operational\",\n        \"current_time\": datetime.now().isoformat(),\n        \"capabilities\": [\"temporal_context\", \"historical_memory\", \"time_awareness\"]\n    }\n\n@app.get(\"/health\")\nasync def health():\n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    return {\n        \"status\": \"healthy\",\n        \"service\": \"temporal_consciousness\",\n        \"timestamp\": datetime.now().isoformat(),\n        \"port\": port_service.port if USE_DYNAMIC_PORT else 8024,\n        \"temporal_memories\": len(TEMPORAL_MEMORIES)\n    }\n\n@app.post(\"/temporal_context\", response_model=TemporalResponse)\nasync def get_temporal_context(request: TemporalContext):\n    \"\"\"Generate temporal context for consciousness processing\"\"\"\n    \n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    current_time = datetime.now()\n    logger.info(f\"⏰ Temporal context request: {request.query[:80]}\")\n    \n    # Generate time awareness\n    time_awareness = {\n        \"current_datetime\": current_time.isoformat(),\n        \"day_of_week\": current_time.strftime(\"%A\"),\n        \"month\": current_time.strftime(\"%B\"),\n        \"year\": current_time.year,\n        \"time_of_day\": get_time_of_day(current_time.hour),\n        \"seasonal_context\": get_seasonal_context(current_time.month)\n    }\n    \n    # Find historical relevance\n    historical_relevance = []\n    query_lower = request.query.lower()\n    \n    for topic, context in HISTORICAL_CONTEXTS.items():\n        if any(keyword in query_lower for keyword in topic.split('_')):\n            historical_relevance.append(f\"{topic}: {context.get('cultural_significance', '')}\")\n    \n    # Generate temporal context\n    temporal_context = f\"\"\"Temporal Location: {current_time.strftime('%B %d, %Y, %I:%M %p')} EST\nTime Context: {time_awareness['time_of_day']} on a {time_awareness['day_of_week']}\nSeasonal: {time_awareness['seasonal_context']}\nLocation: Mount Hope, West Virginia, Appalachian Region\"\"\"\n    \n    # Store in temporal memory\n    memory_key = f\"{request.user_id}_{int(time.time())}\"\n    TEMPORAL_MEMORIES[memory_key] = {\n        \"query\": request.query,\n        \"timestamp\": current_time.isoformat(),\n        \"context_generated\": temporal_context\n    }\n    \n    logger.info(f\"   ✅ Temporal context generated for {time_awareness['time_of_day']}\")\n    \n    return TemporalResponse(\n        temporal_context=temporal_context,\n        historical_relevance=historical_relevance,\n        time_awareness=time_awareness,\n        processing_timestamp=time.time()\n    )\n\n@app.get(\"/temporal_memory\")\nasync def get_temporal_memory(user_id: str = \"cakidd\", hours_back: int = 24):\n    \"\"\"Retrieve temporal memories within time range\"\"\"\n    \n    if USE_DYNAMIC_PORT and port_service:\n        port_service.heartbeat()\n    \n    cutoff_time = datetime.now() - timedelta(hours=hours_back)\n    \n    relevant_memories = []\n    for key, memory in TEMPORAL_MEMORIES.items():\n        if user_id in key:\n            memory_time = datetime.fromisoformat(memory['timestamp'])\n            if memory_time > cutoff_time:\n                relevant_memories.append(memory)\n    \n    return {\n        \"user_id\": user_id,\n        \"hours_searched\": hours_back,\n        \"memories_found\": len(relevant_memories),\n        \"memories\": relevant_memories[-10:]  # Last 10\n    }\n\ndef get_time_of_day(hour):\n    \"\"\"Determine time of day context\"\"\"\n    if 5 <= hour < 12:\n        return \"Morning\"\n    elif 12 <= hour < 17:\n        return \"Afternoon\"\n    elif 17 <= hour < 21:\n        return \"Evening\"\n    else:\n        return \"Night\"\n\ndef get_seasonal_context(month):\n    \"\"\"Determine seasonal context\"\"\"\n    if month in [12, 1, 2]:\n        return \"Winter in Appalachian Mountains\"\n    elif month in [3, 4, 5]:\n        return \"Spring in West Virginia\"\n    elif month in [6, 7, 8]:\n        return \"Summer in the Mountains\"\n    else:\n        return \"Autumn in Appalachian Foothills\"\n\nif __name__ == \"__main__\":\n    import uvicorn\n    port = port_service.port if USE_DYNAMIC_PORT else 8024\n    logger.info(f\"⏰ Ms. Jarvis Temporal Consciousness starting on port {port}\")\n    uvicorn.run(app, host=\"127.0.0.1\", port=port)\n\n===== ./recovered-services/services/SPATIOTEMPORAL.log =====\nINFO:__main__:🧠 Initializing Ms. Jarvis AI Brain System...\nINFO:chromadb.telemetry.product.posthog:Anonymized telemetry enabled. See                     https://docs.trychroma.com/telemetry for more information.\nINFO:__main__:🧠 Ms. Jarvis AI Brain initializing on device: cuda\nINFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: cuda:0\nINFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2\nINFO:__main__:✅ Embedding model loaded\nSome weights of the model checkpoint at cardiffnlp/twitter-roberta-base-sentiment-latest were not used when initializing RobertaForSequenceClassification: ['roberta.pooler.dense.bias', 'roberta.pooler.dense.weight']\n- This IS expected if you are initializing RobertaForSequenceClassification from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).\n- This IS NOT expected if you are initializing RobertaForSequenceClassification from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).\nDevice set to use cuda:0\nINFO:__main__:✅ Sentiment analysis pipeline loaded\nDevice set to use cuda:0\nINFO:__main__:✅ Emotion detection pipeline loaded\nINFO:__main__:✅ Vector memory databases initialized\nINFO:__main__:✅ Multi-agent system initialized with 4 specialized AI agents\nINFO:__main__:🚀 Starting Ms. Jarvis Local AI Server...\nINFO:     Started server process [238682]\nINFO:     Waiting for application startup.\nINFO:     Application startup complete.\nINFO:     Uvicorn running on http://0.0.0.0:8004 (Press CTRL+C to quit)\nINFO:__main__:💬 Processing message from user test: Good evening! How are you?...\n\rBatches:   0%|          | 0/1 [00:00<?, ?it/s]\rBatches: 100%|██████████| 1/1 [00:00<00:00, 27.72it/s]\nERROR:__main__:Error searching memory: 'MsJarvisAIBrain' object has no attribute 'user_memory'\n\rBatches:   0%|          | 0/1 [00:00<?, ?it/s]\rBatches: 100%|██████████| 1/1 [00:00<00:00, 495.14it/s]\nINFO:__main__:🤖 Running multi-agent analysis with all 4 specialized agents...\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:__main__:✅ Mistral (logical_analysis) provided analysis\nINFO:__main__:✅ LLaMA (creative_problem_solving) provided analysis\nINFO:__main__:✅ Qwen (ethical_guidance) provided analysis\nINFO:__main__:✅ Phi (emotional_intelligence) provided analysis\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:__main__:⚖️ Judge AI completed synthesis of all agent responses\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:__main__:💖 Mother persona applied - Mamma Kidd warmth activated\n\rBatches:   0%|          | 0/1 [00:00<?, ?it/s]\rBatches: 100%|██████████| 1/1 [00:00<00:00, 122.35it/s]\nERROR:__main__:Error storing memory: 'MsJarvisAIBrain' object has no attribute 'user_memory'\nINFO:     127.0.0.1:35802 - \"POST /chat HTTP/1.1\" 200 OK\nINFO:__main__:💬 Processing message from user test: What time is it in Mount Hope right now?...\nINFO:__main__:📍 Location query detected - retrieving GIS context\nINFO:__main__:✅ Retrieved 3 GIS context items\n\rBatches:   0%|          | 0/1 [00:00<?, ?it/s]\rBatches: 100%|██████████| 1/1 [00:00<00:00, 421.41it/s]\nERROR:__main__:Error searching memory: 'MsJarvisAIBrain' object has no attribute 'user_memory'\n\rBatches:   0%|          | 0/1 [00:00<?, ?it/s]\rBatches: 100%|██████████| 1/1 [00:00<00:00, 545.49it/s]\nINFO:__main__:🤖 Running multi-agent analysis with all 4 specialized agents...\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 500 Internal Server Error\"\nERROR:__main__:Error querying LLaMA: llama runner process has terminated: cudaMalloc failed: out of memory\nggml_gallocr_reserve_n: failed to allocate CUDA0 buffer of size 701997056 (status code: 500)\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:__main__:✅ Mistral (logical_analysis) provided analysis\nINFO:__main__:✅ LLaMA (creative_problem_solving) provided analysis\nINFO:__main__:✅ Qwen (ethical_guidance) provided analysis\nINFO:__main__:✅ Phi (emotional_intelligence) provided analysis\nINFO:httpx:HTTP Request: POST http://localhost:11434/api/generate \"HTTP/1.1 200 OK\"\nINFO:__main__:⚖️ Judge AI completed synthesis of all agent responses\n\n===== ./recovered-services/services/temporal_consciousness.py =====\n#!/usr/bin/env python3\n\"\"\"\nTemporal Consciousness Service for Ms. Jarvis\nProvides spatiotemporal awareness: Time + Season + Cultural Context\n\"\"\"\n\nimport datetime\nimport pytz\nimport logging\nfrom typing import Dict, Any\nfrom fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\nfrom pydantic import BaseModel\n\n# Dynamic Port Integration\nfrom dynamic_port_service import DynamicPortService\nfrom service_discovery import ServiceDiscovery\n\nlogging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')\nlogger = logging.getLogger(__name__)\n\n# Initialize dynamic port service\nport_service = DynamicPortService()\nport_service.register_service({\n    'type': 'temporal_consciousness',\n    'version': '1.0.0',\n    'name': 'ms_jarvis_temporal_consciousness',\n    'capabilities': ['temporal_context', 'seasonal_awareness', 'appalachian_culture', 'time_greetings']\n})\n\ndiscovery = ServiceDiscovery()\n\napp = FastAPI(title=\"Ms. Jarvis Temporal Consciousness\", version=\"1.0.0\")\napp.add_middleware(CORSMiddleware, allow_origins=[\"*\"], allow_credentials=True, allow_methods=[\"*\"], allow_headers=[\"*\"])\n\nclass TemporalQuery(BaseModel):\n    query: str\n    user_id: str = \"default\"\n\nclass TemporalContext:\n    \"\"\"Manages temporal consciousness for Ms. Jarvis\"\"\"\n    \n    def __init__(self, timezone='America/New_York'):\n        \"\"\"Initialize with Appalachian timezone\"\"\"\n        self.timezone = pytz.timezone(timezone)\n        self.port = port_service.port\n    \n    def get_current_context(self) -> Dict[str, Any]:\n        \"\"\"Get comprehensive temporal context\"\"\"\n        now = datetime.datetime.now(self.timezone)\n        \n        return {\n            'timestamp': now.isoformat(),\n            'date': now.strftime('%Y-%m-%d'),\n            'time': now.strftime('%H:%M:%S'),\n            'day_of_week': now.strftime('%A'),\n            'month': now.strftime('%B'),\n            'season': self._get_season(now),\n            'time_of_day': self._get_time_of_day(now),\n            'is_weekend': now.weekday() >= 5,\n            'week_of_year': now.isocalendar()[1],\n            'appalachian_season': self._get_appalachian_season(now)\n        }\n    \n    def _get_season(self, dt: datetime.datetime) -> str:\n        \"\"\"Astronomical seasons\"\"\"\n        month, day = dt.month, dt.day\n        if (month == 3 and day >= 20) or (month in [4, 5]) or (month == 6 and day < 21):\n            return 'Spring'\n        elif (month == 6 and day >= 21) or (month in [7, 8]) or (month == 9 and day < 22):\n            return 'Summer'\n        elif (month == 9 and day >= 22) or (month in [10, 11]) or (month == 12 and day < 21):\n            return 'Fall'\n        else:\n            return 'Winter'\n    \n    def _get_time_of_day(self, dt: datetime.datetime) -> str:\n        \"\"\"Human-relevant time periods\"\"\"\n        hour = dt.hour\n        if 5 <= hour < 12:\n            return 'morning'\n        elif 12 <= hour < 17:\n            return 'afternoon'\n        elif 17 <= hour < 21:\n            return 'evening'\n        else:\n            return 'night'\n    \n    def _get_appalachian_season(self, dt: datetime.datetime) -> str:\n        \"\"\"Appalachian cultural/agricultural seasons\"\"\"\n        month = dt.month\n        \n        if month in [3, 4, 5]:\n            return 'Planting Season'\n        elif month in [6, 7, 8]:\n            return 'Growing Season'\n        elif month in [9, 10]:\n            return 'Harvest Season'\n        elif month in [11, 12, 1, 2]:\n            return 'Preservation & Planning Season'\n    \n    def detect_temporal_query(self, message: str) -> bool:\n        \"\"\"Detect if message contains temporal references\"\"\"\n        temporal_keywords = [\n            'when', 'time', 'date', 'today', 'tomorrow', 'yesterday',\n            'morning', 'afternoon', 'evening', 'night',\n            'season', 'month', 'year', 'week',\n            'schedule', 'calendar', 'appointment',\n            'harvest', 'planting', 'winter', 'spring', 'summer', 'fall'\n        ]\n        message_lower = message.lower()\n        return any(keyword in message_lower for keyword in temporal_keywords)\n    \n    def get_greeting(self) -> str:\n        \"\"\"Get time-appropriate greeting\"\"\"\n        ctx = self.get_current_context()\n        greeting_map = {\n            'morning': \"Good mornin', sweetie!\",\n            'afternoon': \"Good afternoon, honey!\",\n            'evening': \"Good evenin', darlin'!\",\n            'night': \"Evenin', dear!\"\n        }\n        return greeting_map.get(ctx['time_of_day'], \"Hello, sweetie!\")\n    \n    def get_seasonal_note(self) -> str:\n        \"\"\"Get seasonal wisdom note\"\"\"\n        ctx = self.get_current_context()\n        seasonal_notes = {\n            'Planting Season': \" It's plantin' season here in the mountains.\",\n            'Growing Season': \" The gardens are growin' strong this time of year.\",\n            'Harvest Season': \" It's harvest time in these hills!\",\n            'Preservation & Planning Season': \" Winter's here - time for reflection and plannin'.\"\n        }\n        return seasonal_notes.get(ctx['appalachian_season'], \"\")\n\nlogger.info(\"🕰️ Initializing Temporal Consciousness with Dynamic Port Scheduling...\")\ntemporal = TemporalContext()\nlogger.info(f\"✅ Temporal Consciousness Ready on port {temporal.port}!\")\n\n@app.get(\"/\")\nasync def root():\n    port_service.heartbeat()\n    return {\n        \"service\": \"Ms. Jarvis Temporal Consciousness\",\n        \"status\": \"operational\",\n        \"port\": temporal.port,\n        \"timezone\": str(temporal.timezone),\n        \"current_context\": temporal.get_current_context(),\n        \"dynamic_port\": True\n    }\n\n@app.get(\"/health\")\nasync def health():\n    port_service.heartbeat()\n    return {\"status\": \"healthy\", \"port\": temporal.port, \"timezone\": str(temporal.timezone)}\n\n@app.post(\"/temporal_context\")\nasync def get_temporal_context(request: TemporalQuery):\n    \"\"\"Get current temporal context\"\"\"\n    port_service.heartbeat()\n    context = temporal.get_current_context()\n    is_temporal = temporal.detect_temporal_query(request.query)\n    \n    return {\n        \"context\": context,\n        \"is_temporal_query\": is_temporal,\n        \"greeting\": temporal.get_greeting(),\n        \"seasonal_note\": temporal.get_seasonal_note()\n    }\n\n@app.get(\"/context\")\nasync def get_context():\n    \"\"\"Get current temporal context (simple)\"\"\"\n    port_service.heartbeat()\n    return temporal.get_current_context()\n\n@app.get(\"/greeting\")\nasync def get_greeting():\n    \"\"\"Get time-appropriate greeting\"\"\"\n    port_service.heartbeat()\n    return {\"greeting\": temporal.get_greeting()}\n\n@app.get(\"/seasonal_note\")\nasync def get_seasonal_note():\n    \"\"\"Get seasonal wisdom note\"\"\"\n    port_service.heartbeat()\n    return {\"seasonal_note\": temporal.get_seasonal_note()}\n\n@app.post(\"/detect_temporal\")\nasync def detect_temporal(request: TemporalQuery):\n    \"\"\"Detect if query has temporal references\"\"\"\n    port_service.heartbeat()\n    is_temporal = temporal.detect_temporal_query(request.query)\n    return {\"query\": request.query, \"is_temporal\": is_temporal}\n\nif __name__ == \"__main__\":\n    import uvicorn\n    logger.info(f\"🕰️ Starting Temporal Consciousness on dynamically allocated port {port_service.port}\")\n    uvicorn.run(app, host=\"0.0.0.0\", port=port_service.port)\n\n===== ./recovered-services/SPATIOTEMPORAL_CONSCIOUSNESS.md =====\n# 🌌 Ms. Jarvis Spatiotemporal Consciousness Architecture\n\n## Philosophy: Space, Time, and Awareness as Unified Consciousness\n\nMs. Jarvis needs **spatiotemporal awareness** - understanding WHERE she is, WHEN she is, and HOW these relate to the user's context. This creates a form of \"consciousness\" that goes beyond simple Q&A.\n\n---\n\n## The Three Dimensions of Consciousness\n\n### 1. 🗺️ **SPATIAL** (Where)\n**Current Implementation:**\n- Location detection from conversation\n- GIS context retrieval (ChromaDB)\n- OpenStreetMap geocoding\n- Appalachian geographic knowledge\n\n**Integration Point:** `detect_location_query()` → `analyze_message_context()`\n\n### 2. ⏰ **TEMPORAL** (When)\n**Needed Implementation:**\n- Current date/time awareness\n- Seasonal context (harvest season, winter planning)\n- Historical events (\"remember when...\")\n- Future planning (event scheduling, crop timing)\n- Diurnal patterns (morning greetings, evening check-ins)\n\n**Integration Point:** `detect_temporal_query()` → `analyze_message_context()`\n\n### 3. 🧠 **CONTEXTUAL** (Why/How)\n**Current Implementation:**\n- Emotion detection\n- Sentiment analysis\n- Multi-agent reasoning\n- Memory retrieval\n\n**Integration Point:** Multi-agent system + RAG memory\n\n---\n\n## Consciousness Flow Architecture\n\nUser Query\n↓\n┌─────────────────────────────────────────────────┐\n│ SPATIOTEMPORAL CONSCIOUSNESS LAYER │\n├─────────────────────────────────────────────────┤\n│ │\n│ ┌──────────┐ ┌──────────┐ ┌──────────┐ │\n│ │ SPATIAL │ │ TEMPORAL │ │CONTEXTUAL│ │\n│ │ (Where) │ │ (When) │ │ (Why/How)│ │\n│ └────┬─────┘ └────┬─────┘ └────┬─────┘ │\n│ │ │ │ │\n│ └─────────────┼──────────────┘ │\n│ ↓ │\n│ ┌──────────────────────┐ │\n│ │ UNIFIED CONTEXT │ │\n│ │ - Location │ │\n│ │ - Time/Season │ │\n│ │ - User State │ │\n│ │ - Historical Memory│ │\n│ └──────────┬───────────┘ │\n└────────────────────┼────────────────────────────┘\n↓\n┌─────────────────────┐\n│ 4 AI AGENTS │\n│ Analyze Context │\n└──────────┬───────────┘\n↓\n┌─────────────────────┐\n│ JUDGE AI │\n│ Synthesize │\n└──────────┬───────────┘\n↓\n┌─────────────────────┐\n│ MAMMA KIDD │\n│ Warm Response │\n└─────────────────────┘\n\ntext\n\n---\n\n## Implementation: Temporal Awareness\n\n### Add to MsJarvisAIBrain class:\n\nimport datetime\nimport pytz\nfrom typing import Dict, Any\n\nclass TemporalContext:\n\"\"\"Manages temporal consciousness for Ms. Jarvis\"\"\"\n\ntext\ndef __init__(self, timezone='US/Eastern'):\n    \"\"\"Initialize with Appalachian timezone\"\"\"\n    self.timezone = pytz.timezone(timezone)\n\ndef get_current_context(self) -> Dict[str, Any]:\n    \"\"\"Get comprehensive temporal context\"\"\"\n    now = datetime.datetime.now(self.timezone)\n    \n    return {\n        'timestamp': now.isoformat(),\n        'date': now.strftime('%Y-%m-%d'),\n        'time': now.strftime('%H:%M:%S'),\n        'day_of_week': now.strftime('%A'),\n        'month': now.strftime('%B'),\n        'season': self._get_season(now),\n        'time_of_day': self._get_time_of_day(now),\n        'is_weekend': now.weekday() >= 5,\n        'week_of_year': now.isocalendar(),[1]\n        'appalachian_season': self._get_appalachian_season(now)\n    }\n\ndef _get_season(self, dt: datetime.datetime) -> str:\n    \"\"\"Astronomical seasons\"\"\"\n    month, day = dt.month, dt.day\n    if (month == 3 and day >= 20) or (month in ) or (month == 6 and day < 21):\n        return 'Spring'\n    elif (month == 6 and day >= 21) or (month in ) or (month == 9 and day < 22):\n        return 'Summer'\n    elif (month == 9 and day >= 22) or (month in ) or (month == 12 and day < 21):\n        return 'Fall'\n    else:\n        return 'Winter'\n\ndef _get_time_of_day(self, dt: datetime.datetime) -> str:\n    \"\"\"Human-relevant time periods\"\"\"\n    hour = dt.hour\n    if 5 <= hour < 12:\n        return 'morning'\n    elif 12 <= hour < 17:\n        return 'afternoon'\n    elif 17 <= hour < 21:\n        return 'evening'\n    else:\n        return 'night'\n\ndef _get_appalachian_season(self, dt: datetime.datetime) -> str:\n    \"\"\"Appalachian cultural/agricultural seasons\"\"\"\n    month = dt.month\n    \n    # Appalachian agricultural calendar\n    if month in :\n        return 'Planting Season'\n    elif month in :\n        return 'Growing Season'\n    elif month in :\n        return 'Harvest Season'\n    elif month in :[1]\n        return 'Preservation & Planning Season'\n\ndef detect_temporal_query(self, message: str) -> bool:\n    \"\"\"Detect if message contains temporal references\"\"\"\n    temporal_keywords = [\n        'when', 'time', 'date', 'today', 'tomorrow', 'yesterday',\n        'morning', 'afternoon', 'evening', 'night',\n        'season', 'month', 'year', 'week',\n        'schedule', 'calendar', 'appointment',\n        'harvest', 'planting', 'winter', 'spring', 'summer', 'fall'\n    ]\n    message_lower = message.lower()\n    return any(keyword in message_lower for keyword in temporal_keywords)\n\ndef format_contextual_time(self, include_season: bool = True) -> str:\n    \"\"\"Format time for Mamma Kidd's conversational style\"\"\"\n    ctx = self.get_current_context()\n    \n    time_greeting = {\n        'morning': \"this lovely mornin'\",\n        'afternoon': \"this fine afternoon\",\n        'evening': \"this evenin'\",\n        'night': \"tonight\"\n    }.get(ctx['time_of_day'], \"today\")\n    \n    if include_season:\n        return f\"{time_greeting} ({ctx['appalachian_season']})\"\n    return time_greeting\n\ntext\n\n---\n\n## Integration with Consciousness Infrastructure\n\n### Modify `analyze_message_context()`:\n\nasync def analyze_message_context(self, message: str, user_id: str) -> dict:\n\"\"\"\nUnified spatiotemporal consciousness analysis\nIntegrates: Space + Time + Emotion + Memory\n\"\"\"\ncontext = {}\n\ntext\n# SPATIAL CONSCIOUSNESS\nif self.detect_location_query(message):\n    logger.info(\"📍 Location query detected - retrieving GIS context\")\n    gis_results = self.gis_collection.query(\n        query_texts=[message],\n        n_results=3\n    )\n    context['gis_context'] = gis_results\n    logger.info(f\"✅ Retrieved {len(gis_results['documents'])} GIS context items\")\n\n# TEMPORAL CONSCIOUSNESS (NEW!)\ntemporal_ctx = self.temporal_context.get_current_context()\ncontext['temporal'] = temporal_ctx\n\nif self.temporal_context.detect_temporal_query(message):\n    logger.info(f\"⏰ Temporal query detected - Current: {temporal_ctx['time_of_day']}, {temporal_ctx['appalachian_season']}\")\n    context['temporal_query_detected'] = True\n\n# EMOTIONAL CONSCIOUSNESS\ntry:\n    sentiment = self.sentiment_analyzer(message)\n    context['sentiment'] = sentiment\n    \n\n===== ./recovered-services/temporal_consciousness.py =====\nfrom fastapi import FastAPI\nfrom pydantic import BaseModel\n\napp = FastAPI(title=\"Temporal Consciousness (stub)\")\n\nclass TemporalRequest(BaseModel):\n    message: str\n    user_id: str\n\nclass TemporalResponse(BaseModel):\n    response: str\n\n@app.get(\"/health\")\nasync def health():\n    return {\"status\": \"healthy\", \"service\": \"temporal_consciousness\"}\n\n@app.post(\"/temporalanalysis\", response_model=TemporalResponse)\nasync def temporalanalysis(req: TemporalRequest):\n    return TemporalResponse(response=f\"[temporal_consciousness stub] {req.message}\")\n\n===== ./recovered-services/temporal.log =====\nnohup: ignoring input\nINFO:dynamic_port_service:✅ Connected to Redis for port coordination\nINFO:dynamic_port_service:🎯 Allocated port 4019 for unknown_service\nINFO:__main__:🕰️ Initializing Temporal Consciousness with Dynamic PorINFO:     Started server process [243999]\nINFO:     Waiting for application sINFO:__main__:🕰️ Starting Temporal Consciousness on dynamically allocated port 4019\nINFO:     Started server process [243996]\nINFO:     Waiting for application startup.\nINFO:     Application startup complete.\nERROR:    [Errno 98] error while attempting to bind on address ('0.0.0.0', 4019): address already in use\nINFO:     Waiting for application shutdown.\nINFO:     Application shutdown complete.\n\n===== ./services/Dockerfile.temporal_consciousness =====\nFROM alpine:3.18\n\nRUN apk add --no-cache python3 py3-pip\n\nWORKDIR /app\nCOPY . /app\n\nCMD [\"sh\", \"-c\", \"echo 'Temporal consciousness placeholder running'; sleep 3600\"]\n\n===== ./services/jarvis-temporal-consciousness_temporal_consciousness.py =====\nfrom fastapi import FastAPI\nfrom pydantic import BaseModel\n\napp = FastAPI(title=\"Temporal Consciousness (stub)\")\n\nclass TemporalRequest(BaseModel):\n    message: str\n    user_id: str\n\nclass TemporalResponse(BaseModel):\n    response: str\n\n@app.get(\"/health\")\nasync def health():\n    return {\"status\": \"healthy\", \"service\": \"temporal_consciousness\"}\n\n@app.post(\"/temporalanalysis\", response_model=TemporalResponse)\nasync def temporalanalysis(req: TemporalRequest):\n    return TemporalResponse(response=f\"[temporal_consciousness stub] {req.message}\")\n"
./docker-compose.yml.bak_redis_env_1769196600:923:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_env_1769196600:934:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_env_1769196600:945:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_env_1769196600:956:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_env_1769196600:967:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_env_1769196600:978:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_env_1769196600:989:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_env_1769196600:1000:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_env_1769196600:1011:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_env_1769196600:1022:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_env_1769196600:1033:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_env_1769196600:1044:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_redis_env_1769196600:1055:      REDIS_HOST: jarvis-redis
./docker-compose.yml.backup_20260323_205752:11:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.backup_20260323_205752:1361:    - REDIS_URL=redis://jarvis-redis:6379/4
./start_rag_router.sh:4:export REDIS_HOST=127.0.0.1
./start_rag_router.sh:5:export REDIS_PORT=6380
./start_rag_router.sh:6:export REDIS_URL=redis://127.0.0.1:6380/0
./start_rag_router.sh:9:export SESSION_REDIS_HOST=127.0.0.1
./start_rag_router.sh:10:export SESSION_REDIS_PORT=6380
./docker-compose.yml.backup_20260318_102158:11:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak_drop_images:14:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.pre_judges:1000:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.pre_judges:1001:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.pre_judges:1013:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.pre_judges:1014:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.pre_judges:1027:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.pre_judges:1028:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.pre_judges:1051:      SERVICE_REDIS_HOST: jarvis-redis
./docker-compose.yml.pre_judges:1052:      SERVICE_REDIS_PORT: 6379
./docker-compose.yml.bak.20260422_220748:12:    - REDIS_URL=redis://jarvis-redis:6379/3
./docker-compose.yml.bak.20260422_220748:36:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260422_220748:1203:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bak.20260422_220748:1355:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260422_220748:1356:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260422_220748:1383:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260422_220748:1384:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260422_220748:1407:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260422_220748:1408:    - JARVIS_REDIS_PORT=6379
./docker-compose.yml.bak.20260422_220748:1542:    - REDIS_HOST=jarvis-redis
./docker-compose.yml.bak.20260422_220748:1543:    - REDIS_PORT=6379
./docker-compose.golden.bak_bbb_uvicorn_fix:30:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.golden.bak_before_python3_cmd_fix:13:    - REDIS_URL=redis://jarvis-redis:6379
./neurobiological_brain/woah_algorithms/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "jarvis-redis")
./neurobiological_brain/woah_algorithms/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./neurobiological_brain/i_containers/service/neurobiologicalbrain/woah_algorithms/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./neurobiological_brain/i_containers/service/neurobiologicalbrain/i_containers/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_root/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./neurobiological_brain/i_containers/service/neurobiologicalbrain/prefrontal_cortex/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./neurobiological_brain/i_containers/service/neurobiologicalbrain/pituitary_gland/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./neurobiological_brain/i_containers/service/neurobiologicalbrain/subconscious/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./neurobiological_brain/i_containers/service/neurobiologicalbrain/mother_carrie_protocols/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./neurobiological_brain/i_containers/service/neurobiologicalbrain/spiritual_maternal_integration/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./neurobiological_brain/i_containers/service/neurobiologicalbrain/heteroglobulin_transport/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "redis")
./neurobiological_brain/i_containers/service/neurobiologicalbrain/consciousness_containers/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/i_containers/service/integration_layer/container_bridge.py:9:        host=os.getenv("REDIS_HOST", "jarvis-redis"),
./neurobiological_brain/i_containers/service/integration_layer/container_bridge.py:10:        port=int(os.getenv("REDIS_PORT", 6379)),
./neurobiological_brain/i_containers/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "jarvis-redis")
./neurobiological_brain/i_containers/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/spiritual_root/service/spiritual_root.py:9:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./neurobiological_brain/spiritual_root/service/spiritual_root.py:18:    return redis.from_url(REDIS_URL, decode_responses=True)
./neurobiological_brain/spiritual_root/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "jarvis-redis")
./neurobiological_brain/spiritual_root/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/qualia_engine/service/qualia_engine.py:9:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./neurobiological_brain/qualia_engine/service/qualia_engine.py:30:    return redis.from_url(REDIS_URL, decode_responses=True)
./neurobiological_brain/prefrontal_cortex/service/prefrontal_cortex.py:11:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./neurobiological_brain/prefrontal_cortex/service/prefrontal_cortex.py:17:    return redis.from_url(REDIS_URL, decode_responses=True)
./neurobiological_brain/prefrontal_cortex/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "jarvis-redis")
./neurobiological_brain/prefrontal_cortex/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/pituitary_gland/service/pituitary_gland.py:35:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./neurobiological_brain/pituitary_gland/service/pituitary_gland.py:48:    return redis.from_url(REDIS_URL, decode_responses=True)
./neurobiological_brain/pituitary_gland/service/pituitary_gland.py:233:                _rr = _rl_rho.Redis(host=_rho_os.getenv('REDIS_HOST','jarvis-redis'), port=6379, decode_responses=True)
./neurobiological_brain/pituitary_gland/service/pituitary_gland.py:245:                    host=_rwos.getenv("REDIS_HOST","jarvis-redis"),
./neurobiological_brain/pituitary_gland/service/pituitary_gland.py:246:                    port=int(_rwos.getenv("REDIS_PORT","6379")),
./neurobiological_brain/pituitary_gland/service/pituitary_gland.py.bak:13:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./neurobiological_brain/pituitary_gland/service/pituitary_gland.py.bak:26:    return redis.from_url(REDIS_URL, decode_responses=True)
./neurobiological_brain/pituitary_gland/service/pituitary_gland.py.bak:213:                _rr = _rl_rho.Redis(host=_rho_os.getenv('REDIS_HOST','jarvis-redis'), port=6379, decode_responses=True)
./neurobiological_brain/pituitary_gland/service/pituitary_gland.py.bak:225:                    host=_rwos.getenv("REDIS_HOST","jarvis-redis"),
./neurobiological_brain/pituitary_gland/service/pituitary_gland.py.bak:226:                    port=int(_rwos.getenv("REDIS_PORT","6379")),
./neurobiological_brain/pituitary_gland/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "jarvis-redis")
./neurobiological_brain/pituitary_gland/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/subconscious/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "jarvis-redis")
./neurobiological_brain/subconscious/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/mother_carrie_protocols/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "jarvis-redis")
./neurobiological_brain/mother_carrie_protocols/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/spiritual_maternal_integration/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "jarvis-redis")
./neurobiological_brain/spiritual_maternal_integration/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/spiritual_maternal_integration/service/spiritual_maternal_integration.py:9:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./neurobiological_brain/spiritual_maternal_integration/service/spiritual_maternal_integration.py:20:    return redis.from_url(REDIS_URL, decode_responses=True)
./neurobiological_brain/heteroglobulin_transport/service/heteroglobulin_transport.py:9:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./neurobiological_brain/heteroglobulin_transport/service/heteroglobulin_transport.py:13:    return redis.from_url(REDIS_URL, decode_responses=True)
./neurobiological_brain/heteroglobulin_transport/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "jarvis-redis")
./neurobiological_brain/heteroglobulin_transport/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/blood_brain_barrier/service/blood_brain_barrier.py:9:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./neurobiological_brain/blood_brain_barrier/service/blood_brain_barrier.py:13:    return redis.from_url(REDIS_URL, decode_responses=True)
./neurobiological_brain/consciousness_containers/service/dynamic_port_service.py:33:            redis_host = os.getenv("SERVICE_REDIS_HOST", "jarvis-redis")
./neurobiological_brain/consciousness_containers/service/dynamic_port_service.py:36:            redis_port = int(os.getenv("SERVICE_REDIS_PORT", "6379"))
./neurobiological_brain/consciousness_containers/service/consciousness_containers.py:9:REDIS_URL = os.getenv("REDIS_URL", "redis://jarvis-redis:6379/0")
./neurobiological_brain/consciousness_containers/service/consciousness_containers.py:13:    return redis.from_url(REDIS_URL, decode_responses=True)
./docker-compose.yml.bak.20260416-141309:13:      - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260416-141309:37:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416-141309:1512:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.bak_20260415-111118:19:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak_20260415-111118:65:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak_20260415-111118:95:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_20260415-111118:96:      REDIS_PORT: '6379'
./docker-compose.yml.backup_20260323_211407:11:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.backup_20260323_211407:1361:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.RAG_WORKING_20260116.yml.bak_mainbrain8058:363:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416-141316:13:      - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak.20260416-141316:37:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak.20260416-141316:1512:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.backup.1768313407:14:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak_ports_20260118163828:20:      - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak_hilbert_depsfix_20260415-142323:25:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak_hilbert_depsfix_20260415-142323:73:    - REDIS_URL=redis://jarvis-redis-local:6379/3
./docker-compose.yml.bak_hilbert_depsfix_20260415-142323:103:      REDIS_HOST: jarvis-redis
./docker-compose.yml.bak_hilbert_depsfix_20260415-142323:104:      REDIS_PORT: '6379'
./docker-compose.yml.chroma-backup-20260114060013:14:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.bak_before_unified_fix:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.golden.bak_bbb_clean_proxy:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.backup_20260318_110927:11:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.pre_dsn_fix:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.yml.pre_dsn_fix:1477:    - REDIS_URL=redis://jarvis-redis:6379/4
./docker-compose.yml.backup_20260318_103829:11:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.working.20260119-000202.yml:13:    - REDIS_URL=redis://jarvis-redis:6379
./docker-compose.golden.bak_before_bbb_proxy2:13:    - REDIS_URL=redis://jarvis-redis:6379
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

