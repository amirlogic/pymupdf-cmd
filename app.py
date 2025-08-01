
def main():

    print("\nPyMuPDF Command Line App")

    print("\n\n","Infos:\t\t|","\ttoc","\tdata","\ttable")

    print("\n\n","Pages:\t\t|","\tmerge","\tsplit", "\tmove", "\tdelete", "\tfcopy")

    print("\n\n","Ext. files:\t|","\tattach")

    print("\n\n","Text:\t\t|","\tsearch", "\thtmlbox")

    print("\n\n","Images:\t|","\tpixmap", "\tgetimages", "\tdelimages")

    print("\n\n","Transform:\t|","\tdiaportrait", "\tbgcolor")

    print("\n\n","Security:\t|","\tencrypt", "\tdecrypt", "\tscrub")

    print("\n")

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

    elif(goto == "scrub"):

        import scrub

    elif(goto == "attach"):

        import attach

    elif(goto == "toc"):

        import toc

    elif(goto == "data"):

        import data

    elif(goto == "table"):

        import table

    elif(goto == "start"):

        import start

    elif(goto == "diaportrait"):

        import diaportrait

    elif(goto == "bgcolor"):

        import bgcolor

    elif(goto == "delimages"):

        import delimages


    more = input("Continue? (y/n): ")

    if(more.strip().lower() == "y"):

        main()

    else:

        print("Exiting...")


if __name__ == "__main__":

    main()