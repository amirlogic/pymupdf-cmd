
import pymupdf

import pathlib

print("\nSearch PDF Documents in a Directory\n")

wdir = input("Directory (defaults to CWD): ")

if(wdir == ""):

    wdir = pathlib.Path.cwd()

wlkpath = pathlib.Path(wdir)

def findIt():

    needle = input("Search for: ")

    total = 0

    for file_path in wlkpath.iterdir():

        if(file_path.suffix == ".pdf"):

            print(file_path.name)

            try:

                doc = pymupdf.open(file_path)

                for index,page in enumerate(doc):

                    res = page.search_for(needle)

                    if(len(res) > 0):
                        print("\tpage #",index,":",len(res),"match(es) found")
                        total += len(res)


                doc.close()

                print("\n")
            
            except:
                print("Error")

    print("\nTotal matches: ",total,"\n")

    more = input("Find more strings? (y/n): ").strip().lower() == "y"

    if(more):

        findIt()


findIt()