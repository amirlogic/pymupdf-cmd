import pymupdf

print("Insert HTML Box from Text/HTML File")

filename = input("PDF Filename: ")

src = input("Source file: ")

css = input("CSS file: ")

doc = pymupdf.open(filename) 

pgnum = int(input("Page: "))

page = doc[pgnum]

newfile = input("New file: ")

with open(src,'r') as srcfile:

    cssfile = open(css,"r")

    res = page.insert_htmlbox(page.rect, srcfile.read(), css=cssfile.read())

    doc.save(newfile)

    print("Text inserted",res)

doc.close()


