import datetime as dt   #importar funciones - modulo fecha 
import random as rd     #importar funciones - modulo aleatorio
fecha = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #variable
nombre = "Alejandro Huertos"    #constantes
print("Buenas tardes, Ing " + nombre)
print("Siendo la fecha: "+fecha)
print("Se presentan los siguientes valores medidos:")
#valores aleatorios
for i in range(10): #bucle
    v = rd.randint(0,1023)
    if v < 100: #condicional 
        print("Valor bajo: " + str(v))
    elif 100 <= v and v <= 500: #Condicional logica
        print("Valor medio: " + str(v))
    else: #Para toda las demas situaciones >500
        print("Valor alto: " + str(v))

print("Saludos Cordiales.")