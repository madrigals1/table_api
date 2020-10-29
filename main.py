from flask import Flask
from constants import STATIC_PATH
from utils import create_png_from_dict
from flask import request


app = Flask(__name__, static_url_path=f"/{STATIC_PATH}")


@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    table = data.get("table")

    if not table:
        return Flask.abort(404)

    return {"link": create_png_from_dict(table)}
