#Declarar
T : float = 0.0
V : float = 0.0
#Início
T = float(input("Digite a duração da viagem em horas:"))
V = float(input("Digite a velocidade média em km/h:"))
print("o valor de litros gasto foi:",T * V / 12)
#Fim.