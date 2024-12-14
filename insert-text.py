import pymupdf

print("Insert text")

filename = input("Filename: ")

pgnum = int(input("Page: "))

doc = pymupdf.open(filename)

px = int(input("Point x: "))
py = int(input("Point y: "))
#rx1 = int(input("Rect x1: "))
#ry1 = int(input("Rect y1: "))


pt = pymupdf.Point(px,py) 

instext = input("Text content: ")

fontsize = int(input("Font size: "))

rotate = int(input("Rotate(x90): "))

page = doc[pgnum]

rc = page.insert_text(pt,  # bottom-left of 1st char
                     instext, 
                     fontname = "helv",  # the default font
                     fontsize = fontsize,  # the default font size
                     rotate = rotate,  # also available: 90, 180, 270
                     )


export = input("New filename: ")

doc.save(export)

print("Text inserted: ", export)

import session

import datetime

session.add([datetime.datetime.now(),'insert_text',px,py,filename,export])

doc.close()



