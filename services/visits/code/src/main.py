from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import codefly_sdk.codefly as codefly
from src.models import *
from src.setup import setup

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
cache = None

def set_store(store_):
    global store
    store = store_

def set_cache(cache_):
    global cache
    cache = cache

if codefly.in_runtime_mode():
    print("RUNNING")
    store_, cache_ = setup()
    set_store(store_)
    set_cache(cache_)

@app.get("/version")
async def version():
    return {"version": codefly.get_version()}


@app.post("/visit", response_model=CreateVisitResponse)
async def visit():
    if not store:
        print("no store")
        raise HTTPException(status_code=500, detail="No store available")
    resp = store.create_visit()
    statistics = store.get_visit_statistics()
    if cache:
        cache.set("statistics", statistics)
    if not resp:
        raise HTTPException(status_code=500, detail="Can't create visit")
    return resp


@app.get("/visit/statistics", response_model=GetVisitStatisticsResponse)
async def visit():
    if not store:
        print("no store")
        raise HTTPException(status_code=500, detail="No store available")
    if cache:
        statistics = cache.get("statistics", GetVisitStatisticsResponse)
        if statistics:
            print("getting cached value")
            return statistics
    resp = store.get_visit_statistics()
    if not resp:
        raise HTTPException(status_code=500, detail="Can't get visit statistics")
    if cache:
        print("setting cache")
        cache.set("statistics",resp)
    return resp
