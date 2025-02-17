# Dale Like <3
# Sigueme Para mas \(o_o)/

def calculadora():
    print("Elige una operación: +, -, *, /")
    operacion = input("Operación: ")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if operacion == '+':
        print(f"Resultado: {num1 + num2}")
    elif operacion == '-':
        print(f"Resultado: {num1 - num2}")
    elif operacion == '*':
        print(f"Resultado: {num1 * num2}")
    elif operacion == '/':
        print(f"Resultado: {num1 / num2}")
    else:
        print("Operación no válida")


