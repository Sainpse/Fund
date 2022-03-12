from pydantic import BaseModel
from typing import List, Optional


class Observation(BaseModel):
    asset: str
    observation: List[float]
    time: str