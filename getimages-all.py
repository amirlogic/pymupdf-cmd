import pymupdf

print("Get Images (all pages)")

filename = input("Filename: ")


doc = pymupdf.open(filename) 


imgcount = 0

for pgno,page in enumerate(doc):

    images = page.get_images()

    for index,img in enumerate(images):
        
        imgdata = doc.extract_image(img[0])

        with open(filename[:-4]+"_"+str(pgno)+"_ximage"+str(index)+"."+imgdata['ext'],"wb") as f:

            f.write(imgdata['image'])

            imgcount += 1

print(f"{imgcount} images exported")

doc.close()