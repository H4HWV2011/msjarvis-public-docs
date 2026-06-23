(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ cd /mnt/nvme1/msjarvis-rebuild

printf '\n===== 1. Confirm Chroma heartbeat on the correct host port =====\n'
curl -s http://127.0.0.1:8002/api/v2/heartbeat || true
echo
curl -s http://127.0.0.1:8002/api/v1/heartbeat || true
echo

printf '\n===== 2. Show Chroma health details =====\n'
docker inspect jarvis-chroma --format '{{json .State.Health}}' | python3 -m json.tool

printf '\n===== 3. Count collections from inside Hilbert =====\n'
docker exec jarvis-hilbert-spatial-chat python3 - <<'PY'
import os, json, chromadb
host = os.getenv('CHROMA_HOST', 'jarvis-chroma')
port = int(os.getenv('CHROMA_PORT', '8000'))
client = chromadb.HttpClient(host=host, port=port)
cols = client.list_collections()
names = [getattr(c, 'name', str(c)) for c in cols]
print(json.dumps({
    "host": host,
    "port": port,
    "collection_count": len(names),
    "collections": names[:50]
curl -s http://127.0.0.1:8235/health | python3 -m json.tool\n'e.override.yml services 2>/dev/null | head -200

===== 1. Confirm Chroma heartbeat on the correct host port =====
{"nanosecond heartbeat":1782244504720790583}
{"error":"Unimplemented","message":"The v1 API is deprecated. Please use /v2 apis"}

===== 2. Show Chroma health details =====
{
    "Status": "healthy",
    "FailingStreak": 0,
    "Log": [
        {
            "Start": "2026-06-23T15:54:26.484098208-04:00",
            "End": "2026-06-23T15:54:26.528287365-04:00",
            "ExitCode": 0,
            "Output": ""
        },
        {
            "Start": "2026-06-23T15:54:56.52936979-04:00",
            "End": "2026-06-23T15:54:56.593720794-04:00",
            "ExitCode": 0,
            "Output": ""
        }
    ]
}

===== 3. Count collections from inside Hilbert =====

===== 4. Check Neo4j container presence =====

===== 5. Find Neo4j references in source and compose =====
docker-compose.yml:1086:  neo4j:
docker-compose.yml:1087:    image: neo4j:5.13-community
docker-compose.yml:1088:    container_name: neo4j
docker-compose.yml:1090:      - 127.0.0.1:7687:7687
docker-compose.yml:1093:      - NEO4J_ACCEPT_LICENSE_AGREEMENT=yes
docker-compose.yml:1094:      - NEO4J_AUTH=neo4j/neo4jpassword
services/indexgrid15minutequads_wvgistc_utm83_attrs.csv:249:0,4376935.683730496,768710.2287298313,"POLYGON((757959.7716798313 4376562.347867112,757959.7716798313 4377309.01959388,779460.6857798314 4377309.01959388,779460.6857798314 4376562.347867112,757959.7716798313 4376562.347867112))",feat_0,indexgrid15minutequads_wvgistc_utm83,USA
services/indexgrid15minutequads_wvgistc_utm83_attrs.csv:265:0,4401698.784588736,660636.9380214557,"POLYGON((649927.1073256728 4401474.594010216,649927.1073256728 4401922.975167256,671346.7687172384 4401922.975167256,671346.7687172384 4401474.594010216,649927.1073256728 4401474.594010216))",feat_0,indexgrid15minutequads_wvgistc_utm83,USA
services/indexgrid15minutequads_wvgistc_utm83_attrs.csv:266:0,4402177.090945156,682056.8996618716,"POLYGON((671346.7687172384 4401922.975167256,671346.7687172384 4402431.206723057,692767.0306065048 4402431.206723057,692767.0306065048 4401922.975167256,671346.7687172384 4401922.975167256))",feat_0,indexgrid15minutequads_wvgistc_utm83,USA
services/indexgrid15minutequads_wvgistc_utm83_attrs.csv:319:0,4483329.768706052,468224.75584946544,"POLYGON((457632.98646784585 4483284.746308977,457632.98646784585 4483374.791103127,478816.5252310849 4483374.791103127,478816.5252310849 4483284.746308977,457632.98646784585 4483284.746308977))",feat_0,indexgrid15minutequads_wvgistc_utm83,USA
services/indexgrid15minutequads_wvgistc_utm83_attrs.csv:322:0,4483329.768706052,531775.2441505314,"POLYGON((521183.47476891184 4483284.746308977,521183.47476891184 4483374.791103127,542367.0135321509 4483374.791103127,542367.0135321509 4483284.746308977,521183.47476891184 4483284.746308977))",feat_0,indexgrid15minutequads_wvgistc_utm83,USA
services/indexgrid15minutequads_wvgistc_utm83_attrs.csv:591:0,4388048.502711222,671655.7687820196,"POLYGON((671346.7687172384 4374174.030255187,671346.7687172384 4401922.975167256,671964.7688468009 4401922.975167256,671964.7688468009 4374174.030255187,671346.7687172384 4374174.030255187))",feat_0,indexgrid15minutequads_wvgistc_utm83,USA
services/indexgrid15minutequads_wvgistc_utm83_attrs.csv:592:0,4415797.974154576,671036.1314961306,"POLYGON((670725.4942750228 4401922.975167256,670725.4942750228 4429672.973141896,671346.7687172384 4429672.973141896,671346.7687172384 4401922.975167256,670725.4942750228 4401922.975167256))",feat_0,indexgrid15minutequads_wvgistc_utm83,USA
services/geolgyl_reg_ll83_attrs.csv:400:378,36.91776870599808,-76.1738925486109,"POLYGON((-76.1756004396857 36.917571659248544,-76.1756004396857 36.91811615924905,-76.17216593968249 36.91811615924905,-76.17216593968249 36.917571659248544,-76.1756004396857 36.917571659248544))",feat_378,geolgyl_reg_ll83,USA
services/geolgyl_reg_ll83_attrs.csv:1250:1232,38.6785241466055,-76.20105748581663,"POLYGON((-76.20279243971102 38.67088716088145,-76.20279243971102 38.68679116089626,-76.19768793970627 38.68679116089626,-76.19768793970627 38.67088716088145,-76.20279243971102 38.67088716088145))",feat_1232,geolgyl_reg_ll83,USA
services/geolgyl_reg_ll83_attrs.csv:1266:1249,38.710580144071784,-76.09952856277687,"POLYGON((-76.10096693961619 38.704280660912545,-76.10096693961619 38.71696016092436,-76.09847243961386 38.71696016092436,-76.09847243961386 38.704280660912545,-76.10096693961619 38.704280660912545))",feat_1249,geolgyl_reg_ll83,USA
services/route_declarations_raw.txt:111:belief_integrator.py:56:@app.post("/integrate_neo4j_belief")
services/empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907_attrs.csv:154:153,4352115.178684399,456762.27687513834,"POLYGON((454108.65488438803 4348869.545284115,454108.65488438803 4354652.887675274,459155.1932021032 4354652.887675274,459155.1932021032 4348869.545284115,454108.65488438803 4348869.545284115))",,empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907,USA
services/empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907_attrs.csv:283:282,4251564.630062899,433670.876870761,"POLYGON((430168.44907939725 4248915.556213427,430168.44907939725 4254010.471560418,437005.68520973634 4254010.471560418,437005.68520973634 4248915.556213427,430168.44907939725 4248915.556213427))",,empowermentzonesandenterprisecommunitiesbytract_uscens_30c72907,USA
services/enrich_geodb_layers.py:7:from neo4j import GraphDatabase
services/enrich_geodb_layers.py:18:# Neo4j connection
services/enrich_geodb_layers.py:19:NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
services/enrich_geodb_layers.py:20:NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
services/enrich_geodb_layers.py:21:NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")
services/enrich_geodb_layers.py:27:# - id_column: primary id used to build Neo4j node id
services/enrich_geodb_layers.py:28:# - id_prefix: prefix to build Neo4j id (id_prefix + id value)
services/enrich_geodb_layers.py:32:# - attribute_columns: dict of {alias_in_neo4j: sql_column_name}
services/enrich_geodb_layers.py:361:def connect_neo4j():
services/enrich_geodb_layers.py:362:    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
services/enrich_geodb_layers.py:470:    driver = connect_neo4j()
services/hilbert_spatial_chat.py:11:from neo4j import GraphDatabase  # NEW
services/hilbert_spatial_chat.py:113:# === Neo4j integration (NEW) ===
services/hilbert_spatial_chat.py:115:NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
services/hilbert_spatial_chat.py:116:NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
services/hilbert_spatial_chat.py:117:NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")  # override via env
services/hilbert_spatial_chat.py:119:driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
services/hilbert_spatial_chat.py:153:# === graph/nearby_resources endpoint using Neo4j ===
services/hilbert_spatial_chat.py:157:    place_id: str = Query(..., description="Place node id in Neo4j"),
services/hilbert_spatial_chat.py:179:        logger.error(f"Neo4j query failed: {e}")
services/hilbert_spatial_chat.py:182:            "error": f"Neo4j query failed: {str(e)[:200]}",
services/hilbert_spatial_chat.py:203:# === graph/project_impact endpoint using Neo4j (NEW) ===
services/hilbert_spatial_chat.py:207:    project_id: str = Query(..., description="Project node id in Neo4j"),
services/hilbert_spatial_chat.py:232:        logger.error(f"Neo4j project_impact query failed: {e}")
services/hilbert_spatial_chat.py:235:            "error": f"Neo4j query failed: {str(e)[:200]}",
services/hilbert_spatial_chat.py:272:    neo4j_status = "unknown"
services/hilbert_spatial_chat.py:275:        neo4j_status = "connected"
services/hilbert_spatial_chat.py:277:        neo4j_status = f"disconnected: {str(e)[:50]}"
services/hilbert_spatial_chat.py:283:        "neo4j": neo4j_status,
services/manufacturingandbusiness_wvdo_200803_utm83_attrs.csv:684:546,4252636.2794076875,409550.06627345335,POINT(409550.06627345335 4252636.2794076875),Walter Hayslett,manufacturingandbusiness_wvdo_200803_utm83,USA
services/manufacturingandbusiness_wvdo_200803_utm83_attrs.csv:1236:1058,4266086.697687862,553299.7605859741,POINT(553299.7605859741 4266086.697687862),Arden E Cogar Logging Co,manufacturingandbusiness_wvdo_200803_utm83,USA
services/manufacturingandbusiness_wvdo_200803_utm83_attrs.csv:1719:1541,4254701.48468009,376871.71010144986,POINT(376871.71010144986 4254701.48468009),Allied Processing Services Inc,manufacturingandbusiness_wvdo_200803_utm83,USA
services/manufacturingandbusiness_wvdo_200803_utm83_attrs.csv:2682:2544,4247687.297451551,437571.9213996561,POINT(437571.9213996561 4247687.297451551),Yellow Transportation Inc,manufacturingandbusiness_wvdo_200803_utm83,USA
services/manufacturingandbusiness_wvdo_200803_utm83_attrs.csv:6108:6160,4382485.409776878,589702.0322383255,POINT(589702.0322383255 4382485.409776878),D & M Investments Inc,manufacturingandbusiness_wvdo_200803_utm83,USA
services/manufacturingandbusiness_wvdo_200803_utm83_attrs.csv:6642:6571,4345278.056366059,557868.3985976875,POINT(557868.3985976875 4345278.056366059),Harrison County Board of Educn,manufacturingandbusiness_wvdo_200803_utm83,USA
services/manufacturingandbusiness_wvdo_200803_utm83_attrs.csv:7558:7493,4252336.6167687,379114.86233630957,POINT(379114.86233630957 4252336.6167687),Prestera Center For Mental,manufacturingandbusiness_wvdo_200803_utm83,USA
services/manufacturingandbusiness_wvdo_200803_utm83_attrs.csv:7734:7687,4370533.955475906,571915.3049949205,POINT(571915.3049949205 4370533.955475906),Family Service Of Marion,manufacturingandbusiness_wvdo_200803_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:3425:4973,4316024.459818348,407687.76992880553,POINT(407687.76992880553 4316024.459818348),feat_4973,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:4809:4716,4316141.9768771585,549364.365878799,POINT(549364.365878799 4316141.9768771585),feat_4716,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:5027:6087,4315512.630355645,416293.91987687536,POINT(416293.91987687536 4315512.630355645),feat_6087,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:5480:6256,4315388.17045215,407687.01976430044,POINT(407687.01976430044 4315388.17045215),feat_6256,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:7087:7687,4313839.585571829,531634.3264951734,POINT(531634.3264951734 4313839.585571829),feat_7687,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:7474:3068,4317687.849428713,409214.1700158082,POINT(409214.1700158082 4317687.849428713),feat_3068,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:8514:8799,4313103.809768744,433645.69015153777,POINT(433645.69015153777 4313103.809768744),feat_8799,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:8575:8860,4313075.030604191,565812.9776876392,POINT(565812.9776876392 4313075.030604191),feat_8860,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:9327:9187,4312938.876872284,565973.3098235503,POINT(565973.3098235503 4312938.876872284),feat_9187,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:11250:11988,4311762.149976872,434742.21021268796,POINT(434742.21021268796 4311762.149976872),feat_11988,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:13595:14670,4310325.829768728,434600.1500084754,POINT(434600.1500084754 4310325.829768728),feat_14670,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:13769:13096,4311298.1700324975,434380.519976872,POINT(434380.519976872 4311298.1700324975),feat_13096,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:14105:14901,4310225.520076875,428767.21980784833,POINT(428767.21980784833 4310225.520076875),feat_14901,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:16672:17257,4309007.8457687255,537675.4902529949,POINT(537675.4902529949 4309007.8457687255),feat_17257,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:16858:18101,4308472.122276876,522687.8464815803,POINT(522687.8464815803 4308472.122276876),feat_18101,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:17615:18437,4308282.209840447,437687.4503415581,POINT(437687.4503415581 4308282.209840447),feat_18437,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:17661:17687,4308757.950054457,438400.8795697391,POINT(438400.8795697391 4308757.950054457),feat_17687,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:18330:18734,4308095.768745765,553740.8547690501,POINT(553740.8547690501 4308095.768745765),feat_18734,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:18775:19436,4307687.956671476,610980.752585642,POINT(610980.752585642 4307687.956671476),feat_19436,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:19016:19536,4307641.50547689,611365.5964768762,POINT(611365.5964768762 4307641.50547689),feat_19536,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:19385:20418,4307273.7042069305,527687.321797288,POINT(527687.321797288 4307273.7042069305),feat_20418,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:20332:14012,4310763.176878605,566171.9675315777,POINT(566171.9675315777 4310763.176878605),feat_14012,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:21420:21333,4306745.899577469,417687.9303562213,POINT(417687.9303562213 4306745.899577469),feat_21333,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:21861:14173,4310606.998576878,515077.7467730157,POINT(515077.7467730157 4310606.998576878),feat_14173,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:23042:22513,4305886.576873235,506618.7677672021,POINT(506618.7677672021 4305886.576873235),feat_22513,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:24374:25547,4304325.084106844,601111.2102427687,POINT(601111.2102427687 4304325.084106844),feat_25547,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:25108:25862,4304227.9544003885,561047.9255776871,POINT(561047.9255776871 4304227.9544003885),feat_25862,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:25231:26653,4303990.707818303,620403.032876879,POINT(620403.032876879 4303990.707818303),feat_26653,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:26333:27589,4303718.29076878,405275.0599723775,POINT(405275.0599723775 4303718.29076878),feat_27589,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:26574:27686,4303688.23982119,558644.3768700827,POINT(558644.3768700827 4303688.23982119),feat_27686,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:26575:27687,4303693.969778454,402479.12956376653,POINT(402479.12956376653 4303693.969778454),feat_27687,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:27303:28793,4303410.900396323,402150.5304737687,POINT(402150.5304737687 4303410.900396323),feat_28793,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:27498:28850,4303392.979768738,428306.16967160907,POINT(428306.16967160907 4303392.979768738),feat_28850,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:27848:28252,4303551.300237568,401929.14942768775,POINT(401929.14942768775 4303551.300237568),feat_28252,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:29886:30367,4302859.768717783,597223.3842014987,POINT(597223.3842014987 4302859.768717783),feat_30367,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:30086:31236,4302613.340199303,402012.17003768776,POINT(402012.17003768776 4302613.340199303),feat_31236,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:31940:32486,4302269.94715463,524460.2644976871,POINT(524460.2644976871 4302269.94715463),feat_32486,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:32231:32636,4302233.098273981,495073.4591037687,POINT(495073.4591037687 4302233.098273981),feat_32636,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:33422:33933,4301884.820060164,549633.4620357687,POINT(549633.4620357687 4301884.820060164),feat_33933,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:36466:37687,4300539.432771416,562336.5523015745,POINT(562336.5523015745 4300539.432771416),feat_37687,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:37209:38002,4300441.95012445,597898.1768709552,POINT(597898.1768709552 4300441.95012445),feat_38002,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:37671:38182,4300377.461381134,526828.1876874799,POINT(526828.1876874799 4300377.461381134),feat_38182,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:37845:38741,4300214.439147687,599956.2977207704,POINT(599956.2977207704 4300214.439147687),feat_38741,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:39360:39413,4299954.409587687,401640.6407636963,POINT(401640.6407636963 4299954.409587687),feat_39413,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:39549:40272,4299690.7447687145,597568.3273816742,POINT(597568.3273816742 4299690.7447687145),feat_40272,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:41981:41821,4299274.310174694,432137.799576872,POINT(432137.799576872 4299274.310174694),feat_41821,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:43446:43643,4298609.60957687,424753.0602207044,POINT(424753.0602207044 4298609.60957687),feat_43643,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:44049:44635,4298203.055235691,597687.2157317577,POINT(597687.2157317577 4298203.055235691),feat_44635,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:44127:44713,4298168.276875159,490615.3318902487,POINT(490615.3318902487 4298168.276875159),feat_44713,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:44572:44872,4298108.181710437,482778.6676870873,POINT(482778.6676870873 4298108.181710437),feat_44872,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:46236:46084,4297687.176943731,498086.43271496706,POINT(498086.43271496706 4297687.176943731),feat_46084,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:46247:46095,4297687.449547725,433127.75039271545,POINT(433127.75039271545 4297687.449547725),feat_46095,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:46249:46097,4297687.348202623,571708.2752712928,POINT(571708.2752712928 4297687.348202623),feat_46097,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:47043:46473,4297562.189941781,438645.79976871144,POINT(438645.79976871144 4297562.189941781),feat_46473,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:48155:47687,4297196.889766753,437784.6600971846,POINT(437784.6600971846 4297196.889766753),feat_47687,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:49149:50521,4296550.183899082,595957.8797687367,POINT(595957.8797687367 4296550.183899082),feat_50521,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:52821:48631,4296985.176879527,492123.271145802,POINT(492123.271145802 4296985.176879527),feat_48631,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:52975:53429,4295621.019907687,445153.8597716531,POINT(445153.8597716531 4295621.019907687),feat_53429,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:53048:53502,4295596.7598386165,417687.83050021436,POINT(417687.83050021436 4295596.7598386165),feat_53502,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:54181:54460,4295194.412168082,394277.2967687771,POINT(394277.2967687771 4295194.412168082),feat_54460,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:54653:54652,4295123.540276878,428486.68046889454,POINT(428486.68046889454 4295123.540276878),feat_54652,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:55050:55575,4294768.768797476,394133.5706632752,POINT(394133.5706632752 4294768.768797476),feat_55575,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:55539:55785,4294666.209867001,520510.76871429663,POINT(520510.76871429663 4294666.209867001),feat_55785,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:55650:55083,4294957.220124517,435838.71993197687,POINT(435838.71993197687 4294957.220124517),feat_55083,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:56673:56746,4294213.002224717,466888.73076870013,POINT(466888.73076870013 4294213.002224717),feat_56746,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:56988:56917,4294145.976872452,595196.8110559443,POINT(595196.8110559443 4294145.976872452),feat_56917,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:57088:57687,4293832.931288393,579554.4836294334,POINT(579554.4836294334 4293832.931288393),feat_57687,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:57656:58734,4293383.865889115,488376.1777687883,POINT(488376.1777687883 4293383.865889115),feat_58734,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:58682:58848,4293341.977685692,488943.35940768756,POINT(488943.35940768756 4293341.977685692),feat_58848,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:59206:60272,4292791.780290518,427690.0296768723,POINT(427690.0296768723 4292791.780290518),feat_60272,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:60077:60722,4292631.060067687,651325.7277555885,POINT(651325.7277555885 4292631.060067687),feat_60722,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:61218:59104,4293251.491768714,596290.7149214931,POINT(596290.7149214931 4293251.491768714),feat_59104,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:61714:62599,4291919.507324018,593349.3776876479,POINT(593349.3776876479 4291919.507324018),feat_62599,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:62593:63826,4291526.29997687,438050.11037431937,POINT(438050.11037431937 4291526.29997687),feat_63826,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:63145:63195,4291741.691947687,592930.8195694648,POINT(592930.8195694648 4291741.691947687),feat_63195,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:63551:64216,4291377.523768781,508817.90648767445,POINT(508817.90648767445 4291377.523768781),feat_64216,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:64039:64421,4291287.416296875,487687.5311896857,POINT(487687.5311896857 4291287.416296875),feat_64421,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:64127:64509,4291262.0268435795,584447.4937467687,POINT(584447.4937467687 4291262.0268435795),feat_64509,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:66526:66727,4290310.557687944,633268.647341881,POINT(633268.647341881 4290310.557687944),feat_66727,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:67078:59720,4293007.768752035,596272.617019821,POINT(596272.617019821 4293007.768752035),feat_59720,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:67216:66992,4290159.773768766,518941.9089864334,POINT(518941.9089864334 4290159.773768766),feat_66992,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:67437:67606,4289874.546812136,503841.67987687886,POINT(503841.67987687886 4289874.546812136),feat_67606,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:67660:67687,4289841.780136421,562441.3246365134,POINT(562441.3246365134 4289841.780136421),feat_67687,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:68538:68811,4289429.590776879,651533.8446225859,POINT(651533.8446225859 4289429.590776879),feat_68811,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:69010:69003,4289332.4304816425,507687.55542464554,POINT(507687.55542464554 4289332.4304816425),feat_69003,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:69402:70842,4288582.585987687,535947.6154626412,POINT(535947.6154626412 4288582.585987687),feat_70842,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:69974:71132,4288462.536542766,519380.27576871775,POINT(519380.27576871775 4288462.536542766),feat_71132,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:70232:71246,4288423.276705548,466971.2275476875,POINT(466971.2275476875 4288423.276705548),feat_71246,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:70858:72261,4288017.77037687,415128.2093040189,POINT(415128.2093040189 4288017.77037687),feat_72261,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:71323:69803,4289003.726548204,519401.6047687642,POINT(519401.6047687642 4289003.726548204),feat_69803,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:71621:72661,4287881.926385839,653588.3187577687,POINT(653588.3187577687 4287881.926385839),feat_72661,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:72617:73173,4287687.495745789,490839.9906452885,POINT(490839.9906452885 4287687.495745789),feat_73173,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:72622:73178,4287687.75460471,464285.16174981557,POINT(464285.16174981557 4287687.75460471),feat_73178,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:72628:73184,4287687.069396943,532331.2731862357,POINT(532331.2731862357 4287687.069396943),feat_73184,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:72642:73198,4287687.139728071,423456.56969226804,POINT(423456.56969226804 4287687.139728071),feat_73198,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:72646:73202,4287687.689225975,588787.6784006143,POINT(588787.6784006143 4287687.689225975),feat_73202,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:72648:73204,4287687.10609467,587983.9712140039,POINT(587983.9712140039 4287687.10609467),feat_73204,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:72654:73210,4287687.449712049,404922.27953872085,POINT(404922.27953872085 4287687.449712049),feat_73210,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:73376:70146,4288873.6406768765,524097.84325073846,POINT(524097.84325073846 4288873.6406768765),feat_70146,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:74684:75349,4286980.1505966745,591971.5257687075,POINT(591971.5257687075 4286980.1505966745),feat_75349,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:75614:76870,4286329.154507846,473701.0215885518,POINT(473701.0215885518 4286329.154507846),feat_76870,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:75615:76871,4286345.367723264,651257.4516810793,POINT(651257.4516810793 4286345.367723264),feat_76871,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:75616:76872,4286328.348960374,518265.3174015973,POINT(518265.3174015973 4286328.348960374),feat_76872,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:75617:76873,4286328.7828109395,530340.9309412176,POINT(530340.9309412176 4286328.7828109395),feat_76873,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:75618:76874,4286330.149735127,441012.8601205284,POINT(441012.8601205284 4286330.149735127),feat_76874,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:75619:76875,4286327.748138322,518199.6024009194,POINT(518199.6024009194 4286327.748138322),feat_76875,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:75620:76876,4286328.101629168,467088.85167452134,POINT(467088.85167452134 4286328.101629168),feat_76876,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:75621:76877,4286327.422097173,518188.0708321985,POINT(518188.0708321985 4286327.422097173),feat_76877,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:75622:76878,4286331.199879827,425926.60994956736,POINT(425926.60994956736 4286331.199879827),feat_76878,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:75623:76879,4286327.566873388,473721.19688539393,POINT(473721.19688539393 4286327.566873388),feat_76879,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:75983:75939,4286717.010721836,397725.0297768768,POINT(397725.0297768768 4286717.010721836),feat_75939,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:76174:77148,4286215.603928216,468012.6768733151,POINT(468012.6768733151 4286215.603928216),feat_77148,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:76402:77237,4286181.503076872,529334.2461051885,POINT(529334.2461051885 4286181.503076872),feat_77237,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:77005:76383,4286537.103030086,476874.85003428813,POINT(476874.85003428813 4286537.103030086),feat_76383,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:77427:77687,4286007.846992461,530176.5354912523,POINT(530176.5354912523 4286007.846992461),feat_77687,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:78355:79262,4285335.210372943,417687.9595169984,POINT(417687.9595169984 4285335.210372943),feat_79262,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:78642:79371,4285280.316638811,407687.21056208387,POINT(407687.21056208387 4285280.316638811),feat_79371,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:80404:81597,4284118.499364195,397687.530812799,POINT(397687.530812799 4284118.499364195),feat_81597,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:80602:80588,4284660.337057142,527214.3549577687,POINT(527214.3549577687 4284660.337057142),feat_80588,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:81130:82831,4283509.682756128,509436.137687332,POINT(509436.137687332 4283509.682756128),feat_82831,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:81278:81933,4283971.294076879,589632.5575646469,POINT(589632.5575646469 4283971.294076879),feat_81933,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:81892:82238,4283816.953943461,539768.8687687544,POINT(539768.8687687544 4283816.953943461),feat_82238,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:82000:83164,4283335.19966693,397687.96036542766,POINT(397687.96036542766 4283335.19966693),feat_83164,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:82142:82348,4283749.139768777,463768.3903296264,POINT(463768.3903296264 4283749.139768777),feat_82348,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:83247:84086,4282910.998664796,590241.9854676872,POINT(590241.9854676872 4282910.998664796),feat_84086,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:83256:84095,4282903.221311364,555696.4593676878,POINT(555696.4593676878 4282903.221311364),feat_84095,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:84514:84646,4282658.660010723,633375.1224768749,POINT(633375.1224768749 4282658.660010723),feat_84646,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:85396:85879,4282096.80076232,403773.34937687963,POINT(403773.34937687963 4282096.80076232),feat_85879,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:86306:86242,4281955.74971028,554295.976875429,POINT(554295.976875429 4281955.74971028),feat_86242,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:86832:87687,4281418.896700652,506405.31281919125,POINT(506405.31281919125 4281418.896700652),feat_87687,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:87843:88130,4281264.6015953235,535650.2673776876,POINT(535650.2673776876 4281264.6015953235),feat_88130,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:88325:88324,4281199.638386665,493144.57687001117,POINT(493144.57687001117 4281199.638386665),feat_88324,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:88329:88328,4281199.22661447,476160.0587687185,POINT(476160.0587687185 4281199.22661447),feat_88328,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:88589:88445,4281151.129675087,536090.6596676875,POINT(536090.6596676875 4281151.129675087),feat_88445,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:89143:88714,4281061.289776875,398052.28030412644,POINT(398052.28030412644 4281061.289776875),feat_88714,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:89826:91204,4280157.287887687,519030.10702578444,POINT(519030.10702578444 4280157.287887687),feat_91204,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:89858:90202,4280523.601482766,663726.1829007687,POINT(663726.1829007687 4280523.601482766),feat_90202,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:90331:91253,4280141.97768762,483825.17258561123,POINT(483825.17258561123 4280141.97768762),feat_91253,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:90985:90742,4280297.499987222,427687.80007654615,POINT(427687.80007654615 4280297.499987222),feat_90742,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:91704:91034,4280213.87025528,418455.19987687934,POINT(418455.19987687934 4280213.87025528),feat_91034,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:94322:95125,4278885.757687813,475742.7595445905,POINT(475742.7595445905 4278885.757687813),feat_95125,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:94499:95166,4278878.820276873,399093.70036351215,POINT(399093.70036351215 4278878.820276873),feat_95166,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:94960:91778,4279990.455675457,587687.637310721,POINT(587687.637310721 4279990.455675457),feat_91778,structurepointssouth_samb_2003_utm83,USA
services/structurepointssouth_samb_2003_utm83_attrs.csv:95649:96328,4278457.014289167,654607.7687101588,POINT(654607.7687101588 4278457.014289167),feat_96328,structurepointssouth_samb_2003_utm83,USA

===== 6. Check Hilbert health one more time =====
{
    "status": "healthy",
    "service": "hilbert_spatial_chat",
    "chromadb": "connected",
    "neo4j": "disconnected: Couldn't connect to localhost:7687 (resolved to ('",
    "collections_indexed": [
        "appalachian_english_corpus",
        "geospatialfeatures"
    ],
    "consensus": "connected:4001",
    "port": 5002,
    "quantum_entanglement": "active"
}
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ 

