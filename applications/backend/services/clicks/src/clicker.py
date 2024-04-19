from pydantic import BaseModel
from typing import List
from datetime import datetime


class GetClicksResponse(BaseModel):
    count: int
