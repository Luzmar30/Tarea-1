dato1 = input("introduzca un valor numérico ")
dato2 = input("introduzca otro valor numérico ")

if dato1.isnumeric() and dato2.isnumeric():
    
    suma = int(dato1) + int(dato2)
elif dato1.replace('.', '', 1).isnumeric() and dato2.replace('.', '', 1).isnumeric():
    
    suma = float(dato1) + float(dato2)
else:
    
    print("los datos que suministró no son válidos para esta operacion. Vuelva a correr el programa e introduzca datos valores numéricos.")
    exit()
print("La suma de sus datos es: ", suma)