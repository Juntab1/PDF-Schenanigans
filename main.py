from pypdf import PdfReader, PdfWriter

def write_pages(write_pdf, read):
    for page in read.pages:
        write_pdf.add_page(page)

def new_pdf(write_pdf):
    with open("new-dummy.pdf", "wb") as output:
        write_pdf.write(output)


def main():
    read = PdfReader("dummy.pdf")
    write_pdf = PdfWriter()

    write_pages(write_pdf, read)
    new_pdf(write_pdf)

if __name__ == "__main__":
    main()

# look at the documentation and maybe work on encrypting next that would be fun


