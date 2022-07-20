class Cadastro:

    def __init__(self, nome, funcao, salario, anoNascimento, idade=0):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario
        self.anoNascimento = anoNascimento
        self.idade = idade
        # self.anoAtual = anoAtual

    def fezCadastro(self):
        print(f"Seu nome é {self.nome}, profissão: {self.funcao}, salario: {self.salario} e ano de nascimento: {self.anoNascimento}")
        # return self.nome + ' ' + self.funcao + ' ' + self.salario + ' ' + self.anoNascimento
        return self.nome, self.funcao, self.salario, self.anoNascimento

    def limiteDeGasto(self):
        print(f"Seu limite de gasto é de R${limiteLiberado} e sua idade é {self.idade}")
        return limiteLiberado, self.idade

    @classmethod
    def fazerCadastro(self):

        global salario
        global anoNascimento

        while True:
            try:
                nome = str(input("Insira seu nome: "))
                funcao = str(input("Insira sua profissão: "))
                salario = int(input("Seu salário: "))
                anoNascimento = int(input("Ano de nascimento: "))
                return self(nome, funcao, salario, anoNascimento)
            except:
                print("Alguma informação está errada")
                # continue
                break

    @classmethod
    def obterLimiteGasto(self):
        
        anoAtual = 2022

        # self.idade = idade
        # self.limiteLiberado = limiteLiberado

        # idade = anoAtual - anoNascimento
        # limiteLiberado = (salario * (idade/1000)) + 1000

        # if idade < 18:
        #     print("Pessoa menor de idade.")

        # return self(idade, limiteLiberado)

        # global anoAtual
        # global idade
        global limiteLiberado

        # anoAtual = 2022
        # idade = anoAtual - anoNascimento
        # limiteDeGasto = (salario * (idade / 1000)) + 1000

        # if idade < 18:
        #     print("Pessoa menor de idade")

        while True:
            try:
                anoAtual = 2022
                calculaIdade = anoAtual - anoNascimento
                idade = calculaIdade

                if idade < 18:
                    print("Pessoa menor de idade")
                    break

                limiteLiberado = (salario * (idade / 1000)) + 1000
                return idade, limiteLiberado
            except:
                break

cadastro1 = Cadastro.fazerCadastro()
cadastro1.fezCadastro()
cadastro1.limiteDeGasto()