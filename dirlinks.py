
import pathlib

import pymupdf


print("Get links in a directory")


wdir = input("Directory (defaults to CWD): ")

if(wdir == ""):

    wdir = pathlib.Path.cwd()

wlkpath = pathlib.Path(wdir)

all_links = []

for file_path in wlkpath.iterdir():

    if(file_path.suffix == ".pdf"):

        print(file_path.name)

        try:

            doc = pymupdf.open(file_path)

            for page in doc:

                links = page.get_links()


                if(len(links)>0):
                    print("Page",page.number,"\n")

                    for lnk in links:
                        
                        if(lnk["kind"] == 2):
                        
                            print("\t",lnk["uri"],"\n")
                            all_links.append(lnk["uri"])

            doc.close()

        except:
            print("Error")

if all_links:
    txtfile = input("Output filename (defaults to pdf_links.txt): ") or "pdf_links.txt"
    output_file = wdir / pathlib.Path(txtfile)
    output_file.write_text("\n".join(all_links), encoding="utf-8")
    print(f"\nSaved links to {output_file}")
else:
    print("\nNo links found.")


"""filename = input("Filename: ")

doc = pymupdf.open(filename)"""




