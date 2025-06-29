import pymupdf

print("Fill Form\n")

filename = input("Filename: ")


doc = pymupdf.open(filename)

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


flq = "n" #input("Flatten form? (y/n): ")

if(flq.strip().lower() == "y"):

    print("Flattening...")

    for page_num in range(len(doc)):

        page = doc[page_num]
        widgets = page.widgets()

        for widget in widgets:
            widget.fill()
            page.delete_widget(widget) 

exported = input("Exported file: ")

doc.save(exported,deflate=True,incremental=False,clean=True)

doc.close()



