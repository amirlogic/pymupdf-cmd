import pymupdf

import pathlib

formats = (".png",".svg",".jpg",".jpeg",".tiff",".bmp",".gif")

print("Image Dir to PDF")

imgdir = pathlib.Path(input("Directory: "))

doc = pymupdf.open()

for item in imgdir.iterdir():
    if(item.is_file()):
        if item.suffix in formats:
            print(item)
            img = pymupdf.open(item)
            pdfbytes = img.convert_to_pdf()
            pdf = pymupdf.open("pdf", pdfbytes)
            doc.insert_pdf(pdf)
            img.close()


exported = input("Exported file: ")

doc.save(exported)

doc.close()

print("Task complete")