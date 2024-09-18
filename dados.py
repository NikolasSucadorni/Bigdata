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
mycursor.execute("SELECT * FROM produtos")
result = mycursor.fetchall()

df = pd.DataFrame(result, columns=["coluna x", "coluna y", "coluna z"])

#supondo que o cliente tenha um faturamento e tenhamos valores e datas podemos plotar uma análise simples
plt.plot(df["data"], df["valor"])
plt.xlabel("data")
plt.ylabel("valor")
plt.title("Faturamento em anos Cliente")
plt.show