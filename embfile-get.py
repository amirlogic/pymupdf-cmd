import pymupdf

import pathlib

print("Embed a file")

filename = input("PDF Filename: ")

doc = pymupdf.open(filename)

embcount = doc.embfile_count()

print("Number of embedded files:",embcount)

for emb in range(embcount):
    print("\n")
    embdata = doc.embfile_info(emb)
    print(embdata)
    print("\n")
    xq = input("Extract file? (y/n) ")
    if(xq == "y" or xq == "Y"):
        filebytes = doc.embfile_get(embdata['name']) 
        fp = pathlib.Path(embdata['filename'])
        fp.write_bytes(filebytes) 

doc.close()