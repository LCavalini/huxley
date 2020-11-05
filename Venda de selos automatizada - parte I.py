entrada = []
peso = 0
comprimento = None
largura = None
profundidade = None

while True:
    try:
        entrada.append(float(input()))
    except:
        break

for dado in entrada:

    if peso == 0:
        
				if dado <= 0:
					print("Peso invalido!")
					continue
        
				peso = dado
        print("Peso valido!")
        
    elif comprimento == None:
        comprimento = dado
        
    elif largura == None:
        largura = dado
        
    elif profundidade == None:

        if comprimento <= 0 or largura <= 0 or dado <= 0:
            print("Dimensoes invalidas!")
            comprimento = None
            largura = None
            continue

        profundidade = dado

        print("Dimensoes validas!")

        somaDimensoes = sum([comprimento, largura, profundidade])
        maxDimensao = max([comprimento, largura, profundidade])

        if peso <= 500 and maxDimensao <= 28 and somaDimensoes <= 52:
            custoPeso = lambda x : 0.5 if x <= 100 else 0.5 + (x - 100)//10/10
            custoDimensoes = lambda x : 0.2 if x <= 22 else 0.2 + (x - 22)//2/10
            custoTotal = custoPeso(peso) + custoDimensoes(somaDimensoes)
            print(f"Custo total do envio: R$ {custoTotal:.2f}")
        
				else:
            print("Este pacote nao atende os limites para envio no caixa de autoatendimento, dirija-se ao balcao de atendimento para posta-lo!")
