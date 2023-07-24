# dato = input("ingrese dato:")

# lista = ["hola", "mundo", "chanchito", "feliz", "dragones"]

# if lista.count(dato) > 0:
#     print("el dato esta en la lista")
# else:
#     print("el dato no esta en la lista :(", dato)

primero = input("ingrese primer número: ")

try:
    primero = int(primero)
except:
    primero = "chanchito feliz"

segundo = input("ingrese el segundo dato: ")

try:
    segundo = int(segundo)
except:
    segundo = "chanchito feliz"

if primero == "chanchito feliz" or segundo == "chanchito feliz":
    print("Ingresaste mal un dato, prueba de nuevo solo con números")
else:
    print(primero + segundo)
