import psycopg2
import os

DATABASE_URL = os.environ.get("postgresql://krishvika_db_user:d8vPEO77hkNjM2u9UsrUHYhSbIyOBpkf@dpg-d62ciq8nputs739l31dg-a/krishvika_db")

def get_connection():
    return psycopg2.connect(DATABASE_URL)
