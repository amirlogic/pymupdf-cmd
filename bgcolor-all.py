import pymupdf

print("Background color edit")

filename = input("Filename: ")

color_r = int(input("Color R: "))

color_g = int(input("Color G: "))

color_b = int(input("Color B: "))

background_color = (color_r/255, color_g/255, color_b/255)

doc = pymupdf.open(filename) 

for page in doc:

    page.draw_rect(page.rect, color=None, fill=background_color, overlay=False)


doc.save("bgcolor_"+str(color_r)+" "+str(color_g)+" "+str(color_b)+" "+filename)

print("Document exported")

doc.close()

