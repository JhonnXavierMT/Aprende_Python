# Dale Like <3
# Sigueme Para mas \(o_o)/

#[ejercico_7 en python]
"""Recibir números hasta 
   que digite el número:
   0, luego mostrar la cantidad 
   de números ingresados. """

cont=0

while True:
    numeros=int(input("Ingrese numeros:\n"))
    if numeros==0:
        print(f"La cantidad es :{cont} ")
        break
    cont+=1