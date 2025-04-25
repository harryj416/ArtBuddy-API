import requests
import json

# The API URL
API_URL = "https://art-buddy-api.vercel.app/api/vision"

# Use a public image URL
payload = {
    "image": "https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg",
    "prompt_number": 0  # Use the default prompt
}

# Call the API
print("Sending request to", API_URL)
response = requests.post(API_URL, json=payload)

# Print the response
print(f"Status code: {response.status_code}")
print("Response:")
print(json.dumps(response.json(), indent=2)) 