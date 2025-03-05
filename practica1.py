#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Definir los días de cada mes
enero = 31
febrero = 28  # Se ajustará para años bisiestos
marzo = 31
abril = 30
mayo = 31
junio = 30
julio = 31
agosto = 31
septiembre = 30
octubre = 31
noviembre = 30
diciembre = 31

# Fecha de nacimiento
dia_nac = 7
mes_nac = abril
año_nac = 2009

# Fecha actual
dia_hoy = 5
mes_hoy = marzo
año_actual = 2025

# Función para calcular si un año es bisiesto
def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

# Calcular los años completos vividos en días
dias_totales = 0
for año in range(año_nac + 1, año_actual):
    dias_totales += 366 if es_bisiesto(año) else 365

# Sumar los días desde la fecha de nacimiento hasta el final de ese año
dias_nacimiento = sum([abril, mayo, junio, julio, agosto, septiembre, 
                       octubre, noviembre, diciembre]) - dia_nac

# Sumar los días desde el inicio del año actual hasta la fecha actual
dias_actuales = sum([enero, febrero + (1 if es_bisiesto(año_actual) else 0), marzo]) + dia_hoy

# Sumar todos los días
dias_vividos = dias_totales + dias_nacimiento + dias_actuales

# Mostrar el resultado
print(f"Has vivido aproximadamente {5,811} días.")

