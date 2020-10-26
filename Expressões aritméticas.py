import math

a = float(input())
b = float(input())
c = float(input())
d = float(input())

print("i)", round((a**2+3*b)/c+d, 4))
print("ii)", round(math.log10(a)+math.e**(-b/c)-(d**2/math.pi), 4))
print("iii)", round((a**(2/3)*b**(1/3)+c*d)/(a+b+c+d), 4))
print("iv)", round(((a+b)*(c+d))/(a*b*c*d), 4))
print("v)", round((a**2+b**2)/(c*d)-(c**2+d**2)/(a*b), 4))
print("vi)", round((a+b+c+d)**2, 4))
print("vii)", round(a**2+b**2+c**2+d**2, 4))
print("viii)", round((a*b*c*d)**(1/3), 4))
