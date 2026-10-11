import os

import psycopg
from dotenv import load_dotenv
from pgvector.psycopg import register_vector

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/citations")


def connect() -> psycopg.Connection:
    conn = psycopg.connect(DATABASE_URL)
    register_vector(conn)
    return conn
