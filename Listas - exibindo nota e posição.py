n = int(input())
notas = list()
soma = 0

if n > 0 and n <= 5:

    for i in range(n):
        notas.append(float(input()))
        
    for i in range(n):
        print(f"Nota {i+1}: {notas[i]:.1f}")
        soma += notas[i]
        
    print(f"Media: {soma / n:.2f}")
    
else:
    print("Numero de notas invalido.")
