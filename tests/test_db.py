import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.request import TronRequest
from app.schemas.request import TronRequestCreate
from app.crud.request import create_request

@pytest.mark.asyncio
async def test_create_request(db_session: AsyncSession):
    test_address = "TPAe77oEGDLXuNjJhTyYeo5vMqLYdE3GN8U"
    request_data = TronRequestCreate(address=test_address)
    new_request = await create_request(db_session, request_data)
    assert isinstance(new_request, TronRequest)
    assert new_request.address == test_address
