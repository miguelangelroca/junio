def intercambiar():
    with open('intercambiar.txt', 'r') as f:
        datos = []
        contador = 0
        for i in f.readlines():
            datos.append([])
            for e in i:
                datos[contador].append(e)
            contador += 1
        for dato in datos:
            for i in range(1, 10):
                if str(i) not in dato:
                    dato[dato.index('*')] = str(i)
        with open('resultadointercambiar.txt', 'w') as f:
            for dato in datos:
                f.writelines(dato)


intercambiar()
