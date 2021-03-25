altas=0
bajas=0
x=1
while x<=10:
    nota=int(input("ingrese notas"))
    if nota>=7:
        altas=altas+1
    else:
        bajas=bajas+1
    x=x+1
print("la cantidad de notas altas es de:",altas)
print("la cantidad de notas bajas es de: ",bajas)
