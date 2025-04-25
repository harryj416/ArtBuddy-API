import requests
import json

# The API URL
API_URL = "https://art-buddy-api.vercel.app/api/vision"

# Use a public image URL
payload = {
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Vincent_van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1280px-Vincent_van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg",
    "prompt": "What can you tell me about this famous artwork?"
}

# Call the API
print("Sending request to", API_URL)
response = requests.post(API_URL, json=payload)

# Print the response
print(f"Status code: {response.status_code}")
print("Response:")
print(json.dumps(response.json(), indent=2)) 