import os
import platform
import mysql.connector

conexao = mysql.connector.connect(user='root', password='180219', host='127.0.0.1', database='dividas-table')
conexao.close()

def limpar_tela():
    if plataform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def sair():
    print("obrigado por ultilizar o sistema!")
    os.exit(0)


def mensagem_menu_principal():
    limpar_tela()
    print("******************************************* ")
    print("*      Bem-Vindo Ao Sistema De Cadastro    *")
    print("*----------------------------------------- *")
    print("*      ESCOLHA UMA DAS OPÇÕES DSPONÍVEIS   *")
    print("*        1 - CADASTRAR DIVIDA              *")
    print("*        2 - ALTERAR DIVIDA                *")
    print("*        3 - LISTAR DIVIDAS                *")
    print("*        4 - ESPORTAR DIVIDA               *")
    print("*        0 - SAIR DO SISTEMA               *")
    print("********************************************")

def mensagem_menu_alterar():
    limpar_tela()
    print("*********************************************** ")
    print("*         ALTERAR UM CONTATO EXISTENTE         *")
    print("*--------------------------------------------- *")
    print("*  ESCOLHA UMA DAS OPÇÕES PARA LOCALIZA DIVIDA *")
    print("*           1 - ID                             *")
    print("*           2 - NOME                           *")
    print("*           3 - PARCELA                        *")
    print("*           4 - DATA VENCIMENTO                *")
    print("*           5 - VALOR                          *")
    print("*           0 - SAIR DO SISTEMA                *")
    print("************************************************")


def mensagem_cadastrar():
    limpar_tela()
    print("*********************************************** ")
    print("*        CADASTRANDO NOVA DIVIDA               *")
    print("************************************************")

def cadastrar():
    mensagem_cadastrar()
    nome = input("Informe o nome da divida: ")
    parcela = int(input("Informe o numero de parcelas: "))
    vencimento = dataclasses(input("Informe a data de vencimento: "))
    valor = float(input("Informe o valor da divida: "))

def menu_principal():
    mensagem_menu_principal()
    opcao = input("Informe a opção desejada: ")
    print(f"Opção: {opcao}")

if __name__ == "__main__":
    menu_principal()
