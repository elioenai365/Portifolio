class Main:
    pass

print("Hello World")
print("Hello World")
print("Hello World")

#impotação da classe
from Cliente import Cliente

from Conta import Conta



c1= Cliente("João", "111445654-465486546")
conta= Conta(c1.get_nome(), 6565, 0)

conta.debosita(100)
conta.saque(50)
conta.extrato()
