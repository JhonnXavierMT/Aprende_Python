"""Obtener B elevado a P, utilizando operaciones de suma únicamente. """
b = int(input("ingrese un numero b: "))
p = int(input("ingrese un numero p: "))
for x in range(p-1):
    b=b+b
print(b)
"""Mostrar los primeros N números primos en orden decreciente.!!!!!!!!!!mejorar :("""
n = int(input("ingrese un numero : "))
cont,nn=0,0
aux=1
while cont<n:
    sw=0
    aux+=1
    if(aux==2):
        nn=(nn*10+aux)
        cont+=1
    else:       
        for x in range(2,aux):
            if x % aux == 0:
                sw=1
            else:
                nn=(nn*10+aux)
                cont+=1            
print("---",nn)
