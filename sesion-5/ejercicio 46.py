cantidad=0
n=int(input("cuantos valores ingresa"))
for f in range(n):
    valor=int(input("ingrese el valor"))
    if valor>=1000:
        cantidad=cantidad+1
print("la cantidad de numeros mayores a 1000 es de:",cantidad)    
