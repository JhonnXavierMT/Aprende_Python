# Dale Like <3
# Sigueme Para mas \(o_o)/

#----ESTRUCTURAS EN PYTHON---------

#-----------LISTAS-----------------
mi_lista = [1,2,3,"infiltrado"]

print("---------------------------")
print("Mostramos la lista Original ")
print(mi_lista)

mi_lista.append(4)  # Agrega un elemento
mi_lista.remove('infiltrado')  # Elimina un elemento

print("---------------------------")
print("Mostramos la lista agregando y eliminando un elemento: ")
print(mi_lista)

print("---------------------------")
print("Mostramos un elemento de la lista: ")
print(mi_lista[1])  # Accede al primer elemento

print("---------------------------")
print("Mostramos el tamaño de la lista: ")
print(len(mi_lista))  # Tamaño de la lista

#-----------TUPLAS-----------------
mi_tupla = (10, 20, 30)

print("---------------------------")
print("Mostramos elemento de la tupla: ")
print(mi_tupla[1])  # Accede al segundo elemento

print("---------------------------")
print("Mostramos el tamaño de la tupla: ")
print(len(mi_tupla))  # Tamaño de la tupla

#-----------DICCIONARIO-----------------

mi_diccionario = {'nombre': 'Lail Kaneki', 'edad': 20}
print("---------------------------")
print("Mostramos Diccionario Original: ")
print(mi_diccionario)

mi_diccionario['edad'] = 25  # Actualiza el valor de una clave
print("---------------------------")
print("Mostramos actualizacion: ")
print(mi_diccionario)

mi_diccionario['pais'] = 'España'  # Agrega una nueva clave
print("---------------------------")
print("Mostramos el agregado del elemento: ")
print(mi_diccionario)

print("---------------------------")
print("Mostramos un elemento del diccionario: ")
print(mi_diccionario['nombre'])  # Accede al valor de una clave

#-----------CONJUNTO-----------------

mi_conjunto = {1, 2, 3}
print("---------------------------")
print("Mostramos el conjunto: ")
print(mi_conjunto)

mi_conjunto.add(4)  # Agrega un elemento
mi_conjunto.add(2)  # No agrega duplicados X_X
print("---------------------------")
print("Mostramos el conjunto agregando un elemento :")
print(mi_conjunto)

mi_conjunto.remove(3)  # Elimina un elemento
print("---------------------------")
print("Mostramos el conjunto eliminando un elemento :")
print(mi_conjunto)
print("---------------------------")
print("Mostramos el tamaño del conjunto: ")
print(len(mi_conjunto))
