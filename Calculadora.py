num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")
#Define a operação baseado no simbolo selecionado

if operacao == '+':
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == '/':
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")
