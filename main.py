class informacoes_pessoas(object):
    def __init__(self, nome, salario_bruto, liquido, desconto):
       self.nome = nome
       nome.get()
       nome.set()
       self.salario_bruto = salario_bruto
       salario_bruto.get()
       salario_bruto.set()
       self.desconto = salario_bruto / 100 * ()
       desconto.get()
       desconto.set()
       self.liquido = salario_bruto - desconto
       liquido.get()
       liquido.set()

    nome = input( "informe seu nome: ")
    salario_bruto = int(input("informe seu salário: "))
    if salario_bruto<=2400:
            desconto = (salario_bruto / 100) * 8
            print("seu liquido é de: ", salario_bruto - desconto)
    elif salario_bruto<=3600:
        desconto = (salario_bruto / 100) * 9
        print("seu liquido é de: ", salario_bruto - desconto)
    else:
        desconto = (salario_bruto / 100) * 11
        print("seu liquido é de: ", salario_bruto - desconto)

def _init_(self, investimento):
    investimento = investimento
    investimento.get()
    investimento.set()
investimento = input("quanto é o seu aporte inicial: ")