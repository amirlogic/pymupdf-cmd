import pymupdf

print("Grayscale")

filename = input("Filename: ")

doc = pymupdf.open(filename)

for page in doc:

    page.recolor(components=1)

exported = input("New file: ")

doc.ez_save(exported)

doc.close()

print("Task complete")