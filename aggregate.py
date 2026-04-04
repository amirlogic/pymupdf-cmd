
import pymupdf

from pathlib import Path

print("Search text then aggregate pages with match(es)")

wdir = Path(input("Directory: ")) or Path.cwd()

out = pymupdf.open()

needle = input("Needle: ")

total = 0

# Next screen

for file_path in wdir.iterdir():

    if file_path.suffix.lower() == ".pdf":

        print(file_path.name)

        with pymupdf.open(file_path) as doc:

            # Next screen

            for index,page in enumerate(doc):

                res = page.search_for(needle, quads=True)

                if(len(res) > 0):

                    # Next screen

                    print("\tpage #",index,":",
                          len(res),"match(es) found")
                    
                    page.add_highlight_annot(res)

                    out.insert_pdf(doc, 
                                   from_page = index, 
                                   to_page = index)
                    total += 1

                    #for r in res:
                        #pass

# Next Screen

if total > 0:

    xfname = input("Output file:")

    output_file = wdir / xfname

    out.save(output_file)

    out.close()
    
    print(f"\nSaved PDF to: {output_file}")

else:
    print("\nNo match found.")