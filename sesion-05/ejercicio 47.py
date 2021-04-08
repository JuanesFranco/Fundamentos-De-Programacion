n=int(input("ingrese la cantidad de triangulos a procesar"))
cantidad=0
for f in range(n):
    altura=int(input("ingrese la altura"))
    base=int(input("ingrese el valor"))
    superficie=base*altura/2
    print("la superficie del triangulo es de",superficie)
    if superficie>12:
         cantidad=cantidad+1
print("la cantidad de triangulos con superficie mayor a 12 es de",cantidad)    
