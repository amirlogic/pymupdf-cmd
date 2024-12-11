
import pymupdf

import session

import datetime


print("Text Search")

filename = input("Filename: ")

needle = input("Search for: ")

doc = pymupdf.open(filename)

total = 0

for index, page in enumerate(doc):

    #txtpg = page.get_textpage()
    #res = txtpg.search(needle)

    res = page.search_for(needle)
    
    print("page #",index," ",len(res)," match found")
    for found in res:
        print(res)



session.add([datetime.datetime.now(),'search_text',filename,needle,total])

doc.close()

print("Task complete")