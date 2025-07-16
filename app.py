from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai_model import generate_response

# Initialize app
app = FastAPI()

# Allow frontend (like React, Vercel) to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define input structure
class Message(BaseModel):
    user_input: str

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "🧘‍♂️ Spiritual Avatar AI is running."}

# Chat endpoint
@app.post("/chat")
async def chat(msg: Message):
    response = generate_response(msg.user_input)
    return {"response": response}
