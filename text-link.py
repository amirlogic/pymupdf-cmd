
import pymupdf

import session

import datetime


print("Turn Text into Link")

filename = input("Filename: ")

needle = input("Search for: ")

doc = pymupdf.open(filename)

total = 0

for index, page in enumerate(doc):

    #txtpg = page.get_textpage()
    #res = txtpg.search(needle)

    res = page.search_for(needle)
    
    print("page #",index," ",len(res)," match found")
    for found in res:
        print(found)
        #for fr in found:
        ans = input("Make link? (y/n): ")
        if(ans == "y" or ans=="Y"):
            print("Turning into link...")
            print("0: LINK_NONE")
            print("1: LINK_GOTO")
            print("2: LINK_URI")
            print("3: LINK_LAUNCH")
            print("4: LINK_NAMED")
            print("5: LINK_GOTOR")
            lnktype = int(input("Link type (0-5): "))

            if(lnktype == 0):
                print("not supported")

            elif(lnktype == 1):
                print("GOTO")
                dpg = int(input("Destination page: "))
                linkdict = {"kind":lnktype,"page":dpg, "from":found}

            elif(lnktype == 2):
                print("Internet uri")
                uri = input("URI: ")
                linkdict = {"kind":lnktype,"uri":uri, "from":found}

            else:
                print("not supported")
                
            #print(fr)
            page.insert_link(linkdict)
            total += 1

        #print(res)

if(total > 0):
    newfile = input("New file: ")

    doc.save(newfile)

    session.add([datetime.datetime.now(),'text_to_link',filename,needle,total,newfile])

doc.close()

print("Task complete")