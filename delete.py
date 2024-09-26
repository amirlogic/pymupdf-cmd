import pymupdf


filename = input("Filename: ")

pgnum = input("Page number: ")

pgnum = int(pgnum)

doc = pymupdf.open(filename)

doc.delete_page(pgnum)

doc.save(f"del-{filename}")



doc.close()

print("Page deleted")

#doc.save("doc-with-new-blank-page.pdf")