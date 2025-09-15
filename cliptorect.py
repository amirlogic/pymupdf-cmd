import pymupdf

print("Clip to Rect")

filename = input("Filename: ")

doc = pymupdf.open(filename)

rstr = input("Rect (x0,y0,x1,y1): ")

r = rstr.split(',')

for page in doc:

    page.clip_to_rect( pymupdf.Rect(r[0],r[1],r[2],r[3]) )


exported = input("New file: ")

if(exported == ""):

    exported = filename[:-4]+"_clip.pdf"

doc.ez_save(exported)

doc.close()

print("Task complete")