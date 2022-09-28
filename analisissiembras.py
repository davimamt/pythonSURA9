import pandas as pd

tablasiembra=pd.read_csv('./Siembras.csv')

#1. Datos Municipios
tablaDatosMunicipios= tablasiembra[(tablasiembra["Ciudad"]=="Andes") | (tablasiembra["Ciudad"]=="Barbosa") | (tablasiembra["Ciudad"]=="Caldas") | (tablasiembra["Ciudad"]=="Támesis") | (tablasiembra["Ciudad"]=="Yarumal")]

archivoHTML=tablaDatosMunicipios.to_html()
archivoTEXTO=open("tablaDatosMunicipios.html", "w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
