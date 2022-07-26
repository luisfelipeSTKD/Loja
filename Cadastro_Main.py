# from threading import local


from tracemalloc import stop


class Cadastro:

    def __init__(self, nome, funcao, salario, anoNascimento):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario
        self.anoNascimento = anoNascimento

    def fezCadastro(self):
        print(f"\nSeu nome é {self.nome}, profissão {self.funcao}, salario: R${self.salario} e o ano de nascimento {self.anoNascimento}")

    @classmethod
    def fazerCadastro(self):

        global anoNascimento
        global salario

        while 1:
            try:
                nome = input("Insira seu nome: ")
                funcao = input("Insira sua profissão: ")
                salario = int(input("Seu salário: "))
                anoNascimento = int(input("Ano de nascimento: "))

                return self(nome, funcao, salario, anoNascimento)
            except:
                continue

class LimiteDeGasto:

    global anoAtual
    anoAtual = 2022

    def __init__(self, calculaLimite, idade):
        self.calculaLimite = calculaLimite
        self.idade = idade

    def limiteDeGasto(self):
        print(f"\nSeu limite de gasto é de R${self.calculaLimite} e a sua idade é de {self.idade}")

    @classmethod
    def limiteCalculado(self):

        global calculaLimite

        while 1:
            try:
                idade = anoAtual - anoNascimento
                calculaLimite = (salario * (idade / 1000)) + 1000

                if idade < 18:
                    print("##################")
                    print("Pessoa menor de idade!")
                    print("##################")
                    break

                return self(calculaLimite, idade)
            except:
                continue

class CadastraProduto:

    def __init__(self, produto, precoProduto, produtosDisponiveis, valorTotal):
        self.produto = produto
        self.precoProduto = precoProduto
        self.produtosDisponiveis = produtosDisponiveis
        self.valorTotal = valorTotal

    global produtosDisponiveis
    produtosDisponiveis = ["Mesa", "Pia", "Janela"]

    def mostraProdutos(self):
        print(f"Os produtos cadastrados são {self.produto} com valor total de R${self.precoProduto}")

    @classmethod
    def cadastraProduto(self):
        global precoProduto
        global valorTotal

        prodCadastrados = 0
        # valorTotal = valorTotal + precoProduto

        while valorTotal <= calculaLimite:
            try:
                produto = input("Qual produto deseja cadastrar? ")
                valorTotal = valorTotal + precoProduto

                if produto == "FIM":
                    print(f"\nValor final da compra: R${valorTotal}")
                    print(f"\nLimite restante: R${calculaLimite - valorTotal}")
                    pass

                precoProduto = int(input("Qual o valor da etiqueta? "))
                
                prodCadastrados = prodCadastrados + produto

                return self(produto, precoProduto)
            except:
                continue
    
    @classmethod
    def parcelamento(self):

        desc60 = int(precoProduto * 0.60)
        desc90 = int(precoProduto * 0.90)

        while 1:
            try:
                if precoProduto <= desc60:
                    print("\nLiberado!")
                elif (precoProduto >= desc60) and (precoProduto <= desc90):
                    print("\nPermitido parcelamento em até duas vezes.")
                else:
                    print("\nPermitido parcelamento em três vezes ou mais.")

                return self(precoProduto)
            except:
                continue

cadastro1 = Cadastro.fazerCadastro()
cadastro1.fezCadastro()
limite1 = LimiteDeGasto.limiteCalculado()
limite1.limiteDeGasto()
cadastroProduto1 = CadastraProduto.cadastraProduto()
cadastroProduto1.mostraProdutos()
cadastroProduto1.parcelamento()