n=int(input("ingrese la cantidad de empleados a evaluar"))
x=1
cobrador1=0
cobrador2=0
gastos=0
while x<=n:
    sueldo=float(input("ingrese el sueldo del empleado"))
    if sueldo<=300:
        cobrador1=cobrador1+1
    else:
        cobrador2=cobrador2+1
    gastos=gastos+sueldo
    x=x+1
print("cantidad de empleados con sueldo entre 100 y 300",cobrador1)
print("cantidad de empleados con sueldo superior a 300",cobrador2)    
