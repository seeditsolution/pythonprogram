from pathlib import Path
from PyPDF2 import PdfFileReader

def text_from_pdf(pdf_path):
	
	pdf_reader = PdfFileReader(str(pdf_path))

	num_pages = pdf_reader.getNumPages()
	print(f"This PDF contains {num_pages} pages.")
	count = int(input("How many page do you want :"))
	
	text_of_pdf = []

	for i in range(count):
	
		first_page = pdf_reader.getPage(i)
		text = i+1, first_page.extractText() 
		text_of_pdf.append(text)
	
	return print(text_of_pdf)

pdf_path = input("Paste here path of pdf :")	
text_from_pdf(pdf_path)
