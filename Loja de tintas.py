import math

a = float(input())

l = a / 7

ltg = math.ceil(l / 24)
p = ltg * 91

print(f"a) {ltg} lata(s) de 24 litros: R$ {p:.2f}")

ltp = math.ceil(l / 5.4)
p = ltp * 23

print(f"b) {ltp} lata(s) de 5.4 litros: R$ {p:.2f}")

ltg = math.floor(l / 24)
ltp = math.ceil((l % 24) / 5.4)
p = ltg * 91 + ltp * 23

print(f"c) {ltg} lata(s) de 24 litros e {ltp} lata(s) de 5.4 litros: R$ {p:.2f}")
