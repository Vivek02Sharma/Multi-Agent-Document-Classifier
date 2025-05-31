from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import UploadFile, File

from agents.classifier_agent import classify_input

app = FastAPI()

@app.post("/process")
async def process_input(file: UploadFile = File(...)):
    content = await file.read()
    format_type, intent, result, thread_id = classify_input(file, content)

    return JSONResponse(
        status_code = 200,
        content = {
            "format": format_type,
            "intent": intent,
            "content": result,
            "thread_id": thread_id
        }
    )
