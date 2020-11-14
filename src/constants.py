from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

STATIC_HOSTING_URL = os.getenv("STATIC_HOSTING_URL")
IMAGES_PATH = os.getenv("IMAGES_PATH")
COMPRESS_IMAGES = os.getenv("COMPRESS_IMAGES", False) in (True, "True")


def project_root_path():
    return Path(__file__).parent.parent


TABLE_CSS = """
@page {
    size: A5;
    margin: 0.5cm;
}

unicode {
    font-family: 'OpenSansEmoji', sans-serif;
}

@font-face {
    font-family: 'OpenSansEmoji';
    src: url(data:font/truetype;charset=utf-8;base64,<-- encoded_font_base64_string-->) format('truetype');
}

table {
    background-color: white;
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
