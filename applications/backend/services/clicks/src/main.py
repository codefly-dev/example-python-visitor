from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import codefly.codefly as codefly
from clicker import *
from setup import setup

print("Starting server")

codefly.init()

app = FastAPI()

# if codefly.is_local():
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


store = None

if codefly.is_running():
    print("RUNNING")
    store = setup()

@app.get("/version")
async def version():
    return {"version": codefly.get_service().version}


@app.post("/click", response_model=GetClicksResponse)
async def do_click():
    if not store:
        print("no store")
        raise HTTPException(status_code=500, detail="No store available")
    resp = store.create_click()
    if not resp:
        raise HTTPException(status_code=500, detail="Can't get clicks")
    return resp

@app.get("/clicks", response_model=GetClicksResponse)
async def get_clicks():
    if not store:
        print("no store")
        raise HTTPException(status_code=500, detail="No store available")
    resp = store.get_clicks()
    if not resp:
        raise HTTPException(status_code=500, detail="Can't get clicks")
    return resp
