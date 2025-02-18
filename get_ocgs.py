
import pymupdf

import pprint

print("Get OCG Layers")

filename = input("Filename: ")

doc = pymupdf.open(filename)

print("\n")

pprint.pp(doc.get_ocgs())



