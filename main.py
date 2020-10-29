from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
STATIC_PATH = os.environ.get("STATIC_PATH")

app = Flask(__name__, static_url_path=f"/{STATIC_PATH}")


@app.route("/")
def hello_world():
    return "Hello, World!"
