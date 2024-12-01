import pymupdf

print("Attach a file")

filename = input("Filename: ")

#attach = input("Attach: ")

pgnum = int(input("Page number: "))

point_x = int(input("Point x: "))

point_y = int(input("Point y: "))


doc = pymupdf.open(filename) 

attachment = pymupdf.open("evsales.svg")   # attach

page = doc[pgnum]

point = pymupdf.Point(point_x, point_y)

attachment_data = attachment.tobytes()

file_annotation = page.add_file_annot(point, attachment_data, "attachment.svg")


doc.save("output.pdf")        # filename[:4]+"-"+attach[:4]+".pdf"

print("File attached")

doc.close()

