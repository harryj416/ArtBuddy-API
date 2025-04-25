import requests
import base64
import json
import sys
import os

def test_with_local_image(image_path, prompt="What can you tell me about this image?"):
    # The API URL
    API_URL = "https://art-buddy-api.vercel.app/api/vision"
    
    # Read and encode the image file
    try:
        with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"Error loading image: {e}")
        return
    
    # Prepare payload
    payload = {
        "image": image_data,
        "prompt": prompt
    }
    
    # Call the API
    print(f"Sending {os.path.basename(image_path)} to {API_URL}")
    response = requests.post(API_URL, json=payload)
    
    # Print the response
    print(f"Status code: {response.status_code}")
    print("Response:")
    print(json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    # Check if an image path was provided
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        
        # Check if a prompt was provided
        prompt = "What can you tell me about this image?"
        if len(sys.argv) > 2:
            prompt = sys.argv[2]
            
        test_with_local_image(image_path, prompt)
    else:
        print("Usage: python test_local_image.py <path_to_image> [optional_prompt]")
        print("Example: python test_local_image.py example.jpg \"What style is this artwork?\"") 