from prettytable import PrettyTable
from pdb import set_trace
from Produto import Produto
from Mesa import Mesa
import sqlite3
import os

CONN = sqlite3.connect('sistemas.db')
CURSOR = CONN.cursor()

class Sistema():
    def __init__(self):
        self.mesas = []
        # try:
        #     with open('recover.json', encoding="UTF-8") as f:
        #         data = json.load(d)
        # except


def cadastra_produtos():
    os.system('cls')
    nome_produto = input('Nome do produto - ')
    valor_produto = input('Valor do produto - ')
    CURSOR.execute(f'INSERT INTO Produtos (nome, valor), VALUES ("{nome_produto}", {valor_produto})')
    CONN.commit()

def lista_produtos():
    os.system('cls')
    CURSOR.execute('SELECT * FROM Produtos')
    retorno = CURSOR.fetchall()
    t = PrettyTable(['ID', 'DESCRIÇÃO', 'VALOR'])
    for produto in retorno:
        t.add_row([produto[0], produto[1], produto[2]])
    print(t)

def deleta_produto():
    os.system('cls')
    CURSOR.execute('SELECT * FROM Produtos')
    retorno = CURSOR.fetchall()
    t = PrettyTable(['ID', 'DESCRIÇÃO', 'VALOR'])
    for produto in retorno:
        t.add_row([produto[0], produto[1], produto[2]])
    print(t)
    item_excluir = input('Selecione ID para Excluir - ')
    CURSOR.execute(f'DELETE FROM Produtos WHERE ID = {item_excluir}')
    CONN.commit()

def altera_produto():
    os.system('cls')
    CURSOR.execute('SELECT * FROM Produtos')
    retorno = CURSOR.fetchall()
    t = PrettyTable(['ID', 'DESCRIÇÃO', 'VALOR'])
    for produto in retorno:
        t.add_row([produto[0], produto[1], produto[2]])
    print(t)
    item_alterar = input('Selecione ID para Alterar - ')
    novo_nome = input('Novo nome - ')
    novo_valor = input('Novo valor - ')
    CURSOR.execute(f'UPDATE Produtos set nome "{novo_nome}", valor = {novo_valor} WHERE ID = {item_alterar}')
    CONN.commit()

def lancar_produto(numero_mesa):
    mesa = [mesa for mesa in sistema.mesas if mesa.id == numero_mesa][0]
    id_produto = int(input('ID do produto - '))
    qtd_produto = int(input('Quantidade - '))
    if id_produto in [produto.id for produto in mesa.produtos]:
        produto = [produto for produto in mesa.produtos if produto.id == id_produto]
        produto[0].quantidade += qtd_produto
    else:
        CURSOR.execute(f'SELECT * FROM Produtos WHERE ID = {id_produto}')
        retorno = CURSOR.fetchone()
        if not retorno:
            os.system('cls')
            print("Produto Inválido")
            lancar_produto(numero_mesa)
        else:
            produto = Produto()
            produto.id = retorno[0]
            produto.valor = retorno[2]
            produto.nome = retorno[1]
            produto.quantidade = qtd_produto
            mesa.produtos.append(produto)

def manage_mesa(numero_mesa):
    if numero_mesa not in [mesa.id for mesa in sistema.mesas]:
        mesa = Mesa()
        mesa.id = numero_mesa
        sistema.mesas.append(mesa)
        lancar_produto(numero_mesa)
    else:
        lancar_produto(numero_mesa)

def montar_total_mesa(mesa):
    t = PrettyTable(['NOME', 'VALOR', 'QUANTIDADE'])
    for produto in mesa.produtos:
        t.add_row([produto.nome, produto.valor, produto.quantidade])
    set_trace()
    # print(t.get_string())
    pass

def fechar_conta():
    os.system('cls')
    numero_mesa = int(input("Informe o numero da mesa - "))
    if numero_mesa in [mesa.id for mesa in sistema.mesas]:
        mesa = [mesa for mesa in sistema.mesas if numero_mesa == mesa.id][0]
        output_mesa = montar_total_mesa(mesa)
    else:
        resposta = input("Mesa inexistente\n"
                         "Para voltar - *")
        if resposta != '*':
            fechar_conta()


if __name__ == '__main__':
    os.system('cls')
    sistema = Sistema()
    tecla = ''
    while tecla != '*':
        os.system('cls')
        tecla = input('Digite a mesa - ')
        try:
            numero_mesa = int(tecla)
            # manage_mesa(numero_mesa)
        except ValueError:
            os.system('cls')
            tecla = input('p1 - Cadastrar Produto\n'
                          'p2 - Listar Produtos\n'
                          'p3 - Excluir Produtos\n'
                          'p4 - Alterar Produto\n'
                          'p5 - Fechar Conta\n'
                          'p0 - Voltar\n'
                          '* - Sair\n')
            if tecla == 'p1':
                cadastra_produtos()
            elif tecla == 'p2':
                lista_produtos()
            elif tecla == 'p3':
                deleta_produto()
            elif tecla == 'p4':
                altera_produto()
            elif tecla == 'p5':
                fechar_conta()
            elif tecla == 'p0':
                os.system('cls')
                break
            else:
                os.system('cls')
                print('Função não listada')

    CONN.close()