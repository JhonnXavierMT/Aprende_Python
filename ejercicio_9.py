# Dale Like <3
# Sigueme Para mas \(o_o)/

#[ejercico_9 en python]
"""Recibir números hasta que 
aparezca un número par, luego
mostrar por pantalla la 
suma de menores a 10, el producto
de mayores a 20 y la cantidad de 
los demás números (los resultados
solo toman en cuenta números impares).  """
sum=0
mult=1
cont=0
n=int(input("ingrese un numero"))
while n % 2 != 0:# mientras n sea impar entrar
    if n<10: #sumar si es menor a 10
        sum=sum+n
    elif n>20: #multiplicar si es mayor a 20
        mult=mult*n
    else:
        cont+=1 # contar si es otro numero
    n=int(input("ingrese un numero"))
if mult==1:mult=0 # si no hay numeros > a 20 entonces es 0
print(f"suma de numeros menores a 10 : {sum}")
print(f"multiplicacion de numeros mayores a 20 : {mult}")
print(f"cantidad de los demas numeros: {cont}")
    