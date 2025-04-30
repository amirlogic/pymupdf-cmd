import pymupdf

print("Scrub")

filename = input("Filename: ")

doc = pymupdf.open(filename) 

doc.scrub()

newfile = input("New file: ")
    
doc.save(newfile)



doc.close()


