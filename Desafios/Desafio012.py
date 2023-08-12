preço = float(input("Qual é o preço deste produto? $"))
novo = preço - (preço * 5 / 100)
print("O produto que custa {}$, na promoção com desconto de 5% vai custar ${}".format(preço, novo))
