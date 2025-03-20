# Dale Like <3
# Sigueme Para mas \(o_o)/

#[ejercico_4 en python]
"""GENERAR Y DESPLEGAR LOS N NUMERO QUE
   TENGAN LA SIGUIENTE FORMA:
   1,5,9,13,17... """

#Leer longitud de la serie
n = int(input("Ingrese largo de la serie quiere :\n"))
#inicializamos dos variables 
cont=0 # inicio de contador
num_s=1 # inicio de serie
while cont<n: # condicion de la longitud de la serie
    cont+=1 #contador en aumento de 1 a 1
    if cont==1:
        print(num_s) # inicio de la serie 
    else:
        num_s = num_s + 4 # continuacion de la serie
        print(num_s)