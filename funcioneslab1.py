# funcioneslab1.py
# Funciones para procesar datos de voltaje y temperatura paso a paso

import csv

# 1. Leer y limpiar una fila del CSV

def limpiar_fila(row):
    """
    Recibe una fila del CSV y limpia los datos:
    - Elimina espacios
    - Normaliza decimales (comas a puntos)
    - Verifica errores en timestamp y voltaje
    Retorna: timestamp, voltaje (float), error_timestamp (bool), error_valor (bool)
    """
    timestamp = row.get('Timestamp', '').strip()
    voltaje_raw = row.get('Voltaje', '').strip()
    error_ts = False
    error_val = False
    if not timestamp or timestamp.lower() in ['na', 'error']:
        error_ts = True
    voltaje_raw = voltaje_raw.replace(',', '.')
    try:
        voltaje = float(voltaje_raw)
    except (ValueError, TypeError):
        error_val = True
        voltaje = None
    return timestamp, voltaje, error_ts, error_val

# 2. Convertir voltaje a temperatura

def convertir_a_temperatura(voltaje):
    """
    Aplica la fórmula T(°C) = 18 * V - 64 y redondea a 2 decimales
    """
    return round(18 * voltaje - 64, 2)

# 3. Generar alerta

def generar_alerta(temp_c):
    """
    Si la temperatura es mayor a 40°C retorna 'ALERTA', si no 'OK'
    """
    return 'ALERTA' if temp_c > 40 else 'OK'

# 4. Calcular KPIs

def calcular_kpis(filas_totales, filas_validas, descartes_timestamp, descartes_valor, temperaturas, alertas):
    """
    Calcula los indicadores clave de desempeño y los retorna en un diccionario
    """
    n = filas_validas
    temp_min = min(temperaturas) if temperaturas else None
    temp_max = max(temperaturas) if temperaturas else None
    temp_prom = round(sum(temperaturas) / n, 2) if n else None
    return {
        'Filas_totales': filas_totales,
        'Filas_validas': filas_validas,
        'Descartes_Timestamp': descartes_timestamp,
        'Descartes_valor': descartes_valor,
        'n': n,
        'temp_min': temp_min,
        'temp_max': temp_max,
        'temp_prom': temp_prom,
        'Alertas': alertas
    }
