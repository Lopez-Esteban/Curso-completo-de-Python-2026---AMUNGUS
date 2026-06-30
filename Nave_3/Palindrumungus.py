
palabralungus = input("Ingrese una plabra: ")

palabralungus = palabralungus.lower()

palabralungus = palabralungus.replace(" ", "")

palabralungus_reverse = palabralungus[::-1]

if palabralungus == palabralungus_reverse:
    print(f"{palabralungus} Es una Palindrumungus")
else:
    print(f"{palabralungus} No es una Palindrumungus")