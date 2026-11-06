class Funcionario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.horas = {}  # dicionario das horasdo mes em questão
        self.salario_hora = {}  # salario relativo as ho ras do mes

    def cadastro_hora(self, mes, horas):
        if (mes not in self.horas):
            self.horas[mes] = horas

    def cadastro_salario_hora(self, mes, valor):
         if (mes not in self.salario_hora):
            self.salario_hora[mes] = valor

    def calcula_salario(self, mes):
            if (mes not in self.horas) or (mes not in self.salario_hora):
                print('Mês inexistente')
            else:
                return self.horas[mes] * self.salario_hora[mes]

    def _repr_(self):

         return f'Funcionario: {self.nome}, \nEmail: {self.email}, \nHoras: {self.salario_hora},\nsalario_hora: {self.salario_hora}'

