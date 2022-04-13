import datetime
import mysql.connector
from tabulate import tabulate
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'dabely2006',
    auth_plugin='mysql_native_password',
    database = 'testdata'
)
def main():
    insert_data_to_database(name = 'Abel', gender = 'M')
    show_information()
    remove_data_by_name(name = 'Abel')
    print('Tabla modificada')
    show_information()


def insert_data_to_database(name: str = 'nombre', date: str = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'), gender: str = None) -> None:   
    mycursor = db.cursor()
    query = f"INSERT INTO Test (name, created, gender) VALUE ('{name}', '{date}', '{gender}')"
    mycursor.execute(query)
    db.commit()
    
def remove_data_by_id(id: int = None):
    if id is None:
        print('id cannot be None')
        return None
    else:
        mycursor = db.cursor()
        query = f'DELETE FROM Test WHERE ID={id};'
        mycursor.execute(query)
        db.commit()
        return None
        
def remove_data_by_name(name: str = None) -> None:   
    if name == None:
        print('name cannot be None')
        return None
    else:
        mycursor = db.cursor()
        query = f'DELETE FROM Test WHERE name="{name}";'
        mycursor.execute(query)
        db.commit()
        return None
    
def get_columns():
    mycursor = db.cursor()
    query = f"DESCRIBE Test"
    mycursor.execute(query)
    for x in mycursor:
        print(x)

def show_information():
    mycursor = db.cursor()
    query = 'SELECT * FROM Test '
    mycursor.execute(query)
    data = []
    for x in mycursor:
        data.append(x)
    print (tabulate(data, headers=["Name", "Created", "Gender", 'ID']))
        
        
if __name__ == '__main__':
    main()