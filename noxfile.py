import nox
from shlex import split
from os.path import realpath

nox.options.reuse_existing_virtualenvs = True


@nox.session
def site(session):
    session.install("-r", "requirements.txt")
    if "live" in session.posargs:
        session.run(
            *split(
                f"sphinx-autobuild -b dirhtml . _build/dirhtml --ignore {realpath('_build')}"
            )
        )
    else:
        session.run(
            *"sphinx-build -nW --keep-going -b dirhtml . _build/dirhtml".split()
        )
        session.log("open ./_build/dirhtml/index.html")
