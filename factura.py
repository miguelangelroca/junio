
def factura():
    with open('factura.txt', 'r') as f:
        lista = []
        total = 0
        for i in f.readlines():
            lista.append(i.rstrip())
        resultado = []
        resultado.append(lista[0] + '  Importe\n')
        resultado.append(lista[1] + '  -------\n')

        for linea in lista[2:]:
            linea = linea.split()
            cantidad = int(linea[0])
            descripcion = linea[1]
            precio = float(linea[2])
            importe = cantidad * precio
            total += importe
            resultado.append(
                f'{cantidad:2} {descripcion:14} {precio:7.2f} {importe:7.2f}\n')
        resultado.append(f'----------------------------------\n')
        resultado.append(f'TOTAL: {total:26.2f}\n')

    with open('resultadofactura.txt', 'w') as f:
        f.writelines(resultado)


factura()
