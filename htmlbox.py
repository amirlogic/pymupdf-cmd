import pymupdf

print("Insert HTML Box")

filename = input("Filename: ")

doc = pymupdf.open(filename) 

pgnum = int(input("Page: "))

page = doc[pgnum]

textcontent = input("Text: ")

rx0 = int(input("Rect x0: "))
ry0 = int(input("Rect y0: "))
rx1 = int(input("Rect x1: "))
ry1 = int(input("Rect y1: "))

newfile = input("New file: ")

page.insert_htmlbox(pymupdf.Rect(rx0,ry0,rx1,ry1), textcontent)

doc.save(newfile)


print("Text inserted")

doc.close()


