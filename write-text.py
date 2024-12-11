import pymupdf

print("Write text")

filename = input("Filename: ")

pgnum = int(input("Page: "))

doc = pymupdf.open(filename)

""" rx0 = int(input("Rect x0: "))
ry0 = int(input("Rect y0: "))
rx1 = int(input("Rect x1: "))
ry1 = int(input("Rect y1: ")) """

#rc = pymupdf.Rect(rx0,ry0,rx1,ry1)

instext = input("Text content: ")

fontsize = float(input("Font size: "))

rotate = float(input("Rotate: "))

opacity = float(input("Opacity: "))

page = doc[pgnum]


wrt = pymupdf.TextWriter(page.rect)     #pymupdf.Rect(rx0,ry0,rx1,ry1) 
wrt2 = pymupdf.TextWriter(page.rect)

wrt.append(pymupdf.Point(20,20),instext,fontsize=fontsize)
wrt2.append(pymupdf.Point(0,0),"Zero",fontsize=fontsize)
wrt2.append(pymupdf.Point(30,30),"Test",fontsize=fontsize)



page.write_text(rect=page.rect, writers=(wrt,wrt2),    # pymupdf.Rect(rx0,ry0,rx1,ry1)
                overlay=True, color=None, opacity=opacity, keep_proportion=True, rotate=rotate, oc=0)

#page.draw_circle((20, 20), 5, color=(1, 0, 0), width=2)

export = input("New filename: ")

doc.save(export)

print("Text inserted: ", export)

import session

import datetime

#session.add([datetime.datetime.now(),'write_text',rx0,ry0,rx1,ry1,filename,export])

doc.close()



