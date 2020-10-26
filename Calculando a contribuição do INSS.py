s = float(input())

if (s <= 1751.81):
    a = s * 0.08
elif (s <= 2919.72):
    a = s * 0.09
elif (s <= 5839.45):
    a = s * 0.11
else:
    a = 5839.45 * 0.11
    
print(f"Desconto do INSS: R$ {a:.2f}")
