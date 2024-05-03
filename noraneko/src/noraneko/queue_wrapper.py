from __future__ import annotations

from asyncio import Queue, TimeoutError, gather, wait_for
from types import TracebackType
from typing import Awaitable, Callable, Self

from blacksheep.server.sse import ServerSentEvent


class QueueManager:
    def __init__(self) -> None:
        self.queues: set[QueueWrapper] = set()

    def add(self, wrapper: QueueWrapper) -> None:
        self.queues.add(wrapper)

    def discard(self, wrapper: QueueWrapper) -> None:
        self.queues.discard(wrapper)

    async def broadcast(
        self,
        filter_func: Callable[
            [QueueWrapper],
            bool,
        ],
        item: ServerSentEvent,
    ):
        consumers = filter(filter_func, self.queues)
        tasks = [wrapper.put(item) for wrapper in consumers]
        await gather(*tasks)


class QueueWrapper:
    def __init__(self, uid: str, manager: "QueueManager", stop: Callable[..., Awaitable[bool]]) -> None:
        self.queue: Queue[ServerSentEvent] = Queue()
        self.uid = uid
        self.manager = manager
        self.stop = stop

    async def put(self, item: ServerSentEvent):
        await self.queue.put(item)

    async def iterator(self):
        while not await self.stop():
            try:
                yield await wait_for(self.queue.get(), 1)
            except TimeoutError:
                ...

    def __aiter__(self):
        return self

    async def __anext__(self):
        while not await self.stop():
            try:
                return await wait_for(self.queue.get(), 1)
            except TimeoutError:
                ...
        raise StopAsyncIteration

    def __enter__(self) -> Self:
        self.manager.add(self)
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> bool | None:
        self.manager.discard(self)
