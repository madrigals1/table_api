from flask import Flask, jsonify
from src.utils import create_png_from_dict
from flask import request
import asyncio

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(
        detail="Table API is working. Use /convert to convert dict into table PNG"
    )


@app.route("/convert", methods=["POST", "GET"])
def convert():
    if request.method == "GET":
        return jsonify(
            detail="Please, make POST request and provide 'table' in request body"
        )

    data = request.json
    table = data.get("table")

    if not table:
        return jsonify(detail="Please, provide 'table' in request body")

    return {
        "link": asyncio.get_event_loop().run_until_complete(create_png_from_dict(table))
    }
