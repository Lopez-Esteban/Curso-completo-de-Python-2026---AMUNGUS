# entrada del amungu
a = int(input("¿Cual es la cantidad de amungus que entraron?: "))

if a / 2 == 0:
    print("Entraron bien (Mungus par)")
else:
    print("Entraron mal (Mungus impar)")

##########################################
Amungusus = "Mungus par" if a / 2 == 0 else "Mungus impar"
print(Amungusus)
##########################################

if a > 0:
    print("Mungus par positivo" if a / 2 == 0 else "Mungus impar positivo")
elif a < 0:
    print("Mungus par negativo" if a / 2 == 0 else "Mungus impar negativo")
else:
    print("El numero es cero")        