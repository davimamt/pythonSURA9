#importar modulos
from modulo import crearTabla
from modulo2 import generarHTML


def filtro1():
    tablaMunicipios=crearTabla()
    tablaBarbosa=tablaMunicipios[tablaMunicipios["Ciudad"]=="Barbosa"]
    generarHTML(tablaBarbosa, "barbosa.html")
    
filtro1()