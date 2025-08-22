class ContaSemEncapsulamento:
    def __init__(self, titular, saldo, senha):
        self.titular = titular
        self.saldo = saldo
        self.senha = senha

    def ver_saldo(self, senha_digitada):
        if senha_digitada == self.senha:
            print(f"Saldo de {self.titular}: R${self.saldo:.2f}")
        else:
            print("Senha incorreta!")

conta1= ContaSemEncapsulamento("Leo", 1000.00, "123")
conta1.ver_saldo("123")

conta1.saldo = 999_999.99
conta1.senha = "0000"
conta1.titular = "Novo Titular"

conta1.ver_saldo("0000")