

# precoProduto = float(input("Insira o preço: "))

# porcento60 = precoProduto * 0.60
# porcento90 = precoProduto * 0.90

# # print(porcento60)
# print(porcento90)
    
# # nota = int(input("Digite uma nota: "))

# if precoProduto < porcento60:
#     print("Reprovado")
# elif precoProduto > porcento60 < porcento90:
#     print("Recuperação")
# else:
#     print("Aprovado")

# nome = input('Insira seu nome: ')

# print(len(nome))

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

    print(f"O seu limite lirado é a quantia de R${limiteDeGasto}\n")

    print("Análise finalizada!\n")

    return limiteDeGasto

limiteDeGasto = obter_limite()

def verificar_produto(limiteDeGasto):

    if totalProdutos in produtosDisponiveis:
        qtdProdutos = int(input("Quantos"))

    totalProdutos = 0
    # limiteMax = 0
    while totalProdutos < limiteDeGasto:
        produtosCadastrados = input("Informe os produtos para cadastrar: ")
        print(f"\nProdutos cadastrados {totalProdutos + 1}")

        # Dentro da sua estrutura de repetição, chame sua função “verificar_produto”, permitindo que o usuário consiga cadastrar todos os produtos e verificar se teria ou não limite sobrando para comprá-los.

        totalProdutos, limiteMax = verificar_produto(limiteDeGasto)
    # limite = limiteDeGasto
    # produto = input("Qual produto gostaria de comprar? ")
    precoProduto = float(input("\nE o valor dele em reais: "))

    limite60 = float(precoProduto * 0.60)
    limite90 = float(precoProduto * 0.90)

    if precoProduto <= limite60:
        print("\nLiberado!")
    elif (precoProduto >= limite60) and (precoProduto <= limite90):
        print("\nPermitido parcelamento em até duas vezes.")
    else:
        print("\nPermitido parcelamento em três vezes ou mais.")

    return produto, precoProduto

produto, precoProduto = verificar_produto(limiteDeGasto)

# Coloque o código que você fez nas etapas 1 e 2 dentro de uma única função chamada “obter_limite”. Essa função deverá retornar o limite que o usuário poderá gastar.




# Coloque o código que você fez na etapa 3 dentro de uma única função chamada “verificar_produto”. Essa função terá como parâmetro de entrada o limite de gasto do cliente.


# Após o cliente informar os dados dele (pela função “obter_limite”), armazene o limite que ele poderá gastar dentro de uma variável chamada “limite”.

limite = obter_limite()

# print(limite)

# Por fim, utilize uma estrutura de repetição (for ou while) por n vezes, com n equivalendo à quantidade de produtos que ele deseja cadastrar.

produtosDisponiveis = ['Mesa', 'Cadeira', 'Pia']

print("Quais produtos deseja cadastrar? ")
