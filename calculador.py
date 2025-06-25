# Operadores soma(+), subtração(-), Divisão(/) e multiplicação(*)

def calculadora(numero1, numero2, operacao):
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "/":
        try:
            return numero1 / numero2
        except ZeroDivisionError:
            return "Erro, não é possivel realizar divisão por ZERO!"
    else:
        return "Operação inválida!"

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação ( + , - , * , / ): ")

    resultado = calculadora(numero1, numero2, operacao)
    print("Resultado: ", resultado)
except ValueError:
    print("Erro: digite um número válido.")