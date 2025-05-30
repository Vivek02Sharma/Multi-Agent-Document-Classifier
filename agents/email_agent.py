import re

def process_email(email_bytes):
    try:
        email = email_bytes.decode("utf-8")
    except Exception as e:
        raise f"error : {e}"

    sender_match = re.search(r"From:\s*(.*)", email)
    urgency = "High" if "urgent" in email.lower() else "Normal"
    
    email_lower = email.lower()
    if "invoice" in email_lower:
        intent = "Invoice"
    elif "quote" in email_lower or "quotation" in email_lower:
        intent = "RFQ"
    elif "complaint" in email_lower or "not satisfied" in email_lower or "issue" in email_lower:
        intent = "Complaint"
    elif "regulation" in email_lower or "compliance" in email_lower or "policy" in email_lower:
        intent = "Regulation"
    else:
        intent = "Inquiry"

    return {
        "sender": sender_match.group(1) if sender_match else "Unknown",
        "intent": intent,
        "urgency": urgency,
        "content": email
    }
