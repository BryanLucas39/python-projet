n1 = input ("Digite a primeira nota do aluno\n")
n2 = input ("Digite a segunda a nota do aluno\n")
n3 = input ("Digite a terceira nota do aluno\n")
n4 = input ("Digite a quarta nota do aluno\n")

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

média = n1 + n2 + n3 + n4 / 4

if média >= 6:
    print("Aprovado")
elif média <= 4:
    print("Reprovado")

else: 
    print("Recuperação")