import pymupdf

import os

print("Extract Tables\n\n")

filename = input("Filename: ")

output_dir = f"output/{filename.split('.')[0]}"

os.makedirs(output_dir, exist_ok=True)

doc = pymupdf.open(filename)

tbl_strategy = input("Table strategy (“lines” / “lines_strict” / “text”): ") or None

table_count = 0

for page in doc:

    ft = page.find_tables(strategy=tbl_strategy)

    if(len(ft.tables)>0):

        for table in ft.tables:

            print(f"Table {table_count}: {len(table.extract())} rows, bbox: {table.bbox}")

            pix = page.get_pixmap(dpi=150, clip=table.bbox)

            pix.save(f"output/{filename}_table_{table_count}.png")
            
            table_count += 1



doc.close()

#print("Task complete")
