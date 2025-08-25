import datetime as dt

fecha = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Inicio del programa
print("Reporte de Lecturas de Voltaje\n ")
print(fecha)
#Entrada del nombre
nombre = input("Ingrese su nombre: ")

# Entrada de número de muestras
try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: Debes ingresar un número entero para la edad")
    exit()

# Entrada de lecturas
try:
    lectura1 = float(input("Lectura 1 (V): "))
    lectura2 = float(input("Lectura 2 (V): "))
except ValueError:
    print("Error: Debes ingresar valores numéricos para las lecturas.")
    exit()

# Cálculo de promedio
promedio = (lectura1 + lectura2) / 2

# Constantes de umbral
UMBRAL_BAJO = 1.0
UMBRAL_MEDIO = 3.0
UMBRAL_ALTO = 5.0

# Clasificación
if promedio < UMBRAL_BAJO:
    estado = "BAJO"
elif promedio < UMBRAL_MEDIO:
    estado = "MEDIO"
else:
    estado = "ALTO"

# Reporte
print(f"Alumno: {nombre}")
print(f"Lecturas (V): {lectura1:.2f}, {lectura2:.2f} | Promedio: {promedio:.2f} V")
print(f"Estado: {estado} ({promedio:.2f} V)")