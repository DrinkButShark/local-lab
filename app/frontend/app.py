import os
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")

@app.get("/")
def index():
    try:
        response = requests.get(f"{BACKEND_URL}/")
        if response.status_code == 200:
            backend_data = response.json()
            message = backend_data.get("message", "No message from backend")
        else:
            message = f"Error from backend: {response.status_code}"
    except requests.exceptions.RequestException as e:
        message = f"Could not connect to backend: {e}"
        
    return render_template("index.html", message=message, backend_url=BACKEND_URL)

@app.get("/api/data")
def api_proxy():
    try:
        response = requests.get(f"{BACKEND_URL}/")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
