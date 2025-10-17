import pymupdf

print("Quiz Maker\n")


doc = pymupdf.open()

y_offset = 100 

qheight = 200

doc.new_page()

pgno = 0

page = doc[pgno]

ocg_xref = doc.add_ocg("Answers",on=False)

page.insert_text(pymupdf.Point(300,50),"Quiz",fontsize=22)


def add_question():
    
    global y_offset
    global pgno
    global page
    global doc

    qtxt = input("Question text: ")

    page.insert_text(pymupdf.Point(50,y_offset),qtxt,fontsize=12)

    widget = pymupdf.Widget()

    widget.field_type = 4

    widget.field_name = f"question_{y_offset}"

    widget.rect = pymupdf.Rect(50,y_offset+20,page.rect.x1-50,y_offset+100)

    options = []

    cnt = int(input("Number of items? "))

    for opt in range(0,cnt):

                optxt = input("Option: ")
                options.append(optxt)

    widget.choice_values = options

    widget.text_fontsize = 12

    try:
            annot = page.add_widget(widget)
            print("xref:",widget.xref)

    except ValueError:
            print("ERROR: Could not add widget (page.add_widget(): Bad xref) #1")

    except:
            print("ERROR: Could not add widget") 


    anstxt = input("Answer:")

    page.insert_text(pymupdf.Point(50,y_offset+120),anstxt,fontsize=12,oc=ocg_xref)


    more = input("Add more questions? (y/n): ").strip().lower() == "y"

    if(more):
        
        y_offset += qheight

        if(y_offset + qheight > page.rect.y1):
            doc.new_page()
            pgno += 1
            page = doc[pgno]

        add_question()


add_question()



exported = input("Exported file: ")

doc.ez_save(exported)

doc.close()



