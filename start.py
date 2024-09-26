import pymupdf

content = input("Text: ")
filename = input("Filename: ")

doc = pymupdf.open() # some new or existing PDF document

page = doc.insert_page(-1, # insertion point: end of document
                        text = content,
                        fontsize = 11,
                        width = 595, # page dimension: A4 portrait
                        height = 842,
                        fontname = "Helvetica", # default font
                        fontfile = None, # any font file name
                        color = (0, 0, 0))

doc.save(filename)

print("File created")

doc.close()