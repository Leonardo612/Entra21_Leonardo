
#--- Exercício 2  - Funções
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a divisão entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string

4

def divisao():
    num_1 = int(input())
    num_2 = int(input())
    if num_2 == 0:
        print('Divisão não é possivel')
    elif num_2 > 0:
        divisao_dos_numeros = num_1/num_2
        print(f'A divisão entre o numero {num_1} e {num_2} é {divisao_dos_numeros}')
    return divisao

divisao()
