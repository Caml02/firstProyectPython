print ("Hello world!")

# Comentarios de una sola linea
"""Primer Ejercicio (Otra manera de comentar
de lineas multiples)"""

# Primer ejemplo
"""
print ("ingrese el primer numero")
numero1 = input()
print ("ingrese el segundo numero")
numero2 = input()
if (numero1 > numero2):
 print ("El primer numero es mayor")
if (numero1 == numero2):
 print ("Son iguales")
else:
 print ("El segundo numero es mayor")  """


# Segundo ejemplo


"""a = int(input("numero 1: "))
b = int(input("numero 2: "))
operador = input("operacion: ")
if operador == 'suma':
 print (a + b)
elif operador == 'resta':
 print (a - b)
elif operador == 'multiplica':
 print (a * b)
elif operador == 'divide':
 print (a / b)
else:
 print ("Operacion no valida")"""

# Tercer Ejemplo

"""veces = int(input("numero de veces: "))
caracter = input("caracter: ")
for i in range(0, veces):
 print(caracter, end = '')"""

# Cuarto Ejemplo

"""x = 1
while x != 0:
    x = int(input("Ingrese un numero (0 para finalizar): "))
    for i in range(0, 11):
        r = i * x
    print(str(x) + " x " + str(i) + " = " + str(r))"""


#Quinto ejercicio

password_1 = 1616
for i in range (1, 4):
    pass_key = int(input('Enter password /Ingresa contraseña: '))
    if(pass_key is password_1 and i <=3):
        break
    print("Correct Password / Contraseña correcta!")
    if(pass_key is not password_1 and i>3):
        print  ("ERROR! / CONTRASEÑA INCORRECTA!")
