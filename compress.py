import pymupdf

print("Compress a document")

filename = input("Filename: ")

doc = pymupdf.open(filename)

pimgs = input("Compress images? (y/n): ")

if(pimgs.strip().lower() == 'y'):

    doc.rewrite_images()

doc.subset_fonts()

doc.ez_save(filename[:-4]+"_compressed.pdf")

print("Task complete")