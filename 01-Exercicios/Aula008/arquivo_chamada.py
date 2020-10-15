from Ex1 import cadastros

def cadastros(nome:str, sobrenome:str, idade:int):
    dados = {}
    dados['nome'] = nome
    dados['sobrenome'] = sobrenome
    dados['idade'] = idade
    if idade < 18:
        return 'Idade não permitida'
    pessoas.append(dados)
    id_cadastros = len(pessoas)
    return f'id = {id_cadastros}'