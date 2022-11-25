import PyPDF2

file_name = 'pdf_test.pdf'
path = "C:\\Users\\elias\\PycharmProjects\\file-read-automation\downloads\\"


pdf_file = open(f'{path}{file_name}', 'rb')
pdf_data = PyPDF2.PdfFileReader(pdf_file)
pdf_page = pdf_data.getPage(0)
text = pdf_page.extractText()

if text == 'TESTING PDF':
    print('Certificado válido')



