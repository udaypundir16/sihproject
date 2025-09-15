# backend.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Mock data for market prices
market_prices = {
    "wheat": 22.50,
    "rice": 35.75,
    "sugarcane": 3.40,
    "corn": 19.20
}

# Mock weather data
weather_forecast = [
    {"day": "Today", "condition": "Sunny", "temp": 28},
    {"day": "Wed", "condition": "Partly Cloudy", "temp": 27},
    {"day": "Thu", "condition": "Cloudy", "temp": 26},
    {"day": "Fri", "condition": "Rainy", "temp": 24},
    {"day": "Sat", "condition": "Heavy Rain", "temp": 23},
    {"day": "Sun", "condition": "Partly Cloudy", "temp": 25},
    {"day": "Mon", "condition": "Sunny", "temp": 27}
]

@app.route('/')
def home():
    return "AgroVision Backend API"

@app.route('/api/market-prices', methods=['GET'])
def get_market_prices():
    return jsonify(market_prices)

@app.route('/api/weather', methods=['GET'])
def get_weather():
    return jsonify(weather_forecast)

@app.route('/api/predict-crop', methods=['POST'])
def predict_crop():
    data = request.json
    # Mock prediction logic
    soil_type = data.get('soil_type', 'loamy')
    rainfall = data.get('rainfall', 750)
    temperature = data.get('temperature', 28)
    ph = data.get('ph', 6.5)
    
    if soil_type == "sandy" and rainfall < 600:
        crop = "Millets"
        yield_estimate = 3.5
    elif soil_type == "clay" and temperature > 30:
        crop = "Cotton"
        yield_estimate = 2.8
    else:
        crop = "Rice"
        yield_estimate = 4.2
        
    return jsonify({
        "recommended_crop": crop,
        "expected_yield": yield_estimate
    })

@app.route('/api/calculate-fertilizer', methods=['POST'])
def calculate_fertilizer():
    data = request.json
    crop_type = data.get('crop_type', 'wheat')
    area = data.get('area', 1)
    
    # Mock calculation
    if crop_type == "rice":
        recommendation = "60-50-40"
    elif crop_type == "corn":
        recommendation = "45-35-30"
    else:
        recommendation = "50-40-30"
        
    return jsonify({
        "npk_recommendation": recommendation,
        "amount": f"{recommendation} kg/acre"
    })

if __name__ == '__main__':
    app.run(debug=True)