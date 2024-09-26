import pymupdf

print("Please input the target file: ")

filename = input("Filename: ")
pgnum = input("Page: ")

pgnum = int(pgnum)

doc = pymupdf.open(filename) # some new or existing PDF document

#print("Metadata: ", doc.metadata)
#print("Pages: ", doc.page_count)
#print("Links: ", doc.page_count)
#print("Analyzing pages...")
#print(type(doc[0]))

page = doc[pgnum]

pix = page.get_pixmap()

pix.save("page-%i.png" % page.number)

print("pixmap saved")

""" for index,page in enumerate(doc):
    #print(index,page.search_for("for"))
    lnks = page.get_links()
    print(index,"Links: ", len(lnks))
    if(len(lnks)>0):
        print(lnks)

    #print("Fonts:",page.get_fonts()) """





doc.close()