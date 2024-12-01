import pymupdf

print("Replace an image")

filename = input("Filename: ")

pgnum = int(input("Page: "))

xref = int(input("xref: "))

replaceby = input("Replace by: ")

newfile = input("New file: ")

doc = pymupdf.open(filename) 

page = doc[pgnum]

page.replace_image(xref, filename=replaceby)

doc.save(newfile)

print("Image replaced!")

doc.close()



