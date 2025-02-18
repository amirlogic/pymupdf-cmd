
import pymupdf

from deep_translator import GoogleTranslator

 # Define color "white"
WHITE = pymupdf.pdfcolor["white"]

 # This flag ensures that text will be dehyphenated after extraction.
textflags = pymupdf.TEXT_DEHYPHENATE

filename = input("Filename: ")

srclang = input("Source Language: ")

newlang = input("New Language: ")

 # Configure the desired translator
to_lang = GoogleTranslator(source=srclang, target=newlang)


 # Open the document
doc = pymupdf.open(filename)

 # Define an Optional Content layer in the document named "Korean".
 # Activate it by default.
ocg_xref = doc.add_ocg("Translated", on=True)

print("Processing...")
 # Iterate over all pages
for page in doc:
     # Extract text grouped like lines in a paragraph.
    blocks = page.get_text("blocks", flags=textflags)

     # Every block of text is contained in a rectangle ("bbox")
    for block in blocks:
        bbox = block[:4]  # area containing the text
        original = block[4]  # the text of this block

         # Invoke the actual translation to deliver us a Korean string
        translated = to_lang.translate(original)

         # Cover the English text with a white rectangle.
        page.draw_rect(bbox, color=None, fill=WHITE, oc=ocg_xref)

         # Write the Korean text into the rectangle37         
          
        try:
            page.insert_htmlbox(bbox, translated, oc=ocg_xref)
            
        except:
            print("htmlbox error")

exported = input("New filename: ")

print("Saving...")

doc.save(exported,garbage=0,deflate=True)