
import pymupdf

print("Index text into internal links in the document")

filename = input("Filename: ")

doc = pymupdf.open(filename)

pgnum = input("Page index: ")

page = doc[int(pgnum)]

gt = page.get_text("dict",sort=True)

for b in gt["blocks"]:

    if b["type"] == 0:  # text block

        for line in b["lines"]:
            for span in line["spans"]:
            
                if(len(span['text']) > 3):

                    print(span['text'],"\n")

                    mklink = input("Make link (y/n): ").strip().lower() == 'y'

                    if(mklink):

                        topage = int(input("To page index: "))
                        print(span['bbox'])

                        page.insert_link({
                            "kind": pymupdf.LINK_GOTO,
                            "from": pymupdf.Rect(span['bbox'][0], span['bbox'][1], span['bbox'][2], span['bbox'][3]),
                            "page": topage})
                        
                        print("Link created to page", topage, "\n")

output = input("Output filename: ")

if(output.strip()):
    doc.save(output)

doc.close()