 contador=0
contador2=0
contador3=0
n=int(input("ingrese la cantidad de triangulos a calcular"))
for f in range(n):
    lado1=int(input("ingrese lado 1"))
    lado2=int(input("ingrese lado 2"))
    lado3=int(input("ingrese lado 3"))
    if lado1==lado2 and lado2==lado3:
        print("triangulo equilatero")
        contador=contador+1
    else:
         if lado1==lado2 or lado2==lado3:
             print("triangulo isoceles")
             contador2=contador2+1
         else:
             print("triangulo escaleno")
             contador3=contador3+1
print("la cantidad de equilateros es de:",contador)
print("la cantidad de isoceles es de:",contador2)
print("la cantidad de escalenos es de:",contador3)

      
       
