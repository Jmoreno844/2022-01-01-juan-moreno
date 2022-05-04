tamaño = int(input("Ingrese el tamaño de la tabla"))
print("Creando la tabla")
x = []
y = []

for a in range(tamaño):
    print("----")
    print("Ingrese el valor", (a + 1), "de x")
    x.append(float(input()))
    print("----")
    print("Ingrese el valor", (a + 1), "de y")
    y.append(float(input()))

for j in range(tamaño):
    x[j] = 1/x[j]
    y[j] = 1/y[j]

xsumat = sum(x)
xmedia = xsumat / tamaño

ysumat = sum(y)
ymedia = ysumat / tamaño
xy = 0
xx = 0
for j in range(tamaño):
    xy += x[j] * y[j]
    xx += x[j] * x[j]

m = (tamaño * xy - xsumat * ysumat) / (tamaño * xx - (xsumat * xsumat))
b = ymedia - m * xmedia

alpha = 1/b
beta = m/b


print("La ecuacion de la recta queda de la siguiente manera:")
print(" y =", alpha, "*(x /",beta,"+ x)")