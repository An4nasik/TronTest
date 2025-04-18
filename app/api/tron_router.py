from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.request import TronRequestCreate, TronInfoResponse, TronRequestRead
from app.services.tron import get_tron_info
from app.crud.request import create_request, get_requests
from typing import List
from aiolimiter import AsyncLimiter

router = APIRouter()


limiter = AsyncLimiter(max_rate=1, time_period=2)

@router.post("/tron", response_model=TronInfoResponse)
async def get_tron_data(request: TronRequestCreate, db: AsyncSession = Depends(get_db)):
    async with limiter:
        info = await get_tron_info(request.address)

    await create_request(db, request)
    return info

@router.get("/requests", response_model=List[TronRequestRead])
async def list_requests(skip: int = Query(0), limit: int = Query(10), db: AsyncSession = Depends(get_db)):
    return await get_requests(db, skip, limit)