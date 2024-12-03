import pymupdf

print("Insert HTML Box from Text/HTML File")

filename = input("PDF Filename: ")

src = input("Source file: ")

doc = pymupdf.open(filename) 

pgnum = int(input("Page: "))

page = doc[pgnum]

newfile = input("New file: ")

with open(src,'r') as srcfile:

    res = page.insert_htmlbox(page.rect, srcfile.read())

    doc.save(newfile)

    print("Text inserted",res)

doc.close()


