def multiplicar(lista, valor):
    for x in range(len(lista)):
        multi=lista[x]*valor
        print(multi)

#bloque prncipal
lista=[3, 7, 8, 10, 2]
print("lista original")
print(lista)
print("lista de los elementos multiplicados por 3")
multiplicar(lista,3)
