#Escribe un programa que diga hola mundo
print("Hola mundo")
#Solicitud y mostrar nombre al usuario
print("ingresa tu nombre por favor")
nombre = str(input("ingrese su nombre: "))
print(f"Hola, {nombre}")
#Suma de 2 numeros
print("ingrese 2 numeros a sumar")
num1 = int(input("ingrese numero: "))
num2 = int(input("ingrese numero: "))
suma = num1 + num2 
print(f"El total sumado fue {suma}")
#Promedio de 3 numeros
print("ingrese los 3 numeros")
a = int(input("ingrese el numero: "))
b = int(input("ingrese el numero: "))
c = int(input("ingrese el numero: "))
total = a + b + c 
promedio = total/3
print(f"El promedio fue {promedio}")
#Verificacion numero par o impar
print("Ingresa un numero")
numero = int(input("ingrese el numero: "))
if numero %2 == 0:
    print("es par")
else:
    print("es impar")
#Comparacion de numeros
print("Vamos a comparar 2 numeros")
nume1 = int(input("Ingresa el numero a comparar: "))
nume2 = int(input("Ingresa el numero a comparar: "))
if nume1 > nume2:
    print(f"el numero {nume1} es mayor")
elif nume2 > nume1:
    print("el numero mayor es el 2")
else:
    print("ambos numeros son iguales")
#Validacion de edad
print("Hola usuario, ingrese su edad para determinar algunos datos")
edad = int(input("Ingrese su edad: "))
if edad >= 0:
    print("edad invalida")
elif edad >= 18:
    print("usted es mayor de edad")
else:
    print("Usted es menor de edad")
#Conversion Celsius a Farenheit
print("Ingrese la temperatura en Celsium")
temp =float(input("Ingrese la temperatura"))
Conver = temp *9/5 +32
print(f"Su conversion dio {Conver}")
#Calcular area
print("Ingrese las medidas de la figura")
A = int(input("ingrese la medida"))
B = int(input("ingrese la medida"))
area = A * B
print(f"El area de la figura es: {area}")
#Validar numeros positivos y negativos
print("ingrese el numero")
valid = int(input("Ingrese el numero a validar"))
if valid == 0:
    print("su numero es 0")
elif valid < 0:
    print(f"su numero que es {valid}  es negativo")
else:
    print(f"su numero que es {valid} es positivo")
# contar las letras de una palabra
palabra = input("Ingrese una palabra: ")
for letra in palabra:
    print(letra)
#Palabra primera y ultima letra
print("Ingresa una palabra")
word = str(input("ingrese una palabra"))
primera = word[0]
ultima = word[-1]
print(f"La primera letra es: {primera} ")
print(f"La ultima letra es: {ultima}")
#Validar contraseña.
print("ingrese  una contraseña")
validpas="pyton123"
pas = str(input("la contraseña es:"))
if pas == validpas:
    print("contraseña correcta")
else:
    print("no es valida")
#Año biciesto
print("ingrese un año")
año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año", año, "es bisiesto.")
else:
    print("El año", año, "no es bisiesto.")
#Usa un ciclo for para sumar los números del 1 al 10
print("Suma de números del 1 al 10")

suma = 0

for i in range(1, 11):
    suma += i

print("La suma es:", suma)
# Contador de vocales
texto = input("Ingrese una palabra o frase: ")

vocales = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1

print("La cantidad de vocales es:", contador)
#Tabla de multiplicar
print("Ingrese un número para mostrar su tabla")
nu = int(input("Ingresa el número: "))

print("Tabla del", nu)

for i in range(1, 11):
    print(nu, "x", i, "=", nu * i)
#Validacion de numero en rango de 0 a 100
numerito = int(input("Ingrese su numero a validar: "))
if numerito <0:
    print("Su numero no es valido")
elif numerito <= 100:
    print("Su numero esta en rango de 0 a 100")
else:
    print("Su numero es mayor que 100")
#Repetidor de palabras 
print("Ingrese la palabra y la cantidad de veces a repetir")
p_r = str(input("Ingresa la palabra"))
n_r = int(input("Ingrese el numero de repeticion"))

for i in range(n_r):
    print(p_r)
#Suma hasta que se ingrese 0
print("Ingrese la cantidad de sumas que elijas")
t_s = 0
while True:
    sumas = int(input("Ingrese sus sumas 0 para orden de parar"))
    if sumas == 0:
        break
t_s += sumas
print(f"la suma total es: {t_s}")