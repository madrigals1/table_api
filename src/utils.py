from src.constants import project_root_path
from uuid import uuid4
import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy as np


def render_mpl_table(
    data,
    col_width=3.0,
    row_height=0.625,
    font_size=14,
    header_color="#40466e",
    row_colors=["#f1f1f2", "w"],
    edge_color="w",
    bbox=[-0.1615, -0.138, 1.29, 1.29],
    header_columns=0,
    ax=None,
    **kwargs,
):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array(
            [col_width, row_height]
        )
        fig, ax = plt.subplots(figsize=size)
        ax.axis("off")
    mpl_table = ax.table(
        cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs
    )
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in mpl_table._cells.items():
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight="bold", color="w")
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0] % len(row_colors)])
    return ax.get_figure(), ax


def create_png_from_dict(dict):
    # Create dataframe
    data_frame = DataFrame.from_dict(dict)

    fig, ax = render_mpl_table(data_frame, header_columns=0, col_width=1.5)
    table_uid = uuid4()
    root = str(project_root_path())
    static_path = f"/static/images/{table_uid}.png"
    path = root + static_path
    fig.savefig(path)

    return static_path
