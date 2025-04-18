import pymupdf

import pathlib

formats = (".png",".svg",".jpg",".jpeg",".tiff",".bmp",".gif")

print("Image Dir to PDF")

imgdir = pathlib.Path(input("Directory: "))

doc = pymupdf.open()

toc = []

tpg = 1

for item in imgdir.iterdir():
    if(item.is_file()):
        if item.suffix in formats:
            print(item)
            img = pymupdf.open(item)
            pdfbytes = img.convert_to_pdf()
            pdf = pymupdf.open("pdf", pdfbytes)
            doc.insert_pdf(pdf)
            img.close()
            toc.append([1,item.stem,tpg])
            print("Done")
            tpg += 1

doc.set_toc(toc)

exported = input("Exported file: ")

doc.save(exported)

doc.close()

print("Task complete")