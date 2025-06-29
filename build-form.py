
import pymupdf

print("Build a Form\n")


doc = pymupdf.open()

doc.new_page()

page = doc[0]

more = True

next_y0 = 80

field_x0 = 150

wnum = 0

while(more):

    print("""\tTEXT         7\n
            BUTTON       1\n
            CHECKBOX     2\n
            COMBOBOX     3\n
            LISTBOX      4\n
            RADIOBUTTON  5\n
            SIGNATURE    6\n""")

    wtype = input("Widget type: ")

    widget = pymupdf.Widget()

    widget.field_type = int(wtype)

    wtxt = input("Field text: ")

    page.insert_text(pymupdf.Point(50,next_y0+60),wtxt)

    # Text
    if(wtype == "7"):

        widget.rect = pymupdf.Rect(field_x0,next_y0+50,300,next_y0+65)

        widget.field_name = f"textfield-{wnum}"


    # Radio
    elif(wtype == "5"):

        #widget.field_type = 1

        widget.rect = pymupdf.Rect(field_x0,next_y0+50,field_x0+15,next_y0+65)

        widget.field_name = f"radiofield-{wnum}"
        


        #widget.field_value = "test"

        #widget.text_font = "ZaDb"

        #widget.text_fontsize = 0

        widget.field_flags = pymupdf.PDF_BTN_FIELD_IS_RADIO


    # Button
    elif(wtype == "1"):

        widget.rect = pymupdf.Rect(field_x0,next_y0+50,field_x0+100,next_y0+65)

        widget.field_name = f"button-{wnum}"

        widget.border_color = pymupdf.pdfcolor['blue']

        widget.text_fontsize = 12

        widget.button_caption = "Test"

        widget.script = 'app.alert("Hello From PDF!")'


    # ListBox
    elif(wtype == "4"):

        cnt = int(input("Number of items? "))

        options = []

        for opt in range(0,cnt):

            optxt = input("Option: ")
            options.append(optxt)

        widget.choice_values = options

        widget.rect = pymupdf.Rect(field_x0,next_y0+50,300,next_y0+100)



        widget.field_name = f"listbox-{wnum}"

        widget.text_fontsize = 12

       
    # CheckBox
    elif(wtype == "2"):

        widget.rect = pymupdf.Rect(field_x0,next_y0+50,field_x0+10,next_y0+60)

        widget.field_name = f"checkbox-{wnum}"

        widget.text_font = "ZaDb"

        widget.text_fontsize = 0


    try:
        annot = page.add_widget(widget)
        print("xref:",widget.xref)

    except ValueError:
        print("ERROR: Could not add widget (page.add_widget(): Bad xref)")

    except:
        print("ERROR: Could not add widget")

    wnum += 1

    moreprompt = input("More? (y/n): ").strip().lower()

    if(moreprompt == "y"):

        more = True

    else:

        more = False

    next_y0 += 40


print("\nFill the Form\n")

# Iterate through each page
for page_num in range(len(doc)):
    page = doc[page_num]
    print(f"Page {page_num + 1}:")

    # Get all widgets (form fields) on the page
    widgets = page.widgets()
    if not widgets:
        print("  No form fields found on this page.")
        continue

    # Iterate through each widget and extract data
    for widget in widgets:
        field_name = widget.field_name  
        field_value = widget.field_value  
        field_type = widget.field_type_string  
        
        print(f"  Field Name: {field_name}")
        print(f"  Field Value: {field_value}")
        print(f"  Field Type: {field_type}\n")
        

        if(field_type == "Text"):

            print("Fill field")

            field_input = input("Field data: ")

            widget.field_value = field_input

            widget.update()


        elif(field_type == "ListBox"):

            print(widget.choice_values)

            print("\n")

            field_input = int(input(f"New value: (0-{len(widget.choice_values)-1}) "))

            widget.field_value = widget.choice_values[field_input]

            widget.update()

            print("New field value: ",widget.field_value)


        elif(field_type == "CheckBox"):

            print("Fill field")

            #field_input = input("New value (On/Off): ")

            field_input = bool(input("New value (True/False): "))

            widget.field_value = field_input

            widget.update()



exported = input("Exported file: ")

doc.save(exported,deflate=True,incremental=False,clean=True)

doc.close()



