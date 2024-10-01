import pymupdf


filename = input("Filename: ")

pgnum = input("Page number: ")

mvto = input("Move to: ")



pgnum = int(pgnum)

mvto = int(mvto)

doc = pymupdf.open(filename)

doc.move_page(pgnum, mvto)

doc.save(f"mv-{pgnum}-{mvto}{filename}")



doc.close()

print("Page moved")

#doc.save("doc-with-new-blank-page.pdf")