import pymupdf

import pathlib

ftypes = ('.png','.jpg','.jpeg','.bmp','.svg','.mp4')

print("Embed multiple files (Walk)")

filename = input("PDF Filename: ")

doc = pymupdf.open(filename)

embnum = 0

def addFile(embpath):

    global embnum

    print("Embed #"+str(embnum))

    embytes = pathlib.Path(embpath).read_bytes()

    embname = input("Entry identifier: ")

    doc.embfile_add(embname, embytes)

    embnum += 1

wdir = input("Working directory: ")

wlkpath = pathlib.Path(wdir)

for file_path in wlkpath.iterdir():

    if(file_path.suffix in ftypes):

        print(file_path)
        af = input("Add file? (y/n): ")

        if(af == 'y' or af == 'Y'):
            addFile(file_path)



exported = input("New filename: ")

doc.save(exported)

doc.close()

print(embnum,"files added")