import PyPDF2
import sys

inputs = sys.argv[1:] #this will grab all the arguments besides the first on

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger() #this will merge all the pdfs in one
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf') #all merged pdfs will be saved in this file.

pdf_combiner(inputs)