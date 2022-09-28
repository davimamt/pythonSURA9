import pandas as pd

tablasiembra=pd.read_csv('./Siembras.csv')

#3. Datos Caucasia incluyendo el numero de hectareas sembradas
tablaCaucasia= tablasiembra[tablasiembra["Ciudad"]=="Caucasia"]
tablaCaucasia2= tablaCaucasia["Hectareas"].to_frame()

'''print(tablaCaucasia)'''
'''print(type(tablaCaucasia))
print(type(tablaCaucasia2.to_frame()))'''


archivoHTML=tablaCaucasia2.to_html()
archivoTEXTO=open("tablaCaucasia.html", "w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()