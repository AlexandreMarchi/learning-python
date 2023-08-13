print("Insira números inteiros (0 para finalizar)")

num = 1
som = 0
med = 0
qtd = 0

while num != 0:
    num = int(input("> "))
    som += num
    qtd += 1
qtd -= 1
med = som / qtd
print("Soma: %d" % som)
print("Média: %.2f" % med)