from flask.cli import FlaskGroup

from . import src


cli = FlaskGroup(src)


if __name__ == "__main__":
    cli()
