idade = int(input())

if idade < 16:
    msg = 'nao eleitor'
elif idade >= 18 and idade <= 65:
    msg = 'eleitor obrigatorio'
else:
    msg = 'eleitor facultativo'

print(msg)
