a,b,c = input().split()     
a = float(a)
b = float(b)
c = float(c)
pi = 3.14159

aR = a*c/2
bR = pi*c**2
cR = (a+b)*c/2
dR = b*b
eR = a*b

print("TRIANGULO:",'{:.3f}'.format(aR))
print("CIRCULO:",'{:.3f}'.format(bR))
print("TRAPEZIO:",'{:.3f}'.format(cR))
print("QUADRADO:",'{:.3f}'.format(dR))
print("RETANGULO:",'{:.3f}'.format(eR))

