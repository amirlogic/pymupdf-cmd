import pymupdf

import session

import datetime


print("Insert TOC")

filename = input("Filename: ")

doc = pymupdf.open(filename) 

#instext = input('Text: ')


def tocItem():

    print("Insert TOC item:")

    lvl = int(input('Level (starts at 1): '))

    title = input("Title: ")

    pgnum = int(input("Page (1-based) :"))

    last = input("Last one? (y/n) ")

    if(last == "y" or last == "Y"):
        last = True
    else:
        last = False

    return ([lvl,title,pgnum,None],last)


tocdata = []


def tocExtend():

    newitem = tocItem()

    tocdata.append(newitem[0])

    if(newitem[1] == False):
        tocExtend()


tocExtend()

ins = doc.set_toc(tocdata)

newfile = input("New file: ")

doc.save(newfile)


print("TOC inserted",ins)

doc.close()

session.add([datetime.datetime.now(),'set_toc',ins,filename,newfile])
