class Conta:
    def __init__(self,titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = 0


    @property
    def get_saldo(self):
        return self._saldo

    @saldo.setter
    def set_saldo(self,saldo):
        if (saldo < 0):
            print("Saldo insuficiente")
        else:
            self._saldo = saldo

    def saque(self,valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def debosita(self,valor):
        self.saldo += valor

    def extrato(self):
        print("CLIENTE:",self._titular)
        print("SALDO", self._saldo)