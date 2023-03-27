#%%
x = 5
print(type(x))
# %%
x = 6
y = "John"
print(x)
print(y)

# %%
# text
x = 6
y = "John"
print(x)
print(y)
# %% Números de Python
#complex

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
# %% Conversión de tipo
#complex, float, int
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(x)
print(y)
print(z)

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
# %% Número aleatorio
import random

print(random.randrange(1, 10))
# %% Filas
#multilineia
a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# %%
#una fila

a="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
print(a)

b="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(b)

# %% Cortar la cadena en interval
#[x:y] y - no incluido; empieza con índice 0
b = "Hello, World!"
print(b[2:5])

# Cortar la cadena del inicio hasta índice n
b = "Hello, World!"
print(b[:7])

# Cortar la cadena del índice n hasta final
b = "Hello, World!"
print(b[2:])

# Indexación negativa
#iniciar el segmento desde el final de la cadena
##[x:y] x - no incluido; empieza con índice 0
b = "Hello, World!"
print(b[-8:-1])
# %% Mayúsculas ()
a = "Hello, World!"
print(a.upper())
# Minúscula ()
a = "Hello, World!"
print(a.lower())
# %% Eliminar espacios en blanco
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# %% Reemplazar cadena
a = "Hello, World!"
print(a.replace("H", "J"))
# %% ??
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
# %% Conectar las cadenas
#metodo 1
a = "Hello"
b = "World"
c = a + " " + b
print(c)
# metodo 2
print(a+b)
#metodo 3
print(a + " " + b)
#metodo 4
a = "Hello"
b = "World"
c = a + b
print(c)
# %% Formato de cadena
"""age = 36
txt = "My name is John, I am " + age
print(txt)"""
#sale error

# <arg>.format(arg1,arg2...) 
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# %% ejemplo
txt = "Estamos en {}."
mes = "marzo"
print(txt.format(mes))
# %% ??? Caracteres de escape/Metodos de cadena
txt = "We are the so-called \"Vikings\" from the north."
# %%Casos cuando boolean vuelve false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
# %% Vuelve false, cuando el metodo incorrecto
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# %% determinar si un objeto es de cierto tipo de datos
x = 200
print(isinstance(x, int))
# %%
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# %%
