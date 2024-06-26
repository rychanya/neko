import uvicorn

from noraneko.app import app


def run():
    uvicorn.run(
        app,
        # host="0.0.0.0",
        port=8080,
        log_level="info",
    )


if __name__ == "__main__":
    run()
