# Calculadora Segurança Norma IT-12

#Dimensionamento por área:

P = float(input("Entre com a lotação desejada: "))
A = float(input("Insira a area total de circulação do evento: "))
L = float(input("Insira a largura total das saídas existentes: "))

D = P/A

print("A densidade de público é igual a: ", D)

#Condição de densidade máxima:

#Capacidade de escoamento:

T = 5

F_h = 83
F_v = 66

E_h = F_h * T
E_v = F_v * T

#Largura mínima necessária para o escoamento da população estimada:

L_h = P/E_h
L_v = P/E_v

#Dimensionamento para lotação máxima pelas saídas de emergência existentes:

P1 = L*E_h
P2 = L*E_v

#Entregar as informações:
print("As saídas de emergência sem escadas devem ter no minímo: ", L_h, " metros para a lotação estipulada.")
print("As saídas de emergência com escadas devem ter no minímo: ", L_v, " metros para a lotação estipulada.")
print("A lotação máxima pelas saídas de emergência existentes é: ", P1, " para saídas sem escadas e ", P2, " para saídas com escadas.")