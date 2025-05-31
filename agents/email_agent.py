import re

def process_email(email_bytes):
    try:
        email = email_bytes.decode("utf-8")
    except Exception as e:
        raise f"error : {e}"

    sender_match = re.search(r"From:\s*(.*)", email)
    urgency = "High" if "urgent" in email.lower() else "Normal"
    
    return {
        "sender": sender_match.group(1) if sender_match else "Unknown",
        "urgency": urgency,
        "content": email
    }
