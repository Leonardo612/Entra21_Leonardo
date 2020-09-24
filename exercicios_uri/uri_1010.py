cod_1,uni_1,preco_uni_1 = input().split()
cod_2,uni_2,preco_uni_2 = input().split()

total_1 = (int(uni_1)*float(preco_uni_1))
total_2 = (int(uni_2)*float(preco_uni_2))
total = (total_1+total_2)

print("VALOR A PAGAR: R$",'{:.2f}'.format(total))