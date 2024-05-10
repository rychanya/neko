import pytest
from httpx import AsyncClient
from httpx_sse import aconnect_sse

pytestmark = pytest.mark.anyio


async def test_root(client: AsyncClient):
    r = await client.get("/")
    assert r.text == "root"


async def test_event(client: AsyncClient):
    async with aconnect_sse(client=client, method="GET", url="/events?uid=1") as event_source:
        async for sse in event_source.aiter_sse():
            assert sse.json() == {"ok": "ok"}
