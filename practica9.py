#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for i in range(1, 11):
    print(i)


# In[ ]:


for i in range(1, 20, 2):
    print(i)


# In[ ]:


for i in range(10, 0, -1):
    print(i)
    


# In[ ]:


num = int(input("2: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    


# In[ ]:


num = int(input("2: "))
producto = 1
for digito in str(num):
    producto *= int(digito)
print(f"El producto de los dígitos de {num} es {producto}")

