from pydantic import BaseModel, Field

class Threat(BaseModel):
    name: str
    location: str
    risk_level: int = Field(..., x=1, y=10) 

class ResponseThreat(BaseModel):
    count: int
    top: list[Threat]
