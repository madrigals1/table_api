from flask import Flask
from src.constants import STATIC_PATH, FLASK_DEBUG
from src.utils import create_png_from_dict
from flask import request

# Run app
debug_mode = FLASK_DEBUG == 1
app = Flask(__name__, static_url_path=f"/{STATIC_PATH}")
app.run(debug=debug_mode)


@app.route("/")
def index():
    return {
        "Detail": "Table API is working. Use /convert to convert dict into table PNG"
    }


@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    table = data.get("table")

    if not table:
        return Flask.abort(404)

    return {"link": create_png_from_dict(table)}
