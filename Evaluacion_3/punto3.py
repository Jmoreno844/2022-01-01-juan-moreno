import numpy as np
from scipy import linalg
try:
    m = np.matrix([[4,0,-2],[2,0,4],[6,2,-2]])
    print("La matriz inversa es:")
    print(linalg.inv(m))
except:
    print("Singular Matrix, Inverse not possible.")
