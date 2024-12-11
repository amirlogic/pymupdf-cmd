import pymupdf

print("Insert HTML Box - Affects all pages")

filename = input("Filename: ")

doc = pymupdf.open(filename) 

textcontent = input("Text: ")

rx0 = int(input("Rect x0: "))
ry0 = int(input("Rect y0: "))
rx1 = int(input("Rect x1: "))
ry1 = int(input("Rect y1: "))

newfile = input("New file: ")

for pgno,page in enumerate(doc):

    res = page.insert_htmlbox(pymupdf.Rect(rx0,ry0,rx1,ry1), textcontent)
    print("Page #",pgno,res)

doc.save(newfile)

print("Text inserted")

doc.close()


