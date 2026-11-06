#Criando uma classe
class Cliente:
   # inserindo um metodo construtor
    def __init__(self, n, fone):
        #inserindo atributos da classe com modificador de acesso
        self._nome = n
        self._telefone = fone

#DANDO ACESSO A MÉTODOS PRIVADOS

# Método get
def get_nome(self):
    return self._nome

#método set
def set_nome(self, nome):
    self._nome = nome


