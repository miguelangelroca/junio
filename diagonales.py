matriz = {(0, 0): 11, (0, 1): 5, (0, 2): 3,
          (1, 0): 9, (1, 1): 8, (1, 2): 2,
          (2, 0): 6, (2, 1): 7, (2, 2): -12}

# Realizar la suma absoluta de las diagonales de la matriz.


def diagonales(matriz):
    principal, secundaria = 0, 0
    for i, j in matriz:
        if i == j:
            principal += matriz[i, j]
        if i+j == max(matriz)[0]:
            secundaria += matriz[i, j]
    return abs(principal - secundaria)


print(diagonales(matriz))


# def diagonales2(matriz):
#     principal = sum(matriz[i] for i in matriz if i[0] == i[1])
#     secundaria = sum(matriz[j] for j in matriz if j[0] + j[1] == max(matriz)[0])
#     return abs(principal - secundaria)


# print(diagonales2(matriz))
