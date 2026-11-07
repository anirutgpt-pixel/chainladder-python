#!/usr/bin/env python
"""Export the Chapter 15 monitoring notebook tables to an Excel workbook."""

from __future__ import annotations

import argparse
import contextlib
import io
import json
from pathlib import Path
from typing import Any

import pandas as pd


NOTEBOOK_PATH = Path(__file__).with_name("chapter_15_monitoring.ipynb")
SHEET_NAMES = {
    "Reported_Triangle": "Origin Year",
    "Selected_CDF": "Group",
    "Ultimates_2007": "Origin Year",
    "Monitoring_2008": "Origin Year",
    "Monitor_Totals": "Group",
    "Monthly_2008": "Origin Year",
    "Monthly_Totals": "Group",
}


def execute_notebook(notebook_path: Path) -> dict[str, Any]:
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    namespace: dict[str, Any] = {
        "__name__": "__main__",
        "display": lambda *args, **kwargs: None,
    }

    with contextlib.redirect_stdout(io.StringIO()):
        for number, cell in enumerate(notebook["cells"], start=1):
            if cell.get("cell_type") != "code":
                continue
            source = cell.get("source", "")
            if isinstance(source, list):
                source = "".join(source)
            source = source.replace("from IPython.display import display", "")
            exec(compile(source, f"{notebook_path}#cell-{number}", "exec"), namespace)

    return namespace


def export_workbook(notebook_path: Path, output_path: Path) -> None:
    namespace = execute_notebook(notebook_path)
    sheet1 = namespace["sheet1"]
    sheet2 = namespace["sheet2"]
    sheet3 = namespace["sheet3"]
    sheet4 = namespace["sheet4"]
    dev = namespace["dev"]

    cdf_triangle = dev.cdf_
    cdf_triangle = cdf_triangle[cdf_triangle.ddims <= 36]
    selected_cdf = cdf_triangle.to_frame(origin_as_datetime=False)

    sheet3_totals = (
        sheet3[["Actual", "Expected", "Difference"]]
        .sum()
        .rename("Total")
        .to_frame()
        .T
    )
    sheet4_totals = (
        sheet4[
            [
                "Actual Jan",
                "Expected Jan",
                "Diff Jan",
                "Actual Feb",
                "Expected Feb",
                "Diff Feb",
            ]
        ]
        .sum()
        .rename("Total")
        .to_frame()
        .T
    )

    tables = {
        "Reported_Triangle": sheet1,
        "Selected_CDF": selected_cdf,
        "Ultimates_2007": sheet2,
        "Monitoring_2008": sheet3,
        "Monitor_Totals": sheet3_totals,
        "Monthly_2008": sheet4,
        "Monthly_Totals": sheet4_totals,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        for sheet_name, frame in tables.items():
            frame.to_excel(
                writer,
                sheet_name=sheet_name,
                index=True,
                index_label=SHEET_NAMES[sheet_name],
            )
            worksheet = writer.sheets[sheet_name]
            worksheet.freeze_panes = "B2"
            worksheet.auto_filter.ref = worksheet.dimensions


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        default=NOTEBOOK_PATH.with_suffix(".xlsx"),
        help="Output workbook path (defaults next to the notebook).",
    )
    args = parser.parse_args()
    export_workbook(NOTEBOOK_PATH, args.output)
    print(f"Exported workbook: {args.output}")


if __name__ == "__main__":
    main()
