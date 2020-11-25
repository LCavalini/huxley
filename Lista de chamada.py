entrada = input().split()
n = int(entrada[0])
k = int(entrada[1])

nomes = list()

for i in range(n):
    nomes.append(input())
    
nomes.sort()

print(nomes[k-1])
    
