# Dale Like <3
# Sigueme Para mas \(o_o)/

#Estructuras de repeticion 
# for , while  

"""_Controlador WHILE_"""
# Contar del 1 al 5
contador = 1
while contador <= 5:
    print(contador)
    contador += 1


"""_ controlador FOR_"""

# Iterar sobre una lista
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

# Iterar usando un rango
for i in range(5):  # Rango del 0 al 4
    print(i)

# Iterar usando un rango definido de dos extremos
for i in range(1,5):  # Rango del 0 al 4
    print(i)
    

""" _bucles con else_"""

#Con while y else
contador = 0
while contador < 3:
    print(contador)
    contador += 1
else:
    print("Se cumplió la condición del bucle")
#con for y else
for i in range(5):
    print(i)
else:
    print("Bucle terminado")

"""Otros controladores para los bucles :
break: Sale del bucle antes de completarlo.
continue: Salta a la siguiente iteración del bucle.
pass: No realiza ninguna acción; se usa como un marcador de posición.
"""
# Uso del BREAK
for i in range(5):
    if i == 3:
        break  # Termina el bucle cuando i es 3
    print(i)
#Uso del CONTINUE
for i in range(5):
    if i == 2:
        continue  # Salta cuando i es 2
    print(i)

# Uso del PASS
for i in range(5):
    if i == 2:
        pass  # No hacer nada si i es 2
    else:
        print(i)




