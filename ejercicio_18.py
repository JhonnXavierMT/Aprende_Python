""""""
hora_1 = int(input("ingrese la hora: "))
minuto_1 = int(input("ingrese el minuto: "))
segundo_1 = int(input("ingrese el segundo: "))
hora_2 = int(input("ingrese la hora 2: "))
minuto_2 = int(input("ingrese el minuto 2: "))
segundo_2 = int(input("ingrese el segundo 2: "))
nhora,nmin,nseg=0,0,0
if hora_1<hora_2:
    nhora=hora_2-hora_1
    nmin=minuto_2-minuto_1
    nseg=segundo_2-segundo_1
    print(nhora,":",nmin,":",nseg)
elif minuto_2<minuto_1:
    nmin=minuto_2-minuto_1
    nseg=segundo_2-segundo_1
    print(hora_1,":",nmin,":",nseg)
elif segundo_2<segundo_1:
    nseg=segundo_2-segundo_1
    print(hora_1,":",minuto_1,":",nseg)
else:
    print("Error :(")
