def sumar (v1,v2,*lista):
    suma=v1+v2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma


print(sumar(1,2))
print (sumar(1,2,3,4,5))
