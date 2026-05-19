import pymupdf

print("PDF to SVG - Please input the target file: ")

filename = input("Filename: ")
pgnum = input("Page: ")

pgnum = int(pgnum)

doc = pymupdf.open(filename)


page = doc[pgnum]

txtpath = ( input("Text as path? (y/n): ") == "y" )

print("Processing...")

svg = page.get_svg_image(text_as_path=txtpath)

f = open(filename[:-4]+"-"+str(pgnum)+".svg", "a")
f.write(svg)
f.close()


print("SVG saved")

doc.close()