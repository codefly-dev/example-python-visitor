import os
from httpx import AsyncClient, ASGITransport
import pytest
import codefly_sdk.codefly as codefly
from codefly_cli.codefly import with_dependencies, with_cli_logs, with_debug, with_code_path
import time
from src.main import app, set_store, set_cache, setup
from src.models import *

with_cli_logs()
with_debug()
with_code_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost:8080") as ac:
        response = await ac.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "0.0.0"}

import os

@pytest.mark.asyncio
async def test_visits(with_dependencies):
    store, cache = setup()
    set_store(store)
    set_cache(cache)

    # Get statistics
    resp = store.get_visit_statistics()
    total_visits = resp.total_visits

    # Create a visit
    resp = store.create_visit()
    assert resp.total_visits == total_visits + 1

    stats = store.get_visit_statistics()
    assert total_visits + 1 == stats.total_visits

    cache.set("statistics", stats)
    # Wait a bit because of possible read/replica
    time.sleep(1)
    back = cache.get("statistics", GetVisitStatisticsResponse)
    assert stats.total_visits == back.total_visits

    total_visits = back.total_visits

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost:8080") as ac:
        resp = await ac.get("/visit/statistics")
        assert resp.status_code == 200
        assert resp.json()["total_visits"] == total_visits

        resp = await ac.post("/visit")
        assert resp.status_code == 200
        updated_total_visits = resp.json()["total_visits"]
        assert total_visits + 1 == updated_total_visits

        # Wait a bit because of possible read/replica
        time.sleep(1)
        resp = await ac.get("/visit/statistics")
        assert resp.status_code == 200
        assert resp.json()["total_visits"] == updated_total_visits
