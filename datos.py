with open('datos.txt', 'r') as f:
    datos = f.readlines()
    res = 0
    ant = 0
    salida = []
    for i in datos:
        clean = i.strip()
        res += int(clean)
        ant = res
        salida.append(f'{clean:9} {str(ant)}\n')
    salida.append('-------------\n')
    salida.append(f'SUMA:  {res:6}')
with open('resultadodatos.txt', 'w') as f:
    f.writelines(salida)
