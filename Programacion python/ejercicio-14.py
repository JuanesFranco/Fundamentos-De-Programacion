nota1=int(input("ingrese 1 nota"))
nota2=int(input("ingrese 2 nota"))
nota3=int(input("ingrese 3 nota"))
promedio=(nota1+nota2+nota3)/3
if promedio>=7:
    print("promocionado")
else:
    if promedio>=4:
        print("regular")
    else:
        print("reprobado")
        
