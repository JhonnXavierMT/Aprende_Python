# Dale Like <3
# Sigueme Para mas \(o_o)/
def Mostra_archivo():
    with open('mi_archivo.txt','r') as archivo:
        print(archivo.read())
#----ARCHIVOS EN PYTHON---------

# METODO WITH  
with open('mi_archivo.txt', 'r') as archivo: #ABRE Y CIERRA AUTOMATICO
    contenido = archivo.read()
    print("---------------------------------")
    print(contenido)
    print("---------------------------------")

with open('mi_archivo.txt','a') as adicionar:
    adicionar.write(" soy el nuevo texto \O_O/... \n")

Mostra_archivo()

with open('mi_archivo.txt','w') as archivo:
    print(archivo.write("Soy un texto que se sobrescribio U-U/"))

Mostra_archivo()




