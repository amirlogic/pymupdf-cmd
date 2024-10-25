import pymupdf

filename = input("Filename: ")

pgnum = input("Page: ")

pgnum = int(pgnum)


doc = pymupdf.open(filename) # some new or existing PDF document


page = doc[pgnum]

txt = page.get_text("blocks")

for row in txt:
    print(row[4][:30],"...")



#print("Metadata: ", doc.metadata)
#print("Pages: ", doc.page_count)
#print("Analyzing pages...")
#print("Total images count: ",imgCount)

doc.close()

print("Done")

