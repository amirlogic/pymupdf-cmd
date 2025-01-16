import pymupdf

import pathlib

print("Embed multiple files")

filename = input("PDF Filename: ")

doc = pymupdf.open(filename)

embnum = 0

def addFile():

    global embnum

    print("Embed #"+str(embnum))

    try:
        embpath = input("Embedded filename: ")

        embytes = pathlib.Path(embpath).read_bytes()

    except:

        print("File not found! Try again")

        embpath = input("Embedded filename: ")

        embytes = pathlib.Path(embpath).read_bytes()

    embname = input("Entry identifier: ")

    doc.embfile_add(embname, embytes)

    embnum += 1

    qmore = input("Embed more files? (y/n) ")

    if(qmore == "y" or qmore == "Y"):
        addFile()

addFile()

exported = input("New filename: ")

doc.save(exported)

doc.close()