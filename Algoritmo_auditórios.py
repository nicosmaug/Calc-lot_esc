# Calculadora Lotação e Escoamento conforme COE e NBR 9077//ABNT

#Dimensionamento por área:

P = float(input("Entre com a lotação desejada: "))
A = float(input("Insira a area total de circulação do evento: "))
K = float(input("Digite 1 para saídas COM escadas e/ou rampas: "))
L = float(input("Insira a largura total das saídas existentes: "))

I = A/P

print("Setor para público em pé > 0,4 m2/pessoa")
print("Setor para público sentado > 1,00 m2/pessoa")
print("Atividades não específicas ou administrativas > 7,00 m2/pessoa")

print("O dimensionamento por área é: ", I)

#Capacidade da unidade de passagem:

if K == 1:
	C = 75
else:
	C = 100

#Condição de densidade máxima:

#Dimensionamento para saídas de emergência com lotação estipulada:
#Número de unidades de passagem, arredondado para número inteiro;

N1 = (P/C)

#N sempre deve ser um número inteiro:

N = round(N1)

#Largura mínima necessária para escoamento da população em metros:

L1 = (N * 0.55)

#Dimensionamento para lotação máxima pelas saídas de emergência existentes:

P1 = (round(L/0.55)) * C

print("As saídas de emergência devem ter no minímo: ",L1, " metros para a lotação estipulada.")
print("A lotação máxima pelas saídas de emergência existentes é: ", P1)
