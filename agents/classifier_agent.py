import os
from groq import Groq
from dotenv import load_dotenv

from agents.json_agent import process_json
from agents.email_agent import process_email
from agents.pdf_agent import process_pdf

load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

def classify_input(file, content):
    filename = file.filename.lower()
    
    if filename.endswith(".pdf"):
        format_type = "PDF"
        result = process_pdf(content)
    elif filename.endswith(".json"):
        format_type = "JSON"
        result = process_json(content)
    elif filename.endswith(".txt"):
        format_type = "Text"
        result = process_email(content)
    else:
        format_type = "Unknown"

    prompt = f"""You are an AI that classifies the intent of the following document.
            Input:
            {result}

            Classify the intent as one of the following categories:
            - Invoice
            - RFQ
            - Complaint
            - Regulation
            - Other

            Return only the intent as a single word, nothing else.
            """
    chat_completion = client.chat.completions.create(
        messages = [{"role": "user", "content": prompt}],
        model = "llama-3.3-70b-versatile",
    )

    reply = chat_completion.choices[0].message.content.strip()
    # print("reply:", reply)

    intent = None
    if "intent" in reply.lower():
        for line in reply.splitlines():
            if "intent" in line.lower():
                intent = line.split(":")[-1].strip()
                break
    elif len(reply.split()) == 1:
        intent = reply
    else:
        intent = reply.split()[-1]

    return format_type, intent, result
