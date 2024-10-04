import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

# Example usage:
if __name__ == "__main__":
    pdf_path = "data/input/sample.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)
