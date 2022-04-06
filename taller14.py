import copy

def imprimirEcuaciones(a, b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(str(a[i][j]), end=" ")
        
        print("| " + str(b[i]))



def gaussJordan(a, b):
    aAux = copy.deepcopy(a)
    bAux = copy.deepcopy(b)

    n = len(bAux)

    print("Ecuaciones")
    imprimirEcuaciones(aAux, bAux)
    print()

    #Se construye la matriz identidad
    

    for i in range(n):
        #Reducción
        if(aAux[i][i]==0):
                for x in range((i+1),n):
                    if(aAux[x][i]!=0):
                        temp1 = aAux[i]
                        aAux[i]=aAux[x]
                        aAux[x]=temp1
                        temp1 = bAux[i]
                        bAux[i]=bAux[x]
                        bAux[x]=temp1
                        break
        for j in range(n):
            
            
            
            if i != j:
                fact = -aAux[j][i] / aAux[i][i]

                for k in range(n):
                    aAux[j][k] += (aAux[i][k] * fact)

                bAux[j] += (bAux[i] * fact)
                
            

            print("Reducción " + str(i + 1))
            imprimirEcuaciones(aAux, bAux)
            print()
    for i in range(n):
                if (aAux[i][i]!=1):
                    bAux[i] = bAux[i]/aAux[i][i]
                    aAux[i][i] = aAux[i][i]/aAux[i][i]
    return bAux


#Programa principal
a = [[0, 0, 3], [3, 4, 3], [4, 1, 0]]
b = [2.5, 11.5, 15]

x = gaussJordan(a, b)

#Se imprimen los resultados
for i in range(len(x)):
    print("x" + str(i + 1) + " = " + str(x[i]))

print()

#Se imprimen las pruebas
for i in range(len(x)):
    test = 0;
    for j in range(len(x)):
        test += a[i][j] * x[j]
    test -= b[i]
    print("test " + str(i + 1) + " = " + str(test))