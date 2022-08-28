import mysql.connector
db = mysql.connector.connect(host = 'localhost',
                             user = 'root', 
                             passwd = 'dabely2006', 
                             auth_plugin = 'mysql_native_password',
                             database = 'neuro_innova')