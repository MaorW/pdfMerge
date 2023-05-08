from pypdf import PdfWriter

merged_location = "./merged-result/"
merger = PdfWriter()
# Here you should edit the PDFs names
pdf_files = ['pdf_files/pdf1.pdf', 'pdf_files/pdf2.pdf']

for pdf in pdf_files:
    merger.append(pdf)

merger.write(merged_location + "merged-pdf.pdf")
merger.close()