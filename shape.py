
import pymupdf

doc = pymupdf.open()

doc.new_page()

print("Draw a Shape\n")

print("1. Line")
print("2. Rectangle")
print("3. Circle")

snum = input("Shape #: ")

page = doc[0]


if(snum == "1"):

    shape = page.new_shape()

    pt1 = input("Point 1 (x,y): ").split(",")

    pt2 = input("Point 2 (x,y): ").split(",")

    shape.draw_line(pymupdf.Point(int(pt1[0]),int(pt1[1])),pymupdf.Point(int(pt2[0]),int(pt2[1])))

    shape.commit()


elif(snum == "2"):
     
    shape = page.new_shape()

    rc = input("Rectangle: (x0,y0,x1,y1): ")

    rect = rc.split(",")

    shape.draw_rect(pymupdf.Rect(*rect))

    shape.commit()


elif(snum == "3"):
     
    shape = page.new_shape()

    rd = input("Center: (x,y)").split(",")
    
    radius = input("Radius: ")

    shape.draw_circle(pymupdf.Point(*rd))

    shape.commit()

else:

    print("Not supported")


exported = input("Exported: ")

doc.ez_save(exported)

doc.close()