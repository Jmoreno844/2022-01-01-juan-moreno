print("Ingrese la longitud de los vectores")
n = int(input())
a = []
b = []

print("Ingrese los valores del primer vector")
for i in range(n):
    print("El valor #"+str(i+1)+" es:")
    t = int(input())
    a.append(t)

print("Ingrese los valores del segundo vector")
for i in range(n):
    print("El valor #" + str(i+1) + " es:")
    t = int(input())
    b.append(t)

print(a)
print(b)
c=[]


for i in range(n):
    t = (a[i]*b[i])
    c.append(t)

total = 0
for i in range(n):
    total += c[i]

print("El producto escalar de los dos vectores es:",total)



