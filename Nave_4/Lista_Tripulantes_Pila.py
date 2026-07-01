
pila = []
pila.append("Tripulante 1")
pila.append("Tripulante 2")
pila.append("Tripulante 3")
print(pila)

elemento = pila.pop()
print("Elemento eliminado:", elemento)

print("Pila actual:", pila)

print("---------------------------------------------------------------")

cola = []
cola.append("Tripulante A")
cola.append("Tripulante B")
cola.append("Tripulante C")
print(cola)

elemento = cola.pop(0)
print("Tripulante eliminado:", elemento)

print("Cola actual:", cola)

print("---------------------------------------------------------------")

from collections import deque
cola2 = deque()
cola2.append("Tripulante A")
cola2.append("Tripulante B")
cola2.append("Tripulante C")
print(cola2)

print("Tripulante eliminado:", cola2.popleft())
print("Cola actual:", cola2)