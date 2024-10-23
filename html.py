import pymupdf

filename = input("Filename: ")

pgnum = input("Page: ")

doc = pymupdf.open(filename)


page = doc[int(pgnum)]

tpg = page.get_textpage()


doc.close()

html = tpg.extractHTML()

print(tpg.extractHTML())

HTML_BEFORE = "<!DOCTYPE html><html><head><title>HTML</title></head><body>"

HTML_AFTER = "</body></html>"

f = open(filename[:-4]+".html", "a")
f.write(HTML_BEFORE+html+HTML_AFTER)
f.close()
