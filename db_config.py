import mysql.connector

def func_db_with_blob():
    db_with_blob = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Seamusoutside1",
        database = "db_with_blob")
    return db_with_blob