import PySimpleGUI as sg
import mysql.connector

try:
        mydb = mysql.connector.connect(
        host="host",
        user="usuario",
        password="senha",
        database="banco"
        )
        mycursor = mydb.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")

sg.theme('Reddit')
product_categories = ["Limpeza", "Temperos", "Enlatados", "Brinquedos", "Frios", "Bebidas", 
                      "Cosméticos", "Padaria", "Pet", "Cozinha"]

layout = [
    [sg.Text('Cliente',size=(6,0)),sg.Input(key='1',size=(20,0))],
    [sg.Text('Produto',size=(6,0)),sg.Input(size=(20,0),key='2')],
    [sg.Text('Quantidade'),sg.Input(key='3',size=(3,0))],
    [sg.Text('Categoria do Produto'), sg.Combo(product_categories, key='4')],
    [sg.Button('Salvar')]
]

window = sg.Window('Cadastro de Produtos',layout)

event = window.read()

if event == 'Salvar':
    cliente = window.read(['1'].value)
    produto = window.read(['2'].value)
    quantidade = int(window.read(['3'].value))
    categoria = window.read(['4'].value)

try:
        sql = "INSERT INTO produtos (cliente, produto, quantidade, categoria) VALUES (%s, %s, %s, %s)"
        val = (cliente, produto, quantidade, categoria)
        mycursor.execute(sql, val)
        mydb.commit()
        sg.popup('Produto cadastrado com sucesso!')

except mysql.connector.Error as err:
        sg.popup(f"Erro ao inserir o produto: {err}")

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        sg.popup('Produto Cadastrado')
        window['1'].update('')
        window['2'].update('')
        window['3'].update('')
        window['4'].update('')
mydb.close()