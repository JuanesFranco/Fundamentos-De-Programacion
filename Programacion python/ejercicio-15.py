num1=int(input("ingrese 1 numero"))
num2=int(input("ingrese 2 numero"))
num3=int(input("ingrese 3 numero"))
print("el valor mayor de los tres valores ingresados es")
if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)

        
