import csv
import pandas as pd

tabla= pd.read_csv("./Siembras.csv")

#tabla estadisticas 
tablaEstadisticas=tabla.describe()


#solo obtener medias de la tabla estadistica (SOLO UNA FILA)
tablaMedias=tablaEstadisticas.loc[['mean']]

#Solo obtener los datos de una columna
tablaMediasArboles= tablaMedias["Arboles"].to_frame()

print(tablaEstadisticas)