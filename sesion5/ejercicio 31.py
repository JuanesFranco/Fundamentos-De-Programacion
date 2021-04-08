x=1
cantidad=0
n=int(input("ingrese la cantidad de piezas a procesar"))
while x<=n:
    largo=float(input("ingrese la medida de la pieza"))
    if largo>=1.20 and largo<1.30:
        cantidad=cantidad+1
    x=x+1
print("cantidad de piezas aptas",cantidad)
