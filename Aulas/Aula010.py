n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 +n2) /2
print("A sua média foi {:.1f}".format(m))
if m >= 6.0:
    print("A sua média foi boa! Parabéns!")
else:
    print("A sua média foi má estude mais!")