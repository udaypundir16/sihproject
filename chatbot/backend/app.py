from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure Gemini API (Replace with your actual API key)
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'ENTER_YOUR_GEMINI_API_KEY_HERE')
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Generate response using Gemini API
        response = model.generate_content(user_message)
        
        return jsonify({'response': response.text})
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK', 'message': 'Server is running'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)