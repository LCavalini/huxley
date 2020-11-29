n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = map(int, input().split())

result = 1

for i in b:
    if i not in a:
        result = 0
        break
        
print(result)
