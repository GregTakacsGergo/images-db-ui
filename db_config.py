import mysql.connector
from config import DB_PASSWORD

def func_db_with_blob():
    db_with_blob = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = DB_PASSWORD,
        database = "db_with_blob")
    return db_with_blob