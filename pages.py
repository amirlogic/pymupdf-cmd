import pymupdf

print("Please input the target file: ")

filename = input("Filename:")

doc = pymupdf.open(filename) # some new or existing PDF document

print("Metadata: ", doc.metadata)

print("Pages: ", doc.page_count)

#print("Links: ", doc.page_count)
#print("Analyzing pages...")
#print(type(doc[0]))

for index,page in enumerate(doc):
    #print(index,page.search_for("for"))
    lnks = page.get_links()
    print(index,"Links: ", len(lnks))
    if(len(lnks)>0):
        print(lnks)

    #print("Fonts:",page.get_fonts())


""" imgCount = 0

for page in doc:
    tbls = page.find_tables()
    imgs = page.get_images()

    print("Tables found: ",len(tbls.tables))
    if(len(tbls.tables)>0):
        print("This page contains tables")
        for t in tbls.tables:
            print(t.extract())

    if(len(imgs)>0):
        print("This page contains images")
        imgCount += len(imgs)

print("Total images count: ",imgCount) """

""" page = doc.insert_page(-1, # insertion point: end of document
                        text = "The quick brown fox jumped over the lazy dog",
                        fontsize = 11,
                        width = 595, # page dimension: A4 portrait
                        height = 842,
                        fontname = "Helvetica", # default font
                        fontfile = None, # any font file name
                        color = (0, 0, 0)) """

#doc.save("doc-with-new-blank-page.pdf")

doc.close()