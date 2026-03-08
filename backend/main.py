from fastapi import FastAPI
from pydantic import BaseModel
from backend.websocket_server import router as ws_router

app = FastAPI(title="Real-Time Multilingual Voice AI Agent")

# Include WebSocket router
app.include_router(ws_router)

# Request body model
class Message(BaseModel):
    message: str

# Health check
@app.get("/")
def health():
    return {"status": "Voice AI Agent Running"}

# HTTP endpoint for voice_input.py
@app.post("/process")
def process_message(msg: Message):
    user_message = msg.message
    
    # Simple AI agent response
    response = f"AI Agent received: {user_message}"
    
    return {
        "input": user_message,
        "response": response
    }
