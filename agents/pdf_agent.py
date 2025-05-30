from typing import Dict, Any
from datetime import datetime
import uuid

from utils.pdf_loader import extract_text_from_pdf

def process_pdf(file_path) -> Dict[str, Any]:

    extracted_text = extract_text_from_pdf(file_path)

    return {
        "thread_id": str(uuid.uuid4()),
        "type": "PDF",
        "timestamp": datetime.now().isoformat(),
        "raw_text": extracted_text
    }

# print(datetime.now().isoformat())