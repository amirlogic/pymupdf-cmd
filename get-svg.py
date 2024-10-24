import pymupdf

print("PDF to SVG - Please input the target file: ")

filename = input("Filename: ")
pgnum = input("Page: ")

pgnum = int(pgnum)

doc = pymupdf.open(filename) # some new or existing PDF document


page = doc[pgnum]

svg = page.get_svg_image()

f = open(filename[:-4]+".svg", "a")
f.write(svg)
f.close()

#pix.save("page-%i.png" % page.number)

print("SVG saved")


doc.close()