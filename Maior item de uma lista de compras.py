item = [0, 0, 0.0]

while (True):
    novoItem = input().split()
    novoItem = [int(novoItem[0]), int(novoItem[1]),
float(novoItem[2])*int(novoItem[1])]
    if novoItem[0] == 0:
        break
    if novoItem[2] > item[2]:
        item = novoItem

if item[0] > 0:    
    print("Item mais caro")
    print("Codigo:", item[0])
    print("Quantidade:", item[1])
    print(f"Custo: {item[2]:.2f}")
else:
    print("nao tem compras")
