import csv
import os
from utils import limpiar_fila, conversor_temperatura, generar_alerta, calcular_kpis

# Rutas de archivos
INPUT_PATH = os.path.join('..', 'data', 'voltajes.csv')
OUTPUT_PATH = os.path.join('..', 'Temperaturas_Procesado.csv')

filas_totales = 0
filas_validas = 0
descartes_timestamp = 0
descartes_valor = 0
temperaturas = []
alertas = 0
n=0

with open(INPUT_PATH, 'r', encoding='utf-8') as infile, open(OUTPUT_PATH, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['Timestamp', 'Voltaje', 'Temp_C', 'Alertas']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        filas_totales += 1
        timestamp, voltaje, error_ts, error_val = limpiar_fila(row)
        if error_ts:
            descartes_timestamp += 1
            continue
        if error_val:
            descartes_valor += 1
            continue
        temp_c = conversor_temperatura(voltaje)
        temperaturas.append(temp_c)
        filas_validas += 1
        alerta = generar_alerta(temp_c)
        if alerta == 'ALERTA':
            alertas += 1
        writer.writerow({
            'Timestamp': timestamp,
            'Voltaje': voltaje,
            'Temp_C': temp_c,
            'Alertas': alerta
        })

temp_min = min(temperaturas) if temperaturas else None
temp_max = max(temperaturas) if temperaturas else None
temp_prom = round(sum(temperaturas) / n, 2) if n else None

# KPIs finales
kpis = calcular_kpis(filas_totales, filas_validas, descartes_timestamp, descartes_valor, temperaturas, alertas)
for k, v in kpis.items():
    print(f'{k}: {v}')
print(f'Salida generada en: {OUTPUT_PATH}')
