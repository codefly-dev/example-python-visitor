import codefly.codefly as codefly
from storage import Storage
from typing import Optional

def setup() -> [Storage]:
    connection_db = codefly.secret(application="backend", service="store", name="postgres", key="connection")

    if connection_db:
        print("setting storage", connection_db)
        store = Storage(connection_db)
    else:
        raise Exception("No connection string for storage")

    return store
