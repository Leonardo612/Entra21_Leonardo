#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

nome = input('Digite o Nome: ')
sobrenome = input('Digite o Sobrenome: ')
cpf = (input('Digite o cpf: '))
rg = (input('Digite o rg: '))
salario = float(input('Digite o Salario: '))

print(f'''
nome: {nome}
Sobrenome: {sobrenome}
cpf: {cpf}
rg: {rg}
Salario: {'{:.3f}'.format(salario)}'''.format(nome,sobrenome,cpf,rg,salario))

