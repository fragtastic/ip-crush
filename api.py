from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import JSONResponse
import ipaddress

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Default response"}

@app.post("/ipconsolidation")
async def consolidate_ips(file: UploadFile = File(...), grouped: bool = True, json: bool = False):
    ips = []
    count_addresses = 0
    count_networks = 0
    output = []
    for line in file.file:
        line = line.decode().strip()
        if not line:
            continue
        try:
            addr = ipaddress.IPv4Address(line)
            ips.append(addr)
            count_addresses += 1
        except ipaddress.AddressValueError:
            if grouped:
                for network in ipaddress.collapse_addresses(ips):
                    output.append(str(network))
                    count_networks += 1
                ips = []
                output.append(line)
    # Must do this one final time since there may be nothing after the last set of addresses
    for network in ipaddress.collapse_addresses(ips):
        output.append(str(network))
        count_networks += 1
    if json:
        return JSONResponse(content={"output": output, "count_addresses": count_addresses, "count_networks": count_networks})
    else:
        return Response(content='\n'.join(output), media_type="text/plain", headers={"X-Count-Addresses": str(count_addresses), "X-Count-Networks": str(count_networks)})
