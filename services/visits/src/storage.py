from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import text
from typing import Optional
import datetime

from models import *

class Storage:
    def __init__(self, connection: str) -> None:
        self.engine = create_engine(connection)
        self.metadata = MetaData()
        self.store = Table('store', self.metadata, autoload_with=self.engine)
        self.session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.session_factory)

    def create_visit(self) -> Optional[CreateVisitResponse]:
        session = self.Session()
        try:
            today = datetime.today().date()
            session.execute(text("""
                INSERT INTO store (date, visits)
                VALUES (:date, 0)
                ON CONFLICT (date) DO NOTHING
            """), {'date': today})
            result = session.execute(text("""
                UPDATE store
                SET visits = visits + 1
                WHERE date = :date
                RETURNING visits
            """), {'date': today}).fetchone()
            session.commit()
            stats = self.get_visit_statistics()
            return CreateVisitResponse(total_visits=stats.total_visits) if result else None
        except Exception as e:
            session.rollback()
            print(f"database: error occurred: {e}")
        finally:
            session.close()

    def get_visit_statistics(self) -> Optional[GetVisitStatisticsResponse]:
        session = self.Session()
        try:
            rows = session.execute(text("""
            SELECT date, SUM(visits) OVER (ORDER BY date) as cumulative_visits
            FROM store
            ORDER BY date
        """)).fetchall()
            visits = [DailyVisitStatistics(date=row[0], visits=row[1]) for row in rows]
            total_visits = visits[-1].visits if visits else 0
            return GetVisitStatisticsResponse(total_visits=total_visits, visits=visits)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            session.close()
