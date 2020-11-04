n = int(input())

c = 0

for i in range(1, n + 1):
    c += 1/(i**2)
    
print("{:.6f}".format(c))
