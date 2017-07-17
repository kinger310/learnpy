import PyPDF2

pdf_obj = open(r'D:\360Downloads\zhongshiyou.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
print(pdf_reader.numPages)
page_obj = pdf_reader.getPage(0)
page_obj.extractText()
