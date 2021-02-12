# Rupali Wadhwani
# Program to merge PDFs
import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    # Now that you have copied all the pages in all the documents, write them into the a new document

    merger.write('super.pdf')


pdf_combiner(inputs)
