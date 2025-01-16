
import sys

hdata = [

    [ "start.py", "Creates a one page pdf and inserts text in it*" ],

    [ "pixmap.py", "Saves page as png image" ],

    [ "delete.py", "Delete page from pdf file" ],

    [ "merge.py", "Merge two pdf files" ],

    [ "move.py", "Move pages inside pdf document" ],

    [ "split.py", "Split a pdf document" ],

    [ "search.py", "Find a word in a document" ],

    [ "get-links.py", "Extract links from a document" ],

    [ "text-link.py", "Turn text into link in a document" ],

    [ "insert-link.py", "Inserts a link in a document (requires a Rect object)*" ],

    [ "embfile.py", "Embed a file in a document*" ],

    [ "embfile-multi.py", "Embed multiple files in a document" ],

    [ "bgcolor.py", "Edit background color for one page" ],

    [ "bgcolor-all.py", "Edit background color for all pages" ],

]

print("\n\tPyMuPDF Command Line Apps\n")

if(len(sys.argv)>1):
    if(sys.argv[1] == "start"):
        print("\tCreates a new PDF file\n")

    elif(sys.argv[1] == "insert-link"):
        print("\tinsert-link\n")
        print("\tSupported links: LINK_GOTO (1) and LINK_URI (2)\n")

    elif(sys.argv[1] == "embfile"):
        print("\tembfile - Embed a file\n")
        print("\tembfile \n")
    else:
        print("\tUnknown script\n")
        
else:

    for line in hdata:
        print("\t",line[0],"\t",line[1],"\n")
