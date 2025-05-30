import redis
import json
from datetime import datetime
import uuid

r = redis.Redis(host = "localhost", port = 6379, db = 0, decode_responses = True)

def store_context(source, format_type, intent, result):
    thread_id = str(uuid.uuid4())
    
    context = {
        "source": source,
        "format": format_type,
        "intent": intent,
        "timestamp": datetime.now().isoformat(),
        "result": result
    }

    r.set(f"context:{thread_id}", json.dumps(context))

    return thread_id

def get_context(thread_id):
    data = r.get(f"context:{thread_id}")
    if data:
        return json.loads(data)
    return None
