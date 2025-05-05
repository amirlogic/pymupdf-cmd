import pymupdf

print("\nDecrypt a PDF\n")

try:
        doc = pymupdf.open(input("Source document: "))

        if doc.needs_pass:  # we need the owner password!

                owner_pw = input("Enter owner password:")

                rc = doc.authenticate(owner_pw)  # authenticate with the password string
                
                if rc not in (1, 4, 6):  # authorization levels including ownership
                        
                        raise Exception("Bad owner password.")

                # you now have full (owner) document access
                # save a decrypted version of the document

                encr_method = pymupdf.PDF_ENCRYPT_NONE  # option for removing encryption

                newfile = input("New filename: ")

                doc.save(newfile, encryption=encr_method)

                doc.close()
        
        else:
                print("Document not encrypted!")

except:
        print("Error!")