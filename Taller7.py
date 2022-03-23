import math
import decimal


es = (0.5*10**-7)*100
ea = 100
contador = 1
valoractual  = 1
valoranterior = 1
x = 1.75

while (es<ea):
    if ((contador%2)==0):
        valoractual +=  ((x)**contador)/math.factorial(contador)
    else:
        valoractual -= ((x) ** contador) / math.factorial(contador)
    ea = abs((valoractual-valoranterior)/valoractual)*100
    valoranterior = valoractual
    contador += 1

print("Primer ecuacion:\nValor: ",valoractual,"\nUltimo error aproximado: ",ea,"\nNumero de iteraciones: ",(contador-1))

ea = 100
contador = 1
denominador  = 1
valoranterior = 1
valoractual = 1



while (es<ea):
    denominador += ((x)**contador)/math.factorial(contador)
    valoractual = 1/denominador
    ea = abs((valoractual-valoranterior)/valoractual)*100
    valoranterior = valoractual
    contador += 1

print("Segunda ecuacion:\nValor: ",valoractual,"\nUltimo error aproximado: ",ea,"\nNumero de iteraciones: ",(contador-1))