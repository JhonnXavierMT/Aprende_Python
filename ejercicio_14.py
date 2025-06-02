"""Dado un número natural de varios dígitos, mostrar cada uno de sus dígitos primos de 
derecha a izquierda. 
"""
n = int(input("ingrese un numero: "))
nn=0
while n>0:
    dig=n%10
    sw=0
    for i in range(2,n):
        if dig %i==0:
            sw=1
        else:
            nn=(nn*10)+dig
    n=n//10
print(nn)