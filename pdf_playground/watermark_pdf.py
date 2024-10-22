import PyPDF2
import sys

template = PyPDF2.PdfFileReader(open('pdf_you_want_to_watermark.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('water_mark.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i) #since we don't know how many pages does the pdf file has, we use range
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    
    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)

