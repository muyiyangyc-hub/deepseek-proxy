DeepSeek API Proxy
RapidAPI
Vercel

A lightweight proxy service that provides OpenAI-compatible API endpoints for DeepSeek models, with built-in usage tracking and cost calculation.

70% cheaper than GPT-4o, same response quality, zero code changes.

Why Use This?
Compared to GPT-4o	DeepSeek V3 (via this proxy)
Input cost	$0.5/million tokens
Output cost	$1.0/million tokens
API format	OpenAI-compatible
Code changes needed	None
Quick Start
Endpoint
POST https://deepseek-proxy-psi.vercel.app/v1/chat/completions
Authentication
Pass your RapidAPI key in the header:

x-rapidapi-key: YOUR_RAPIDAPI_KEY
cURL Example
bash
复制
curl -X POST "https://deepseek-proxy-psi.vercel.app/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "x-rapidapi-key: YOUR_KEY" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Hello, how are you?"}]
  }'
Python Example
python
复制
import requests

url = "https://deepseek-proxy-psi.vercel.app/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "x-rapidapi-key": "YOUR_RAPIDAPI_KEY"
}
data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Explain quantum computing in 3 sentences."}]
}

response = requests.post(url, json=data, headers=headers)
print(response.json())
Features
OpenAI-compatible — Drop-in replacement for /v1/chat/completions
70% cheaper than GPT-4o with comparable quality
Built-in cost tracking — Every response includes usage.cost_usd
CORS enabled — Ready for frontend/browser integration
Serverless — Deployed on Vercel, scales automatically
Pricing (on RapidAPI)
Plan	Price	Requests/Month
BASIC (Free)	$0	3,000
PRO	$9.99	10,000
Get your API key here →

Self-Host
Deploy to Vercel
Fork this repo
Import to Vercel
Add environment variable: DEEPSEEK_API_KEY = your DeepSeek API key
Deploy
Local Development
bash
复制
pip install -r requirements.txt
python -m uvicorn deepseek_proxy_api:app --reload --port 8000
License
MIT
