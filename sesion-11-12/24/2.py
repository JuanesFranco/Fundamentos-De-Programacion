def mostrar_mayor(v1,v2,v3):
    print("el valor mayor es:")
    if v1>v2 and v1>v3:
        print(v3)
    else:
        if v2>3:
            print(v2)
        else:
            print(v3)

def cargar():
    valor1=int(input("ingrese 1 valor"))
    valor2=int(input("ingrese 2 valor"))
    valor3=int(input("ingrese 3 valor"))
    mostrar_mayor(valor1,valor2,valor3)
#bloque principal
cargar()








               
    
