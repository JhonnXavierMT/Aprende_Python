# Dale Like <3
# Sigueme Para mas \(o_o)/

#[ejercico_1 en python]

"""_LEER DOS NUMEROS 
    A Y B, DEL MAYOR RESTARLE
    EL MENOR. DESPLEGAR EL
    RESULTADO_"""
#INICIO
#Leer A y B
A = int(input("ingrese el primer número\n"))
B = int(input("ingrese el segundo número\n"))

# Si A es Mayor a B entonces:
if A > B:
    resultado = A - B
    print("el mayor es: ",A)
    print("el menor es: ",B)
else:
    resultado = B - A
    print("el mayor es: ",B)
    print("el menor es: ",A)
#Mostramos al final
print("El resultado es : ",resultado)