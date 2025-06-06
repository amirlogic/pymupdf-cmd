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

            extract = input("Extract file? (y/n): ")

            if(extract == 'y' or extract == 'Y'):

                import pathlib

                filebytes = annot.get_file()

                xpath = pathlib.Path(input("Extract to: ")) / annot.file_info['filename']

                xpath.write_bytes(filebytes)

                print("File extracted")
        
        else:
            print("type: ",annot.type)
            print(annot.rect)
            pprint.pp(annot.info)
            
        print("\n")



#print(str(lnkcount),"link(s) found")

doc.close()


