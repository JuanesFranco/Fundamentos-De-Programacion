def mostrar_perimetro(lado):
    per=lado*4
    print("el perimetro es",per)

def mostrar_superficie(lado):
    sup=lado*lado
    print("la superficie es:",sup)

def cargar_lado():
    la=int(input("ingrese el lado"))
    res=int(input("ingrese 1 para calcular el lado o 2 para calcular el perimetro"))
    if res==1:
        mostrar_perimetro(la)
    if res==2:
        mostrar_superficie(la)
    
#bloque principal
cargar_lado()
