pedidos = []

while (True):

    comandos = input().split()

    if comandos[0] == "exibir":
        if len(pedidos) == 0:
            print("sem pedidos")
        else:
            print(' '.join(pedidos))
            
    if comandos[0] == "novo":
        pedidos.append(comandos[1])
        print("pedido", comandos[1], "adicionado")
        
    if comandos[0] == "cancela":
        if comandos[1] not in pedidos:
            print("pedido", comandos[1], "inexistente")
        else:
            pedidos.remove(comandos[1])
            print("pedido", comandos[1], "removido")

    if comandos[0] == "sair":
        break
    
    if comandos[0] == "ajuda":
        print("-----------------------------------")
        print("Pizzaria 0.1 - menu de comandos")
        print("-----------------------------------")
        print("- ajuda: exibe o menu de ajuda")
        print("- sair: encerra o programa")
        print("- exibir: exibe a lista de pedidos")
        print("- novo #pedido: adiciona o #pedido")
        print("- cancela #pedido: remove o #pedido")
        print("-----------------------------------")
        
