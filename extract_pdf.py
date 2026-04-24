import sys
import PyPDF2

try:
    reader = PyPDF2.PdfReader('Catálogo - Explovale..pdf')
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    with open("pdf_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Success. Extracted to pdf_text.txt")
except Exception as e:
    print("Error:", e)
