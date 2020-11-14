from src.constants import (
    STATIC_HOSTING_URL,
    project_root_path,
    IMAGES_PATH,
    TABLE_CSS,
    COMPRESS_IMAGES,
)
from uuid import uuid4
import os
import pngquant
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration


def table_dict_to_html(table_dict):
    """ Generate HTML string from Python Dict """

    # Table headers
    headers = "".join([f"<th>{key}</th>" for key in table_dict[0]])
    header_row = f"<tr>{headers}</tr>"

    # Table body
    body = ""
    for row in table_dict:
        body += (
            "<tr>" + "".join([f"<td>{value}</td>" for value in row.values()]) + "</tr>"
        )

    html = "<table>" + header_row + body + "</table>"

    return HTML(string=html)


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

    # Convert to png
    convert_table_dict_to_png(table_dict, image_path)

    # Compress the image
    if COMPRESS_IMAGES:
        compress_image(image_path)

    return f"{STATIC_HOSTING_URL}/{hosting_path}"


def convert_table_dict_to_png(table_dict, image_path):
    # Configuration is used
    font_config = FontConfiguration()
    html_object = table_dict_to_html(table_dict)
    css_object = CSS(string=TABLE_CSS, font_config=font_config)
    html_object.write_png(image_path, stylesheets=[css_object], font_config=font_config)


def compress_image(path):
    """ Compress image to take less space """

    pngquant.quant_image(path)
