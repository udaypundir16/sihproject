from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to call backend

# Configure Gemini
genai.configure(api_key="enter your gemini api key here")
model = genai.GenerativeModel("gemini-1.5-flash")
from flask import Flask, render_template

app = Flask(__name__, template_folder="../frontend")

@app.route("/")
def home():
    # returns index.html
    return render_template("index.html")

@app.route("/fertilizer")
def fertilizer():
    # just return hello
    return "Hello"
    # return render_template("chatbot.html")

@app.route("/chat")
def chat():
    # returns chatbot.html
    return render_template("chatbot.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("message", "")
    response = model.generate_content(prompt)
    return jsonify({"reply": response.text})

@app.route("/fertilizer", methods=["POST"])
def fertilizer_calc():
    data = request.json
    crop = data["crop"]
    area = float(data["area"])
    soil = data["soil"]

    base = {
        "wheat": {"N":120, "P":60, "K":40},
        "rice": {"N":150, "P":70, "K":60},
        "corn": {"N":180, "P":80, "K":80},
        "sugarcane": {"N":200, "P":100, "K":120},
        "cotton": {"N":160, "P":80, "K":60}
    }
    soil_factor = {"sandy":1.2, "loamy":1.0, "clay":0.8, "silt":1.1}
    mult = soil_factor.get(soil,1)

    rec = {k: v*area*mult for k,v in base[crop].items()}
    return jsonify(rec)

if __name__ == "__main__":
    app.run(debug=True)
