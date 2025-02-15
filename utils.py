# utils.py
import redis
from rq import Queue
import os
from . import get_weather_data  # Import the function

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = os.getenv('REDIS_PORT', 6379)

redis_connection = redis.Redis(host=redis_host, port=redis_port)
task_queue = Queue(connection=redis_connection)

def store_weather_data(city_name):
    data = get_weather_data(city_name)
    # Store the data in the database (PostgreSQL)
    # Example:
    # weather_data = WeatherData(timestamp=datetime.now(), ...)
    # db.session.add(weather_data)
    # db.session.commit()
    print(f"Stored weather data for {city_name}")

def enqueue_weather_data_fetch(city_name):
    task_queue.enqueue(store_weather_data, city_name)
