import pymupdf

import session

print("Insert link")

filename = input("Filename: ")

doc = pymupdf.open(filename) 

pgnum = int(input("Page: "))

instext = input('Text: ')

page = doc[pgnum]

rx0 = int(input("Rect x0: "))
ry0 = int(input("Rect y0: "))
rx1 = int(input("Rect x1: "))
ry1 = int(input("Rect y1: "))

print("0: LINK_NONE")
print("1: LINK_GOTO")
print("2: LINK_URI")
print("3: LINK_LAUNCH")
print("4: LINK_NAMED")
print("5: LINK_GOTOR")

kind = int(input("Kind: (0-5) "))

if(kind == 0):
    print("not supported")

elif(kind == 1):
    print("GOTO")
    dpg = int(input("Destination page: "))
    linkdict = {"kind":kind,"page":dpg, "from":pymupdf.Rect(rx0,ry0,rx1,ry1)}

elif(kind == 2):
    print("Internet uri")
    uri = input("URI: ")
    linkdict = {"kind":kind,"uri":uri, "from":pymupdf.Rect(rx0,ry0,rx1,ry1)}

elif(kind == 3):
    print("not supported")

elif(kind == 4):
    print("not supported")

elif(kind == 5):
    print("not supported")

newfile = input("New file: ")

page.insert_link(linkdict)

page.insert_textbox(pymupdf.Rect(rx0,ry0,rx1,ry1), instext)

doc.save(newfile)


print("Link inserted")

doc.close()


