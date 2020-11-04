from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

STATIC_HOSTING_URL = os.getenv("STATIC_HOSTING_URL")


def project_root_path():
    return Path(__file__).parent.parent
