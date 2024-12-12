import pymupdf

print("Get Table of Content")

filename = input("Filename: ")

doc = pymupdf.open(filename)

#pgno = int(input("Page: "))

#doc.save(filename[:-4]+"_compressed.pdf",garbage=4,deflate=True)

#page = doc[p]

print(doc.get_toc())

print("Task complete")