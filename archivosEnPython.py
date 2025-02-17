# Dale Like <3
# Sigueme Para mas \(o_o)/

#----ARCHIVOS EN PYTHON---------

archivo = open('mi_archivo.txt', 'r')  
contenido = archivo.read() 
print(contenido)
archivo.close()  # Siempre cierra el archivo !!!

# METODO WITH  
with open('mi_archivo.txt', 'r') as archivo: #ABRE Y CIERRA AUTOMATICO
    print("Segunda forma de abrir un archivo :")  # comentario Guia
    contenido = archivo.read()
    print("---------------------------------")
    print(contenido)
    print("---------------------------------")

with open('mi_archivo.txt','a') as adicionar:
    adicionar.write(" soy el nuevo texto \O_O/... \n")

with open('mi_archivo.txt','r') as archivo:
    print(archivo.read())

with open('mi_archivo.txt','w') as archivo:
    print(archivo.write("Soy un texto que se sobrescribio U-U/"))

with open('mi_archivo.txt','r') as archivo:
    print(archivo.read())




