import pymupdf

import pprint

print("Get links")

filename = input("Filename: ")

#pgnum = input("Page: ")
#pgnum = int(pgnum)

doc = pymupdf.open(filename) 

lnkcount = 0

for page in doc:

    links = page.get_links()
    if(len(links)>0):
        pprint.pp(page.get_links())
        lnkcount += 1

#page = doc[pgnum]
#txt = page.get_text("blocks")
""" for row in txt:
    print(row[4][:30],"...") """

print(str(lnkcount),"link(s) found")

doc.close()

#print("Done")

