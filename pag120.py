idade = int (input("Digite sua idade: "))

if idade < 4:
    print("Entrada gratuita")

elif idade >= 4 and idade < 18:
    print("Ingresso R$ 5,00 reais")

elif idade >= 18 and idade > 60:
    print("Ingresso R$ 10,00 reais")

else:
    print("Ingresso R$ 5,00 reais")