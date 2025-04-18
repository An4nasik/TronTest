from pydantic import BaseModel
from datetime import datetime


class TronRequestCreate(BaseModel):
    address: str

class TronRequestRead(BaseModel):
    id: int
    address: str
    timestamp: datetime

    class Config:
        from_attributes = True

class TronInfoResponse(BaseModel):
    address: str
    balance: int
    bandwidth: int
    energy: int
