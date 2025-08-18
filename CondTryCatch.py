valor_txt = input("Ingrese los valores de Temperatura en C: ")
try:
    t = float(valor_txt)
    if t>= 30: #condicion if "Condicion 1"
        print("Alerta! Alta temperatura")
    elif t < 0: #Condicion 2
        print("temperatura bajo 0")
    else:
        print("Temperatura normal")
except ValueError:
    print("Entrada invalida. Use números(ej. 26.5).")
