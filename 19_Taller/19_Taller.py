import math
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
    
     
xsumat = sum(x)
xmedia = xsumat/tamaño

ysumat = sum(y)
ymedia = ysumat/tamaño
xy = 0
xx = 0

for j in range (tamaño):
    xy += x[j] * y[j]
    xx += x[j] * x[j]
    

xxmedia = xx/tamaño
xymedia = xy/tamaño

# a1 = m           -  a0 = b
m = (tamaño*xy-xsumat*ysumat)/(tamaño*xx-(xsumat*xsumat))
b = ymedia - m*xmedia

st = 0
for j in range (tamaño):
    st += (y[j]-ymedia)*(y[j]-ymedia)
sr=0
for j in range (tamaño):
    sr  += (y[j]-b-m*x[j])*(y[j]-b-m*x[j])

#desviacion estandar
sy= math.sqrt(st/(tamaño-1))
#error estandar
sy_x = math.sqrt(sr/(tamaño-2))
#coeficiente de correlacion
r = math.sqrt((st-sr)/st)*100
print("La ecuacion de la recta queda de la siguiente manera:")
print(" y =",m,"x +",b)
print("La desviacion estandar (Sy) es  =",sy)
print("El error estandar (Sy_x) es = ",sy_x)
print("El coeficiente de correlacion (r ) es = ",r,"%")
