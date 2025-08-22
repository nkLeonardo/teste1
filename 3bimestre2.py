class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def Apresentar(self):
        print(f"Meu nome é {self.nome}, tenho {self.idade} anos e moro no {self.cidade}")
pessoa1 = Pessoa("Thiego", "16", "lixão")
pessoa2 = Pessoa("Luiz", "16", "Ermelino")

pessoa1.Apresentar()
pessoa2.Apresentar()