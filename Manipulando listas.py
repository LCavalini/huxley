orders = list()

while (True):
    
    cmd = input().split()
    
    if cmd[0] == "a" and cmd[1] not in orders:
        orders.append(cmd[1])
        
    if cmd[0] == "r":
        if cmd[1] in orders:
            orders.remove(cmd[1])
            print("removido")
        else:
            print("falha")
    
    if cmd[0] == "p":
        if len(orders) < 1:
            print("vazia")
        else:
            print(' '.join(orders))
    
    if cmd[0] == "s":
        break
