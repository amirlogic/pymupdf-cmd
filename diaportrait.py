import pymupdf

filename = input("Source Filename: ")


pgnum = 0 
srcnum = 0


src = pymupdf.open(filename)

out = pymupdf.open()

toprect = True

for p in range(0,len(src)):

    if(toprect == True):

        out.new_page()
        page = out[pgnum]
        outrect = pymupdf.Rect(0,0,page.rect.x1,page.rect.y1/2)
        
    else:

        page = out[pgnum]
        outrect = pymupdf.Rect(0,page.rect.y1/2,page.rect.x1,page.rect.y1)
        
    
    page.show_pdf_page(outrect,src,srcnum)

    srcnum += 1

    if(toprect == True):

        toprect = False

    else:

        toprect = True
        pgnum += 1



exported = input("Exported file: ")

out.save(exported,garbage=4,deflate=True)

out.close()

print("File created")



