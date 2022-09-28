import pandas as pd

tablasiembra=pd.read_csv('./Siembras.csv')

#4. Datos SantafeAntioquia incluyendo el numero de hectareas sembradas
tablaSantafe= tablasiembra[(tablasiembra["Arboles"]>250) & (tablasiembra["Ciudad"]=="Santa Fe de Antioquia")]

'''print(tablaSantafe)'''

archivoHTML=tablaSantafe.to_html()
archivoTEXTO=open("tablaSantafe.html", "w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()