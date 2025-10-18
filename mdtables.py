
import pymupdf


def mdsave(res, output):

    import pathlib

    pathlib.Path(output).write_bytes(res.encode())


filename = input("Filename: ")

doc = pymupdf.open(filename)

hzlst = input("Horizontal strategies (lines/lines_strict/text, default lines): ").strip().lower()

verst = input("Vertical strategies (lines/lines_strict/text, default lines): ").strip().lower()

if(not hzlst):
    hzlst = "lines"

if(not verst):
    verst = "lines"

for page in doc:

    ft = page.find_tables(horizontal_strategy=hzlst, vertical_strategy=verst)

    if(len(ft.tables)>0):

        for index,table in enumerate(ft.tables):

            print("Page #", page.number, "Table #", index)

            if(table.header.external):
                print(table.header.names)

            for row in table.extract():
                print(row)

            tomd = input("Convert to markdown (y/n): ").strip().lower() == 'y'

            if(tomd):
                res = table.to_markdown()

                output = input("Output filename: ")

                if(output.strip()):
                    mdsave(res, output)
                else:
                    print(res)


doc.close()