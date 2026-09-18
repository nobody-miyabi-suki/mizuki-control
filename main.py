from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
import asyncio
from pydantic import BaseModel
import json
from fastapi import FastAPI
import platform
import psutil

app = FastAPI()

@app.get("/")
def home():
    print("OK")
    return "Lelouch VI Britannia Commands YOU"

@app.get("/doc")
def doc():
    print("Doc OK")
    return "DOC IN YOUR DOCKER"

@app.get("/system")
def system():
    print("You See my Pengiun?!")
    return {
	    "hostname": platform.node(),
	    "system": platform.system(),
	    "release": platform.release(),
	    "machine": platform.machine(),
	    "i Am": "ATOMIC"
    }
@app.get("/anime")
def anime():
    print("oni san")
    return "Python DaiSuki"
@app.get("/cpu")
def cpu():
    return {
        "cores": psutil.cpu_count(),
        "usage": psutil.cpu_percent()
    }
@app.get("/ui")
def ui():
    return FileResponse("ui/index.html")

@app.get("/event")
async def event():
    async def generate():
        while True:
            data = {
                "cpu": psutil.cpu_percent(),
                "ram": psutil.virtual_memory().percent
            }

            yield f"data: {json.dumps(data)}\n\n"

            await asyncio.sleep(1)

    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )

class Command(BaseModel):
    command: str


@app.post("/command")
def command(data: Command):
    print(f"Command received: {data.command}")

    return {
        "status": "ok",
        "command": data.command
    }