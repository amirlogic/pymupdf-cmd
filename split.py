import pymupdf

#print("Please enter the filenames ")

srcfile = input("Source file: ")

frompg = int(input("From Page: "))

topage = int(input("To Page: "))

output = input("Output filename: ")

doc1 = pymupdf.open(srcfile)

doc2 = pymupdf.open()                 # new empty PDF

doc2.insert_pdf(doc1, from_page = frompg, to_page = topage )

doc2.save(output)


doc1.close()
doc2.close()

print("File splitted")

