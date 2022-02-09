
conjuntoa = set()
conjuntob = set()

print("Ingrese el tamaño del conjunto A")
tam = int(input())
print("Ingrese los elementos del conjunto A")
for i in range(tam):
    temporal = int(input("-> "))
    conjuntoa.add(temporal)

print("Ingrese el tamaño del conjunto B")
tam = int(input())
print("Ingrese los elementos del conjunto B")
for i in range(tam):
    temporal = int(input("-> "))
    conjuntob.add(temporal)
pasa = True

while pasa:
    opcion = int(input("Ingrese la opcion a realizar\n1.Union\n2.Interseccion\n3.Diferencia\n4.Diferencia simetrica\n"))
    if opcion==1:
        print("El resultado de la operacion es",conjuntoa.union(conjuntob))
        pasa=False
    elif opcion==2:
        print("El resultado de la operacion es",conjuntoa.intersection(conjuntob))
        pasa=False
    elif opcion==3:
        print("El resultado de la operacion es",conjuntoa.difference(conjuntob))
        pasa=False
    elif opcion==4:
        print("El resultado de la operacion es", (conjuntoa.union(conjuntob)).difference(conjuntoa.intersection(conjuntob)))
        pasa = False
    else:
        print("Opcion incorrecta")


