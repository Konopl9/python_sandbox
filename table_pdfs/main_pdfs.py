import pypdf

pdfFile = open('My resume.pdf', 'rb')
reader = pypdf.PdfReader(pdfFile)
print(len(reader.pages))
page = reader.pages[0]
print(page.extract_text())
pdfFile.close()

# Merge 2 PDFs
pdfFile1 = open('My resume.pdf', 'rb')
pdfFile2 = open('My resume copy.pdf', 'rb')

reader1 = pypdf.PdfReader(pdfFile1)
reader2 = pypdf.PdfReader(pdfFile2)

writter = pypdf.PdfWriter()
for page in reader1.pages:
    writter.add_page(page)
for page in reader2.pages:
    writter.add_page(page)

outPutfile = open('Merged PDF.pdf', 'wb')
writter.write(outPutfile)
outPutfile.close()
pdfFile1.close()
pdfFile2.close()