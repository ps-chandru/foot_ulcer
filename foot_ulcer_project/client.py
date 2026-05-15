import requests
import random
import time

url = "http://127.0.0.1:5000/predict"

while True:
    data = {
        "Temp_Left": round(random.uniform(32, 37), 2),
        "Temp_Right": round(random.uniform(32, 37), 2),
        "Pressure1": random.randint(20, 100),
        "Pressure2": random.randint(20, 100),
        "Humidity": random.randint(50, 90)
    }

    response = requests.post(url, json=data)

    print("Data:", data)
    print("Prediction:", response.json())

    if response.json()['risk'] == 2:
        print("⚠️ HIGH RISK ALERT!")

    print("----------------------")
    time.sleep(3)