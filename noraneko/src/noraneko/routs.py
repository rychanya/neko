import asyncio
from collections.abc import AsyncIterable

from blacksheep import FromQuery, Request, Router
from blacksheep.server.process import is_stopping
from blacksheep.server.sse import ServerSentEvent

from noraneko.queue_wrapper import QueueManager

router = Router()





@router.get("/")
async def root():
    return "root"


@router.get("/events")
async def home(request: Request, queue_manager: QueueManager, uid: FromQuery[str]) -> AsyncIterable[ServerSentEvent]:
    stop_event = asyncio.Event()

    async def stop_task():
        while True:
            if is_stopping() or await request.is_disconnected():
                stop_event.set()
            await asyncio.sleep(1)

    stop = asyncio.create_task(stop_task())

    # while True:
    #     await asyncio.sleep(1)
    #     yield ServerSentEvent(data="test")
    yield ServerSentEvent(data={"ok": "ok"})

    stop.cancel()
