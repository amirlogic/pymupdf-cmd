import pymupdf

import pprint

print("Drawings - Please input the target file: ")

filename = input("Filename: ")
pgnum = input("Page: ")

pgnum = int(pgnum)

doc = pymupdf.open(filename) # some new or existing PDF document


page = doc[pgnum]

drawings = page.get_drawings()

pprint.pp(drawings)

#pix.save("page-%i.png" % page.number)

print("Completed")


doc.close()