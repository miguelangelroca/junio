nombre = 'Juan Manuel  Perez Sarmiento'


def invertir(nombre):
    nuevonombre = nombre.split('  ')
    if len(nuevonombre) > 1:
        return nuevonombre[1] + ', ' + nuevonombre[0]
    else:
        return nombre


print(invertir(nombre))
