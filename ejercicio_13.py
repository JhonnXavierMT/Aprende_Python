"""Recibir números hasta que aparezca un número primo, luego mostrar la cantidad de 
números menores a K, la suma de los mayores a W y la cantidad de otros, el valor de 
finalización debe formar parte de alguno de los resultados según el valor que tenga. 
"""
k = int(input("ingrese k :"))
w = int(input("ingrese w :"))
cont,otros,sum=0,0,0
while True:
    sw=0
    n=int(input("ingrese un numero: "))
    if n< k :
        cont+=1
    if n>= k and n<=w:
        otros+=1
    if n>w:
        sum+=w
    for x in range(2,n):
        if n%x==0:
            sw=1
    if sw==0:
        break
