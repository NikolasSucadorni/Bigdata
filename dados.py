import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(
    host = "192.168.1.100",
    user = "MerceariaMeninas",
    password = "30710670#",
    database = "MMeninasDB"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM produtos WHERE movimentacao ='Saída'")
result = mycursor.fetchall()

df = pd.DataFrame(result, columns=["produto", "valor",])

plt.plot(df["produto"], df["valor"])
plt.xlabel("produto")
plt.ylabel("valor")
plt.title("Faturamento Cliente")
plt.show