"""Dado un número natural de varios dígitos, determinar si es “capícua”. """
n = int(input("ingrese un numero: "))
dig,nn,aux=0,0,0
while n>0:
    dig=n%10
    nn=(nn*10)+dig
    n=n//10
if nn==aux:
    print("Es capicua!!!")
else:
    print("No es capicua!!!")
