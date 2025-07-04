
import pymupdf

import session

import datetime


print("Text Search")

filename = input("Filename: ")

doc = pymupdf.open(filename)

def findIt():

    needle = input("Search for: ")

    total = 0

    for index, page in enumerate(doc):

        res = page.search_for(needle)
        
        print("page #",index," ",len(res)," match found")

        for found in res:
            print(res)
            total += 1

    print("\n")

    more = input("Find more strings? (y/n): ")

    if(more.strip().lower() == "y"):

        findIt()


findIt()

session.add([datetime.datetime.now(),'search_text',filename])

doc.close()

print("Task complete")