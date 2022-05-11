
tamaño = int(input("Ingrese el tamaño de la tabla"))
print("Creando la tabla")
x = []
y = []

for a in range (tamaño):
    print("----")
    print("Ingrese el valor",(a+1),"de x")
    x.append(float(input()))
    print("----")
    print("Ingrese el valor",(a+1),"de y")
    y.append(float(input()))

numero = float(input("Ingrese el valor de x a encontrar"))
indice = 0
while(numero>x[indice]):
    indice += 1
indice -=1
x0 = x[indice]
x1 = x[indice+1]
x2 = x[indice-1]
x3 = x[indice+2]
f0 = y[indice]
f1 = y[indice+1]
f2 = y[indice-1]
f3 = y[indice+2]

grado1 = (f0*(numero-x1)/(x0-x1))    + (f1*(numero-x0)/(x1-x0)) 
grado2 = (f0*(numero-x1)*(numero-x2)/((x0-x1)*(x0-x2)))   +  (f1*(numero-x0)*(numero-x2)/((x1-x0)*(x1-x2)))  + (f2*(numero-x0)*(numero-x1)/((x2-x0)*(x2-x1)))
grado3 = (f0*(numero-x1)*(numero-x2)*(numero-x3)/((x0-x1)*(x0-x2)*(x0-x3))) + (f1*(numero-x0)*(numero-x2)*(numero-x3)/((x1-x0)*(x1-x2)*(x1-x3))) + \
         (f2*(numero-x0)*(numero-x1)*(numero-x3)/((x2-x0)*(x2-x1)*(x2-x3))) + (f3*(numero-x0)*(numero-x1)*(numero-x2)/((x3-x0)*(x3-x1)*(x3-x2)))

print("--------Los valores son --------")
print("Grado 1: ",grado1,"\nGrado 2: ",grado2,"\nGrado 3: ",grado3)