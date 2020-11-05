entregas = []

for i in range(7):
    entregas.append(int(input()))
    
media = int(sum(entregas) / 7)
cumprimento = len([i for i in entregas if i >= 100])

print(f"{cumprimento}\n{media}")
