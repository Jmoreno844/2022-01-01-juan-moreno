import math
import decimal


es = (0.5*10**-8)*100
ea = 100
contador = 2
valoractual  = 1
valoranterior = 1
angulo = math.pi/3

while (es<ea and contador):
    if ((contador%4)==0):
        valoractual +=  ((angulo)**contador)/math.factorial(contador)
    else:
        valoractual -= ((angulo) ** contador) / math.factorial(contador)
    ea = abs((valoractual-valoranterior)/valoractual)*100
    valoranterior = valoractual
    contador += 2

print(valoractual)

