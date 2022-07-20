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
        print(f"Seu limite de gasto é de R${self.limiteDeGasto} e sua idade é {self.idade}")
        return self.limiteDeGasto, self.idade

    @classmethod
    def fazerCadastro(self):

        global salario
        global anoNascimento

        while True:
            try:
                nome = input("Insira seu nome: ")
                funcao = input("Insura sua profissão: ")
                salario = int(input("Seu salário: "))
                anoNascimento = int(input("Ano de nascimento: "))
                return self(nome, funcao, salario, anoNascimento)
            except:
                print("Alguma informação está errada")
                # continue
                break

    @classmethod
    def obterLimiteGasto(self):

        global anoAtual

        while True:
            try:
                anoAtual = 2022
                idade = anoAtual - anoNascimento

                if idade < 18:
                    print("Pessoa menor de idade")
                    break

                limiteDeGasto = (salario * (idade / 1000)) + 1000
                return idade, limiteDeGasto
            except:
                break

cadastro1 = Cadastro.fazerCadastro()
cadastro1.fezCadastro()
cadastro1.limiteDeGasto()