from taskiq import InMemoryBroker
from noraneko.game.engine import GameEvent

broker = InMemoryBroker()


@broker.task
async def handle_game_event(event: GameEvent): ...

 
async def setup():
    await broker.startup()
    yield broker
    await broker.shutdown()
