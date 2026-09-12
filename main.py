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
