n = int(input("Diz-me um número qualquer: "))
resultado = n % 2
if resultado == 0:
    print("O número {} é PAR!".format(n))
else:
    print("O número {} é IMPAR!".format(n))
