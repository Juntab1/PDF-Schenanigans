import os
from flask import Flask, render_template, request, send_file
from pypdf import PdfReader, PdfWriter
from werkzeug.utils import secure_filename
import pdf
from os import remove

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

# use SQLAlchamy to keep track of path names to be able to use it here
# without having to create global variables
@app.after_request
def remove_temp_pdf(response):
    if (os.path.exists(curr_path))
    os.remove(curr_path)
    os.remove(new_file_path)
    return response

# app.route with get and post
@app.route('/', methods = ['POST'])
def upload_file():
   # if statement make sure it is post
    if  request.method == 'POST':
      
      # use request to get filename
      f = request.files['user_file']

      # empty filename check, return comment
      if f.filename == '':
        return "no file"
      
      # make sure the file is secure
      filename = secure_filename(f.filename)

      # specify new filename
      new_file_name = "new_" + filename

      # Ensure the 'uploads' directory exists
      if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
      # make sure app.config['UPLOAD_FOLDER'] exists, if not make it a dir
      curr_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      # Save the uploaded file with the new filename
      new_file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_file_name)
      
      f.save(curr_path)

      write_pdf = PdfWriter()
      read = PdfReader(curr_path)

      if request.form.get('Encrypt'):
        pdf.encrypt_pdf(write_pdf)

      if request.form.get('Decrypt'):
        pdf.decrypt_given_pdf(read, "password")

      if request.form.get('Text_extract'):
        read = pdf.extract_text_pdf(read)

      pdf.write_pages(write_pdf, read)

      pdf.new_pdf(write_pdf, new_file_path)

      # Need to return response to maintain exectuion of normal response
      # before getting to this after request
      @app.after_request
      def remove_temp_pdf(response):
         os.remove(curr_path)
         os.remove(new_file_path)
         return response
         
      # Return the uploaded file with the new filename as an attachment for download
      return send_file(new_file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)



# TODO:
    # Make if statements to check cases such as a file that is not encrypted is passed
    # as a file to decrypt