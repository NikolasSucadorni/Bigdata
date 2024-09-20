import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(
    host = "192.168.1.100",
    user = "MerceariaMeninas",
    password = "30710670#",
    database = "MMeninasDB"
)

def connect_to_database(db_config):
    try:
        mydb = mysql.connector.connect(mydb)
        return mydb
    except mysql.connector.Error as err:
        print(f"Error: {err}")

mydb = connect_to_database(mydb)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM MerceariaMeninas'")
result = mycursor.fetchall()

df = pd.DataFrame(result, columns=['idcompra', 'Movimentação', 'Quantidade', 'Categoria do Produto','Data', 'Valor', 'Produto'])

mydb.close()

print(df.head())
