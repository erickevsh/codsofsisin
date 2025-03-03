#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Zonas Horarias
# Definir 5 ciudades del mundo y checar su diferencia en la zona horaria
# Calcular la hora de las 5 ciudades a base de la hora especificada por el usuario
# Cabe considerar que la hora será representada en un sistema de 12 horas

# Diferencias horarias respecto a México
zonas_horarias = {
    "Dublín": 6,
    "Londres": 7,
    "Tokio": 15,
    "Los Ángeles": -2,
    "Nueva York": 2,
    "Nueva Delhi": 11.3
}

# Solicitar la hora en México
hora_mexico = float(input("Ingresa la hora en México (formato 12 horas): "))

# Calcular y mostrar la hora en otras ciudades
print("\nLa hora en las siguientes ciudades sería:\n")

for ciudad, diferencia in zonas_horarias.items():
    hora_ciudad = hora_mexico + diferencia
    if hora_ciudad > 12:
        hora_ciudad -= 12
        formato = "PM"
    else:
        formato = "AM"

    print(f"{ciudad}: {hora_ciudad:.1f} {formato}")


# In[ ]:





# In[ ]:




