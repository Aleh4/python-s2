# Lab4.py
# Script detallado paso a paso para procesar datos de voltaje y temperatura

import csv
import os
from funcioneslab1 import limpiar_fila, convertir_a_temperatura, generar_alerta, calcular_kpis

# -------------------- BLOQUE 1: Definir rutas de archivos --------------------
INPUT_PATH = os.path.join('..', 'data','raw', 'voltajes.csv')
OUTPUT_PATH = os.path.join('..', 'Temperaturas_Procesado.csv')

# -------------------- BLOQUE 2: Inicializar variables para KPIs --------------------
filas_totales = 0
filas_validas = 0
descartes_timestamp = 0
descartes_valor = 0
temperaturas = []
alertas = 0

# -------------------- BLOQUE 3: Abrir archivos y preparar CSV --------------------
with open(INPUT_PATH, 'r', encoding='utf-8') as infile, open(OUTPUT_PATH, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['Timestamp', 'Voltaje', 'Temp_C', 'Alertas']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    # -------------------- BLOQUE 4: Procesar cada fila --------------------
    for row in reader:
        filas_totales += 1
        # Paso 1: Limpiar la fila
        timestamp, voltaje, error_ts, error_val = limpiar_fila(row)
        if error_ts:
            descartes_timestamp += 1
            continue
        if error_val:
            descartes_valor += 1
            continue
        # Paso 2: Convertir voltaje a temperatura
        temp_c = convertir_a_temperatura(voltaje)
        temperaturas.append(temp_c)
        filas_validas += 1
        # Paso 3: Generar alerta
        alerta = generar_alerta(temp_c)
        if alerta == 'ALERTA':
            alertas += 1
        # Paso 4: Escribir la fila procesada en el archivo de salida
        writer.writerow({
            'Timestamp': timestamp,
            'Voltaje': voltaje,
            'Temp_C': temp_c,
            'Alertas': alerta
        })

# -------------------- BLOQUE 5: Calcular y mostrar KPIs --------------------
kpis = calcular_kpis(filas_totales, filas_validas, descartes_timestamp, descartes_valor, temperaturas, alertas)
print('--- KPIs ---')
for k, v in kpis.items():
    print(f'{k}: {v}')
print(f'Salida generada en: {OUTPUT_PATH}')
