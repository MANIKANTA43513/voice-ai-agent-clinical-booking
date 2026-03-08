
from fastapi import APIRouter, WebSocket
from backend.conversation import process_text

router = APIRouter()

@router.websocket("/ws/voice")
async def voice_socket(ws: WebSocket):
    await ws.accept()

    while True:
        data = await ws.receive_text()

        result = process_text(data)

        await ws.send_json(result)
