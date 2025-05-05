import pymupdf

print("Encrypt and Password protect a PDF")

encr_method = pymupdf.PDF_ENCRYPT_AES_256  # strongest encryption

doc = pymupdf.open(input("Source file: "))

owner_pw = input("Owner Password: ")

user_pw = input("User Password: ")

# define a bit field of user permissions:
perm = (pymupdf.PDF_PERM_ACCESSIBILITY  # always use this
        | pymupdf.PDF_PERM_PRINT  # permit printing
        | pymupdf.PDF_PERM_COPY  # permit copying
        | pymupdf.PDF_PERM_ANNOTATE  # permit adding annotations
)

output_pdf_path = input("Output file: ")

doc.save(output_pdf_path,
 owner_pw=owner_pw,  # set the owner password
 user_pw=user_pw,  # set the user password
 encryption=encr_method,  # set the encryption method
 permissions=perm,  # set the user permissions
)