class ContaSemEncapsulamento:
    def __init__(self, titular, saldo, senha):
        self.titular = titular
        self._saldo = saldo
        self.__senha = senha

    def ver_saldo(self, senha_digitada):
        if senha_digitada == self.__senha:
            print(f"Saldo de {self.titular}: R${self._saldo:.2f}")
        else:
            print("Senha incorreta!")

conta1= ContaSemEncapsulamento("Leo", 1000.00, "123")
conta1.ver_saldo("123")

conta1._saldo = 999_999.99
conta1.__senha = "0000"
conta1.titular = "Novo Titular"

conta1.ver_saldo("0000")