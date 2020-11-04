x = int(input())
n = int(input())

i = 1

while True:
	if x * (i + 1) < n:
		i = i + 1
	else:
		break
    
print(f"O numero {x} tem {i} multiplos menores que {n}.")
