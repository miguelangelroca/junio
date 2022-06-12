import xml.etree.ElementTree as ET

arbol = ET.parse('colegio.xml')


def colegio(arbol):
    raiz = arbol.getroot()
    grupos = ET.SubElement(raiz, 'grupos')
    alumnos = raiz.findall('alumnos/alumno')
    grupo = None
    for alumno in alumnos:
        edad = int(alumno.get('edad'))
        if grupo is None:
            grupo = ET.SubElement(grupos, 'grupo', {'nivel': str(edad - 5)})
        if int(grupo.get('nivel')) == edad - 5:
            grupo.append(alumno)
        else:
            grupo = ET.SubElement(grupos, 'grupo', {'nivel': str(edad - 5)})
            grupo.append(alumno)
    raiz.remove(raiz.find('alumnos'))
    arbol.write('resultadocolegio.xml')  # return arbol


colegio(arbol)
