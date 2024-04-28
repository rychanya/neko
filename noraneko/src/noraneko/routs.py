from collections.abc import AsyncIterable

from blacksheep import FromQuery, Request, Router
from blacksheep.server.process import is_stopping
from blacksheep.server.sse import ServerSentEvent

from noraneko.game import GameStore
from noraneko.queue_wrapper import Lobby, QueueManager, QueueWrapper

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


@router.get("/lobby/join")
async def join(lobby: Lobby, uid: FromQuery[str], queue_manager: QueueManager):
    lobby.add(uid.value)
    await queue_manager.broadcast(lambda x: True, ServerSentEvent(data={"uid": uid.value}, event="lobby"))


@router.get("/lobby")
async def lobby(lobby: Lobby):
    return tuple(lobby.players)


@router.get("/game")
async def create_game(uid: FromQuery[str], player: FromQuery[str], game_store: GameStore):
    return game_store.create(tuple([uid.value, player.value]))
