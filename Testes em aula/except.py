try:
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite um número: "))
    resultado = numero1 / numero2
    print("Resultado: ", resultado)
except ValueError:
    print("Número invalido")
except ZeroDivisionError:
    print("Impossivel dividir por zero")