from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import codefly.codefly as codefly
from storage import Storage
from cache import Cache
from visit import *

codefly.init()

app = FastAPI()

if codefly.is_local():
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

connection_db = codefly.get_service_provider_info(application="backend", service="store", name="postgres", key="connection")
connection_write_redis = codefly.get_service_provider_info(application="backend", service="cache", name="redis", key="write")
connection_read_redis = codefly.get_service_provider_info(application="backend", service="cache", name="redis", key="read")


if connection_db:
    print("setting storage")
    store = Storage(connection_db)

if connection_read_redis and connection_write_redis:
    print("setting cache")
    print("read: " + connection_read_redis)
    print("write: " + connection_write_redis)
    cache = Cache(connection_write=connection_write_redis, connection_read=connection_read_redis)



@app.get("/version")
async def version():
    return {"version": codefly.get_service().version}


@app.post("/visit", response_model=CreateVisitResponse)
async def visit():
    if not store:
        print("no store")
        raise HTTPException(status_code=500, detail="No store available")
    resp = store.create_visit()
    statistics = store.get_visit_statistics()
    if cache:
        cache.set("statistics",statistics)
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
