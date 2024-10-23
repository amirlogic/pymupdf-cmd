import pymupdf


filename = input("Filename: ")

needle = input("Search for: ")

#mvto = input("Move to: ")
#pgnum = int(pgnum)
#mvto = int(mvto)

doc = pymupdf.open(filename)

total = 0

for index, page in enumerate(doc):

    txtpg = page.get_textpage()
    print("page #",index," ",len(txtpg.search(needle))," match found")



#doc.move_page(pgnum, mvto)
#doc.save(f"mv-{pgnum}-{mvto}{filename}")

doc.close()

print("Task complete")

#doc.save("doc-with-new-blank-page.pdf")