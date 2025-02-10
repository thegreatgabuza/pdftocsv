from flask import Flask, render_template, request, send_file
import pdfplumber
import pandas as pd
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def pdf_to_csv(pdf_path, csv_path):
    data = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extract text and tables from the page
            text = page.extract_text()
            if text:
                # Split text into lines and process each line
                lines = text.split('\n')
                for line in lines:
                    # Split line into columns (adjust this based on your PDF structure)
                    columns = line.split()
                    if columns:
                        data.append(columns)
    
    # Convert to DataFrame and save as CSV
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            csv_filename = f"{filename.rsplit('.', 1)[0]}.csv"
            csv_path = os.path.join(app.config['UPLOAD_FOLDER'], csv_filename)
            
            # Save the uploaded PDF
            file.save(pdf_path)
            
            # Convert PDF to CSV
            pdf_to_csv(pdf_path, csv_path)
            
            # Return the CSV file
            return send_file(csv_path, as_attachment=True)
        
        return 'Invalid file type'
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000) 