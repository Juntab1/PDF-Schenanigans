from pypdf import PdfReader, PdfWriter

# Write the provided pdf to be able to 
# do functions such as encrypt
def write_pages(write_pdf, read):
    for page in read.pages:
        write_pdf.add_page(page)

# Creates a new pdf to be returned
def new_pdf(write_pdf):
    with open("decrypted-dummy.pdf", "wb") as output:
        write_pdf.write(output)

# This function encrypts a pdf with a password
def encrypt_pdf(write_pdf):
    # AES-256: gov adopted symmetric-key encryption algorithm
    write_pdf.encrypt("password", algorithm="AES-256")

# This function decrypts a encrypted pdf provided by the user
def decrypt_given_pdf(read, password):
    if read.is_encrypted:
        read.decrypt(password)

def main():
    read = PdfReader("dummy.pdf")
    write_pdf = PdfWriter()

    write_pages(write_pdf, read)
    new_pdf(write_pdf)

if __name__ == "__main__":
    main()


