# Laboratorio 1: Procesamiento de Datos de Sensores en Python

Este proyecto es parte del Laboratorio 1 del curso de Programación de Computadoras con Python, enfocado en el aprendizaje de telemetría y el manejo de datos de sensores. Aquí aprenderás a limpiar, transformar y analizar datos de voltaje, generando alertas y métricas clave para evaluar la calidad y el comportamiento de los datos.

---

## ¿Qué vas a lograr con este laboratorio?

- **Limpiar datos** de archivos CSV, normalizando formatos y descartando valores inválidos.
- **Convertir lecturas de voltaje** en temperaturas usando una fórmula sencilla.
- **Generar alertas** cuando la temperatura supera un umbral.
- **Documentar resultados** en un archivo CSV procesado y mostrar KPIs en pantalla.

---

## ¿Cómo está organizado el proyecto?

```
PROYECTO_LAB1/
│
├── data/
│   ├── raw/
│   │   └── datos_sucios_250.csv         # Archivo de entrada con datos crudos
│   └── processed/
│       └── datos_sucios_250_limpio1.csv # Archivo de salida con datos limpios
│
└── src/
    └── Lab1.py                          # Script principal de procesamiento
```

---

## ¿Cómo funciona el código principal (`Lab1.py`)?

1. **Lectura de datos:**  
   El script abre el archivo CSV de entrada y lee los datos crudos de sensores.

2. **Limpieza de datos:**  
   - Cambia comas por puntos en los decimales.
   - Descarta valores vacíos, "NA", "error", etc.
   - Convierte los valores de voltaje a números flotantes.
   - Limpia y estandariza los formatos de fecha y hora (timestamp).

3. **Conversión de voltaje a temperatura:**  
   Se usa la fórmula:  
   `Temperatura (°C) = 18 * Voltaje - 64`

4. **Generación de alertas:**  
   Si la temperatura es mayor o igual a 25°C, se genera una alerta ("CUIDADO"), si no, se marca como "OK".

5. **Escritura de datos procesados:**  
   Los datos limpios y procesados se guardan en un nuevo archivo CSV con las columnas:  
   `Tiempo, Voltaje, Temperatura, Alerta`

6. **Cálculo de KPIs:**  
   Al final, el script muestra en pantalla:
   - Número total de filas procesadas
   - Filas válidas
   - Filas descartadas por timestamp y por valor
   - Voltaje mínimo, máximo y promedio
   - Temperatura promedio
   - Número y porcentaje de alertas

---

## ¿Cómo lo uso?

1. Coloca tu archivo de datos crudos en `data/raw/datos_sucios_250.csv`.
2. Ejecuta el script principal desde la carpeta `src`:
   ```bash
   python Lab1.py
   ```
3. Revisa el archivo procesado en `data/processed/datos_sucios_250_limpio1.csv` y los KPIs que aparecen en la pantalla.

---

## ¿Por qué es útil este laboratorio?

Este laboratorio te ayuda a entender cómo trabajar con datos reales de sensores, algo fundamental en telemetría y monitoreo. Aprenderás a limpiar datos, convertir unidades, generar alertas automáticas y calcular métricas de calidad, habilidades esenciales para cualquier ingeniero o científico de datos.

---

## Autor

Curso de Programación de Computadoras - Python  
Universidad / Profesor: [Completa según corresponda]

---

¿Tienes dudas sobre el código o quieres adaptarlo para otros sensores? ¡Explora, experimenta y aprende!