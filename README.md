# DeepSeek API Proxy

[![RapidAPI](https://img.shields.io/badge/RapidAPI-DeepSeek%20API%20Proxy-blue?logo=rapidapi)](https://rapidapi.com/muyiyangyc-hub/api/deepseek-api-proxy)
[![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black?logo=vercel)](https://deepseek-proxy-psi.vercel.app/v1/chat/completions)

A lightweight proxy service that provides **OpenAI-compatible** API endpoints for DeepSeek models, with built-in usage tracking and cost calculation.

> **90%+ cheaper** than GPT-4o. Same quality, pay only for what you use.

---

## Why Use This?

| Compared to GPT-4o | DeepSeek V3 (via this proxy) |
|---------------------|------------------------------|
| Price per request | **$0.004** |
| Input cost | $0.27/million tokens |
| Output cost | $1.10/million tokens |
| API format | OpenAI-compatible |
| Code changes needed | **None** |

---

## Quick Start

### Endpoint

POST https://deepseek-proxy-psi.vercel.app/v1/chat/completions


### Authentication

Pass your RapidAPI key in the header:

x-rapidapi-key: YOUR_RAPIDAPI_KEY


### cURL Example

```bash
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
90%+ cheaper than GPT-4o with comparable quality
Pay per use — No monthly commitment, billed per request
Built-in cost tracking — Every response includes usage.cost_usd
CORS enabled — Ready for frontend/browser integration
Serverless — Deployed on Vercel, scales automatically
Pricing (on RapidAPI)
Plan	Price	Details
BASIC (Free)	$0/month	100 requests/month — perfect for testing
PRO	$0.004/request	Pay per use, unlimited requests
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
