from funcionario import Funcionario

functionary= Funcionario('Matheus', 'matheus@blablabla.com.br')

functionary.cadastro_hora('Jan', 300)
functionary.cadastro_hora('Fev', 200)
functionary.cadastro_salario_hora('Jan', 30)
functionary.cadastro_salario_hora('Fev', 20)

print(functionary)
print(functionary.calcula_salario('Jan'))
print(functionary.calcula_salario('Fev'))

