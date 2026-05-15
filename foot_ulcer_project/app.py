from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load("foot_ulcer_model.pkl")

# UI Page
@app.route('/')
def home():
    return render_template('index.html')

# API
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    df = pd.DataFrame([{
        'Temp_Left': data['Temp_Left'],
        'Temp_Right': data['Temp_Right'],
        'Pressure1': data['Pressure1'],
        'Pressure2': data['Pressure2'],
        'Humidity': data['Humidity']
    }])

    prediction = model.predict(df)[0]

    return jsonify({"risk": int(prediction)})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)