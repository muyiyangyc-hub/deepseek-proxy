import os
import time
import requests
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"

app = FastAPI(title="DeepSeek Proxy", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "service": "DeepSeek API Proxy"}

@app.post("/v1/chat/completions")
async def chat(body: dict, x_api_key: str = Header(...)):
    if not DEEPSEEK_API_KEY:
        raise HTTPException(500, "Server not configured: DEEPSEEK_API_KEY missing")

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": body.get("model", "deepseek-chat"),
        "messages": body.get("messages", []),
        "max_tokens": body.get("max_tokens", 1024),
        "temperature": body.get("temperature", 0.7),
        "stream": False
    }

    try:
        resp = requests.post(DEEPSEEK_URL, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        result = resp.json()
        usage = result.get("usage", {})
        pt = usage.get("prompt_tokens", 0)
        ct = usage.get("completion_tokens", 0)
        result["usage"]["cost_usd"] = round(pt / 1_000_000 * 0.5 + ct / 1_000_000 * 1.0, 6)
        return result
    except requests.exceptions.RequestException as e:
        raise HTTPException(500, f"DeepSeek call failed: {str(e)}")