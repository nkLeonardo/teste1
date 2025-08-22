entrada = input("Insira a distância percorrida em KM e depois o combustìvel gasto: (apenas números)").split()
#Split divide todas as palavras separadas em strings diferentes
X = int(entrada[0])
Y = float(entrada[1])
consumo_medio = X / Y
print(consumo_medio)
print(f"{consumo_medio:.3f} m por litro")