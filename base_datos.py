import base_datos
import mysql.connector

def conectarBD():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ACADEMICO",
        port=3306
    )

