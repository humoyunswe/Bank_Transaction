import psycopg2
from db_connection import connect, close_connection

def table_of_accounts():
    connection = connect()
    cur = connection.cursor()
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS accounts(id SERIAL PRIMARY KEY, id_card VARCHAR(50) NOT NULL UNIQUE, name VARCHAR(30) NOT NULL, balance DECIMAL(10, 2) DEFAULT 0)")
        connection.commit()
    except psycopg2.Error as error:
        connection.rollback()
        print(f"Akkaunt yaratilishda xatolik: {error}")
    finally:
        close_connection(connection)

def create_account(id_card:int, name:str):
    connection = connect()
    cur = connection.cursor()
    try:
        cur.execute("INSERT INTO accounts(id_card, name) VALUES (%s, %s)", (id_card, name))
        connection.commit()
        print("Account muvaffaqiyatli yaratildi!")
    except psycopg2.Error as error:
        connection.rollback()
        print(f"Akkaunt yaratilishda xatolik: {error}")
    finally:
        close_connection(connection)

def deposit_plus(id_card:int, amount:float):
    connection = connect()
    cur = connection.cursor()
    try:
        cur.execute("UPDATE accounts SET balance = balance + %s WHERE id_card = %s", (amount, id_card))
        connection.commit()
        print("Hisob muvaffaqiyatli to'ldirildi!")
    except psycopg2.Error as error:
        connection.rollback()
        print(f"Hisob to'ldirishda xatolik: {error}")
    finally:
        close_connection(connection)

def deposit_minus(id_card:int, amount:float):
    connection = connect()
    cur = connection.cursor()
    try:
        cur.execute("UPDATE accounts SET balance = balance - %s WHERE id_card = %s", (amount, id_card))
        connection.commit()
        print("Hisob mablag' muvaffaqiyatli yechildi!")
    except psycopg2.Error as error:
        connection.rollback()
        print(f"Hisob yechishda xatolik: {error}")
    finally:
        close_connection(connection)

def trans_history(id_card:int):
    connection = connect()
    cur = connection.cursor()
    try:
        cur.execute("SELECT * FROM accounts WHERE id_card = %s",(id_card, ))
        transactions = cur.fetchall()
        print("Otkazmalar tarixi: ")
        for transaction in transactions:
            print(f"Otkazuvchi ID si: {transaction[0]},\nAccount egasi: {transaction[2]},\nMiqdor: {transaction[3]}")
    except psycopg2.Error as error:
        print(f"Tarixni olishda xatolik: {error}")
    finally:
        close_connection(connection)
