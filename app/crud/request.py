from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.request import TronRequest
from app.schemas.request import TronRequestCreate
from typing import List

async def create_request(db: AsyncSession, request: TronRequestCreate) -> TronRequest:
    db_request = TronRequest(address=request.address)
    db.add(db_request)
    await db.commit()
    await db.refresh(db_request)
    return db_request

async def get_requests(db: AsyncSession, skip: int = 0, limit: int = 10) -> List[TronRequest]:
    result = await db.execute(
        select(TronRequest).order_by(TronRequest.timestamp.desc()).offset(skip).limit(limit)
    )
    return list(result.scalars().all())
