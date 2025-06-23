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
        field_name = widget.field_name  # Name of the form field
        field_value = widget.field_value  # Value entered in the field
        field_type = widget.field_type_string  # Type of the field (e.g., Text, CheckBox)
        
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


        elif(field_type == "CheckBox"):

            print("Fill field")

            #field_input = input("New value (On/Off): ")

            field_input = bool(input("New value (True/False): "))

            widget.field_value = field_input

            widget.update()



exported = input("Exported file: ")

doc.save(exported,deflate=True,garbage=3)

doc.close()



