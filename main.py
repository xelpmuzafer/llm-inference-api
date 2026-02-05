"""
LLM Inference API — FastAPI server for chat and completion endpoints.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="LLM Inference API", version="0.1.0")


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    model: str = "default"
    messages: list[ChatMessage]
    max_tokens: Optional[int] = 1024
    temperature: Optional[float] = 0.7


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    return {"ready": True}


@app.post("/v1/chat/completions")
def chat_completions(req: ChatRequest):
    """OpenAI-compatible chat completions (stub). Wire to your model backend."""
    return {
        "id": "gen-1",
        "object": "chat.completion",
        "choices": [
            {
                "message": {"role": "assistant", "content": "Hello from LLM Inference API. Replace with your model."},
                "finish_reason": "stop",
            }
        ],
    }


@app.post("/v1/completions")
def completions(req: dict):
    """Text completion (stub)."""
    return {"choices": [{"text": "Completion stub. Wire to your model.", "finish_reason": "stop"}]}
