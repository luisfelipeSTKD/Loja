# import datetime as DataAtual
# from itertools import product

# print("######")
# print("Bem vindo! \n")
# print("Inicialmente iremos realizar uma análise de crédito.")
# print("###### \n")

# nomeCliente = input('Qual o seu nome? ')
# cargo = input('Por gentileza, insira seu cargo atual: ')
# salario = int(input('Seu salário: '))
# anoNascimento = int(input('E o ano de seu nascimento: '))
# print(f'\nEssas são as informações que você inseriu. Cargo: {cargo}, Salário: R${salario} e ano de nascimento: {anoNascimento}.\n')


# # Etapa 2
# # Mostre na tela a idade aproximada do usuário. Você pode fazer isso ao subtrair o ano em que estamos pelo ano de nascimento que ele digitou.

# # Mostre quanto o cliente poderá gastar na sua loja (o limite de gasto), calculado da seguinte forma: [salário x (idade / 1.000)] + 100.


# # ETAPA 3

# # Solicite ao cliente que digite o nome de um produto e o preço dele.


# # Se o valor do produto for menor ou igual a 60% do limite que o cliente tem para gastar, mostre a mensagem “Liberado!”. Se estiver entre 60% e 90%, mostre a mensagem “Liberado ao parcelar em até 2 vezes”. Se estiver entre 90% e 100%, mostre a mensagem “Liberado ao parcelar em 3 ou mais vezes”. Caso contrário, mostre a mensagem “Bloqueado”.


# # Se o valor do produto estiver entre a quantidade de caracteres do seu nome completo e a idade do cliente, mostre que ele terá um desconto igual à quantidade de caracteres do seu primeiro nome.



# # Mostre também ao cliente o valor do produto com o desconto.



# # Coloque o código que você fez nas etapas 1 e 2 dentro de uma única função chamada “obter_limite”. Essa função deverá retornar o limite que o usuário poderá gastar.

# # Coloque o código que você fez na etapa 3 dentro de uma única função chamada “verificar_produto”. Essa função terá como parâmetro de entrada o limite de gasto do cliente.

# # Após o cliente informar os dados dele (pela função “obter_limite”), armazene o limite que ele poderá gastar dentro de uma variável chamada “limite”.

# # Na sequência, pergunte ao usuário quantos produtos deseja cadastrar.

# # Por fim, utilize uma estrutura de repetição (for ou while) por n vezes, com n equivalendo à quantidade de produtos que ele deseja cadastrar.

# # Dentro da sua estrutura de repetição, chame sua função “verificar_produto”, permitindo que o usuário consiga cadastrar todos os produtos e verificar se teria ou não limite sobrando para comprá-los.

def cadastroCliente():

    nomeCliente = input('Qual o seu nome? ')
    cargo = input('Por gentileza, insira seu cargo atual: ')
    salario = int(input('Seu salário: '))
    anoNascimento = int(input('E o ano de seu nascimento: '))
    anoAtual = 2022 

    print(f'\nEssas são as informações que você inseriu. Cargo: {cargo}, Salário: R${salario} e ano de nascimento: {anoNascimento}.\n')

    return nomeCliente, anoAtual, anoNascimento, salario

nomeCliente, anoAtual, anoNascimento, salario = cadastroCliente()

def obter_limite():

    idade = anoAtual - anoNascimento
    limiteDeGasto = (salario * (idade/1000)) + 100

    print(f"O seu limite liberado é a quantia de R${limiteDeGasto}\n")

    print("Análise finalizada!\n")

    return limiteDeGasto

limiteDeGasto = obter_limite()

produtosDisponiveis = ['Mesa', 'Cadeira', 'Pia']


def verificarProduto(limiteDeGasto):

    valorTotal = 0

    while valorTotal <= limiteDeGasto:        

        cadastroProduto = input(f"\nInforme o produto para cadastrar, caso deseje encerrar digite FIM: ")

        if cadastroProduto == "FIM":
            print(f"\nValor final da compra: R${valorTotal}.")
            print(f"\nLimite restante: R${limiteDeGasto - valorTotal}")
            break         

        valorProduto = float(input("\nInsira o valor do produto cadastrado: "))
        
        # while cadastroProduto != len(produtosDisponiveis):
            # print("Produto não cadastrado")

        valorTotal = valorTotal + valorProduto

        print(f"\nProduto {cadastroProduto} R${valorProduto}, soma dos valores em R${valorTotal}, limite restante R${limiteDeGasto - valorTotal}.")          
    
    else:
        print(f"\nExcede limite. Valor total {valorTotal}. Faltam {valorTotal - limiteDeGasto}")        

    return cadastroProduto, valorTotal, valorProduto

cadastroProduto, valorTotal, valorProduto = verificarProduto(limiteDeGasto)

limite60 = valorTotal * 0.60
limite90 = valorTotal * 0.90


# if cadastroProduto in produtosDisponiveis:
#         cadastroProduto = cadastroProduto + 1

if valorTotal < limite60:
    print("\nLiberado!")

elif valorTotal >= limite60 and valorTotal <= limite90:
    print("\nPagamento em até 2X.")

else:
    print("\nParcelamento em até 3X")

def descontoNome():

    lenNome = len(nomeCliente)

    if (valorTotal > lenNome) and (valorTotal < anoNascimento):
        print(f"\nDesconto no produto de {lenNome}%!")
    else:
        print("\nSem desconto.")

    # Mostre também ao cliente o valor do produto com o desconto.

    novoValor = valorTotal / 100
    descNoProduto = (novoValor - valorTotal) * (-1)

    print(f"Novo valor com desconto é de R${descNoProduto}")

    return descNoProduto

desconto = descontoNome()