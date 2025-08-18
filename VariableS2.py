NOMBRE = "Alejandro"    #Constante por convencion - str
edad = 23               #int
voltaje = 2.7182        #float
activo = True           #bool
#f-string (formato para cadena y caracteres, letras)
print(f"Hola, {NOMBRE}. Edad: {edad}")
#Para float {voltaje:.sf} el valor antes del f nos dice el numero desoues de la coma
print(f"Voltaje: {voltaje:.5f} V | Activo: {activo}")
print(f"Tipos -> edad:{type(edad).__name__}, voltaje:{type(voltaje).__name__}")