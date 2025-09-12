# El objetivo de este código es crear un archivo CSV con datos aleatorios de timestamp y voltaje (el voltaje flotante entre 0 y 25 voltios)

import csv
import random
from datetime import datetime, timedelta

ROOT=Path(__file__).resolve().parents[1]

# Parámetros
num_filas = 250  # Es el numero de filas generada
output_path = ROOT/"data"/"raw"/"voltajesaleatorios.csv"

# Generar timestamps secuenciales
start_time = datetime.now()
timestamps = [(start_time + timedelta(seconds=i*60)).strftime('%Y-%m-%d %H:%M:%S') for i in range(num_filas)]

# Generar voltajes aleatorios
voltajes = [round(random.uniform(0, 25), 3) for _ in range(num_filas)] 


# Escribir archivo CSV
with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Timestamp', 'Voltaje'])
	for ts, v in zip(timestamps, voltajes):
		writer.writerow([ts, v])

print(f"Archivo generado: {output_path} con {num_filas} filas aleatorias.")