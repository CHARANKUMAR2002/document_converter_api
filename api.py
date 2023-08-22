from flask import Flask, request, send_file
from pdf2docx import parse
from docx2pdf import convert
app = Flask(__name__)

@app.route('/convert_pdf', methods=['POST'])

def convert_pdf():
    file = request.files['pdf']
    file.save('input.pdf')

    parse(str('input.pdf'), str('output.docx'))

    return send_file(str(f'output.docx'),)

@app.route('/convert_docx', methods=['POST'])

def convert_docx():
    file = request.files['docx']
    file.save('input.docx')

    convert(str('input.docx'), str('output.pdf'))

    return send_file(str('output.pdf'))


if __name__ == "__main__":
    app.run(debug=True, port=4000)