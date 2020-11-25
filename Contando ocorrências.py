def conta(sequencia, caractere):
    c = 0
    for i in sequencia:
        if i == caractere:
            c += 1
    return c
    
sequencia = input()
caractere = input()
quantidade = conta(sequencia, caractere)

if quantidade == 0:
    print("Caractere nao encontrado.")
else:
    print("O caractere buscado ocorre", quantidade, "vezes na sequencia.")

