#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Función para evaluar la calificación
def evaluar_calificacion(porcentaje):
    if porcentaje > 90:
        return 'A'
    elif 80 < porcentaje <= 90:
        return 'B'
    elif 60 <= porcentaje <= 80:
        return 'C'
    else:
        return 'D'

# Solicitar la entrada del porcentaje
porcentaje = float(input("Introduce el porcentaje del alumno: "))

# Evaluar y mostrar el grado correspondiente
grado = evaluar_calificacion(porcentaje)
print(f"El grado del alumno es: {grado}")


# In[ ]:


# Función para calcular el impuesto basado en el precio
def calcular_impuesto(costo):
    if costo > 100000:
        return costo * 0.15
    elif 50000 < costo <= 100000:
        return costo * 0.10
    else:
        return costo * 0.05

# Solicitar el precio de la bicicleta
costo = float(input("Introduce el costo de la bicicleta: "))

# Calcular el impuesto
impuesto =


# In[ ]:


# Función para verificar si un año es bisiesto
def es_bisiesto(anio):
    # Un año es bisiesto si es divisible por 4, pero no por 100, 
    # o si es divisible por 400
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

# Solicitar el año al usuario
anio = int(input("Introduce el año: "))

# Verificar si es bisiesto
if es_bisiesto(anio):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")


# In[ ]:


# Función para obtener el nombre del día de la semana
def obtener_dia(numero):
    dias = {
        1: "Domingo",
        2: "Lunes",
        3: "


# In[ ]:


# Función para obtener el nombre del mes y los días que tiene
def obtener_mes_y_dias(numero):
    meses = {
        1: ("Enero", 31),
        2: ("Febrero", 28),  # Considerando un año no bisiesto, puedes modificar para años bisiestos
        3: ("Marzo", 31),
        4: ("Abril", 30),
        5: ("Mayo", 31),
        6: ("Junio", 30),
        7: ("Julio", 31),
        8: ("Agosto", 31),
        9: ("Septiembre", 30),
        10: ("Octubre", 31),
        11: ("Noviembre", 30),
        12: ("Diciembre", 31)
    }
    return meses.get(numero, "Número inválido, por favor ingresa un número entre 1 y 12.")

# Solicitar el número del mes al usuario
numero = int(input("Introduce un número del 1 al 12 para el mes: "))

# Obtener y mostrar el nombre del mes y los días que tiene
resultado = obtener_mes_y_dias(numero)

if isinstance(resultado, tuple):

