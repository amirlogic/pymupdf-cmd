
import pathlib

import pymupdf

import csv


print("Convert all tables to csv")


wdir = input("Directory (defaults to CWD): ")

if(wdir == ""):

    wdir = pathlib.Path.cwd()

wlkpath = pathlib.Path(wdir)

all_tables = []

for file_path in wlkpath.iterdir():

    if(file_path.suffix == ".pdf"):

        print(file_path.name)

        try:

            doc = pymupdf.open(file_path)

            for page in doc:

                ft = page.find_tables()

                if(len(ft.tables)>0):

                    for tindx,tbl in enumerate(ft):

                        if(tbl.row_count>1 and tbl.col_count>2):

                            print("Writing CSV...")

                            with open(f'{file_path}_{tindx}.csv', 'w', newline='') as csvfile:

                                tblwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)

                                if(tbl.header.external):
                                    tblwriter.writerow(tbl.header.names)

                                for row in tbl.extract():

                                    #print(row)
                                    
                                    tblwriter.writerow(row)

            doc.close()

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

print("\nTask completed.")






