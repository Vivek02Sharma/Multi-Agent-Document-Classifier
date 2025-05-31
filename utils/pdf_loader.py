from io import BytesIO
import fitz

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    with fitz.open(stream = BytesIO(pdf_bytes), filetype = "pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        # print(text)
    return text
