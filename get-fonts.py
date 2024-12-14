import pymupdf

print("Get document fonts")

filename = input("Filename: ")

doc = pymupdf.open(filename)

pgno = int(input("Page: "))

#doc.save(filename[:-4]+"_compressed.pdf",garbage=4,deflate=True)

#page = doc[p]

print(doc.get_page_fonts(pgno))

print("Task complete")