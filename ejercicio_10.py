# Dale Like <3
# Sigueme Para mas \(o_o)/

#[ejercico_10 en python]
"""Recibir números naturales, hasta 
que aparezca un numero perfecto, 
luego mostrar la cantidad de pares y
la cantidad de impares, el valor de 
finalización no forma parte de 
los resultados"""
#inicializacion de variables
div=2
sumPerfetc,par,impar=0,0,0
while True:
    n=int(input("ingrese un numero: "))
    while div<=n:#condi para encontrar sus divisores
        if n%div==0:#solo si es exacta la division
            #acumular suma de divisores de n
            sumPerfetc=sumPerfetc+(n/div)
        div+=1
    if sumPerfetc == n:
    # salir del bucle si se encontro un numero perfecto
        print("Encontro un numero perfecto!!!")
        print("cantidad de pares:",par)
        print("cantidad de impares: ",impar)
        break
    else:
    #sino recetear div y suPerfect para el siguiente n
        div=2
        sumPerfetc=0
        #verificar si es par o impar
        if n%2==0:
            par+=1
        else:impar+=1
    