nome = str(input("Qual é o seu nome? "))
if nome == "Tiago":
    print("Que nome bonito! ")
elif nome == "Pedro" or nome == "Maria" or nome == "João":
    print("Sue nome é bem popular em Portugal!")
else:
    print("Seu nome é bem normal.")
print("Tenha um bom dia, {}!".format(nome))
