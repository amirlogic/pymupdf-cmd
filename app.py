
def main():

    print("\nPyMuPDF Command Line App")

    print("\n\n","Pages","\n")

    print("\tmerge - split")

    print("\tmove - delete - fcopy")

    print("\n\n","Embed files","\n")

    print("\n\n","Text","\n")

    print("\tsearch")

    print("\thtmlbox")

    print("\n\n","Images","\n")

    print("\tpixmap - getimages")

    print("\n\n","Security","\n")

    print("\tencrypt - decrypt")


    goto = input("\nFunction: ")

    print("\n")

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

    elif(goto == "delete"):

        import delete

    elif(goto == "fcopy"):

        import fcopy

    elif(goto == "encrypt"):

        import encrypt

    elif(goto == "decrypt"):

        import decrypt

    elif(goto == "getimages"):

        import getimages

    elif(goto == "split"):

        import split


    more = input("Continue? (y/n): ")

    if(more.strip().lower() == "y"):

        main()

    else:

        print("Exiting...")


if __name__ == "__main__":

    main()