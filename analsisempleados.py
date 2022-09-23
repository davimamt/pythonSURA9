from tkinter import W
import pandas as pd

tablaempleados=pd.read_csv('./empleados.csv')
#print(tablaempleados)


#Filtro 1 quiero obtener todos los datos de los analistas 1
''''
tablaanalistas1=tablaempleados[tablaempleados["cargo"]=="analista1"].head(50)
archivoHTML=tablaanalistas1.to_html()
archivoTEXTO=open("datosanalistas1.html", "w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''

#Filtro 2
tablaanalistas2=tablaempleados[(tablaempleados["salario"]>5500000) & (tablaempleados["cargo"]=="analista2")].head(50)
archivoHTML=tablaanalistas2.to_html()
archivoTEXTO=open("datosanalistas2.html", "w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()

