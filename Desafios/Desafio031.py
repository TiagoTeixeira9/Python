distância = float(input("Qual é a distância da sua viagem? "))
print("Estás prestes a começar uma viagem de {}KM.".format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print("E o preço da sua viagem vai ser de {:.2f}US$".format(preço))
