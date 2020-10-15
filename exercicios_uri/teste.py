
idades_menores = []
nome_menores = []
for i in range(3):
    idade = int(input())
    nome = (input())
    if idade < 18:
        print(f"Mais um menor de idade {i+1}")
        idades_menores.append(idade)
        nome_menores.append(nome)

print(f"Idades dos menores {idades_menores}")
print(f"Nomes dos menores {nome_menores}")

    