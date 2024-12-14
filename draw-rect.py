import pymupdf

import session

import datetime


print("Draw Rectangle")

filename = input("Filename: ")

doc = pymupdf.open(filename) 

pgnum = int(input("Page: "))

page = doc[pgnum]

rstr = input("Rect (x0,y0,x1,y1): ")

rectrr = rstr.split(',')

""" ry0 = int(input("Rect y0: "))
rx1 = int(input("Rect x1: "))
ry1 = int(input("Rect y1: ")) """
""" if(kind == 0):
    print("not supported")
elif(kind == 1):
    print("GOTO")
    dpg = int(input("Destination page: "))
    linkdict = {"kind":kind,"page":dpg, "from":pymupdf.Rect(rx0,ry0,rx1,ry1)}
elif(kind == 2):
    print("Internet uri")
    uri = input("URI: ")
    linkdict = {"kind":kind,"uri":uri, "from":pymupdf.Rect(rx0,ry0,rx1,ry1)}
elif(kind == 3):
    print("not supported")
elif(kind == 4):
    print("not supported")
elif(kind == 5):
    print("not supported") """

#newfile = input("New file: ")
#page.insert_link(linkdict)

page.draw_rect(pymupdf.Rect(int(rectrr[0]),int(rectrr[1]),int(rectrr[2]),int(rectrr[3])))

newfile = input('Newfile: ')

doc.save(newfile)

session.add([datetime.datetime.now(),'draw_rect',filename,rstr])

print("Task completed")

doc.close()


