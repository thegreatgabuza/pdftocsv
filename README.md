# PDF to CSV Converter

A simple Flask web application that converts PDF files into structured CSV files. This tool extracts text content from PDF files and organizes it into a tabular format.

## Features

- Web-based interface for PDF file upload
- Converts PDF text content to CSV format
- Automatic download of converted CSV files
- Supports files up to 16MB
- Simple and intuitive user interface

## Requirements

- Python 3.x
- Flask
- pdfplumber
- pandas
- Werkzeug

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
pdf-to-csv-converter/
├── app.py              # Main Flask application
├── requirements.txt    # Project dependencies
├── README.md          # Project documentation
├── uploads/           # Directory for uploaded files
└── templates/
    └── upload.html    # HTML template for the upload page
```

## Usage

1. Start the application:
```bash
python app.py
```
2. Open your web browser and navigate to `http://localhost:8000`
3. Upload a PDF file using the web interface
4. The converted CSV file will automatically download once processing is complete

## Limitations

- Currently handles basic text-based PDFs
- May need adjustments for PDFs with complex layouts or tables
- Maximum file size is 16MB

## Customization

The PDF to CSV conversion can be customized by modifying the `pdf_to_csv` function in `app.py`. The current implementation:
- Extracts text from each page
- Splits text into lines
- Converts lines into columns

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the MIT License.
