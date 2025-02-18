
import pymupdf

res = pymupdf.open()

filename = input("Filename: ")

doc = pymupdf.open(filename)

for page in doc:

    pix = page.get_pixmap()

    pdfbytes = pix.pdfocr_tobytes(language="eng")

    imgpdf = pymupdf.open("pdf", pdfbytes)

    res.insert_pdf(imgpdf)

exported = input("New filename: ")

res.save(exported)

print("Task completed")