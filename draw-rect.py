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


page.draw_rect(pymupdf.Rect(int(rectrr[0]),int(rectrr[1]),int(rectrr[2]),int(rectrr[3])))

newfile = input('Newfile: ')

doc.save(newfile)

session.add([datetime.datetime.now(),'draw_rect',filename,rstr])

print("Task completed")

doc.close()


