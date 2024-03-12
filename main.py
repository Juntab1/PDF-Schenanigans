from pypdf import PdfReader, PdfWriter

read = PdfReader("dummy.pdf")
write_pdf = PdfWriter()

# this writes the one page in read
for page in read.pages:
    write_pdf.add_page(page)

# save for new PDF to a file
with open("new-dummy.pdf", "wb") as output:
    write_pdf.write(output)


