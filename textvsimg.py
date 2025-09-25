import pymupdf

filename = input("Filename: ")

doc = pymupdf.open(filename)

txtcount = 0

imgcount = 0

for page in doc:

    r = page.get_text("dict")

    for b in r['blocks']:

        if(b['type'] == 0):

            txtcount += 1

        elif(b['type'] == 1):

            imgcount += 1

print("Text blocks:",txtcount)

print("Image count:",imgcount)


doc.close()

