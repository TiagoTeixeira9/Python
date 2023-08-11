salario = float(input("Qual era o salário deste funcionário? $"))
novo = salario + (salario * 15 / 100)
print("O salário antigo deste funcionário era {}$, e agora o seu novo salário teve um aumento de 15% que corresponde a {}$".format(salario, novo))