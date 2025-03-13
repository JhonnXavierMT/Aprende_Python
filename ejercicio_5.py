import emoji as em
# Dale Like <3
# Sigueme Para mas \(o_o)/

#[ejercico_5 en python]

"""CREE UN PROGRAMA ESTILO TERMOSTATO QUE INDIQUE 
   QUE SI ESTA A MENOS DE 10 C° HACE FRIO
   O  SI ESTA MAS DE 27 C° HACE CALOR Y SI ESTA
   EN MEDIO DEL RANGO DE MAYOR A 10 Y MENOR A 27 
   EL AMBIENTE ES ESTABLE """
#INICIO 
 # Leer temperatura
temp =int(input("Temperatura del ambiente:\n "))
#Establecer el rango de temp estable
if temp > 10 and temp < 27:
    # mostramos si esta en el rango
    print("la Temperatura es estable 😀 ") 
elif temp <=10:
    # mostramos si esta en abajo del rango
    print("La temperatura esta muy Fria ❄️ ")
elif temp >=27:
    # mostramos si esta encima del rango
    print("La temperatura esta muy caliente 🔥 ")



