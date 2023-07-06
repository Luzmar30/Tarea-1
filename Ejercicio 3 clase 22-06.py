#PROGRAMA PARA REVERTIR EL ORDEN DE UNA PALABRA Y SABER SI UNA PALABRA PALINDROMA

palabra= input("Ingrese la frase: ")
acumm_palabra=""

for i in range(len(palabra)):
    acumm_palabra=palabra[i]+acumm_palabra

if palabra==acumm_palabra:
    print("La frase ingresada es palindroma")
else:
    print("La frase ingresada NO es palindroma")