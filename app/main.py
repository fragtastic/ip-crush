from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import JSONResponse
from ipconsolidation import consolidate

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Default response"}

@app.post("/ipconsolidation")
async def consolidate_ips(file: UploadFile = File(...), grouped: bool = True, json: bool = False):
    output, count_addresses, count_networks = consolidate(file.file, grouped=grouped)
    if json:
        return JSONResponse(content={"output": output, "count_addresses": count_addresses, "count_networks": count_networks})
    else:
        return Response(content='\n'.join(output), media_type="text/plain", headers={"X-Count-Addresses": str(count_addresses), "X-Count-Networks": str(count_networks)})
