import PySimpleGUI as sg
import mysql.connector


try:
        mydb = mysql.connector.connect(
        host="192.168.1.100",
        user="MerceariaMeninas",
        password="30710670#",
        database="MMeninasDB"
        )
        mycursor = mydb.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")


sg.theme('Reddit')
entrada_saída = ["Entrada", "Saídas"]


sg.theme('Reddit')
product_categories = ["Grãos", "Massas","Óleos", "Temperos", "Enlatados", "Frios", "Laticínios", "Congelados", "Bebidas",
                      "Higiene", "Padaria", "Pet", "Chocolates e doces"]


layout = [
    [sg.Text('Produto',size=(6,0)),sg.Input(key='1',size=(20,0))],
    [sg.Text('Movimentação'),sg.Combo(entrada_saída,key='2')],
    [sg.Text('Quantidade'),sg.Input(key='3',size=(3,0))],
    [sg.Text('Valor'),sg.Input(key='4',size=(10,0))],
    [sg.Text('Categoria do Produto'), sg.Combo(product_categories, key='5')],
    [sg.Button('Salvar')]
]


window = sg.Window('Cadastro de Produtos',layout)


event = window.read()


if event == 'Salvar':
    produto = window.read(['1'].value)
    movimentacao = window.read(['2'].value)
    quantidade = int(window.read(['3'].value))
    valor = float(window.read(['4'].value))
    categoria = window.read(['5'].value)


try:
        sql = "INSERT INTO produtos (produto, movimentação, quantidade, valor, categoria) VALUES (%s, %s, %s, %s)"
        val = (produto, movimentacao, quantidade, categoria)
        mycursor.execute(sql, val)
        mydb.commit()
        sg.popup('Lançamento efetuado com sucesso!')


except mysql.connector.Error as err:
        sg.popup(f"Erro ao inserir o produto: {err}")


while True:
    event, values = window.read()


    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        sg.popup('Lançamento efetuado')
        window['1'].update('')
        window['2'].update('')
        window['3'].update('')
        window['4'].update('')
        window['5'].update('')
mydb.close()
