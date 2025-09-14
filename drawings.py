import pymupdf

import pprint

print("Vector graphics")

filename = input("Filename: ")

doc = pymupdf.open(filename)

pgnum = int(input("Page: "))

page = doc[pgnum]

drawings = page.get_drawings()

#pprint.pp(drawings)

print("Vector(s) found: ", len(drawings))

newdoc = pymupdf.open()

newdoc.new_page()

newpg = newdoc[0]

#newpg.cluster_drawings(drawings=drawings)

for index,d in enumerate(drawings):

    newpg.draw_rect(d['rect'])

    print(f"\n{index}")
    print(d['rect'])

    x = d['rect'].x0

    y = d['rect'].y0

    try:

        newpg.insert_text(pymupdf.Point(x,y),str(index))

    except:

        print("error",index)

print("\n")

""" for page in doc:

    page.recolor(components=4) """


exported = input("New file: ")

if(exported == ""):

    exported = filename[:-4]+f"_pg0_vectors.pdf"

newdoc.ez_save(exported)

doc.close()

newdoc.close()

print("Task complete")