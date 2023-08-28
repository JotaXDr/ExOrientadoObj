class ContaBancaria:
    def __init__(self, titular, saldo, numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero

    def deposito(self, depositar):
        self.saldo += depositar

    def sacar(self, saque):
        self.saldo -= saque

    def exibir(self):
        print(f'O saldo atual é: {self.saldo}')


Conta1 = ContaBancaria(titular='Bruno', saldo=1000, numero=3456)

a = int(input('Digite o valor que você deseja sacar: '))

Conta1.sacar(a)
Conta1.exibir()
