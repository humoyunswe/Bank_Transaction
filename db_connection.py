import psycopg2

DB = input("DATABASE: ")
USER = input("USER: ")
HOST = 'localhost'
PORT = 5432
PASSWORD = input("Password: ")

def connect():
    connection = psycopg2.connect(database=DB, user=USER, host=HOST, port=PORT, password=PASSWORD)
    return connection

def close_connection(connection):
    connection.close()
