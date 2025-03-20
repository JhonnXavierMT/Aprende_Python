# Dale Like <3
# Sigueme Para mas \(o_o)/

#[ejercico_5 en python]
"""GENERAR Y DESPLEGAR LOS N NUMERO QUE
   TENGAN LA SIGUIENTE FORMA:
   1,3,2,4,5,7,6,8... """
#Leer n
n = int(input("longitud de la serie: "))#2
#Inicializacion de variables
cont,impares,pares=0,1,0
while cont<n:#condicion de la longitud de la serie
    cambio=0
    while cambio < 2 and cont < n:#genera dos numeros
        print(impares)
        impares+=2 #genera serie de impares
        cambio+=1 #contador while 2
        cont+=1 #contador while 1
    cambio=0
    while cambio < 2 and cont < n:#genera dos numeros
        pares+=2 #genera serie de pares
        print(pares)
        cambio+=1 # contador while 3
        cont+=1 # conatdor while 1