# Dale Like <3
# Sigueme Para mas \(o_o)/

#[ejercico_11 en python]
""" 
Recibir N sueldos de empleados
luego en función de los intervalos
cerrados:De 1 a 1500 es Mensajero, de 1501
a 3500 es Secretaria, de 3501 a 5000 es
Oficinista,de 5001 a 9000 es Director y de
9001 en adelante es Gerente. Mostrar las
frecuencias de cada cargo. """

n=int(input("cantidad de sueldos\n"))
cont,contMensajeros,contSecretarios=0,0,0
contOficinistas,contDirectores,contGerentes=0,0,0
while cont<n:
    sueldo=int(input("ingrese el salario: "))
    if sueldo>=1 and sueldo<=1500:
        contMensajeros+=1
    elif sueldo>=1501 and sueldo<=3500:
        contSecretarios+=1
    elif sueldo>=3501 and sueldo<=5000:
        contOficinistas+=1
    elif sueldo>=5001 and sueldo<=9000:
        contDirectores+=1
    else:
        contGerentes+=1
    cont+=1
print("Es Mensajeros ",contMensajeros)
print("Es Secretarias ",contSecretarios)
print("Es Oficinistas ",contOficinistas)
print("Es Directores ",contDirectores)
print("Es Gerentes ",contGerentes)