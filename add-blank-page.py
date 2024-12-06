
import pymupdf

print("Insert blank page")

filename = input("Filename: ")

print("Use 0 to insert at the start")
print("Use -1 to insert at the end")
pgnum = int(input("Insert position: "))

output = input("New file: ")

doc = pymupdf.open(filename)

doc.new_page(pgnum)

doc.save(output)

print("Page inserted at position",pgnum)

doc.close()