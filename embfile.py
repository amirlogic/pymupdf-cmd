import pymupdf

import pathlib

print("Embed a file")

filename = input("PDF Filename: ")

doc = pymupdf.open(filename)

embpath = input("Embedded filename: ")

embytes = pathlib.Path(embpath).read_bytes()

embname = input("Entry identifier: ")

doc.embfile_add(embname, embytes) 

exported = input("New filename: ")

doc.save(exported)

doc.close()