# Multi-Agent Document Classifier
This project is a multi-agent AI system that classifies and processes documents in PDF, JSON, or Email (text) format. It uses LLMs for intelligent classification, Redis for shared memory, and a Streamlit frontend for user interaction.

## Features
- Detects document format (PDF, JSON, Text)

- Classifies intent: Invoice, RFQ, Complaint, Regulation, Other

- Routes input to specialized agents (Email, PDF, JSON)

- Uses Groq LLM API for classification and field extraction

- Stores results in Redis with thread ID traceability

- User-friendly Streamlit frontend

- Works with uploaded files or pasted email content

## Folder Structure
```
.
├── agents/
│   ├── classifier_agent.py       
│   ├── email_agent.py         
│   ├── json_agent.py             
│   └── pdf_agent.py            
│
├── front-end/
│   └── app.py                  
│
├── memory/
│   └── memory.py                
│
├── utils/
│   └── pdf_loader.py        
│
├── Test-Files/
│   ├── email.txt
│   ├── new.pdf                 
│   └── customer.json             
│
├── docker-compose.yml
│
├── main.py                     
├── requirements.txt              
├── README.md                  
```

## Sample Inputs
Located in the Test-Files/ folder:

- `email.txt`: A sample email

- `customer.json`: A structured invoice

- `new.pdf`: A pdf sample

## Set Environment Variable
Create a .env file in the root with:
```
GROQ_API_KEY=your_groq_api_key_here
```

## How to Run

1. Install Dependencies
   ```
   pip install -r requirements.txt
   ```
2. Start Redis Server
   ```
   redis-server
   ```
3. Run FastAPI Backend
   ```
   uvicorn main:app --reload
   ```
4. Run Streamlit Frontend
   ```
   streamlit run front-end/app.py
   ```

   **OR**

- Run docker compose ( make sure to set environment variable )
   ```
   docker compose up
   ```
- Go to local url
   ```
   http://localhost:8501
   ```

