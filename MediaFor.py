# Inicializa a variável 'soma' com o valor 0
soma = 0
for i in range(5):
  nota = float(input(f"Digite a {i}ª nota: "))
  soma += nota  
media = soma / 5
print(f"A média das notas é: {media}")
