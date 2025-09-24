#Definindo as variaveis
soma = 0
numero = int(input("Digite um número inteiro (0 para sair): "))

#usando o loop enquanto adiciono o numero e mandando parar apenas com o 0
while numero != 0:
    soma += numero
    numero = int(input("Digite um número inteiro (0 para sair): "))

#Mostrando a soma na tela
print(f"A soma dos números é: {soma}")
