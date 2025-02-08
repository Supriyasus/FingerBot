from flask import Flask, render_template, request, jsonify
from utils import process_gesture  # Function to process gestures
import base64
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    image_data = request.json.get('image')
    if image_data:
        # Decode the base64 image
        image_data = image_data.split(",")[1]
        image_bytes = base64.b64decode(image_data)

        # Save the image temporarily
        temp_image_path = 'temp_image.png'
        with open(temp_image_path, 'wb') as f:
            f.write(image_bytes)

        # Process the image
        result = process_gesture(temp_image_path)

        # Clean up temporary image file
        os.remove(temp_image_path)

        return jsonify({'result': result})
    return jsonify({'error': 'No image provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
