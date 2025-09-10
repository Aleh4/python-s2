import csv
from datetime import datetime
from pathlib import Path #importo el comando path (busca el lugar del codigo)
from statistics import mean

#crear mis variables de rutas para ingreso de archivo y salida de archivo
ROOT=Path(__file__).resolve().parents[1]#busca el lugar donde esta guardado el codigo
#/USUARIO/Sesion4
IN_FILE=ROOT/"data"/"raw"/"voltajes_250_sucio.csv" #ruta de ingreso
OUT_FILE=ROOT/"data"/"processed"/"voltajes_250_sucio_limpio5.csv" #ruta de salida

with open(IN_FILE,'r',encoding="utf-8", newline="") as fin, \
    open(OUT_FILE, "w", encoding="utf-8", newline="") as fout:
    reader=csv.DictReader(fin,delimiter=';')
    writer=csv.DictWriter(fout,fieldnames=["Tiempo","Voltaje","Temperatura","Alerta"])
    writer.writeheader()
#leer linea por lineal y seleccionar en crudo raw 
    total = kept = 0
    bad_ts = bad_val = 0
    temp=0
    voltajes=[]
    Temperaturas=[]
    Alertas=[]
    for row in reader:
        total+=1
        ts_raw  = (row.get("timestamp") or "").strip() #toma todos los valores de la columna timestamp
        val_raw = (row.get("value") or "").strip() #toma todos los valores de la columna value
#limpiar data
        val_raw = val_raw.replace(",", ".")
        val_low = val_raw.lower() #empezar a eliminar valores no existentes
        if val_low in {"", "na", "n/a", "nan", "null", "none", "error"}:
            bad_ts += 1
            continue #salta el comando
        try:
            val = float(val_raw)
            voltajes.append(val)
        except ValueError:
            bad_ts += 1
            continue  # saltar fila si no es número
#limpieza de data de tiempo 
        ts_clean = None
        for fmt in ("%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M:%S"):
            try:
                dt = datetime.strptime(ts_raw, fmt)
                ts_clean = dt.strftime("%Y-%m-%dT%H:%M:%S")
                break
            except ValueError:
                pass
#milisegundo (opcional)
        if ts_clean is None and "T" in ts_raw and len(ts_raw) >= 19:
            try:
                dt = datetime.strptime(ts_raw[:19], "%Y-%m-%dT%H:%M:%S")
                ts_clean = dt.strftime("%Y-%m-%dT%H:%M:%S")
            except ValueError:
                ts_clean = None

        if ts_clean is None:
            bad_ts += 1
            continue  # saltar fila si no pudimos interpretar la fecha
        
#sistema de Alerta de voltaje - si V>= a 5 V entonces lanza una alerta
        #if val >= 5:
         #   Alerta = "CUIDADO"
        #else:
         #   Alerta = "OK"
        #voltajes.append(val)
        
        if val is not None:
            temp = 18*val-64
            Temperaturas.append(temp) #creo una lista de temperaturas a partir de los voltajes
            if temp >= 25:  #sistema de Alerta de temperatura - si T>= a 25°C entonces lanza una alerta
                Alerta = "CUIDADO"
                Alertas.append(Alerta)
            else:
                Alerta = "OK"    
                           
#grabar data en writer
        writer.writerow({"Tiempo": ts_clean, "Voltaje": f"{val:.2f}","Temperatura":f"{temp:.2f}", "Alerta":Alerta})
        kept += 1 #sume 1 kept, en nuestro caso cambia de fila
        
#KPIs
n=len(voltajes)
if n==0:
    #En caso no haya datos, seteamos los KPIs en 0 o None para evitar el error
    kips={"n": 0 , "min": None, "max": None, "prom": None,"Temperaturas":None, "alerts": 0, "alerts_pct": 0.0} 
    
else:
    alert=len(Alertas) #estructuras repetitivas simples
    kips={
        'n': n,
        'Vmin': float(f"{min(voltajes):.3f}"),
        "Vmax": float(f"{max(voltajes):.3f}"),
        "Vprom": float(f"{mean(voltajes):.3f}"),
        "Temperatura_prom": float(f"{mean(Temperaturas):.3f}"),
        "alerts": alert,
        "alerts_pct": 100.0 * alert / n,
    }

descartes_totales = bad_ts + bad_val            # equivale a (total - kept) con esta lógica
pct_descartadas = (descartes_totales / total * 100.0) if total else 0.0
kpis_calidad = {
    "filas_totales": total,
    "filas_validas": kept,
    "descartes_timestamp": bad_ts,
    "descartes_valor": bad_val,
    "%descartadas": round(pct_descartadas, 2),
}

#salida de pantalla y verificacion de KPIS
print(kips)
print(kpis_calidad)