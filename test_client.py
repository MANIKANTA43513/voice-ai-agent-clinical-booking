import asyncio
import websockets

async def test():
    uri = "ws://127.0.0.1:8000/ws/voice"

    async with websockets.connect(uri) as websocket:
        message = "நாளை மருத்துவரை பார்க்க வேண்டும்"
        await websocket.send(message)

        response = await websocket.recv()

        print("Server Response:")
        print(response)

asyncio.run(test())