import os  # This lets us access environment variables and system functions
from flask import Flask, request, jsonify  # Flask is the web framework that handles HTTP requests
from openai import OpenAI  # This is the library that allows us to talk to OpenAI's AI models
from dotenv import load_dotenv  # This loads our secret keys from a file so we don't have to hardcode them

# Load secret keys and settings from the .env file
# Think of this like opening a locked drawer to get our private keys
load_dotenv()

# Get our OpenAI API key (like a special password) from environment variables
api_key = os.getenv("OPENAI_API_KEY")
# If we can't find the API key, stop everything and show an error
if not api_key:
    raise ValueError("Missing OPENAI_API_KEY environment variable")

# Set up our connection to OpenAI's AI service using our API key
client = OpenAI(api_key=api_key)
# Choose which AI model to use, either from our settings or use a default one
DEFAULT_MODEL = os.getenv("MODEL", "gpt-4o-mini-2024-07-18")

# Create our web application using Flask
app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health_check():
    """This is a simple endpoint that just tells us if the API is running.
    It's like checking if the lights are on before entering a room."""
    return jsonify({"status": "healthy", "message": "API is running"})

@app.route('/api/chat', methods=['POST'])
def chat():
    """This is the main endpoint that handles chat messages.
    
    When a user sends a message:
    1. We receive the message
    2. We send it to OpenAI's AI
    3. We get the AI's response
    4. We send the response back to the user
    
    It's like being a messenger between the user and the AI.
    """
    # Get the data that was sent to us (in JSON format)
    # JSON is just a structured way to send data, like a digital envelope with information inside
    data = request.json
    
    # Make sure we actually received some data
    if not data:
        # If not, return an error message
        return jsonify({"error": "No JSON data received"}), 400
    
    # Check if the data contains a 'message' field, which is what we need
    user_message = data.get('message')
    if not user_message:
        # If there's no message, return an error
        return jsonify({"error": "No 'message' field in request"}), 400
    
    try:
        # Now let's talk to the AI!
        # We're sending the user's message to OpenAI and asking for a response
        response = client.chat.completions.create(
            model=DEFAULT_MODEL,  # Which AI model to use
            messages=[
                {"role": "user", "content": user_message}  # The message from our user
            ],
            max_tokens=500  # Limit the response length so it doesn't go on forever
        )
        
        # Extract the AI's response text from the data we got back
        ai_message = response.choices[0].message.content
        
        # Add the AI's response to our original data
        # This way, we return both the original message and the AI's reply
        data["ai_response"] = ai_message
        
    except Exception as e:
        # If anything goes wrong (like network issues or API errors)
        # We catch the error and include it in our response
        data["error"] = str(e)
    
    # Add a tag to show this went through our Vercel server
    # This is like adding our stamp to the envelope before sending it back
    data["VERCEL_MESSAGE"] = "GONE THROUGH VERCEL!"
    
    # Return the enhanced data back to whoever called our API
    return jsonify(data)

# This is a catch-all route that handles all other URLs
# If someone goes to a URL we don't specifically handle above,
# they'll get this friendly message instead
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({"message": "Welcome to Lock-In-Buddy API", "path": path})

# This code only runs if we're starting the application directly
# (not if it's being imported by another file)
# Think of this as the "if you're running this program directly, do this" section
if __name__ == '__main__':
    # Start the web server in debug mode (which shows helpful error messages)
    app.run(debug=True) 