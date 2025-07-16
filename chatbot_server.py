from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

# Allow frontend JS to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load question-answer pairs from file
with open("qa_data.json", "r", encoding="utf-8") as f:
    qa_map = json.load(f)

# Serve static HTML/CSS/JS from 'public' folder
app.mount("/", StaticFiles(directory="public", html=True), name="static")

# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            message = await websocket.receive_text()
            print(f"Received: {message}")
            reply = qa_map.get(message.lower().strip(), "Sorry, I didn’t understand that.")
            await websocket.send_text(json.dumps({"reply": reply}))
        except Exception as e:
            await websocket.send_text(json.dumps({"reply": "Oops! Server error."}))
            print(f"WebSocket error: {e}")
            break
