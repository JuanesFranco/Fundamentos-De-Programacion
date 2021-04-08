cantidad1=0
cantidad2=0
cantidad3=0
cantidad4=0
for f in range(10):
    valor=int(input("ingrese numero entero"))
    if valor>0:
        cantidad1=cantidad1+1
    else:
        if valor<0:
            cantidad2=cantidad2+1
            
    if valor%15==0:
        cantidad3=cantidad3+1
    if valor%2==0:
        cantidad4=cantidad4+1
print("la cantidad de positivos es de",cantidad1)
print("la cantidad de negativos es de",cantidad2)
print("la cantidad de multiplos de 15 es de",cantidad3)
print("la cantidad de pares es de",cantidad4)        






