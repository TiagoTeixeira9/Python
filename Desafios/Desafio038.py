n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
if n1 > n2:
    print("\033[32mO primeiro valor é maior \033[m")
elif n2 > n1:
    print("\033[31m O segundo número é maior \033[m")
else:
    print("\033[33m Os dois valores são iguais \033[m")
