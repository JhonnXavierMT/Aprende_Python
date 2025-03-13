# Cadenas en Python
# Definir cadenas
cadena1 = 'Hola, Python'
cadena2 = "Aprendiendo Python"
texto_largo = '''Esto es un texto
en varias líneas.'''

# Concatenación y repetición
saludo = "Hola" + " " + "Mundo"  # Une las cadenas con el operador +
eco = "Python " * 3  # Repite la cadena 3 veces
print(saludo)
print(eco)

# Acceder a caracteres y subcadenas
mi_cadena = "Python"
print(mi_cadena[0])   # Primer carácter 'P'
print(mi_cadena[-1])  # Último carácter 'n'
print(mi_cadena[1:4]) # Subcadena 'yth' (índices 1 al 3)

# Métodos de cadenas
print(len("Python"))  # Devuelve la longitud de la cadena
print("Hola Mundo".upper())  # Convierte a mayúsculas
print("Hola Mundo".lower())  # Convierte a minúsculas
print("Hola Mundo".title())  # Convierte la primera letra de cada palabra en mayúscula
print("  Hola  ".strip())  # Elimina espacios en blanco al inicio y al final
print("Me gusta Python".replace("Python", "Java"))  # Reemplaza "Python" por "Java"
print("Me gusta Python".find("Python"))  # Devuelve la posición donde aparece "Python"
print("Me gusta Python".count("a"))  # Cuenta las veces que aparece la letra 'a'
print("12345".isdigit())  # Verifica si la cadena contiene solo dígitos
print("Python123".isalnum())  # Verifica si la cadena es alfanumérica
print("Hola".isalpha())  # Verifica si la cadena contiene solo letras
print("   ".isspace())  # Verifica si la cadena contiene solo espacios en blanco

# Formateo de cadenas
nombre = "Jhonn"
edad = 25
print(f"Hola, soy {nombre} y tengo {edad} años.")  # Formato con f-strings
print("Hola, soy {} y tengo {} años.".format(nombre, edad))  # Formato con format()
print("Hola, soy %s y tengo %d años." % (nombre, edad))  # Formato con %

# Convertir otros tipos a cadena
numero = 100
cadena_numero = str(numero)  # Convierte el número en cadena
print(cadena_numero)