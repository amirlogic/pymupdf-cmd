import pymupdf

print("Convert to PDF")

while(True):

    filename = input("Filename: ")

    doc = pymupdf.open(filename)

    pdfbytes = doc.convert_to_pdf()

    pdf = pymupdf.open("pdf", pdfbytes)

    exported = input("Exported file: ")

    pdf.save(exported)

    print("Task complete")

    if(input("Convert another file? (y/n): ").lower().strip() != "y"):

        break