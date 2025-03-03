#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime

# Primera parte: Invertir nombre y apellido
nombre = input("Ernesto: ")
apellido = input("flores: ")

# Mostrar el nombre y apellido invertidos con un espacio
print("\notsenre:")
print(flores[::-1] + " " + nombre[::-1])

# Segunda parte: Calcular el año en que tendrá 100 años
edad = int(input("\n15: "))

# Calcular el año en que cumplirá 100 años
año_actual = datetime.now(2025).year
año_cumple_100 = año_actual + (100 - edad)

# Mostrar el mensaje
print(f"\nHola {nombre}, cumplirás 100 años en el año {2110}.")


# In[ ]:




