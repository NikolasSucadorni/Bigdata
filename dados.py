import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(
    host = "banco do cliente",
    user = "usuário integrador",
    password = "senha",
    database = "banco de dados"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tabela")
result = mycursor.fetchall()

df = pd.DataFrame(result, columns=["coluna x", "coluna y", "coluna z"])

#supondo que o cliente tenha um faturamento e tenhamos valores e datas podemos plotar uma análise simples
plt.plot(df["data"], df["valor"])
plt.xlabel("data")
plt.ylabel("valor")
plt.title("Faturamento em anos Cliente")
plt.show