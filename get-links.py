import pymupdf

import pprint

print("Get links")

filename = input("Filename: ")

doc = pymupdf.open(filename) 

lnkcount = 0

for page in doc:

    links = page.get_links()
    
    if(len(links)>0):
        print("page",page.number,"\n")
        pprint.pp(page.get_links())
        lnkcount += 1
        print("\n")



print(str(lnkcount),"link(s) found")

doc.close()


