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

A = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
B = {2,4,6,8,10,12,14,16,18,20,22,24,26,28}
C = {2,5,8,9,11,15,17,19,21}
D = {2,3,5,7,11,13,17,19,23,29,31,37}


print(difsim(C,inter(A,D)))
print(inter(union(B,D),A))
print(diferencia(B,difsim(A,D)))
print(inter(union(B,C),diferencia(A,D)))




