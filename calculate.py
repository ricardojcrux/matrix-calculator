import numpy as np

def numpy_matriz(lista : list):
    matriz = np.array(lista)
    determ = np.linalg.det(matriz)
    return matriz, int(determ)

def inversa(matriz, determ):
    if determ == 0:
        return 'La matriz no tiene inversa'
    else:
        return (np.linalg.inv(matriz)*determ)