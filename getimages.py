import pymupdf

print("Get Images")

filename = input("Filename: ")

pgnum = int(input("Page: "))


doc = pymupdf.open(filename) 

page = doc[pgnum]

images = page.get_images()

imgcount = 0

for index,img in enumerate(images):
    
    imgdata = doc.extract_image(img[0])

    with open(filename+"_ximage"+str(index)+"."+imgdata['ext'],"wb") as f:

        f.write(imgdata['image'])

        imgcount += 1

print(f"{imgcount} images exported")

doc.close()