import pymupdf

import pathlib

print("Attach a file")

filename = input("Filename: ")


pgnum = int(input("Page number: "))

point_x = int(input("Point x: "))
point_y = int(input("Point y: "))


doc = pymupdf.open(filename) 

attachpath = input("Attach path: ")

attachment = pathlib.Path(attachpath).read_bytes()

page = doc[pgnum]

point = pymupdf.Point(point_x, point_y)


attachname = input("Entry identifier: ")

file_annotation = page.add_file_annot(point, attachment, attachname)

exported = input("New filename: ")

doc.save(exported) 

print("File attached")

doc.close()

