#Declarar
H : float = 0.0
V : float = 0.0
PD : float = 0.0
D : float = 0.0
#Início
H = float(input("Digite as horas trabalhadas:"))
V = float(input("Digite o valor de uma hora de trabalho:"))
PD = float(input("Digite o valor de desconto:"))
D = float(input("Digite o número de dependentes:"))
print("O salário a receber é:",(H * V + 100 * D) * (1 - PD / 100))
#Fim.