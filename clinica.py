import xml.etree.ElementTree as ET


def cita():

    arbol = ET.parse('clinica.xml')
    raiz = arbol.getroot()

    for socio in raiz.findall('socios/socio'):
        if socio.find('compania').text == "Mapfre":
            socio_selec = socio

    for medico in raiz.findall('medicos/medico'):
        if medico.find('companias/compania').text == "Mapfre":
            medico_selec = medico

    ET.SubElement(socio_selec, 'cita', {'medico': medico_selec.get('id')})

    arbol.write('prueba.xml')
    return arbol


print(cita())
