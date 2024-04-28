from asyncio import sleep
from typing import Protocol


class GameEvent: ...


class EventSource(Protocol):
    async def __call__(self) -> GameEvent: ...


class GameEngine:
    def __init__(self, event_source: EventSource) -> None:
        self._event_source = event_source

    async def process_event(self, event: GameEvent): ...

    def __aiter__(self):
        return self

    async def __anext__(self):
        await sleep(1)
        return 1
