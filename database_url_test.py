import os
from dotenv import load_dotenv
import psycopg

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found. Check your .env file.")

with psycopg.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        db_version = cur.fetchone()[0]
        print("Connected successfully to:", db_version)