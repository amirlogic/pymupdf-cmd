
import pymupdf

import pathlib

print("\nAnalyze PDF Documents in a Directory\n")

wdir = input("Directory (defaults to CWD): ")

if(wdir == ""):

    wdir = pathlib.Path.cwd()

wlkpath = pathlib.Path(wdir)

for file_path in wlkpath.iterdir():

    if(file_path.suffix == ".pdf"):

        print(file_path.name)

        try:

            doc = pymupdf.open(file_path)

            toclen = len(doc.get_toc())

            print("pages:",doc.page_count,"- TOC items:",toclen,"- Embedded files:",doc.embfile_count())

            if(doc.is_form_pdf != False):
                print("This PDF has forms")

            #print(doc.get_layer())

            lnkcnt = 0

            imgcnt = 0

            for page in doc:

                lnkcnt += len(page.get_links())

                imgcnt += len(page.get_images())


            doc.close()

            print("Links:",lnkcnt,"- Images:",imgcnt)

            print("\n")
        
        except:
            print("Error")

        