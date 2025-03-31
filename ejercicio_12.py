# Dale Like <3
# Sigueme Para mas \(o_o)/

#[ejercico_12 en python]
"""Recibir la edad y el género de los N alumnos
de la materia, luego mostrar: la cantidad 
de mujeres, la cantidad de varones, el mayor
de las mujeres, el menor de los varones, 
el promedio de edad de las mujeres y finalmente
el promedio de edad de los varones (Para diferenciar
el género, ingrese: 1 para indicar que es mujer 
y 2 para indicar que es varón)."""
n=int(input("Cantidad de alumnos: "))
cVarones,menorvaron,cont=0,0,0
cMujeres,mayorMujer,edadVarones,edadMujeres=0,0,0,0
while cont<n:
    edades=int(input("ingrese la edad: "))
    genero=int(input("ingrese el genero: "))
    if genero !=1:
        if edades<menorvaron or edades!=0:menorvaron=edades
        cVarones+=1
        edadVarones+=edades
    else:
        if edades>mayorMujer:mayorMujer=edades
        cMujeres+=1
        edadMujeres+=edades
    cont+=1
print("----------------------")
print("Cantidad de Varones: ",cVarones)
print("Varon menor: ",menorvaron)
print("Promedio de edad Varones :",edadVarones/cVarones)
print("----------------------")
print("Cantidad de Mujeres: ",cMujeres)
print("Mujer mayor: ",mayorMujer)
print("Promedio de edad Mujeres :",edadMujeres/cMujeres)
print("----------------------")
