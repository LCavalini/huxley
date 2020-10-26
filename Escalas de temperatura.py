t_fahrenheit = float(input())

t_celsius = (t_fahrenheit - 32) * 5/9
t_kelvin = t_celsius + 273.15

print(f"Convertendo {t_fahrenheit} graus Fahrenheit temos:\n{t_celsius} graus Celsius e {t_kelvin} Kelvin")
