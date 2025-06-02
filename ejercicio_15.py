"""Dado un número natural n de varios dígitos, obtener un nuevo número m 
formado por los dígitos de n, pero en orden creciente!!!!!!!! mejorar. 
"""
n = int(input("ingrese un numero: "))
dig,cont,cont2,x=0,0,0,n
while x>0:
    cont+=1
    x=x//10
x,t,nn=n,n,0
print(cont)
while cont2<cont:
    cont2+=1
    men=9
    while x>0:
        dig = x%10
        if dig <= men and dig!=0:
            men=dig
            print(f"menor{cont2}->",men)
        x=x//10
    nn=(nn*10)+men
    t=t//10
    x=t
print("fin-> ",nn)
