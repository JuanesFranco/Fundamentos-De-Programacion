def largo(cadena):
    return len(cadena)

#bloque principal
nombre1=input("ingrese primer nombre")
nombre2=input("ingrese primer nombre")
la=largo(nombre1)
la2=largo(nombre2)
if la==la2:
    print("la cantidad de letras es igual")
else:
    if la>la2:
        print(nombre1,"es mas largo")
    else:
        print(nombre2,"es mas largo")
