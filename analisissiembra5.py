import pandas as pd

tablasiembra=pd.read_csv('./Siembras.csv')

#5. Los Datos de la veredas Rio Arriba y Salazar de Belmira
tablaDatosVereda= tablasiembra[(tablasiembra["Vereda"]=="Rio Arriba") | (tablasiembra["Vereda"]=="La Salazar") ]

'''print(tablaDatosVereda)'''

archivoHTML=tablaDatosVereda.to_html()
archivoTEXTO=open("tablaDatosVereda.html", "w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()