data = request.get_json()
    # message = data.get('message', '')

    # headers = {
    #     "Content-Type": "application/json"
    # }
    # payload = {
    #     "contents": [
    #         {
    #             "parts": [
    #                 {"text": message}
    #             ]
    #         }
    #     ]
    # }

    # response = requests.post(
    #     f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
    #     headers=headers,
    #     json=payload
    # )

    # if response.status_code == 200:
    #     gemini_response = response.json()
    #     # Extract the response text from Gemini API
    #     try:
    #         reply = gemini_response['candidates'][0]['content']['parts'][0]['text']
    #     except (KeyError, IndexError):
    #         reply = "Sorry, I couldn't understand your question."
    # else:
    #     reply = "Sorry, there was an error connecting to the chatbot service."

    # return jsonify({"response": reply})
    # data = request.get_json()
    # message = data.get('message', '').lower()
    
    # responses = {
    #     'fertilizer': 'For fertilizer recommendations, use our calculator tool. It considers your crop type, land area, and soil type.',
    #     'weather': 'Check the weather section for detailed forecasts and rainfall predictions.',
    #     'price': 'Current market prices are available in the Market Prices section.',
    #     'hello': 'Hello! How can I assist with your farming needs today?',
    #     'bye': 'Goodbye! Feel free to ask if you have more questions.',
    #     'pest': 'For pest management, I recommend consulting with local agricultural experts.',
    #     'crop': 'The best crops to plant depend on your soil type, climate, and market demand.'
    # }
    
    # response = "I'm here to help with farming-related questions. You can ask me about fertilizers, weather, market prices, or other agricultural topics."
    
    # for keyword, resp in responses.items():
    #     if keyword in message:
    #         response = resp
    #         break
    
    # return jsonify({"response": response})