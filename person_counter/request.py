import requests

API_URL = "http://127.0.0.1:5000/detect"

# Symulacja przesyłania 1000 zadań
for i in range(1000):
    files = {"file": open(f"uploads/ludzie3.jpg", "rb")}
    response = requests.post(API_URL, files=files)
    print(response.json())