
import pymupdf as fitz  # PyMuPDF
import pathlib

print("\nAnalyze & Filter PDF Documents in a Directory\n")

# Input parameters
wdir = input("Directory: ").strip()
min_pages = int(input("Minimum page count: ").strip() or "0")
filter_forms = input("Require PDF to have forms? (y/n): ").strip().lower() == "y"
filter_toc = input("Require PDF to have a TOC? (y/n): ").strip().lower() == "y"
filter_embedded = input("Require PDF to have embedded files? (y/n): ").strip().lower() == "y"

wlkpath = pathlib.Path(wdir)

for file_path in wlkpath.iterdir():
    if file_path.suffix.lower() == ".pdf":
        try:
            doc = fitz.open(file_path)

            has_forms = bool(doc.is_form_pdf)
            has_toc = len(doc.get_toc()) > 0
            page_count_ok = doc.page_count >= min_pages
            has_embedded = doc.embfile_count() > 0

            # Apply filters
            if (
                (not filter_forms or has_forms) and
                (not filter_toc or has_toc) and
                (not filter_embedded or has_embedded) and
                page_count_ok
            ):
                print(f"\n{file_path.name}")
                print("Pages:", doc.page_count,
                      "- TOC items:", len(doc.get_toc()),
                      "- Embedded files:", doc.embfile_count())
                if has_forms:
                    print("This PDF has forms")

                lnkcnt = sum(len(page.get_links()) for page in doc)
                imgcnt = sum(len(page.get_images()) for page in doc)
                print("Links:", lnkcnt, "- Images:", imgcnt)

            doc.close()

        except Exception as e:
            print(f"Error reading {file_path.name}: {e}")
