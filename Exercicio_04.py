numero = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
#f transforma em formated string
#(tudo dentro das chaves funciona como se não estivesse entre as aspas)
#O código se repete até chegar em 11. aumentando o número do contador(variavel I)
#em 1 toda vez, logo o multiplicador tambem aumenta.