import psycopg2


def conectar():
    return psycopg2.connect(
        host="localhost",
        database="mercado",
        user="postgres",
        password="260903"
    )