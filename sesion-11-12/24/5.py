def ordenar_imprimir(v1,v2,v3):
    if v1>v2 and v1>v2:
        if v2>v3:
            print(v1,v2,v3)
        else:
            print(v1,v3,v2)
    else:
        if v2>v3:
            if v1>v3:
                print(v2,v1,v3)
            else:
                print(v2,v3,v1)
        else:
            if v1>v2:
                print(v3,v1,v2)
            else:
                print(v3,v2,v1)

                
def cargar():
    num1=int(input("ingrese 1 valor"))
    num2=int(input("ingrese 2 valor"))
    num3=int(input("ingrese 3 valor"))
    ordenar_imprimir(num1,num2,num3)


# bloque principal
cargar()
