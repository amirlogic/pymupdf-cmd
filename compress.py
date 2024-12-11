import pymupdf

print("Compress a document")

filename = input("Filename: ")

doc = pymupdf.open(filename)


doc.save(filename[:-4]+"_compressed.pdf",garbage=4,deflate=True)

print("Task complete")