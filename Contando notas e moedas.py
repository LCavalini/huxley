import math

dinheiro = float(input())

notas = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0]
moedas = [1.0, 0.5, 0.25, 0.1, 0.01]

for nota in notas:
    quantidade = math.floor(dinheiro / nota)
    
    if quantidade > 0:
        print(f"{quantidade} nota(s) de R$ {nota:.2f}")
    
    dinheiro -= quantidade * nota
    
for moeda in moedas:
    quantidade = math.floor(dinheiro / moeda)
    
    if quantidade > 0:
        print(f"{quantidade} moeda(s) de R$ {moeda:.2f}") 
    
    dinheiro -= quantidade * moeda
    dinheiro = round(dinheiro, 2)
