import pymupdf


print("Vector graphics to Pixmap")

filename = input("Filename: ")

doc = pymupdf.open(filename)

pgnum = int(input("Page: "))

page = doc[pgnum]

rect = input("Rect (x0, y0, x1, y1): ")

r = rect.split(', ')

if len(r) != 4:
    r = rect.split(',')

rx0 = float(r[0])
ry0 = float(r[1])
rx1 = float(r[2])
ry1 = float(r[3])


page.set_cropbox(pymupdf.Rect(rx0,ry0,rx1,ry1))


svg = page.get_svg_image()

print("\n")

exported = input("New file: ")

if(exported == ""):

    exported = filename[:-4]+"-"+str(pgnum)+".svg"

f = open(exported, "a")
f.write(svg)
f.close()


doc.close()


print("Task complete")