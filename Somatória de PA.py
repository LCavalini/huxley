r = int(input())
n = int(input())

c = 0

for x in range(1, n + 1, r):
    c += x
    
print("A somatoria da PA eh:", c)
