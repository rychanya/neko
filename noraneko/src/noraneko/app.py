from typing import cast

from blacksheep import Application
from rodi import Container

from noraneko.broker import broker
from noraneko.queue_wrapper import QueueManager
from noraneko.routs import router

app = Application(router=router, show_error_details=True)

app.use_cors(allow_methods="*", allow_origins="http://localhost:5173")


@app.lifespan  # type: ignore
async def lifespan():
    if not broker.is_worker_process:
        await broker.startup()

    cast(Container, app.services).add_instance(QueueManager())  # type: ignore

    yield
    if not broker.is_worker_process:
        await broker.shutdown()
