Peso= float (input("Qual seu peso?(apenas dois números decimais)"))
Altura= float (input("Qual sua altura? (em metros, e apenas dois numeros decimais)"))
Altura2= float (Altura*Altura)
IMC= float (Peso/Altura2)

if IMC < 18.5:
 print("Abaixo do peso:",IMC)
elif IMC <= 25:
 print("Peso normal:",IMC)
elif IMC <= 30:
 print("Sobrepeso:",IMC)
else:
 print("Obesidade:",IMC)
 #trate elif como if, e encerre com else
 #If, else e elif fazem parte de estruturas de decisão, se o valor é verdadeiro, if é executado, 
 # valor não é igual ao if, porém ainda é verdadeiro=elif executado
 #valor é falso=else executado

 #Multiplicação funciona como na matemática, representado pelo "*" multiplicando o 1° (ou mais) pelo 2°
