from pypdf import PdfReader, PdfWriter
from flask import Flask
from reportlab.pdfgen import canvas
from os import remove

read = PdfReader()

# Write the provided pdf to be able to 
# do functions such as encrypt
def write_pages(write_pdf, read):
    for page in read.pages:
        write_pdf.add_page(page)

# Creates a new pdf to be returned
def new_pdf(write_pdf, new_user_file, delete_file = None):
    with open(new_user_file, "wb") as output:
        write_pdf.write(output)
    if (delete_file != None):
        remove(delete_file)

# This function encrypts a pdf with a password
def encrypt_pdf(write_pdf):
    # AES-256: gov adopted symmetric-key encryption algorithm
    write_pdf.encrypt("password", algorithm="AES-256")

# This function decrypts a encrypted pdf provided by the user
def decrypt_given_pdf(read, password):
    if read.is_encrypted:
        read.decrypt(password)

# This function extracts text without excess vertical whitespace and preserving 
# horizontal positioning. Reads all pages passed in.
# Return new pdf that contains the text extracted.
def extract_text_pdf(read):
    extracted_text = ""
    for page in read.pages:
        extracted_text += page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False) + " "
    return create_pdf_from_str(extracted_text)
    

# helper method to add text object to new pdf
def create_pdf_from_str(text):
    new_page = canvas.Canvas("temp.pdf", pagesize=(595.27, 841.89)) # A4 pagesize
    new_page.drawString(50, 780, text)
    new_page.showPage()
    new_page.save()
    return PdfReader("temp.pdf")







