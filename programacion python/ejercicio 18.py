total_preguntas=int(input("ingrese el total de preguntas"))
total_correctas=int(input("ingrese el total de preguntas correctas"))
porcentaje=total_correctas*100/total_preguntas
if porcentaje>=90:
    print("nivel maximo")
else:
    if porcentaje>=75:
        print("nivel medio")
    else:
        if porcentaje>=50:
            print("nivel regular")
        else:
            print("fuera de nivel")
