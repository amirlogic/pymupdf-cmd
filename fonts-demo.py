
import pymupdf

print("Font Demo - Requires pymupdf-fonts")

doc = pymupdf.open()

doc.new_page()

page = doc[0]


figo = pymupdf.Font("figo")

page.insert_font(fontname="figo", fontbuffer=figo.buffer)

page.insert_text(pymupdf.Point(50,50), "This text is in figo", fontname="figo")


notos = pymupdf.Font("notos")

page.insert_font(fontname="notos", fontbuffer=notos.buffer)

page.insert_text(pymupdf.Point(50,70), "This text is in notos", fontname="notos")


ubuntu = pymupdf.Font("ubuntu")

page.insert_font(fontname="ubuntu", fontbuffer=ubuntu.buffer)

page.insert_text(pymupdf.Point(50,90), "This text is in ubuntu", fontname="ubuntu")


spacemo = pymupdf.Font("spacemo")

page.insert_font(fontname="spacemo", fontbuffer=spacemo.buffer)

page.insert_text(pymupdf.Point(50,110), "This text is in spacemo", fontname="spacemo")


# FiraGO Bold
figbo = pymupdf.Font("figbo")
page.insert_font(fontname="figbo", fontbuffer=figbo.buffer)
page.insert_text(pymupdf.Point(50,130), "This text is in figbo", fontname="figbo")

# FiraGO Italic
figit = pymupdf.Font("figit")
page.insert_font(fontname="figit", fontbuffer=figit.buffer)
page.insert_text(pymupdf.Point(50,150), "This text is in figit", fontname="figit")

# FiraGO BoldItalic
figbi = pymupdf.Font("figbi")
page.insert_font(fontname="figbi", fontbuffer=figbi.buffer)
page.insert_text(pymupdf.Point(50,170), "This text is in figbi", fontname="figbi")

# FiraMono Regular
fimo = pymupdf.Font("fimo")
page.insert_font(fontname="fimo", fontbuffer=fimo.buffer)
page.insert_text(pymupdf.Point(50,190), "This text is in fimo", fontname="fimo")

# FiraMono Bold
fimbo = pymupdf.Font("fimbo")
page.insert_font(fontname="fimbo", fontbuffer=fimbo.buffer)
page.insert_text(pymupdf.Point(50,210), "This text is in fimbo", fontname="fimbo")

# SpaceMono Bold
spacembo = pymupdf.Font("spacembo")
page.insert_font(fontname="spacembo", fontbuffer=spacembo.buffer)
page.insert_text(pymupdf.Point(50,230), "This text is in spacembo", fontname="spacembo")

# SpaceMono Italic
spacemit = pymupdf.Font("spacemit")
page.insert_font(fontname="spacemit", fontbuffer=spacemit.buffer)
page.insert_text(pymupdf.Point(50,250), "This text is in spacemit", fontname="spacemit")

# SpaceMono BoldItalic
spacembi = pymupdf.Font("spacembi")
page.insert_font(fontname="spacembi", fontbuffer=spacembi.buffer)
page.insert_text(pymupdf.Point(50,270), "This text is in spacembi", fontname="spacembi")

# Noto Sans Math
math = pymupdf.Font("math")
page.insert_font(fontname="math", fontbuffer=math.buffer)
page.insert_text(pymupdf.Point(50,290), "This text is in math", fontname="math")

# Noto Music
music = pymupdf.Font("music")
page.insert_font(fontname="music", fontbuffer=music.buffer)
page.insert_text(pymupdf.Point(50,310), "This text is in music", fontname="music")

# Noto Sans Symbols (Regular)
symbol1 = pymupdf.Font("symbol1")
page.insert_font(fontname="symbol1", fontbuffer=symbol1.buffer)
page.insert_text(pymupdf.Point(50,330), "This text is in symbol1", fontname="symbol1")

# Noto Sans Symbols2
symbol2 = pymupdf.Font("symbol2")
page.insert_font(fontname="symbol2", fontbuffer=symbol2.buffer)
page.insert_text(pymupdf.Point(50,350), "This text is in symbol2", fontname="symbol2")

# Noto Sans Regular (you already did “notos” – but there are the Bold/Italic variants too:)
# Noto Sans Italic
notosbi = pymupdf.Font("notosbi")
page.insert_font(fontname="notosbi", fontbuffer=notosbi.buffer)
page.insert_text(pymupdf.Point(50,370), "This text is in notosbi", fontname="notosbi")

# Noto Sans Bold
notosbo = pymupdf.Font("notosbo")
page.insert_font(fontname="notosbo", fontbuffer=notosbo.buffer)
page.insert_text(pymupdf.Point(50,390), "This text is in notosbo", fontname="notosbo")

# Noto Sans BoldItalic
notosbi2 = pymupdf.Font("notosbi")  # note: same code as italic? table shows "notosbi" for Bold Italic too
page.insert_font(fontname="notosbi2", fontbuffer=notosbi2.buffer)
page.insert_text(pymupdf.Point(50,410), "This text is in notosbi (bold/italic)", fontname="notosbi2")

# Ubuntu Regular (you already did “ubuntu”) – the other ubuntu variants:
# Ubuntu Bold
ubuntubo = pymupdf.Font("ubuntubo")
page.insert_font(fontname="ubuntubo", fontbuffer=ubuntubo.buffer)
page.insert_text(pymupdf.Point(50,430), "This text is in ubuntubo", fontname="ubuntubo")

# Ubuntu Bold Italic
ubuntubi = pymupdf.Font("ubuntubi")
page.insert_font(fontname="ubuntubi", fontbuffer=ubuntubi.buffer)
page.insert_text(pymupdf.Point(50,450), "This text is in ubuntubi", fontname="ubuntubi")

# Ubuntu Italic
ubuntuit = pymupdf.Font("ubuntuit")
page.insert_font(fontname="ubuntuit", fontbuffer=ubuntuit.buffer)
page.insert_text(pymupdf.Point(50,470), "This text is in ubuntuit", fontname="ubuntuit")

# Ubuntu Mono Regular
ubuntm = pymupdf.Font("ubuntm")
page.insert_font(fontname="ubuntm", fontbuffer=ubuntm.buffer)
page.insert_text(pymupdf.Point(50,490), "This text is in ubuntm", fontname="ubuntm")

doc.new_page()

page = doc[1]

# Ubuntu Mono Bold
ubuntmbo = pymupdf.Font("ubuntmbo")
page.insert_font(fontname="ubuntmbo", fontbuffer=ubuntmbo.buffer)
page.insert_text(pymupdf.Point(50,50), "This text is in ubuntmbo", fontname="ubuntmbo")

# Ubuntu Mono Bold Italic
ubuntmbi = pymupdf.Font("ubuntmbi")
page.insert_font(fontname="ubuntmbi", fontbuffer=ubuntmbi.buffer)
page.insert_text(pymupdf.Point(50,70), "This text is in ubuntmbi", fontname="ubuntmbi")

# Ubuntu Mono Italic
ubuntmit = pymupdf.Font("ubuntmit")
page.insert_font(fontname="ubuntmit", fontbuffer=ubuntmit.buffer)
page.insert_text(pymupdf.Point(50,90), "This text is in ubuntmit", fontname="ubuntmit")

# Cascadia Mono Regular
cascadia = pymupdf.Font("cascadia")
page.insert_font(fontname="cascadia", fontbuffer=cascadia.buffer)
page.insert_text(pymupdf.Point(50,110), "This text is in cascadia", fontname="cascadia")

# Cascadia Mono Bold
cascadiab = pymupdf.Font("cascadiab")
page.insert_font(fontname="cascadiab", fontbuffer=cascadiab.buffer)
page.insert_text(pymupdf.Point(50,130), "This text is in cascadiab", fontname="cascadiab")

# Cascadia Mono Italic
# cascadiiai = pymupdf.Font("cascadiiai")
# page.insert_font(fontname="cascadiiai", fontbuffer=cascadiiai.buffer)
# page.insert_text(pymupdf.Point(50,150), "This text is in cascadiiai", fontname="cascadiiai")

# Cascadia Mono BoldItalic
cascadiabi = pymupdf.Font("cascadiabi")
page.insert_font(fontname="cascadiabi", fontbuffer=cascadiabi.buffer)
page.insert_text(pymupdf.Point(50,170), "This text is in cascadiabi", fontname="cascadiabi")


doc.save("output/fonts-demo.pdf")

doc.close()

