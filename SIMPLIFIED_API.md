# ArtBuddy-API

This document explains how to use the ArtBuddy API in simple terms. Think of this API as a messenger that takes your message, sends it to an AI, and brings back the AI's response.

## What is an API?

An API (Application Programming Interface) is like a waiter in a restaurant:
- You (the app) tell the waiter (the API) what you want
- The waiter goes to the kitchen (the AI service) to get what you ordered
- The waiter brings back your order (the AI response)

## Available Services (Endpoints)

### Health Check

**What it does**: Tells you if the API service is up and running.

**How to use it**: Send a GET request to `/api/health`

**What you'll get back**:
```json
{
  "status": "healthy", 
  "message": "API is running"
}
```

### Chat with AI

**What it does**: Takes your message, sends it to the AI, and returns the AI's response.

**How to use it**: Send a POST request to `/api/chat` with this information:
```json
{
  "message": "Your message to the assistant",
  "user_id": "optional_user_identifier"
}
```

* `message`: This is your question or statement (required)
* `user_id`: This is optional - you can use it to identify different users

**What you'll get back**:
```json
{
  "message": "Your message to the assistant",
  "user_id": "optional_user_identifier",
  "ai_response": "The AI's answer to your message",
  "VERCEL_MESSAGE": "GONE THROUGH VERCEL!"
}
```

* `ai_response`: This is what the AI replied with
* If something goes wrong, you'll get an `error` message explaining what happened

## Setting Up Your Own Copy

1. **Get the code**: Clone (copy) the repository to your computer
2. **Set up your secret key**: Create a file named `.env` with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   MODEL=gpt-4o-mini-2024-07-18
   ```
3. **Install the tools**: Run `pip install -r requirements.txt` to install all required software
4. **Start the service**: Run `python api/index.py` to start the API on your computer

## Putting it Online (Deployment)

To make this available on the internet using Vercel:

1. Connect your GitHub repository to Vercel
2. Add these secret environment variables in Vercel:
   - `OPENAI_API_KEY`: Your OpenAI API key (required)
   - `MODEL`: Which AI model to use (optional, defaults to gpt-4o-mini-2024-07-18)
3. Deploy your application

Now anyone on the internet can use your API! 