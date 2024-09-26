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

img_xref = pg.insert_image(rect, stream=img,
                 xref=img_xref )

print("Image inserted: ", filename)

""" doc.insert_image(rect, 
             *, 
             alpha=-1, 
             filename=filename, 
             height=0, 
             keep_proportion=True, 
             mask=None, 
             oc=0, 
             overlay=True, 
             pixmap=None, 
             rotate=0, 
             stream=None, 
             width=0, 
             xref=0)
 """
""" page = doc.insert_page(-1, # insertion point: end of document
                        text = "The quick brown fox jumped over the lazy dog",
                        fontsize = 11,
                        width = 595, # page dimension: A4 portrait
                        height = 842,
                        fontname = "Helvetica", # default font
                        fontfile = None, # any font file name
                        color = (0, 0, 0)) """

doc.save("doc-with-inserted-image.pdf")

doc.close()



