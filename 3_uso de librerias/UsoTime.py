import time
"""hola soy un comentario"""
tiempoInicial=time.time()

duracion = 10

tiempo_final =  tiempoInicial + duracion

while time.time()< tiempo_final:
    tiempo_restante= int(tiempo_final-time.time())
    print("tiempo restante ",tiempo_restante,"segundos")
    time.sleep(1)
print("Proceso terminado")