import pymupdf

print("Text vs OCR Needed Checker")

filename = input("Filename: ")

doc = pymupdf.open(filename)

txtcount = 0

imgcount = 0

docfonts = []

for page in doc:

    r = page.get_text("dict")

    for b in r['blocks']:

        if(b['type'] == 0):

            txtcount += 1

        elif(b['type'] == 1):

            imgcount += 1

    pagefonts = page.get_fonts()

    for f in pagefonts:

        if(f[3] not in tuple(docfonts)):

            docfonts.append(f[3])


print("Text blocks:",txtcount)

print("Image count:",imgcount)

print(f"Fonts ({len(docfonts)})")

for ft in docfonts:

    print(ft)

doc.close()

