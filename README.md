# ArtBuddy-API

A simple API server that connects your ArtBuddy application to OpenAI's models. 

## Features

- Simple health check endpoint
- Chat endpoint that forwards messages to OpenAI's API
- Easy deployment on Vercel

See SIMPLIFIED_API.md for detailed usage instructions.

## Endpoints

- `GET /api/health` - Health check endpoint
- `POST /api/chat` - Echo endpoint that returns the same JSON with "GONE THROUGH VERCEL!" added

## Sample Request

```json
{
  "message": "Hello",
  "user_id": "ios_user"
}
```

## Sample Response

```json
{
  "message": "Hello",
  "user_id": "ios_user",
  "VERCEL_MESSAGE": "GONE THROUGH VERCEL!"
}
```

## How to Deploy

1. Push this repository to GitHub
2. Import to Vercel
3. Deploy

That's it!