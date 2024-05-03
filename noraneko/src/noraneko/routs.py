from collections.abc import AsyncIterable

from blacksheep import FromQuery, Request, Router
from blacksheep.server.process import is_stopping
from blacksheep.server.sse import ServerSentEvent

from noraneko.queue_wrapper import QueueManager, QueueWrapper

router = Router()


@router.get("/events")
async def home(request: Request, queue_manager: QueueManager, uid: FromQuery[str]) -> AsyncIterable[ServerSentEvent]:
    async def stop() -> bool:
        if is_stopping() or await request.is_disconnected():
            return True
        return False

    with QueueWrapper(uid.value, queue_manager, stop) as queue:
        async for q in queue:
            yield q
