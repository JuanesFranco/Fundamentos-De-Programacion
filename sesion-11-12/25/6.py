def superficie(lado1,lado2):
    superficie=lado1*lado2
    return superficie
print("primer rectangulo")
lado1=int(input("ingrese el lado menor del rectangulo"))
lado2=int(input("ingrese el lado mayor del rectangulo"))
print("sgundo rectangulo")
lado3=int(input("ingrese el lado menor del rectangulo"))
lado4=int(input("ingrese el lado mayor del rectangulo"))
if superficie(lado1,lado2)>superficie(lado3,lado4):
    print("el primer rectangulo es mayor")
else:
    print("el segundo rectangulo es mayor")
