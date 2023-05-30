import os
from flask import Flask, request, jsonify
from pdf2docx import Converter

app = Flask(__name__)

# Route to handle the PDF to DOCX conversion
@app.route('/convert', methods=['POST'])
def convert_to_docx():
    pdf_file = request.files['file']

    # Generate the output file path with .docx extension
    filename = os.path.splitext(pdf_file.filename)[0]
    docx_file_path = os.path.join("output", filename + ".docx")

    # Perform the conversion
    cv = Converter()
    cv.from_file(pdf_file)
    cv.to_file(docx_file_path)
    cv.close()

    # Generate the file URL
    server_address = request.host_url.rstrip('/')
    file_url = f"{server_address}/{docx_file_path}"

    return jsonify({'file_url': file_url})

if __name__ == '__main__':

    os.makedirs('output', exist_ok=True)

    app.run(debug=True)
