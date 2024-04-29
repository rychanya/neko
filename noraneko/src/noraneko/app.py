from typing import cast

from blacksheep import Application
from rodi import Container

from noraneko.queue_wrapper import Lobby, QueueManager
from noraneko.routs import router

app = Application(router=router)

app.use_cors(allow_methods="*", allow_origins="http://localhost:5173")


@app.lifespan  # type: ignore
async def lifespan():
    cast(Container, app.services).add_instance(QueueManager())  # type: ignore
    cast(Container, app.services).add_instance(Lobby())  # type: ignore
    yield
