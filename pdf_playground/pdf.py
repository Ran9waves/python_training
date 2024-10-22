import PyPDF2

with open('./pdf_folder/insert_pdf_name_here.pdf', 'rb') as file:
    print(file)
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages) #tells us how many pages does the pdf has
    print(reader.getPage(1)) #show us a specific page, in this case, the second
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page) = PyPDF2.PdfFileWriter() 
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)


