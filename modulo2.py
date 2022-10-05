def generarHTML(tabla, nombreArchivo):
    html=tabla.to_html()
    archivo=open(nombreArchivo, "w", encoding="utf-8")
    archivo.write(html)
    archivo.close()
    