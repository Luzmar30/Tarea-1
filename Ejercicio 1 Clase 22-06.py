#PROGRAMA QUE DONDE SE REALIZA LA FUNCION DE SIMAR LOS ELEMENTOS DE UNA LISTA
arg_1=[2,3,4]
def suma (arg_1):
    len_list=len(arg_1)
    acumulador=0
    for i in range(len_list):
        acumulador+=arg_1[i]
    return acumulador

print (suma(arg_1))