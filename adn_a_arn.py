def adn_a_arn(adn):
    lista = [i for i in adn]
    indice = 0
    for j in lista:
        if j == 'A':
            lista[indice] = 'U'
        if j == 'T':
            lista[indice] = 'A'
        if j == 'G':
            lista[indice] = 'C'
        if j == 'C':
            lista[indice] = 'G'
        indice += 1
    lista = ''.join(lista)
    return lista


print(adn_a_arn('GCGTAC'))
print(adn_a_arn('ATTAGCGCGATATACGCGTAC'))
