# db.py
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file (if present)

DB_NAME = os.environ.get("DB_NAME", "your_db_name") 
DB_USER = os.environ.get("DB_USER", "your_db_user") 
DB_PASSWORD = os.environ.get("DB_PASSWORD", "your_db_password")  
DB_HOST = os.environ.get("DB_HOST", "localhost") 
DB_PORT = os.environ.get("DB_PORT", "5432")  

def get_db_connection():
   
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Database connection successful")  # Optional: Confirmation message
    except psycopg2.Error as e:
        print(f"Database connection failed: {e}")
    return conn
