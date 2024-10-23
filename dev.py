import pymupdf
#from io import BytesIO

doc = pymupdf.open("acea.pdf") # some new or existing PDF document

""" page = doc.insert_page(-1, # insertion point: end of document
                        text = "The quick brown fox jumped over the lazy dog",
                        fontsize = 11,
                        width = 595, # page dimension: A4 portrait
                        height = 842,
                        fontname = "Helvetica", # default font
                        fontfile = None, # any font file name
                        color = (0, 0, 0))
 """

page = doc[0]

tpg = page.get_textpage()



#pdf_bytes = BytesIO()

#doc.save(pdf_bytes)

#pdf_bytes.seek(0)

doc.close()

html = tpg.extractHTML()

print(tpg.extractHTML())

HTML_BEFORE = "<!DOCTYPE html><html><head><title>HTML</title></head><body>"

HTML_AFTER = "</body></html>"

f = open("output.html", "a")
f.write(html)
f.close()

#doc.save("doc-with-new-blank-page.pdf")