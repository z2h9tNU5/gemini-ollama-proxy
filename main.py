import os
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

# Gemini API 初期化
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-3-flash-preview")
model = genai.GenerativeModel(MODEL_NAME)

app = FastAPI()


# --- OpenAI互換リクエスト ---
class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    model: str | None = None
    messages: list[Message]


@app.post("/v1/chat/completions")
async def chat(req: ChatRequest):
    # OpenAI形式 → Gemini形式へ変換
    prompt = "\n".join(
        f"{m.role}: {m.content}" for m in req.messages
    )

    response = model.generate_content(prompt)

    # OpenAI互換レスポンス
    return {
        "id": "chatcmpl-gemini",
        "object": "chat.completion",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": response.text,
                },
                "finish_reason": "stop",
            }
        ],
    }
