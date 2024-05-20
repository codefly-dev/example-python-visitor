from typing import Optional

import codefly_sdk.codefly as codefly

from src.storage import Storage
from src.cache import Cache


def setup() -> [Storage, Optional[Cache]]:
    connection_db = codefly.secret(service="store", name="postgres", key="connection")

    if connection_db:
        print("setting storage", connection_db)
        store = Storage(connection_db)
    else:
        raise Exception("No connection string for storage")

    cache = None

    connection_write_redis = codefly.secret(service="cache", name="write", key="connection")
    connection_read_redis = codefly.secret(service="cache", name="read", key="connection")

    if connection_read_redis and connection_write_redis:
        print("setting cache")
        print("read: " + connection_read_redis)
        print("write: " + connection_write_redis)
        cache = Cache(connection_write=connection_write_redis, connection_read=connection_read_redis)

    return store, cache
