def cargar_datos():
    nombres=[]
    edades=[]
    for x in range (5):
        v1=input("ingrese el nombre dela persona")
        nombres.append(v1)
        v2=int(input("ingrese la edad"))
        edades.append(v2)
    return [nombres,edades]
def mayores_edad(nombres,edades):
    for x in range(len(edades)):
        if edades [x]>=18:
            print(nombres[x])


def promedio_edades(edades):
    suma=0
    for x in range(len(edades)):
        suma=suma+edades[x]
    promedio=suma//5
    print("edad prmedio de las personas",promedio)

#bloque principal
nombres,edades=cargar_datos()
mayores_edad(nombres,edades)
promedio_edades(edades)
