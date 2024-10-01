import pymupdf


filename = input("Filename: ")

pgnum = input("Page number: ")

pgnum = int(pgnum)

doc = pymupdf.open(filename)

doc.fullcopy_page(pgnum)

doc.save(f"fcopy-{pgnum}-{filename}")



doc.close()

print("Page copied")
