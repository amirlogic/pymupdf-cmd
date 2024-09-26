import pymupdf

print("Please enter the filenames of the two files to be merged:")

fileone = input("Filename 1: ")

filetwo = input("Filename 2: ")

merged = input("Merged filename: ")


doc_a = pymupdf.open(fileone)
doc_b = pymupdf.open(filetwo)

doc_a.insert_pdf(doc_b) # merge the docs
doc_a.save(merged)


doc_a.close()
doc_b.close()

print("Files merged")

