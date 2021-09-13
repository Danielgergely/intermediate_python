from flask import Flask, request
from weather_service.umbrella import makeUmbrellaDecision
app = Flask(__name__)

@app.route('/')
def home():
    city = request.args.get('city')
    if city is None:
        city = 'new york'
    if makeUmbrellaDecision(city, 'us'):
        return f'Bring an umbrella in {city}!!'
    else:
        return f'No need for an umbrella in {city}'