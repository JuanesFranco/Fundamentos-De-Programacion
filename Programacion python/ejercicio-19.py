num1=int(input("ingrese el 1 valor"))
num2=int(input("ingrese el 2 valor"))
num3=int(input("ingrese el 3 valor"))
if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)
