from src.constants import STATIC_HOSTING_URL, project_root_path, IMAGES_PATH
from uuid import uuid4
import os
import imgkit


def table_dict_to_html(table_dict):
    before = """
<html lang="en">
  <head>
    <title>Title</title>
    <style>
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
    </style>
  </head>
  <body>
    <table>
    """
    after = "</table></body></html>"
    headers = "".join([f"<th>{key}</th>" for key in table_dict[0]])
    header_row = f"<tr>{headers}</tr>"
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
    hosting_path = f"{image_uid}.png"
    image_path = f"{root}/{IMAGES_PATH}/{hosting_path}"

    # Table path
    html_name = "tmp.html"
    html_path = f"{root}/{IMAGES_PATH}/{html_name}"

    # If path for file doesn't exist, create it
    if not os.path.exists(f"{root}/{IMAGES_PATH}"):
        os.makedirs(f"{root}/{IMAGES_PATH}")

    # Save HTML
    html = table_dict_to_html(table_dict)
    with open(html_path, "w+") as f:
        f.write(html)

    # Options for wkhtmltopdf
    options = {"encoding": "UTF-8"}
    # Create PNG image
    imgkit.from_file(html_path, image_path, options=options)

    return f"{STATIC_HOSTING_URL}/{hosting_path}"
