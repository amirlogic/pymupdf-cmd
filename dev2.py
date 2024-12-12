import pymupdf

filename = input("Image filename: ")

#pgnum = int(input("Page number: "))

doc = pymupdf.open()

img = pymupdf.open(filename)

pix = img.get_pixmap()

width, height = pymupdf.paper_size("a4")

rect = pymupdf.Rect(0, 0, width, height) 

#img = open(filename, "rb").read()

img_xref = 0 

page = doc.insert_page(-1) #doc[pgnum]

pg = doc[0]

pg.insert_image(rect, stream=pix.tobytes(), xref=img_xref, keep_proportion=True, overlay=True)

print("Image inserted: ", filename)


doc.save("doc-with-inserted-image.pdf")

#page = doc[pgnum]

#txtdata = page.get_text(opt)


doc.close()

