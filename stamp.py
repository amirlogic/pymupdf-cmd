import pymupdf


print("\nAdd a Stamp Annot\n")

filename = input("Filename: ")

doc = pymupdf.open(filename) 

print("\nSTAMP_Approved \t0")
print("\nSTAMP_AsIs \t1")
print("\nSTAMP_Confidential \t2")
print("\nSTAMP_Departmental \t3")
print("\nSTAMP_Experimental \t4")
print("\nSTAMP_Expired \t5")
print("\nSTAMP_Final \t6")
print("\nSTAMP_ForComment \t7")
print("\nSTAMP_ForPublicRelease \t8")
print("\nSTAMP_NotApproved \t9")
print("\nSTAMP_NotForPublicRelease \t10")
print("\nSTAMP_Sold \t11")
print("\nSTAMP_TopSecret \t12")
print("\nSTAMP_Draft \t13\n")

stampnum = int(input("Stamp: "))

rect_str = input("Rect x0,y0,x1,y1: ")

rectrr = rect_str.split(',')


for page in doc:

    page.add_stamp_annot(pymupdf.Rect(rectrr[0],rectrr[1],rectrr[2],rectrr[3]), stamp=stampnum)



exported = input("New filename: ")

doc.save(exported) 

print("Stamp added")

doc.close()

