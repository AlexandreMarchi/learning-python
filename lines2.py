a = int(input("Escreva o número de linhas: "))
b = a - (a-1)

while a >= b:
    print("Linha %d" % a)
    a -= 1