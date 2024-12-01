import pymupdf

import base64

print("Get Images (all pages)")

filename = input("Filename: ")


doc = pymupdf.open(filename) 

html_content = "<html><head><title>Image List</title></head><body><header><h2>xref images</h2></header>"

imgcount = 0

lenXREF = doc.xref_length()

for xref in range(1, lenXREF):
    
    if(doc.xref_get_key(xref, "Subtype")[1] == "/Image"):

        imgcount += 1

        imgdata = doc.extract_image(xref)

        base64_bytes = base64.b64encode(imgdata['image'])

        base64_string = base64_bytes.decode("ascii")

        html_content += '<div style="padding:10px;">Image xref='+str(xref)+' ext: '+ imgdata['ext'] +' width: '+ str(imgdata['width']) +' height: '+ str(imgdata['height'])

        html_content += '<img src="data:image/' + imgdata['ext'] + ';base64,' + base64_string + '" alt="xref' + str(xref) + '" />'        # imgbytes.getvalue()

        html_content += '</div>'
        


print(f"{imgcount} images found")

html_content += "</body></html>"

with open(filename[:-4]+"_image_list.html","a") as html_file:
    html_file.write(html_content)

doc.close()