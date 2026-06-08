import re

regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

correo = input("Ingresa tu correo electrónico: ")

if re.match(regex, correo):
    print("Correo válido")
else:
    print(" Correo inválido")