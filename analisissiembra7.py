import pandas as pd

tablasiembra=pd.read_csv('./Siembras.csv')

#6. Los Datos de CARAMANTA
tablaDatosCaramanta= tablasiembra[(tablasiembra["Ciudad"]=="Caramanta") ]

#print(tablaDatosCaramanta)

archivoHTML=tablaDatosCaramanta.to_html()
archivoTEXTO=open("tablaDatosCaramanta.html", "w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()