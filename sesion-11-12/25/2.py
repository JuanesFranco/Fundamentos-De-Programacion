def retornar_mayor(v1,v2):
    if v1>v2:
        return v1
    else:
        return v2
#bloque principal
valor1=int(input("ingrese valor"))
valor2=int(input("ingrese valor")) 
x=retornar_mayor(valor1,valor2)
print(x)
