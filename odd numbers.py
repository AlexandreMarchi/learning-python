a = int(input("Digite o número de impares que deseja imprimir: "))

i = 1
count = 0

while count < a:
    if i % 2 != 0:
        print(i, end=' ')
        count += 1
    i += 1