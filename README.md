# ArtBuddy-API

A simple API server that connects your ArtBuddy application to OpenAI's models. 

## Features

- Simple health check endpoint
- Chat endpoint that forwards messages to OpenAI's API
- Vision endpoint that analyzes images with OpenAI's vision models
- Easy deployment on Vercel

See SIMPLIFIED_API.md for detailed usage instructions.

## Endpoints

- `GET /api/health` - Health check endpoint
- `POST /api/chat` - Chat endpoint that sends text to OpenAI and returns AI responses
- `POST /api/vision` - Vision endpoint that accepts base64-encoded images and returns AI analysis

## Sample Chat Request

```json
{
  "message": "Hello",
  "user_id": "ios_user"
}
```

## Sample Vision Request

```json
{
  "image": "base64_encoded_image_data_here",
  "prompt": "What can you tell me about this artwork?"
}
```

## Sample Response

```json
{
  "prompt": "What can you tell me about this artwork?",
  "ai_response": "This appears to be an abstract painting with vibrant colors...",
  "VERCEL_MESSAGE": "GONE THROUGH VERCEL!"
}
```

## How to Deploy

1. Push this repository to GitHub
2. Import to Vercel
3. Add environment variables:
   - `OPENAI_API_KEY` (required)
   - `MODEL` (optional, default: gpt-4o-mini-2024-07-18)
   - `VISION_MODEL` (optional, default: gpt-4o)
4. Deploy

That's it!