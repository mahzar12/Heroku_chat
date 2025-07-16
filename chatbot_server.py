from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

# Load question-answer pairs from file
with open("qa_data.json", "r", encoding="utf-8") as f:
    qa_map = json.load(f)

# Serve static frontend files
app.mount("/", StaticFiles(directory="public", html=True), name="static")

# WebSocket endpoint for browser connection
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            message = await websocket.receive_text()
            reply = qa_map.get(message.lower().strip(), "Sorry, I didn’t understand that.")
            await websocket.send_text(json.dumps({"reply": reply}))
        except Exception as e:
            print(f"WebSocket error: {e}")
            break