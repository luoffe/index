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
n = int (input())
if n >= 0 and n <=2:
 print(thislist[n])
elif n >= -3:
 print(thislist[n])


# %%
thislist = ["apple", "banana", "cherry"]
mylist = thislist
print(mylist)

thislist.insert(1, "watermelon")
print(mylist)


# %%
def max (x,y):
 if x > y:
  print (x)
 else:
  print (y)

max (8,5)

# %%
def my_function():
  print("Hello from a function")

my_function()
# %%
def max_de_3(x, y, z):
 if x > y and x > z:
  print("Número mayor es "+str(x))
 elif y > x and y > z:
  print("Número mayor es "+str(y))
 elif z > y and z > x:
  print("Número mayor es "+str(z))
 else: print ("Son iguales.")

x = input ()
print(x)
y = input ()
print(y)
z = input ()
print(z)

max_de_3(x, y, z)

# %%
listado_de_vocales = ("a", "e", "u", "i", "o")
def tipo_de_caracter(i):
 if i in listado_de_vocales:
  print("True")
 else: print("False")
i = input()
print (i)
tipo_de_caracter(i)
# %%
def sum (name_list):
 i=0
 for num in name_list:
  i+=num
 else:
  print(i)

list1 = list (range(1,4))
print(list1)
#sum (list1)

def multip(name_list):
 i=0
 while i<len(name_list):
  for num in name_list:
      if i == 0:
       num=a
       if i > 0:
         multiple=a*num
         multiple=a
  i+=1
  

    
#multip(list1)

def multip (lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion

multip (list1)
# %% funcion len
list1=[1, 2, 3]
def calcular_longitud (name):
 cont = 0
 for i in name:
   cont += 1
 return cont

calcular_longitud (list1)
# %%
def inversa(text):
  rtext=""
  i=j=-1
  while n<len(text):
   rtext=text[i:]
   if i == -1:
     i-=1
     rtext=rtext+text[i:j]
     if i < -1:
       i-=1
       j-=1
       rtext=rtext+text[i:j]
       print(rtext)
   
     
"""txt="hola "
print(txt[-1:])
rtxt=txt[-1:]
print(txt[-2:-1])
rtxt=rtxt+txt[-2:-1]
print(rtxt)"""

inversa("estoy bien")
# %%
def alreves (text):
  print(text[::-1])

alreves("hola")
# %%
def superposicion(list1,list2):
  for i in list1:
    for j in list2:
      if i == j:
       return True
  return False

l1 = [1, 7, 4]
l2 = [5, 2, 3]

superposicion(l1,l2)
# %%
def alreves (text):
  rtext = text[::-1]
  if rtext == text:
    return True
  else:
   return False

alreves ("hola")
# %%
""""Definir una función generar_n_caracteres() 
que tome un entero n
y devuelva el caracter multiplicado por n. 
Por ejemplo: generar_n_caracteres(5, "x")
debería devolver "xxxxx"."""

"""def generar_n_caracteres(x,n):
 i=0
 txt = ""
 while i<x:
   txt+=n
   i+=1
 else: print(txt)

generar_n_caracteres(3,"y")"""

def generar_n_caracteres(x,n):
  print(x * n)

generar_n_caracteres(7,"o")

# %%
def procedimiento(name_list):
  for j in name_list:
   print (j * "*")
    
  

l2 = [5, 2, 3]
procedimiento(l2)

# %%
def max_in_list(lista):
    inicio = 0
    for i in lista:
     if i > inicio:
        inicio = i
    return inicio

l2 = [5, 2, 3]
max_in_list(l2)
# %%
def mas_larga(listado):
  cont=0
  for i in listado:
  
    cont += 1
  return cont

l2 = ["Tom", "Oliver"]
mas_larga(l2)
# %%
l2 = ["Tom"]
str 
#%%
lista = ["Tom", "Oliver", "Ana", "Oliver2"]
def fun(lista):
  palabas_mas_larga = ""
  chars_anteriores = 0
  for palabra in lista:
    chars = len(palabra)
    if chars > chars_anteriores:
      palabas_mas_larga = palabra
  return palabas_mas_larga
res = fun(lista)
# %%
