
import pymupdf

print("Font Demo - Requires pymupdf-fonts")

doc = pymupdf.open()

doc.new_page()

page = doc[0]


figo = pymupdf.Font("figo")

page.insert_font(fontname="figo", fontbuffer=figo.buffer)

page.insert_text(pymupdf.Point(50,50), "This text is in figo", fontname="figo")




doc.save("output/fonts-demo.pdf")

doc.close()

