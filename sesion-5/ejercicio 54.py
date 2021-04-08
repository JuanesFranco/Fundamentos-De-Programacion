suma1=0
suma2=0
suma3=0
for f in range(5):
    edad=int(input("ingrese la edad"))
    suma1=suma1+1
prom1=suma1/5
print("el promedio de edades del turno de la mañana es de:")
print(prom1)
for f in range(6):
      edad=int(input("ingrese la edad"))
      suma2=suma2+1
prom2=suma2/6
print("el promedio de edades del turno de la tarde es de:",prom2)
for f in range(11):
      edad=int(input("ingrese la edad"))
      suma3=suma3+1
prom3=suma3/11
print("el promedio de edades del turno noche es de:")
print(prom3)
if prom1<prom2 and prom1<prom3:
      print("el turno de mañana tiene un promedio de edades menor")
else:
     if prom<prom3:
              print("el turno de tarde tiene un promedio de eddes menor")
     else:
              print("el turno de noche tiene unpromedio de edades menor")
         

           
      
            
      
      
