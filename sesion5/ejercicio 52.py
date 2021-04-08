cantidad1=0
cantidad2=0
cantidad3=0
cantidad4=0
n=int(input("ingrese la cantidad de puntos"))
for f in range(n):
    x=int(input("ingrese el valor de x"))
    y=int(input("ingrese el valor de y"))
    if x>0 and y>0:
        cantidad1=cantidad1+1
    else:
        if x<0 and y>0:
            cantidad2=cantidad2+1
        else:
            if x<0 and y<0:
                cantidad3=cantidad3+1
            else:
                if x>0 and y<0:
                    cantidad4=cantidad4+1
print("cantidad de puntos ingresados en el cuadrante 1",cantidad1)
print("cantidad de puntos ingresados en el cuadrante 2",cantidad2)
print("cantidad de puntos ingresados en el cuadrante 3",cantidad3)
print("cantidad de puntos ingresados en el cuadrante 4",cantidad4)  
                    
