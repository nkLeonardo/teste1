class Carro:
    def __init__(self, marca, modelo, cor, ano):
        # Construtor correto: atribui atributos à instância
        self.marca = marca
        self.modelo = modelo
        self.cor = cor 
        self.ano = ano


    def Acelerar(self):
        print(f"O carro {self.marca} {self.modelo} {self.cor} {self.ano} está acelerando")
    def Frear(self):
        print(f"O carro {self.marca} {self.modelo} {self.cor} {self.ano} está freando")
# Criando dois objetos diferentes
carro1 = Carro("Hyundai", "Creta", "Preto", "2020")
carro2 = Carro("Hyundai", "Tcuson", "Azul", "2017")

# Chamando métodos
carro1.Acelerar()
carro2.Frear()  