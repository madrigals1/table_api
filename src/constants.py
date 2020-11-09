from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

STATIC_HOSTING_URL = os.getenv("STATIC_HOSTING_URL")
IMAGES_PATH = os.getenv("IMAGES_PATH")


def project_root_path():
    return Path(__file__).parent.parent


TABLE_CSS = """
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
"""

TABLE_HTML_CONTENT = {
    "before": (
        '<html lang="en"><head><title>Title</title>'
        f"<style>{TABLE_CSS}</style></head><body><table>"
    ),
    "after": "</table></body></html>",
}
