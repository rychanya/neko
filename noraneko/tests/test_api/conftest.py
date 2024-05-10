import pytest
from httpx import ASGITransport, AsyncClient
from noraneko.app import app

pytestmark = pytest.mark.anyio


@pytest.fixture
async def client():
    await app.start()
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost") as _client:
        yield _client
