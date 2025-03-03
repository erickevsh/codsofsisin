#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Programa que calcula el número factorial de un número ingresado por el usuario
num = int(input("Ingrese un número: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"El factorial de {num} es {factorial}")

# Programa que muestra la suma de los dígitos de un número ingresado por el usuario
num = int(input("Ingrese un número: "))
suma = sum(int(digito) for digito in str(num))
print(f"La suma de los dígitos de {num} es {suma}")

# Programa que escribe un patrón hasta un número definido por el usuario
num = int(input("Ingrese un número: "))
for i in range(1, num + 1):
    print("".join(str(x) for x in range(1, i + 1)))
for i in range(num, 0, -1):
    print("*" * i)

# Programa que acepta 10 números separados por comas y calcula su promedio
numeros = list(map(int, input("Ingrese 10 números separados por comas: ").split(",")))
promedio = sum(numeros) / len(numeros)
print(f"El promedio de los números ingresados es {promedio}")

# Programa que escribe todos los números primos entre dos números ingresados por el usuario
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
primos = [n for n in range(inicio, fin + 1) if es_primo(n)]
print(f"Los números primos entre {inicio} y {fin} son: {primos}")


# In[ ]:




