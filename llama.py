#import pymupdf
import pymupdf4llm

filename = input("Filename: ")

#doc = pymupdf.open(filename)


llama_reader = pymupdf4llm.LlamaMarkdownReader()
llama_docs = llama_reader.load_data(filename)




#doc.move_page(pgnum, mvto)
#doc.save(f"mv-{pgnum}-{mvto}{filename}")

import pathlib
pathlib.Path("llama-output.md").write_bytes(llama_docs.encode())

#doc.close()

print("Task complete")

#doc.save("doc-with-new-blank-page.pdf")