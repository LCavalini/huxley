n1 = float(input())
n2 = float(input())
n3 = float(input())
f = float(input())

f = int(f * 100)
m = round((n1*2 + n2*2 + n3*3) / 7, 1)

print(f"Frequencia: {f}%")
print(f"Media: {m}")

if (f < 75):
    print(f"Aluno reprovado por faltas!")
else:
    if (m > 9):
        print(f"Aluno aprovado com louvor!")
    elif (m >= 6):
        print(f"Aluno aprovado!")
    elif (m >= 4):
        print(f"Aluno de recupera��o!")
    else:
        print(f"Aluno reprovado!")
