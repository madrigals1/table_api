import os
from dotenv import load_dotenv

load_dotenv()

STATIC_PATH = os.environ.get("STATIC_PATH")
