# ********************------------------- Working with PDF Files
import PyPDF2

# *-*-*-*-*-*-*-*-* Reading and writing PDF files
# with open("flexbox.pdf", "rb") as file:
#     reader = PyPDF2.PdfFileReader(file)

#     print(reader.numPages)

#     page = reader.getPage(10)

#     page.rotateClockwise(180)

#     writer = PyPDF2.PdfFileWriter()

#     writer.addPage(page)

#     with open("flexboxV2.pdf", "wb") as result:
#         writer.write(result)


# *-*-*-*-*-*-*-*-* Merging PDF files
merger = PyPDF2.PdfFileMerger()
pdf_files = ["flexbox.pdf", "grid.pdf"]

for pdf_file in pdf_files:
    merger.append(pdf_file)

merger.write("Flex-Grid-Guide.pdf")
