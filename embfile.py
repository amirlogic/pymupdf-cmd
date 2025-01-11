import pymupdf

import pathlib

print("Embed a file")

filename = input("PDF Filename: ")

#embed = input("Embed: ")

doc = pymupdf.open(filename)

embpath = input("Embedded filename: ")

embytes = pathlib.Path(embpath).read_bytes()

#embedded_doc = pymupdf.open("Video-Game-Revenue.jpg")
#embedded_data = embedded_doc.tobytes()
# embed with the file name and the data

embfname = input("Emb filename: ")

doc.embfile_add(embfname, embytes) 

exported = input("New filename: ")

doc.save(exported)

doc.close()