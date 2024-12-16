import pymupdf


def exportPage(doc,pgno):

    page = doc[pgno]

    pix = page.get_pixmap(dpi=150)

    exported = input("Exported image (add .png):")

    pix.save(exported)   # "page-%i.png" % page.number

    print("pixmap saved")

    morepages = input("Do more pages? (y/n) ")

    if(morepages == "y" or morepages == "Y"):
        return True
    else:
        return False


def enterPage(doc):

    pgnum = input("Page: ")

    pgnum = int(pgnum)

    res = exportPage(doc,pgnum)

    if(res == True):
        enterPage()


def enterDocument():

    print("Please input the target file: ")

    filename = input("Filename: ")

    doc = pymupdf.open(filename) 

    enterPage(doc)

    doc.close()

    moredocs = input("Do more documents? (y/n) ")

    if(moredocs == "y" or moredocs == "Y"):
        enterDocument()
    else:
        print("Task completed")


enterDocument()