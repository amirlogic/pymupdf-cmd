import pymupdf

print("Remove an image")

filename = input("Filename: ")

pgnum = int(input("Page: "))

xref = int(input("xref: "))

newfile = input("New file: ")

doc = pymupdf.open(filename) 

page = doc[pgnum]

page.delete_image(xref)     


doc.save(newfile)

print("Image removed!")

doc.close()



