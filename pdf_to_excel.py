from PyPDF2 import PdfFileWriter, PdfFileReader
import tabula


inputpdf = PdfFileReader(open("pdf_link", "rb"))
print(inputpdf.numPages)
i = 110

output = PdfFileWriter()
output.addPage(inputpdf.getPage(i + 1))
with open("document-page%s.pdf" % str(i + 1), "wb") as outputStream:
    output.write(outputStream)


df = "pdf_link/document-page%s.pdf" % (i + 1)
output = "output_link/test%s.csv" % (i)
tabula.convert_into(df, output, output_format="csv", lattice = False,  stream = True, guess = True)





