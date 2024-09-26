import pymupdf

filename = input("Filename:")

doc = pymupdf.open(filename) # some new or existing PDF document

print("Metadata: ", doc.metadata)

print("Pages: ", doc.page_count)

print("Analyzing pages...")

imgCount = 0

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

print("Total images count: ",imgCount)

""" page = doc.insert_page(-1, # insertion point: end of document
                        text = "The quick brown fox jumped over the lazy dog",
                        fontsize = 11,
                        width = 595, # page dimension: A4 portrait
                        height = 842,
                        fontname = "Helvetica", # default font
                        fontfile = None, # any font file name
                        color = (0, 0, 0)) """

#doc.save("doc-with-new-blank-page.pdf")