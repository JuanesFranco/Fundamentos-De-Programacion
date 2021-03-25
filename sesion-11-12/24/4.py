def cantidad_vocales(cadena):
    cant=0
    for x in range(len(cadena)):
        if cadena[x]=="a" or cadena[x]=="e" or cadena[x]=="i" or cadena[x]=="o" or cadena[x]=="u":
            cant=cant+1
    print("cantidad de vocales total de la palabra",cadena,"es",cant)

#bloque principal
cantidad_vocales("administracion")
cantidad_vocales("hola mundo")
cantidad_vocales("hola")
