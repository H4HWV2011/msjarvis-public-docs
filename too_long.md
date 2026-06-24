(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ # Confirm the 3-layer DGM cascade (port 9999 → 4002 → 7239)
cat /mnt/nvme1/msjarvis-rebuild/services/dgm_orchestrator.py

# Is it actually running?
docker ps --format "table {{.Names}}\t{{.Ports}}\t{{.Status}}" | grep -E "dgm|pituitary|judge|torod|egeria|swarm"

# What ports are bound on host right now?
ss -tlnp | grep -E "999|7239|4002|8021|8010|5200|5215" | sort
#!/usr/bin/env python3
"""
69-DGM Orchestrator (Port 9999)

Receives messages from the port_9000_69dgm_bridge and coordinates validation
across the DGM / WOAH / judge layers. For now, this returns a sane, deterministic
decision and can be extended to call individual bridge_cross_dgm_100xx services.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from pathlib import Path
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("69_DGM_Orchestrator")

app = FastAPI(
    title="69-DGM Orchestrator",
    version="1.0.0",
    description="Central DGM orchestrator for Ms. Jarvis",
)

# Load active connectors (same file used by port_9000_69dgm_bridge)
REGISTRY_PATH = Path(__file__).with_name("dgm_connectors_active.json")
if REGISTRY_PATH.exists():
    try:
        CONNECTORS = json.loads(REGISTRY_PATH.read_text())
        logger.info(
            f"🧩 Orchestrator loaded {len(CONNECTORS)} active connectors from {REGISTRY_PATH}"
        )
    except Exception as e:
        logger.error(f"Failed to load {REGISTRY_PATH}: {e}")
        CONNECTORS: List[dict] = []
else:
    logger.warning(f"No active connector registry found at {REGISTRY_PATH}")
    CONNECTORS: List[dict] = []


class OrchestratorRequest(BaseModel):
    message: str
    userid: str
    source: str


class OrchestratorResponse(BaseModel):
    status: str
    dgm_importance: float
    woah_alignment: float
    connectors_considered: int
    reason: Optional[str] = None


# Simple, local DGM/WOAH heuristics based on your originals
IMPORTANT_KEYWORDS = [
    "community", "mount hope", "appalachian", "growth", "purpose",
    "serve", "wv", "west virginia", "fayette", "consciousness",
    "learning", "identity", "blockchain", "smart contract",
]

COMMUNITY_FACTORS = {
    "growth": 0.3,
    "community": 0.3,
    "education": 0.2,
    "opportunity": 0.2,
    "connection": 0.2,
}


def calculate_dgm_importance(query_text: str, accuracy: float = 0.7) -> float:
    score = 0.0
    q = query_text.lower()
    for kw in IMPORTANT_KEYWORDS:
        if kw in q:
            score += 0.15
    score += accuracy * 0.3
    score = min(score, 1.0)
    return score


def calculate_woah_alignment(query_text: str) -> float:
    score = 0.5
    q = query_text.lower()
    for factor, weight in COMMUNITY_FACTORS.items():
        if factor in q:
            score += weight
    return min(score, 1.0)


@app.post("/process", response_model=OrchestratorResponse)
async def process(req: OrchestratorRequest):
    """
    Main orchestrator endpoint called by port_9000_69dgm_bridge.
    For now:
    - Compute DGM importance and WOAH alignment locally.
    - If both exceed thresholds, approve; else require more validation.
    """
    dgm_score = calculate_dgm_importance(req.message, accuracy=0.7)
    woah_score = calculate_woah_alignment(req.message)

    logger.info(
        f"🧮 Orchestrator scores for user={req.userid}: "
        f"DGM={dgm_score:.2f}, WOAH={woah_score:.2f} "
        f"(connectors={len(CONNECTORS)})"
    )

    if dgm_score >= 0.2 and woah_score >= 0.4:
        status = "approved_by_69_validators"
        reason = "Query is important and aligned with community values."
    else:
        status = "needs_additional_judging"
        reason = "Query did not meet importance/alignment thresholds."

    return OrchestratorResponse(
        status=status,
        dgm_importance=dgm_score,
        woah_alignment=woah_score,
        connectors_considered=len(CONNECTORS),
        reason=reason,
    )


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "69_dgm_orchestrator",
        "connectors_loaded": len(CONNECTORS),
    }


if __name__ == "__main__":
    import uvicorn
    logger.info("🚦 Starting 69-DGM Orchestrator on port 9999")
    uvicorn.run(app, host="127.0.0.1", port=9999)
jarvis-dgm-bridge-07                 127.0.0.1:10007->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-22                 127.0.0.1:10022->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-01                 127.0.0.1:10001->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-14                 127.0.0.1:10014->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-19                 127.0.0.1:10019->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-10                 127.0.0.1:10010->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-06                 127.0.0.1:10006->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-09                 127.0.0.1:10009->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-12                 127.0.0.1:10012->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-15                 127.0.0.1:10015->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-08                 127.0.0.1:10008->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-21                 127.0.0.1:10021->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-23                 127.0.0.1:10023->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-05                 127.0.0.1:10005->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-17                 127.0.0.1:10017->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-18                 127.0.0.1:10018->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-11                 127.0.0.1:10011->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-20                 127.0.0.1:10020->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-03                 127.0.0.1:10003->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-02                 127.0.0.1:10002->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-13                 127.0.0.1:10013->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-04                 127.0.0.1:10004->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-16                 127.0.0.1:10016->10001/tcp                                                                                     Up 3 hours
jarvis-69dgm-bridge                  127.0.0.1:9000->9000/tcp                                                                                       Up 3 hours
jarvis-judge-pipeline                7239/tcp                                                                                                       Up 5 hours
jarvis-fifth-dgm                     127.0.0.1:4002->4002/tcp                                                                                       Up 5 hours
jarvis-swarm-intelligence            8021/tcp                                                                                                       Up 5 hours
jarvis-judge-ethics                  7233/tcp                                                                                                       Up 5 hours
jarvis-judge-alignment               7232/tcp                                                                                                       Up 5 hours
nbb_pituitary_gland                  127.0.0.1:8108->8010/tcp                                                                                       Up 5 hours
jarvis-judge-truth                   7230/tcp                                                                                                       Up 5 hours
jarvis-judge-consistency             7231/tcp                                                                                                       Up 5 hours
LISTEN 0      2048         0.0.0.0:9999       0.0.0.0:*    users:(("uvicorn",pid=2239,fd=13))        
LISTEN 0      4096       127.0.0.1:4002       0.0.0.0:*                                              
LISTEN 0      4096       127.0.0.1:8010       0.0.0.0:*                                              
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ # Confirm Docker service name and health
docker inspect jarvis-torodial 2>/dev/null | python3 -c "
import json,sys
d=json.load(sys.stdin)[0]
s=d['State']
n=d['NetworkSettings']['Networks']
print('Status:', s['Status'])
print('Health:', s.get('Health',{}).get('Status','no healthcheck'))
print('Networks:', list(n.keys()))
print('IP:', [v['IPAddress'] for v in n.values()])
"

# What does it actually serve?
curl -s http://localhost:$(docker port jarvis-torodial 2>/dev/null | awk -F: '{print $2}' | head -1)/health 2>/dev/null || \
  curl -s http://localhost:8010/health 2>/dev/null || \
  echo "No health endpoint responding"

# Is it in the unified gateway routing table?
grep -n "torod\|toroidal" \
  /mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_unified_swagger_gateway.py \
  /mnt/nvme1/msjarvis-rebuild/docker-compose.yml 2>/dev/null
Traceback (most recent call last):
  File "<string>", line 3, in <module>
IndexError: list index out of range
/mnt/nvme1/msjarvis-rebuild/docker-compose.yml:16:    - TOROIDAL_URL=http://jarvis-toroidal:8025
/mnt/nvme1/msjarvis-rebuild/docker-compose.yml:54:    - jarvis-toroidal
/mnt/nvme1/msjarvis-rebuild/docker-compose.yml:1244:  jarvis-toroidal:
/mnt/nvme1/msjarvis-rebuild/docker-compose.yml:1247:      dockerfile: Dockerfile.toroidal
/mnt/nvme1/msjarvis-rebuild/docker-compose.yml:1248:    image: msjarvis-toroidal:latest
/mnt/nvme1/msjarvis-rebuild/docker-compose.yml:1249:    container_name: jarvis-toroidal
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ # How many judge stubs are actually differentiated vs identical?
md5sum /mnt/nvme1/msjarvis-rebuild/services/judge_10*.py 2>/dev/null | \
  awk '{print $1}' | sort | uniq -c | sort -rn | head -5

# What does the bridge actually call?
grep -n "port\|url\|host\|judge_id\|localhost\|http" \
  /mnt/nvme1/msjarvis-rebuild/services/judge_to_pituitary_bridge.py | head -30

# Is the judge pipeline endpoint (7239) live?
curl -s -X POST http://localhost:7239/judge \
  -H "Content-Type: application/json" \
  -d '{"query":"test","response":"Mount Hope community test"}' 2>/dev/null \
  | python3 -m json.tool 2>/dev/null || echo "Port 7239 not responding"
     66 71a7509aa6f47d2e10a3308aa07a1103
3:from fastapi import FastAPI
4:import uvicorn
5:import logging
13:    return {"status": "bridge_alive", "name": "judge_to_pituitary", "port": 5215}
21:        "port": 5215,
25:import argparse
26:import os
29:parser.add_argument("--port", type=int, default=5215)
31:PORT = args.port
42:        "port": PORT,
46:import argparse
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")
51:    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="error")
Port 7239 not responding
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ # Does the sandbox directory actually exist?
ls -la /home/ms-jarvis/msjarvis-rebuild/egeria_sandbox/ 2>/dev/null || \
  ls -la /mnt/nvme1/msjarvis-rebuild/egeria_sandbox/ 2>/dev/null || \
  echo "Sandbox path does not exist"

# Has it ever successfully committed a correction?
sqlite3 /mnt/nvme1/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite \
  "SELECT COUNT(*), MAX(timestamp) FROM ms_jarvis_learning_log WHERE learning_action LIKE '%correct%' OR learning_action LIKE '%self_improv%';" 2>/dev/null

# Full Egeria class — see if commit logic is complete
cat /mnt/nvme1/msjarvis-rebuild/services/egeria_safe_self_correction.py
Sandbox path does not exist
#!/usr/bin/env python3
from fastapi import Depends, HTTPException, Header
from typing import Optional
import logging
logger = logging.getLogger(__name__)
"""
Ms. Egeria Safe Self-Correction System
Allows her to improve her code safely within boundaries
"""

import os
import json
import hashlib
from datetime import datetime

class SafeSelfCorrection:
    def __init__(self):
        self.sandbox = "/home/ms-jarvis/msjarvis-rebuild/egeria_sandbox"
        self.learning = "/home/ms-jarvis/msjarvis-rebuild/egeria_learning_data"
        self.protected = [
            "/home/ms-jarvis/msjarvis-rebuild/neurobiological_brain",
            "/home/ms-jarvis/msjarvis-rebuild/services",
            "/home/ms-jarvis/msjarvis-rebuild/egeria_metadata.json"
        ]
        self.db = "/home/ms-jarvis/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite"
    
    def is_path_protected(self, path):
        """Is this path protected from modification?"""
        for protected in self.protected:
            if path.startswith(protected):
                return True
        return False
    
    def propose_correction(self, file_path, corrected_code):
        """She proposes a code correction"""
        if self.is_path_protected(file_path):
            return {
                "status": "blocked",
                "reason": "Core system file - protected from modification",
                "file": file_path
            }
        
        # Save to sandbox first
        filename = os.path.basename(file_path)
        sandbox_path = os.path.join(self.sandbox, f"correction_{filename}")
        
        try:
            with open(sandbox_path, "w") as f:
                f.write(corrected_code)
            
            return {
                "status": "proposed",
                "original": file_path,
                "proposed_location": sandbox_path,
                "message": "Correction saved to sandbox for testing"
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def test_correction(self, code):
        """Test corrected code safely"""
        try:
            # Execute in restricted context
            safe_globals = {'__builtins__': {}}
            exec(code, safe_globals)
            return {"status": "safe", "passed": True}
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def log_self_improvement(self, original_file, correction):
        """Log that she improved her code"""
        import sqlite3
        
        try:
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO ms_jarvis_learning_log 
                (ueid, learning_action, data_processed)
                VALUES (?, ?, ?)
            """, (
                "egeria_self",
                "self_correction_proposed",
                json.dumps({
                    "original": original_file,
                    "timestamp": datetime.now().isoformat(),
                    "type": "code_improvement"
                })
            ))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error logging: {e}")
            return False

if __name__ == '__main__':
    correction = SafeSelfCorrection()
    
    # Example: She wants to improve a learning script
    corrected = """
def improved_analysis():
    return "better version"
"""
    
    result = correction.propose_correction(
        "/home/ms-jarvis/msjarvis-rebuild/egeria_learning_data/analysis.py",
        corrected
    )
    print(json.dumps(result, indent=2))
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ # WOAH function — does calculate_woah_alignment() exist anywhere?
grep -rn "def calculate_woah_alignment\|woah_score\|woah_evaluation" \
  /mnt/nvme1/msjarvis-rebuild/services/ --include="*.py" | head -15

# I-Container SQLite state right now
sqlite3 /mnt/nvme1/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite "
SELECT
  (SELECT COUNT(*) FROM central_i_container) as central_count,
  (SELECT COUNT(*) FROM subconscious_i_container) as subconscious_count,
  (SELECT AVG(integration_confidence) FROM central_i_container) as avg_confidence,
  (SELECT MAX(created_at) FROM central_i_container) as last_integrated;
" 2>/dev/null

# What's in the I-Container docker service?
curl -s http://localhost:8015/health 2>/dev/null || \
  curl -s http://localhost:7005/health 2>/dev/null || echo "I-Container not responding"
/mnt/nvme1/msjarvis-rebuild/services/bridge_autonomous_to_i_container_fixed.py:42:            woah_score = calculate_woah_alignment(query_text)
/mnt/nvme1/msjarvis-rebuild/services/bridge_autonomous_to_i_container_fixed.py:43:            print(f"   WOAH alignment: {woah_score:.2f}/1.0")
/mnt/nvme1/msjarvis-rebuild/services/bridge_autonomous_to_i_container_fixed.py:45:            combined = (dgm_score + woah_score) / 2
/mnt/nvme1/msjarvis-rebuild/services/bridge_autonomous_to_i_container_fixed.py:51:            (data_content, data_source, importance_score, dgm_reasoning, woah_evaluation_score)
/mnt/nvme1/msjarvis-rebuild/services/bridge_autonomous_to_i_container_fixed.py:58:                woah_score
/mnt/nvme1/msjarvis-rebuild/services/bridge_autonomous_to_i_container_fixed.py:71:                    f"Autonomous + DGM: {dgm_score:.2f} + WOAH: {woah_score:.2f}",
/mnt/nvme1/msjarvis-rebuild/services/bridge_autonomous_to_i_container_fixed.py:122:def calculate_woah_alignment(query_text):
/mnt/nvme1/msjarvis-rebuild/services/create_dual_consciousness_i_containers.psychology_patched.py:56:        woah_evaluation_score FLOAT,
/mnt/nvme1/msjarvis-rebuild/services/create_dual_consciousness_i_containers.psychology_patched.py:136:        woah_evaluation_score,
/mnt/nvme1/msjarvis-rebuild/services/create_dual_consciousness_i_containers.psychology_patched.py:189:    (data_content, data_source, importance_score, dgm_reasoning, woah_evaluation_score)
/mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_fifth_dgm_orchestrator.py:120:        self.woah_evaluation_cycles = 0
/mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_fifth_dgm_orchestrator.py:121:        self.last_woah_evaluation = None
/mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_fifth_dgm_orchestrator.py:209:        self.woah_evaluation_cycles += 1
/mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_fifth_dgm_orchestrator.py:210:        self.last_woah_evaluation = datetime.now().isoformat()
/mnt/nvme1/msjarvis-rebuild/services/ms_jarvis_fifth_dgm_orchestrator.py:346:            "woah_evaluations": self.woah_evaluation_cycles,
{"status":"healthy","i_container_1":"active","i_container_2":"active","integration_layer":"active","dual_awareness":(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ # Full route table — what's registered vs what's deadroute table — what's registered vs what's dead
curl -s http://localhost:8008/routes 2>/dev/null | python3 -m json.tool 2>/dev/null || \
  curl -s http://localhost:9000/routes 2>/dev/null | python3 -m json.tool 2>/dev/null

# Which NBB containers are actually up with correct ports?
docker ps --format "table {{.Names}}\t{{.Ports}}\t{{.Status}}" | \
  grep -E "nbb|jarvis" | sort

# service_registry_client — what does get_service_url() actually resolve?
python3 -c "
import sys
sys.path.insert(0, '/mnt/nvme1/msjarvis-rebuild/services')
try:
    from service_registry_client import get_service_url
    for svc in ['pituitary_gland','judge_pipeline','toroidal','egeria','swarm']:
        print(f'{svc}: {get_service_url(svc)}')
except Exception as e:
    print(f'Registry error: {e}')
" 2>/dev/null
{
    "detail": "Not Found"
}
jarvis-20llm-production              127.0.0.1:8008->8008/tcp                                                                                       Up 5 hours
jarvis-69dgm-bridge                  127.0.0.1:9000->9000/tcp                                                                                       Up 3 hours
jarvis-aaacpe-rag                    127.0.0.1:8032->8032/tcp                                                                                       Up 5 hours
jarvis-aaacpe-scraper                127.0.0.1:8033->8033/tcp                                                                                       Up About an hour
jarvis-agents-service                8005/tcp                                                                                                       Up 5 hours
jarvis-auth-api                      127.0.0.1:8096->8091/tcp                                                                                       Up 5 hours
jarvis-autonomous-learner            127.0.0.1:8425->8425/tcp                                                                                       Up 5 hours
jarvis-blood-brain-barrier           0.0.0.0:8016->8016/tcp, [::]:8016->8016/tcp                                                                    Up 5 hours
jarvis-brain-orchestrator            127.0.0.1:17260->7260/tcp                                                                                      Up 5 hours (healthy)
jarvis-chroma                        127.0.0.1:8002->8000/tcp                                                                                       Up 3 hours (healthy)
jarvis-commons-gamification          127.0.0.1:8081->8081/tcp                                                                                       Up 2 hours
jarvis-community-stake-registry      127.0.0.1:8084->8084/tcp                                                                                       Up 2 hours
jarvis-consciousness-bridge          8002/tcp, 127.0.0.1:8020->8018/tcp                                                                             Up 5 hours
jarvis-constitutional-guardian       127.0.0.1:8091->8091/tcp                                                                                       Up 5 hours
jarvis-contracts                                                                                                                                    Up 5 hours
jarvis-crypto-policy                 127.0.0.1:8099->8099/tcp                                                                                       Up 2 hours
jarvis-dao-governance                127.0.0.1:8082->8082/tcp                                                                                       Up 2 hours
jarvis-dgm-bridge-01                 127.0.0.1:10001->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-02                 127.0.0.1:10002->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-03                 127.0.0.1:10003->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-04                 127.0.0.1:10004->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-05                 127.0.0.1:10005->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-06                 127.0.0.1:10006->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-07                 127.0.0.1:10007->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-08                 127.0.0.1:10008->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-09                 127.0.0.1:10009->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-10                 127.0.0.1:10010->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-11                 127.0.0.1:10011->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-12                 127.0.0.1:10012->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-13                 127.0.0.1:10013->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-14                 127.0.0.1:10014->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-15                 127.0.0.1:10015->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-16                 127.0.0.1:10016->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-17                 127.0.0.1:10017->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-18                 127.0.0.1:10018->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-19                 127.0.0.1:10019->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-20                 127.0.0.1:10020->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-21                 127.0.0.1:10021->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-22                 127.0.0.1:10022->10001/tcp                                                                                     Up 3 hours
jarvis-dgm-bridge-23                 127.0.0.1:10023->10001/tcp                                                                                     Up 3 hours
jarvis-eeg-beta                      127.0.0.1:8075->8075/tcp                                                                                       Up 5 hours
jarvis-eeg-delta                     127.0.0.1:8073->8073/tcp                                                                                       Up 5 hours
jarvis-eeg-theta                     127.0.0.1:8074->8074/tcp                                                                                       Up 5 hours
jarvis-fifth-dgm                     127.0.0.1:4002->4002/tcp                                                                                       Up 5 hours
jarvis-fractal-consciousness         8002/tcp, 8027/tcp                                                                                             Up 5 hours
jarvis-gbim-benefit-indexer          127.0.0.1:7206->7206/tcp                                                                                       Up 2 hours
jarvis-gbim-query-router             127.0.0.1:7205->7205/tcp                                                                                       Up About an hour
jarvis-gis-rag                       127.0.0.1:8004->8004/tcp, 8044/tcp                                                                             Up 5 hours
jarvis-hilbert-gateway                                                                                                                              Up 2 hours
jarvis-hilbert-spatial-chat          127.0.0.1:8235->8235/tcp                                                                                       Up 5 hours
jarvis-hilbert-state                 127.0.0.1:18092->8081/tcp                                                                                      Up 5 hours
jarvis-hippocampus                   127.0.0.1:8011->8011/tcp                                                                                       Up 3 hours
jarvis-i-containers                  8015/tcp                                                                                                       Up 5 hours
jarvis-ingest-api                                                                                                                                   Up About an hour
jarvis-ingest-watcher                                                                                                                               Up 2 hours
jarvis-intake-service                127.0.0.1:8007->8007/tcp                                                                                       Up 2 hours
jarvis-jaeger                        4317-4318/tcp, 5775/udp, 5778/tcp, 9411/tcp, 14250/tcp, 14268/tcp, 6831-6832/udp, 127.0.0.1:16686->16686/tcp   Up 5 hours
jarvis-judge-alignment               7232/tcp                                                                                                       Up 5 hours
jarvis-judge-consistency             7231/tcp                                                                                                       Up 5 hours
jarvis-judge-ethics                  7233/tcp                                                                                                       Up 5 hours
jarvis-judge-pipeline                7239/tcp                                                                                                       Up 5 hours
jarvis-judge-truth                   7230/tcp                                                                                                       Up 5 hours
jarvis-kyc-vault                     127.0.0.1:8045->8045/tcp                                                                                       Up 2 hours
jarvis-lm-synthesizer                8001/tcp                                                                                                       Up 5 hours
jarvis-local-resources               127.0.0.1:8006->8006/tcp, 8035/tcp                                                                             Up 5 hours
jarvis-local-resources-db            127.0.0.1:5435->5432/tcp                                                                                       Up 5 hours
jarvis-main-brain                    127.0.0.1:8050->8050/tcp                                                                                       Up 2 hours
jarvis-memory                        127.0.0.1:8056->8056/tcp                                                                                       Up 2 hours
jarvis-mother-protocols              4000/tcp                                                                                                       Up 5 hours
jarvis-ms-analytics                  127.0.0.1:8083->8083/tcp                                                                                       Up About an hour
jarvis-ms-coordinator                127.0.0.1:7300->7300/tcp                                                                                       Up 2 hours
jarvis-ms-indexer                    127.0.0.1:8080->8080/tcp                                                                                       Up About an hour
jarvis-nbb-i-containers-2            127.0.0.1:8015->8015/tcp                                                                                       Up About an hour
jarvis-neurobiological-master        8018/tcp                                                                                                       Up 5 hours
jarvis-ollama                        127.0.0.1:11434->11434/tcp                                                                                     Up 5 hours
jarvis-phi-probe                     127.0.0.1:8026->8025/tcp                                                                                       Up 5 hours
jarvis-pia-sampler                   8076/tcp                                                                                                       Up 5 hours
jarvis-provenance                    127.0.0.1:8046->8046/tcp                                                                                       Up 5 hours
jarvis-psychology-services           127.0.0.1:8019->8019/tcp                                                                                       Up 5 hours
jarvis-qualia-engine                 8017/tcp                                                                                                       Up 5 hours
jarvis-rag-router                    8003/tcp, 127.0.0.1:5015->5001/tcp                                                                             Up 5 hours
jarvis-rag-server                    127.0.0.1:8003->8003/tcp                                                                                       Up 5 hours
jarvis-redis                         127.0.0.1:6380->6379/tcp                                                                                       Up 5 hours (healthy)
jarvis-semaphore                     127.0.0.1:8030->8030/tcp                                                                                       Up 5 hours
jarvis-session-sidecar               127.0.0.1:8060->8060/tcp, 8070/tcp                                                                             Up 5 hours
jarvis-spiritual-rag                 127.0.0.1:8005->8005/tcp                                                                                       Up 5 hours
jarvis-steward                       127.0.0.1:8014->8014/tcp                                                                                       Up 2 hours
jarvis-stewardship-scheduler         127.0.0.1:8079->8079/tcp                                                                                       Up 2 hours
jarvis-swarm-intelligence            8021/tcp                                                                                                       Up 5 hours
jarvis-temporal-consciousness        7007/tcp                                                                                                       Up 5 hours
jarvis-toroidal                      127.0.0.1:8025->8025/tcp                                                                                       Up 5 hours
jarvis-unified-gateway               127.0.0.1:8001->8001/tcp                                                                                       Up 5 hours (healthy)
jarvis-web-research                  8008/tcp                                                                                                       Up 5 hours
jarvis-woah                          127.0.0.1:7012->7012/tcp                                                                                       Up 5 hours
jarvis-wv-entangled-gateway          127.0.0.1:8010->8010/tcp                                                                                       Up 5 hours
nbb_blood_brain_barrier              127.0.0.1:8301->8010/tcp                                                                                       Up 5 hours
nbb_consciousness_containers         127.0.0.1:8102->8010/tcp                                                                                       Up 5 hours
nbb_darwin_godel_machines            127.0.0.1:8302->8010/tcp                                                                                       Up 5 hours
nbb_heteroglobulin_transport         127.0.0.1:8106->8010/tcp                                                                                       Up 5 hours
nbb-i-containers                     127.0.0.1:8101->7005/tcp                                                                                       Up 5 hours
nbb_mother_carrie_protocols          127.0.0.1:8107->8010/tcp                                                                                       Up 5 hours
nbb_pituitary_gland                  127.0.0.1:8108->8010/tcp                                                                                       Up 5 hours
nbb_prefrontal_cortex                127.0.0.1:8105->8010/tcp                                                                                       Up 5 hours
nbb_qualia_engine                    127.0.0.1:8303->8010/tcp                                                                                       Up 5 hours
nbb_spiritual_maternal_integration   127.0.0.1:8109->8010/tcp                                                                                       Up 5 hours
nbb_spiritual_root                   127.0.0.1:8103->8010/tcp                                                                                       Up 5 hours
nbb_subconscious                     127.0.0.1:8112->8010/tcp                                                                                       Up 5 hours
nbb_woah_algorithms                  127.0.0.1:8104->8010/tcp                                                                                       Up 5 hours
Registry error: HTTPConnectionPool(host='jarvis-brain-orchestrator', port=7260): Max retries exceeded with url: /registry (Caused by NewConnectionError("HTTPConnection(host='jarvis-brain-orchestrator', port=7260): Failed to establish a new connection: [Errno 111] Connection refused"))
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ # The single most important test: can the loop actually close?
# Send a query → autonomous_learner → bridge → i-container → confirm storage
sqlite3 /mnt/nvme1/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite "
INSERT INTO autonomous_learner_queries
  (query_text, learner_decision, accuracy_average, status)
VALUES
  ('Mount Hope cooperative blockchain governance test', 'learn', 0.85, 'new');
" 2>/dev/null

# Run the bridge manually
cd /mnt/nvme1/msjarvis-rebuild && python3 -c "
import sys
sys.path.insert(0, 'services')
try:
    from bridge_autonomous_to_i_container_fixed import bridge_autonomous_to_identity
    bridge_autonomous_to_identity()
except Exception as e:
    print(f'Bridge error: {e}')
" 2>/dev/null

# Confirm it landed in central identity
sqlite3 /mnt/nvme1/msjarvis-rebuild/data/GISGEODB_ACTIVE.sqlite "
SELECT identity_element, integration_confidence, dgm_acceptance_reasoning
" 2>/dev/nulld DESC LIMIT 3;

🧬 BRIDGING AUTONOMOUS LEARNER → DGM + WOAH → I-CONTAINER
════════════════════════════════════════════════════════════════
Bridge error: no such table: autonomous_learner_queries
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/nvme1/msjarvis-rebuild$ 

