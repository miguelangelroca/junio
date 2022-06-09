import xml.etree.ElementTree as ET


def shows():

    arbol = ET.parse('shows.xml')
    raiz = arbol.getroot()

    res = {}

    for show in raiz.findall('pelicula'):
        titulo = show.find('titulo').text
        genero = show.find('genero').text
        if genero == 'Fantasía':
            res[titulo] = None

    for show in raiz.findall('serie'):
        titulo = show.find('titulo').text
        genero = show.find('genero').text
        if genero == 'Fantasía':
            res[titulo] = len(show.findall('.//episodio'))

    return res


print(shows())
