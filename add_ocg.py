
import pymupdf

print("Add OCG Layer")

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
        
new_ocg()

newfile = input("New filename: ")

doc.save(newfile)

doc.close()

print("Task completed")