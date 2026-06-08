bandera = True

while bandera:

    print("calculadora")
    print("1 suma")
    print("2 resta")
    print("3 multiplicación")
    print("4 division")
    print("5 salir")

    opcion = input("elige una operacion: ")

    if opcion == "1":
        num1 = int(input("ingresa el primer numero: "))
        num2 = int(input("ingresa el segundo numero: "))
        resultado = num1 + num2
        print("resultado:", resultado)

    elif opcion == "2":
        num1 = int(input("ingresa el primer numero: "))
        num2 = int(input("ingresa el segundo numero: "))
        resultado = num1 - num2
        print("resultado:", resultado)

    elif opcion == "3":
        num1 = int(input("ingresa el primer numero: "))
        num2 = int(input("ingresa el segundo número: "))
        resultado = num1 * num2
        print("resultado:", resultado)

    elif opcion == "4":
        num1 = int(input("ingresa el primer número: "))
        num2 = int(input("ingresa el segundo número: "))
        
        if num2 == 0:
            print("no se puede dividir entre cero")
        else:
            resultado = num1 / num2
            print("resultado:", resultado)

    elif opcion == "5":
        print("programa terminado")
        bandera = False

    else:
        print("opcion incorrecta")