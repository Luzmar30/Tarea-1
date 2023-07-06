#PROGRAMA PARA REVERTIR EL ORDEN DE UNA FRASE
frase= input("Ingrese la frase")
acumm_frase=" "
for i in range(len(frase)):
    acumm_frase=frase[i]+acumm_frase
print("la frase al reves es:", acumm_frase)
if frase==acumm_frase:
    print("La frase ingresada es palindroma")
else:
    print("La frase ingresada NO es palindroma")