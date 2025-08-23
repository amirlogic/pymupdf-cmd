import pymupdf


filename = input("Filename: ")

pgnum = input("Page index: ")

tblindx = input("Table index: ")

pgnum = int(pgnum)
tblindx = int(tblindx)

doc = pymupdf.open(filename)

page = doc[pgnum]

ft = page.find_tables()

if(len(ft.tables)>0):

    table = ft.tables[tblindx]

    if(table.header.external):
        print(table.header.names)

    for row in table.extract():
        print(row)

else:
    print("No table found on this page")


doc.close()

#print("Task complete")
