
import pymupdf

import session

import datetime

#def removeText(doc):


print("Remove Text")

filename = input("Filename: ")

needle = input("Search for: ")

doc = pymupdf.open(filename)

total = 0

for index, page in enumerate(doc):

    res = page.search_for(needle)
    
    print("page #",index," ",len(res)," match found")
    for found in res:
        print(res)
        total += 1

        rq = input("Remove text? (y/n) ")

        if(rq == "y" or rq == "Y"):
            page.add_redact_annot(found, text=None, fontname=None, fontsize=11, fill=(1, 1, 1), text_color=(0, 0, 0), cross_out=True)   # align=TEXT_ALIGN_LEFT,
            page.apply_redactions()
            print("Text removed")

newfile = input("New filename: ")

doc.save(newfile)

#session.add([datetime.datetime.now(),'remove_text',filename,needle,total])

doc.close()

print("Task complete")