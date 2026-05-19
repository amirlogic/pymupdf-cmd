
import pymupdf4llm

from pathlib import Path

def doRapOCR(img):
    from rapidocr import RapidOCR

    engine = RapidOCR()

    result, _ = engine(img)

    ocr_output = []
    for line in result:
        box, text, conf = line
        # Convert polygon -> bounding box
        x_coords = [p[0] for p in box]
        y_coords = [p[1] for p in box]
        bbox = [min(x_coords), min(y_coords), max(x_coords), max(y_coords)]

        ocr_output.append((bbox, text, conf))

    return ocr_output

def mdImages():

    pass

def main():

    print("\n\tPyMuPDF4LLM Command Line App\n")

    print("\n\n","Whole file(s) to MD:\t\t|","\tfilemd","\tdirmd","\tnohdft",)

    print("\n\n","To MD with Images:\t\t|","\tfilemdi","\tfilemdi64",)

    print("\n\n","Force OCR:\t\t|","\tfullocr",)

    print("\n\n","Table strategy:\t\t|",)

    #print("\n\n","Images:\t\t|",)

    #print("\n\n","Forms:\t|",)

    #print("\n\n","Transform:\t|",)

    #print("\n\n","Export:\t|",)

    print("\n\n","Multiple parameters:\t\t|","\tcombine", )

    print("\n")

    goto = input("\nFunction: ")

    print("\n")

    if(goto == "filemd"):

        print("Single File to Markdown\n")

        filename = input("Filename: ")
        md = pymupdf4llm.to_markdown(filename,show_progress=True)
        #print("Processing...")

        if input("Write MD file? (y/n): ").lower() == "y":
            output_path = Path(filename).with_suffix(".md")
            output_path.write_text(md, encoding="utf-8")
            print(f"Wrote markdown to: {output_path}")
        else:
            print("\n", md, "\n")


    elif(goto == "dirmd"):

        print("Directory to Markdown\n")

        wdir = input("Directory (defaults to CWD): ") or Path.cwd()

        wlkpath = Path(wdir)

        for file_path in wlkpath.iterdir():

            if(file_path.suffix == ".pdf"):

                print(file_path.name)

                try:

                    md = pymupdf4llm.to_markdown(file_path,show_progress=True)

                    

                except:

                    print("Error")

        print("All files have been processed")

    elif(goto == "nohdft"):

        print("Single File to Markdown (Header and Footer Removed)\n")

        filename = input("Filename: ")
        md = pymupdf4llm.to_markdown(filename, header=False, footer=False, show_progress=True)
        #print("Processing...")

        if input("Write MD file? (y/n): ").lower() == "y":
            output_path = Path(filename).with_suffix(".md")
            output_path.write_text(md, encoding="utf-8")
            print(f"Wrote markdown to: {output_path}")
        else:
            print("\n", md, "\n")
    

    elif(goto == "filemdi"):

        print("Single File to Markdown (Images included in folder)\n")

        filename = input("Filename: ")
        img_path = Path(filename).parent or Path.cwd()
        mdi = pymupdf4llm.to_markdown(filename,show_progress=True,write_images=True,image_path=img_path)

        if input("Write MD file? (y/n): ").lower() == "y":
            output_path = Path(filename).with_suffix(".md")
            output_path.write_text(mdi, encoding="utf-8")
            print(f"Wrote markdown to: {output_path}")
        else:
            print("\n", mdi, "\n")


    elif(goto == "filemdi64"):

        print("Single File to Markdown (Images included in file as base64)\n")

        filename = input("Filename: ")
        mdi = pymupdf4llm.to_markdown(filename,show_progress=True,embed_images=True)

        output_path = Path(filename).with_suffix(".md")
        output_path.write_text(mdi, encoding="utf-8")
        print(f"Wrote markdown to: {output_path}")



    elif(goto == "fullocr"):

        pass

        print("Single File to Markdown (Force OCR)\n")

        #from rapidocr import RapidOCR

        filename = input("Filename: ")
        md = pymupdf4llm.to_markdown(filename,show_progress=True,ocr_function=doRapOCR,force_ocr=True)    #force_ocr=True, ,ocr_function=doRapOCR
        # ocr_function needs to be provided



    elif(goto == "quit" or goto == "exit"):

        print("Exiting...")
        quit()


    more = input("Continue? (y/n): ")

    if(more.strip().lower() == "y"):

        main()

    else:

        print("Exiting...")


if __name__ == "__main__":

    main()