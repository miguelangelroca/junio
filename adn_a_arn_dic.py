def adn_a_arn(adn):
    dic = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    res = []
    for i in adn:
        res.append(dic.get(i))
    return ''.join(res)


print(adn_a_arn('GCGTAC'))
print(adn_a_arn('ATTAGCGCGATATACGCGTAC'))
