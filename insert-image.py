import pymupdf

filename = input("Filename: ")

#pgnum = input("Page: ")
#pgnum = int(pgnum)

doc = pymupdf.open() # some new or existing PDF document

rect = pymupdf.Rect(0, 0, 100, 100) 

img = open(filename, "rb").read()

img_xref = 0 

page = doc.insert_page(-1) #doc[pgnum]

pg = doc[0]

img_xref = pg.insert_image(rect, stream=img, xref=img_xref )

print("Image inserted: ", filename)


doc.save("doc-with-inserted-image.pdf")

doc.close()



