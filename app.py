


if __name__ == "__main__":

    print("PyMuPDF Command Line App")

    print("\n\n","Pages","\n")

    print("\tmerge")

    print("\tmove")

    print("\n\n","Embed files","\n")

    print("\n\n","Text","\n")

    print("\tsearch")

    print("\thtmlbox")

    print("\n\n","Images","\n")

    print("\tpixmap")

    goto = input("Function#: ")

    if(goto == "htmlbox"):

        import htmlbox

    elif(goto == "merge"):

        import merge

    elif(goto == "move"):

        import move

    elif(goto == "pixmap"):

        import pixmap

    elif(goto == "search"):

        import search