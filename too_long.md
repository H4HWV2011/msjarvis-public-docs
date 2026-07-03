(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

rg -n '@app\.(post|get)\("/validate"' services
echo '---'
rg -n '10001|10002|10023|--port' services/bridge_cross_dgm_*.py
echo '---'
sed -n '1,220p' services/dgm_orchestrator_fake.py
services/bbb_validator.py
16:@app.post("/validate", response_model=ValidateResponse)
---
services/bridge_cross_dgm_10061.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10062.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10049.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10050.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10037.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10063.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10038.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10025.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10051.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10026.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10013.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10014.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10039.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10001.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10002.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10027.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10064.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10028.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10016.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10065.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10052.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10004.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10015.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10017.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10053.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10005.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10066.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10030.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10003.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10054.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10029.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10042.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10006.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10031.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10007.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10040.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10055.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10067.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10068.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10019.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10044.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10020.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10033.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10009.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10021.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10045.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10057.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10022.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10058.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10046.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10008.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10023.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10035.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10011.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10043.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10036.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10024.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10060.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10032.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10018.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10056.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10034.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10041.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10059.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10047.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10069.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10048.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10012.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")

services/bridge_cross_dgm_10010.py
29:parser.add_argument("--port", type=int, default=5215)
49:    parser.add_argument("--port", type=int, default=5215, help="Port to listen on")
---
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Fake 69-DGM Orchestrator")

class Req(BaseModel):
    message: str
    userid: str
    source: str

@app.post("/process")
async def process(req: Req):
    # For testing: always approve
    return {"status": "approved_by_69_validators", "info": "fake orchestrator"}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "fake_69_dgm_orchestrator"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

