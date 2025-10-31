
import pymupdf

from pathlib import Path

print("Export to HTML Page\n")

filename = input("Filename: ")

doc = pymupdf.open(filename)

pagebody = ""

for index,page in enumerate(doc):

    svg = page.get_svg_image()
    pagebody += f"<div style=\"text-align:center;\">{svg}</div>"

html = f"<!DOCTYPE html><html><head><title>{filename}</title></head><body>{pagebody}</body></html>"

exported = input("Exported file: ")

html_path = Path(exported)

html_path.write_text(html, encoding="utf-8")

print("File exported")

doc.close()