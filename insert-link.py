import pymupdf

print("Insert link")

filename = input("Filename: ")

doc = pymupdf.open(filename) 

pgnum = int(input("Page: "))

page = doc[pgnum]

print("0: LINK_NONE")
print("1: LINK_GOTO")
print("2: LINK_URI")
print("3: LINK_LAUNCH")
print("4: LINK_NAMED")
print("5: LINK_GOTOR")

kind = int(input("Kind: (0-5) "))

if(kind == 0):
    print("not supported")

elif(kind == 1):
    print("not supported")

elif(kind == 2):
    print("Internet uri")
    uri = input("URI: ")
    linkdict = {"kind":kind,"uri":uri}



page.insert_link(linkdict)
    
""" if(len(links)>0):
        print("page",page.number,"\n")
        pprint.pp(page.get_links())
        lnkcount += 1
        print("\n") """



print("Link inserted")

doc.close()


