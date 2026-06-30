
amungus = "Fede"
edad = 67
talla = 1.69

mensaje = "Hola, soy el amungu %s , tengo %s y mido %.2f metros" % (amungus,edad,talla)
print(mensaje)
#-----------------------------------------------------------------------------------------------
mensaje = "Hola, soy el amungu {} , tengo {} y mido {} metros".format(amungus,edad,talla)
print(mensaje)
#-----------------------------------------------------------------------------------------------
mensaje = f"Hola, soy el amungu {amungus} , tengo {edad} y mido {talla} metros"
print(mensaje)
