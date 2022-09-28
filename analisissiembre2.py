import pandas as pd

tablasiembra=pd.read_csv('./Siembras.csv')

#2. Datos Medellin ordenados de mayor a menor
tablaMedellin= tablasiembra[tablasiembra["Ciudad"]=="Medellín"].sort_values("Arboles", ascending=False)
'''print(tablaMedellin)'''

archivoHTML=tablaMedellin.to_html()
archivoTEXTO=open("tablaMedellin.html", "w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
