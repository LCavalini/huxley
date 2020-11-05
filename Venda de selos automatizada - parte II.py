custos = []

while True:
    try:
        custos.append(round(float(input())*100))
        
    except:
        break
        
for custo in custos:
    
    if custo >= 70 and custo <= 620 and not custo % 10:
        
        s50 = int(custo / 50)
        s20 = (custo - s50 * 50) / 20
    
        if s20 % 1:
            s50 -= 1
            s20 += 3
            
        print(f"Compre {s50} selo(s) de R$ 0.50 e {int(s20)} selo(s) de R$ 0.20!")
        break
    
    print("Preco invalido, refaca a leitura do pacote.")
