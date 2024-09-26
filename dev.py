import pymupdf
from io import BytesIO

doc = pymupdf.open() # some new or existing PDF document

page = doc.insert_page(-1, # insertion point: end of document
                        text = "The quick brown fox jumped over the lazy dog",
                        fontsize = 11,
                        width = 595, # page dimension: A4 portrait
                        height = 842,
                        fontname = "Helvetica", # default font
                        fontfile = None, # any font file name
                        color = (0, 0, 0))

pdf_bytes = BytesIO()

doc.save(pdf_bytes)

pdf_bytes.seek(0)

doc.close()

print(pdf_bytes.getvalue())

#doc.save("doc-with-new-blank-page.pdf")