def retornar_superficie(lado):
    sup=lado*lado
    return sup


#bloque principal
la=int(input("ingrese el lado del cuadrado"))
superficie=retornar_superficie(la)
print("la superficie del ciadrado es",superficie)

