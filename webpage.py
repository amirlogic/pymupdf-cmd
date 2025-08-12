
import pymupdf

import requests

url = input("Webpage URL: ")

r = requests.get(url)


#print("Result:", r.text)


story = pymupdf.Story(r.text)

outfile = input("Output file: ")

writer = pymupdf.DocumentWriter(outfile)

def rectfn(rect_num, filled):

    print("rect_num",rect_num,"filled",filled)

    width, height = pymupdf.paper_size("a4")

    margin = 20

    rect_w = width - 2*margin

    rect_h = height - 2*margin

    mediabox = pymupdf.Rect(0, 0, width, height)

    rect_x = margin

    rect_y = margin

    rect = pymupdf.Rect(rect_x, rect_y, rect_x + rect_w, rect_y + rect_h)

    return mediabox, rect, None
    

story.write(writer, rectfn)

writer.close()

print("Task completed")