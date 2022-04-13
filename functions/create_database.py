import mysql.connector
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'dabely2006',
    auth_plugin='mysql_native_password',
)

def crear_basedatos():
    mycursor = db.cursor()
    query = """CREATE DATABASE IF NOT EXISTS tdah"""
    mycursor.execute(query)
    return True