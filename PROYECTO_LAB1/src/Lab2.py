import csv
import os

# Rutas de archivos
INPUT_PATH = os.path.join('..', 'data', 'voltajes.csv')
OUTPUT_PATH = os.path.join('..', 'Temperaturas_Procesado.csv')

# KPIs
filas_totales = 0
filas_validas = 0
descartes_timestamp = 0
descartes_valor = 0
temperaturas = []
alertas = 0

with open(INPUT_PATH, 'r', encoding='utf-8') as infile, open(OUTPUT_PATH, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['Timestamp', 'Voltaje', 'Temp_C', 'Alertas']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        filas_totales += 1
        timestamp = row.get('Timestamp', '').strip()
        voltaje_raw = row.get('Voltaje', '').strip()

        # Limpieza de timestamp
        if not timestamp or timestamp.lower() in ['na', 'error']:
            descartes_timestamp += 1
            continue

        # Limpieza de voltaje
        voltaje_raw = voltaje_raw.replace(',', '.')
        try:
            voltaje = float(voltaje_raw)
        except (ValueError, TypeError):
            descartes_valor += 1
            continue

        # Conversión a temperatura
        temp_c = round(18 * voltaje - 64, 2)
        temperaturas.append(temp_c)
        filas_validas += 1

        # Alerta
        alerta = 'ALERTA' if temp_c > 40 else 'OK'
        if alerta == 'ALERTA':
            alertas += 1

        writer.writerow({
            'Timestamp': timestamp,
            'Voltaje': voltaje,
            'Temp_C': temp_c,
            'Alertas': alerta
        })

# KPIs finales
n = filas_validas
temp_min = min(temperaturas) if temperaturas else None
temp_max = max(temperaturas) if temperaturas else None
temp_prom = round(sum(temperaturas) / n, 2) if n else None

print('--- KPIs ---')
print(f'Filas_totales: {filas_totales}')
print(f'Filas_validas: {filas_validas}')
print(f'Descartes_Timestamp: {descartes_timestamp}')
print(f'Descartes_valor: {descartes_valor}')
print(f'n: {n}')
print(f'temp_min: {temp_min}')
print(f'temp_max: {temp_max}')
print(f'temp_prom: {temp_prom}')
print(f'Alertas: {alertas}')
print(f'Salida generada en: {OUTPUT_PATH}')
