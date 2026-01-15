from pydantic import BaseModel, Field

class Threat(BaseModel):
    name: str
    location: str
    danger_rate: int = Field(..., x=1, y=10) 

class ResponseThreat(BaseModel):
    count: int
    top: list[Threat]
