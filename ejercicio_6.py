# Dale Like <3
# Sigueme Para mas \(o_o)/

#[ejercico_6 en python]
"""GENERAR Y DESPLEGAR LOS N NUMERO QUE
   TENGAN LA SIGUIENTE FORMA:
   1,2,4,7,11,16, ... """
#Leer n
n=int(input("longitud de la serie: "))
#Inicializacion de variables
cont=0
serie=1
while cont<n:#condicion de la longitud de la serie
    print(serie)#mostrar la serie
    cont+=1# contador en aumento de 1 a 1
    serie=serie+cont # se genera la serie 
