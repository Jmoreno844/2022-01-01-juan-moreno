from math import e, factorial

contador = 0
valor = 0
h=0.005
x = 0.77
ea = 100
valoranterior = 1
for i in range (0,16):
    
    if((i%2)==0):
        valor += (e**-x)/factorial(i)*(h**i)
    if((i%2)!=0):
        valor -= (e**-x)/factorial(i)*(h**i)
    ea = abs((valor-valoranterior)/valoranterior)*100
    valoranterior = valor
    print("Orden: ",i,"\nValor: ",valor,"\nError: ",ea)
    