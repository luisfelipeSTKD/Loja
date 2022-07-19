class Cadastro:

    anoAtual = 2022

    def __init__(self, nome, funcao, salario, anoNascimento):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario
        self.anoNascimento = anoNascimento
        # self.anoAtual = anoAtual

    def fezCadastro(self):
        print(f"Seu nome é {self.nome}, profissão: {self.funcao}, salario: {self.salario:5.2f} e ano de nascimento: {self.anoNascimento}")
        # return self.nome + ' ' + self.funcao + ' ' + self.salario + ' ' + self.anoNascimento
        return self.nome, self.funcao, self.salario, self.anoNascimento

    def limiteDeGasto(self, idade):
        print(f"Seu limite de gasto é de R${self.limiteDeGasto:5.2f} e sua idade é {self.idade}")
        return self.limiteDeGasto, self.idade

            

    @classmethod
    def fazerCadastro(self):
        while 1:
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
    def limiteGasto(self, anoAtual, anoNascimento, salario):
        idade = anoAtual - anoNascimento
        while 2:
            try:
                limiteDeGasto = (salario * (idade / 1000)) + 1000
                return idade, limiteDeGasto
            except:
                break

cadastro1 = Cadastro.fazerCadastro()
cadastro1.fezCadastro()
cadastro1.limiteDeGasto()