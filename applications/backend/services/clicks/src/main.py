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
    print("setting up store")
    store = setup()
    if store is None:
        print("no store")
        raise Exception("No store available")

@app.get("/version")
async def version():
    return {"version": codefly.get_service().version}


@app.post("/click", response_model=GetClicksResponse)
async def do_click():
    resp = store.create_click()
    if not resp:
        raise HTTPException(status_code=500, detail="can't get clicks")
    return resp

@app.get("/clicks", response_model=GetClicksResponse)
async def get_clicks():
    resp = store.get_clicks()
    if not resp:
        raise HTTPException(status_code=500, detail="Can't get clicks")
    return resp
