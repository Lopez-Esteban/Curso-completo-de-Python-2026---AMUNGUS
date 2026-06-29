consumo_amungu = float(input("Ingrese el monto de consumo amungusero: "))

if consumo_amungu < 50 and consumo_amungu <= 100:
    descuento = 0.1
elif consumo_amungu > 100 and consumo_amungu <= 200:
    descuento = 0.2
elif consumo_amungu > 200:
    descuento = 0.3
else:
    descuento = 0.0

monto_descuento = consumo_amungu * descuento
total = consumo_amungu - monto_descuento

print("RESUMEN DE LA CUENTA")
print("Monto de consumo del amungus: ", consumo_amungu)
print("Descuento amungusero: ", descuento * 100, "%")
print("Monto total con descuento: ", total)