# from flask import Flask, render_template, request, jsonify
# import json
# import random
# from datetime import datetime, timedelta

# app = Flask(__name__)

# # Sample data for the application
# crop_data = {
#     "wheat": {
#         "nitrogen": 120,
#         "phosphorus": 60,
#         "potassium": 40,
#         "water_requirement": 500,
#         "growth_period": 120
#     },
#     "rice": {
#         "nitrogen": 100,
#         "phosphorus": 50,
#         "potassium": 50,
#         "water_requirement": 1000,
#         "growth_period": 150
#     },
#     "corn": {
#         "nitrogen": 150,
#         "phosphorus": 70,
#         "potassium": 70,
#         "water_requirement": 600,
#         "growth_period": 110
#     },
#     "sugarcane": {
#         "nitrogen": 200,
#         "phosphorus": 80,
#         "potassium": 100,
#         "water_requirement": 1500,
#         "growth_period": 365
#     },
#     "cotton": {
#         "nitrogen": 80,
#         "phosphorus": 40,
#         "potassium": 30,
#         "water_requirement": 700,
#         "growth_period": 180
#     }
# }

# soil_multipliers = {
#     "sandy": {"nitrogen": 1.2, "phosphorus": 1.1, "potassium": 1.1},
#     "loamy": {"nitrogen": 1.0, "phosphorus": 1.0, "potassium": 1.0},
#     "clay": {"nitrogen": 0.9, "phosphorus": 0.9, "potassium": 0.9},
#     "silt": {"nitrogen": 1.0, "phosphorus": 1.0, "potassium": 1.0}
# }

# market_prices = {
#     "wheat": 2100,
#     "rice": 2500,
#     "corn": 1800,
#     "sugarcane": 180,
#     "cotton": 5500
# }

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/calculate_fertilizer', methods=['POST'])
# def calculate_fertilizer():
#     data = request.get_json()
    
#     crop = data.get('crop', 'wheat')
#     area = float(data.get('area', 1))

#     soil = data.get('soil', 'loamy')
    
#     if crop not in crop_data:
#         return jsonify({"error": "Invalid crop type"}), 400
    
#     # Calculate fertilizer requirements
#     crop_info = crop_data[crop]
#     soil_info = soil_multipliers[soil]
    
#     nitrogen = crop_info['nitrogen'] * area * soil_info['nitrogen']
#     phosphorus = crop_info['phosphorus'] * area * soil_info['phosphorus']
#     potassium = crop_info['potassium'] * area *  soil_info['potassium']
    
#     return jsonify({
#         "nitrogen": round(nitrogen, 2),
#         "phosphorus": round(phosphorus, 2),
#         "potassium": round(potassium, 2),
#         "water_requirement": crop_info['water_requirement'] * area,
#         "growth_period": crop_info['growth_period']
#     })

# @app.route('/market_prices')
# def get_market_prices():
#     # Simulate price fluctuations
#     fluctuations = {}
#     for crop, price in market_prices.items():
#         fluctuation = random.uniform(-0.05, 0.05)  # ±5% fluctuation
#         fluctuations[crop] = {
#             "current_price": round(price * (1 + fluctuation)),
#             "change_percent": round(fluctuation * 100, 2)
#         }
    
#     return jsonify(fluctuations)

# @app.route('/weather_forecast')
# def get_weather_forecast():
#     # Generate a 7-day weather forecast
#     forecast = []
#     base_temp = random.randint(25, 30)
    
#     for i in range(7):
#         date = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
#         temp = base_temp + random.randint(-3, 3)
#         conditions = ['Sunny', 'Partly Cloudy', 'Cloudy', 'Light Rain', 'Moderate Rain']
#         condition = random.choice(conditions)
        
#         forecast.append({
#             "date": date,
#             "temperature": temp,
#             "condition": condition,
#             "humidity": random.randint(50, 90),
#             "wind_speed": random.randint(5, 20)
#         })
    
#     return jsonify(forecast)

# @app.route('/crop_prediction', methods=['POST'])
# def predict_crop():
#     data = request.get_json()
    
#     # Extract parameters
#     soil_type = data.get('soil_type', 'loamy')
#     rainfall = float(data.get('rainfall', 100))
#     temperature = float(data.get('temperature', 25))
#     ph_level = float(data.get('ph_level', 6.5))
    
#     # Simple prediction algorithm
#     suitable_crops = []
    
#     for crop, info in crop_data.items():
#         score = 0
        
#         # Soil type matching (simplified)
#         if soil_type == 'loamy':
#             score += 10
#         elif soil_type in ['sandy', 'silt'] and crop in ['cotton', 'groundnut']:
#             score += 8
#         elif soil_type == 'clay' and crop in ['rice', 'wheat']:
#             score += 8
        
#         # Rainfall suitability
#         if abs(rainfall - info['water_requirement'] / 10) < 50:
#             score += 8
#         elif abs(rainfall - info['water_requirement'] / 10) < 100:
#             score += 5
        
#         # Temperature suitability
#         if 20 <= temperature <= 30:
#             score += 8
#         elif 15 <= temperature <= 35:
#             score += 5
        
#         # pH level suitability
#         if 6 <= ph_level <= 7:
#             score += 8
#         elif 5.5 <= ph_level <= 7.5:
#             score += 5
        
#         if score >= 20:  # Threshold for suitability
#             suitable_crops.append({
#                 "crop": crop,
#                 "score": score,
#                 "expected_yield": random.randint(15, 25) * 100,  # kg per acre
#                 "market_price": market_prices.get(crop, 0)
#             })
    
#     # Sort by score
#     suitable_crops.sort(key=lambda x: x['score'], reverse=True)
    
#     return jsonify(suitable_crops)

# @app.route('/chatbot', methods=['POST'])
# def chatbot():
#     data = request.get_json()
#     message = data.get('message', '').lower()
    
#     responses = {
#         'fertilizer': 'For fertilizer recommendations, use our calculator tool. It considers your crop type, land area, and soil type.',
#         'weather': 'Check the weather section for detailed forecasts and rainfall predictions.',
#         'price': 'Current market prices are available in the Market Prices section.',
#         'hello': 'Hello! How can I assist with your farming needs today?',
#         'bye': 'Goodbye! Feel free to ask if you have more questions.',
#         'pest': 'For pest management, I recommend consulting with local agricultural experts.',
#         'crop': 'The best crops to plant depend on your soil type, climate, and market demand.'
#     }
    
#     response = "I'm here to help with farming-related questions. You can ask me about fertilizers, weather, market prices, or other agricultural topics."
    
#     for keyword, resp in responses.items():
#         if keyword in message:
#             response = resp
#             break
    
#     return jsonify({"response": response})

# if __name__ == '__main__':
#     app.run(debug=True)
    
from flask import Flask, render_template, request, jsonify
import json
import random
from datetime import datetime, timedelta
import google.generativeai as genai
import os

app = Flask(__name__)

# ---------------- GEMINI SETUP ----------------
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "enter your gemini api key")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# ---------------- SAMPLE DATA -----------------
crop_data = {
    "wheat": {"nitrogen": 120, "phosphorus": 60, "potassium": 40, "water_requirement": 500, "growth_period": 120},
    "rice": {"nitrogen": 100, "phosphorus": 50, "potassium": 50, "water_requirement": 1000, "growth_period": 150},
    "corn": {"nitrogen": 150, "phosphorus": 70, "potassium": 70, "water_requirement": 600, "growth_period": 110},
    "sugarcane": {"nitrogen": 200, "phosphorus": 80, "potassium": 100, "water_requirement": 1500, "growth_period": 365},
    "cotton": {"nitrogen": 80, "phosphorus": 40, "potassium": 30, "water_requirement": 700, "growth_period": 180}
}

soil_multipliers = {
    "sandy": {"nitrogen": 1.2, "phosphorus": 1.1, "potassium": 1.1},
    "loamy": {"nitrogen": 1.0, "phosphorus": 1.0, "potassium": 1.0},
    "clay": {"nitrogen": 0.9, "phosphorus": 0.9, "potassium": 0.9},
    "silt": {"nitrogen": 1.0, "phosphorus": 1.0, "potassium": 1.0}
}

market_prices = {
    "wheat": 2100,
    "rice": 2500,
    "corn": 1800,
    "sugarcane": 180,
    "cotton": 5500
}

# ---------------- ROUTES -----------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_fertilizer', methods=['POST'])
def calculate_fertilizer():
    data = request.get_json()
    crop = data.get('crop', 'wheat')
    area = float(data.get('area', 1))
    soil = data.get('soil', 'loamy')

    if crop not in crop_data:
        return jsonify({"error": "Invalid crop type"}), 400

    crop_info = crop_data[crop]
    soil_info = soil_multipliers[soil]

    nitrogen = crop_info['nitrogen'] * area * soil_info['nitrogen']
    phosphorus = crop_info['phosphorus'] * area * soil_info['phosphorus']
    potassium = crop_info['potassium'] * area * soil_info['potassium']

    return jsonify({
        "nitrogen": round(nitrogen, 2),
        "phosphorus": round(phosphorus, 2),
        "potassium": round(potassium, 2),
        "water_requirement": crop_info['water_requirement'] * area,
        "growth_period": crop_info['growth_period']
    })

@app.route('/market_prices')
def get_market_prices():
    fluctuations = {}
    for crop, price in market_prices.items():
        fluctuation = random.uniform(-0.05, 0.05)
        fluctuations[crop] = {
            "current_price": round(price * (1 + fluctuation)),
            "change_percent": round(fluctuation * 100, 2)
        }
    return jsonify(fluctuations)

@app.route('/weather_forecast')
def get_weather_forecast():
    forecast = []
    base_temp = random.randint(25, 30)
    for i in range(7):
        date = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
        temp = base_temp + random.randint(-3, 3)
        conditions = ['Sunny', 'Partly Cloudy', 'Cloudy', 'Light Rain', 'Moderate Rain']
        condition = random.choice(conditions)
        forecast.append({
            "date": date,
            "temperature": temp,
            "condition": condition,
            "humidity": random.randint(50, 90),
            "wind_speed": random.randint(5, 20)
        })
    return jsonify(forecast)

@app.route('/crop_prediction', methods=['POST'])
def predict_crop():
    data = request.get_json()
    soil_type = data.get('soil_type', 'loamy')
    rainfall = float(data.get('rainfall', 100))
    temperature = float(data.get('temperature', 25))
    ph_level = float(data.get('ph_level', 6.5))

    suitable_crops = []
    for crop, info in crop_data.items():
        score = 0
        if soil_type == 'loamy':
            score += 10
        elif soil_type in ['sandy', 'silt'] and crop in ['cotton', 'groundnut']:
            score += 8
        elif soil_type == 'clay' and crop in ['rice', 'wheat']:
            score += 8

        if abs(rainfall - info['water_requirement'] / 10) < 50:
            score += 8
        elif abs(rainfall - info['water_requirement'] / 10) < 100:
            score += 5

        if 20 <= temperature <= 30:
            score += 8
        elif 15 <= temperature <= 35:
            score += 5

        if 6 <= ph_level <= 7:
            score += 8
        elif 5.5 <= ph_level <= 7.5:
            score += 5

        if score >= 20:
            suitable_crops.append({
                "crop": crop,
                "score": score,
                "expected_yield": random.randint(15, 25) * 100,
                "market_price": market_prices.get(crop, 0)
            })

    suitable_crops.sort(key=lambda x: x['score'], reverse=True)
    return jsonify(suitable_crops)

# ----------------- CHATBOT USING GEMINI -----------------
@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data.get("message", "")

    try:
        response = model.generate_content(
            f"You are an agricultural assistant chatbot. The farmer asked: {message}"
        )
        reply = response.text.strip()
    except Exception as e:
        reply = f"Error generating response: {str(e)}"

    return jsonify({"response": reply})



@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data.get("message", "")

    try:
        response = model.generate_content(
            [f"You are an agricultural assistant chatbot. Reply simply and clearly.\nFarmer: {message}"]
        )

        # Some versions return .text, others need candidates
        if hasattr(response, "text"):
            reply = response.text.strip()
        elif hasattr(response, "candidates"):
            reply = response.candidates[0].content.parts[0].text.strip()
        else:
            reply = "Sorry, I couldn’t understand the response from Gemini."

    except Exception as e:
        reply = f"Error generating response: {str(e)}"

    return jsonify({"response": reply})

# --------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
