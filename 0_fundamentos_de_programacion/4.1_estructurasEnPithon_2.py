# 🚀 "Si quieres ser un programador PRO, debes dominar esto…" 🧠💻
# 🤯 "Las estructuras de datos son la clave para escribir código rápido y eficiente." 🔥

# Estructuras de datos básicas en Python

# 1. Listas (arrays dinámicos en Python)
mi_lista = [1, 2, 3, 4, 5]
mi_lista.append(6)  # Agregar un elemento al final
print("Lista:", mi_lista)

# 2. Pilas (Stack - LIFO: Último en entrar, primero en salir)
pila = []
pila.append("A")  # Apilar
pila.append("B")
pila.append("C")
print("Pila antes de desapilar:", pila)
pila.pop()  # Desapilar
print("Pila después de desapilar:", pila)

# 3. Colas (Queue - FIFO: Primero en entrar, primero en salir)
from collections import deque
cola = deque(["A", "B", "C"])
print("Cola antes de desencolar:", cola)
cola.popleft()  # Desencolar
print("Cola después de desencolar:", cola)





