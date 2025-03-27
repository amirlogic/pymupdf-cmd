import pymupdf

import pprint

print("Get Annotations")

filename = input("Filename: ")

doc = pymupdf.open(filename) 



for page in doc:

    for annot in page.annots():

        if annot.type[1] == "FreeText":

            print("FreeText annot: ")
            print(annot.get_text())

        elif annot.type[1] == "Text":

            print("Text")
            pprint.pp(annot.info['content'])
        
        elif annot.type[1] == "Highlight":
            
            print("Highlight")
            pprint.pp(annot.rect)
            print("Highlighted:",page.get_text(clip=annot.rect))

        elif annot.type[1] == "FileAttachment":

            print("File Attach.")
            pprint.pp(annot.file_info)
        
        else:
            print("type: ",annot.type)
            print(annot.rect)
            pprint.pp(annot.info)
            
        print("\n")



#print(str(lnkcount),"link(s) found")

doc.close()


