from typing import Dict, Any

from utils.pdf_loader import extract_text_from_pdf

def process_pdf(file_path) -> Dict[str, Any]:

    extracted_text = extract_text_from_pdf(file_path)

    return {
        "raw_text": extracted_text
    }
