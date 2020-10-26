lengthTable[1] = 1
size = 1000000
lengthTable = [0] * size

def cycleLength(n):
    
    if n < size and lengthTable[n]:
        return lengthTable[n]
        
    if n & 1:
        if n < size:
            lengthTable[n] = 2 + cycleLength((3 * n + 1) >> 1)
            return lengthTable[n]
        else:
            return 2 + cycleLength((3 * n + 1) >> 1)
        
    else:
        if n < size:
            lengthTable[n] = 1 + cycleLength(n >> 1)
            return lengthTable[n]
        else:
            return 1 + cycleLength(n >> 1)

while (True):

    # mapeia a entrada em dois numeros, considerando o espaco como separador
    try:
        i, j = map(int, input().split())
    
    except:
        break
        
    if j < i:
        l = j
        m = i
        
    else:
        l = i
        m = j
        
    if l <= 0 or m >= size:
        break
        
    maxLength = 1
    
    for n in range(l, m+1):
    
        length = cycleLength(n)
            
        if length > maxLength:
            maxLength = length
            
    print(i, j, maxLength)
