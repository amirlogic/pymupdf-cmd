# PyMuPDF-cmd

PyMuPDF command-line scripts

PyMuPDF must be installed

```help.py```            List all scripts

```insert-image.py```    Inserts image in a page

```start.py```           Creates an empty pdf document with one or more pages

```data.py```            Gets infos from a pdf file: Metadata, page count, images, tables and links 

```table.py```           Extract a table from a page

```to-pdf.py```          Convert to PDF


## Working with pages

```delete.py```          Delete page from pdf file 

```merge.py```           Merge two pdf files 

```move.py```            Move pages inside pdf document

```fcopy.py```           Duplicate a page

```split.py```           Split a pdf document

```add-blank-page.py```  Insert empty page


## Exporting

```pixmap.py```          Saves page as png image

```get-svg.py```         Export page to SVG

```html.py```            Export page to HTML


## Text

```search.py```          Find a word in a document

```htmlbox.py```         Insert text (supports HTML syntax)

```file-htmlbox.py```    Insert text from text or HTML file (supports HTML syntax, uses page.rect)

```file-htmlbox.py```    Insert text from text or HTML file (supports HTML syntax, uses page.rect)

```file-css-htmlbox.py```  Insert text from file (supports external CSS2 stylesheet)


## Images

```getimages.py``` & ```getimages-all.py```   Extract images to files

```xref-images.py```     Generates an HTML file containing the extracted images (from xref table)

```replace-image.py```   Replaces an image in a document (requires xref)

```remove-image.py```    Removes an image in a document (requires xref)


## Links

```get-links.py```       Extract links from a document

```text-link.py```       Turn text into link in a document

```insert-link.py```     Inserts a link in a document (requires a Rect object)


## Alter

```bgcolor.py``` & ```bgcolor-all.py```       Edit background color


## RAG-LLM

```llama.py```       Requires llama-index module
