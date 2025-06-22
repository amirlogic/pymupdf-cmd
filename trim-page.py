import pymupdf

filename = input("Source Filename: ")

src = pymupdf.open(filename)

out = pymupdf.open()

print("Affected pages (zero-based):")

start = int(input("Start page (default 0): "))

end = int(input("End page (default last page): "))

top = int(input("Top margin: "))

bottom = int(input("Bottom margin: "))

pgnum = 0 


for p in range(0,len(src)):

    out.new_page()
    page = out[pgnum]

    if(p >= start and p <= end):

        crop = pymupdf.Rect( 0, page.rect.y0+top, page.rect.x1, page.rect.y1-bottom )

        page.show_pdf_page(page.rect,src,pgnum,clip=crop)

    else:
        page.show_pdf_page(page.rect,src,pgnum)

    pgnum += 1

exported = input("Exported file: ")

out.save(exported,garbage=4,deflate=True)

out.close()

print("File created")



