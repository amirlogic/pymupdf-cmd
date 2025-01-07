import pymupdf

import pathlib

filename = input("Filename: ")

pgnum = int(input("Page: "))

#img = open(input("Image file: "), "rb").read()

img = pathlib.Path(input("Image file: ")).read_bytes()

doc = pymupdf.open(filename)

page = doc[pgnum]

def getRect():

    opt = input("Whole page? (y/n) ")

    if(opt == "y" or opt == "Y"):
        return page.rect
    
    else:
        rstr = input("Rect (x0,y0,x1,y1): ")
        spr = rstr.split(',')
        return pymupdf.Rect(int(spr[0]), int(spr[1]), int(spr[2]), int(spr[3])) 


img_xref = 0 

img_xref = page.insert_image(getRect(), stream=img, xref=img_xref )

exported = input("Exported file: ")

doc.save(exported)

doc.close()

print("Image inserted: ", filename)



