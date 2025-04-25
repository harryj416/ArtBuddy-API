import requests
import base64
import json
import sys
import os
from PIL import Image
import io

def simulate_mobile_upload(image_path, prompt_number=1):
    """
    Simulates an iOS app uploading a photo from camera roll:
    1. Reads the image file
    2. Resizes it to a typical mobile photo size if needed
    3. Converts to JPEG format (common for mobile uploads)
    4. Encodes as base64
    5. Sends to API
    """
    API_URL = "https://art-buddy-api.vercel.app/api/vision"
    
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Resize if very large (simulating iOS processing)
        max_dimension = 1200  # Typical size for mobile uploads
        if max(img.size) > max_dimension:
            # Calculate new dimensions while maintaining aspect ratio
            width, height = img.size
            if width > height:
                new_width = max_dimension
                new_height = int(height * (max_dimension / width))
            else:
                new_height = max_dimension
                new_width = int(width * (max_dimension / height))
            
            img = img.resize((new_width, new_height), Image.LANCZOS)
            print(f"Resized image to {new_width}x{new_height}")
        
        # Convert to JPEG format (common for mobile uploads)
        if img.format != 'JPEG':
            print(f"Converting from {img.format if img.format else 'unknown'} to JPEG")
            buffer = io.BytesIO()
            img.convert('RGB').save(buffer, format='JPEG', quality=85)
            buffer.seek(0)
            image_bytes = buffer.read()
        else:
            # Re-open the file if it's already JPEG
            with open(image_path, 'rb') as f:
                image_bytes = f.read()
        
        # Encode as base64 (how mobile apps typically send image data)
        base64_data = base64.b64encode(image_bytes).decode('utf-8')
        
        # Create payload that mimics iOS app
        payload = {
            "image": base64_data,
            "prompt_number": prompt_number,
            "metadata": {
                "source": "mobile_camera",
                "device": "iOS_simulator",
                "format": "jpeg"
            }
        }
        
        # Log upload size
        size_kb = len(base64_data) / 1024
        print(f"Uploading image: {os.path.basename(image_path)} ({size_kb:.1f} KB as base64)")
        
        # Send to API
        response = requests.post(API_URL, json=payload)
        
        # Print the response
        print(f"Status code: {response.status_code}")
        print("Response:")
        print(json.dumps(response.json(), indent=2))
        
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    # First, check if PIL is installed
    try:
        import PIL
    except ImportError:
        print("PIL (Pillow) is required. Install it with: pip install pillow")
        sys.exit(1)
        
    # Check if an image path was provided
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        
        # Check if a prompt was provided
        prompt_number = 1
        if len(sys.argv) > 2:
            prompt_number = int(sys.argv[2])
        
        simulate_mobile_upload(image_path, prompt_number)
    else:
        print("Usage: python test_mobile_upload.py <path_to_image> [optional_prompt_number]")
        print("Example: python test_mobile_upload.py example.jpg 2") 