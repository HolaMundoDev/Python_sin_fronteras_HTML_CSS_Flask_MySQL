# Aca va un comentario
if 5 < 3:
  print("5 es mayor a 3")

# if 5 > 3: # Aca va otro comentario
#   print("5 es mayor a 3")

x = 5
y = "chanchito feliz"

# print(x, y)

correo = "chanchito@feliz.com"

# print(correo)

_mi_var = "canchito"
MIVAR = "canchito"

a,b,c = "Lala", "Lele", "Lili"
# print(a,b,c)

valor1 = valor2 = valor3 = "Chanchito Feliz"
# print(valor1, valor2, valor3)

inicio = "Hola"
final = "Mundo"

# print(inicio + final)

palabra = 'hola mundo' # string
oracion = "hola mundo comilla doble" # string 

entero = 20 # integer
conDecimales = 20.2 # float
complejo = 1j # numeros complejos se les agrega una j

# print(palabra, oracion, entero, conDecimales, complejo)

lista = ["Hola","Mundo", "Chanchito feliz"]
lista2 = lista.copy()
lista.append("Chanchito Triste")
# lista.clear()

# print(lista, lista2.count(1))
# print(len(lista), len(lista2))

largoLista = len(lista)
largoLista2 = len(lista2)

# print(largoLista, largoLista2)

# print(lista[2])

# lista.pop() # Elimina el ultimo elemento de la lista

# lista.remove("Hola") # Elimina el elemento que se le pase como parametro

lista.reverse() # Invierte la lista
lista.sort() # Ordena la lista
# print(lista)

tupla = ("hola", "mundo", "somos", "tupla")

print(tupla.count("hola"))
print(tupla.index("mundo"))
print(tupla[0])
listaDeTupla = list(tupla)
# print(listaDeTupla)

rango = range(6)
# print(rango)

diccionario = {
  "nombre": "Chanchito Feliz",
  "raza": "Persa",
  "edad": 5
}

# print(diccionario)
# print(diccionario["nombre"])
# print(diccionario["raza"])
# print(diccionario.get("nombre"))

diccionario["nombre"] = "Fluffy"
# print(len(diccionario))

diccionario["ronronea"] = "Si"
print(diccionario)
# diccionario.pop("ronronea")
# diccionario.popitem()

copiaGatito = diccionario.copy()
otraCopiaGatito = dict(diccionario)
# del diccionario["ronronea"]
diccionario.clear()
print(diccionario, copiaGatito, otraCopiaGatito)