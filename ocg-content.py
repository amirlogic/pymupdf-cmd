
import pymupdf

print("Add OCG Content")

filename = input("Filename: ")

doc = pymupdf.open(filename)

def new_ocg():

    ocgname = input("OCG Name: ")

    activate = input("Activate? (y/n): ")

    ocgon = True if activate in ("y","Y") else False

    ocg_xref = doc.add_ocg(ocgname,on=ocgon)

    print("OCG Added xref:",ocg_xref)

    more = input("Add more? (y/n): ")

    if(more in ("y","Y")):
        new_ocg()

nwocg = input("Add New OCG xref? (y/n): ").lower()

if nwocg == "y":
    new_ocg()

def insert_ocg():

    ocg_xref = int(input("OCG xref: "))

    pg = int(input("Page: "))

    print("\n","1. insert_text","\n",
          "2. insert_textbox","\n",
          "3. insert_htmlbox","\n")
          #"4. insert_textbox","\n",)
    
    ctype = input("Type of content? ")

    if(ctype == "1"):

        pos = input("Point x,y: ")

        pt = pymupdf.Point(pos.split(',')) 

        txt = input("Text to insert: ")

        page = doc[pg]

        page.insert_text(pt,txt,color=(0,0,0),oc=ocg_xref)

    else:
        print("Not supported")

    #ocgname = input("OCG Name: ")

    #activate = input("Activate? (y/n): ")

    #ocgon = True if activate in ("y","Y") else False

    #ocg_xref = doc.add_ocg(ocgname,on=ocgon)

    #print("OCG Added xref:",ocg_xref)

    more = input("Add more? (y/n): ")

    if(more in ("y","Y")):
        insert_ocg()
        
insert_ocg()

newfile = input("New filename: ")

doc.save(newfile)

doc.close()

print("Task completed")