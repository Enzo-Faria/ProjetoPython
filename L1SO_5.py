#Declarar
A : float
B : float
C : float
#Início
A = float(input("Digite o valor de A:"))
B = float(input("Digite o valor de B:"))
C = float(input("Digite o valor de C:"))
D = B ** 2 -4 * A * C
X1 = (-B + D ** 0.5) / 2 * A
X2 = (-B - D ** 0.5) / 2 * A
print("O valor da primeira raiz é:",X1 ,"O valor da segunda raiz é:",X2)
#Fim.