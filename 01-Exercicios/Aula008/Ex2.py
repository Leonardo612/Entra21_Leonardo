#--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

from cadastrando_pessoas import cadastros
#=== escopo global
enderecos = []

def cadastrar_enderecos(i_d, rua, numero, complemento, bairro, cidade, estado):
    endereco = { 
    'rua': rua,
    'numero': numero,
    'complemento': complemento,
    'bairro': bairro,
    'cidade': cidade,
    'estado': estado,
    'i_d': i_d}
    enderecos.append(endereco)

    for chave, valor in endereco.items():
        if chave == None or valor == '':
            return 'Valores não preenchidos!'
        else: 
            return 'Endereço realizado com sucesso'


i_d = len(cadastros) + 1
rua = input('Digite sua rua: ')
numero = input('Digite seu numero: ')
complemento = input('Digite o complemento: ')
bairro = input('Digite o seu bairro: ')
cidade = input('Digite a sua cidade: ')
estado = input('Digite seu Estado: ')

cadastrar_enderecos(i_d, rua, numero, complemento, bairro, cidade, estado)

for endereco in enderecos:
    print(enderecos)