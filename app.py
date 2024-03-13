import os
from flask import Flask, render_template, request, send_file
from pypdf import PdfReader, PdfWriter
from werkzeug.utils import secure_filename
import main

app = Flask(__name__)

write_pdf = PdfWriter()

app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['user_file']
      if f.filename == '':
          return "Select a file"
      # Generate a new filename
      filename = secure_filename(f.filename)
      new_filename = 'new_' + filename

      # Ensure the 'uploads' directory exists
      if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
      # Save the uploaded file with the new filename
      file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
      f.save(file_path)
    
      # Return the uploaded file with the new filename as an attachment for download
      return send_file(file_path, as_attachment=True)
    #   filename = secure_filename(f.filename)
    #   file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    #   f.save(file_path)
      
    #   updated_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'updated' + filename)
    #   read = PdfReader(file_path)
    #   main.write_pages(write_pdf, read)
    #   main.new_pdf(write_pdf, file_path, updated_file_path)
    #   return send_file(updated_file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)