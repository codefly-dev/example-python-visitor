from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import text
from typing import Optional
import datetime

from clicker import *

class Storage:
    def __init__(self, connection: str) -> None:
        self.engine = create_engine(connection)
        self.metadata = MetaData()
        self.store = Table('store', self.metadata, autoload_with=self.engine)
        self.session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.session_factory)

    def create_click(self) -> Optional[GetClicksResponse]:
        session = self.Session()
        try:
            session.execute(text("""
                INSERT INTO click (count)
                VALUES (0)
                ON CONFLICT DO NOTHING
            """))
            result = session.execute(text("""
                UPDATE click
                SET count = count + 1
                RETURNING count 
            """), {}).fetchone()
            session.commit()
            return GetClicksResponse(count=result[0])
        except Exception as e:
            session.rollback()
            print(f"database: error occurred: {e}")
        finally:
            session.close()

    def get_clicks(self) -> Optional[GetClicksResponse]:
        session = self.Session()
        try:
            rows = session.execute(text("""
                SELECT count
                FROM click
            """)).fetchone()
            if rows is None:
                return GetClicksResponse(count=0)
            return GetClicksResponse(count=rows[0])
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            session.close()
