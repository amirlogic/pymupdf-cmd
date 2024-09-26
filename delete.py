import pymupdf


filename = input("Filename: ")

doc = pymupdf.open(filename)

doc.delete_page()

doc.save(f"del-{filename}")



doc.close()

print("Page deleted")

#doc.save("doc-with-new-blank-page.pdf")