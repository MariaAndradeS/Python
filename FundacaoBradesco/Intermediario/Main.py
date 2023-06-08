class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Maria", "988315322")
conta = Conta(c1.get_nome(), 2806, 0)

conta.deposito(100)
conta.saque(50)
conta.extrato()