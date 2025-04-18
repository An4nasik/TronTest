import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_post_tron_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/tron", json={"address": "TPAe77oEGDLXuNjJhTyYeo5vMqLYdE3GN8U"})
    assert response.status_code == 200
    data = response.json()
    assert "balance" in data
    assert "bandwidth" in data
    assert "energy" in data
