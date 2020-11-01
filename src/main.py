from flask import Flask, jsonify, send_from_directory
from src.utils import create_png_from_dict
from flask import request

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
            detail="Please, make POST request and provide 'table' in body params"
        )

    data = request.json
    table = data.get("table")

    if not table:
        return Flask.abort(404)

    return {"link": create_png_from_dict(table)}


@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)
