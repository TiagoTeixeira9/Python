real = float(input("Quanto dinheiro tens na carteira? R$"))
dolar = real/ 3.27
print("Com R${:.2f} podes comprar US${:.2f}".format(real, dolar))