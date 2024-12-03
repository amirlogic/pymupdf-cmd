import pymupdf

print("Insert HTML Box from Text/HTML File")

filename = input("PDF Filename: ")

src = input("Source file: ")

doc = pymupdf.open(filename) 

pgnum = int(input("Page: "))

page = doc[pgnum]

#textcontent = input("Text: ")

""" rx0 = int(input("Rect x0: "))
ry0 = int(input("Rect y0: "))
rx1 = int(input("Rect x1: "))
ry1 = int(input("Rect y1: ")) """

newfile = input("New file: ")

with open(src,'r') as srcfile:

    page.insert_htmlbox(page.rect, srcfile.read())

doc.save(newfile)


print("Text inserted")

doc.close()


