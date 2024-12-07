

hdata = [

    [ "start.py", "Creates a one page pdf and inserts text in it" ],

    [ "pixmap.py", "Saves page as png image" ],

    [ "delete.py", "Delete page from pdf file" ],

    [ "merge.py", "Merge two pdf files" ],

    [ "move.py", "Move pages inside pdf document" ],

    [ "split.py", "Split a pdf document" ],

    [ "search.py", "Find a word in a document" ],

    [ "add-blank-page.py", "Insert empty page" ],

    [ "bgcolor.py", "Edit background color for one page" ],

    [ "bgcolor-all.py", "Edit background color for all pages" ],

]

print("\n\t","PyMuPDF Command Line Apps\n")

for line in hdata:
    print("\t",line[0],"\t",line[1],"\n")
