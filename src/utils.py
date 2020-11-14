from src.constants import (
    STATIC_HOSTING_URL,
    project_root_path,
    IMAGES_PATH,
    TABLE_HTML_CONTENT,
)
from uuid import uuid4
import os
import imgkit
import pngquant


def table_dict_to_html(table_dict):
    """ Generate HTML string from Python Dict """

    # Content before and after table
    before = TABLE_HTML_CONTENT.get("before")
    after = TABLE_HTML_CONTENT.get("after")

    # Table headers
    headers = "".join([f"<th>{key}</th>" for key in table_dict[0]])
    header_row = f"<tr>{headers}</tr>"

    # Table body
    body = ""
    for row in table_dict:
        body += "<tr>"
        body += "".join([f"<td>{value}</td>" for value in row.values()])
        body += "</tr>"

    return before + header_row + body + after


def create_png_from_dict(table_dict):
    """ Create PNG image from Table Dict """

    # Get root path of project
    root = project_root_path()

    # Generate unique name for image
    image_uid = uuid4()
    hosting_path = f"{IMAGES_PATH}/{image_uid}.png"
    image_path = f"{root}/static/{hosting_path}"

    # Table path
    html_name = "tmp.html"
    html_path = f"{root}/static/{IMAGES_PATH}/{html_name}"

    # If path for file doesn't exist, create it
    if not os.path.exists(f"{root}/static/{IMAGES_PATH}"):
        os.makedirs(f"{root}/static/{IMAGES_PATH}")

    # Save HTML
    html = table_dict_to_html(table_dict)

    with open(html_path, "w+") as f:
        f.write(html)

    # Options for wkhtmltopdf
    options = {"encoding": "UTF-8"}
    # Create PNG image
    imgkit.from_file(html_path, image_path, options=options)

    # Compress the image
    compress_image(image_path)

    return f"{STATIC_HOSTING_URL}/{hosting_path}"


def compress_image(path):
    """ Compress image to take less space """

    pngquant.quant_image(path)
