import pymupdf

print("\nSave for Fast Web Access\n")

try:
        doc = pymupdf.open(input("Source document: "))

        if doc.is_fast_webaccess:

                print("Document already linear!")

        else:

                newfile = input("New filename: ")

                doc.save(newfile, linear=True)

                doc.close()

except:
        print("Error!")