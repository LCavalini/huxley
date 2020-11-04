n = int(input())

c = 0

for x in range(1, n + 1):
    if x % 2:
        x *= -1
    c += 1/x
    
print(f"{c:.6f}")
