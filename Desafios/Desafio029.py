velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido que é 80KM/h")
    multa = (velocidade-80) * 1
    print("Tens que pagar uma multa de {:.2f}US$".format(multa))
    print("Tenha um bom dia! Dirija com mais segurança!")
else:
    print("Tenha um bom dia! Dirija com segurança!")
