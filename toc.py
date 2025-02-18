import pymupdf

import pprint

print("Get Table of Content")

filename = input("Filename: ")

doc = pymupdf.open(filename)

#print("Table of Content")

pprint.pp(doc.get_toc())

print("Task complete")