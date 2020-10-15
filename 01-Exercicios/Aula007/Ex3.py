#--- Exercício 3  - Funções
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)

def media():
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    media_dos_nums = (num_1+num_2+num_3)/3
    print(f"A média dos numeros {num_1}, {num_2} e {num_3} é "'{:.1f}'.format(media_dos_nums))
    return media

media()
