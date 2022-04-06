import copy
import numpy as np
def prodesca(a,b,n):
    print(a)
    print(b)
    c = []

    for i in range(n):
        t = (a[i] * b[i])
        c.append(t)

    total = 0
    for i in range(n):
        total += c[i]
    return total

print("Ingrese la cantidad de filas del vector A")
ia = int(input())
print("Ingrese la cantidad de columnas del vector A")
ib = int(input())

print("Ingrese la cantidad de filas del vector B")
ic = int(input())
print("Ingrese la cantidad de columnas del vector B")
id = int(input())

ej = []
a = []
b= []
print("-----------------------")
print("Vector A")


for i in range(ia):
    
    ej = []
    for x in range(ib):

        print("Ingrese el valor #"+str(x+1)+" de la columna",(i+1))
        t = int(input())
        ej.append(t)
    a.append(ej)
   
print("-----------------------")
print("Vector B")

for i in range(ic):
    ej = []
    for x in range(id):

        print("Ingrese el valor #"+str(x+1)+" de la columna",(i+1))
        t = int(input())
        ej.append(t)
    b.append(ej)
print("-----------------------")


copiaa = copy.deepcopy(a)
copiab = copy.deepcopy(b)


print("Punto A:")
for i in range(ia):
    for j in range(ib):
        copiaa[i][j] = (copiaa[i][j])*3

for i in range(ia):
    print(copiaa[i])

print("-----------------------")

print("Punto B:")
for i in range(ic):
    for j in range(id):
        copiab[i][j] = (copiab[i][j])*4

for i in range(ic):
    print(copiab[i])

print("-----------------------")


print("Punto C:")
if (ia==ic and ib==id):
    c = copy.deepcopy(a)
    for i in range(ic):
        for x in range(id):
            c[i][x] = (a[i][x])+(a[i][x])
    for i in range(ic):
        print(c[i])
else:
    print("La suma de las matrices no es compatible")
print("-----------------------")
print("Punto D:")
if(ib==ic):
    d=[]
    da = np.array(a)
    db = np.array(b)
    print(np.matmul(da, db))
    
    for r in d:
        print(r)