import pymupdf

pgnum = int(input("Number of pages: "))
filename = input("Filename: ")

doc = pymupdf.open() # some new or existing PDF document

for p in range(pgnum):

    doc.new_page()

""" page = doc.insert_page(-1, # insertion point: end of document
                        text = content,
                        fontsize = 11,
                        width = 595, # page dimension: A4 portrait
                        height = 842,
                        fontname = "Helvetica", # default font
                        fontfile = None, # any font file name
                        color = (0, 0, 0)) """

doc.save(filename)

print("File created, ",pgnum,"page(s)")

doc.close()