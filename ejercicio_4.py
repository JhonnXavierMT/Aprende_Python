# Dale Like <3
# Sigueme Para mas \(o_o)/

#[ejercico_3 en python]

"""_LEER DOS NUMEROS 
    A Y B,DEL MAYOR RESTARLE
    EL MENOR. DESPLEGAR EL
    RESULTADO_"""

#Entrada
A = int(input("ingrese el primer número\n"))
B = int(input("ingrese el segundo número\n"))

#Proceso
if A > B:
    resultado = A - B
    print("el mayor es: ",A)
    print("el menor es: ",B)
else:
    resultado = B - A
    print("el mayor es: ",B)
    print("el menor es: ",A)
    
#salida
print("El resultado es : ",resultado)