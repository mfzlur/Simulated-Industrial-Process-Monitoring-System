# app.py
import os
from flask import Flask, jsonify
from flask_restful import Api
from config import Config
import logging
from utils import enqueue_weather_data_fetch # Import the function

# Initialize logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)  # Get a logger for this module

# Create Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flask-RESTful API
api = Api(app)

# Import and register API resources (endpoints)
from api.weather import WeatherDataResource
api.add_resource(WeatherDataResource, '/weather/<int:location_id>')  # Register the resource

# Error handling (example)
@app.errorhandler(404)
def not_found(error):
    logger.warning(f"404 error: {error}") # Log the error
    return jsonify({'message': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    logger.error(f"Internal Server Error: {error}")
    return jsonify({'message': 'Internal server error'}), 500

# Basic route for testing purposes, triggers data fetch
@app.route('/test_data_fetch/<string:city_name>')
def test_data_fetch(city_name):
    enqueue_weather_data_fetch(city_name) # Enqueue the data fetch task
    return jsonify({'message': f'Data fetch for {city_name} enqueued'}), 200

if __name__ == '__main__':
    logger.info("Starting the application...") # Log startup message
    app.run(debug=Config.DEBUG) # Use config for debug mode
