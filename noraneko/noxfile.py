import nox
from nox.sessions import Session

nox.options.force_venv_backend = "none"


@nox.session()
def run(session: Session):
    session.run("pdm", "install")
    session.run("pdm", "run", "noraneko-cli", env={"APP_SIGNAL_HANDLER": "1"})


@nox.session()
def format(session: Session):
    session.run("pdm", "run", "ruff", "check", "--select", "I", "--fix")
    session.run("pdm", "run", "ruff", "format")
