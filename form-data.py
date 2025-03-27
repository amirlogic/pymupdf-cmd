import pymupdf

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
        print(f"  Field Type: {field_type}")
        print()


doc.close()



