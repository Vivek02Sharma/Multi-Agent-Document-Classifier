import json

def process_json(data):
    try:
        parsed = json.loads(data)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON"}

    required_fields = ["id", "amount", "date"] # assuming these are the required fields
    missing = []
    
    for field in required_fields:
        if field not in parsed:
            missing.append(field)

    return {
        "normalized": parsed,
        "required_fields": required_fields,
        "missing_fields": missing
    }
