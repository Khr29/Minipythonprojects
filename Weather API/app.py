from flask import Flask, redirect,jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

API_KEY = os.getenv("Weather_api_key")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/weather', methods=['GET'])
def get_weather():
    
