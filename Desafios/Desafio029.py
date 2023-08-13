velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade > 80:
    print("\033[31mMULTADO! Você excedeu o limite permitido que é 80KM/h\033[m")
    multa = (velocidade-80) * 1
    print("\033[31mTens que pagar uma multa de {:.2f}US$\033[m".format(multa))
    print("\033[31mTenha um bom dia! Dirija com mais segurança!\033[m")
else:
    print("\033[32mTenha um bom dia! Dirija com segurança!\033[m")
