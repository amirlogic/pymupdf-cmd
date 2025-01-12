import pymupdf

import pprint

print("Get an overview of a PDF file")

filename = input("Filename: ")

doc = pymupdf.open(filename)

print("\n","Metadata: ")

pprint.pp(doc.metadata)

print("\n")

print("Pages: ", doc.page_count,"\n")

print("Analyzing pages...","\n")

imgCount = 0

for index,page in enumerate(doc):

    tbls = page.find_tables()
    imgs = page.get_images()
    lnks = page.get_links()

    print("pg#",index,": ")
    
    print("Rect x1,y1:",page.rect.x1,",",page.rect.y1)

    if(len(tbls.tables)>0):
        print("This page contains tables")
        for t in tbls.tables:
            print(t.extract())

    if(len(imgs)>0):
        print("This page contains images")
        imgCount += len(imgs)

    if(len(lnks)>0):
        print("This page contains links")
        print(lnks)

    print("\n")

doc.close()

print("Done")

