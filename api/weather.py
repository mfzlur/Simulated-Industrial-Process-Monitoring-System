# api/weather.py
from flask_restful import Resource
<<<<<<< HEAD

class WeatherDataResource(Resource):
    def get(self, location_id):
        # Fetch weather data from database based on location_id
        # Example:
        # data = WeatherData.query.filter_by(location_id=location_id).all()
        # return [item.serialize() for item in data]
        return {'message': f'Weather data for location {location_id}'}  # Placeholder
=======
import requests
from dotenv import load_dotenv
import os
from db import get_db_connection
import psycopg2
from flask import render_template, Response


load_dotenv()

appid = os.environ.get("API_KEY")



def fetch_data(table_name):
    conn = get_db_connection()
    if conn is None:
        return None

    try:
        with conn.cursor() as cursor:
            query = f"SELECT * FROM {table_name};"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
    except psycopg2.Error as e:
        print(f"Error fetching rows: {e}")
        return None
    finally:
        conn.close()



class WeatherDataResource(Resource):
    def get(self):

        rows = fetch_data('lat_n_long')

        responses = {}

        for id, lat, lon, city in rows:
            url = f'http://api.openweathermap.org/data/2.5/forecast/?lat={lat}&lon={lon}&cnt=1&appid={appid}'

            response = requests.get(url)

            responses[city] = response.json()
            # print(responses)


        return responses



>>>>>>> 2f5cab2 (api update)
