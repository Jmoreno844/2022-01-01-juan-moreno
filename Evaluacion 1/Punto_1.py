def union(a,b):
    c = set()
    for element in a:
        c.add(element)
    for element in b:
        c.add(element)
    return c

def diferencia(a,b):
    c = set()
    for element in a:
        c.add(element)
    for element in b:
        c.discard(element)
    return c

def inter(a,b):
    a = set(a)
    b= set(b)
    c = set()
    c = a.intersection(b)
    return c

def difsim(a,b):
    a = set(a)
    b= set(b)
    un = a.union(b)
    c=set()
    inn = a.intersection(b)
    c = un.difference(inn)
    return  c

A = {2,4,6,8,12,24,48}
B = {3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27}
C = {6,9,12,15,18,21,24,27,30,33}
D = {2,3,5,7,11,13,17,19,23,29,31,37,41,43}


print(inter(difsim(B,D),union(A,C)))
print(difsim(inter(diferencia(A,D),C),union(B,C)))
print(diferencia(union(diferencia(A,C),inter(B,D)),union(A,union(B,C))),"SET 3 VACIO")
