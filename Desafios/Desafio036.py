casa = float(input("Qual é o valor da casa: US$ "))
salário = float(input("Qual é o seu salário: US$ "))
anos = int(input("Por quanto anos vai pagar: "))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print("Para pagar a casa de {:.2f} US$ em {} anos".format(casa, anos), end=" ")
print("A prestação será de {:.2f} US$".format(prestação))
if prestação <=mínimo:
    print("Emprestimo pode ser Concedido")
else:
    print("Empréstimo Negado")
