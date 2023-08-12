velocidade = float(input("Qual é a velocidade atual do carro? "))
m = 1*10
if velocidade <= 80:
    print("MULTADO! Você excedeu o limite permitido que é 80KM/h")
    multa = (velocidade-80) * 7
    print("Tens que pagar uma multa de {}US$".format(m))
    print("Tenha um bom dia! Dirija com mais segurança !")

print("Tenha um bom dia! Dirija com segurança !")
