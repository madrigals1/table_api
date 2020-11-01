import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

STATIC_PATH = os.environ.get("STATIC_PATH")
FLASK_DEBUG = os.environ.get("FLASK_DEBUG")


def project_root_path():
    return Path(__file__).parent.parent
