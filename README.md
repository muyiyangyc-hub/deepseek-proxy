# DeepSeek API Proxy

A lightweight proxy service that provides OpenAI‑compatible API endpoints for DeepSeek models, with built‑in usage tracking and cost calculation.

## Features

- **OpenAI‑compatible** – Use the same request format as OpenAI's `/v1/chat/completions`
- **Cost‑aware** – Automatically calculates USD cost for each request
- **Simple authentication** – Client‑side API key via `x-api-key` header
- **CORS enabled** – Ready for frontend integration

## Deployment to Vercel

1. **Install Vercel CLI** (optional):
   ```bash
   npm i -g vercel
   ```

2. **Deploy**:
   ```bash
   vercel
   ```
   Follow the prompts, or use the Vercel web dashboard.

3. **Set environment variable**:
   In your Vercel project settings → Environment Variables, add:
   ```
   DEEPSEEK_API_KEY = sk-your-deepseek-api-key-here
   ```

4. **Your API endpoint will be**:
   ```
   https://your-project.vercel.app/v1/chat/completions
   ```

## Local Development

```bash
# 1. Set your DeepSeek API key
set DEEPSEEK_API_KEY=sk-your-key-here

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the server
python -m uvicorn deepseek_proxy_api:app --reload --port 8000
```

## API Usage

### Request
```bash
curl -X POST https://your-api.vercel.app/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-client-key" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Hello!"}],
    "max_tokens": 100,
    "temperature": 0.7
  }'
```

### Response
```json
{
  "id": "chatcmpl-...",
  "object": "chat.completion",
  "created": 1234567890,
  "model": "deepseek-chat",
  "choices": [...],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 50,
    "total_tokens": 60,
    "cost_usd": 0.000055
  }
}
```

## Pricing (Example)

| Item               | Your Price | Your Cost | Margin |
|--------------------|------------|-----------|--------|
| Input tokens       | $0.5 / 1M  | ~ $0.2    | 150%   |
| Output tokens      | $1.0 / 1M  | ~ $0.2    | 400%   |

## RapidAPI Listing

Once deployed, list your API on [RapidAPI](https://rapidapi.com/hub) or [OpenRouter](https://openrouter.ai/):

- **Category**: AI & Machine Learning → Text Generation
- **Pricing**: Per‑token (input/output separate)
- **Documentation**: Use the interactive Swagger UI at `/docs`

## License

MIT