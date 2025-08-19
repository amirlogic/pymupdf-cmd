import pymupdf

print("\nDelete All Images (Keeps graphics)\n")

filename = input("Filename: ")

doc = pymupdf.open(filename)

for index, page in enumerate(doc):
    print(f"processing page #{index}...")
    page.add_redact_annot(page.rect)
    page.apply_redactions(
        images=pymupdf.PDF_REDACT_IMAGE_REMOVE,            # remove images
        graphics=pymupdf.PDF_REDACT_LINE_ART_NONE, # don't touch graphics
        text=pymupdf.PDF_REDACT_TEXT_NONE,                 # don't touch text
    )

doc.ez_save(filename[:-4]+"_imgdel.pdf")

print("\nTask complete")