def limpiar_fila(row):
    """
    Limpia una fila del CSV y retorna:
    timestamp, voltaje (float), error_timestamp (bool), error_valor (bool)
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

def conversor_temperatura(voltaje):
    """Convierte voltaje a temperatura con dos decimales."""
    return round(18 * voltaje - 64, 2)

def generar_alerta(temp_c):
    """Genera alerta si la temperatura es mayor a 40°C."""
    return 'ALERTA' if temp_c > 40 else 'OK'

def calcular_kpis(filas_totales, filas_validas, descartes_timestamp, descartes_valor, temperaturas, alertas):
    """Calcula los KPIs y los retorna en un diccionario."""
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
