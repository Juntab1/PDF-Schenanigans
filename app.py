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

      # Ensure the 'uploads' directory exists
      if not os.path.exists(app.config['UPLOAD_FOLDER']):
          os.makedirs(app.config['UPLOAD_FOLDER'])
      # make sure app.config['UPLOAD_FOLDER'] exists, if not make it a dir
          
      # specify new filename
      new_file_name = "new_" + filename
    
      # Save the uploaded file with the new filename
      new_file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_file_name)
      # hint os join
    
      # Return the uploaded file with the new filename as an attachment for download
      return send_file(new_file_path, as_attachment=True)
    

    #   filename = secure_filename(f.filename)
    #   file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    #   f.save(file_path)
      
    #   updated_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'updated' + filename)
    #   read = PdfReader(file_path)
    #   main.write_pages(write_pdf, read)
    #   main.new_pdf(write_pdf, file_path, updated_file_path)
    #   return send_file(updated_file_path, as_attachment=True)
   
    # tommorow try to make code into comments and figure out how to program it yourself

if __name__ == "__main__":
    app.run(debug=True)