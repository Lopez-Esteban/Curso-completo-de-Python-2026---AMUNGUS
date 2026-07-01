
Amungus = ["Fede", "Nico", "Dross", "Juli3p", "Santi", "Tomi"]
print(Amungus)

Amungus.append("Esteban")
print(Amungus)

Impostor = ["Jose", "Pedro"]
print(Impostor)

Amungus.extend(Impostor)
print(Amungus)

Amungus.insert(2, "Lautaro")
print(Amungus)

Amungus.remove("Tomi")
print(Amungus)

print(Amungus.index("Dross"))