# dato = input("ingrese dato:")

# lista = ["hola", "mundo", "chanchito", "feliz", "dragones"]

# if lista.count(dato) > 0:
#     print("el dato esta en la lista")
# else:
#     print("el dato no esta en la lista :(", dato)

primero = input("ingrese el primer dato: ")

try:
    primero = int(primero)
except:
    primero = "chanchito feliz"

if primero == "chanchito feliz":
    print("El valor ingresado no es un entero")
    exit()

segundo = input("ingrese el segundo dato: ")

try:
    segundo = int(segundo)
except:
    segundo = "chanchito feliz"

if segundo == "chanchito feliz":
    print("El valor ingresado no es un entero")
    exit()

simbolo = input("ingrese el operación: ")
if simbolo == "+":
    print(primero + segundo)
elif simbolo == "-":
    print(primero - segundo)
elif simbolo == "*":
    print(primero * segundo)
elif simbolo == "/":
    print(primero / segundo)
else:
    print("El símbolo ingresado no es válido")
